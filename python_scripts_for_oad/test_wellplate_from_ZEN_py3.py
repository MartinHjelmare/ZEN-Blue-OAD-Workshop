# coding: utf-8

import pandas as pd
import wellplate_tools_pandas_py3 as wpt
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser(description='Read Filename and Parameters.')
parser.add_argument('-f', action="store", dest='filename')
# get the arguments
args = parser.parse_args()
print('CSV Filename: ', args.filename)

############################ TEST #########################################

# define the filenames
filename_single = args.filename

# define wellplate type
Nr = 8
Nc = 12

# define number of measured parameters beside the actual object number
num_param = 5

# THIS PARAMETER LIST DEPENDS ON THE ACTUAL ZEN Image Analysis Setting (CZIAS) AND MUST BE ADAPTED
parameter_list = ['DAPI_Mean', 'Area', 'Perimeter', 'Roundness', 'FeretRatio']

# read the CSV table containing all the single object data for
# further "in-depth" analysis
df_single = pd.read_csv(filename_single, sep=';')

# rename columns and correct data types
df_single = wpt.rename_col_fromcsv_single(df_single, parameter_list)

# show part of dataframe
df_single[:3]

# use statistics --> we just calculate the mean values
# for a wells to be displayed inside the heatmaps.
# currently implemented are mean, median, min, max.
stf = 'mean'

# create a dictionary containing a dataframe for every measure parameters
# as a heatmap and a dictionary containing the mean values for all wells
# containing actual data points.
heatmap_dict, well_dict = wpt.fill_heatmaps(df_single, num_param, Nr, Nc, statfunc=stf, showbar=False, verbose=False)

# show all keys
#print heatmap_dict.keys()

# define parameters to display the heatmap
parameter2display = 'ObjectNumber'
hm = heatmap_dict[parameter2display]

# show the heatmap for a single parameter
wpt.showheatmap(hm, parameter2display, fontsize_title=16, fontsize_label=12,
                colormap='Blues', save=True, filename=filename_single)

# show all heatmaps
wpt.showheatmap_all(heatmap_dict, [3, 2], fontsize_title=14, fontsize_label=12,
                    colormap='Blues', save=True, filename=filename_single)

# modify the layout so the the axis labels and titles do not overlap
plt.tight_layout()
# show plots
plt.show()


                    
            
                
        





