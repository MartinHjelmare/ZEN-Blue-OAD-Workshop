#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, print_function, absolute_import, unicode_literals)
import sys
import numpy as np
import argparse
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
import matplotlib.cm as cm
import mpl
import time
import os
import seaborn as sns
import pandas as pd

class MyGUI(QtGui.QDialog):

    def __init__(self, **kwargs):
        super(MyGUI, self).__init__(**kwargs)

        #self.setGeometry(600, 480, 600, 480)
        #self.move(QtGui.QApplication.desktop().screen().rect().center() - self.rect().center())
        self.setWindowTitle('Wound Healing Assay - Online Plot')

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

        # Create a matplotlib axes
        self.ax1 = self.figure_widget.figure.add_subplot(211)
        self.ax2 = self.figure_widget.figure.add_subplot(212)
        self.ax1.set_title('Wound Healing Assay - Scratch Area [%]')
        self.ax2.set_title('Wound Healing Assay - Scratch Relative Delta [%]')

        return None

    def on_start(self):

        # create timer object upon the start of the application
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

            # read the actual data and store them into pandas data frame
            df = pd.read_csv(filename, sep='\t', header=0)

            # do some stats and normalization on the data
            df['area_t_norm'] = df['area_t']/df['area_t'].max()
            df['area_p_norm'] = df['area_p']/df['area_p'].max()*100

            # read first value of area_p_norm to be used a reference
            area_p_ref = df['area_p_norm'][0]

            # calculate the difference relative to the 1st data point last datapoint
            df['area_p_delta'] = df['area_p_norm'] - area_p_ref

            # calculate the difference relative to the previous data point
            df['area_p_delta_diff'] = df['area_p_delta'].diff()

            try:
                # do the plot using columns from the dataframe
                self.ax1 = sns.barplot(x='frame', y='area_p_delta', palette='Blues_d', data=df, ax=self.ax1)
                #self.ax1 = sns.barplot(x='frame', y='area_p_norm', palette='Blues_d', data=df, ax=self.ax1)
                self.ax2 = sns.barplot(x='frame', y='area_p_delta_diff', palette='BuGn_d', data=df, ax=self.ax2)

                # update the plot and the time since the last modification
                self.figure_widget.draw()
                self.ct_last = ct
            except:
                print('Reading data did not work or update might be too fast.')


        # check if the current time is equal to the last one
        elif ct == self.ct_last:

            print('No new datapoints.')
            self.nodatacount = self.nodatacount + 1

        # close app and save figure if ... time no change was detected
        if self.nodatacount > 4:
            self.figure_widget.draw()
            # save figure before closing
            time.sleep(3)
            if saveopt == 'True':
                self.figure_widget.figure.savefig(savename)
            sys.exit()

###############################################################################

def main():

    app = QtGui.QApplication(sys.argv)
    window = MyGUI()
    window.on_start()
    window.exec_()

if __name__ == "__main__":

    # setup commandline parameters
    parser = argparse.ArgumentParser(description='Read Filename and Parameters.')
    parser.add_argument('-f', action="store", dest='filename')
    parser.add_argument('-fqr', action="store", dest='frequency')
    parser.add_argument('-s', action="store", dest='saveoption')

    # get the arguments
    args = parser.parse_args()

    filename = args.filename
    print('Datalog Filename: ', args.filename)

    saveopt = args.saveoption
    print('SaveOption: ', saveopt)
    if saveopt == 'True':
        savename = filename[:-4] + '.png'
        print('Savename: ', savename)

    frequency = np.float(args.frequency)
    print('Update Frequency [s]: ', frequency)

    # this actually starts the application
    main()
