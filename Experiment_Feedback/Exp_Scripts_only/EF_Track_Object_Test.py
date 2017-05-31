###   PreScript   ###

from System import Array

logfile = ZenService.Xtra.System.AppendLogLine('Frame\tImgX\tImgY\tObj\tX[]\tY[]\tInt[]\tID MaxInt\tX\tY')
# creates a readable string from all entries of an array
def createstr(arrayin):
    dim = len(arrayin)
    strout = ''
    for i in range(0,dim):
        if (i < dim-1): 
            strout = strout + str(round(arrayin[i],2)) + '\t' # add tab at the end if it is NOT the last entry
        else:
            strout = strout + str(round(arrayin[i],2)) # no tab since it is the last entry
    return strout

###   LoopScript ###

# get total number of objects and frame number
num_obj = ZenService.Analysis.AllParticles.RegionsCount
frame = ZenService.Experiment.CurrentTimePointIndex

# get current stage position XY of the image center
imgX = ZenService.Analysis.AllParticles.ImageStageXPosition
imgY = ZenService.Analysis.AllParticles.ImageStageYPosition

# get current object positions array for all detected objects
#posx = ZenService.Analysis.SingleParticle.CenterX
#posy = ZenService.Analysis.SingleParticle.CenterY
posx = ZenService.Analysis.SingleParticle.BoundCenterXStage
posy = ZenService.Analysis.SingleParticle.BoundCenterYStage
intensities = ZenService.Analysis.SingleParticle.IntensityMean_EGFP

# get ID of the brightest detected particle
ID = Array.IndexOf(intensities, max(intensities))

# move the stage
ZenService.HardwareActions.SetStagePosition(posx[ID], posy[ID])

# create strings:
POSX = createstr(posx)
POSY = createstr(posy)
INTS = createstr(intensities)

# write positions to data log file
logfile = ZenService.Xtra.System.AppendLogLine(str(frame)+'\t'+str(imgX)+'\t'+str(imgY)+'\t'+
    str(num_obj)+'\t'+POSX+'\t'+POSY+'\t'+INTS+'\t'+str(ID+1)+'\t'+str(round(posy[ID],2))+'\t'+str(round(posy[ID],2)))




###   PostScript   ###

# this is all optional
ZenService.Xtra.System.ExecuteExternalProgram(r'C:\Program Files (x86)\Notepad++\notepad++.exe', logfile)