### -------------------- PreScript ---------------------------------------------- ###


lastindex = 0
sumcells = 0
filename = '-f ' + ZenService.Experiment.ImageFileName[:-4] + '_Log.txt'
#script = 'dynamic_plot_bar.py'
script = 'CellCount_Qt_Mpl2.py'
#script = 'dynamic_plotting_qwt.py'
ZenService.Xtra.System.ExecuteExternalProgram(script, filename)


### -------------------- LoopScript --------------------------------------------- ###


index = ZenService.Analysis.Cells.ImageAcquisitionTime

if (index < lastindex or index > lastindex):
    frame = ZenService.Analysis.Cells.ImageIndexTime
    cn = ZenService.Analysis.Cells.RegionsCount
    sumcells = sumcells + cn
    # create the logfile with the required columns
    if (script == 'dynamic_plot_bar.py' or script == 'dynamic_plotting_qwt.py'):
        ZenService.Xtra.System.AppendLogLine(str(frame) + '\t' + str(cn))
    elif (script == 'CellCount_Qt_Mpl2.py'):
        ZenService.Xtra.System.AppendLogLine(str(frame) + '\t' + str(cn) + '\t' + str(sumcells))

    lastindex = index


### -------------------- PostScript --------------------------------------------- ###


