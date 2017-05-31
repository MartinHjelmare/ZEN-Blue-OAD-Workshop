###   PreScript   ###

cells_total = 0 # total number of cells
logfile = ZenService.Xtra.System.AppendLogLine('Tile\tCells\tTotal\tPosX\tPosY')
script = r'c:\Users\M1SRH\Documents\Projects\ExpFeedback_Current\Python_Scripts_for_Data_Display\display_results_tiles.py'

###   LoopScript ###

# get cell number for the current tile
cn =ZenService.Analysis.Cells.RegionsCount
# get current tile number
tile = ZenService.Experiment.CurrentTileIndex
# sum up the number of cells
cells_total = cells_total + cn
# stop if the desired cell number was already reached
if (cells_total > 2000):
    ZenService.Actions.StopExperiment()

# read the xy position of the current image
posx = ZenService.Analysis.Cells.ImageStageXPosition
posy = ZenService.Analysis.Cells.ImageStageYPosition
# write data into log file
logfile = ZenService.Xtra.System.AppendLogLine(str(tile)+'\t'+str(cn)+'\t'+str(cells_total)+'\t'+str(posx)+'\t'+str(posy))

###   PostScript   ###

ZenService.Xtra.System.ExecuteExternalProgram(script, '-f ' + logfile)
ZenService.Xtra.System.ExecuteExternalProgram(r'C:\Program Files (x86)\Notepad++\notepad++.exe', logfile)