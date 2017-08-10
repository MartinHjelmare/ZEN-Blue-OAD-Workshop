#
# Generated automatically a timestitching for MultiBlock acquisition (ie: Experiment Designer)
# created by: Julien KISSENBERGER (ZEISS Fr)
#

image= Zen.Application.Documents.ActiveDocument


if (image.IsZenMultiBlockImage == True):
    block_count= image.AcquisitionBlockCount
    for i in range (0, block_count):
        timestitching= Zen.Processing.Utilities.MultiBlockTimeStitching(image,image.SelectBlockIndices(i))
        Zen.Application.Documents.Add(timestitching)
