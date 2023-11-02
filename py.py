import pyvisa
import time
import matplotlib.pyplot as plt



################################################################################################################
rm = pyvisa.ResourceManager("@py")
ports = rm.list_resources()
print(ports)

device = rm.open_resource(
    "ASRL7::INSTR", read_termination="\r\n", write_termination="\n"
)
##############################################################################################################
lstadc = [] 
class ArduinoVISADevice():
    
    def __init__():
        port = "ASRL7::INSTR"
        device = ArduinoVISADevice(port=7)      

    def get_identification():
        print(device.get_identification())

    def set_output_value(value):
        device.query(f"OUT:CH0 {value}")
        lstadc.append(value)

    def prevadc():
        if len(lstadc) <= 0:
            return print("There is no previous value")
        else:
            return print(f"The previous value is {lstadc[len(lstadc) - 2]}")
    
    def get_input_value(channel_num):
        if channel_num == 1:
            return print(device.query("MEAS:CH1?"))
        elif channel_num == 2:
            return print(device.query("MEAS:CH2?"))
        else:
            return print("This channel can not be read")



ArduinoVISADevice.set_output_value(200)
ArduinoVISADevice.set_output_value(200)
ArduinoVISADevice.prevadc()

########################################################################################################################

listU1 = []
listU2 = []
for i in range(0,1500):
            device.query(f"OUT:CH0 {i}")
            a = device.query("MEAS:CH1?")
            b = device.query("MEAS:CH2?")
            listU1.append(a)
            listU2.append(b)

device.query(f"OUT:CH0 {0}")
#################################################################################################################

measurements = []
lstR = []
lstU = []
lstP= []

class ElectronicLoadMeasurements ():
    
    def add_measurement(R, U):
        lstR.append(R)
        lstU.append(U)
        lstP.append(U/R)
        
        return 

    def getloads():
        return print(f"R={lstR}")

    def getvoltages():
        return print(f"U={lstU}")

    def get_powers():
        return print(f"P={lstP}")

    def clear():
        lstR = []
        lstU = []
        lstP= []
        return

ElectronicLoadMeasurements.add_measurement(10, 12)
ElectronicLoadMeasurements.getloads()
ElectronicLoadMeasurements.getvoltages()





################################################################################################################
fig = plt.figure()

x = range(0, 1500)
y2 = listU2

plt.plot(x,y2)
plt.xlim(700,1100)
plt.ylim(0,150)

####################################################################################
fig = plt.figure('assa')

x = range(0, 1500)
lstmin = []

for i in range(len(listU1)):
    lstmin.append(int(listU1[i]) - int(listU2[i]))
plt.plot(x,lstmin)
plt.xlim(0,1500)
plt.ylim(0,1000)

########################################################################################
fig = plt.figure('assa2')

y = listU1
x = range(0, 1500)

plt.plot(x,listU1)
plt.xlim(0,1500)
plt.ylim(0,1000)
########################################################################################################
plt.legend()
plt.show()





