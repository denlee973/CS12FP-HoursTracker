from Tkinter import *
import tkFont
import ttk
from abc import ABCMeta, abstractmethod


class Master:
    __metaclass__ = ABCMeta
    text = []
    def __init__(self):
        default_font = tkFont.nametofont("TkDefaultFont")
        default_font.configure(size=12)
        self.menubar = Menu(window)
        self.filemenu = Menu(self.menubar, tearoff=0)
        
        self.filemenu.add_cascade(label="Settings", command=self.settings) # under tools
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
    
    def combobox(self,listv,style):
        self.varname = ttk.Combobox(window, state=style)
        self.varname['values'] = listv
        self.varname.current(0)
        return self.varname
    
    def retrieve(self,submitData,numElement,listn,other):
        for i in range(numElement):
            self.item = self.listn[i].get()
            self.data[0].append(self.item)
        if submitData == "newentry":
            # date formatting to mm-dd-yyyy
            imon = self.data[0][2]
            date = ""
            for i in range(len(other)):
                if imon == other[i]:
                    if i <= 9:
                        date += "0"+str(i+1)+"-"
                    else:
                        date += str(i+1)+"-"
            if len(self.data[0][3]) < 2:
                date += "0"+self.data[0][3]+"-"+self.data[0][4]
            else:
                date += self.data[0][3]+"-"+self.data[0][4]
                
            for j in range(3):
                self.data[0].pop(2)
             
            self.data[0].insert(2,date)
            print self.data
            
            # calculating length
            if self.data[0][5] == "":
                if self.data[0][3].find("m") >= 0 or self.data[0][3].find("M"):
                    if self.data[0][3][-2:] == self.data[0][4][-2:]:
                        start = self.data[0][3][:-2].split(":")
                        end = self.data[0][4][:-2].split(":")
                        print start, end
                        hrs = int(end[0])-int(start[0])
                        mins = int(end[1])-int(start[1])
                    elif (self.data[0][3].find("a") >= 0 or self.data[0][3].find("A") >= 0) and (self.data[0][4].find("p") >= 0 or self.data[0][4].find("P")):
                        start = self.data[0][3][:-2].split(":")
                        end = self.data[0][4][:-2].split(":")
                        print start, end
                        hrs = int(end[0])-int(start[0])+12
                        mins = int(end[1])-int(start[1])
                else:
                    start = self.data[0][3].split(":")
                    end = self.data[0][4].split(":")
                    print start, end
                    hrs = int(end[0])-int(start[0])
                    mins = int(end[1])-int(start[1])
                for r in range(3):
                    self.data[0].pop(3)
                if len(str(hrs)) < 2:
                    hrs = "0"+str(hrs)
                else:
                    hrs = str(hrs)
                if len(str(mins)) < 2:
                    mins = "0"+str(mins)
                else:
                    mins = str(mins)
                self.data[0].insert(3,hrs+":"+mins)
            elif self.data[0][3] == "":
                for r in range(2):
                    self.data[0].pop(3)
            self.addToFile('data.txt',self.data)
            
        self.data = [[]]
            
    def addToFile(self,filename,adding):
        f = open(filename,'a')
        for i in range(len(adding)):
            line = "\n"
            for j in range(len(adding[i])-1):
                line += str(adding[i][j])+"/t"
            line += str(adding[i][len(adding[i])-1])
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
    
    def OnVsb(self, *args):
        vlists = [self.subjectList,self.categoryList,self.nameList,self.dateList,self.lengthList,self.infoList]
        for i in range(len(vlists)):
            vlists[i].yview(*args)

    def __init__(self,window):
        Master.__init__(self)
        self.window = window
        window.title("Hours Tracker - Home")
        window.geometry("1090x850")
        
        # search items
        self.search = Entry(window, width=70)
        self.search.grid(row=1, column=1, columnspan=4)
        self.searchButton = Button(window, text="Search")
        self.searchButton.grid(row=1, column=5)
        
        # list of inputted events
        self.listEvents = self.readFile('data.txt')[2:]
        print "hi",self.listEvents
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
        self.subjectList = Listbox(window, yscrollcommand=self.vscrollbar.set, xscrollcommand=self.hscrollbar1.set, width=30, height=30)
        for k in range(len(self.listEvents)):
            self.subjectList.insert(END, self.listEvents[k][0])
        self.subjectList.grid(row=3, column=1)
        
        self.categoryList = Listbox(window, yscrollcommand=self.vscrollbar.set, width=20, height=30)
        for k in range(len(self.listEvents)):
            self.categoryList.insert(END, self.listEvents[k][1])
        self.categoryList.grid(row=3, column=2)
        
        self.nameList = Listbox(window, yscrollcommand=self.vscrollbar.set, xscrollcommand=self.hscrollbar2.set, width=15, height=30)
        for k in range(len(self.listEvents)):
            self.nameList.insert(END, self.listEvents[k][2])
        self.nameList.grid(row=3, column=3)
        
        self.dateList = Listbox(window, yscrollcommand=self.vscrollbar.set, width=12, height=30)
        for k in range(len(self.listEvents)):
            self.dateList.insert(END, self.listEvents[k][3])
        self.dateList.grid(row=3, column=4)
        
        self.lengthList = Listbox(window, yscrollcommand=self.vscrollbar.set, width=7, height=30)
        for k in range(len(self.listEvents)):
            self.lengthList.insert(END, self.listEvents[k][4])
        self.lengthList.grid(row=3, column=5)
        
        self.infoList = Listbox(window, yscrollcommand=self.vscrollbar.set, xscrollcommand=self.hscrollbar3.set, width=20, height=30)
        for k in range(len(self.listEvents)):
            self.infoList.insert(END, self.listEvents[k][5])
        self.infoList.grid(row=3, column=6)
        
        # configuring scrollbars to respective listboxes
        self.vscrollbar.config(command=self.OnVsb)
        self.hscrollbar1.config(command=self.subjectList.xview)
        self.hscrollbar2.config(command=self.nameList.xview)
        self.hscrollbar3.config(command=self.infoList.xview)
        
        
        

            
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
        self.nodatey = IntVar()

        # creating labels for the inputs
        for i in range(len(self.attributes)):
            self.newLbls = Label(window, text=self.attributes[i])
            self.newLbls.grid(row=i, column=1)
        self.endTime = Label(window, text="Time End:")
        self.endTime.grid(row=3, column=3)
            
        # generating and grid-ing the input stuff
        self.subject = Entry(window, width=70)
        self.names = Entry(window, width=70)
        # want to make placeholder grey but I'll do that later.
        # self.names.insert(0, 'Please enter names of people associated with this event separated by commas.')
        # self.names.bind("<FocusIn>", lambda args: self.names.delete('0', 'end'))
        self.subject.grid(row=0, column=2, columnspan=3)
        self.names.grid(row=1, column=2, columnspan=3)
        
        self.month = self.combobox(self.months, "readonly")
        self.month.config(width=10)
        self.day = self.combobox(self.days, "normal")
        self.day.config(width=7)
        self.year = self.combobox(self.years, "normal")
        self.year.config(width=7)
        self.month.grid(row=2, column=2)
        self.day.grid(row=2, column=3)
        self.year.grid(row=2, column=4)
        self.nodate = Checkbutton(self.window, text="No Date", variable=self.nodatey, command=lambda widgets=[self.month,self.day,self.year]: self.disableWidget(widgets))
        self.nodate.grid(row=2, column=5)
        
        # add keybind to which type of length using (ie. which one has text and which doesn't)
        
        self.tstart = Entry(window, width=28)
        self.tend = Entry(window, width=28)
        self.tstart.grid(row=3, column=2)
        self.tend.grid(row=3, column=4)
        # self.twentyfour = Checkbutton(self.window, text="24-Hour", variable=self.twnty4)

        
        self.length = Entry(window, width=70)
        self.length.grid(row=4, column=2, columnspan=3)
        
        self.info = Entry(window, width=70)
        self.info.grid(row=5, column=2, columnspan=3)
        
        self.listn = [self.subject,self.names,self.month,self.day,self.year,self.tstart,self.tend,self.length,self.info]

        self.submit = Button(window, text="Submit", command= lambda submitData="newentry", numElement=9, listn=self.listn, other=self.months: self.retrieve(submitData, numElement, listn, other))
        self.submit.grid(row=6, column=1, columnspan=4)
        
    def disableWidget(self,widgets):
        if self.nodatey.get() == 1:
            for i in range(len(widgets)):
                widgets[i].config(state="disabled")
        else:
            for i in range(len(widgets)):
                widgets[i].config(state="normal")
        
        
class CalculateHours(Master):
    pass
        
        
window = Tk()
home = Home(window)
window.mainloop()
    