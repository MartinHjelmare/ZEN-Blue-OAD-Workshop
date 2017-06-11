# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 10:34:13 2013

@author: Sebastian Rhode
"""

import numpy as np
import pandas as pd
#import optparse
import matplotlib.pyplot as plt
from matplotlib import cm
import csv


def ReadCSV(Filename, delim, rows2skip):

    """Reads a CSV file and returns it as a list of rows."""
    data = []
    for row in csv.reader(open(Filename), delimiter = delim):
        data.append(row)

    # 1st row = names of measured parameter
    # 2nd row = unit of parameter
    headers = data[0]
    numvar = len(headers)
    numrows = len(data) - rows2skip
    values = np.zeros((numrows,numvar))

    for i in range(0, numrows,1 ):
        # read in the data but skip the specified number of rows
        tmp = data[i + rows2skip]
        for k in range(0,len(tmp),1):
            # replace ',' by '.' in c ae there are any
            tmp[k] = str.replace(tmp[k], ',','.')
            try:
                values[i,k] = float(tmp[k])
                #print values[i,k]
            except:
                values[i,k] = np.NaN

    return values


def ReadPlateData(Filename, Nr, Nc, col2show, delim, rows2skip, parameter):

    # specify the delimiter for data files
    data = ReadCSV(Filename, delim, rows2skip)
    # show the well as a heat map
    ShowPlateData(data, Nr, Nc, col2show, parameter)

def ReadPlateData_Hinton(Filename, Nr,Nc, col2show, delim, rows2skip):

    # specify the delimiter for data files
    data = ReadCSV(Filename, delim, rows2skip)
    # show the well as a heat map
    ShowPlateData_Hinton(data, Nr, Nc, col2show)

def ReadPlateData_HintonC(Filename, Nr,Nc, col2show, delim, rows2skip):

    # specify the delimiter for data files
    data = ReadCSV(Filename, delim, rows2skip)
    # show the well as a heat map
    ShowPlateData_HintonC(data, Nr, Nc, col2show)


def ExtractLabels(Nr, Nc):

    # labeling schemes
    LabelX = ['1','2','3','4','5','6','7','8','9','10','11','12',
              '13','14','15','16','17','18','19','20','21','22','23','24',
              '25','26','27','28','29','30','31','32','33','34','35','36',
              '37','38','39','40','41','42','43','44','45','46','47','48',]

    LabelY = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P',
              'Q','R','S','T','U','V','W','X','Y','Z','AA','AB','AC','AD','AE','AF']

    Lx = LabelX[0:Nc]
    Ly = LabelY[0:Nr]
    #print "Label X: ",Lx
    #print "Label Y: ",Ly

    return Lx, Ly

def ShowPlateData(data, Nr, Nc, col2show, parameter):

    print(np.shape(data), Nr, Nc, col2show)    

    # reshape data to create 2D matrix
    WellData = data[:,col2show].reshape(Nr, Nc)
    [labelx, labely] = ExtractLabels(Nr, Nc)

    # create figure
    fig = plt.figure(figsize=(8,4), dpi=100)
    ax1 = fig.add_subplot(111)

    # set colormap
    cmap = cm.hot

    # show the well plate as an image
    cax = ax1.imshow(WellData, interpolation = 'nearest', cmap = cmap)

    # determine an appropiate font size
    if (Nr <= 32 and Nr > 16):
        fs = 7
    elif (Nr <= 16 and Nr > 8):
        fs = 9
    elif (Nr <= 8):
        fs = 11

    #format the display
    ax1.set_xticks(np.arange(0,Nc,1))
    ax1.set_xticklabels(labelx, fontsize=fs)
    ax1.set_yticks(np.arange(0,Nr,1))
    ax1.set_yticklabels(labely, fontsize=fs)
    ax1.set_title(parameter)
    ax1.set_ylim(ax1.get_ylim()[::-1])
    cbar = fig.colorbar(cax)

    # show graph
    plt.show()

    return fig


def test_pandas(filename, Nr, Nc, rows2skip, delim, col2show):

    # specify the delimiter for data files
    data = ReadCSV(filename, delim, rows2skip)
    # reshape data to create 2D matrix
    WellData = data[:,col2show].reshape(Nr, Nc)

    #Index= ['A','B','C','D','E','F','G','H']
    #Cols = ['1','2','3','4','5','6','7','8','9','10','11','12']
    Index, Cols = ExtractLabels(Nr, Nc)
    df = pd.DataFrame(WellData, index= Index, columns=Cols)

    return df
