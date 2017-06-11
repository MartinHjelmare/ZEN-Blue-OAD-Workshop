"""  
Author: Sebastian Rhode
Date: 2017_03_03
File: SegmentationPipeline.czmac
Version: 0.1
"""

############# Function to create the Image Analysis Pipeline ##################

def RollingBall(input, radius=50, createBackground=False, doPreSmooth=False, isLightBackground=False, id=0, showresult=True):
# do the rolling ball background substraction
    print '* RollingBall Background Subtraction ...'
    print 'Radius=', radius, ' doPreSmooth=', doPreSmooth, ' createBackground=', createBackground, ' isLightBackground=', isLightBackground
    rb = Zen.Processing.Adjust.BackgroundSubtraction(input, 50, doPreSmooth=False, createBackground=False, isLightBackground=False)
    rb.Name = 'RollingBall_' + str(id) + '.czi'
    if showresult:
        Zen.Application.Documents.Add(rb)
        
    return rb
    

def CorrectIllumination(input, lowpasscount=3, kernelsize=300, id=0, showresult=True):
    # remove uneven illumination with highpass
    print '* Correct Illumination using Highpass ...'
    print 'Count=', lowpasscount, ' KernelSize=', kernelsize
    lowpass = Zen.Processing.Filter.Smooth.Lowpass(input, lowpasscount, kernelsize, False)
    highpass = Zen.Processing.Arithmetics.Subtraction(input, lowpass, ZenNormalizeMode.Auto, False)
    lowpass.Name = 'Lowpass_' + str(id) + '.czi'
    highpass.Name = 'Highpass_' + str(id) + '.czi'
    if showresult:
        Zen.Application.Documents.Add(lowpass)
        Zen.Application.Documents.Add(highpass)
        
    return highpass


def MedianFilter(input, radius=5, id=0, showresult=True):
    # apply median filter
    print '* Median Filter ...'
    print 'Radius=', radius
    filtered = Zen.Processing.Filter.Smooth.Median(input, 5, False)
    filtered.Name = 'Filtered_' + str(id) + '.czi'
    if showresult:
        Zen.Application.Documents.Add(filtered)
        
    return filtered


def AutoThreshold(input, method=ZenThresholdingMethod.ThreeSigmaThreshold, createBinary=True, invertResult=False, id=0, showresult=True):
    # apply thrsehold method
    print '* Automatic Thresholding ...'
    print 'Method=', method, ' createBinary=', createBinary, ' invertResult=', invertResult
    th = Zen.Processing.Segmentation.ThresholdAutomatic(input, method, createBinary, invertResult, False)
    th.Name = 'Thresholded_' + str(id) + '.czi'
    if showresult:
        Zen.Application.Documents.Add(th)
        
    return th

    
def Sobel(input, thirdDim=ZenThirdProcessingDimension.None, id=0, showresult=True):
    # apply sobel filter
    print '* Sobel Filter ...'
    print '3rd Dimenension=', thirdDim
    sobel = Zen.Processing.Filter.Edges.Sobel(input, ZenSobelMode.Clip, thirdDim, False)
    sobel.Name = 'SoblelFilter_' + str(id) + '.czi'
    if showresult:
        Zen.Application.Documents.Add(sobel)
        
    return sobel


def FillHoles(input, id=0, showresult=True):
    # fill holes inside binary image
    print '* Filling Holes ...'
    fh = Zen.Processing.Binary.FillHoles(input)
    fh.Name = 'FillHoles_' + str(id) + '.czi'
    if showresult:
        Zen.Application.Documents.Add(fh)
        
    return fh
        

def MorphoDilate(input, count=3, elem=ZenStructureElement.Square, binary=True, id=0, showresult=True):
    # apply dilate operation
    print '* Morphology Dilate ...'
    print 'Count=', count, ' Binary=', binary, ' Structure Element=', elem
    mdl = Zen.Processing.Morphology.Dilate(input, count, binary, elem, False)
    mdl.Name = 'MorphoDilate_' + str(id) + '.czi'
    if showresult:
        Zen.Application.Documents.Add(mdl)
        
    return mdl


def MorphoTopHatWhite(input, count=3, elem=ZenStructureElement.Square, id=0, showresult=True):
    # apply TopHatWhite Filter
    print '* Morphology TopHatWhite ...'
    print 'Count=', count, ' Structure Element=', elem
    thw = Zen.Processing.Morphology.TopHatWhite(input, count, elem, False)
    thw.Name = 'TopHatWhite_' + str(id) + '.czi'
    if showresult:
        Zen.Application.Documents.Add(thw)
        
    return thw


def MorphoClose(input, count=3, elem=ZenStructureElement.Octagon, binary=True, id=0, showresult=True):
    # apply morphological close operation
    print '* Morphology Close ...'
    print 'Count=', count, ' Binary=', binary,' Structure Element=', elem
    mcl = Zen.Processing.Morphology.Close(input, count, binary, elem, False)
    mcl.Name = 'MorphoClose_' + str(id) + '.czi'
    if showresult:
        Zen.Application.Documents.Add(mcl)
        
    return mcl


def Scrap(input, minarea=50, maxarea=100000, inrange=True, id=0, showresult=True):
    # scarp objects
    print '* Scrap Objects ...'
    print 'MinArea=', minarea, ' MaxArea=', maxarea,' Select in Range=', inrange
    scr = Zen.Processing.Binary.Scrap(input, minarea, maxarea, inrange, False)
    scr.Name = 'ScrapObjects_' + str(id) + '.czi'
    if showresult:
        Zen.Application.Documents.Add(scr)
        
    return scr

###########################################################################################################################
###########################################################################################################################

#filename = r'c:\Users\M1SRH\Documents\Testdata_Zeiss\Atomic\Neurons\neurons_T=1.czi'
filename = r'c:\Users\M1SRH\Documents\Testdata_Zeiss\Atomic\Neurons\neurons.ome.tiff'

# clear console output
Zen.Application.MacroEditor.ClearMessages()
Zen.Application.Documents.RemoveAll(False)

# load and show the original image
orig = Zen.Application.LoadImage(filename, False)
#Zen.Application.Documents.Add(out)

runpipes = {'0': [False, 0],
            '1': [True, 1],
            '2': [False, 2],
            '3': [False, 3]}


if runpipes['0'][0]:
    # pipeline 0
    print '\n-----   Running Pipeline-0 -----'
    pipe = runpipes['0'][1]
    #out0 = CorrectIllumination(orig, lowpasscount=3, kernelsize=50, id=pipe, showresult=True)
    out0 = RollingBall(orig, radius=50, createBackground=False, doPreSmooth=False, isLightBackground=False, id=pipe, showresult=True)
    #out0 = MedianFilter(out0, radius=3, id=pipe, showresult=True)
    #out0 = AutoThreshold(out0, method=ZenThresholdingMethod.ThreeSigmaThreshold, createBinary=True, invertResult=False, id=pipe, showresult=True)
    out0 = AutoThreshold(out0, method=ZenThresholdingMethod.TriangleThreshold, createBinary=True, invertResult=False, id=pipe, showresult=True)
    out0 = Scrap(out0, minarea=50, maxarea=100000, inrange=True, id=pipe, showresult=True)
    out0 = MorphoClose(out0, count=2, elem=ZenStructureElement.Octagon, binary=True, id=pipe, showresult=False)
    #out0 = AutoThreshold(out0, method=ZenThresholdingMethod.Otsu, createBinary=True, invertResult=False, id=pipe, showresult=True)
    #out0 = Zen.Processing.Segmentation.Threshold(out0, 15, 255, False)
    #Zen.Application.Documents.Add(out0)
    out0 = FillHoles(out0, id=pipe, showresult=True)
    #out0 = MorphoClose(out0, count=3, elem=ZenStructureElement.Octagon, binary=True, id=pipe, showresult=True)
    out0 = MorphoDilate(out0, count=1, elem=ZenStructureElement.Octagon, binary=True, id=pipe, showresult=True)



if runpipes['1'][0]:
    # pipeline 1
    print '\n-----   Running Pipeline-1 -----'
    pipe = runpipes['1'][1]
    out1 = CorrectIllumination(orig, lowpasscount=3, kernelsize=50, id=pipe, showresult=False)
    out1 = RollingBall(out1, radius=50, createBackground=False, doPreSmooth=False, isLightBackground=False, id=pipe, showresult=False)
    out1 = MedianFilter(out1, radius=2, id=pipe, showresult=True)
    out1 = Sobel(out1, thirdDim=ZenThirdProcessingDimension.None, id=pipe, showresult=True)
    out1 = MedianFilter(out1, radius=3, id=pipe, showresult=True)
    #out1 = Zen.Processing.Arithmetics.Inversion(out1)
    #Zen.Application.Documents.Add(out1)
    
    out1 = AutoThreshold(out1, method=ZenThresholdingMethod.ThreeSigmaThreshold, createBinary=True, invertResult=False, id=pipe, showresult=False)
    #out1 = AutoThreshold(out1, method=ZenThresholdingMethod.TriangleThreshold, createBinary=True, invertResult=False, id=pipe, showresult=True)
    #out1 = AutoThreshold(out1, method=ZenThresholdingMethod.Otsu, createBinary=True, invertResult=False, id=pipe, showresult=True)
    out1 = FillHoles(out1, id=pipe, showresult=True)
    #out1 = MorphoClose(out1, count=3, elem=ZenStructureElement.Octagon, binary=True, id=pipe, showresult=True)
    #out1 = MorphoDilate(out1, count=1, elem=ZenStructureElement.Octagon, binary=True, id=pipe, showresult=False)



if runpipes['2'][0]:
    # pipeline 2
    print '\n-----   Running Pipeline-2 -----'
    pipe = runpipes['2'][1]
    out2 = CorrectIllumination(orig, lowpasscount=3, kernelsize=50, id=pipe, showresult=False)
    out2 = MorphoTopHatWhite(out2, count=3, elem=ZenStructureElement.Square, id=pipe, showresult=False)
    out2 = MedianFilter(out2, radius=5, id=pipe, showresult=False)
    #out2 = AutoThreshold(out2, method=ZenThresholdingMethod.ThreeSigmaThreshold, createBinary=True, invertResult=False, id=pipe, showresult=False)
    out2 = AutoThreshold(out2, method=ZenThresholdingMethod.TriangleThreshold, createBinary=True, invertResult=False, id=pipe, showresult=False)
    #out2 = AutoThreshold(out2, method=ZenThresholdingMethod.Otsu, createBinary=True, invertResult=False, id=pipe, showresult=True)
    out2 = FillHoles(out2, id=pipe, showresult=True)

    

if runpipes['3'][0]:
    # pipeline 3
    print '\n-----   Running Pipeline-3 -----'
    pipe = runpipes['3'][1]
    print 'Combining images using OR ...'
    out3 = Zen.Processing.Binary.Or(out2, out0, False)
    out3 = Zen.Processing.Binary.Or(out3, out1, False)
    out3 = Scrap(out3, minarea=50, maxarea=100000, inrange=True, id=pipe, showresult=True)
