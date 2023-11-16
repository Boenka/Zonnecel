import matplotlib.pyplot as plt
from pythondaq.DiodeExperiment import DiodeExperiment, list_devices
import csv

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

    #Save data to csv
    zipped_data = zip(U,I, err, erry)
    with open('metingen.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, lineterminator= '\n')
        writer.writerow([
            'Voltage in [V]',
            'Amperage in [A]',
            'Error on the voltage',
            'Error on the Amperage'
        ])
        writer.writerows(zipped_data)


    return csvfile

#TYPE STARTTEST IN TERMINAL TO START TEST