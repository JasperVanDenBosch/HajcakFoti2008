from __future__ import print_function
import nidaqmx
from psychopy.core import wait


## DIGITAL PORTS 1-8!!

#port = USB651





class NidaqPort:

    def __init__(self, address: str):
        address = 'Dev1'
        DOPORT = address + '/port0/line0'

        device = nidaqmx.libnidaqmx.Device(address)
        device.reset()

        digitalOutputTask = nidaqmx.DigitalOutputTask(name='MyDOTask')
        digitalOutputTask.create_channel(DOPORT, name='line0')
        digitalOutputTask.start()


    def trigger(self, val: int) -> None:

        for i in range(10):
            # Set DO port to HIGH
            digitalOutputTask.write(1)
            wait(1, hogCPUperiod=1)
            # Set DO port to LOW
            digitalOutputTask.write(0)
            wait(1, hogCPUperiod=1)

# Stop DO signal generation
digitalOutputTask.stop()

