import numpy as np

from Zonnecel.zonneceldevice import (ArduinoVISADevice, list_devices,
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
        self.lst_lists_U0 = []
        self.lst_lists_U1 = []
        self.lst_lists_U2 = []

        self.lst_lists_I1 = []
        self.lst_lists_Iz = []

        self.lst_mean_U0 = []
        self.lst_mean_U1 = []
        self.lst_mean_U2 = []
        self.lst_mean_I1 = []
        self.lst_mean_Iz = []

        self.lst_error_Uz = []
        self.lst_error_Iz = []

        self.lst_lists_Pz = []
        self.lst_mean_Pz = []
        self.lst_mean_Rz = []
        self.lst_lsts_Rz = []

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
        for k in range (start, end):
            #self.lst_lists_U0.append([])
            self.lst_lists_U1.append([])
            #self.lst_lists_U2.append([])
            #self.lst_lists_I1.append([])
            self.lst_lists_Iz.append([])
            self.lst_lsts_Rz.append([])
            self.lst_lists_Pz.append([])

            
            
        for i in range(start, end):       
            for j in range (rep):
                self.dev.set_output_value(i)
                
                self.lst_lists_U1[i].append(3*float(self.dev.get_input_voltage(1)))
                #self.lst_lists_U2[i].append(float(self.dev.get_input_voltage(2)))
                #self.lst_lists_I1[i].append(float(self.dev.get_input_voltage(1)) / 1*10**6)
                self.lst_lists_Iz[i].append((float(self.dev.get_input_voltage(2)) / 4.7) + (float(self.dev.get_input_voltage(1)) / 1000000))
                self.lst_lsts_Rz[i].append(3*float(self.dev.get_input_voltage(1))/ ((float(self.dev.get_input_voltage(2)) / 4.7) + (float(self.dev.get_input_voltage(1)) / 1000000)))
                self.lst_lists_Pz[i].append(float(self.dev.get_input_voltage(2)) * (float(self.dev.get_input_voltage(2)) / 4.7) + (float(self.dev.get_input_voltage(1)) / 1000000))
        #calculaties maken:

            #Fill the mean and error lists      
        for i in range(start, end): 
            #self.lst_mean_U0.append(np.mean(self.lst_lists_U0[i]))
            self.lst_mean_U1.append(np.mean(self.lst_lists_U1[i]))
            #self.lst_mean_U2.append(np.mean(self.lst_lists_U2[i]))
            #self.lst_mean_I1.append(np.mean(self.lst_lists_I1[i]))
            self.lst_mean_Iz.append(np.mean(self.lst_lists_Iz[i]))
            self.lst_mean_Pz.append(np.mean(self.lst_lists_Pz[i]))
            self.lst_mean_Rz.append(np.mean(self.lst_lsts_Rz[i]))

            self.lst_error_Uz.append(np.std(self.lst_lists_U1[i]) / np.sqrt(rep))
            self.lst_error_Iz.append(np.std(self.lst_lists_Iz[i]) / np.sqrt(rep))


        #turn off lamp
        self.dev.set_output_value(0)
        

        return self.lst_mean_U1, self.lst_mean_Iz, self.lst_error_Uz, self.lst_error_Iz , self.lst_mean_Pz, self.lst_mean_Rz
