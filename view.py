import pyvisa
import time
import math
import matplotlib.pyplot as plt
from arduino_device import ArduinoVISADevice, list_devices
from DiodeExperiment import DiodeExperiment, error

Begin = DiodeExperiment(8)
test1 = Begin.scan()


x = test1[0]
y = test1[1]
er = error(test1)
plt.xlabel("Voltage in [V]")
plt.ylim
plt.ylabel("Amperage in [A]")
plt.scatter(x,y, er)
plt.show()