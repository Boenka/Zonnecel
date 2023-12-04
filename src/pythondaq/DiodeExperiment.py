import numpy as np

from pythondaq.arduino_device import (ArduinoVISADevice, list_devices,
                                      list_devices_noprint)


#Class for the experiment
class DiodeExperiment():

    """
    Initializing a class to set up different experiments.

    """
    
    #Making lists that will be used
    def __init__(self, port):

        """
        Initialitzing the lists used for calculations and plotting and creating an instance of the ArduinoVISADevice class to use.

        Args:
        port (int) = the number of the port on which the arduino is connected.

        """

        self.dev = ArduinoVISADevice(port)
        self.lst_lists_U = []
        self.lst_lists_I = []
        self.lst_mean_U = []
        self.lst_mean_I = []
        self.lst_error_U = []
        self.lst_error_I = []
        self.lst_tot = []

    def close(self):
        """
        Closes the device
        """
        self.dev.close()

    def iden(self):
        """
        Returns the identification string
        """
        return self.dev.get_identification()

    def scan(self, start, end, rep):

        """
        Makes a start to end long list of lists. Sets the output voltage to the values start to end. Gets the input voltage rep times for each ADC value and appends these the corresponding list.
        With these values calculate U and I for plotting. For all the lists in the main list calculate the mean value and the standart deviation. 
        Return lists with the mean U , mean I, std U, std I for each ADC value.

        Args:
        start (int) : the ADC value at which the scan starts
        end (int)   : the ADC value at which the scan end
        rep (int)   : the amount of repetitions of the scan for caluclations of mean and std
        
        """
        
            #Fill the lists with 1024 lists to prepare for mean and std calculations for all the ADC values
        for k in range (1024):
            self.lst_lists_U.append([])
            self.lst_lists_I.append([])
            
        for i in range(start, end):       
            for j in range (rep):
                self.dev.set_output_value(i)
                self.lst_lists_U[i].append(float(self.dev.get_input_voltage(1) - float(self.dev.get_input_voltage(2)))) #U1 - U2 for Ulamp
                self.lst_lists_I[i].append(float(self.dev.get_input_voltage(2) / 220)) #Calc I

            #Fill the mean and error lists      
        for i in range(start,end):
            self.lst_mean_U.append(np.mean(self.lst_lists_U[i]))
            self.lst_mean_I.append(np.mean(self.lst_lists_I[i]))
            self.lst_error_U.append(np.std(self.lst_lists_U[i]))
            self.lst_error_I.append(np.std(self.lst_lists_I[i]))


        #turn off lamp
        self.dev.set_output_value(0)
        

        return self.lst_mean_U, self.lst_mean_I, self.lst_error_U, self.lst_error_I

