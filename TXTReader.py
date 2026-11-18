#Yea this is more a formailty if anything, but ill do it anyway

class txtReader():
     info = ""
     
     def __init__(self):
          pass
     
     def fileOpen(self, path):
          
          with open (path) as file:
              info = file.read() 
          
          return info
     