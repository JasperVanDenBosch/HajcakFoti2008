"""Abstracts access to the various ways to send triggers to the EEG
"""
from __future__ import annotations
from typing import TYPE_CHECKING, Union
from serial import Serial
from psychopy.parallel import ParallelPort as PsychopyParallelPort
from experiment.fake_engine import FakeTriggerPort
if TYPE_CHECKING:
    from experiment.engine import PsychopyEngine


class SerialTriggerPort:

    def __init__(self, address: str, baud: int):
        self.sport = Serial(port=address, baudrate=baud)

    def trigger(self, val: int) -> None:
        self.sport.write(bytes([val]))
		

class ParallelPort:

    def __init__(self, address: str):
        self.pport = PsychopyParallelPort(address=address)

    def trigger(self, val: int) -> None:
        self.pport.setData(val)


class LabJackPort:

    def __init__(self):
        from psychopy.hardware.labjacks import U3
        self.inner = U3()

    def trigger(self, val: int) -> None:
        self.inner.setData(val, address='FIO')


class EegoLSLPort:

    def __init__(self):
        from pylsl import StreamInfo, StreamOutlet
        stream = StreamInfo('PsychoPy2eego','Markers',1,0,'string','7357')
        self.inner = StreamOutlet(stream)

    def trigger(self, val: int) -> None:
        self.inner.push_sample([str(val)])


class ViewPixxTriggerPort:

    def __init__(self, win: PsychopyEngine, scale: float, viewPixBulbSize: float):
        #halfWidth, halfHeight = self.win.size[0]*scale/2, self.win.size[1]*scale/2
        halfWidth, halfHeight = 5, 5
        self.line = win.createLine(
            win=win,
            units = 'pix',
            lineWidth=viewPixBulbSize+0.5,
            start=[-halfWidth, halfHeight],
            end=[-halfWidth+viewPixBulbSize, halfHeight-viewPixBulbSize],
            interpolate = False,
            colorSpace = 'rgb255',
            lineColor = (200, 200, 200)
        )

    def trigger(self, val: int) -> None:
        val = 200
        self.line.setLineColor((val, val, val))
        self.line.draw()


TriggerInterface = Union[SerialTriggerPort, FakeTriggerPort,
    ViewPixxTriggerPort, LabJackPort, ParallelPort, EegoLSLPort]

def createTriggerPort(typ: str, engine: PsychopyEngine, scale: float, address: str='', rate: int=0, viewPixBulbSize: float=7.0) -> TriggerInterface:
    if typ == 'dummy':
        return FakeTriggerPort()
    elif typ == 'serial':
        return SerialTriggerPort(address, rate)
    elif typ == 'viewpixx':
        return ViewPixxTriggerPort(engine, scale, viewPixBulbSize)
    elif typ == 'labjack':
        return LabJackPort()
    elif typ == 'parallel':
        return ParallelPort(address)
    elif typ == 'eegolsl':
        return EegoLSLPort()
    else:
        raise ValueError('Unknown port type in lab settings.')
