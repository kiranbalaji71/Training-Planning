from pathlib import Path
from pypdf import PdfReader, PdfWriter, PdfMerger 
from pdf2image import convert_from_bytes
import pypdfium2 as ium
from PIL import Image


# Splitting the pdf file
inputPath = Path('./inputfile/sample.pdf')
inputFile = PdfReader(inputPath)
for index,page in enumerate(inputFile.pages[0:4]):
    outputFile = PdfWriter()
    outputFile.add_page(page)
    outputFile.write(f"./outputfile/Spilt{index+1}.pdf")
print("Spilt have done!!!")

# Merging the pdf file
mergePath = Path('./merge_input')
outputMerge = PdfMerger()
for page in mergePath.glob('*.pdf'):
        outputMerge.append(page)

outputMerge.write('./outputfile/Merge.pdf')
print("Merge have done!!!")

# Cropping the pdf file
cropPath = Path('./inputfile/sample.pdf')
cropInput = PdfReader(cropPath)
cropOutput = PdfWriter()
singlePage = cropInput.pages[4]
singlePage.mediabox.upper_left = [550, 0]
singlePage.mediabox.upper_right = [50, 112]
cropOutput.add_page(singlePage)
cropOutput.write('./outputfile/Crop.pdf')
print('Crop have done!!!')

# Tilting the pdf File
tiltOutput = PdfWriter()
tiltPage = cropInput.pages[5]
tiltPage.rotate(90)
tiltOutput.add_page(tiltPage)
tiltOutput.write('./outputfile/Tilt.pdf')
print('Tilt have done!!!')

#convert pdf to jpeg
pdf = ium.PdfDocument("./inputfile/sample.pdf")
page = pdf[4]
image = page.render(scale=4).to_pil()
image.save("./outputfile/pdf_to_image.jpg")
print("PDF convert to JPEG")

#convert jpg to pdf
image1 = Image.open(r'./outputfile/pdf_to_image.jpg')
outputImage = image1.convert('RGB')
outputImage.save(r'./outputfile/image_to_pdf.pdf')
print("Image convert to PDF")