"""
This is an interface / wrapper around the psychopy functionality.
This makes it easier to work on the rest of the code without psychopy,
and to debug trial order, data formatting etc.

https://psychopy.org/coder/codeStimuli.html
https://psychopy.org/general/timing/detectingFrameDrops.html#warn-me-if-i-drop-a-frame
"""
from __future__ import annotations
from typing import TYPE_CHECKING, Tuple, Dict, List, Union, Any, Optional, Literal
import json
from experiment.triggers import Triggers
from psychopy.monitors import Monitor
from psychopy.core import wait
from psychopy import logging
from psychopy.hardware.keyboard import Keyboard
from psychopy.visual import Window, TextStim, ImageStim
from psychopy.visual.line import Line
from psychopy.visual.rect import Rect
from psychopy.visual.shape import ShapeStim
from psychopy.sound import Sound
from psychopy.info import RunTimeInfo
from psychopy.event import waitKeys, getKeys, Mouse
from psychopy import plugins
plugins.activatePlugins()

import numpy
from experiment.ports import TriggerInterface, FakeTriggerPort, createTriggerPort
if TYPE_CHECKING:
    Stimulus = Union[TextStim, ShapeStim, Rect]
    from experiment.conditions import Phase, Direction, Compatibility, StartleCondition
    from experiment.constants import Constants


class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, numpy.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)


class PsychopyEngine(object):

    win: Window
    port: TriggerInterface
    _exitNow: bool

    ## stimuli
    cards: List[Rect]
    fixCross: ShapeStim
    const: Constants

    def __init__(self, const: Constants, triggers: Triggers) -> None:
        self.port = FakeTriggerPort()
        self._exitNow = False
        self.kb = Keyboard()
        self.const = const
        self.triggers = triggers

    def configureLog(self, fpath: str):
        logging.console.setLevel(logging.WARN)
        logging.LogFile(fpath, level=logging.INFO, filemode='w')

    def logDictionary(self, label: str, content: Dict[str, Any]) -> None:
        logging.info(
            json.dumps({label: content}, sort_keys=True, indent=4, cls=NumpyEncoder)
        )

    def flush(self) -> None:
        logging.flush()

    def configureWindow(self, settings: Dict) -> None:
        mon_settings = settings['monitor']
        my_monitor = Monitor(
            name='EML',
            distance=mon_settings['distance']
        )
        my_monitor.setSizePix(mon_settings['resolution'])
        my_monitor.setWidth(mon_settings['width'])
        my_monitor.saveMon()
        self.win = Window(
            size=mon_settings['resolution'],
            monitor=my_monitor,
            color='black',
            fullscr=True,
            units='deg',
            screen=int(mon_settings['screen']),
        )
        self.win.mouseVisible = False 
        scaling = mon_settings['resolution'][0] / self.win.size[0]
        if scaling == 0.5: 
            print('Looks like a retina display')
        if scaling != 1.0:
            print('Weird scaling. Is your configured monitor resolution correct?')
        self.mouse = Mouse(visible=None, win=self.win)

    def askForParticipantId(self) -> str:
        DEFAULT = '9999'
        LABEL = 'Participant ID'
        try:
            from psychopy.gui import Dlg
            dlg = Dlg(title=LABEL)
            dlg.addField(LABEL, DEFAULT)
            string_id = dlg.show()
            if not dlg.OK:
                raise ValueError('No participant ID given')
        except:
            from tkinter.simpledialog import askstring
            string_id = askstring(LABEL, LABEL, initialvalue=str(DEFAULT))
            if string_id is None:
                raise ValueError('No participant ID given')
        return string_id

    def measureHardwarePerformance(self) -> Dict[str, Any]:
        return RunTimeInfo(win=self.win)

    def loadStimuli(self, bitrate=44100):
        assert bitrate in (44100, 48000), 'invalid bitrate parameter'
        self.startle = Sound(
            value=f'stimuli/alternativeStartle_{bitrate}_50ms.wav',
            volume=1.0,
            hamming=False,
            name='startle',
            autoLog=False
        )

        self.vol_test_sound = Sound(
            value=f'stimuli/alternativeStartle_60s_{bitrate}.wav',
            volume=1.0,
            hamming=False,
            name='startle',
            autoLog=False
        )

        self.all_left = ImageStim(
            win=self.win,
            image='stimuli/All_Left.jpg',
            size=(self.const.img_size, self.const.img_size),
            units='deg',
            pos=(0, 0),
            name='all_left',
        )
        self.all_right = ImageStim(
            win=self.win,
            image='stimuli/All_Right.jpg',
            size=(self.const.img_size, self.const.img_size),
            units='deg',
            pos=(0, 0),
            name='all_right',
        )
        self.center_left = ImageStim(
            win=self.win,
            image='stimuli/Center_Left.jpg',
            size=(self.const.img_size, self.const.img_size),
            units='deg',
            pos=(0, 0),
            name=f'center_left',
        )
        self.center_right = ImageStim(
            win=self.win,
            image='stimuli/Center_Right.jpg',
            size=(self.const.img_size, self.const.img_size),
            units='deg',
            pos=(0, 0),
            name=f'center_right',
        )

        self.fixCross = ShapeStim(
            self.win,
            pos=(0.0, 0.0),
            vertices=(
                (0,-self.const.fix_size),
                (0,self.const.fix_size),
                (0,0),
                (-self.const.fix_size,0),
                (self.const.fix_size,0)
            ),
            units = 'deg',
            lineWidth = self.const.fix_size*10,
            closeShape = False,
            lineColor='white',
            name='fixCross'
        )
        self.fixCross.autoLog = True

    def createLine(self, **kwargs):
        """Paint a line of pixels

        Used by viewpixx triggers
        """
        return Line(**kwargs)

    def showMessage(self, message: str, confirm=True, min_dur=2):
        msg = TextStim(
            self.win,
            text=message,
            height=self.const.instruction_text_size,
            units='deg',
            wrapWidth=100,
            name='message'
        )
        msg.autoLog = True
        msg.draw()
        self.win.flip()
        if confirm:
            wait(min_dur)
            self.mouse.clickReset()
            while True:
                buttons, _ = self.mouse.getPressed(getTime=True)
                if sum(buttons):
                    return
        else:
            wait(1.5)

    def connectTriggerInterface(self, settings: Dict) -> None:
        self.port = createTriggerPort(
            typ=settings.get('type', '?'),
            engine=self,
            scale=1.0,
            address=settings.get('address', ''),
            rate=settings.get('baudrate', 0),
            viewPixBulbSize=7.0
        )

    def displayFlankersAndAwaitResponse(self,
                phase: Phase,
                direction: Direction,
                compatibility: Compatibility,
                stim_dur: int,
                resp_dur: int,
            ) -> Tuple[Optional[bool], Optional[float]]:
        if direction == 'left' and compatibility == 'compatible':
            img = self.all_left
        if direction == 'right' and compatibility == 'compatible':
            img = self.all_right
        if direction == 'left' and compatibility == 'incompatible':
            img = self.center_left
        if direction == 'right' and compatibility == 'incompatible':
            img = self.center_right
        
        img.draw()
        triggerNr = self.triggers.forFlanker(phase, compatibility, direction)
        self.win.logOnFlip(level=logging.DATA, msg=f'flip {triggerNr}')

        def flipHandler():
            self.port.trigger(triggerNr)
            self.mouse.clickReset() #buttons=(0, 1, 2)

        self.win.callOnFlip(flipHandler)
        self.win.flip()
        wait(stim_dur/1000)
        self.win.flip()

        n_iter = int(resp_dur / 5)
        for _ in range(n_iter):
            buttons, times = self.mouse.getPressed(getTime=True)
            if sum(buttons):
                if direction == 'left':
                    rt = times[0]
                    correct = buttons == [1, 0, 0]
                else:
                    rt = times[-1]
                    correct = buttons == [0, 0, 1]
                break
            wait(5/1000)
            ## todo check at end instead
        else:
            rt = 0.0
            correct = None
        triggerNr = self.triggers.forResponse(phase, correct)
        self.port.trigger(triggerNr)
        return correct, rt

    def displayFixCross(self, duration: int):
        self.fixCross.draw()
        self.win.flip()
        wait(duration/1000)

    def delayAndStartle(self, reason: StartleCondition, delay: int):
        wait(delay/1000)
        triggerNr = self.triggers.forStartle(reason)
        self.startle.play()
        self.port.trigger(triggerNr)
        wait(self.startle.getDuration())

    def playSoundCheck(self, msg: str):
        msg = TextStim(
            self.win,
            text=msg,
            height=self.const.instruction_text_size,
            units='deg',
            wrapWidth=100,
            name='message'
        )
        msg.draw()
        self.win.flip()
        self.vol_test_sound.play()
        wait(self.vol_test_sound.getDuration())

    def exitRequested(self) -> bool:
        if self._exitNow:
            return True
        new_keys = getKeys(keyList=['escape', 'esc']) #
        if len(new_keys):
            self._exitNow = True
            logging.warn('EXIT REQUESTED (ESC pressed)')
            return True
        return False
    
    def signalStartRecording(self) -> None:
        self.port.trigger(self.const.eego_start_trigger)
    
    def stop(self) -> None:
        self.port.trigger(self.const.eego_stop_trigger)
        self.win.close()
