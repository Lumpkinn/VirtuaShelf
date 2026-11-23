
from ebooklib import epub
import ebooklib
import io
class reader():

     def __init__(self):
          pass
     
     def read(self, path):
          book = epub.read_epub(io.BytesIO(open(path,'rb').read()))
          for doc in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
               return doc.content
          