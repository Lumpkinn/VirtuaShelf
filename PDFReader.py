from pypdf import PdfReader
#i = 0
class pdfread():
     #sets up path to correct file, and creates a reader for it
     
     def __init__(self, ):
          #i += 1
          #this part ONLY extracts the text. set images to True to include images
          #This extracts both the images, and the text from the PDF file
          #else:
               #IDEA: Maybe just display the pdf as an image? I think that would save me some issues.
               pass

     #gets the text + images from the data.
     def getdata(self, path, images=False):
          if images == False:

               pdf = self.reader = PdfReader(path)
               currentpage = pdf.pages[1]
          return currentpage.extract_text(extraction_mode="layout")
     
