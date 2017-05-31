###   PreScript   ###

# define initial exposure time
exposure = 50

###   LoopScript ###

# get the current time index
index  = 1 + ZenService.Experiment.CurrentTimePointIndex * 0.2
# increase the exposure time
ZenService.Actions.SetExposureTime(1, index*exposure)

###   PostScript   ###

