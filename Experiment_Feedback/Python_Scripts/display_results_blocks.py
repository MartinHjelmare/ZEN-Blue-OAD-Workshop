# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 11:26:27 2012

@author: m1srh
"""
import numpy as np
import optparse
import matplotlib.pyplot as plt

# configure parsing option for command line usage
parser = optparse.OptionParser()

parser.add_option('-f', '--file',
    action="store", dest="filename",
    help="query string", default="spam")

# read command line arguments 
options, args = parser.parse_args()

print 'Filename:', options.filename
# load data
data = np.loadtxt(options.filename, delimiter='\t', skiprows=1)
# create figure
figure = plt.figure(figsize=(8,5), dpi=100)
ax1 = figure.add_subplot(111)

maxindex = int(data[:,2].max())
print 'Number of Blocks: ',maxindex

for i in  range(0,maxindex):
    
    data2plot = data[data[:,2] == i+1]
    ax1.plot(data2plot[:,0],data2plot[:,1],'-o',lw=2,label='Block'+str(i+1))

ax1.grid(True)
ax1.legend()
ax1.set_xlim([0,data[:,0].max()+1])
ax1.set_ylim([data[:,1].min()*0.9,data[:,1].max()*1.1])
ax1.set_xlabel('Frame Number')
ax1.set_ylabel('Cells detected')

# show graph
plt.show()