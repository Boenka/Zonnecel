import pyvisa
import time
import math
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
        for i in range (0, 2000):
            self.dev.set_output_value(i)
            self.List_U_Lamp.append(float(self.dev.get_input_voltage(1) - float(self.dev.get_input_voltage(2)))) #U1 - U2 voor Ulamp
            self.List_I_Lamp.append(float(self.dev.get_input_voltage(2) / 220))
        return self.List_U_Lamp, self.List_I_Lamp

#Berekent de error met Var / sqrt(N)
def error(lijst):
    teller = 0
    for i in lijst[0]:
        teller += i
    gemiddelde = teller / len(lijst[1])
    var = 0
    for i in range(1024):
        var += (lijst[1][i] - gemiddelde)**2
    return math.sqrt(var) / math.sqrt(1023)
