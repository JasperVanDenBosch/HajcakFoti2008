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
from psychopy.monitors import Monitor
from psychopy.event import waitKeys, getKeys
from psychopy.core import wait
from psychopy import logging
from psychopy.hardware.keyboard import Keyboard
from psychopy.visual import Window, TextStim
from psychopy.visual.line import Line
from psychopy.visual.rect import Rect
from psychopy.visual.shape import ShapeStim
from psychopy.info import RunTimeInfo
#from psychopy.gui import Dlg
import numpy
from experiment.ports import TriggerInterface, FakeTriggerPort, createTriggerPort
if TYPE_CHECKING:
    Stimulus = Union[TextStim, ShapeStim, Rect]
    from experiment.conditions import CardPos
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
    params: Constants

    def __init__(self, params: Constants) -> None:
        self.port = FakeTriggerPort()
        self._exitNow = False
        self.kb = Keyboard()
        self.params = params

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
            name='ICON_YS04',
            distance=mon_settings['distance'])
        my_monitor.setSizePix(mon_settings['resolution'])
        my_monitor.setWidth(mon_settings['width'])
        my_monitor.saveMon()
        self.win = Window(
            size=mon_settings['resolution'],
            monitor=my_monitor,
            color='black',
            fullscr=True,
            units='deg'
        )
        self.win.mouseVisible = False 
        scaling = mon_settings['resolution'][0] / self.win.size[0]
        if scaling == 0.5: 
            print('Looks like a retina display')
        if scaling != 1.0:
            print('Weird scaling. Is your configured monitor resolution correct?')

    def measureHardwarePerformance(self) -> Dict[str, Any]:
        return RunTimeInfo(win=self.win)

    def loadStimuli(self):
        """
        card left
        card right
        value left
        value right
        fixation
        """
        self.val_left = TextStim(self.win, height=1, units='deg', name='value_left')
        self.val_left.autoLog = True
        self.val_right = TextStim(self.win, height=1, units='deg', name='value_right')
        self.val_right.autoLog = True


        self.card_left = Rect(
                win=self.win,
                size=(self.params.card_size, self.params.card_size),
                units='deg',
                pos=(-5, 0),
                lineColor='white',
                fillColor='white',
                lineWidth=0,
                name=f'card_left',
                colorSpace='rgb255'
        )
        self.card_right = Rect(
                win=self.win,
                size=(self.params.card_size, self.params.card_size),
                units='deg',
                pos=(+5, 0),
                lineColor='white',
                fillColor='white',
                lineWidth=0,
                name=f'card_left',
                colorSpace='rgb255'
        )

        self.value_left = TextStim(
            self.win,
            text='0.0',
            font=self.params.value_font,
            units='deg',
            height=self.params.value_text_size,
            pos=(-5, 0),
            color=(1, 1, 1),
            name=f'value_left'
        )
        self.value_right = TextStim(
            self.win,
            text='0.0',
            font=self.params.value_font,
            units='deg',
            height=self.params.value_text_size,
            pos=(+5, 0),
            color=(1, 1, 1),
            name=f'value_right'
        )

        self.fixCross = ShapeStim(
            self.win,
            pos=(0.0, 0.0),
            vertices=(
                (0,-self.params.fix_size),
                (0,self.params.fix_size),
                (0,0),
                (-self.params.fix_size,0),
                (self.params.fix_size,0)
            ),
            units = 'deg',
            lineWidth = self.params.fix_size*10,
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

    def showMessage(self, message: str, confirm=True):
        msg = TextStim(
            self.win,
            text=message,
            height=self.params.instruction_text_size,
            units='deg',
            wrapWidth=100,
            name='message'
        )
        msg.autoLog = True
        msg.draw()
        self.win.flip()
        if confirm:
            waitKeys(keyList='space')
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

    def displayCardsAndAwaitChoice(self, card1:int, card2:int, triggerNr: int) -> Tuple[CardPos, float]:
        response = self.displayCards(card1, card2, choose=True, duration=500_000, triggerNr=triggerNr)
        assert response is not None
        return response
    
    def displayCards(
                self,
                card1:int,
                card2:int,
                duration: int,
                triggerNr: int,
                highlight: Optional[CardPos]=None,
                showValue: Optional[CardPos]=None,
                value: float=0.0,
                choose=False,
            ) -> Optional[Tuple[CardPos, float]]:
        self.fixCross.draw()
        self.card_left.fillColor = self.params.colors[card1]
        self.card_left.lineWidth = 10 if highlight == 'left' else 0
        self.card_left.draw()
        self.card_right.fillColor = self.params.colors[card2]
        self.card_right.lineWidth = 10 if highlight == 'right' else 0
        self.card_right.draw()
        if showValue == 'left':
            self.value_left.text = f'{value:+d}'
            self.value_left.draw()
        if showValue == 'right':
            self.value_right.text = f'{value:+d}'
            self.value_right.draw()
        triggerNr = triggerNr
        self.win.logOnFlip(level=logging.DATA, msg=f'flip {triggerNr}')
        record = dict()
        self.win.timeOnFlip(record, 'flipTime')
        self.kb.clearEvents()
        def flipHandler():
            self.kb.clock.reset()
            self.port.trigger(triggerNr)

        self.win.callOnFlip(flipHandler)
        self.win.flip()
        for _ in range(duration-1):

            if choose:
                keys = self.kb.getKeys(self.params.valid_keys, waitRelease=False)
                if keys:
                    key = keys[0]
                    sideChosen = ['left', 'right'][self.params.valid_keys.index(key.name)]
                    return (sideChosen, key.rt)

            self.fixCross.draw()
            self.card_left.draw()
            self.card_right.draw()
            if showValue == 'left':
                self.value_left.draw()
            if showValue == 'right':
                self.value_right.draw()
            self.win.flip()

    def displayFixCross(self, duration: int):
        for _ in range(duration):
            self.fixCross.draw()
            self.win.flip()

    def exitRequested(self) -> bool:
        if self._exitNow:
            return True
        new_keys = getKeys(keyList=['q', 'delete'])
        if 'q' in new_keys and 'delete' in new_keys:
            self._exitNow = True
            logging.warn('EXIT REQUESTED (Q and DEL pressed)')
            return True
        return False
    
    def stop(self) -> None:
        self.win.close()


