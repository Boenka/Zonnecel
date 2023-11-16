import pyvisa
import matplotlib.pyplot as plt

class ArduinoVISADevice():
    
    #Initializing class with correct port
    def __init__(self, p):
        self.rm = pyvisa.ResourceManager("@py")
        self.port = f"ASRL{p}::INSTR"
        self.list_adc = [] 
        self.device = self.rm.open_resource(
    f"{self.port}", read_termination="\r\n", write_termination="\n"
)      
    #Returns the identification string
    def get_identification(self):
        print(f"The identification string of the port is: {self.device.query("*IDN?")}")
        return self.device.query("*IDN?")

    #Sets the output value 
    def set_output_value(self,value):
        self.device.query(f"OUT:CH0 {value}")
        self.list_adc.append(value)
        print(f"The output value has been set to {value}")

    #Gets back the previous output value MOET AANGEPAST
    def get_ouput_value(self):
        print(f'The previous ouput voltage in ADC values was: {self.list_adc[len(self.list_adc) - 2]}')
        return self.list_adc[len(self.list_adc) - 2]
    
    #Gets input value for either channel 1 or 2 
    def get_input_value(self,channel_num):
        if channel_num == 1 or 2:
            return self.device.query(f"MEAS:CH{channel_num}?")
        else:
            return print("This channel can not be read")
    
    #Converst input ADC value to voltage
    def get_input_voltage(self, port):
        self.a = float(self.device.query(f"MEAS:CH{port}?")) / 1023 * 3.3
        #print(f"The voltage in V for input channel {port} is {round(self.a, 2)}V")
        return self.a

#Gives a list of the devices
def list_devices():
    rm = pyvisa.ResourceManager("@py")
    ports = rm.list_resources()
    return print(ports)
