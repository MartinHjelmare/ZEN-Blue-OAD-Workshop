### -------------------- PreScript ---------------------------------------------- ###


filename = '-f ' + ZenService.Experiment.ImageFileName[:-4] + '_Log.txt'
# !!! watch the space before the -c in params !!!
params = ' -c 24 -r 16 -fqr 0.8' # specify well plate format, e.g. 12 x 8 = 96 Wells
script = r'c:\TFS\Doc\3-ZIS\2-ProjectManagement\Teilprojekte\Teilprojekt_Dokumentation\Temporary Doku (raw data)\Rhode\ExpFeedback\Python_Scripts\heatmap_gui.py'
# this is a external python application
ZenService.Xtra.System.ExecuteExternalProgram(script, filename + params)



### -------------------- LoopScript --------------------------------------------- ###


# get number of cells from current image
cn = ZenService.Analysis.All.RegionsCount
# get the current well name, column idex, row index and position index
well = ZenService.Analysis.All.ImageSceneContainerName
col = ZenService.Analysis.All.ImageSceneColumn
row = ZenService.Analysis.All.ImageSceneRow
# create logfile
logfile = ZenService.Xtra.System.AppendLogLine(str(well)+'\t'+str(cn)+'\t'+str(col)+'\t'+str(row))


### -------------------- PostScript --------------------------------------------- ###


# open logfile
ZenService.Xtra.System.ExecuteExternalProgram(logfile, r'C:\Program Files (x86)\Notepad++\notepad++.exe')