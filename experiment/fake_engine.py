"""Drop-in replacement for the PsychopyEngine for testing
when psychopy is not available
"""
from __future__ import annotations
from typing import Tuple, Dict, Any, TYPE_CHECKING, Union, Literal, Optional
import json
if TYPE_CHECKING:
    CardPos = Union[Literal['left'], Literal['right']]


class FakeTriggerPort:

    def trigger(self, val: int) -> None:
        print(f'[TRIGGER] {val}')


class FakeEngine(object):

    flips = 0
    secs = 0
    flip_dur = 0.016
    exitChecks = 0

    def __init__(self) -> None:
        self.port = FakeTriggerPort()

    def askForString(self, question: str) -> str:
        print(f'[ENGINE] askForString: {question}')
        return '999'

    def configureLog(self, fpath: str):
        pass

    def logDictionary(self, label: str, content: Dict[str, Any]) -> None:
        msg = json.dumps({label: content}, sort_keys=True, indent=4)
        print(f'[DICT] {msg}')

    def connectTriggerInterface(self, settings: Dict) -> None:
        print('[ENGINE] connectTriggerInterface()')

    def configureWindow(self, settings: Dict):
        print('[ENGINE] configureWindow()')

    def measureHardwarePerformance(self) -> Dict[str, Any]:
        return dict(windowRefreshTimeAvg_ms=16)
    
    def loadStimuli(self, cardSize: float, cardOffset: float, fixSize: float):
        print('[ENGINE] loadStimuli()')

    def createLine(self, **kwargs):
        """Paint a line of pixels

        Used by viewpixx triggers
        """
        print('[ENGINE] createLine()')

    def showMessage(self, message: str, height=0.6, confirm=True):
        print(f'[ENGINE] Message: {"WAIT" if confirm else ""} {message}')
        self.secs += 20

    def displayEmptyScreen(self, duration: int) -> float:
        print(f'[ENGINE] EmptyScreen ({duration} x flip)')
        self.flips += duration
        return (self.flips - duration) * self.flip_dur

    def displayFixCross(self, duration: int):
        print(f'[ENGINE] Fixation ({duration} x flip)')
        self.flips += duration

    def displayCards(self,
                     card1:int,
                     card2:int,
                     highlight: Optional[CardPos]=None,
                     showValue: Optional[CardPos]=None,
                     value: float=0.0,
                     choose=False,
                     duration: int=100
                     ):
        print(f'[ENGINE] displayCards card1={card1} card2={card2} highlight={highlight} showValue={showValue}')
    
    def estimateDuration(self) -> int:
        """Simulated duration in seconds
        """
        return self.secs + round(self.flips * (1/60))
    
    def exitRequested(self) -> bool:
        self.exitChecks += 1
        return self.exitChecks > 10
    
    def flush(self) -> None:
        print(f'[ENGINE] Flushing')
    
    def stop(self) -> None:
        print(f'[ENGINE] Stopping')
