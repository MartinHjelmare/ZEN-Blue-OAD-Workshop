from pylab import *
import numpy as np
import optparse
import os
import time
from PyQt4.QtCore import *
from PyQt4.QtGui import *
# Qt4 bindings for core Qt functionalities (non-GUI)
from PyQt4 import QtCore
# Python Qt4 bindings for GUI objects
from PyQt4 import QtGui

# import the MainWindow widget from the converted .ui files
import ui_Ratio_Online_Plot2

frequency = 0.7 # update frequency in ms

class Ratio_Online_Plot(QtGui.QWidget, ui_Ratio_Online_Plot2.Ui_Ratio_Online_Plot):

    def __init__(self, parent=None):
        super(Ratio_Online_Plot, self).__init__(parent)
        self.setupUi(self)       
        # add title & legends for plots        
        self.setLegends()
        try:
            self.ct_last = os.stat(options.filename).st_mtime
        except:
            self.ct_last = 0.0
            
        self.nodatacount = 0
            
          
    def on_start(self):
        
        # create timer object
        self.timer = QTimer()
        # connect signals with slots
        self.connect(self.timer, SIGNAL('timeout()'), self.on_timer)
        # update timer every ... miliseconds
        self.timer.start(frequency * 1000)
        
    
    def on_timer(self):
        """
        Executed periodically when the monitor update timer is fired.
        """
        
        ## get file modification time        
        ct = os.stat(options.filename).st_mtime
        ## check if the time is bigger than the last one        
        if ct > self.ct_last:        
        
            # read the actual data
            data = np.genfromtxt(options.filename, dtype=float, invalid_raise=False,delimiter='\t')
            # update ratio plot               
            if (options.plotoption == 'all'):
                # plot all columns
                self.ratioplot.axes.plot(data[:,0],data[:,1:], 'r-', lw=2, label = 'Ratio')
            elif (options.plotoption != 'all'):
                # plot one column only - the index must be passed as a string
                cl = np.int(options.plotoption)
                self.ratioplot.axes.plot(data[:,0],data[:,cl:], 'ro-', lw=2, label = 'Ratio')
            
            # update plots   
            self.ratioplot.draw()
            self.ct_last = ct
            
        ## check if the current btime is equal to the last one
        elif ct == self.ct_last:
            
            print 'NO NEW DATA ANYMORE'
            self.nodatacount = self.nodatacount + 1
            
        ## close app and save figure if ... time no change was detected        
        if self.nodatacount > 10:
            
            ## read the data one more time and colourize the plot
            data = np.genfromtxt(options.filename, dtype=float, invalid_raise=False,delimiter='\t')
            self.ratioplot.axes.plot(data[:,0],data[:,1:], '-', lw=2, label = 'Ratio')
            self.ratioplot.draw()
            ## save figure before closing
            time.sleep(5)
            self.ratioplot.figure.savefig(savename)            
            sys.exit()
               
    ## format the figure            
    def setLegends(self):
       
        # add title & legends for ratio plot
        self.ratioplot.axes.set_title('Ratio CH1/CH2')        
        self.ratioplot.axes.set_xlabel('Frame')
        self.ratioplot.axes.set_ylabel('Ratio')
        self.ratioplot.axes.grid(True)
        self.ratioplot.axes.hold(True)

def main():
    
    app = QApplication(sys.argv)
    form = Ratio_Online_Plot()
    form.show()
    form.on_start() # start data monitoring right away
    app.exec_()

if __name__ == "__main__":
    
    # configure parsing option for command line usage
    parser = optparse.OptionParser()
    parser.add_option('-f', '--file',
    action="store", dest="filename",
    help="query string", default="No filename passed.")
    # plot options
    # 'all' --> plot all columns
    # '3' --> plot column 3 only
    parser.add_option('-p', '--plot',
    action="store", dest="plotoption",
    help="query string", default="No plotoption passed.")
    # read command line arguments 
    options, args = parser.parse_args()
    print 'Filename:', options.filename        
    savename = options.filename[:-4] + '.png'
    print 'Savename: ', savename    
    # this actually start the application
    main()
