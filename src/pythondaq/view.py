import pyvisa
import time
import math
import matplotlib.pyplot as plt
from pythondaq.arduino_device import ArduinoVISADevice, list_devices
from pythondaq.DiodeExperiment import DiodeExperiment


#Function to make plot so i can use poetry scripts
def plot():
    Begin = DiodeExperiment(7)
    test1 = Begin.scan()

    #Assign X, Y, X error en Y error 
    x = test1[0]
    y = test1[1]
    err = test1[2]
    erry = test1[3]

    #Plotting the graph
    plt.xlabel("Voltage in [V]")
    plt.ylim
    plt.ylabel("Amperage in [A]")
    plt.errorbar(x,y,xerr = err, yerr= erry)
    plt.show()
    return

#TYPE STARTTEST IN TERMINAL TO START TEST