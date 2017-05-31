###   PreScript   ###

filename = '-f ' + ZenService.Experiment.ImageFileName[:-4] + '_Log.txt'
# !!! watch the space before the -c in params !!!
params = ' -c 12 -r 8' # specify well plate format, e.g. 12 x 8 = 96 Wells
script = 'dynamic_plot_96well_sync.py' ## this is a external python application
ZenService.Xtra.System.ExecuteExternalProgram(script, filename + params)

###   LoopScript ###

# get number of cells from current image
cn = ZenService.Analysis.AllCells.RegionsCount
# get the current well name, column idex, row index and position index
well = ZenService.Analysis.AllCells.ImageSceneContainerName
col = ZenService.Analysis.AllCells.ImageSceneColumn
row = ZenService.Analysis.AllCells.ImageSceneRow
# create logfile
logfile = ZenService.Xtra.System.AppendLogLine(str(well)+'\t'+str(cn)+'\t'+str(col)+'\t'+str(row))

###   PostScript   ###

# open logfile
ZenService.Xtra.System.ExecuteExternalProgram(logfile, r'C:\Program Files (x86)\Notepad++\notepad++.exe')