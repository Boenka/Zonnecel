import csv
import sys

import matplotlib.pyplot as plt
import numpy as np
import pyqtgraph as pg
from numpy import pi
from PySide6 import QtWidgets
from PySide6.QtCore import Slot

from pythondaq.DiodeExperiment import DiodeExperiment, list_devices_noprint


class UserInterface(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.lstports = list_devices_noprint()

        central_widget = QtWidgets.QWidget()
        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(central_widget)
        vbox = QtWidgets.QVBoxLayout(central_widget)
        vbox.addWidget(self.graphWidget)
        
        h2box = QtWidgets.QHBoxLayout()
        vbox.addLayout(h2box)
        hbox = QtWidgets.QHBoxLayout()
        vbox.addLayout(hbox)

        h2box.addWidget(QtWidgets.QLabel('select port'))
        h2box.addWidget(QtWidgets.QLabel('create plot'))
        h2box.addWidget(QtWidgets.QLabel('start ADC'))
        h2box.addWidget(QtWidgets.QLabel('stop ADC'))
        h2box.addWidget(QtWidgets.QLabel('num reps'))
        h2box.addWidget(QtWidgets.QLabel('save file'))
        
        self.combo = QtWidgets.QComboBox()
        for i in range(len(self.lstports)):
            self.combo.addItem(str(self.lstports[i]))
        

        hbox.addWidget(self.combo)

        self.plot_button = QtWidgets.QPushButton("plot")
        hbox.addWidget(self.plot_button)

        self.start_button = QtWidgets.QSpinBox()
        self.start_button.setValue(0)
        self.start_button.setRange(0, 1024)
        self.start_button.setSingleStep(1)
        hbox.addWidget(self.start_button)

        self.stop_button = QtWidgets.QSpinBox()
        self.stop_button.setValue(100)
        self.stop_button.setRange(0, 1024)
        self.stop_button.setSingleStep(1)
        hbox.addWidget(self.stop_button)

        self.rep_button = QtWidgets.QSpinBox()
        self.rep_button.setValue(2)
        self.rep_button.setRange(0,1001)
        self.rep_button.setSingleStep(1)
        hbox.addWidget(self.rep_button)\
        
        self.save_button = QtWidgets.QPushButton("SAVE")
        hbox.addWidget(self.save_button)


        self.plot_button.clicked.connect(self.plot)
        self.save_button.clicked.connect(self.save)
    
    @Slot()
    def plot(self):
        self.graphWidget.clear()
        """
        Initialize a DiodeExperiment class with the correct port. Create test whith parameters scan(start,end,rep). 
        Plot an errorbar with U values of the lamp on the x-axis and I values on the y-axis and the correct std lists for the errorbars. (also hides line between points)
        Shows the plot to the user. 

        Also saves the data from the test in a CSV file
        """
        
        Begin = DiodeExperiment(self.lstports[self.combo.currentIndex()])
        test1 = Begin.scan(self.start_button.value(), self.stop_button.value(), self.rep_button.value())

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



def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = UserInterface()
    ui.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()  