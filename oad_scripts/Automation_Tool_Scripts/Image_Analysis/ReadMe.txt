1. Copy "Analysis_Count_Cells_Active_Image.czmac" into "C:\Users\Public\Documents\Carl Zeiss\ZEN\Documents\Macros"
2. Copy "Count_Cells.czias" into "C:\Users\Public\Documents\Carl Zeiss\ZEN\Documents\Image Analysis Settings"

Data is saved in a folder on "C:\ZEN_Output". Before running the script, create the folder and/or rename its location in the macro (line 7).

The script works on any single or multi-channel image as long as the first channel is the DAPI channel. Feel free to create your own script and rename the file & location in the macro accordingly (line 9).

In ZEN Blue Pro/System, enable Automation, open this script in "After Acquisition". Once image acquisition is finished, it will run automatically and analyze the recently acquired image.
