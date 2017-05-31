#!/usr/bin/env python
"""

"""

import matplotlib
matplotlib.use('WXAgg')

import numpy as np
import optparse
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg
from matplotlib.backends.backend_wx import NavigationToolbar2Wx

from matplotlib.figure import Figure
from wx import *


TIMER_ID = NewId()

class PlotFigure(Frame):

    def __init__(self):
        Frame.__init__(self, None, -1, "Dynamic Data Display - WX")

        self.fig = Figure((5,4), 100)
        self.canvas = FigureCanvasWxAgg(self, -1, self.fig)
        self.toolbar = NavigationToolbar2Wx(self.canvas)
        self.toolbar.Realize()

        # On Windows, default frame size behaviour is incorrect
        # you don't need this under Linux
        tw, th = self.toolbar.GetSizeTuple()
        fw, fh = self.canvas.GetSizeTuple()
        self.toolbar.SetSize(Size(fw, th))

        # Create a figure manager to manage things

        # Now put all into a sizer
        sizer = BoxSizer(VERTICAL)
        # This way of adding to sizer allows resizing
        sizer.Add(self.canvas, 1, LEFT|TOP|GROW)
        # Best to allow the toolbar to resize!
        sizer.Add(self.toolbar, 0, GROW)
        self.SetSizer(sizer)
        self.Fit()
        EVT_TIMER(self, TIMER_ID, self.onTimer)

    def init_plot_data(self):
        
        self.ax1 = self.fig.add_axes([0.15,0.15,0.8,0.8])
        self.ax1.grid(True)
        self.ax1.set_xlabel('Frame Number')
        self.ax1.set_ylabel('Cells detected')        

    def GetToolBar(self):
        # You will need to override GetToolBar if you are using an
        # unmanaged toolbar in your frame
        return self.toolbar

    def onTimer(self, evt):
        
        data = np.loadtxt(options.filename, delimiter='\t')        
        self.ax1.bar(data[:,0],data[:,1],width=0.7, bottom=0)
        self.ax1.set_xlim([data[0,0]-1,data[-1,0]+1])
        self.ax1.set_ylim([data[:,1].min()*0.9,data[:,1].max()*1.1])                          
        
        self.canvas.draw()

    def onEraseBackground(self, evt):
        # this is supposed to prevent redraw flicker on some X servers...
        pass

if __name__ == '__main__':
    
    # configure parsing option for command line usage
    parser = optparse.OptionParser()
    parser.add_option('-f', '--file',
    action="store", dest="filename",
    help="query string", default="spam")

    # read command line arguments 
    options, args = parser.parse_args()
    print 'Filename:', options.filename    
    
    app = PySimpleApp()
    frame = PlotFigure()
    frame.init_plot_data()

    # Initialise the timer - wxPython requires this to be connected to
    # the receiving event handler
    t = Timer(frame, TIMER_ID)
    t.Start(800)

    frame.Show()
    app.MainLoop()

