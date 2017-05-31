### -------------------- PreScript ---------------------------------------------- ###


filename = '-f ' + ZenService.Experiment.ImageFileName[:-4] + '_Log.txt'
# !!! watch the space before the -c in params !!!
params = ' -fqr 1.0 -s True' # specify update frequency and saveoption
script = r'c:\TFS\Doc\3-ZIS\2-ProjectManagement\Teilprojekte\Teilprojekt_Dokumentation\Temporary Doku (raw data)\Rhode\ExpFeedback\Python_Scripts\barplot_gui.py'
# this is a external python application
ZenService.Xtra.System.ExecuteExternalProgram(script, filename + params)
# create logfile header
logfile = ZenService.Xtra.System.AppendLogLine('frame\tarea_t\tarea_p')



### -------------------- LoopScript --------------------------------------------- ###


# get the current well name, column idex, row index and position index
frame = ZenService.Experiment.CurrentTimePointIndex
#reltime = ZenService.Analysis.Scratch.ImageRelativeTime

# get area parameters for the scratchnumber of cells from current image
area_t = ZenService.Analysis.Scratch.RegionsArea
area_p = ZenService.Analysis.Scratch.RegionsAreaPercentage

# create logfile
logfile = ZenService.Xtra.System.AppendLogLine(str(frame)+'\t'+str(area_t) + '\t'+str(area_p))



### -------------------- PostScript --------------------------------------------- ###


# open logfile
ZenService.Xtra.System.ExecuteExternalProgram(logfile, r'C:\Program Files (x86)\Notepad++\notepad++.exe')
