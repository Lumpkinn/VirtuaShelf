import customtkinter as ctk
import os

#Method to make popup windows.

def popup(PopupText, PopUpTitle):
     popupwindow = ctk.CTK()
     popupwindow.geometry("200x100")
     popupwindow.title(PopUpTitle)
     label = ctk.CTkLabel(popupwindow, text=PopupText, fg_color="brown", corner_radius=8, border_color="dark brown")





#Get the title's from the data folder.
title = []
#get the path to the data file
data = os.listdir()
#iterate though the array
for i in range():
     title = data[i].split('.')
     if not(title[1].equals("pdf")) or not (title[1].equals("txt")) or not(title[1].equals("epub")) or not (title[1].equals("html")):
          popup("File type not supported","The data folder contains an unsupported file type. The folder must only contain either html, epub, txt, or pdf files. If you continue to see this message after clearing out the folder of any unwanted files, check for hidden files, and if the issue persists, create an issue on the github page.")
          os.quit()
          pass



#What I need to do here is just set up a ctk window, make a stored array of the books (Persistent storage), and have them return the info

class Shelf (ctk.CTK):
     def __init__(self):
          super().__init__()
          #sets the size of the window! (Tweak this later!)
          self.configure.set_widget_scaling(5.0)
          self.resizable(False, False)
          #Tweak these colors later to seem more homey
          self.itemFrame = ctk.CTkFrame(self, fg_color="gray", border_color="black")
