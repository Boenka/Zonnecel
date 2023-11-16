import matplotlib.pyplot as plt
from pythondaq.arduino_device import ArduinoVISADevice, list_devices
from pythondaq.DiodeExperiment import DiodeExperiment


#Function to make plot so i can use poetry scripts
def plot():
    Begin = DiodeExperiment(9)
    test1 = Begin.scan(0, 1024, 3)

    #Assign X, Y, X error en Y error 
    U, I, err, erry = test1

    #Plotting the graph
    plt.xlabel("Voltage in [V]")
    plt.ylim
    plt.ylabel("Amperage in [A]")
    plt.errorbar(x = U ,y = I ,xerr = err, yerr= erry, linestyle='')
    plt.show()
    return

#TYPE STARTTEST IN TERMINAL TO START TEST