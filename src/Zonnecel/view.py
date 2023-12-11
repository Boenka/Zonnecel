import csv

import matplotlib.pyplot as plt

from Zonnecel.zonnecelcalc import DiodeExperiment, list_devices


#Function to make plot so i can use poetry scripts
def plot():

    """
    Initialize a DiodeExperiment class with the correct port. Create test whith parameters scan(start,end,rep). 
    Plot an errorbar with U values of the lamp on the x-axis and I values on the y-axis and the correct std lists for the errorbars. (also hides line between points)
    Shows the plot to the user. 

    Also saves the data from the test in a CSV file
    """
    
    Begin = DiodeExperiment('ASRL::SIMPV_BRIGHT::INSTR')
    test1 = Begin.scan(0, 1024, 2)

    #Assign X, Y, X error en Y error 
    U, I, err, erry, P, R = test1

    #Plotting the graph
    plt.figure("1")
    plt.xlabel("Voltage in [V]")
    plt.ylabel("Amperage in [A]")
    plt.errorbar(x = U ,y = I ,xerr = err, yerr= erry, linestyle='', marker='o')
    plt.show()

    plt.figure('2')
    plt.xlabel("Resistance in [R]")
    plt.ylabel("Power in [P]")
    plt.scatter(x = R ,y = P , linestyle='', marker='o')
    plt.show()


    #Save data to csv file
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


    return 

#TYPE STARTTEST IN TERMINAL TO START TEST
plot()