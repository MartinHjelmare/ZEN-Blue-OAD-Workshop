###   PreScript   ###

# enter blocks to analyze here
blocks2do = [1,3]
# enter blocks to do nothing
blocksnot2do = [2]
# create header for logfile
logfile = ZenService.Xtra.System.AppendLogLine('Frame\tCells\tBlock')

###   LoopScript ###

# get current block index
block = ZenService.Experiment.CurrentBlockIndex

if block in blocks2do:

    # get current frame number
    frame = ZenService.Experiment.CurrentTimePointIndex
    cn = ZenService.Analysis.Cells.RegionsCount
    logfile = ZenService.Xtra.System.AppendLogLine(str(frame)+'\t'+str(cn)+'\t'+str(block))

elif block in blocksnot2do:
    ZenService.Xtra.System.PlaySound()


###   PostScript   ###

ZenService.Xtra.System.ExecuteExternalProgram(r'C:\Program Files (x86)\Notepad++\notepad++.exe', logfile)