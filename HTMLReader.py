#TODO:
     # Parse the files into text
     # Embed images where they're supposed to be
     # add hyperlinks to text
#DONE:
     # got text from file.

#As of Version 0.0.9, this program will only support embedded images, and hyperlinks in html files. 
from PIL import image
from bs4 import BeautifulSoup

class htmlinfo():
     
     #This just gets all of the text
     def __init__(self, path):
          with open(path) as html_doc:
               soup = BeautifulSoup(html_doc, 'html.parser')     
          pass
     def text(self, path):
          return self.soup.get_text()
          