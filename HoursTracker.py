from Tkinter import *
import ttk
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

        
    def settings(self):
        pass
    
    def readFile(self,filename):
        f = open(filename,'r')
        self.text = f.readlines()
        f.close
        for i in range(len(self.text)-1):
            self.text[i] = self.text[i][0:len(self.text[i])-1]
        for j in range(len(self.text)):
            self.text[j] = self.text[j].split("/t")
        print self.text
        return self.text
    
    def combobox(self,listv):
        self.varname = ttk.Combobox(window)
        self.varname['values'] = listv
        self.varname.current(0)
        return self.varname
    
    def retrieve(self,submitData,numElement,listn):
        for i in range(numElement-1):
            self.item = self.listn[i].get()
            self.data[0].append(self.item)
        if submitData == "newentry":
            self.addToFile('data.txt',self.data)
        self.data = [[]]
            
    def addToFile(self,filename,adding):
        f = open(filename,'a')
        for i in range(len(adding)):
            line = "\n"
            for j in range(len(adding[i])):
                line += str(adding[i][j])+"/t"
            print line
            f.write(line)
        f.close()
            
        
class LogIn(Master):
    username = ""
    __password = ""
    
    def __init__(self,window):
        Master.__init__(self)
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
        if self.u == self.readFile('data.txt')[0][0] and self.p == self.readFile('data.txt')[1][0]:
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
    search = ""
    
    def __init__(self,window):
        Master.__init__(self)
        self.window = window
        window.title("Hours Tracker - Home")
        window.geometry("1000x1000")
        
        # search items
        self.search = Entry(window)
        self.search.grid(row=1, column=1, columnspan=4)
        self.searchIcon = PhotoImage(file="searchIcon.gif")
        self.searchEnter = Button(window, image=self.searchIcon)
        self.searchEnter.grid(row=1, column=5)
        
        # list of inputted events
        self.listEvents = self.readFile('data.txt')[2:]
        print "hi",self.listEvents
        # self.listEvents.sort()
        
        # can you make listbox with different columns?
        self.listbox = Listbox(window)
        self.listbox.grid(row=2, column=1)
        
        for i in range(len(self.listEvents)):
            self.listbox.insert(i, self.listEvents[i][0])
            
class NewEntry(Master):
    attributes = ["Subject:","Names:","Date:","Time Start:","Or Length:","Other Info:"]
    months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
    years = [2017,2018,2019,2020,2021,2022,2023,2024,2025,2026,2027,2028,2029,2030]
    data = [[]]
    
    def __init__(self,window):
        Master.__init__(self)
        self.window = window
        window.title = "Hours Tracker - New Entry"
        
        # creating labels for the inputs
        for i in range(len(self.attributes)):
            self.newLbls = Label(window, text=self.attributes[i])
            self.newLbls.grid(row=i, column=1)
        self.endTime = Label(window, text="End:")
        self.endTime.grid(row=3, column=3)
            
        # generating and grid-ing the input stuff
        self.subject = Entry(window, width=70)
        self.names = Entry(window, width=70)
        self.subject.grid(row=0, column=2, columnspan=3)
        self.names.grid(row=1, column=2, columnspan=3)
        
        self.month = self.combobox(self.months)
        self.day = self.combobox(self.days)
        self.year = self.combobox(self.years)
        self.month.grid(row=2, column=2)
        self.day.grid(row=2, column=3)
        self.year.grid(row=2, column=4)
        
        self.tstart = Entry(window)
        self.tend = Entry(window)
        self.tstart.grid(row=3, column=2)
        self.tend.grid(row=3, column=4)
        
        self.length = Entry(window, width=70)
        self.length.grid(row=4, column=2, columnspan=3)
        
        self.info = Entry(window, width=70)
        self.info.grid(row=5, column=2, columnspan=3)
        
        self.listn = [self.subject,self.names,self.month,self.day,self.year,self.tstart,self.tend,self.length,self.info]

        self.submit = Button(window, text="Submit", command= lambda submitData="newentry", numElement=9, listn=self.listn: self.retrieve(submitData, numElement, listn))
        self.submit.grid(row=6, column=1, columnspan=4)
        
        
class CalculateHours(Master):
    pass
        
        
window = Tk()
newentry = NewEntry(window)
window.mainloop()
    