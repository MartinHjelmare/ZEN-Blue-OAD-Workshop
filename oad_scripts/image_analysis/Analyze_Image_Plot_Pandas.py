"""
File: Analyze_Image_Plot_Pandas.czmac
Author: Sebastian Rhode
Date: 2017_06_10
Verison: 1.2
"""

from System.Diagnostics import Process
from System.IO import File, Path, Directory

# clear output
Zen.Application.MacroEditor.ClearMessages()

# load image and add it to ZEN and get the image path
image_to_analyze = r'c:\Python_ZEN_Output\well96_1Pos.czi'
image = Zen.Application.LoadImage(image_to_analyze)
Zen.Application.Documents.Add(image)
outputpath = Path.GetDirectoryName(image_to_analyze)
resultname = Path.GetFileNameWithoutExtension(image.Name)

# define the image analysis setting and run the image analysis on the active image
iasfilename = r'c:\Users\M1SRH\Documents\Carl Zeiss\ZEN\Documents\Image Analysis Settings\Count_Cells_DAPI_96well.czias'
ias = ZenImageAnalysisSetting()
ias.Load(iasfilename)
Zen.Analyzing.Analyze(image,ias)

# Create data list with results for all regions (e.g. all nuclei)
table_all = Zen.Analyzing.CreateRegionsTable(image)
Zen.Application.Documents.Add(table_all)
# Create data list with results for each region (e.g. every single nucleus)
table_single = Zen.Analyzing.CreateRegionTable(image)
Zen.Application.Documents.Add(table_single)

# Save both data lists as CSV files
table_all_filename = Path.Combine(outputpath, resultname + '_All.csv')
table_all.Save(table_all_filename)
table_single_filename = Path.Combine(outputpath,  resultname + '_Single.csv')
table_single.Save(table_single_filename)

# close the image and image analysis setting
#image.Close()
ias.Close()

# define the external plot script or tool
pythonexe =  r'c:\Anaconda3\python.exe'
#pythonexe =  r'c:\Anaconda3\envs\py27\python.exe'
script = r'c:\Users\M1SRH\Documents\Projects\OAD\External_Python_Scripts_for_OAD\test_wellplate_from_ZEN_py3.py'

# define the actual CSV file and the parameters
csvfile = Path.Combine(outputpath, table_single_filename)
# this depends on the actual CZIAS and the import of the CSV table in python
parameter2display = 'ObjectNumber'
params = ' -f ' + csvfile + ' -w 96' + ' -p ' + parameter2display + ' -sp False'

# start the data display script as an external application
app = Process();
app.StartInfo.FileName = pythonexe
app.StartInfo.Arguments = script + params
app.Start()
app.WaitForExit()

savename_all =  Path.Combine(Path.GetDirectoryName(image_to_analyze), Path.GetFileNameWithoutExtension(image_to_analyze) + '_Single_HM_all.png')
savename_single = Path.Combine(Path.GetDirectoryName(image_to_analyze), Path.GetFileNameWithoutExtension(image_to_analyze) + '_Single_HM_' + parameter2display + '.png')

print 'Showing saved figure in ZEN.'

if File.Exists(savename_all):
    plotfigure1 = Zen.Application.LoadImage(savename_all, False)
    plotfigure2 = Zen.Application.LoadImage(savename_single, False)
    Zen.Application.Documents.Add(plotfigure1)
    Zen.Application.Documents.Add(plotfigure2)
else:
    print 'Saved figure not found.'

print 'Done.'
