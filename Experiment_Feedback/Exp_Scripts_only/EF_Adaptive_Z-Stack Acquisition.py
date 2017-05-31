### -------------------- PreScript ---------------------------------------------- ###


lastindex = 0


### -------------------- LoopScript --------------------------------------------- ###


# read out z-plane and image acqusition time
zplane = ZenService.Experiment.CurrentZSliceIndex
index = ZenService.Analysis.Neurons.ImageAcquisitionTime

# only do the rest if it is a new image = different image acqusition time (or z-plane)
if (index < lastindex or index > lastindex):
    # get data from image analysis
    IntNeuron = ZenService.Analysis.Neurons.RegionsIntensityMean_Alexa_Fluor_488
    IntBackground = ZenService.Analysis.BackgroundField.RegionsIntensityMean_Alexa_Fluor_488
    # calculate intensity ratio as some kind of "sharpness" index
    Ratio = IntNeuron / IntBackground
    # get current z-position
    position = ZenService.Hardware.Focus
    logfile = ZenService.Xtra.System.AppendLogLine(str(zplane) + '\t' + str(position) +'\t' + str(Ratio))
    # if sample runs out off focus --> stop acquisition
    if Ratio < 1:
        ZenService.Actions.StopExperiment()
    # update index
    lastindex = index


### -------------------- PostScript --------------------------------------------- ###


# open data log file at the end of the experiment
ZenService.Xtra.System.ExecuteExternalProgram('C:\\Windows\\system32\\Notepad.exe', logfile)