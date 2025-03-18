"""Play a long version of the startle sound to test loudness

"""
from experiment.constants import Constants
from experiment.engine import PsychopyEngine
from experiment.labs import getLabConfiguration
from experiment.triggers import Triggers
const = Constants()  # load fixed parameters wrt timing, sizing etc


## this object represents drawing and interactions via psychopy
triggers = Triggers()
engine = PsychopyEngine(const, triggers)

## user input
config = getLabConfiguration()

## set log levels and log file location
engine.configureLog('tmp.log')

## setup psychopy monitor and window objects
engine.configureWindow(config)

## record some basic info

## stimuli
if 'sound' in config:
    bitrate = config['sound']['bitrate']
else:
    bitrate = 44100
engine.loadStimuli(bitrate)


## before experiment
engine.showMessage('Click a mouse button to start sound')

engine.delayAndStartle('training' , 500)

N_REPS = 5
for s in range(1, N_REPS+1):
    engine.playSoundCheck(f'Playing sound (1min). Repetition {s}/{N_REPS}.'
                          '\n\nPress ESC to exit after.')

    if engine.exitRequested():
        break ## exit trial loop

engine.stop()
