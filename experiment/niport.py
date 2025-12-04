from __future__ import print_function
import vendor.nidaqmx as nidaqmx
from psychopy.core import wait


class NidaqPort:

    def __init__(self, address: str):
        address = 'Dev1'
        DOPORT = address + '/port0/line0'

        device = nidaqmx.libnidaqmx.Device(address)
        device.reset()

        ## or DIGITAL PORTS 1-8!!
        #port = USB651
        self.do_task = nidaqmx.DigitalOutputTask(name='MyDOTask')
        self.do_task.create_channel(DOPORT, name='line0')
        self.do_task.start()

    def trigger(self, val: int) -> None:
        self.do_task.write(val)
        wait(0.005, hogCPUperiod=0.005)
        self.do_task.write(0)
