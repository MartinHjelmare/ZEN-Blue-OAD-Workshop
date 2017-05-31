### -------------------- PreScript ---------------------------------------------- ###


lastindex = 0
filename = '-f ' + ZenService.Experiment.ImageFileName[:-4] + '_Log.txt'
# !!! watch the space before the -c !!! Important !!!
params = ' -c 12 -r 8' # specify well plate format, e.g. 12 x 8 = 96 Wells
script = 'dynamic_plot_96well.py'
ZenService.Xtra.System.ExecuteExternalProgram(script, filename + params)


### -------------------- LoopScript --------------------------------------------- ###


index = ZenService.Analysis.Cells.ImageAcquisitionTime

if (index < lastindex or index > lastindex):
    cn = ZenService.Analysis.Cells.RegionsCount
    frame = ZenService.Analysis.Cells.ImageIndexTime
    ZenService.Xtra.System.AppendLogLine(str(frame)+'\t'+str(cn))
    lastindex = index


### -------------------- PostScript --------------------------------------------- ###


