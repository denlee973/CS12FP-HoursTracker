from Tkinter import *
from abc import ABCMeta, abstractmethod


class Master:
    __metaclass__ = ABCMeta
    text = []
    def __init__(self):
        self.menubar = Menu(window)
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_cascade(label="Settings", command=self.settings)
        self.filemenu.add_cascade(label="Order")
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        window.config(menu = self.menubar)

        
    # def settings(self):
    #     pass
    
    def readFile(self,filename):
        f = open('data.txt','r')
        self.text = f.readlines()
        f.close
        for i in range(len(self.text)-1):
            self.text[i] = self.text[i][0:len(self.text[i])-1]
        print self.text
        return self.text
            
    # def reWriteFile(filename):
    #     f = open('data.txt', 'r+w')
    #     
class LogIn(Master):
    username = ""
    __password = ""
    
    def __init__(self,window):
        self.window = window
        window.geometry("200x100")
        window.title("Hours Tracker - Log In")
        
        # username and password labels
        self.userlbl = Label(text="Username:")
        self.userlbl.grid(row=1, column=1)
        self.passlbl = Label(text = "Password:")
        self.passlbl.grid(row=2, column=1)
        
        # username and password input
        self.user = Entry(window)
        self.user.grid(row=1, column=2)
        self.passw = Entry(window, show="*")
        self.passw.grid(row=2, column=2)
        
        # login button
        self.login = Button(window, text="Log In", command=self.checkUserPass)
        self.login.grid(row=3, column=1, columnspan=2)
        
    # checks if username and password match
    def checkUserPass(self):
        self.u = self.user.get()
        self.p = self.passw.get()
        if self.u == self.readFile('data.txt')[0] and self.p == self.readFile('data.txt')[1]:
            self.window.withdraw()
            self.window = Home(Toplevel(self.window))
            print "You have logged in."
            return True
        else:
            return False
        
class Home(Master):
    listEvents = []
    listButtonNames = []
    order = "TitleA"
    
    def __init__(self,window):
        self.window = window
        window.title("Hours Tracker - Home")
        
        self.search = Entry(window)
        self.search.grid(row=1, column=2, columnspan=2)
        # self.searchEnter = Button(window)
window = Tk()

login = LogIn(window)
window.mainloop()
    