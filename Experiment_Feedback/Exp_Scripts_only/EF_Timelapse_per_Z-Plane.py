###   PreScript   ###

loopcount = 0 # this variable is required to keep track of the current loop from the Experiment Designer
lastframe = 0
# the z-Stack has to be defined manually !
zstart = 0 # must be the coordinate of the 1st zplane in micron
deltaz = 5.0 # spacing for the z-stack in micron
timepoints = 5 # number of timepoints from Time Series Toolwindow!

###   LoopScript ###

# calculate the desired z-position
zpos = zstart + deltaz * loopcount

# get the current overall frame number
frame = ZenService.Experiment.CurrentTimePointIndex

# create a logile (this is optional)
logfile = ZenService.Xtra.System.AppendLogLine(str(loopcount+1)+'\t'+str(frame)+'\t'+str(zpos))

# only do the following for every new time point ...
if (frame != lastframe):
    
    # check, if the devision of overall frame / timepoints per plane = 0
    rest = divmod(frame, timepoints)
    # and if YES ...
    
    if (rest[1] == 0):
         # increase the loop counter
        loopcount = loopcount + 1
        # calc the new z-position for the next timelapse
        zpos = zstart + (deltaz * loopcount)
        # finally set new focus position
        ZenService.HardwareActions.SetFocusPosition(zpos)
    
    # update the frame to be ready for the next iteration
    lastframe = frame

###   PostScript   ###

ZenService.Xtra.System.ExecuteExternalProgram('C:\\Program Files (x86)\\Notepad++\\notepad++.exe', logfile)