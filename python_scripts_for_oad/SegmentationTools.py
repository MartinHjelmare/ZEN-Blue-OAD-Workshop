"""
Author: Sebastian Rhode
Date: 2017_05_02
File: SegmentationTools.py
Version: 0.2
"""

import clr
clr.AddReferenceByPartialName("Zeiss.Micro")
clr.AddReferenceByPartialName("Zeiss.Micro.Scripting")
clr.AddReferenceByPartialName("Zeiss.Micro.LM.Scripting")
clr.AddReferenceByPartialName("Zeiss.Micro.Scripting.GUI")
from Zeiss.Micro.Scripting import *
from Zeiss.Micro.Scripting.Enumerations import *
Zen = ZenWrapperLM.Instance
ZenImage = ZenImageLM

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


def LocalVariance(input, kernelsize=9, normmethod=ZenFilteringMode.Auto, id=0, showresult=True):
    # LocalVarianceFilter
    print '* LOcalVariance Filter ...'
    print 'KernelSize=', kernelsize
    lvf = Zen.Processing.Filter.Edges.LocalVariance(input, kernelsize, normmethod, False)
    lvf.Name = 'LocalVariance_' + str(id) + '.czi'
    if showresult:
        Zen.Application.Documents.Add(lvf)

    return lvf
