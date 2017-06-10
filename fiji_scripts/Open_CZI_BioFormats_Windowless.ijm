// File: Open_CZI_BioFormats_Windowless.ijm
// Author:	Sebastian Rhode
// Date:	28.07.2015

name = getArgument;
if (name=="") exit("No argument!");

print("File Location : ", name);
run("Bio-Formats Importer", "open=[" + name + "] autoscale color_mode=Default open_all_series view=Hyperstack stack_order=XYCZT");

// set display mode
Stack.setDisplayMode("composite");
run("Enhance Contrast", "saturated=0.35");