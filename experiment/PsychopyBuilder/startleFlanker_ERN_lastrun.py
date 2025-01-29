#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.2.3),
    on January 30, 2024, at 15:12
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '4'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# Run 'Before Experiment' code from code_trial
import random
import time
import psychtoolbox as ptb
from psychopy import sound, visual

# Run 'Before Experiment' code from code_LSL
try :
    import pylsl as LSL
except :
    print(f"LSL not available.")
# Run 'Before Experiment' code from code_trial
import random
import time
import psychtoolbox as ptb
from psychopy import sound, visual

# Run 'Before Experiment' code from code_LSL
try :
    import pylsl as LSL
except :
    print(f"LSL not available.")
# --- Setup global variables (available in all functions) ---
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# Store info about the experiment session
psychopyVersion = '2023.2.3'
expName = 'startleFlanker_ERN'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'Experiment ID': '7357',
    'EEG connected?': ['n','y'],
    'date': data.getDateStr(),  # add a simple timestamp
    'expName': expName,
    'psychopyVersion': psychopyVersion,
}


def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # temporarily remove keys which the dialog doesn't need to show
    poppedKeys = {
        'date': expInfo.pop('date', data.getDateStr()),
        'expName': expInfo.pop('expName', expName),
        'psychopyVersion': expInfo.pop('psychopyVersion', psychopyVersion),
    }
    # show participant info dialog
    dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # restore hidden keys
    expInfo.update(poppedKeys)
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='D:\\OneDrive - MMU\\Experiments\\startleFlanker_ERN\\startleFlanker_ERN_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # this outputs to the screen, not a file
    logging.console.setLevel(logging.WARNING)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=logging.WARNING)
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=[1920, 1200], fullscr=True, screen=0,
            winType='pyglet', allowStencil=True,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height'
        )
        if expInfo is not None:
            # store frame rate of monitor if we can measure it
            expInfo['frameRate'] = win.getActualFrameRate()
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    win.mouseVisible = False
    win.hideMessage()
    return win


def setupInputs(expInfo, thisExp, win):
    """
    Setup whatever inputs are available (mouse, keyboard, eyetracker, etc.)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    dict
        Dictionary of input devices by name.
    """
    # --- Setup input devices ---
    inputs = {}
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    ioSession = '1'
    if 'session' in expInfo:
        ioSession = str(expInfo['session'])
    ioServer = io.launchHubServer(window=win, **ioConfig)
    eyetracker = None
    
    # create a default keyboard (e.g. to check for escape)
    defaultKeyboard = keyboard.Keyboard(backend='iohub')
    # return inputs dict
    return {
        'ioServer': ioServer,
        'defaultKeyboard': defaultKeyboard,
        'eyetracker': eyetracker,
    }

def pauseExperiment(thisExp, inputs=None, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # prevent components from auto-drawing
    win.stashAutoDraw()
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # make sure we have a keyboard
        if inputs is None:
            inputs = {
                'defaultKeyboard': keyboard.Keyboard(backend='ioHub')
            }
        # check for quit (typically the Esc key)
        if inputs['defaultKeyboard'].getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win, inputs=inputs)
        # flip the screen
        win.flip()
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, inputs=inputs, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # restore auto-drawn components
    win.retrieveAutoDraw()
    # reset any timers
    for timer in timers:
        timer.reset()


def run(expInfo, thisExp, win, inputs, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    inputs : dict
        Dictionary of input devices by name.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = inputs['ioServer']
    defaultKeyboard = inputs['defaultKeyboard']
    eyetracker = inputs['eyetracker']
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "intro" ---
    textbox_intro = visual.TextBox2(
         win, text='This is just a test.\n\n\n\n\nClick anywhere to proceed...', placeholder='Type here...', font='Open Sans',
         pos=(0, 0),     letterHeight=0.05,
         size=(None, None), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='textbox_intro',
         depth=0, autoLog=False,
    )
    mouse_intro = event.Mouse(win=win)
    x, y = [None, None]
    mouse_intro.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "fixation" ---
    ISI = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
    image_fixation = visual.ImageStim(
        win=win,
        name='image_fixation', 
        image='stimuli/fixation.bmp', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=[0.2],
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    
    # --- Initialize components for Routine "trial_block" ---
    image_block = visual.ImageStim(
        win=win,
        name='image_block', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=[0.8],
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    mouse_block = event.Mouse(win=win)
    x, y = [None, None]
    mouse_block.mouseClock = core.Clock()
    # Run 'Begin Experiment' code from code_trial
    showBreakMessage = False
    blockLength = 8
    stimulusDuration = 0.2
    totalTrials_count = 0
    totalTrials = 240
    accuracyTotal = 0
    runningAccuracy = 0
    accuracy_lastTrial = 0
    blockof30N = 0
    startled_trials0 = []
    startled_trials1 = []
    startled_trials4 = []
    startle = sound.Sound(value='stimuli/startle2_reencoded.wav',
                                                volume=1.0,
                                                hamming=False,
                                                name='startle',
                                                autoLog=False)
    # Run 'Begin Experiment' code from code_LSL
    if expInfo['EEG connected?'] == 'y' :
        stream = LSL.StreamInfo('psychopy2eego','Markers',1,0,'string',expInfo['Experiment ID'])
        outlet = LSL.StreamOutlet(stream)
        print(f"LSL active... \
                \n{outlet}\
                \n{stream}")
        outlet.push_sample([str(123)])  # start eego recording
    
    # --- Initialize components for Routine "iTi" ---
    ITI = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ITI')
    
    # --- Initialize components for Routine "ready" ---
    textbox_ready = visual.TextBox2(
         win, text='Ready for the real thing?\n\n\n\n\nClick anywhere to proceed...', placeholder='Type here...', font='Open Sans',
         pos=(0, 0),     letterHeight=0.05,
         size=(None, None), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='textbox_ready',
         depth=0, autoLog=True,
    )
    mouse_ready = event.Mouse(win=win)
    x, y = [None, None]
    mouse_ready.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "fixation" ---
    ISI = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
    image_fixation = visual.ImageStim(
        win=win,
        name='image_fixation', 
        image='stimuli/fixation.bmp', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=[0.2],
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    
    # --- Initialize components for Routine "trial_block" ---
    image_block = visual.ImageStim(
        win=win,
        name='image_block', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=[0.8],
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    mouse_block = event.Mouse(win=win)
    x, y = [None, None]
    mouse_block.mouseClock = core.Clock()
    # Run 'Begin Experiment' code from code_trial
    showBreakMessage = False
    blockLength = 8
    stimulusDuration = 0.2
    totalTrials_count = 0
    totalTrials = 240
    accuracyTotal = 0
    runningAccuracy = 0
    accuracy_lastTrial = 0
    blockof30N = 0
    startled_trials0 = []
    startled_trials1 = []
    startled_trials4 = []
    startle = sound.Sound(value='stimuli/startle2_reencoded.wav',
                                                volume=1.0,
                                                hamming=False,
                                                name='startle',
                                                autoLog=False)
    # Run 'Begin Experiment' code from code_LSL
    if expInfo['EEG connected?'] == 'y' :
        stream = LSL.StreamInfo('psychopy2eego','Markers',1,0,'string',expInfo['Experiment ID'])
        outlet = LSL.StreamOutlet(stream)
        print(f"LSL active... \
                \n{outlet}\
                \n{stream}")
        outlet.push_sample([str(123)])  # start eego recording
    
    # --- Initialize components for Routine "iTi" ---
    ITI = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ITI')
    
    # --- Initialize components for Routine "performanceMessage" ---
    textbox_blockBreak = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Open Sans',
         pos=(0, 0),units='norm',     letterHeight=0.1,
         size=(None, None), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='textbox_blockBreak',
         depth=-1, autoLog=True,
    )
    textbox_continue = visual.TextBox2(
         win, text='Click to continue...', placeholder='Type here...', font='Open Sans',
         pos=(0, -0.6),units='norm',     letterHeight=0.1,
         size=(0.5, 0.5), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='textbox_continue',
         depth=-2, autoLog=True,
    )
    mouse_continue = event.Mouse(win=win)
    x, y = [None, None]
    mouse_continue.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "end" ---
    textbox = visual.TextBox2(
         win, text='Fin.', placeholder='Type here...', font='Open Sans',
         pos=(0, 0),     letterHeight=0.2,
         size=(None, None), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='textbox',
         depth=0, autoLog=True,
    )
    
    # create some handy timers
    if globalClock is None:
        globalClock = core.Clock()  # to track the time since experiment started
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6)
    
    # --- Prepare to start Routine "intro" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('intro.started', globalClock.getTime())
    textbox_intro.reset()
    # setup some python lists for storing info about the mouse_intro
    mouse_intro.x = []
    mouse_intro.y = []
    mouse_intro.leftButton = []
    mouse_intro.midButton = []
    mouse_intro.rightButton = []
    mouse_intro.time = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    introComponents = [textbox_intro, mouse_intro]
    for thisComponent in introComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "intro" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textbox_intro* updates
        
        # if textbox_intro is starting this frame...
        if textbox_intro.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textbox_intro.frameNStart = frameN  # exact frame index
            textbox_intro.tStart = t  # local t and not account for scr refresh
            textbox_intro.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textbox_intro, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textbox_intro.started')
            # update status
            textbox_intro.status = STARTED
            textbox_intro.setAutoDraw(True)
        
        # if textbox_intro is active this frame...
        if textbox_intro.status == STARTED:
            # update params
            pass
        # *mouse_intro* updates
        
        # if mouse_intro is starting this frame...
        if mouse_intro.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_intro.frameNStart = frameN  # exact frame index
            mouse_intro.tStart = t  # local t and not account for scr refresh
            mouse_intro.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_intro, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_intro.started', t)
            # update status
            mouse_intro.status = STARTED
            mouse_intro.mouseClock.reset()
            prevButtonState = mouse_intro.getPressed()  # if button is down already this ISN'T a new click
        if mouse_intro.status == STARTED:  # only update if started and not finished!
            buttons = mouse_intro.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    x, y = mouse_intro.getPos()
                    mouse_intro.x.append(x)
                    mouse_intro.y.append(y)
                    buttons = mouse_intro.getPressed()
                    mouse_intro.leftButton.append(buttons[0])
                    mouse_intro.midButton.append(buttons[1])
                    mouse_intro.rightButton.append(buttons[2])
                    mouse_intro.time.append(mouse_intro.mouseClock.getTime())
                    
                    continueRoutine = False  # end routine on response
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in introComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "intro" ---
    for thisComponent in introComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('intro.stopped', globalClock.getTime())
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('mouse_intro.x', mouse_intro.x)
    thisExp.addData('mouse_intro.y', mouse_intro.y)
    thisExp.addData('mouse_intro.leftButton', mouse_intro.leftButton)
    thisExp.addData('mouse_intro.midButton', mouse_intro.midButton)
    thisExp.addData('mouse_intro.rightButton', mouse_intro.rightButton)
    thisExp.addData('mouse_intro.time', mouse_intro.time)
    thisExp.nextEntry()
    # the Routine "intro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    practice_trials = data.TrialHandler(nReps=8.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('conditions.csv'),
        seed=None, name='practice_trials')
    thisExp.addLoop(practice_trials)  # add the loop to the experiment
    thisPractice_trial = practice_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_trial.rgb)
    if thisPractice_trial != None:
        for paramName in thisPractice_trial:
            globals()[paramName] = thisPractice_trial[paramName]
    
    for thisPractice_trial in practice_trials:
        currentLoop = practice_trials
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisPractice_trial.rgb)
        if thisPractice_trial != None:
            for paramName in thisPractice_trial:
                globals()[paramName] = thisPractice_trial[paramName]
        
        # --- Prepare to start Routine "fixation" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('fixation.started', globalClock.getTime())
        # keep track of which components have finished
        fixationComponents = [ISI, image_fixation]
        for thisComponent in fixationComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "fixation" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.6:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_fixation* updates
            
            # if image_fixation is starting this frame...
            if image_fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_fixation.frameNStart = frameN  # exact frame index
                image_fixation.tStart = t  # local t and not account for scr refresh
                image_fixation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_fixation, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_fixation.started')
                # update status
                image_fixation.status = STARTED
                image_fixation.setAutoDraw(True)
            
            # if image_fixation is active this frame...
            if image_fixation.status == STARTED:
                # update params
                pass
            
            # if image_fixation is stopping this frame...
            if image_fixation.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_fixation.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    image_fixation.tStop = t  # not accounting for scr refresh
                    image_fixation.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_fixation.stopped')
                    # update status
                    image_fixation.status = FINISHED
                    image_fixation.setAutoDraw(False)
            # *ISI* period
            
            # if ISI is starting this frame...
            if ISI.status == NOT_STARTED and t >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                ISI.frameNStart = frameN  # exact frame index
                ISI.tStart = t  # local t and not account for scr refresh
                ISI.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ISI, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('ISI.started', t)
                # update status
                ISI.status = STARTED
                ISI.start(0.1)
            elif ISI.status == STARTED:  # one frame should pass before updating params and completing
                ISI.complete()  # finish the static period
                ISI.tStop = ISI.tStart + 0.1  # record stop time
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fixationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "fixation" ---
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('fixation.stopped', globalClock.getTime())
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.600000)
        
        # --- Prepare to start Routine "trial_block" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('trial_block.started', globalClock.getTime())
        image_block.setImage(stimulus)
        # setup some python lists for storing info about the mouse_block
        mouse_block.x = []
        mouse_block.y = []
        mouse_block.leftButton = []
        mouse_block.midButton = []
        mouse_block.rightButton = []
        mouse_block.time = []
        gotValidClick = False  # until a click is received
        # Run 'Begin Routine' code from code_trial
        trialNofcurrentLoop = currentLoop.thisN + 1
        totalTrials_count += 1
        mouse_block.clickReset()
        iTi_time = random.randrange(500,1000,50) / 1000
        
        if totalTrials_count > 1 :
            accuracy_lastTrial = accuracy
        
        if "practice" in currentLoop.name :
            trialType = 'p'
        else :
            trialType = 'e'
        
        if totalTrials_count % blockLength == 0 \
            and trialType == 'e' :
                blockof30N += 1
                showBreakMessage = True
        elif totalTrials_count % blockLength == 0 \
            and trialType == 'p' :
                print("practice_trials finished...")
                practice_trials.finished = True
        else :
                showBreakMessage = False
        # Run 'Begin Routine' code from code_LSL
        if expInfo['EEG connected?'] == 'y' :
            LSL_msg = [str(event_marker)]
            outlet.push_sample(LSL_msg)
            print(f"{LSL_msg}")
        # keep track of which components have finished
        trial_blockComponents = [image_block, mouse_block]
        for thisComponent in trial_blockComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "trial_block" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_block* updates
            
            # if image_block is starting this frame...
            if image_block.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_block.frameNStart = frameN  # exact frame index
                image_block.tStart = t  # local t and not account for scr refresh
                image_block.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_block, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_block.started')
                # update status
                image_block.status = STARTED
                image_block.setAutoDraw(True)
            
            # if image_block is active this frame...
            if image_block.status == STARTED:
                # update params
                pass
            
            # if image_block is stopping this frame...
            if image_block.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_block.tStartRefresh + stimulusDuration-frameTolerance:
                    # keep track of stop time/frame for later
                    image_block.tStop = t  # not accounting for scr refresh
                    image_block.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_block.stopped')
                    # update status
                    image_block.status = FINISHED
                    image_block.setAutoDraw(False)
            # *mouse_block* updates
            
            # if mouse_block is starting this frame...
            if mouse_block.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse_block.frameNStart = frameN  # exact frame index
                mouse_block.tStart = t  # local t and not account for scr refresh
                mouse_block.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_block, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'mouse_block.started')
                # update status
                mouse_block.status = STARTED
                mouse_block.mouseClock.reset()
                prevButtonState = mouse_block.getPressed()  # if button is down already this ISN'T a new click
            if mouse_block.status == STARTED:  # only update if started and not finished!
                buttons = mouse_block.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        x, y = mouse_block.getPos()
                        mouse_block.x.append(x)
                        mouse_block.y.append(y)
                        buttons = mouse_block.getPressed()
                        mouse_block.leftButton.append(buttons[0])
                        mouse_block.midButton.append(buttons[1])
                        mouse_block.rightButton.append(buttons[2])
                        mouse_block.time.append(mouse_block.mouseClock.getTime())
                        
                        continueRoutine = False  # end routine on response
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trial_blockComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trial_block" ---
        for thisComponent in trial_blockComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('trial_block.stopped', globalClock.getTime())
        # store data for practice_trials (TrialHandler)
        practice_trials.addData('mouse_block.x', mouse_block.x)
        practice_trials.addData('mouse_block.y', mouse_block.y)
        practice_trials.addData('mouse_block.leftButton', mouse_block.leftButton)
        practice_trials.addData('mouse_block.midButton', mouse_block.midButton)
        practice_trials.addData('mouse_block.rightButton', mouse_block.rightButton)
        practice_trials.addData('mouse_block.time', mouse_block.time)
        # Run 'End Routine' code from code_trial
        buttons,times = mouse_block.getPressed(getTime=True)
        if buttons[-1] == correct_resp :
            accuracy = 1 
        else:
            accuracy = 0
        accuracyTotal += accuracy
        runningAccuracy = (accuracyTotal / totalTrials_count) * 100
        
        #random.sample([1,0],1)[0]
        if accuracy_lastTrial == 0 and random.randrange(0,100,1) >= 50 and len(startled_trials1) < (totalTrials/100*50) :
            startled = True
            startled_trials1.append(totalTrials_count)
        elif accuracy_lastTrial == 0 and random.randrange(0,100,1) >= 50 and len(startled_trials0) < (totalTrials/100*50):
            startled = True
            startled_trials0.append(totalTrials_count)
        elif random.randrange(0,100,1) >= 50 and len(startled_trials4) < (totalTrials/100*4):
            startled = True
            startled_trials4.append(totalTrials_count)
        else :
            startled = False
        
        if startled == True :
            startle.play()
            #nextFlip = win.getFutureFlipTime(clock='ptb')
            #startle.play(when=nextFlip)  # sync with screen refresh
        
        thisExp.addData('trialType',trialType)
        thisExp.addData('accuracy',accuracy)
        thisExp.addData('rt',mouse_block.time[-1])
        thisExp.addData('trialN',trialNofcurrentLoop)
        thisExp.addData('totalTrials',totalTrials_count)
        thisExp.addData('accuracyTotal',accuracyTotal)
        thisExp.addData('runningAccuracy',runningAccuracy)
        # Run 'End Routine' code from code_LSL
        if expInfo['EEG connected?'] == 'y' :
            outlet.push_sample([str(accuracy)])
            print([str(accuracy)])
            if startled :
                outlet.push_sample([str("5::Startled!")])
        # the Routine "trial_block" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "iTi" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('iTi.started', globalClock.getTime())
        # keep track of which components have finished
        iTiComponents = [ITI]
        for thisComponent in iTiComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "iTi" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # *ITI* period
            
            # if ITI is starting this frame...
            if ITI.status == NOT_STARTED and t >= 0-frameTolerance:
                # keep track of start time/frame for later
                ITI.frameNStart = frameN  # exact frame index
                ITI.tStart = t  # local t and not account for scr refresh
                ITI.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ITI, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('ITI.started', t)
                # update status
                ITI.status = STARTED
                ITI.start(iTi_time)
            elif ITI.status == STARTED:  # one frame should pass before updating params and completing
                ITI.complete()  # finish the static period
                ITI.tStop = ITI.tStart + iTi_time  # record stop time
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in iTiComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "iTi" ---
        for thisComponent in iTiComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('iTi.stopped', globalClock.getTime())
        # the Routine "iTi" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 8.0 repeats of 'practice_trials'
    
    
    # --- Prepare to start Routine "ready" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('ready.started', globalClock.getTime())
    textbox_ready.reset()
    # setup some python lists for storing info about the mouse_ready
    mouse_ready.x = []
    mouse_ready.y = []
    mouse_ready.leftButton = []
    mouse_ready.midButton = []
    mouse_ready.rightButton = []
    mouse_ready.time = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    readyComponents = [textbox_ready, mouse_ready]
    for thisComponent in readyComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ready" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textbox_ready* updates
        
        # if textbox_ready is starting this frame...
        if textbox_ready.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textbox_ready.frameNStart = frameN  # exact frame index
            textbox_ready.tStart = t  # local t and not account for scr refresh
            textbox_ready.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textbox_ready, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textbox_ready.started')
            # update status
            textbox_ready.status = STARTED
            textbox_ready.setAutoDraw(True)
        
        # if textbox_ready is active this frame...
        if textbox_ready.status == STARTED:
            # update params
            pass
        # *mouse_ready* updates
        
        # if mouse_ready is starting this frame...
        if mouse_ready.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_ready.frameNStart = frameN  # exact frame index
            mouse_ready.tStart = t  # local t and not account for scr refresh
            mouse_ready.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_ready, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_ready.started', t)
            # update status
            mouse_ready.status = STARTED
            mouse_ready.mouseClock.reset()
            prevButtonState = mouse_ready.getPressed()  # if button is down already this ISN'T a new click
        if mouse_ready.status == STARTED:  # only update if started and not finished!
            buttons = mouse_ready.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    x, y = mouse_ready.getPos()
                    mouse_ready.x.append(x)
                    mouse_ready.y.append(y)
                    buttons = mouse_ready.getPressed()
                    mouse_ready.leftButton.append(buttons[0])
                    mouse_ready.midButton.append(buttons[1])
                    mouse_ready.rightButton.append(buttons[2])
                    mouse_ready.time.append(mouse_ready.mouseClock.getTime())
                    
                    continueRoutine = False  # end routine on response
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in readyComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ready" ---
    for thisComponent in readyComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('ready.stopped', globalClock.getTime())
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('mouse_ready.x', mouse_ready.x)
    thisExp.addData('mouse_ready.y', mouse_ready.y)
    thisExp.addData('mouse_ready.leftButton', mouse_ready.leftButton)
    thisExp.addData('mouse_ready.midButton', mouse_ready.midButton)
    thisExp.addData('mouse_ready.rightButton', mouse_ready.rightButton)
    thisExp.addData('mouse_ready.time', mouse_ready.time)
    thisExp.nextEntry()
    # the Routine "ready" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    blocks = data.TrialHandler(nReps=3.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='blocks')
    thisExp.addLoop(blocks)  # add the loop to the experiment
    thisBlock = blocks.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            globals()[paramName] = thisBlock[paramName]
    
    for thisBlock in blocks:
        currentLoop = blocks
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
        if thisBlock != None:
            for paramName in thisBlock:
                globals()[paramName] = thisBlock[paramName]
        
        # set up handler to look after randomisation of conditions etc
        trials_block = data.TrialHandler(nReps=8*30, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('conditions.csv'),
            seed=None, name='trials_block')
        thisExp.addLoop(trials_block)  # add the loop to the experiment
        thisTrials_block = trials_block.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_block.rgb)
        if thisTrials_block != None:
            for paramName in thisTrials_block:
                globals()[paramName] = thisTrials_block[paramName]
        
        for thisTrials_block in trials_block:
            currentLoop = trials_block
            thisExp.timestampOnFlip(win, 'thisRow.t')
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    inputs=inputs, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
            )
            # abbreviate parameter names if possible (e.g. rgb = thisTrials_block.rgb)
            if thisTrials_block != None:
                for paramName in thisTrials_block:
                    globals()[paramName] = thisTrials_block[paramName]
            
            # --- Prepare to start Routine "fixation" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('fixation.started', globalClock.getTime())
            # keep track of which components have finished
            fixationComponents = [ISI, image_fixation]
            for thisComponent in fixationComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "fixation" ---
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.6:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *image_fixation* updates
                
                # if image_fixation is starting this frame...
                if image_fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_fixation.frameNStart = frameN  # exact frame index
                    image_fixation.tStart = t  # local t and not account for scr refresh
                    image_fixation.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_fixation, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_fixation.started')
                    # update status
                    image_fixation.status = STARTED
                    image_fixation.setAutoDraw(True)
                
                # if image_fixation is active this frame...
                if image_fixation.status == STARTED:
                    # update params
                    pass
                
                # if image_fixation is stopping this frame...
                if image_fixation.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_fixation.tStartRefresh + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        image_fixation.tStop = t  # not accounting for scr refresh
                        image_fixation.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_fixation.stopped')
                        # update status
                        image_fixation.status = FINISHED
                        image_fixation.setAutoDraw(False)
                # *ISI* period
                
                # if ISI is starting this frame...
                if ISI.status == NOT_STARTED and t >= 0.5-frameTolerance:
                    # keep track of start time/frame for later
                    ISI.frameNStart = frameN  # exact frame index
                    ISI.tStart = t  # local t and not account for scr refresh
                    ISI.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ISI, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.addData('ISI.started', t)
                    # update status
                    ISI.status = STARTED
                    ISI.start(0.1)
                elif ISI.status == STARTED:  # one frame should pass before updating params and completing
                    ISI.complete()  # finish the static period
                    ISI.tStop = ISI.tStart + 0.1  # record stop time
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, inputs=inputs, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in fixationComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "fixation" ---
            for thisComponent in fixationComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('fixation.stopped', globalClock.getTime())
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.600000)
            
            # --- Prepare to start Routine "trial_block" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('trial_block.started', globalClock.getTime())
            image_block.setImage(stimulus)
            # setup some python lists for storing info about the mouse_block
            mouse_block.x = []
            mouse_block.y = []
            mouse_block.leftButton = []
            mouse_block.midButton = []
            mouse_block.rightButton = []
            mouse_block.time = []
            gotValidClick = False  # until a click is received
            # Run 'Begin Routine' code from code_trial
            trialNofcurrentLoop = currentLoop.thisN + 1
            totalTrials_count += 1
            mouse_block.clickReset()
            iTi_time = random.randrange(500,1000,50) / 1000
            
            if totalTrials_count > 1 :
                accuracy_lastTrial = accuracy
            
            if "practice" in currentLoop.name :
                trialType = 'p'
            else :
                trialType = 'e'
            
            if totalTrials_count % blockLength == 0 \
                and trialType == 'e' :
                    blockof30N += 1
                    showBreakMessage = True
            elif totalTrials_count % blockLength == 0 \
                and trialType == 'p' :
                    print("practice_trials finished...")
                    practice_trials.finished = True
            else :
                    showBreakMessage = False
            # Run 'Begin Routine' code from code_LSL
            if expInfo['EEG connected?'] == 'y' :
                LSL_msg = [str(event_marker)]
                outlet.push_sample(LSL_msg)
                print(f"{LSL_msg}")
            # keep track of which components have finished
            trial_blockComponents = [image_block, mouse_block]
            for thisComponent in trial_blockComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "trial_block" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *image_block* updates
                
                # if image_block is starting this frame...
                if image_block.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_block.frameNStart = frameN  # exact frame index
                    image_block.tStart = t  # local t and not account for scr refresh
                    image_block.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_block, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_block.started')
                    # update status
                    image_block.status = STARTED
                    image_block.setAutoDraw(True)
                
                # if image_block is active this frame...
                if image_block.status == STARTED:
                    # update params
                    pass
                
                # if image_block is stopping this frame...
                if image_block.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_block.tStartRefresh + stimulusDuration-frameTolerance:
                        # keep track of stop time/frame for later
                        image_block.tStop = t  # not accounting for scr refresh
                        image_block.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_block.stopped')
                        # update status
                        image_block.status = FINISHED
                        image_block.setAutoDraw(False)
                # *mouse_block* updates
                
                # if mouse_block is starting this frame...
                if mouse_block.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    mouse_block.frameNStart = frameN  # exact frame index
                    mouse_block.tStart = t  # local t and not account for scr refresh
                    mouse_block.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(mouse_block, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'mouse_block.started')
                    # update status
                    mouse_block.status = STARTED
                    mouse_block.mouseClock.reset()
                    prevButtonState = mouse_block.getPressed()  # if button is down already this ISN'T a new click
                if mouse_block.status == STARTED:  # only update if started and not finished!
                    buttons = mouse_block.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            x, y = mouse_block.getPos()
                            mouse_block.x.append(x)
                            mouse_block.y.append(y)
                            buttons = mouse_block.getPressed()
                            mouse_block.leftButton.append(buttons[0])
                            mouse_block.midButton.append(buttons[1])
                            mouse_block.rightButton.append(buttons[2])
                            mouse_block.time.append(mouse_block.mouseClock.getTime())
                            
                            continueRoutine = False  # end routine on response
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, inputs=inputs, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in trial_blockComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "trial_block" ---
            for thisComponent in trial_blockComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('trial_block.stopped', globalClock.getTime())
            # store data for trials_block (TrialHandler)
            trials_block.addData('mouse_block.x', mouse_block.x)
            trials_block.addData('mouse_block.y', mouse_block.y)
            trials_block.addData('mouse_block.leftButton', mouse_block.leftButton)
            trials_block.addData('mouse_block.midButton', mouse_block.midButton)
            trials_block.addData('mouse_block.rightButton', mouse_block.rightButton)
            trials_block.addData('mouse_block.time', mouse_block.time)
            # Run 'End Routine' code from code_trial
            buttons,times = mouse_block.getPressed(getTime=True)
            if buttons[-1] == correct_resp :
                accuracy = 1 
            else:
                accuracy = 0
            accuracyTotal += accuracy
            runningAccuracy = (accuracyTotal / totalTrials_count) * 100
            
            #random.sample([1,0],1)[0]
            if accuracy_lastTrial == 0 and random.randrange(0,100,1) >= 50 and len(startled_trials1) < (totalTrials/100*50) :
                startled = True
                startled_trials1.append(totalTrials_count)
            elif accuracy_lastTrial == 0 and random.randrange(0,100,1) >= 50 and len(startled_trials0) < (totalTrials/100*50):
                startled = True
                startled_trials0.append(totalTrials_count)
            elif random.randrange(0,100,1) >= 50 and len(startled_trials4) < (totalTrials/100*4):
                startled = True
                startled_trials4.append(totalTrials_count)
            else :
                startled = False
            
            if startled == True :
                startle.play()
                #nextFlip = win.getFutureFlipTime(clock='ptb')
                #startle.play(when=nextFlip)  # sync with screen refresh
            
            thisExp.addData('trialType',trialType)
            thisExp.addData('accuracy',accuracy)
            thisExp.addData('rt',mouse_block.time[-1])
            thisExp.addData('trialN',trialNofcurrentLoop)
            thisExp.addData('totalTrials',totalTrials_count)
            thisExp.addData('accuracyTotal',accuracyTotal)
            thisExp.addData('runningAccuracy',runningAccuracy)
            # Run 'End Routine' code from code_LSL
            if expInfo['EEG connected?'] == 'y' :
                outlet.push_sample([str(accuracy)])
                print([str(accuracy)])
                if startled :
                    outlet.push_sample([str("5::Startled!")])
            # the Routine "trial_block" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "iTi" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('iTi.started', globalClock.getTime())
            # keep track of which components have finished
            iTiComponents = [ITI]
            for thisComponent in iTiComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "iTi" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # *ITI* period
                
                # if ITI is starting this frame...
                if ITI.status == NOT_STARTED and t >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    ITI.frameNStart = frameN  # exact frame index
                    ITI.tStart = t  # local t and not account for scr refresh
                    ITI.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ITI, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.addData('ITI.started', t)
                    # update status
                    ITI.status = STARTED
                    ITI.start(iTi_time)
                elif ITI.status == STARTED:  # one frame should pass before updating params and completing
                    ITI.complete()  # finish the static period
                    ITI.tStop = ITI.tStart + iTi_time  # record stop time
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, inputs=inputs, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in iTiComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "iTi" ---
            for thisComponent in iTiComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('iTi.stopped', globalClock.getTime())
            # the Routine "iTi" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # set up handler to look after randomisation of conditions etc
            interBlock = data.TrialHandler(nReps=showBreakMessage, method='sequential', 
                extraInfo=expInfo, originPath=-1,
                trialList=[None],
                seed=None, name='interBlock')
            thisExp.addLoop(interBlock)  # add the loop to the experiment
            thisInterBlock = interBlock.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisInterBlock.rgb)
            if thisInterBlock != None:
                for paramName in thisInterBlock:
                    globals()[paramName] = thisInterBlock[paramName]
            
            for thisInterBlock in interBlock:
                currentLoop = interBlock
                thisExp.timestampOnFlip(win, 'thisRow.t')
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        inputs=inputs, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                )
                # abbreviate parameter names if possible (e.g. rgb = thisInterBlock.rgb)
                if thisInterBlock != None:
                    for paramName in thisInterBlock:
                        globals()[paramName] = thisInterBlock[paramName]
                
                # --- Prepare to start Routine "performanceMessage" ---
                continueRoutine = True
                # update component parameters for each repeat
                thisExp.addData('performanceMessage.started', globalClock.getTime())
                # Run 'Begin Routine' code from code_performance
                '''
                If performance was 75% correct or lower, the message
                ‘‘Please try to be more accurate’’ was displayed; performance
                above 90% correct was followed by ‘‘Please try to respond
                faster’’; if performance was between these levels, the message
                ‘‘You’re doing a great job’’ was displayed.
                '''
                if runningAccuracy <= 75 :
                    message = "Please try to be more accurate"
                elif runningAccuracy > 90 :
                    message = "Please try to respond faster"
                else :
                    message = "You’re doing a great job"
                textbox_blockBreak.reset()
                textbox_blockBreak.setText(message)
                textbox_continue.reset()
                # setup some python lists for storing info about the mouse_continue
                mouse_continue.x = []
                mouse_continue.y = []
                mouse_continue.leftButton = []
                mouse_continue.midButton = []
                mouse_continue.rightButton = []
                mouse_continue.time = []
                gotValidClick = False  # until a click is received
                # keep track of which components have finished
                performanceMessageComponents = [textbox_blockBreak, textbox_continue, mouse_continue]
                for thisComponent in performanceMessageComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "performanceMessage" ---
                routineForceEnded = not continueRoutine
                while continueRoutine:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *textbox_blockBreak* updates
                    
                    # if textbox_blockBreak is starting this frame...
                    if textbox_blockBreak.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        textbox_blockBreak.frameNStart = frameN  # exact frame index
                        textbox_blockBreak.tStart = t  # local t and not account for scr refresh
                        textbox_blockBreak.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(textbox_blockBreak, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'textbox_blockBreak.started')
                        # update status
                        textbox_blockBreak.status = STARTED
                        textbox_blockBreak.setAutoDraw(True)
                    
                    # if textbox_blockBreak is active this frame...
                    if textbox_blockBreak.status == STARTED:
                        # update params
                        pass
                    
                    # *textbox_continue* updates
                    
                    # if textbox_continue is starting this frame...
                    if textbox_continue.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                        # keep track of start time/frame for later
                        textbox_continue.frameNStart = frameN  # exact frame index
                        textbox_continue.tStart = t  # local t and not account for scr refresh
                        textbox_continue.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(textbox_continue, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'textbox_continue.started')
                        # update status
                        textbox_continue.status = STARTED
                        textbox_continue.setAutoDraw(True)
                    
                    # if textbox_continue is active this frame...
                    if textbox_continue.status == STARTED:
                        # update params
                        pass
                    # *mouse_continue* updates
                    
                    # if mouse_continue is starting this frame...
                    if mouse_continue.status == NOT_STARTED and t >= 1-frameTolerance:
                        # keep track of start time/frame for later
                        mouse_continue.frameNStart = frameN  # exact frame index
                        mouse_continue.tStart = t  # local t and not account for scr refresh
                        mouse_continue.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(mouse_continue, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.addData('mouse_continue.started', t)
                        # update status
                        mouse_continue.status = STARTED
                        mouse_continue.mouseClock.reset()
                        prevButtonState = mouse_continue.getPressed()  # if button is down already this ISN'T a new click
                    if mouse_continue.status == STARTED:  # only update if started and not finished!
                        buttons = mouse_continue.getPressed()
                        if buttons != prevButtonState:  # button state changed?
                            prevButtonState = buttons
                            if sum(buttons) > 0:  # state changed to a new click
                                x, y = mouse_continue.getPos()
                                mouse_continue.x.append(x)
                                mouse_continue.y.append(y)
                                buttons = mouse_continue.getPressed()
                                mouse_continue.leftButton.append(buttons[0])
                                mouse_continue.midButton.append(buttons[1])
                                mouse_continue.rightButton.append(buttons[2])
                                mouse_continue.time.append(mouse_continue.mouseClock.getTime())
                                
                                continueRoutine = False  # end routine on response
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, inputs=inputs, win=win)
                        return
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in performanceMessageComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "performanceMessage" ---
                for thisComponent in performanceMessageComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                thisExp.addData('performanceMessage.stopped', globalClock.getTime())
                # store data for interBlock (TrialHandler)
                interBlock.addData('mouse_continue.x', mouse_continue.x)
                interBlock.addData('mouse_continue.y', mouse_continue.y)
                interBlock.addData('mouse_continue.leftButton', mouse_continue.leftButton)
                interBlock.addData('mouse_continue.midButton', mouse_continue.midButton)
                interBlock.addData('mouse_continue.rightButton', mouse_continue.rightButton)
                interBlock.addData('mouse_continue.time', mouse_continue.time)
                # the Routine "performanceMessage" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
            # completed showBreakMessage repeats of 'interBlock'
            
            thisExp.nextEntry()
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
        # completed 8*30 repeats of 'trials_block'
        
    # completed 3.0 repeats of 'blocks'
    
    
    # --- Prepare to start Routine "end" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('end.started', globalClock.getTime())
    textbox.reset()
    # keep track of which components have finished
    endComponents = [textbox]
    for thisComponent in endComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "end" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textbox* updates
        
        # if textbox is starting this frame...
        if textbox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textbox.frameNStart = frameN  # exact frame index
            textbox.tStart = t  # local t and not account for scr refresh
            textbox.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textbox, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textbox.started')
            # update status
            textbox.status = STARTED
            textbox.setAutoDraw(True)
        
        # if textbox is active this frame...
        if textbox.status == STARTED:
            # update params
            pass
        
        # if textbox is stopping this frame...
        if textbox.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textbox.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                textbox.tStop = t  # not accounting for scr refresh
                textbox.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textbox.stopped')
                # update status
                textbox.status = FINISHED
                textbox.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in endComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "end" ---
    for thisComponent in endComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('end.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    # Run 'End Experiment' code from code_LSL
    if expInfo['EEG connected?'] == 'y' :
        outlet.push_sample([str(127)])  # stop eego recording
    # Run 'End Experiment' code from code_LSL
    if expInfo['EEG connected?'] == 'y' :
        outlet.push_sample([str(127)])  # stop eego recording
    
    # mark experiment as finished
    endExperiment(thisExp, win=win, inputs=inputs)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, inputs=None, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # shut down eyetracker, if there is one
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()


def quit(thisExp, win=None, inputs=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    inputs : dict
        Dictionary of input devices by name.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    inputs = setupInputs(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win, 
        inputs=inputs
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win, inputs=inputs)
