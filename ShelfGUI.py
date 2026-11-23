#TODO: fix the file detection system.

from pathlib import Path
from playsound3 import playsound
import customtkinter as ctk
import os, random
import TXTReader, PDFReader, HTMLReader, EPUBReader

# Colors for later use (Vet this!! light colors are making it hard to see text!!!)

bookcolor = ["red", "blue", "green", "SteelBlue", "orange", "violet", "dark green", "dark blue", "dark red", "maroon", "grey", "crimson", "DarkOrchid4", "DarkOliveGreen" ]

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
     label.grid(row=1,column=1,padx=20,pady=20)
     popupwindow.mainloop()

#Checks all the files in the directory, and lets the user know if any of them are not supported.
for i in range(0, len(os.listdir("Data"))):
     info = data[i].split('.')
     #Splitting the info into two arrays!
     for i in range(0, len(info)):
          if i % 2 == 0:
               title.append(info[i])
          elif i % 2 == 1:
               type.append(info[i])

     #make sure to check if this will immediately close out of the program
     for i in range(0,1):
          match type[0]:
               case 'pdf':
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
     #Function vetted, nothing wrong here
     def openfiles(filename,filetype:str, type):
          #plays sfx
          sfx = 'Select.wav'
          playsound(sfx)
          print("I'm being called!")
          #gets path, and opens file
          path = ("Data/"+str(filetype))
          
          SelectedFile = Path(path)
          
          toDisplay = "?"
          
          if type == "txt":
               toDisplay = TXT_reader.fileOpen(SelectedFile)
               print(toDisplay + "txt")
          elif type == "html":
               toDisplay = HTML_reader.text(SelectedFile)
               print(toDisplay+"Html")
          elif type == "epub":
               print("Unfortunately, this currently doesn't work..")
               toDisplay = EPUB_reader.read(SelectedFile) 
               print(toDisplay+"epub")
          else:
               toDisplay = PDF_reader.getdata(SelectedFile)
          readerframe = ctk.CTk()
          readerframe.title(filetype)
          readerframe.configure(corner_radius=8, border_width=2,fg_color="burlywood4")
          frame = ctk.CTkFrame(readerframe, 950, 950 , corner_radius=8, border_width=2,fg_color="cornsilk2")
          frame.grid(row=1, column=1,padx=20,pady=10)
          label = ctk.CTkLabel(frame,text=toDisplay, justify="left",width=100, anchor="center", wraplength=1000 )
          label.grid(row=1,column=1,padx=20,pady=20)
          readerframe.mainloop()

     def __init__(self):
          #Basic setup for the frame. Most likely not here     
          super().__init__()
          self.resizable(False, False)
          self.configure(fg_color="chocolate4")
          self.itemFrame = ctk.CTkFrame(self, fg_color="cornsilk2", border_color="burlywood4",corner_radius=8, border_width=2)
          self.itemFrame.grid(row=1,column=1,padx=10,pady=10)
          self.title("Your Shelf!")
          self.label = ctk.CTkLabel(self, text="Your Shelf!", corner_radius=8, border_width=2,fg_color="cornsilk2")
          self.label.grid(row=1, column=0, padx=20, pady=20, sticky="ew")
          
          #Juicy stuff from here on out
          
          #Make an array of buttons that'll have the titles on them; the types will be saved for future reference
          buttonarr = []
          #Holds the types of each file, in parallel
          fileinfo = ""
          #Possible hint? = THE ISSUE IS THAT THE PARAMETER IS ONLY BEING ASSIGNED A VALUE EITHER ONCE, OR IS LANDINF ON THE LAST POSSIBLE VALUE!!! MAKE IT AN ARRAY TO STORE DATA, AND PASS THE UNIQUE SIGNATURE TO THE OPEN METHOD
          print(title)
          print(type)

     #Possible idea: have one variable thats set as the parameter for open. The value for the variable is just the title of the button, which will end up being unique depending on the button
     #TODO: comfigure the file types outside of the loop
          #Loops through the number of files
          for i in range(0, len(title)):
               #get the filename to get split with /n to make the titles vertical 
               #adds all of the filenames with their type attached to the parametertype array
               #initaliizes buttons
               self.button = ctk.CTkButton(self.itemFrame, text=(title[i]+"."+type[i]), fg_color=random.choice(bookcolor), )#, type[i]) )
               #shows buttons
               self.button.grid(row=1,column=i, padx=20,pady=20, sticky="ew")
               #adds button to array.
               buttonarr.append(self.button)
          
               print("im actually going through the buttons")
               if self.button.cget("text").split('.')[1] == 'txt':
                    print('txt')
                    fileinfo = title[i]+"."+type[i]
                    infotype = 'txt'
                    
               if self.button.cget("text").split('.')[1] == 'pdf':
                    print(title[i]+"."+type[i]+"huh")
                    fileinfo = title[i]+"."+type[i]
                    infotype='pdf'
                    
               if self.button.cget("text").split('.')[1] == 'html':
                    print('html')
                    infotype='html'
                    fileinfo = title[i]+"."+type[i]
                    
               if self.button.cget("text").split('.')[1] == 'epub':
                    print('epub')
                    infotype = 'epub'
                    fileinfo = title[i]+"."+type[i]
               
               
               self.button.configure(command=lambda fileinfo=fileinfo, infotype=infotype: self.openfiles(fileinfo, infotype))
                    
          
          self.mainloop()
          "Data/lorem-ipsum.epub"
huh = bookShelf()