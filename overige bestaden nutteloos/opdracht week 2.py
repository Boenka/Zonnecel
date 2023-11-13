import pyvisa
import time
import matplotlib.pyplot as plt

rm = pyvisa.ResourceManager("@py")

class ArduinoVISADevice():
    
    def __init__(self, p):
        self.port = f"ASRL{p}::INSTR"
        self.lstadc = [] 
        self.device = rm.open_resource(
    f"{self.port}", read_termination="\r\n", write_termination="\n"
)      

    def get_identification(self):
        print(f"The identification string of the port is {self.port}")

    def set_output_value(self,value):
        self.device.query(f"OUT:CH0 {value}")
        self.lstadc.append(value)
        print(f"The output value has been set to {value}")

    def get_ouput_value(self):
        return print(f'The previous ouput voltage in ADC values was: {self.lstadc[len(self.lstadc) - 2]}')
    
    def get_input_value(self,channel_num):
        if channel_num == 1:
            return print(f"The voltage in ADC values for input channel 1 is {self.device.query("MEAS:CH1?")}")
        elif channel_num == 2:
            return print(f"The voltage in ADC values for input channel 2 is {self.device.query("MEAS:CH2?")}")
        else:
            return print("This channel can not be read")
    
    def get_input_voltage(self):
        self.a = float(self.device.query("MEAS:CH1?")) / 1023 * 3.3
        return print(f"The voltage in V for input channel 1 is {round(self.a, 2)}V")

def get_devices():
    

herman = ArduinoVISADevice(8)
herman.set_output_value(780)
herman.set_output_value(1023)
herman.set_output_value(1080)
herman.get_identification()
herman.get_ouput_value()
herman.get_input_value(1)
herman.get_input_value(2)
herman.get_input_voltage()