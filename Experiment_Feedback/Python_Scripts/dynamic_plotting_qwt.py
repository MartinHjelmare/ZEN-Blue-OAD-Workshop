""" 
A simple demonstration that plots live data using PyQwt.
When the monitor is active, you can turn the 'Update speed' knob
to control the frequency of screen updates.

Eli Bendersky (eliben@gmail.com)
License: this code is in the public domain

adapted by Sebastian Rhode
Last modified: 09.11.2012
"""

import numpy as np
import optparse
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import PyQt4.Qwt5 as Qwt
import Queue

from livedatafeed import LiveDataFeed

class DataMonitor(QMainWindow):
    def __init__(self, parent=None):
        super(DataMonitor, self).__init__(parent)
        
        self.monitor_active = False
        self.livefeed = LiveDataFeed()
        self.timer = QTimer()    
        self.create_menu()
        self.create_main_frame()      
        self.create_status_bar()
        
    def make_data_box(self, name):
        label = QLabel(name)
        qle = QLineEdit()
        qle.setEnabled(False)
        qle.setFrame(False)
        return (label, qle)
        
    def create_plot(self):
        
        plot = Qwt.QwtPlot(self)
        plot.setCanvasBackground(Qt.black)
        plot.setAxisTitle(Qwt.QwtPlot.xBottom, 'Frame')
        plot.setAxisScale(Qwt.QwtPlot.xBottom, 0, 10, 1)
        plot.setAxisTitle(Qwt.QwtPlot.yLeft, 'Number of Cells')
        plot.setAxisScale(Qwt.QwtPlot.yLeft, 0, 200, 40)
        plot.replot()
        
        curve = Qwt.QwtPlotCurve('')
        curve.setRenderHint(Qwt.QwtPlotItem.RenderAntialiased)
        pen = QPen(QColor('limegreen'))
        pen.setWidth(2)
        curve.setPen(pen)
        curve.attach(plot)
        curve.setSymbol(Qwt.QwtSymbol(Qwt.QwtSymbol.Ellipse, pen.color(), pen.color(), QSize(10, 10)))
        
        return plot, curve

    def create_knob(self):
        knob = Qwt.QwtKnob(self)
        knob.setRange(0, 20, 0, 1)
        knob.setScaleMaxMajor(10)
        knob.setKnobWidth(50)
        knob.setValue(2)
        return knob
        
    def create_status_bar(self):
        self.status_text = QLabel('Monitor idle')
        self.statusBar().addWidget(self.status_text, 1)

    def create_main_frame(self):

        self.plot, self.curve = self.create_plot()       
        self.updatespeed_knob = self.create_knob()
        self.connect(self.updatespeed_knob, SIGNAL('valueChanged(double)'),
            self.on_knob_change)
        self.knob_l = QLabel('Update speed = %s (Hz)' % self.updatespeed_knob.value())
        self.knob_l.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        knob_layout = QVBoxLayout()
        knob_layout.addWidget(self.updatespeed_knob)
        knob_layout.addWidget(self.knob_l)
        
        plot_layout = QVBoxLayout()
        plot_layout.addWidget(self.plot)
        plot_layout.addLayout(knob_layout)
        
        plot_groupbox = QGroupBox('Data Plot')
        plot_groupbox.setLayout(plot_layout)
        
        # Main frame and layout
        #
        self.main_frame = QWidget()
        main_layout = QVBoxLayout()
        main_layout.addWidget(plot_groupbox)
        main_layout.addStretch(1)
        self.main_frame.setLayout(main_layout)
        
        self.setCentralWidget(self.main_frame)
        self.set_actions_enable_state()

    def create_menu(self):
        
        self.file_menu = self.menuBar().addMenu("&File")
        
        self.start_action = self.create_action("&Start monitor",
            shortcut="Ctrl+M", slot=self.on_start, tip="Start the data monitor")
        self.stop_action = self.create_action("&Stop monitor",
            shortcut="Ctrl+T", slot=self.on_stop, tip="Stop the data monitor")
        exit_action = self.create_action("E&xit", slot=self.close, 
            shortcut="Ctrl+X", tip="Exit the application")
        
        self.start_action.setEnabled(True)
        self.stop_action.setEnabled(False)
        
        self.add_actions(self.file_menu, 
            (   self.start_action, self.stop_action,
                None, exit_action))
        self.add_actions(self.file_menu, (None, exit_action))

    def set_actions_enable_state(self):
        
        start_enable = not self.monitor_active
        stop_enable = self.monitor_active
        
        self.start_action.setEnabled(start_enable)
        self.stop_action.setEnabled(stop_enable)

    def on_stop(self):
        
        # Stop the data monitor
        self.monitor_active = False
        self.timer.stop()
        self.set_actions_enable_state()
        
        self.status_text.setText('Monitor idle')
    
    def on_start(self):
        
        #Start the data monitor
        self.data_q = Queue.Queue()
        self.monitor_active = True
        self.set_actions_enable_state()
        self.timer = QTimer()
        self.connect(self.timer, SIGNAL('timeout()'), self.on_timer)
        
        update_freq = self.updatespeed_knob.value()
        if update_freq > 0:
            self.timer.start(1000.0 / update_freq)
        
        self.status_text.setText('Monitor running')
    
    def on_timer(self):
        """ Executed periodically when the monitor update timer
            is fired.
        """
        self.ReadData()
        self.update_monitor()

    def on_knob_change(self):
        """ When the knob is rotated, it sets the update interval
            of the timer.
        """
        update_freq = self.updatespeed_knob.value()
        self.knob_l.setText('Update speed = %s (Hz)' % self.updatespeed_knob.value())

        if self.timer.isActive():
            update_freq = max(0.01, update_freq)
            self.timer.setInterval(1000.0 / update_freq)

    def update_monitor(self):
        """ Updates the state of the monitor window with new 
            data. The livefeed is used to find out whether new
            data was received since the last update. If not, 
            nothing is updated.
        """
        if self.livefeed.has_new_data:
            data = self.livefeed.read_data()           
            
            try:            
                xdata = data[:,0]
                ydata = data[:,1]
                
                # scale axis automatically              
                self.plot.setAxisScale(Qwt.QwtPlot.xBottom, xdata.min()*0.9, xdata.max()*1.1)
                self.plot.setAxisScale(Qwt.QwtPlot.yLeft, ydata.min()*0.9, ydata.max()*1.1)
                self.curve.setData(xdata, ydata)
                self.plot.replot()
            
            except:
                #print 'No data yet ...'
                test = 1 # just to do something, because otherwise error (ugly, but works ...)
            
    def ReadData(self):
        
        #Called periodically by the update timer to read data
        data = np.loadtxt(options.filename, delimiter='\t')
        self.livefeed.add_data(data)
    
    # The following two methods are utilities for simpler creation
    # and assignment of actions
    #
    def add_actions(self, target, actions):
        for action in actions:
            if action is None:
                target.addSeparator()
            else:
                target.addAction(action)

    def create_action(  self, text, slot=None, shortcut=None, 
                        icon=None, tip=None, checkable=False, 
                        signal="triggered()"):
        action = QAction(text, self)
        if icon is not None:
            action.setIcon(QIcon(":/%s.png" % icon))
        if shortcut is not None:
            action.setShortcut(shortcut)
        if tip is not None:
            action.setToolTip(tip)
            action.setStatusTip(tip)
        if slot is not None:
            self.connect(action, SIGNAL(signal), slot)
        if checkable:
            action.setCheckable(True)
        return action


def main():
    
    app = QApplication(sys.argv)
    form = DataMonitor()
    form.show()
    form.on_start() # start data monitoring right away
    app.exec_()


if __name__ == "__main__":
    
    # configure parsing option for command line usage
    parser = optparse.OptionParser()
    parser.add_option('-f', '--file',
    action="store", dest="filename",
    help="query string", default="spam")
    # read command line arguments 
    options, args = parser.parse_args()
    print 'Filename:', options.filename        
    # this actually start the appication
    main()