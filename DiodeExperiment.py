import pyvisa
import time
import math
import numpy as np
import matplotlib.pyplot as plt
from arduino_device import ArduinoVISADevice, list_devices

#Class voor het experiment
class DiodeExperiment():

    #Maken van lijsten en device voor gebruik in class
    def __init__(self, port):
        self.dev = ArduinoVISADevice(port)
        self.List_U_Lamp = []
        self.List_I_Lamp = []

    #Loop voor experiment    
    def scan(self):
        self.lst_test = []
        for j in range (3):
            self.lst_test.append([])
            for i in range (0, 1024):
                self.dev.set_output_value(i)
                self.List_U_Lamp.append(float(self.dev.get_input_voltage(1) - float(self.dev.get_input_voltage(2)))) #U1 - U2 voor Ulamp
                self.List_I_Lamp.append(float(self.dev.get_input_voltage(2) / 220))
                self.lst_test[j].append(float(self.dev.get_input_voltage(1) - float(self.dev.get_input_voltage(2))))
        
        #standard deviation 
        self.std_lst = []
        for i in range(len(self.lst_test)):
            self.std_lst.append(float(np.std(self.lst_test[i])))

        return self.List_U_Lamp, self.List_I_Lamp, self.std_lst
