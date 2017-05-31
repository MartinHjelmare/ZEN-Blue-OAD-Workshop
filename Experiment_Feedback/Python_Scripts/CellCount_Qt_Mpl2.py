# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 11:43:01 2011

@author: sebastian.rhode

CellCount_Qt_Mpl2.py
Version: 1.0
Date: 2012-11-14

This little Qt widget is designed to read data from and TXT file every ... seconds
and displays the data in two different ways.

1) Bar Plot = number of 2nd column
2) Bar Plot = cumulative sum of number from column so far

This just an example to illustrate what is possible.

"""

from pylab import *
import numpy as np
#import matplotlib.pyplot as plt
import optparse
from livedatafeed import LiveDataFeed


from PyQt4.QtCore import *
from PyQt4.QtGui import *
# Qt4 bindings for core Qt functionalities (non-GUI)
from PyQt4 import QtCore
# Python Qt4 bindings for GUI objects
from PyQt4 import QtGui

# import the MainWindow widget from the converted .ui files
import ui_CellCount_Qt_Mpl

frequency = 1

class CellCount_Qt_Mpl(QtGui.QWidget, ui_CellCount_Qt_Mpl.Ui_CellCount_Qt_Mpl):

    def __init__(self, parent=None):
    #def __init__(self, text, parent=None):
        super(CellCount_Qt_Mpl, self).__init__(parent)
        self.setupUi(self)
        
        # create live data feed object
        self.livefeed = LiveDataFeed()        
        # add title & legends for plots        
        self.setLegends()
          
    def on_start(self):
        # create timer object
        self.timer = QTimer()
        # connect signals with slots
        self.connect(self.timer, SIGNAL('timeout()'), self.on_timer)
        # update timer every ... seconds
        self.timer.start(frequency * 1000)
        
    def on_timer(self):
        """
        Executed periodically when the monitor update timer is fired.
        """
        
        # read the actual data
        data = np.loadtxt(options.filename, delimiter='\t')
        self.livefeed.add_data(data)
        
        """
        The livefeed is used to find out whether new data was received since the last update.
        If not, nothing is updated.
        """        
        
        if self.livefeed.has_new_data:
            data = self.livefeed.read_data()        
        
            # update bar plot
            self.barplot.axes.bar(data[:,0],data[:,1],width=0.5, bottom=0, color='r')
            self.barplot.axes.grid(True)
            self.barplot.axes.set_ylim(data[:,1].min()*0.9, data[:,1].max()*1.1)
            # update sum plot
            self.sumplot.axes.bar(data[:,0],data[:,2],width=0.5, bottom=0, color='g')
            self.sumplot.axes.grid(True)  
            #update plots
            self.setLegends()    
            self.barplot.draw()
            self.sumplot.draw()
            
    def setLegends(self):
        
        # add title & legends for the 1st plot        
        self.barplot.axes.set_title('Cell Count Current')        
        self.barplot.axes.set_xlabel('Frame')
        self.barplot.axes.set_ylabel('Cell Number')
        # add title & legends for the 2nd plot
        self.sumplot.axes.set_title('Cell Count Cumulative')        
        self.sumplot.axes.set_xlabel('Frame')
        self.sumplot.axes.set_ylabel('Sum of Cells')

def main():
    
    app = QApplication(sys.argv)
    form = CellCount_Qt_Mpl()
    form.show()
    form.on_start() # start data monitoring right away
    app.exec_()


if __name__ == "__main__":
    
    # configure parsing option for command line usage
    parser = optparse.OptionParser()
    parser.add_option('-f', '--file',
    action="store", dest="filename",
    help="query string", default="No filename passed.")
    # read command line arguments 
    options, args = parser.parse_args()
    print 'Filename:', options.filename        
    # this actually start the appication
    main()
