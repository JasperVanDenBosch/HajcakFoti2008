"""Run the experiment

"""
from dataclasses import asdict
from os.path import expanduser, join
from datetime import datetime
from os import makedirs
from math import isclose
from statistics import mean
import platform
from random import randint
from pandas import DataFrame
from experiment.constants import Constants
from experiment.fate import Fate
from experiment.trials import generate_trials
#from experiment.fake_engine import FakeEngine
from experiment.engine import PsychopyEngine
from experiment.labs import getLabConfiguration
from experiment.triggers import Triggers
const = Constants()  # load fixed parameters wrt timing, sizing etc


## this object represents drawing and interactions via psychopy
#engine = FakeEngine()
triggers = Triggers()
engine = PsychopyEngine(const, triggers)

## user input
config = getLabConfiguration()
SITE = config['site']['abbreviation']
pidx = randint(99, 99999) ## no easy way to get input on some windows setups so hardcoding for now
sub = f'{SITE}{pidx:05}' # the subject ID is a combination of lab ID + subject index

## data directory and file paths
data_dir = expanduser(config['site']['directory'])
makedirs(data_dir, exist_ok=True) # ensure data directory exists
# current date+time to seconds, helps to generate unique files, prevent overwriting
dt_str = datetime.now().strftime(f'%Y%m%d%H%M%S')
# full file path to trials (structured) and log (unstructured) output 
trials_fpath = join(data_dir, f'sub-{sub}_run-{dt_str}_trials.csv')
log_fpath = join(data_dir, f'sub-{sub}_run-{dt_str}_log.txt')

## set log levels and log file location
engine.configureLog(log_fpath)

## setup psychopy monitor and window objects
engine.configureWindow(config)

## record some basic info
engine.logDictionary('SESSION', dict(
    participant_index=pidx,
    date_str=dt_str))
engine.logDictionary('PLATFORM', platform.uname()._asdict())
engine.logDictionary('SITE_CONFIG', config)
performance = engine.measureHardwarePerformance()
engine.logDictionary('PERFORMANCE', performance)
fr_conf = config['monitor']['refresh_rate']
fr_meas = 1000/performance['windowRefreshTimeAvg_ms']
TOLERANCE_FR = 20
msg = f'Configured ({fr_conf}) and measured ({fr_meas}) refresh rate differ by more than {TOLERANCE_FR}Hz'
assert isclose(fr_conf, fr_meas, abs_tol=TOLERANCE_FR), msg

## setup serial port or other trigger port
engine.connectTriggerInterface(config['triggers'])

## stimuli
engine.loadStimuli()


triggers = Triggers()

engine.signalStartRecording() ## for eego setup

## before experiment
engine.showMessage(const.ready_msg)

## training block
train_trials = generate_trials('training', const)
fate = Fate()
engine.displayFixCross(1000)
for trial in train_trials:
    trial.run(engine, fate, const)
    if engine.exitRequested():
        break ## exit trial loop

#raise ValueError
engine.showMessage(const.exp_msg)

## main experiment
exp_trials = generate_trials('experiment', const)
fate = Fate()
block_trials_correct = []
engine.displayFixCross(1000)
for t, trial in enumerate(exp_trials, start=1):

    trial.run(engine, fate, const)
    block_trials_correct.append(trial.correct==True)
    if engine.exitRequested():
        break ## exit trial loop

    ## end of block
    if t % const.block_trials == 0:

        ## not the end of the task; display feedback:
        if t < len(exp_trials):
            accuracy = mean(block_trials_correct)
            if accuracy <= 0.75 :
                msg = const.low_acc_msg
            elif accuracy > 0.90 :
                msg = const.high_acc_msg
            else :
                msg = const.mid_acc_msg
            engine.showMessage(msg)
            block_trials_correct = [] ## reset list of trial outcomes

        ## do this after every block including the last one:
        engine.displayFixCross(1000) ## fixation cross after block feedback

## Create table from trials and save to csv file
all_trials = train_trials+exp_trials
df = DataFrame([asdict(t) for t in all_trials])
df.to_csv(trials_fpath, float_format='%.4f')

if not engine.exitRequested():
    engine.showMessage(const.thank_msg, confirm=False)
engine.stop()
