###   PreScript   ###

lastindex = 0
cn_last = 0
soundfile1 = r'C:\TFS\Doc\3-ZIS\3-Development\Discussions\ExperimentFeedback\Release_DVD\SoundFiles\PsychoScream.wav'
soundfile2 = r'C:\TFS\Doc\3-ZIS\3-Development\Discussions\ExperimentFeedback\Release_DVD\SoundFiles\YEAH.WAV'

###   LoopScript ###

# get parameters
frame = ZenService.Analysis.Cells.ImageIndexTime
cn = ZenService.Analysis.Cells.RegionsCount
delta = cn - cn_last

# write to log file (optional)
logfile = ZenService.Xtra.System.AppendLogLine(str(frame)+'\t'+str(cn)+'\t'+str(delta))
cn_last = cn

# check if the number of active cells has changed

if (delta > 0): ## active cell number has increased
    #  play soundfile 1 --> this could be anythin else, e.g. sent a TTL to port XY
    ZenService.Xtra.System.PlaySound(soundfile2)

elif (delta < 0): ## active cell number has decreased
    # play soundfile 2 --> just a placeholder for a more meaningful action
    ZenService.Xtra.System.PlaySound(soundfile1)

###   PostScript   ###

ZenService.Xtra.System.ExecuteExternalProgram(r'C:\Program Files (x86)\Notepad++\notepad++.exe', logfile)

# additional script execution to display the data directly from the feedback sricpt
filename = '-f ' + ZenService.Experiment.ImageFileName[:-4] + '_Log.txt'
script = r'c:\TFS\Doc\3-ZIS\3-Development\Discussions\ExperimentFeedback\Release_DVD\Python_Scripts_for_Data_Display\display_jurkat.py'
ZenService.Xtra.System.ExecuteExternalProgram(script, filename)