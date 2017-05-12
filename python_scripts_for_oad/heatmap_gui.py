#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, print_function, absolute_import, unicode_literals)
import sys
import numpy as np
import argparse
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4 import QtGui
import matplotlib.cm as cm
import mpl
import time
import os

class MyGUI(QtGui.QDialog):

    def __init__(self, **kwargs):
        super(MyGUI, self).__init__(**kwargs)

        #self.setGeometry(600, 480, 600, 480)
        #self.move(QtGui.QApplication.desktop().screen().rect().center() - self.rect().center())
        self.setWindowTitle('Wellplate Online Heatmap')

        vertical_layout = QtGui.QVBoxLayout(self)
        self.figure_widget = mpl.MPLWidget(tight_layout=True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.figure_widget.sizePolicy().hasHeightForWidth())
        self.figure_widget.setSizePolicy(sizePolicy)
        vertical_layout.addWidget(self.figure_widget)

        try:
            self.ct_last = os.stat(filename).st_mtime
        except:
            self.ct_last = 0.0

        self.nodatacount = 0

        # Create a matplotlib axes.
        # self.ax = self.figure_widget.figure.add_subplot(111)
        self.ax = self.figure_widget.figure.add_axes([0.075, 0.1, 0.75, 0.85])
        self.cax = self.figure_widget.figure.add_axes([0.85, 0.1, 0.075, 0.85])
        self.ax.set_title('Online Heatmap by Experiment Feedback')

        # read in cell numbers
        self.Nr = numrows
        self.Nc = numcolumns
        # create matrix which will contain the number of counted cells
        self.well = self.create_matrix(numrows=self.Nr, numcols=self.Nc)
        self.labelx, self.labely = self.create_labels(numrows=self.Nr, numcols=self.Nc)
        # add title & legends for plots
        self.setlabels

        return None

    def on_start(self):

        # create timer object
        self.timer = QTimer()
        # connect signals with slots
        self.connect(self.timer, SIGNAL('timeout()'), self.on_timer)
        # update timer every ... seconds
        self.timer.start(frequency * 1000.0)

    def on_timer(self):
        """
        Executed periodically when the monitor update timer is fired.
        """

        # get file modification time
        try:
            ct = os.stat(filename).st_mtime
        except:
            ct = 0.0
        # check if the time is bigger than the last one
        if ct > self.ct_last:
            # read the actual data
            data = np.genfromtxt(filename, dtype=float, invalid_raise=False, delimiter='\t', usecols=(1, 2, 3))
            try:
                for i in range(0, data.shape[0]):
                    cn = data[i, 0]
                    col = data[i, 1]-1  # numpy is zero-based ...
                    row = data[i, 2]-1
                    # update well matrix at the correct position
                    self.well[row, col] = cn

                # do the plot
                self.im = self.ax.imshow(self.well, vmin=data[:, 0].min(), vmax=data[:, 0].max(), cmap=cm.jet, interpolation='nearest')
                #self.figure_widget.figure.colorbar(self.im, cax=self.cax, orientation='vertical')
                self.setlabels()
                self.figure_widget.draw()
                self.ct_last = ct
            except:
                print('Reading data did not work or update might be too fast.')


        # check if the current time is equal to the last one
        elif ct == self.ct_last:

            print('No new datapoints.')
            self.nodatacount = self.nodatacount + 1

        # close app and save figure if ... time no change was detected
        if self.nodatacount > 10:
            self.figure_widget.draw()
            # save figure before closing
            time.sleep(5)
            self.figure_widget.figure.savefig(savename)
            sys.exit()

    def setlabels(self):

        self.ax.set_xticks(np.arange(0, self.Nc, 1))
        self.ax.set_xticklabels(self.labelx)
        self.ax.set_yticks(np.arange(0, self.Nr, 1))
        self.ax.set_yticklabels(self.labely)
        #self.ax.set_title('Cell Count per Well')
        self.figure_widget.figure.colorbar(self.im, cax=self.cax, orientation='vertical')
        self.figure_widget.draw()

        return None

    def create_labels(self, numrows=8, numcols=12):

        # labeling schemes
        LabelX = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12',
                  '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24']

        LabelY = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']

        labelx = LabelX[0:numcols]
        labely = LabelY[0:numrows]

        return labelx, labely

    def create_matrix(self, numrows=8, numcols=12):

        # create matrix which will contain the number of counted cells
        well = np.zeros([numrows, numcols])

        return well


def main():


    app = QtGui.QApplication(sys.argv)
    window = MyGUI()
    window.on_start()
    window.exec_()

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Read Filename and Parameters.')
    parser.add_argument('-f', action="store", dest='filename')
    parser.add_argument('-c', action="store", dest='columns')
    parser.add_argument('-r', action="store", dest='rows')
    parser.add_argument('-fqr', action="store", dest='frequency')

    # get the arguments
    args = parser.parse_args()
    filename = args.filename
    savename = filename[:-4] + '.png'
    numrows = np.int(args.rows)
    numcolumns = np.int(args.columns)
    frequency = np.float(args.frequency)
    print('Filename: ', args.filename)
    print('Savename: ', savename)
    print('Number of rows: ', numrows)
    print('Number of columns: ', numcolumns)
    print('Frequency [s]: ', frequency)

    # this actually start the application
    main()
