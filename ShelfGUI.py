#This is done for now. I need to work on the rest of the file opener classes, make instances of them, and call them in the openfile method. (Realistically, I'll need to make my own file viewer, which will be doen by having the fileopeners return all the data as text. The text will then be displayed with the custom file viewer)
import customtkinter as ctk
import os, random
from pathlib import Path
import TXTReader, PDFReader, HTMLReader, EPUBReader

# Colors for later use
bookcolor = ["red", "blue", "green","yellow","orange","violet","dark green","dark blue","dark red","maroon","light grey","light blue","pink"]

#Get the title's from the data folder.
title = []
type = []
#get the path to the data file
data = os.listdir()
SelectedFile = ""

#Instances of each file opener for the openfile method

TXT_reader = TXTReader.txtReader() 
PDF_reader = PDFReader.pdfread()
HTML_reader = HTMLReader.htmlinfo()
EPUB_reader = EPUBReader.reader()

#Method to make popup windows.
def popup(PopupText, PopUpTitle):
     popupwindow = ctk.CTK()
     popupwindow.geometry("200x100")
     popupwindow.title(PopUpTitle)
     label = ctk.CTkLabel(popupwindow, text=PopupText, fg_color="brown", corner_radius=8, border_color="dark brown")

#Checks all the files in the directory, and lets the user know if any of them are not supported.
for i in range(0, len(os.listdir("Data"))):
     info = data[i].split('.')
     #make sure to check if this will immediately close out of the program
     if not(title[1].equals("pdf")) or not (title[1].equals("txt")) or not(title[1].equals("epub")) or not (title[1].equals("html")):
          popup("File type not supported","The data folder contains an unsupported file type. The folder must only contain either html, epub, txt, or pdf files. If you continue to see this message after clearing out the folder of any unwanted files, check for hidden files, and if the issue persists, create an issue on the github page.")
          os.quit()
     else:
          title.append(info[0])
          type.append(info[1])



#What I need to do here is just set up a ctk window, make a stored array of the books (Persistent storage), and have them return the info
class Shelf (ctk.CTk):

     def openfile(filename, filetype):
          #TODO: make the data returned from the instance get stored into a file, and then use the data to open the text viewer. 
          #ADD THE REST OF THE PATH STUFF!!!! IT WON'T KNOW OTHERWISE!!!
          SelectedFile = Path("VirtuaShelf/Data/" + filename + '.' + filetype)
          toDisplay = ""
          if filetype == "txt":
               toDisplay = TXT_reader.fileOpen(SelectedFile)
          elif filetype == "html":
               toDisplay = HTML_reader.text(SelectedFile)
          elif filetype == "epub":
               toDisplay = EPUB_reader.read(SelectedFile) 
          else:
               PDF_reader.get_data(SelectedFile)
               toDisplay = PDF_reader.getdata(SelectedFile)



     def digireader(title, text):
          readerframe = ctk.CTk()
          readerframe.title(title)
          readerframe.geometry(1000,1000)
          frame = ctk.CTkFrame(readerframe, 950, 950)
          label = ctk.CTkLabel(frame,text=text)
          readerframe.mainloop()


     def __init__(self):
          super().__init__()
          #sets the size of the window! (Tweak this later!)
          self.configure.set_widget_scaling(5.0)
          self.resizable(False, False)
          #Tweak these colors later to seem more homey
          self.itemFrame = ctk.CTkFrame(self, fg_color="gray", border_color="black")

          #Make an array of buttons that'll have the titles on them; the types will be saved for future reference
          buttonarr = []
          for i in range(0, title.length):
               #get the filename to get split with /n to make the titles vertical 
               button = ctk.CTkButton(self, text=title[i], command=self.openfile(title[i],type[i]), bg_color=random.choice(bookcolor))
               buttonarr.append(button)
     
          self.mainloop()
          
     