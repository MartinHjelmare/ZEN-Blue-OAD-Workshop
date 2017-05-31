###   PreScript   ###

cells_per_well = 0 # total number of cells
logfile = ZenService.Xtra.System.AppendLogLine('Well\tTile\tCells/Tile\tCell/Well')
last_tile = 0

###   LoopScript ###

# this value is different for every acquired picture !!!
index = ZenService.Analysis.Cells.ImageAcquisitionTime
# get cell number for the current tile
cpt = ZenService.Analysis.Cells.RegionsCount
# get current well name
well = ZenService.Analysis.Cells.ImageSceneContainerName
# get current tile number
tile = ZenService.Experiment.CurrentTileIndex

if tile != last_tile:
    if tile < last_tile:
        cells_per_well = 0
    # add cells from current tile to cell_per_well
    cells_per_well = cells_per_well + cpt

# stop if the desired cell number was already reached
if (cells_per_well > 2000):
    ZenService.Actions.JumpToNextContainer()

# write data into log file
logfile = ZenService.Xtra.System.AppendLogLine(well+'\t'+str(tile)+'\t'+str(cpt)+'\t'+str(cells_per_well))

# update lasttile
last_tile = tile

###   PostScript   ###

ZenService.Xtra.System.ExecuteExternalProgram(r'C:\Program Files (x86)\Notepad++\notepad++.exe',logfile)