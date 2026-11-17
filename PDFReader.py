import pypdf

class pdfread():
     #sets up path to correct file, and creates a reader for it
     def __init__(self, path, images=False):
          #this part ONLY extracts the text. set images to True to include images
          if images == False:
               self.reader = pypdf.PdfReader(path)
          #This extracts both the images, and the text from the PDF file
          else:
               #IDEA: Maybe just display the pdf as an image? I think that would save me some issues.
               pass

     #gets the text + images from the data.
     def getdata(self):
          return self.reader.extract_text(extraction_mode("layout"))
