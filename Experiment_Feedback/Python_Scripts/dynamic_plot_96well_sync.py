import sys, time, os, gc
import matplotlib
matplotlib.use('WXAgg')

from matplotlib import rcParams
import matplotlib.cm as cm
import numpy as np
import optparse
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg
from matplotlib.backends.backend_wx import NavigationToolbar2Wx
from matplotlib.figure import Figure
from wx import *

TIMER_ID = NewId()

class PlotFigure(Frame):

    def __init__(self):
        Frame.__init__(self, None, -1, "96 Well Plate - Dynamic Heat Map")

        self.fig = Figure((6,4), 100)
        self.canvas = FigureCanvasWxAgg(self, -1, self.fig)

        sizer = BoxSizer(VERTICAL)
        sizer.Add(self.canvas, 1, LEFT|TOP|GROW)
        self.Fit()
        EVT_TIMER(self, TIMER_ID, self.onTimer)

    def init_plot_data(self):
        
        # read in cell numbers
        self.Nr = int(options.rows)
        self.Nc = int(options.columns)
        print "Number of Wells: ",self.Nr*self.Nc              
        # initialize data array and plot for the 1st time
        self.data = np.zeros([self.Nr * self.Nc])
        # create matrix which will contain the number of counted cells
        self.well = np.zeros([self.Nr,self.Nc])

        # labeling schemes        
        LabelX = ['1','2','3','4','5','6','7','8','9','10','11','12',
                  '13','14','15','16','17','18','19','20','21','22','23','24']
        
        LabelY = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P'] 
        
        labelx = LabelX[0:self.Nc]
        labely = LabelY[0:self.Nr]

        print "Label X: ",labelx
        print "Label Y: ",labely        
        
        self.ax1 = self.fig.add_axes([0.075,0.1,0.75,0.85])
        self.cax = self.fig.add_axes([0.85,0.1,0.075,0.85])
        self.im = self.ax1.imshow(self.well, cmap=cm.jet, interpolation='nearest')
        self.fig.colorbar(self.im, cax=self.cax, orientation='vertical')
        self.ax1.set_xticks(np.arange(0,self.Nc,1))
        self.ax1.set_xticklabels(labelx)
        self.ax1.set_yticks(np.arange(0,self.Nr,1))
        self.ax1.set_yticklabels(labely)
        self.ax1.set_title('Cell Count per Well')    
        self.figure_saved = False
            
    def onTimer(self, evt):
        
        datain = np.loadtxt(options.filename, delimiter='\t', usecols=(1,2,3))
        
        try:        
            for i in range(0,datain.shape[0]):        
                # only read the last entry from the data --> this is the last data point        
                cn = datain[i,0]
                col = datain[i,1]-1 # numpy is zero-based ...   
                row = datain[i,2]-1
                # update well matrix at the correct position
                self.well[row, col] = cn
            
            # do the plot            
            self.im = self.ax1.imshow(self.well, vmin = datain[:,0].min(),
                                      vmax = datain[:,0].max(), cmap=cm.jet, interpolation='nearest') 
            self.fig.colorbar(self.im, cax=self.cax, orientation='vertical')
            self.canvas.draw()         
            
        except:
            print 'No data to display yet ...'
            
        # save plot only when done and only once
        if (datain.shape[0] == self.Nr * self.Nc and self.figure_saved == False):
            self.fig.savefig(savename)
            self.figure_saved = True
        

if __name__ == '__main__':
    
    # configure parsing option for command line usage
    parser = optparse.OptionParser()
    
    parser.add_option('-f', '--file',
    action="store", dest="filename",
    help="query string", default="No filename passed.")
    
    parser.add_option('-c', '--columns',
    action="store", dest="columns",
    help="query string", default="No number of columns passed.")
    
    parser.add_option('-r', '--rows',
    action="store", dest="rows",
    help="query string", default="No number of rows passed.")

    # read command line arguments 
    options, args = parser.parse_args()     
    savename = options.filename[:-4] + '.png'
           
    print 'Filename: ', options.filename
    print 'Savename: ', savename    
    
    app = PySimpleApp()
    frame = PlotFigure()
    frame.init_plot_data()

    # Initialise the timer - wxPython requires this to be connected to
    # the receiving event handler
    t = Timer(frame, TIMER_ID)
    t.Start(500)

    frame.Show()
    app.MainLoop()
