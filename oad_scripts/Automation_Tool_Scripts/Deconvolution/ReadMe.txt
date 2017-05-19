This script will automatically deconvolve a z-stack with the Fast Iterative Lucy-Richardson algorithm (100 iterations). The result will be saved in C:\ZEN_Output.

To make adjustments:

1. Line 6 for output folder (always use double "\" to indicate subfolder
2. Line 10 with regards to DCV Parameters

To change these, open an image, go to Decovolution parameters, make changes and save in a new czips-file (save in Parameters window). E.g. this script uses "Lucy_Richardson_DCV.czips". 

This file is stored in (change USERNAME to Windows login name):

C:\Users\USERNAME\Documents\Carl Zeiss\ZEN\Documents\Processing Settings\DeconvolutionApplication