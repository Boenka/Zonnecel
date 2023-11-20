import pyvisa
import matplotlib.pyplot as plt

class ArduinoVISADevice():

    """
    Initialize a class for the arduino device

    """

    #Initializing class with correct port
    def __init__(self, p):

        """
        Initialize a connection with the device and read and write prefrences

        Args:
        p (int) = the port the arduino is connected to
        """

        self.rm = pyvisa.ResourceManager("@py")
        self.port = f"ASRL{p}::INSTR"
        self.list_adc = [] 
        self.device = self.rm.open_resource(
    f"{self.port}", read_termination="\r\n", write_termination="\n"
)      
    #Returns the identification string
    def get_identification(self):

        """
        Return the identification string and print it out.

        """

        print(f"The identification string of the port is: {self.device.query('*IDN?')}")
        return self.device.query("*IDN?")

    #Sets the output value 
    def set_output_value(self,value):

        """
        Sets the output value of the arduino 

        Args:
        value (int): integer value between 0 and 1023

        """

        self.device.query(f"OUT:CH0 {value}")
        self.list_adc.append(value)
        print(f"The output value has been set to {value}")

    #Gets back the previous output value
    def get_ouput_value(self):

        """
        Prints and returns the output value currently set

        """

        print(f'The previous ouput voltage in ADC values was: {self.device.query(f"OUT:CH0?")}')
        return self.device.query(f"OUT:CH0?")
    
    #Gets input value for either channel 1 or 2 
    def get_input_value(self,channel_num):

        """
        Prints and return the input value for either channel 1 or channel 2

        Args:
        channel_num (int) = the number of the channel you want to read (either 1 or 2)
        """

        if channel_num == 1 or 2:
            return self.device.query(f"MEAS:CH{channel_num}?")
        else:
            return print("This channel can not be read")
    
    #Converst input ADC value to voltage
    def get_input_voltage(self, channel_num):

        """
        Returns the input value as a voltage in [V].

        Args:
        channel_num = the number of the channel you want to read (either 1 or 2)
        """

        self.a = float(self.device.query(f"MEAS:CH{channel_num}?")) / 1023 * 3.3
        #print(f"The voltage in V for input channel {port} is {round(self.a, 2)}V")
        return self.a

#Gives a list of the devices
def list_devices():
    rm = pyvisa.ResourceManager("@py")
    ports = rm.list_resources()
    return print(ports)