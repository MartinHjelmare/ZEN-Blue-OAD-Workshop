### -------------------- PreScript ---------------------------------------------- ###


# here we initialize some kind of index counter by setting it to Zero.
lastindex = 0
action_taken = False
RF = 1.5 # ratio activation factor --> when ratio/initial_ration > RF --> Activation Event
interval_initial = 1000.0 # this is the initial exposure time
interval_fast    = 200.0  # desired FASTER exposure time after an activation event was detected


### -------------------- LoopScript --------------------------------------------- ###


# to analyze the 1st frame does not really make sense
# Retrieve the current TimePoint Index
index = ZenService.Experiment.CurrentTimePointIndex

# get intial ratio value to compare with from the frame 2
if (index==2  and (index < lastindex or index > lastindex)):
    initial_ratio = round(ZenService.Analysis.ROIS.DynamicRois[1].Ratio,2)
    i1 = round(ZenService.Analysis.ROIS.DynamicRois[1].IntensityMean[1],0)
    i2 = round(ZenService.Analysis.ROIS.DynamicRois[1].IntensityMean[2],0)
    # write to log file (optional)
    logfile = ZenService.Xtra.System.AppendLogLine(str(index) +'\t' + str(i1) + '\t' + str(i2) + '\t'+str(initial_ratio))
    # update the index counter
    lastindex = index

# check for an actication event from frame 3 on ...
if (index >=3 and (index < lastindex or index > lastindex)):
    # intensity of channels substracted by background
    ratio = round(ZenService.Analysis.ROIS.DynamicRois[1].Ratio,2)
    i1 = round(ZenService.Analysis.ROIS.DynamicRois[1].IntensityMean[1],0)
    i2 = round(ZenService.Analysis.ROIS.DynamicRois[1].IntensityMean[2],0)
    # write to log file (optional)
    logfile = ZenService.Xtra.System.AppendLogLine(str(index) +'\t' + str(i1) + '\t' + str(i2) + '\t'+
            str(ratio) + '\t' + str(round(ratio/initial_ratio,2)))
    # play sound if the cell got activated --> ration is bigger than intial ration by a factor of RF
    if (ratio/initial_ratio > RF and action_taken == False):
        ZenService.Xtra.System.PlaySound()
        ZenService.Actions.SetTimeSeriesInterval(interval_fast, TimeUnit.ms)
        action_taken = True
    
    # update the index counter
    lastindex = index


### -------------------- PostScript --------------------------------------------- ###


ZenService.Actions.SetTimeSeriesInterval(interval_initial, TimeUnit.ms) # restore exposure time from the start of the experiment
ZenService.Xtra.System.ExecuteExternalProgram(r"C:\Program Files (x86)\Notepad++\notepad++.exe", logfile)