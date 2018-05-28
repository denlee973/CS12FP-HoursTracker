

#-----------Denise Lee-----------
#---------timeTracker.py---------
#----------28 May 2018-----------
#------------ICS4U-01------------


# importing all libraries
from Tkinter import *
import tkFont
import xlsxwriter
import random
import datetime
import os
# import ttk
from abc import ABCMeta, abstractmethod

# Master -- parent class
class Master:
    # make Master abstract
    __metaclass__ = ABCMeta
    text = []
    # initializing Master
    # @param: none
    # @return: none
    def __init__(self):
        # setting default font size to 12
        default_font = tkFont.nametofont("TkDefaultFont")
        default_font.configure(size=12)
        
        # menus (but doesn't work for child classes, so each child class has the menus in their respective inits)
        # # first tier menus
        # self.menubar = Menu(window)
        # self.filemenu = Menu(self.menubar, tearoff=False)
        # self.viewmenu = Menu(self.menubar, tearoff=False)
        # self.helpmenu = Menu(self.menubar, tearoff=False)
        # 
        # 
        # # second tier menus
        # self.settingmenu = Menu(self.helpmenu, tearoff=False)
        # self.sortbymenu = Menu(self.viewmenu, tearoff=False)
        # 
        # self.menubar.add_cascade(label="File", menu=self.filemenu)
        # self.menubar.add_cascade(label="View", menu=self.viewmenu)
        # self.menubar.add_cascade(label="Help", menu=self.helpmenu)
        # self.filemenu.add("command", label="Home", command=lambda windname=Home: self.newPage(windname))
        # self.filemenu.add("command", label="New Entry", command=lambda windname=NewEntry: self.newPage(windname))
        # # self.filemenu.add("command", label="Calculate Hours", command=lambda windname=CalculateHours, events=[['','','','','','']]: self.newPage(windname,events))
        # self.helpmenu.add_cascade(label="Settings", menu=self.settingmenu)
        # self.viewmenu.add_cascade(label="Sort by", menu=self.sortbymenu)
        # self.sortbymenu.add("command", label="Subject")
        # 
        # window.config(menu = self.menubar)

    # creates a new window
    # @param: windname(window name):class, *args
    # @return: none
    def newPage(self,windname,*args):
        self.window.withdraw()
        self.window = windname(Toplevel(self.window),*args)
    
    # reads the given file
    # @param: filename:str
    # @return: self.text:str[[]]
    def readFile(self,filename):
        f = open(filename,'r')
        self.text = f.readlines()
        f.close
        for i in range(len(self.text)-1):
            self.text[i] = self.text[i][0:len(self.text[i])-1]
        for j in range(len(self.text)):
            self.text[j] = self.text[j].split("/t")
        return self.text
    
    # retrieves the data in given entry/spinboxes
    # @param: submitData:str, numElement:int, listn:[], other
    # @return: none
    def retrieve(self,submitData,numElement,listn,other):
        data = [[]]
        for i in range(len(listn)):
            item = listn[i].get()
            data[0].append(item)
        
        if submitData == "newacc":
            yourfile = str(random.randint(10000,99999))+".txt"
            f = open(yourfile,'w+')
            f.write(data[0][0]+'\n'+data[0][1])
            f.close()
            
            self.newPage(Home,yourfile)
            
        # if submitData == "calculate":
        #     self.foundTitle = []
        #     self.foundCategory = []
        #     self.foundName = []
        #     self.foundDate = []
        #     self.foundLength = []
        #     self.foundInfo = []
        #     self.foundAll = []
        #     self.foundList = [self.foundTitle,self.foundCategory,self.foundName,self.foundDate,self.foundLength,self.foundInfo,self.foundAll]
        #     self.displayList = [['','','','','','']]
        #     
        #     self.listEntry = self.readFile(self.yourfile)
        #     self.listEntry = self.listEntry[2:]
        #     for i in range(len(self.listEntry)):
        #         if self.listEntry[i][0].find(item) >= 0:
        #             self.foundTitle.append([self.listEntry[i][0],i])
        #         if self.listEntry[i][1].find(item) >= 0:
        #             self.foundCategory.append([self.listEntry[i][1],i])
        #         if self.listEntry[i][2].find(item) >= 0:
        #             self.foundName.append([self.listEntry[i][2],i])
        #         if self.listEntry[i][3].find(item) >= 0:
        #             self.foundDate.append([self.listEntry[i][3],i])
        #         if self.listEntry[i][4].find(item) >= 0:
        #             self.foundLength.append([self.listEntry[i][4],i])
        #         if self.listEntry[i][5].find(item) >= 0:
        #             self.foundInfo.append([self.listEntry[i][5],i])
        #     for i in range(5):
        #         for k in range(len(self.foundList[i])):
        #             self.foundAll.append(self.foundList[i][k])
        #             
        #     print self.foundList
        #     self.newPage(CalculateHours,item,self.foundList)
            
        if submitData == "search":
            self.newPage(Search,item,other)
        
        if submitData == "newentry":
            # date formatting to mm-dd-yyyy
            imon = data[0][3]
            date = ""
            for i in range(len(other)):
                if imon == other[i]:
                    if i <= 9:
                        date += "0"+str(i+1)+"-"
                    else:
                        date += str(i+1)+"-"
            if len(data[0][4]) < 2:
                date += "0"+data[0][4]+"-"+data[0][5]
            else:
                date += data[0][4]+"-"+data[0][5]
                
            for j in range(3):
                data[0].pop(3)
             
            data[0].insert(3,date)
            
            # calculating length
            if data[0][6] == "":
                if data[0][4].find("m") >= 0 or data[0][4].find("M") >= 0:
                    if data[0][4][-2:] == data[0][5][-2:]:
                        start = data[0][4][:-2].split(":")
                        end = data[0][5][:-2].split(":")
                        hrs = int(end[0])-int(start[0])
                        mins = int(end[1])-int(start[1])
                    elif (data[0][4].find("a") >= 0 or data[0][4].find("A") >= 0) and (data[0][5].find("p") >= 0 or data[0][5].find("P")):
                        start = data[0][4][:-2].split(":")
                        end = data[0][5][:-2].split(":")
                        hrs = int(end[0])-int(start[0])+12
                        mins = int(end[1])-int(start[1])
                else:
                    start = data[0][4].split(":")
                    end = data[0][5].split(":")
                    hrs = int(end[0])-int(start[0])
                    mins = int(end[1])-int(start[1])
                for r in range(3):
                    data[0].pop(4)
                if len(str(hrs)) < 2:
                    hrs = "0"+str(hrs)
                else:
                    hrs = str(hrs)
                if len(str(mins)) < 2:
                    mins = "0"+str(mins)
                else:
                    mins = str(mins)
                data[0].insert(4,hrs+":"+mins)
            elif data[0][3] == "":
                for r in range(2):
                    data[0].pop(4)
            self.addToFile(self.yourfile,data)
            self.newPage(Home,self.yourfile)
            
        self.data = [[]]
            
    def addToFile(self,filename,adding):
        f = open(filename,'a')
        for i in range(len(adding)):
            line = "\n"
            for j in range(len(adding[i])-1):
                line += str(adding[i][j])+"/t"
            line += str(adding[i][len(adding[i])-1])
            f.write(line)
        f.close()
    
    def exportData(self,yourfile):
        data = self.readFile(yourfile)[2:]
        workbook  = xlsxwriter.Workbook('timeTracker'+str(datetime.date.today())+'.xlsx')
        worksheet = workbook.add_worksheet()
        worksheet.set_column('A:A', 20)
        titles = ["Subject","Category","With","Date","Length","Info"]
        for r in range(6):
            worksheet.write(0,r,titles[r])
        for i in range(len(data)):
            for k in range(len(data[i])):
                worksheet.write(i+1, k, data[i][k])
        
        workbook.close()

class About(Master):
    def __init__(self,window,yourfile):
        Master.__init__(self)
        self.window = window
        window.geometry('500x300')
        window.title("timeTracker - About")
        Label(window, text="timeTracker 1.0\n2018\nBy Denise Lee\n*boop*").pack()        
        Button(window, text="Ok", command=lambda windname=Home, yourfile=yourfile: self.newPage(windname,yourfile)).pack()

class ExportXls(Master):
    def __init__(self,window,yourfile):
        Master.__init__(self)
        self.window = window
        window.geometry('500x80')
        window.title("timeTracker - Export Data")
        self.exportData(yourfile)
        Label(window, text="Data has been exported to timeTracker{}.xlsx".format(str(datetime.date.today()))).pack()        
        Button(window, text="Ok", command=lambda windname=Home, yourfile=yourfile: self.newPage(windname,yourfile)).pack()

class ClearData(Master):
    def __init__(self,window,yourfile):
        Master.__init__(self)
        self.window = window
        window.config(bg="red")
        window.geometry('410x100')
        window.title("timeTracker - Clear Data")
        self.yourfile = yourfile
        
        Label(window,bg="red", text="Are you sure you would like to clear all data?\nThis action is irreversible.".format(str(datetime.date.today()))).pack()        
        Button(window, text="Yes", command=lambda: self.clearFile()).pack(side=RIGHT)
        Button(window, text="Cancel", command=lambda windname=Home, yourfile=yourfile: self.newPage(windname,yourfile)).pack(side=RIGHT)
        
    def clearFile(self):
        acc = self.readFile(self.yourfile)[:2]
        os.remove(self.yourfile)
        self.yourfile = str(random.randint(10000,99999))+".txt"
        f = open(self.yourfile,'w+')
        f.write(acc[0][0]+'\n'+acc[0][1])
        f.close
        
        self.newPage(Home,self.yourfile)

class NewAcc(Master):
    def __init__(self,window):
        Master.__init__(self)
        self.window = window
        window.title("timeTracker - Create New Account")
        window.geometry("310x140")
        
        labels = ["Username:","Password:"]
        for k in range(2):
            Label(window, text=labels[k]).grid(row=k+1,column=1)
        
        self.userEnt = Entry(window)
        self.userEnt.grid(row=1, column=2)
        self.passEnt = Entry(window)
        self.passEnt.grid(row=2, column=2)
        
        Button(window, text="Submit", command=lambda submitData="newacc", numElement=2, listn=[self.userEnt,self.passEnt],other=None:self.retrieve(submitData,numElement,listn,other)).grid(row=4, column=1, columnspan=2)

class IncorrectPass(Master):
    def __init__(self,window):
        Master.__init__(self)
        self.window = window
        window.title("timeTracker - Log In")
        window.geometry("300x100")
        
        Label(window, text="Incorrect password or username.\nPlease try again.").pack()        
        Button(window, text="Ok", command=lambda windname=LogIn: self.newPage(windname)).pack()
        
class LogOut(Master):
    def __init__(self,window):
        Master.__init__(self)
        self.window = window
        window.geometry('300x80')
        window.title("timeTracker - Logged Out")
        
        Label(window, text="You have been logged out.").pack()        
        Button(window, text="Ok", command=self.window.quit).pack()
 
# LogIn -- creates login window
class LogIn(Master):
    username = ""
    __password = ""
    yourfile = ''
    
    # initializing LogIn class
    # @param: window:Tk()
    # @return: none
    def __init__(self,window):
        Master.__init__(self)
        self.window = window
        window.geometry("250x160")
        window.title("timeTracker - Log In")
        
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
        Button(window, text="Create New Account", command=lambda windname=NewAcc: self.newPage(windname)).grid(row=4, column=1, columnspan=2)
        
    # checks if username and password match
    # @param: none
    # @return: bool
    def checkUserPass(self):
        self.u = self.user.get()
        self.__p = self.passw.get()
        files = []
        dir_path = os.path.dirname(os.path.realpath(__file__))
        for file in os.listdir(dir_path):
            if file.endswith(".txt"):
                files.append(os.path.join(dir_path, file))
        for i in range(len(files)):
            if self.u == self.readFile(files[i])[0][0] and self.__p == self.readFile(files[i])[1][0]:
                print "You have logged in."
                self.yourfile = files[i]
                self.newPage(Home,self.yourfile)
                return True
            else:
                self.newPage(IncorrectPass)
                return False

        
# Home -- creates homepage that displays all data
class Home(Master):
    listEvents = []
    listButtonNames = []
    order = "TitleA"
    search = ""
    
    # controls scrolling for all listboxes
    # @param: *args
    # @return: none
    def OnVsb(self, *args):
        vlists = [self.subjectList,self.categoryList,self.nameList,self.dateList,self.lengthList,self.infoList]
        for i in range(len(vlists)):
            vlists[i].yview(*args)
            
    # initialize Home class
    # @param: window:Tk()
    # @return: none
    def __init__(self,window,yourfile):
        Master.__init__(self)
        self.yourfile = yourfile
        self.window = window
        window.title("timeTracker - Home")
        window.geometry("1090x880")
        
        # first tier menus
        self.menubar = Menu(window)
        self.filemenu = Menu(self.menubar, tearoff=False)
        self.viewmenu = Menu(self.menubar, tearoff=False)
        self.helpmenu = Menu(self.menubar, tearoff=False)
        
        # second tier menus
        self.settingmenu = Menu(self.helpmenu, tearoff=False)
        self.sortbymenu = Menu(self.viewmenu, tearoff=False)
        
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.menubar.add_cascade(label="View", menu=self.viewmenu)
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)
        self.filemenu.add("command", label="Home", command=lambda windname=Home, yourfile=yourfile: self.newPage(windname,yourfile))
        self.filemenu.add("command", label="New Entry", command=lambda windname=NewEntry, yourfile=yourfile: self.newPage(windname,yourfile))
        # self.filemenu.add("command", label="Calculate Hours", command=lambda windname=CalculateHours, events=[['','','','','','']]: self.newPage(windname,events))
        self.helpmenu.add_cascade(label="Settings", menu=self.settingmenu)
        self.settingmenu.add("command", label="Export Data", command=lambda windname=ExportXls, yourfile=yourfile: self.newPage(windname,yourfile))
        self.settingmenu.add("command", label="Clear All Data", command=lambda windname=ClearData, yourfile=yourfile: self.newPage(windname,yourfile))
        self.settingmenu.add("command", label="Log Out/Quit", command=lambda windname=LogOut: self.newPage(windname))
        self.settingmenu.add("command", label="About", command=lambda windname=About, yourfile=yourfile: self.newPage(windname,yourfile))
        # self.viewmenu.add_cascade(label="Sort by", menu=self.sortbymenu)
        # self.sortbymenu.add("command", label="Subject")
        
        window.config(menu = self.menubar)
        
        # search items
        self.search = Entry(window, width=70)
        self.search.grid(row=1, column=1, columnspan=4)
        self.searchButton = Button(window, text="Search", command=lambda submitData="search", numElement=1, listn=[self.search], other=self.yourfile: self.retrieve(submitData,numElement,listn,other))
        self.searchButton.grid(row=1, column=5)
        
        # list of inputted events
        self.listEvents = self.readFile(self.yourfile)[2:]
        # self.listEvents.sort()
        
        # create vertical and 3 horizontal scrollbars
        self.vscrollbar = Scrollbar(window)
        self.vscrollbar.grid(column=7, rowspan=4, sticky=N+S)
        self.hscrollbar1 = Scrollbar(window, orient=HORIZONTAL)
        self.hscrollbar1.grid(row=4, column=1, sticky=E+W)
        self.hscrollbar2 = Scrollbar(window, orient=HORIZONTAL)
        self.hscrollbar2.grid(row=4, column=3, sticky=E+W)
        self.hscrollbar3 = Scrollbar(window, orient=HORIZONTAL)
        self.hscrollbar3.grid(row=4, column=6, sticky=E+W)
        
        # creating listboxes individually (bc unfortunately you can't do the one scrollbar for all listboxes with a loop)
        self.subjectLbl = Label(window, text="Subject")
        self.subjectLbl.grid(row=2, column=1)
        self.subjectList = Listbox(window, yscrollcommand=self.vscrollbar.set, xscrollcommand=self.hscrollbar1.set, width=30, height=30)
        for k in range(len(self.listEvents)):
            self.subjectList.insert(END, self.listEvents[k][0])
        self.subjectList.grid(row=3, column=1)
        
        self.categoryLbl = Label(window, text="Category")
        self.categoryLbl.grid(row=2, column=2)
        self.categoryList = Listbox(window, yscrollcommand=self.vscrollbar.set, width=20, height=30)
        for k in range(len(self.listEvents)):
            self.categoryList.insert(END, self.listEvents[k][1])
        self.categoryList.grid(row=3, column=2)
        
        self.nameLbl = Label(window, text="With")
        self.nameLbl.grid(row=2, column=3)
        self.nameList = Listbox(window, yscrollcommand=self.vscrollbar.set, xscrollcommand=self.hscrollbar2.set, width=15, height=30)
        for k in range(len(self.listEvents)):
            self.nameList.insert(END, self.listEvents[k][2])
        self.nameList.grid(row=3, column=3)
        
        self.dateLbl = Label(window, text="Date")
        self.dateLbl.grid(row=2, column=4)
        self.dateList = Listbox(window, yscrollcommand=self.vscrollbar.set, width=12, height=30)
        for k in range(len(self.listEvents)):
            self.dateList.insert(END, self.listEvents[k][3])
        self.dateList.grid(row=3, column=4)
        
        self.lengthLbl = Label(window, text="Length")
        self.lengthLbl.grid(row=2, column=5)
        self.lengthList = Listbox(window, yscrollcommand=self.vscrollbar.set, width=7, height=30)
        for k in range(len(self.listEvents)):
            self.lengthList.insert(END, self.listEvents[k][4])
        self.lengthList.grid(row=3, column=5)
        
        self.infoLbl = Label(window, text="Info")
        self.infoLbl.grid(row=2, column=6)
        self.infoList = Listbox(window, yscrollcommand=self.vscrollbar.set, xscrollcommand=self.hscrollbar3.set, width=20, height=30)
        for k in range(len(self.listEvents)):
            self.infoList.insert(END, self.listEvents[k][5])
        self.infoList.grid(row=3, column=6)
        
        # configuring scrollbars to respective listboxes
        self.vscrollbar.config(command=self.OnVsb)
        self.hscrollbar1.config(command=self.subjectList.xview)
        self.hscrollbar2.config(command=self.nameList.xview)
        self.hscrollbar3.config(command=self.infoList.xview)
        
# NewEntry -- creates new entry window to receive data
class NewEntry(Master):
    attributes = ["Subject:","Category:","Names:","Date:","Time Start:","Or Length:","Other Info:"]
    months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
    years = [2018,2019,2020,2021,2022,2023,2024,2025,2026,2027,2028,2029,2030]
    
    # initialize NewEntry class
    # @param: window:Tk()
    # @return: none
    def __init__(self,window,yourfile):
        Master.__init__(self)
        self.window = window
        window.title = "timeTracker - New Entry"
        self.yourfile = yourfile
        self.nodatey = IntVar()
        self.nolengthy = IntVar()
        
        # first tier menus
        self.menubar = Menu(window)
        self.filemenu = Menu(self.menubar, tearoff=False)
        self.viewmenu = Menu(self.menubar, tearoff=False)
        self.helpmenu = Menu(self.menubar, tearoff=False)
        
        # second tier menus
        self.settingmenu = Menu(self.helpmenu, tearoff=False)
        self.sortbymenu = Menu(self.viewmenu, tearoff=False)
        
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.menubar.add_cascade(label="View", menu=self.viewmenu)
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)
        self.filemenu.add("command", label="Home", command=lambda windname=Home, yourfile=yourfile: self.newPage(windname,yourfile))
        self.filemenu.add("command", label="New Entry", command=lambda windname=NewEntry, yourfile=yourfile: self.newPage(windname,yourfile))
        # self.filemenu.add("command", label="Calculate Hours", command=lambda windname=CalculateHours, events=[['','','','','','']]: self.newPage(windname,events))
        self.helpmenu.add_cascade(label="Settings", menu=self.settingmenu)
        self.settingmenu.add("command", label="Export Data", command=lambda windname=ExportXls, yourfile=yourfile: self.newPage(windname,yourfile))
        self.settingmenu.add("command", label="Clear All Data", command=lambda windname=ClearData, yourfile=yourfile: self.newPage(windname,yourfile))
        self.settingmenu.add("command", label="Log Out/Quit", command=lambda windname=LogOut: self.newPage(windname))
        self.settingmenu.add("command", label="About", command=lambda windname=About, yourfile=yourfile: self.newPage(windname,yourfile))
        # self.viewmenu.add_cascade(label="Sort by", menu=self.sortbymenu)
        # self.sortbymenu.add("command", label="Subject")
        
        window.config(menu = self.menubar)

        # creating labels for the inputs
        for i in range(len(self.attributes)):
            self.newLbls = Label(window, text=self.attributes[i])
            self.newLbls.grid(row=i, column=1)
        self.endTime = Label(window, text="Time End:")
        self.endTime.grid(row=4, column=3)
            
        # generating and grid-ing the input stuff
        self.subject = Entry(window, width=70)
        self.category = Entry(window, width=70)
        self.names = Entry(window, width=70)
        self.names.insert(0, 'Please enter names of people associated with this event separated by commas.')
        self.names.bind("<FocusIn>", lambda args: self.names.delete('0', 'end'))
        self.subject.grid(row=0, column=2, columnspan=3)
        self.category.grid(row=1, column=2, columnspan=3)
        self.names.grid(row=2, column=2, columnspan=3)
        
        self.month = Spinbox(window,values=self.months,width=15)
        self.day = Spinbox(window,values=self.days,width=15)
        self.year = Spinbox(window,values=self.years,width=15)
        self.month.grid(row=3, column=2)
        self.day.grid(row=3, column=3)
        self.year.grid(row=3, column=4)
        self.nodate = Checkbutton(self.window, text="No Date", variable=self.nodatey, command=lambda button="nodate", widgets=[self.month,self.day,self.year]: self.disableWidget(button,widgets))
        self.nodate.grid(row=3, column=5)
        
        # add keybind to which type of length using (ie. which one has text and which doesn't)
        
        self.tstart = Entry(window, width=28)
        self.tend = Entry(window, width=28)
        self.tstart.grid(row=4, column=2)
        self.tend.grid(row=4, column=4)
        
        self.length = Entry(window, width=70)
        self.length.insert(0, 'hh:mm')
        self.length.grid(row=5, column=2, columnspan=3)
        
        self.tstart.bind("<FocusIn>", lambda args: self.disableWidget("length",[self.tstart,self.tend,self.length]))
        self.tend.bind("<FocusIn>", lambda args: self.disableWidget("length",[self.tstart,self.tend,self.length]))
        self.length.bind("<FocusIn>", lambda args: self.disableWidget("time",[self.tstart,self.tend,self.length]))
        
        self.nolength = Checkbutton(self.window, text="No Length", variable=self.nolengthy, command=lambda button="nolength", widgets=[self.tstart,self.tend,self.length]: self.disableWidget(button,widgets))
        self.nolength.grid(row=5, column=5)
        
        self.info = Entry(window, width=70)
        self.info.grid(row=6, column=2, columnspan=3)
        
        self.listn = [self.subject,self.category,self.names,self.month,self.day,self.year,self.tstart,self.tend,self.length,self.info]

        self.submit = Button(window, text="Submit", command= lambda submitData="newentry", numElement=9, listn=self.listn, other=self.months: self.retrieve(submitData, numElement, listn, other))
        self.submit.grid(row=7, column=1, columnspan=4)
        
    # disables widgets when things are clicked
    # @param: button:str, widgets:object[]
    # @return: none
    def disableWidget(self,button,widgets):
        if button == "nodate":
            if self.nodatey.get() == 1:
                for i in range(len(widgets)):
                    widgets[i].delete(0,'end')
                    widgets[i].config(state="disabled")
            else:
                for i in range(len(widgets)):
                    widgets[i].config(state="normal")
        if button == "nolength":
            if self.nolengthy.get() == 1:
                for i in range(len(widgets)):
                    widgets[i].delete(0,'end')
                    widgets[i].config(state="disabled")
            else:
                for i in range(len(widgets)):
                    widgets[i].config(state="normal")
        elif button == "length":
            widgets[0].config(bg="white")
            widgets[1].config(bg="white")
            widgets[2].config(bg="grey")
        elif button == "time":
            widgets[0].config(bg="grey")
            widgets[1].config(bg="grey")
            widgets[2].config(bg="white")
            widgets[2].delete('0', 'end')

# Search -- displays events with search term
class Search(Master):
    
    # controls scrolling for all listboxes
    # @param: *args
    # @return: none
    def OnVsb(self, *args):
        vlists = [self.subjectList,self.categoryList,self.nameList,self.dateList,self.lengthList,self.infoList]
        for i in range(len(vlists)):
            vlists[i].yview(*args)
    
    # changes which list is being displayed
    # @param: sort:int, lists:object[]
    # @return: none
    def display(self,sort,lists):
        self.displayList = []
        if sort == 0:
            for i in range(len(self.foundTitle)):
                self.displayList.append(self.listEntry[i])
        elif sort == 1:
            for i in range(len(self.foundCategory)):
                self.displayList.append(self.listEntry[i])
        elif sort == 2:
            for i in range(len(self.foundName)):
                self.displayList.append(self.listEntry[i])
        elif sort == 3:
            for i in range(len(self.foundDate)):
                self.displayList.append(self.listEntry[i])
        elif sort == 4:
            for i in range(len(self.foundLength)):
                self.displayList.append(self.listEntry[i])
        elif sort == 5:
            for i in range(len(self.foundInfo)):
                self.displayList.append(self.listEntry[i])
                
        for i in range(len(lists)):
            lists[i].delete(0,END)
            for k in range(len(self.displayList)):
                lists[i].insert(END,self.displayList[k][i])
    
    # initialize Search window
    # @param: window:Tk(), keyword:str
    # @return: none
    def __init__(self,window,keyword,yourfile):
        Master.__init__(self)
        self.window = window
        self.yourfile = yourfile
        window.title = "timeTracker - Search"
        window.geometry("1000x400")
        
        # first tier menus
        self.menubar = Menu(window)
        self.filemenu = Menu(self.menubar, tearoff=False)
        self.viewmenu = Menu(self.menubar, tearoff=False)
        self.helpmenu = Menu(self.menubar, tearoff=False)
        
        # second tier menus
        self.settingmenu = Menu(self.helpmenu, tearoff=False)
        self.sortbymenu = Menu(self.viewmenu, tearoff=False)
        
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.menubar.add_cascade(label="View", menu=self.viewmenu)
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)
        self.filemenu.add("command", label="Home", command=lambda windname=Home, yourfile=yourfile: self.newPage(windname,yourfile))
        self.filemenu.add("command", label="New Entry", command=lambda windname=NewEntry, yourfile=yourfile: self.newPage(windname,yourfile))
        # self.filemenu.add("command", label="Calculate Hours", command=lambda windname=CalculateHours, events=[['','','','','','']]: self.newPage(windname,events))
        self.helpmenu.add_cascade(label="Settings", menu=self.settingmenu)
        self.settingmenu.add("command", label="Export Data", command=lambda windname=ExportXls, yourfile=yourfile: self.newPage(windname,yourfile))
        self.settingmenu.add("command", label="Clear All Data", command=lambda windname=ClearData, yourfile=yourfile: self.newPage(windname,yourfile))
        self.settingmenu.add("command", label="Log Out/Quit", command=lambda windname=LogOut: self.newPage(windname))
        self.settingmenu.add("command", label="About", command=lambda windname=About, yourfile=yourfile: self.newPage(windname,yourfile))
        # self.viewmenu.add_cascade(label="Sort by", menu=self.sortbymenu)
        # self.sortbymenu.add("command", label="Subject")
        
        window.config(menu = self.menubar)
        
        
        self.foundTitle = []
        self.foundCategory = []
        self.foundName = []
        self.foundDate = []
        self.foundLength = []
        self.foundInfo = []
        self.displayList = [['','','','','','']]
        
        # list of inputted events
        self.listEntry = self.readFile(self.yourfile)
        self.listEntry = self.listEntry[2:]
        for i in range(len(self.listEntry)):
            if self.listEntry[i][0].find(keyword) >= 0:
                self.foundTitle.append([self.listEntry[i][0],i])
            if self.listEntry[i][1].find(keyword) >= 0:
                self.foundCategory.append([self.listEntry[i][1],i])
            if self.listEntry[i][2].find(keyword) >= 0:
                self.foundName.append([self.listEntry[i][2],i])
            if self.listEntry[i][3].find(keyword) >= 0:
                self.foundDate.append([self.listEntry[i][3],i])
            if self.listEntry[i][4].find(keyword) >= 0:
                self.foundLength.append([self.listEntry[i][4],i])
            if self.listEntry[i][5].find(keyword) >= 0:
                self.foundInfo.append([self.listEntry[i][5],i])
        
        # self.listEvents.sort()
        
        # create vertical and 3 horizontal scrollbars
        self.vscrollbar = Scrollbar(window)
        self.vscrollbar.grid(column=7, rowspan=4, sticky=N+S)
        self.hscrollbar1 = Scrollbar(window, orient=HORIZONTAL)
        self.hscrollbar1.grid(row=4, column=1, sticky=E+W)
        self.hscrollbar2 = Scrollbar(window, orient=HORIZONTAL)
        self.hscrollbar2.grid(row=4, column=3, sticky=E+W)
        self.hscrollbar3 = Scrollbar(window, orient=HORIZONTAL)
        self.hscrollbar3.grid(row=4, column=6, sticky=E+W)
        
        # creating listboxes individually (bc unfortunately you can't do the one scrollbar for all listboxes with a loop)
        self.subjectLbl = Label(window, text="Subject")
        self.subjectLbl.grid(row=2, column=1)
        self.subjectList = Listbox(window, yscrollcommand=self.vscrollbar.set, xscrollcommand=self.hscrollbar1.set, width=15, height=10)
        for k in range(len(self.displayList)):
            self.subjectList.insert(END, self.displayList[k][0])
        self.subjectList.grid(row=3, column=1)
        
        self.categoryLbl = Label(window, text="Category")
        self.categoryLbl.grid(row=2, column=2)
        self.categoryList = Listbox(window, yscrollcommand=self.vscrollbar.set, width=15, height=10)
        for k in range(len(self.displayList)):
            self.categoryList.insert(END, self.displayList[k][1])
        self.categoryList.grid(row=3, column=2)
        
        self.nameLbl = Label(window, text="With")
        self.nameLbl.grid(row=2, column=3)
        self.nameList = Listbox(window, yscrollcommand=self.vscrollbar.set, xscrollcommand=self.hscrollbar2.set, width=15, height=10)
        for k in range(len(self.displayList)):
            self.nameList.insert(END, self.displayList[k][2])
        self.nameList.grid(row=3, column=3)
        
        self.dateLbl = Label(window, text="Date")
        self.dateLbl.grid(row=2, column=4)
        self.dateList = Listbox(window, yscrollcommand=self.vscrollbar.set, width=15, height=10)
        for k in range(len(self.displayList)):
            self.dateList.insert(END, self.displayList[k][3])
        self.dateList.grid(row=3, column=4)
        
        self.lengthLbl = Label(window, text="Length")
        self.lengthLbl.grid(row=2, column=5)
        self.lengthList = Listbox(window, yscrollcommand=self.vscrollbar.set, width=15, height=10)
        for k in range(len(self.displayList)):
            self.lengthList.insert(END, self.displayList[k][4])
        self.lengthList.grid(row=3, column=5)
        
        self.infoLbl = Label(window, text="Info")
        self.infoLbl.grid(row=2, column=6)
        self.infoList = Listbox(window, yscrollcommand=self.vscrollbar.set, xscrollcommand=self.hscrollbar3.set, width=15, height=10)
        for k in range(len(self.displayList)):
            self.infoList.insert(END, self.displayList[k][5])
        self.infoList.grid(row=3, column=6)
        
        # configuring scrollbars to respective listboxes
        self.vscrollbar.config(command=self.OnVsb)
        self.hscrollbar1.config(command=self.subjectList.xview)
        self.hscrollbar2.config(command=self.nameList.xview)
        self.hscrollbar3.config(command=self.infoList.xview)
        
        buttonList = ["Title","Category","Name","Date","Length","Info","All"]
        for i in range(len(buttonList)):
            buttons = Button(window, text=buttonList[i], command=lambda sort=i, lists=[self.subjectList,self.categoryList,self.nameList,self.dateList,self.lengthList,self.infoList]: self.display(sort,lists))
            buttons.grid(column=i+1, row=1)
        

class CalculateHours(Master):
#     def display(self,sort,lists):
#         self.displayList = []
#         if sort == 0:
#             for i in range(len(self.foundTitle)):
#                 self.displayList.append(self.listEntry[i])
#         elif sort == 1:
#             for i in range(len(self.foundCategory)):
#                 self.displayList.append(self.listEntry[i])
#         elif sort == 2:
#             for i in range(len(self.foundName)):
#                 self.displayList.append(self.listEntry[i])
#         elif sort == 3:
#             for i in range(len(self.foundDate)):
#                 self.displayList.append(self.listEntry[i])
#         elif sort == 4:
#             for i in range(len(self.foundLength)):
#                 self.displayList.append(self.listEntry[i])
#         elif sort == 5:
#             for i in range(len(self.foundInfo)):
#                 self.displayList.append(self.listEntry[i])
#         
#         print self.displayList
#         
#         for i in range(len(lists)):
#             lists[i].delete(0,END)
#             for k in range(len(self.displayList)):
#                 print i,k
#                 lists[i].insert(END,self.displayList[k][i])
#     
#     def __init__(self,window,events):
#         Master.__init__(self)
#         self.window = window
#         window.title = "timeTracker - Calculate Hours"
#         
#         # first tier menus
#         self.menubar = Menu(window)
#         self.filemenu = Menu(self.menubar, tearoff=False)
#         self.viewmenu = Menu(self.menubar, tearoff=False)
#         self.helpmenu = Menu(self.menubar, tearoff=False)
#         
#         
#         # second tier menus
#         self.settingmenu = Menu(self.helpmenu, tearoff=False)
#         self.sortbymenu = Menu(self.viewmenu, tearoff=False)
#         
#         self.menubar.add_cascade(label="File", menu=self.filemenu)
#         self.menubar.add_cascade(label="View", menu=self.viewmenu)
#         self.menubar.add_cascade(label="Help", menu=self.helpmenu)
#         self.filemenu.add("command", label="Home", command=lambda windname=Home: self.newPage(windname))
#         self.filemenu.add("command", label="New Entry", command=lambda windname=NewEntry: self.newPage(windname))
#         self.filemenu.add("command", label="Calculate Hours", command=lambda windname=CalculateHours, events=[['','','','','','']]: self.newPage(windname,events))
#         self.helpmenu.add_cascade(label="Settings", menu=self.settingmenu)
#         self.viewmenu.add_cascade(label="Sort by", menu=self.sortbymenu)
#         self.sortbymenu.add("command", label="Subject")
#         
#         window.config(menu = self.menubar)
#         
#         # search items
#         self.sort = Entry(window, width=70)
#         self.sort.grid(row=1, column=1, columnspan=4)
#         self.sortButton = Button(window, text="Sort", command=lambda submitData="calculate", numElement=1, listn=[self.sort], other=None: self.retrieve(submitData,numElement,listn,other))
#         self.sortButton.grid(row=1, column=5)
#             
#         # list of inputted events
#         self.display(0,)
#         print "hi",self.displayList
#         # self.listEvents.sort()
#         
#         # create vertical and 3 horizontal scrollbars
#         self.vscrollbar = Scrollbar(window)
#         self.vscrollbar.grid(column=3, rowspan=4, sticky=N+S)
#         self.hscrollbar1 = Scrollbar(window, orient=HORIZONTAL)
#         self.hscrollbar1.grid(row=4, column=1, sticky=E+W)
# 
#         # creating listboxes individually (bc unfortunately you can't do the one scrollbar for all listboxes with a loop)
#         self.subjectLbl = Label(window, text="Subject")
#         self.subjectLbl.grid(row=2, column=1)
#         self.subjectList = Listbox(window, yscrollcommand=self.vscrollbar.set, xscrollcommand=self.hscrollbar1.set, width=15, height=10)
#         for k in range(len(self.displayList)):
#             self.subjectList.insert(END, self.displayList[k][0])
#         self.subjectList.grid(row=3, column=1)
#         
#     def calculate(self,events):
#         length = IntVar()
#         hrs = 0
#         mins = 0
#         for i in range(len(events)):
#             length = events[4].split(':')
#             hrs += int(length[0])
#             mins += int(length[1])
#         print hrs,mins
#         totalLbl = Label(self.window, text="{} hrs, {} mins".format(hrs,mins))
#         totalLbl.grid(column=1, columnspan=2, row=4)
        pass
        
        
        
window = Tk()
home = LogIn(window)
window.mainloop()
    