###   PreScript   ###



###   LoopScript ###



###   PostScript   ###

# get the name of the current image data set
filename = ZenService.Experiment.ImageFileName
# use the absolute path --> this works always 
exeloc = 'C:\Users\Public\Documents\Fiji\ImageJ-win64.exe'
 # specify the Fiji macro one wants to use
macro = r'-macro Zen_Test\Open_CZI_and_MaxInt.ijm'
# 'glue' together the options 
option =  macro + ' ' + filename
# start Fiji, open the data set and execute the macro
ZenService.Xtra.System.ExecuteExternalProgram(exeloc, option)