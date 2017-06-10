# coding: utf-8

import pandas as pd
import wellplate_tools_pandas_py3 as wtp
import matplotlib.pyplot as plt
import argparse
import os

parser = argparse.ArgumentParser(description='Read Filename and Parameters.')
parser.add_argument('-f', action="store", dest='filename')
parser.add_argument('-w', action="store", dest='platetype')
parser.add_argument('-p', action="store", dest='parameter')
parser.add_argument('-sp', action="store", dest='showplot')


# get the arguments
args = parser.parse_args()
print('CSV Filename: ', args.filename)
print('PlateType: ', args.platetype)
print('Parameter to display: ', args.parameter)

############################ TEST #########################################

# define the filenames
filename_single = args.filename
Nr, Nc = wtp.getrowandcolumn(args.platetype)

# THIS PARAMETER LIST DEPENDS ON THE ACTUAL ZEN Image Analysis Setting (CZIAS) AND MUST BE ADAPTED
parameter_list = ['DAPI_Mean', 'Area', 'Perimeter', 'Roundness', 'FeretRatio']

# define number of measured parameters beside the actual object number
num_param = len(parameter_list)

# read the CSV table containing all the single object data for
# further "in-depth" analysis
df_single = pd.read_csv(filename_single, sep=';')

# rename columns and correct data types
df_single = wtp.rename_col_fromcsv_single(df_single, parameter_list)

# show part of dataframe
df_single[:3]

# use statistics --> we just calculate the mean values
# for a wells to be displayed inside the heatmaps.
# currently implemented are mean, median, min, max.
stf = 'mean'

# create a dictionary containing a dataframe for every measure parameters
# as a heatmap and a dictionary containing the mean values for all wells
# containing actual data points.
heatmap_dict, well_dict = wtp.fill_heatmaps(df_single, num_param, Nr, Nc, statfunc=stf, showbar=False, verbose=False)

# show all keys
#print heatmap_dict.keys()

# define parameters to display the heatmap
parameter2display = args.parameter
hm = heatmap_dict[parameter2display]

# show the heatmap for a single parameter
wtp.showheatmap(hm, parameter2display, fontsize_title=16, fontsize_label=12,
                colormap='Blues', save=True, filename=filename_single)

# show all heatmaps
wtp.showheatmap_all(heatmap_dict, [3, 2], fontsize_title=14, fontsize_label=12,
                    colormap='Blues', save=True, filename=filename_single)

# modify the layout so the the axis labels and titles do not overlap
if args.showplot == 'True':
    plt.tight_layout()
    # show plots
    plt.show()

print('Exiting ...')
os._exit(42)
