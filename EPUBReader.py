from ebooklib import epub

class reader():

     def __init__(self):
          pass
     
     def read(self, path):
          book = epub.read_epub(path)
          