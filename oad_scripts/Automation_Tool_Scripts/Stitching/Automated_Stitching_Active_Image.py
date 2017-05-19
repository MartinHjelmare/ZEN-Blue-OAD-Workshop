# Run Stitching automatically after acquisition
# Script by Sven Terclavers - Sven.Terclavers@zeiss.com

from System.IO import File, Directory, FileInfo, Path

image = Zen.Application.Documents.ActiveDocument

Stitchset = r'Stitching_Channel_1.czips'
functionsetting1 = Zen.Processing.Transformation.Geometric.Stitching(image)
functionsetting1.Load(Stitchset)

# End
