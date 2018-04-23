from Tkinter import *

class Home():
    listEvents = [[]]
    listButtonNames = []
    order = ""
    
    def __init__(self,window,lE):
        self.window = window
        self.listEvents = lE
        window.title("Hours Tracker - Home")
        
        self.search = Entry(window)
        
    
    