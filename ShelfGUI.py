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
data = os.listdir("Data")
SelectedFile = ""

#Instances of each file opener for the openfile method

TXT_reader = TXTReader.txtReader() 
PDF_reader = PDFReader.pdfread()
HTML_reader = HTMLReader.htmlinfo()
EPUB_reader = EPUBReader.reader()

#Method to make popup windows.
def popup(PopupText, PopUpTitle):
     popupwindow = ctk.CTk()
     popupwindow.geometry("200x100")
     popupwindow.title(PopUpTitle)
     label = ctk.CTkLabel(popupwindow, text=PopupText, fg_color="brown", corner_radius=8, border_color="dark brown")
     popupwindow.mainloop()

#Checks all the files in the directory, and lets the user know if any of them are not supported.

#Long and short of the issue is basically just the fact that we're in the WRONG DIRECTORY!!!!!! title is also just not getting copied to it sooo
for i in range(0, len(os.listdir("Data"))):
     info = data[i].split('.')
     print(info)

     #Splitting the info into two arrays!
     for i in range(0, len(info)):
          if i % 2 == 0:
               title.append(info[i])
          elif i % 2 == 1:
               type.append(info[i])

     #make sure to check if this will immediately close out of the program
     #WHAT IS THE IF STATEMENT DOING???????
     match type[0]:
          case 'pdf':
               print("yay")
               break
          case 'txt':
               break
          case 'html':
               break
          case 'epub':
               break
          case _:
               print("bad eval")
               popup("File type not supported!" , "The data folder contains an unsupported file type. The folder must only contain either html, epub, txt, or pdf files. If you continue to see this message after clearing out the folder of any unwanted files, check for hidden files, and if the issue persists, create an issue on the github page.")
               quit()
          


#What I need to do here is just set up a ctk window, make a stored array of the books (Persistent storage), and have them return the info
class bookShelf (ctk.CTk):

     def openfiles(filename:str, filetype:str):
          #TODO: make the data returned from the instance get stored into a file, and then use the data to open the text viewer. 
          #ADD THE REST OF THE PATH STUFF!!!! IT WON'T KNOW OTHERWISE!!!
          path = ("Data/"+str(filetype))
          print(path)
          SelectedFile = Path(path)
          toDisplay = ""
          if filetype == "txt":
               toDisplay = TXT_reader.fileOpen(SelectedFile)
          elif filetype == "html":
               toDisplay = HTML_reader.text(SelectedFile)
          elif filetype == "epub":
               toDisplay = EPUB_reader.read(SelectedFile) 
          else:
               toDisplay = PDF_reader.getdata(SelectedFile)

          readerframe = ctk.CTk()
          readerframe.title(filetype)
          #readerframe.geometry(1000,1000)
          frame = ctk.CTkFrame(readerframe, 950, 950)
          frame.grid(row=1, column=1,padx=20,pady=10)
          label = ctk.CTkLabel(frame,text=toDisplay)
          label.grid(row=1,column=1,padx=20,pady=20)
          readerframe.mainloop()


     def __init__(self):
          def open():
               self.openfiles(paramerter)
          super().__init__()
          #sets the size of the window! (Tweak this later!)
          #self.configure.set_widget_scaling(5.0)
          self.resizable(False, False)
          #Tweak these colors later to seem more homey
          self.itemFrame = ctk.CTkFrame(self, fg_color="gray", border_color="black")
          self.title("Your Shelf!")
          self.label = ctk.CTkLabel(self, text="Your Shelf!")
          self.label.grid(row=1, column=0, padx=20, pady=20, sticky="ew")
          #Make an array of buttons that'll have the titles on them; the types will be saved for future reference
          buttonarr = []
          
          for i in range(0, len(title)):
               #get the filename to get split with /n to make the titles vertical 
               paramerter:str = title[i] +"."+ type[i]
               self.button = ctk.CTkButton(self, text=title[i], bg_color=random.choice(bookcolor), )#, type[i]) )
               self.button.configure(command=open)
               self.button.grid(row=1,column=i, padx=20,pady=20, sticky="ew")
               buttonarr.append(self.button)
     
          self.mainloop()
          
huh = bookShelf()