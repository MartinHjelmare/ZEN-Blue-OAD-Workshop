###   PreScript   ###

from System import Array

def ArrayDiv(a,b):
    out = Array.CreateInstance(float,len(a))
    outstr = ''
    for i in range(0,len(a)):
        out[i] = a[i] / b[i]
        outstr = outstr + str(round(out[i],2))+'\t'
    
    return out, outstr
    
options = '-f ' + ZenService.Experiment.ImageFileName[:-4] + '_Log.txt' + ' -p all'
script = r'c:\TFS\Doc\3-ZIS\3-Development\Discussions\ExperimentFeedback\Release_DVD\Python_Scripts_for_Data_Display\Dynamic_MeanROI_Cell_Detect.py'
ZenService.Xtra.System.ExecuteExternalProgram(script, options)

###   LoopScript ###

frame = ZenService.Analysis.AllCells340.ImageIndexTime
int340 = ZenService.Analysis.SingleCell340.IntensityMean_F2_340nm
int380 = ZenService.Analysis.SingleCell340.IntensityMean_F2_380nm
ratio, ratiostr = ArrayDiv(int340, int380)
logfile = ZenService.Xtra.System.AppendLogLine(str(frame) +'\t'+ratiostr)


###   PostScript   ###

# open logfile at the end (optional)
ZenService.Xtra.System.ExecuteExternalProgram(r'C:\Program Files (x86)\Notepad++\notepad++.exe', logfile)