# Run ApoTome Processing automatically after acquisition
# Script by Sven Terclavers - Sven.Terclavers@zeiss.com

from System.IO import File, Directory, FileInfo, Path
OutImage = r'C:\\ZEN_Output'

#Read Active Image &amp; prepare Output Image

image = Zen.Application.Documents.ActiveDocument

#Process ApoTome Active Raw Image

nb_phase= image.Bounds.SizeH
apotome_image= Zen.Processing.Utilities.ApoTomeSimConvert(image, ZenApoTomeProcessingMode.Sectioned, ZenSimCorrectionMode.LocalIntensity, ZenNormalizeMode.Clip, ZenApoTomeFilter.Off, False)
Zen.Application.Documents.Add(apotome_image)

#Save Processed file

image_name= image.Name.Replace('.czi', '_Apotome.czi')
imageName = Path.Combine(OutImage,image_name)
apotome_image.Save(imageName)
