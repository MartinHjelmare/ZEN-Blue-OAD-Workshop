"""
File: SendFiji_RunMacro.czmac
Author: Sebastian Rhode
Date: 2017_06_10
Verison: 1.2
"""

version = 1.2

from System.IO import Path, File, Directory, FileInfo
from System.Diagnostics import Process
import sys
import os

# clear output
Zen.Application.MacroEditor.ClearMessages()

# Adapt this to your Fiji macro folder
default_macro_folder = r'C:\Users\Public\Documents\Fiji\macros\Zen_Test'
print 'Current Macro Folder : ', default_macro_folder

# Fiji macro for opening the CZI windowless --&gt; default macro for opening a CZI without the BioFormats input window
bf_windowless = r'c:\Users\Public\Documents\Fiji\macros\Zen_Test\Open_CZI_BioFormats_Windowless.ijm'

macros = Directory.GetFiles(default_macro_folder)
macrofiles_short = []
Macrodict = {}
# get all macros from folder
for macro in macros:
    macrofiles_short.append(Path.GetFileName(macro))
    Macrodict[Path.GetFileName(macro)] = macro

CZIfiles_short = []
CZIdict = {}

# get all open documents
opendocs = Zen.Application.Documents
for doc in opendocs:
    #print doc.Name
    image = Zen.Application.Documents.GetByName(doc.Name)
    
    if image.FileName.EndsWith('.czi'):
        # get the filename of the current document only when it ends with '.czi'
        CZIfiles_short.append(Path.GetFileName(image.FileName))
        CZIdict[Path.GetFileName(image.FileName)] = image.FileName

# Initialize the dialog window for the required user inputs
wd = ZenWindow()
wd.Initialize('Open CZI in Fiji and run IJ Macro - Version: ' + str(version), 450, 220, True, True)
# add components to dialog
wd.AddDropDown('czi', 'Select CZI Image Data', CZIfiles_short, 0)
wd.AddCheckbox('windowless', 'Use windowless BioFormats Importer', True)
wd.AddCheckbox('RunMacro', 'Activate Macro Execution', False)
wd.AddDropDown('ijmacro','Select Macro to be executed', macrofiles_short, 1)

# show the window
result=wd.Show()

# check, if Cancel button was clicked
if result.HasCanceled == True:
    sys.exit('Macro aborted with Cancel!')

# get the input values and store them
cziname = result.GetValue('czi')
macroname = result.GetValue('ijmacro')
runmacro = result.GetValue('RunMacro')
bfimport = result.GetValue('windowless')

CZI2Open = CZIdict[cziname]
Macro2Open = Macrodict[macroname]
print 'Send CZI     : ', CZI2Open

# use the absolute path --&gt; this works always
exeloc = 'C:\Users\Public\Documents\Fiji\ImageJ-win64.exe'
if runmacro == True:
    print 'Run selected Fiji Macro : ', Macro2Open
    option =  '-macro ' + Macro2Open + ' ' + CZI2Open # 'glue' together the options
elif runmacro == False:
    print 'No special macro selected.'
    if bfimport == True:
        option = '-macro ' + bf_windowless + ' ' + CZI2Open
    if bfimport == False:
        option = CZI2Open

print 'Fiji Parameter : ', option

# start Fiji and execute the macro
app = Process();
app.StartInfo.FileName = exeloc
app.StartInfo.Arguments = option
app.Start()
