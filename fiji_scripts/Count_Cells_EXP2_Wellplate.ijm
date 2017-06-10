// Author: Sebastian Rhode
// Version: 1.0
// Date: 2013_08_08

//name = "c:\\Python_ZEN_Output\\Wellplate96_1Position_per_Well.czi"
name = getArgument;
if (name=="") exit("No argument!");

imagedir = File.getParent(name);
imagefilename = File.getName(name);
print("Directory :", imagedir);
print("File Name :", imagefilename);

//run("Bio-Formats Importer", "open=["+ name + "] autoscale color_mode=Default concatenate_series view=Hyperstack stack_order=XYCZT series_list=1-"+sizeT);
run("Bio-Formats Importer", "open=["+ name + "] autoscale color_mode=Default concatenate_series open_all_series view=Hyperstack stack_order=XYCZT");
//run("Bio-Formats Importer", "open=["+ name + "] autoscale color_mode=Default view=Hyperstack stack_order=XYCZT");


// remove slice labels
run("Remove Slice Labels");

// get the name of the image file
title_orig = getTitle();
print("Title : ", title_orig);

// blur image to make it easier for the segmentation
run("Gaussian Blur...", "sigma=1.5");

// specify threshold parameters
setAutoThreshold("Otsu dark");
setOption("BlackBackground", true);

// specify parameters to measure
run("Set Measurements...", "area min display add redirect=[" + title_orig + "] decimal=2");

// Analyze all detected particle
run("Analyze Particles...", "size=50-500 pixel circularity=0.00-1.00 show=[Overlay Outlines] display clear include summarize add in_situ stack");
//run("Analyze Particles...", "size=50-500 pixel circularity=0.00-1.00 show=[Overlay Outlines] clear include summarize add in_situ stack");
roiManager("Show None");

// Save Results Table
selectWindow("Results");
imagefilename_woExt = replace(imagefilename, '.czi', ""); 
saveAs("Results", imagedir + "\\" + imagefilename_woExt + "_Results_Fiji.txt");

// Save Summary Table
selectWindow("Summary of " + title_orig); 
saveAs("Text", imagedir + "\\" + imagefilename_woExt + "_Summary_Fiji.txt");

// Save ROIs
roiManager("Save", imagedir + "\\" + imagefilename_woExt + "_Fiji_ROIs.zip");
