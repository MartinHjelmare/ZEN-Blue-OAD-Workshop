### -------------------- PreScript ---------------------------------------------- ###


from System import Array

# define header for the oitput logfile to your needs - Timeframe - ObjectID - ObjStageX - ObjStageY
logfile = ZenService.Xtra.System.AppendLogLine('T\tObjID\tStageX\tStageY')

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


### -------------------- LoopScript --------------------------------------------- ###


# get total number of objects and frame number
num_obj = ZenService.Analysis.AllParticles.RegionsCount
frame = ZenService.Experiment.CurrentTimePointIndex

# get current stage position XY of the image center
imgX = ZenService.Analysis.AllParticles.ImageStageXPosition
imgY = ZenService.Analysis.AllParticles.ImageStageYPosition

# get current object positions and intensity arrays for all detected objects
posx = ZenService.Analysis.SingleParticle.BoundCenterXStage
posy = ZenService.Analysis.SingleParticle.BoundCenterYStage
intensities = ZenService.Analysis.SingleParticle.IntensityMean_EGFP

# get ID of the brightest detected particle
ID = Array.IndexOf(intensities, max(intensities))

# move the stage to the position of the brightest particle -->
ZenService.HardwareActions.SetStagePosition(posx[ID], posy[ID])

# create strings for optional output for testing --> comment when not used:
POSX = createstr(posx)          # array with all StageX positions
POSY = createstr(posy)          # array with all StageY positions
INTS = createstr(intensities)   # array with all intensities

# write positions to data log file
logfile = ZenService.Xtra.System.AppendLogLine(str(frame)+'\t'+str(ID+1)+'\t'+'{:.2f}'.format(posy[ID])+'\t'+'{:.2f}'.format(posy[ID]))


### -------------------- PostScript --------------------------------------------- ###


# this is all optional
ZenService.Xtra.System.ExecuteExternalProgram(r'C:\Program Files (x86)\Notepad++\notepad++.exe', logfile)