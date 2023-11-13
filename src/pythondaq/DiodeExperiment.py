import pyvisa
import time
import math
import numpy as np
import matplotlib.pyplot as plt
from pythondaq.arduino_device import ArduinoVISADevice, list_devices

#Class for the experiment
class DiodeExperiment():

    #Making lists that will be used
    def __init__(self, port):
        self.dev = ArduinoVISADevice(port)
        self.lst_lijsten_U = []
        self.lst_lijsten_I = []
        self.lst_mean_U = []
        self.lst_mean_I = []
        self.lst_error_U = []
        self.lst_error_I = []

    #Loop for the experiment
    def scan(self):

            #Fill the lists with 1024 lists to prepare for mean and std calculations for all the ADC values
            for i in range (1024):
                self.lst_lijsten_U.append([])
                self.lst_lijsten_I.append([])
                
                for j in range (3):
                    self.dev.set_output_value(i)
                    self.lst_lijsten_U[i].append(float(self.dev.get_input_voltage(1) - float(self.dev.get_input_voltage(2)))) #U1 - U2 for Ulamp
                    self.lst_lijsten_I[i].append(float(self.dev.get_input_voltage(2) / 220)) #Calc I

            #Fill the mean and error lists      
            for i in range(1024):
                self.lst_mean_U.append(np.mean(self.lst_lijsten_U[i]))
                self.lst_mean_I.append(np.mean(self.lst_lijsten_I[i]))
                self.lst_error_U.append(np.std(self.lst_lijsten_U[i]))
                self.lst_error_I.append(np.std(self.lst_lijsten_I[i]))

            return self.lst_mean_U, self.lst_mean_I, self.lst_error_U, self.lst_error_I
