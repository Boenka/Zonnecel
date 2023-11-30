import csv
import sys

import numpy as np
import pyqtgraph as pg
from PySide6 import QtWidgets
from PySide6.QtCore import Slot

from pythondaq.DiodeExperiment import DiodeExperiment, list_devices_noprint

## TYPE APP IN TERMINAL TO START PROGRAM

#Create a class for the user interface
class UserInterface(QtWidgets.QMainWindow):
    
    def __init__(self):
        # roep de __init__() aan van de parent class
        super().__init__()

        #Create a lists of the ports currently connected
        self.list_ports = list_devices_noprint()

        #Create and select the central widget. Create the graphWidget to plot and add to the vbox. Create two horizontal boxes and one vertical box to add widgets to.
        central_widget = QtWidgets.QWidget()
        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(central_widget)
        vbox = QtWidgets.QVBoxLayout(central_widget)
        vbox.addWidget(self.graphWidget)
        
        h2box = QtWidgets.QHBoxLayout()
        vbox.addLayout(h2box)
        hbox = QtWidgets.QHBoxLayout()
        vbox.addLayout(hbox)

        #Create the labels and add them to the h2box above the widgets in the hbox
        h2box.addWidget(QtWidgets.QLabel('select port'))
        h2box.addWidget(QtWidgets.QLabel('create plot'))
        h2box.addWidget(QtWidgets.QLabel('start ADC'))
        h2box.addWidget(QtWidgets.QLabel('stop ADC'))
        h2box.addWidget(QtWidgets.QLabel('num reps'))
        h2box.addWidget(QtWidgets.QLabel('save file'))
        
        #Create the options for the combobox and add the combobox to the hbox
        self.combo = QtWidgets.QComboBox()
        for i in range(len(self.list_ports)):
            self.combo.addItem(str(self.list_ports[i]))
        hbox.addWidget(self.combo)

        #Create a push button and add it to the hbox
        self.plot_QpushButton = QtWidgets.QPushButton("plot")
        hbox.addWidget(self.plot_QpushButton)

        #Create a spinbox for the start button and set the standard value, the range and the size of the steps. Add to hbox.
        self.start_Qspinbox = QtWidgets.QSpinBox()
        self.start_Qspinbox.setValue(0)
        self.start_Qspinbox.setRange(0, 1024)
        self.start_Qspinbox.setSingleStep(1)
        hbox.addWidget(self.start_Qspinbox)

        #Create a spinbox for the stop button and set the standard value, the range and the size of the steps. Add to hbox.
        self.stop_Qspinbox = QtWidgets.QSpinBox()
        self.stop_Qspinbox.setValue(100)
        self.stop_Qspinbox.setRange(0, 1024)
        self.stop_Qspinbox.setSingleStep(1)
        hbox.addWidget(self.stop_Qspinbox)
        
        #Create a spinbox for the rep button and set the standard value, the range and the size of the steps. Add to hbox.
        self.rep_button = QtWidgets.QSpinBox()
        self.rep_button.setValue(2)
        self.rep_button.setRange(0,1001)
        self.rep_button.setSingleStep(1)
        hbox.addWidget(self.rep_button)\
        
        #Create a button to save the file and add it to the hbox
        self.save_QPushButton = QtWidgets.QPushButton("SAVE")
        hbox.addWidget(self.save_QPushButton)

        #Connect the functions to the button created above
        self.plot_QpushButton.clicked.connect(self.plot)
        self.save_QPushButton.clicked.connect(self.save)
    
    @Slot()
    def plot(self):
        self.graphWidget.clear()
        """
        Initialize a DiodeExperiment class with the correct port. Create test whith parameters scan(start,end,rep). 
        Plot an errorbar with U values of the lamp on the x-axis and I values on the y-axis and the correct std lists for the errorbars. (also hides line between points)
        Shows the plot to the user. 

        """
        
        Begin = DiodeExperiment(self.list_ports[self.combo.currentIndex()])
        test1 = Begin.scan(self.start_Qspinbox.value(), self.stop_Qspinbox.value(), self.rep_button.value())

        #Assign X, Y, X error en Y error 
        self.U, self.I, self.err, self.erry = test1

        #Plotting the graph
        self.graphWidget.plot(self.U, self.I, symbol=None, pen={"color": "black", "width": 5})
        self.graphWidget.setLabel("left", "Current in [A]")
        self.graphWidget.setLabel("bottom", "Voltage in [V]")

        xval = np.array(self.U)
        yval = np.array(self.I)
        width = 2 * np.array(self.err)
        height = 2 * np.array(self.erry)
        error_bars = pg.ErrorBarItem(x=xval, y=yval, width = width, height=height, pen = {"color":"white", "width": 2})
        self.graphWidget.addItem(error_bars)

    def save(self):

        """
        Saves the data to a CSV file with a name of choice. The filename can be typed in the application.
        """

        filename, _ = QtWidgets.QFileDialog.getSaveFileName(filter="CSV files (*.csv)")

        #Save data to csv file
        zipped_data = zip(self.U,self.I, self.err, self.erry)
        with open(f'{filename}', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, lineterminator= '\n')
            writer.writerow([
                'Voltage in [V]',
                'Amperage in [A]',
                'Error on the voltage',
                'Error on the Amperage'
            ])
            writer.writerows(zipped_data)


#Start the program
def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = UserInterface()
    ui.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()  