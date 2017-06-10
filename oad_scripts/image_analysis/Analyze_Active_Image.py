"""
File: Analyze_Active_Image.czmac
Author: Sebastian Rhode
Date: 2017_06_10
Verison: 1.1
"""

from System.IO import Path

# clear output console
Zen.Application.MacroEditor.ClearMessages()

# get current active image
image = Zen.Application.Documents.ActiveDocument

# define and load image analysis setting
iasfilename = 'Count_Cells_2C.czias'
ias = ZenImageAnalysisSetting()
ias.Load(iasfilename)

# every class will result in a single CSV table
resulttables = Zen.Analyzing.AnalyzeToTable(image, ias)
# iterate over all tables
for table in resulttables:
    Zen.Application.Documents.Add(table)

# analyze directly into CSV files
resultname = Path.GetFileNameWithoutExtension(image.Name)
outputpath = Path.GetDirectoryName(image.FileName)
Zen.Analyzing.AnalyzeToFile(image, ias, outputpath, resultname, False)
print 'Tables saved as CSV file in: ', outputpath

# close the image analysis setting
ias.Close()
