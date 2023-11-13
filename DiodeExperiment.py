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
        self.lst_lijsten_U = []
        self.lst_lijsten_I = []
        self.lst_mean_U = []
        self.lst_mean_I = []
        self.lst_error_U = []
        self.lst_error_I = []
    #Loop voor experiment    
    def scan(self):

            #Voor de lijsten evenveel lijsten aanmaken als de range om zo gemiddeldes en std uit te kunnen rekenen
            for i in range (1024):
                self.lst_lijsten_U.append([])
                self.lst_lijsten_I.append([])
                
                for j in range (3):
                    self.dev.set_output_value(i)
                    self.lst_lijsten_U[i].append(float(self.dev.get_input_voltage(1) - float(self.dev.get_input_voltage(2)))) #U1 - U2 voor Ulamp
                    self.lst_lijsten_I[i].append(float(self.dev.get_input_voltage(2) / 220)) #Stroomsterkte uiterekeken

            #Lijsten vullen met std en gemiddelde waarden.        
            for i in range(1024):
                self.lst_mean_U.append(np.mean(self.lst_lijsten_U[i]))
                self.lst_mean_I.append(np.mean(self.lst_lijsten_I[i]))
                self.lst_error_U.append(np.std(self.lst_lijsten_U[i]))
                self.lst_error_I.append(np.std(self.lst_lijsten_I[i]))

            return self.lst_mean_U, self.lst_mean_I, self.lst_error_U, self.lst_error_I
