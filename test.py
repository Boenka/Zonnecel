import pyvisa
import time
import matplotlib.pyplot as plt
from arduino_device import ArduinoVISADevice, list_devices

rm = pyvisa.ResourceManager("@py")
ports = rm.list_resources()
print(ports)

device = rm.open_resource(
    "ASRL7::INSTR", read_termination="\r\n", write_termination="\n"
)


class ArduinoVISADevice():
    
    def __init__(self):
        self.port = "ASRL7::INSTR"
        self.lstadc = [] 
        self.device = ArduinoVISADevice(port=7)      

    def get_identification(self):
        print(self.device.get_identification())

    def set_output_value(self,value):
        self.device.query(f"OUT:CH0 {value}")
        self.lstadc.append(value)

    def get_ouput_value(self):
        return print(f'{self.lstadc[len(self.lstadc) - 2]}')
    
    def get_input_value(channel_num):
        if channel_num == 1:
            return print(device.query("MEAS:CH1?"))
        elif channel_num == 2:
            return print(device.query("MEAS:CH2?"))
        else:
            return print("This channel can not be read")

class DiodeExperiment():
    def scan():
        listU = []
        listU2 = []
        for i in range(1023):
            listU.append

ArduinoVISADevice.set_output_value(self, 500)