# -*- coding: utf-8 -*-
"""
Created on Wed May 29 10:03:26 2013

@author: M1SRH
"""

import numpy as np
import argparse
import matplotlib.pyplot as plt
import wellplate as wp

# configure parsing option for command line usage
parser = argparse.ArgumentParser(description='Read Fiji Data Tables.')
parser.add_argument('-f', action="store", dest='filename')

# get the arguments
args = parser.parse_args()

# call the plot script
wp.ReadPlateData(args.filename, 8, 12, 1, '\t', 1, 'Object Number')
