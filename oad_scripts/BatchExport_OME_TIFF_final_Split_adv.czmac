"""
File: BatchExport_OME_TIFF_final_Split_adv.czmac
Author: SRh
Date: 2017_05_19
Version: 0.2

- This macro splits a CZI file from a well experiment into single CZI files
  and saves them in a separate folder.
- There will be one CZI for every scene. The scene and well information will be part of the filename.
- There will be a single OME-TIFF file for every well.
- The well name will be added to the end of the resulting filename.
- Optionally it is possible to split the CZI before the OME-Export

For the OME_TIFF Export an CZIPS-Settings file is used.

"""
version = 0.2

import re
import clr
from System.Diagnostics import Process
from System.IO import Directory, Path, File, FileInfo
import time

# clear output console
Zen.Application.MacroEditor.ClearMessages()

def ExportOME(image, settingsfile, targetdir, workgroup=True):

    # do the OME-TIFF Export and add Split to the image name
    prefix = image.Name[:-4]

    # initialize OME-TIFF Export Setting
    exportsetting = Zen.Processing.Utilities.Settings.OmeTiffExportSetting()
    
    # load setting from the Processing Settings folder - ...\Carl Zeiss\ZEN\Documents\Processing Settings\OmeTiffExport
    if workgroup:
        exportsetting.Load(settingsfile, ZenSettingDirectory.Workgroup)
    if not workgroup:
        exportsetting.Load(settingsfile, ZenSettingDirectory.User)
    
    # execute the OME_TIFF export
    Zen.Processing.Utilities.ExportOmeTiff(image, exportsetting, prefix, targetdir)
    
    return None

def ExportOME_SplitDim(image, strParams, targetdir, splitopt='T', deleteorig=True):
    
    # check if the split dimension is Time
    if splitopt == 'T':
        
        # get the number of timepoints and loop
        SizeT = int(image.Metadata.TimeSeriesCount)
        
        for tIndex in range(0, SizeT):
        
            # do the OME-TIFF Export and add Split to the image name
            prefix = image.Name[:-4] + '_T' + str(tIndex) + '.czi'
            strP = re.sub('T\(\d+\)', 'T('+str(1+tIndex)+')', strParams)
            Zen.Processing.Utilities.ExportOmeTiff(image, strP, prefix, targetdir)
            
    else:
        print 'Doing nothing here.'
        
    return None

################# OME-TIFF Export Setting String  used for Splitting TimePoints ####################

strParams = """<ProcessingParameters Function="OmeTiffExport">
  <FunctionParameters Function="OmeTiffExport">
    <DestFolder>D:\mydata</DestFolder>
    <SubsetSelectionMode>UseSubsetString</SubsetSelectionMode>
    <SubSetString>T(3)</SubSetString>
    <MultichannelMode>DistinctChannels</MultichannelMode>
    <ProcessingModeFlags>Raw</ProcessingModeFlags>
    <MCSelectionMode>SubsetDefinition</MCSelectionMode>
    <UseChannelNames>false</UseChannelNames>
    <BurnInDataZone>false</BurnInDataZone>
    <PanOption>All</PanOption>
    <Zoom>1</Zoom>
    <UseBIGTiffFormat>false</UseBIGTiffFormat>
    <UseCompression>false</UseCompression>
    <UseTiling>true</UseTiling>
    <Prefix>testdata</Prefix>
    <ShiftPixel>false</ShiftPixel>
    <GeneratePyramid>false</GeneratePyramid>
    <GenerateThumbnail>true</GenerateThumbnail>
    <ConvertTo8Bit>false</ConvertTo8Bit>
    <OmeXmlSchemaVersion>Schema201006</OmeXmlSchemaVersion>
  </FunctionParameters>
</ProcessingParameters>"""

###################################################################################################

# spliting options
splitoptions = [ ' NONE', 'T']

# set to True if the application should look for the OME-TIFF export settings inside the WorkGroup Documents
useworkgroup = True

# specify the default source folder and the settings directory
defaultdir = r'c:\Users\M1SRH\Documents\Testdata_Zeiss\Wellplate\CZI_Wellplate_Export\bfconvert'

# get the correct directory for the current user or use the WorkGroup documents
if useworkgroup:
    defaultsettingdir = Path.Combine(Zen.Application.Environment.GetFolderPath(ZenSpecialFolder.WorkgroupDocuments), 'Processing Settings\\OmeTiffExport')
    print 'WorkGroup Documents will be used.'
if not useworkgroup:
    defaultsettingdir = Path.Combine(Zen.Application.Environment.GetFolderPath(ZenSpecialFolder.UserDocuments), 'Processing Settings\\OmeTiffExport')
    print 'User-specific Documents will be used.'

# create list of all existing settings
settingsdir_long = Directory.GetFiles(defaultsettingdir,'*.czips')
settingsdir = []

# create list only containing the seetings names
for s in settingsdir_long:
    settingsdir.append(Path.GetFileNameWithoutExtension(s))

######## Create Dialog ############

# create setup dialog and enter source and destination directory with GUI
window = ZenWindow()
window.Initialize('Batch Well Export after Split from CZI - Version: ' + str(version))
window.AddFolderBrowser('sourcedirectory', 'Source folder: ', defaultdir)
window.AddLabel('-----  Normal OME-TIFF Export using Settings File -----')
window.AddCheckbox('omeexp', 'Export as OME-TIFF after Split', True)
window.AddDropDown('settingspath', 'Settings File OME-TIFF Export (no Split): ', settingsdir, 0)
window.AddLabel('-----  Special DimSplit during OME-TIFF Export  -----')
window.AddCheckbox('dimsplit', 'Split Dimensions for single OME-TIFFs', True)
window.AddDropDown('splitoption', 'Spliting Option', splitoptions, 1)
window.AddLabel('-----  Remove CZI after OME-TIFF Export  -----')
window.AddCheckbox('cziremove', 'Remove single CZIs after OME-Export', True)

# show the window
result = window.Show()
if result.HasCanceled:
    message = 'Macro was canceled by user.'
    print message
    raise SystemExit(message)

# read results
sourcedir = result.GetValue('sourcedirectory')
settingsfile = result.GetValue('settingspath')
omeexport = result.GetValue('omeexp')
czidelete = result.GetValue('cziremove')
splitdim = result.GetValue('dimsplit')
splitopt = result.GetValue('splitoption')
exedir = result.GetValue('bftoolsdir')
waitforkey = result.GetValue('waitkey')
print 'Selected Settings File : ', settingsfile
# currently disbaled - 20170331
bfsplit = False

# OME-TIFF Export
# check base directory for CZI files to export
czidir = Directory.GetFiles(sourcedir,'*.czi')

splitdirs = []

# Batch Loop - Load all CZI images and export as OME-TIFF 
for i in range(0, czidir.Length): 
    
    # get current complete CZI filepath
    czifile = czidir[i]
    file_woExt = Path.GetFileNameWithoutExtension(czifile)
    print 'File to split : ',czifile
    
    # load the image, derive the directory name and create new directory
    image = Zen.Application.LoadImage(czifile, False)
    destdir = Path.Combine(sourcedir, file_woExt + '_Single')
    Directory.CreateDirectory(destdir)
    
    # store directory name inside list
    splitdirs.append(destdir)
    
    # Split single CZI file containing all wells into single CZI files
    Zen.Processing.Utilities.SplitScenes(image, destdir, ZenCompressionMethod.None, True, True, False)
    
    # close image file
    image.Close()
    print 'Finished Split Scences and Write Files for : ', czifile

    if omeexport:
        
        # get all CZI files inside the current subfolder after Split Scenes (Write Files)
        czidir_Single = Directory.GetFiles(destdir,'*.czi')
        
        # optional splitting of a dimension, eg. TimePoints
        for c in range(0, czidir_Single.Length):
        
            # get current complete CZI filepath
            czifile_Single = czidir_Single[c]
            
            # Load single CZI image
            image = Zen.Application.LoadImage(czifile_Single, False)
            print 'Exporting Single CZI File as OME-TIFF: ', czifile_Single
            
            if splitdim == True:
                ExportOME_SplitDim(image, strParams, destdir, splitopt='T', deleteorig=True)
            
            elif splitdim == False:
                # do the OME-TIFF Export
                ExportOME(image, settingsfile, destdir, workgroup=True)
            
            # close the image file when the export is done
            image.Close()
            
            if czidelete:
                # delete the splitted CZI files when option was checked
                print 'Removed CZI file after Split: ', czifile_Single
                File.Delete(czifile_Single)

if bfsplit:
    
    for dir in splitdirs:
        # add dir
        option = ' "' + dir +'"'
        # add split
        option =  option + ' -yes'
        # add splitoption
        option = option + splitopt
        # add wait for key
        if waitforkey == True:
        # wait for key press inside the command line
            option = option + ' -wait'
        elif waitforkey == False:
            option = option + ' -nowait'
        
        # add directory containing the bftools to the options
        option = option + ' "' + exedir + '"' 
        
        # run commad line argument
        print 'Batch script to run the OME-TIFF split using bfconvert.'
        print 'Argument: ' + exeloc
        print 'Working directory: ', dir
        print '...'
        time.sleep(2)
        
        # start batch script (*.bat) to use the bftools
        app = Process()
        print 'Batch File to run: ', exeloc
        print 'Batch Options    : ', option
        app.StartInfo.FileName = exeloc
        app.StartInfo.Arguments = option
        app.Start()
        # wait until the batch script is finished
        app.WaitForExit()


print 'Export finished.'
