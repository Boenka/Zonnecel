
import pyvisa
import time
import matplotlib.pyplot as plt
from arduino_device import ArduinoVISADevice, list_devices

rm = pyvisa.ResourceManager("@py")



#ElectronicLoadMeasurements Dion Koster 14020920
class ElectronicLoadMeasurements ():
    def __init__(self):                     #Te gebruiken lijsten opstellen
        self.lstR = []
        self.lstU = []
        self.lstP= []
        self.lstI = []

    def getloads(self):                     #Lijst weerstanden oproepen
        print(f"R = {self.lstR}")
        return self.lstR

    def getvoltages(self):                  #Lijst met spanningen oproepen
        print(f"U = {self.lstU}")
        return self.lstU

    def get_currents(self):                 #Lijst met stroomsterkten oproepen
        print(f'I = {self.lstI}')
        return self.lstI

    def get_powers(self):                   #Lijst met vermogens oproepen
        print(f"P = {self.lstP}")
        return self.lstP

    def clear(self):                       #Lijsten legen
        self.lstR = []
        self.lstU = []
        self.lstP= []
        self.lstI = []
        return print("All lists have been cleared")

    def add_measurement(self, R, U):                                    #Toevoegen aan lijst
        if R and U is int or float and R >= 0 and U >= 0:
            self.lstR.append(R)
            self.lstU.append(U)
            I = U/R
            self.lstI.append(I)
            self.lstP.append(U*I)
            return print("Measurements succesfully added")
        else:
            return print("Entries must be positive int or float (add_measurement(R,U))")

measurements = ElectronicLoadMeasurements()

# TESTEN
########
# measurements.add_measurement(R=10, U=0.5)
# measurements.add_measurement(R= 20, U=1.5)
# R = measurements.getloads()
# U = measurements.getvoltages()
# P = measurements.get_powers()
# I = measurements.get_currents()
# U = measurements.getvoltages()
# measurements.add_measurement(R= 10, U=0.5)
# measurements.add_measurement(R= 20, U=1.5)
# measurements.add_measurement(R=10, U=0.5)
# R = measurements.getloads()
# P = measurements.get_powers()
# measurements.get_currents()
