"""
Author: Sebastian Rhode
Date: 2016_09_26
Version: 1.1

This macro illustrates the possibility to start Fiji from with an OAD macro to open
a CZI file and run a Fiji macro on the dataset.
The Result and the Summary data tables from Fiji are saved to disk.
Zen reads those data tables and converts them into Zen Data Tables.

1) Execute Experiment
2) Fiji reads the CZI and does the image analyis
3) the results from Fiji are imported into Zen as tables
4) Plot the data using Python script
"""

import sys
# add scriptfolder to path
sys.path.append(r'c:\Users\M1SRH\Documents\Projects\OAD\External_Python_Scripts_for_OAD')
import csv
import FijiTableTools2 as ft
from System.Diagnostics import Process
from System.IO import Directory, Path, File

plotpython = True

# remove documents
Zen.Application.Documents.RemoveAll(False)
Zen.Application.MacroEditor.ClearMessages()
# initialize Zen experiment
exp = ZenExperiment()
# load and execute experiment
exp.Load('Count_Cells_Start_Fiji_from_Macro_Pos.czexp')
image = Zen.Acquisition.Execute(exp)
Zen.Application.Documents.Add(image)

# define Fiji analysis script
filename = image.FileName # get the name of the current image data set
exeloc = 'C:\Users\Public\Documents\Fiji\ImageJ-win64.exe'
macro = '-macro Zen_Test\Count_Cells_EXP2_wellplate.ijm' # specify the Fiji macro one wants to use
option =  macro + ' ' + filename # 'glue' together the options 

# define status of Fiji
Fiji_Finished = False

# start Fiji and execute the macro
app = Process();
app.StartInfo.FileName = exeloc
app.StartInfo.Arguments = option
app.Start()

# check if Fiji already saved the data tables
while (Fiji_Finished == False):
    Fiji_Finished = File.Exists(filename[:-4] + '_Summary_Fiji.txt')

# read the data tables and convert them into Zen tables
rowoffset = 1 # skip ... lines
filename_R = filename[:-4] + '_Results_Fiji.txt'
filename_S = filename[:-4] + '_Summary_Fiji.txt'

# initialize ZenTable object
table_R = ZenTable()
table_S = ZenTable()

# Results Table
[ValuesArray_R, Legends_R, numvar_R, entries_R, coltypelist] = ft.Conv2Array(filename_R, rowoffset, '\t')
table_R = ft.CreateTable(ValuesArray_R, numvar_R, entries_R, Legends_R, 1, 'Result Table', coltypelist, table_R)
print 'Reading Table from Fiji: ', filename_R
# read the slice or frame lables separately since those are strings
labels = ft.Conv2List(filename_R, rowoffset, '\t', 1)
# add them to the Zen table to replace the NaNs
ft.AddLabels(table_R, labels, entries_R, 0)
Zen.Application.Documents.Add(table_R)

# Summary Table
[ValuesArray_S, Legends_S, numvar_S, entries_S,coltypelist] = ft.Conv2Array(filename_S, rowoffset, '\t')
table_S = ft.CreateTable(ValuesArray_S, numvar_S, entries_S, Legends_S, 0, 'Summary Table', coltypelist, table_S)
print 'Reading Table from Fiji: ', filename_S
Zen.Application.Documents.Add(table_S)

if plotpython == True:

    # plot heatmap
    pythonexe = r'c:\Anaconda3\python.exe'
    script = r'c:\Users\M1SRH\Documents\Projects\OAD\External_Python_Scripts_for_OAD\plot_well_from_OAD.py'
    params = ' -f ' + filename_S
    
    # start the data display script as an external application
    app = Process();
    app.StartInfo.FileName = pythonexe
    app.StartInfo.Arguments = script + params
    print 'Starting external plotting script: ', script
    app.Start()
