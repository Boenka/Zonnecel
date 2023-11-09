import pyvisa
import time
import math
import matplotlib.pyplot as plt
from arduino_device import ArduinoVISADevice, list_devices
from DiodeExperiment import DiodeExperiment
Begin = DiodeExperiment(7)
test1 = Begin.scan()


x = test1[0]
y = test1[1]
er = test1[2]
plt.xlabel("Voltage in [V]")
plt.ylim
plt.ylabel("Amperage in [A]")
plt.errorbar(x,y, er)
plt.show()