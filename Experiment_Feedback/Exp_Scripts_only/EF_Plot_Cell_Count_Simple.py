###   PreScript   ###



###   LoopScript ###

# Get current frame number
frame = ZenService.Analysis.Cells.ImageIndexTime

# Get the number of cells for the current frame
cn = ZenService.Analysis.Cells.RegionsCount

# Write data to log file: frame number ; cell number 
logfile = ZenService.Xtra.System.AppendLogLine(str(frame) + '\t' + str(cn))

###   PostScript   ###

# Specify the script used to display the data and call the script with arguments
script = r'...\Python_Scripts\display_results_simple.py'

# Run external python script to display the data
ZenService.Xtra.System.ExecuteExternalProgram(script, '-f ' + logfile)

# Open Notepad.exe to display the logfile
ZenService.Xtra.System.ExecuteExternalProgram(r'C:\Windows\notepad.exe', logfile)