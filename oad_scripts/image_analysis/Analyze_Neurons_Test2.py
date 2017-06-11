"""
Author: Sebastian Rhode
Date: 2017_03_03
File: Analyze_Neurons_Test2.czmac
Version: 0.1
"""

import sys
sys.path.append(r'c:\Users\M1SRH\Documents\Projects\OAD\External_Python_Scripts_for_OAD')

import SegmentationTools as st

#filename = r'c:\Users\M1SRH\Documents\Testdata_Zeiss\Atomic\Neurons\neurons_T=1.czi'
filename = r'c:\Users\M1SRH\Documents\Testdata_Zeiss\Atomic\Neurons\neurons.ome.tiff'

# clear console output
Zen.Application.MacroEditor.ClearMessages()
Zen.Application.Documents.RemoveAll(False)

# load and show the original image
orig = Zen.Application.LoadImage(filename, False)
Zen.Application.Documents.Add(orig)

runpipes = {'0': [True, 0],
            '1': [False, 1],
            '2': [False, 2]}


if runpipes['0'][0]:
    # pipeline 0
    print '\n-----   Running Pipeline-0 -----'
    pipe = runpipes['0'][1]
    out0 = st.CorrectIllumination(orig, lowpasscount=3, kernelsize=200, id=pipe, showresult=False)
    out0 = st.RollingBall(out0, radius=50, createBackground=False, doPreSmooth=True, isLightBackground=False, id=pipe, showresult=False)
    out0 = st.MedianFilter(out0, radius=2, id=pipe, showresult=True)
    out0 = st.AutoThreshold(out0, method=ZenThresholdingMethod.TriangleThreshold, createBinary=True, invertResult=False, id=pipe, showresult=True)
    #out0 = st.MorphoDilate(out0, count=1, elem=ZenStructureElement.Octagon, binary=True, id=pipe, showresult=True)
    out0 = st.MorphoClose(out0, count=3, elem=ZenStructureElement.Octagon, binary=True, id=pipe, showresult=False)
    out0 = st.Scrap(out0, minarea=200, maxarea=100000, inrange=True, id=pipe, showresult=True)
    #out0 = st.FillHoles(out0, id=pipe, showresult=True)



if runpipes['1'][0]:
    # pipeline 1
    print '\n-----   Running Pipeline-1 -----'
    pipe = runpipes['1'][1]
    out1 = st.CorrectIllumination(orig, lowpasscount=3, kernelsize=50, id=pipe, showresult=False)
    out1 = st.MorphoTopHatWhite(out1, count=3, elem=ZenStructureElement.Square, id=pipe, showresult=False)
    out1 = st.MedianFilter(out1, radius=5, id=pipe, showresult=False)
    out1 = st.AutoThreshold(out1, method=ZenThresholdingMethod.TriangleThreshold, createBinary=True, invertResult=False, id=pipe, showresult=False)
    out1 = st.FillHoles(out1, id=pipe, showresult=True)



if runpipes['2'][0]:
    # pipeline 2
    print '\n-----   Running Pipeline-2 -----'
    pipe = runpipes['2'][1]
    print 'Combining images using OR ...'
    out2 = Zen.Processing.Binary.Or(out1, out0, False)
    out2 = st.Scrap(out2, minarea=50, maxarea=100000, inrange=True, id=pipe, showresult=True)
