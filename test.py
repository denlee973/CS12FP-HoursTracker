# import ScrolledText
# from Tkinter import *
# window = Tk()
# window.title("hi")
# 
# 
# textfield = ScrolledText.ScrolledText(wrap=WORD)
# textfield.grid(row=2, column=2)
# 
# window.mainloop()


# def reWriteFile(adding):
#     f = open('test.txt','r')
#     text = f.readlines()
#     f.close
#     print text
#     for i in range(len(text)-1):
#         text[i] = text[i][0:len(text[i])-1]
#     print text
#     for j in range(len(text)):
#         text[j] = text[j].split("/t")
#     print text
#     f = open('test.txt','w')
#     for i in range(len(text)):
#         print text[i]
#         line = ""
#         for j in range(len(text[i])-1):
#             line += str(text[i][j]) + "/t"
#         line += str(text[i][len(text[i])-1])+"\n"
#         print line
#         f.write(line)
#         
#     for m in range(len(adding)-1):
#         print adding[m]
#         line = ""
#         for p in range(len(adding[m])-1):
#             line += str(adding[m][p]) + "/t"
#         line += str(adding[m][len(adding[m])-1])+"\n"
#         print line
#         f.write(line)
# 
# 
#     print adding[len(text)-1]
#     line = ""
#     for k in range(len(adding[len(adding)-1])-1):
#         line += str(adding[len(adding)-1][k]) + "/t"
#     line += str(adding[len(adding)-1][len(adding[len(adding)-1])-1])
#     print line
#     f.write(line)
#     
#     f.close()
#     
# reWriteFile([["Hello World","HI"],["hey there"]])

# T-T
# f = open('test.txt','a')
# f.write("Hello World/tHI\nhey there")


# from Tkinter import *
# 
# master = Tk()
# 
# scrollbar = Scrollbar(master)
# scrollbar.pack(side=RIGHT, fill=Y)
# 
# listbox = Listbox(master, yscrollcommand=scrollbar.set)
# for i in range(1000):
#     listbox.insert(END, str(i))
# listbox.pack(side=LEFT, fill=BOTH)
# 
# scrollbar.config(command=listbox.yview)
# 
# mainloop()

import Tkinter as tk

class App:
    def __init__(self):
        self.root=tk.Tk()
        self.vsb = tk.Scrollbar(orient="vertical", command=self.OnVsb)
        self.lb1 = tk.Listbox(self.root, yscrollcommand=self.vsb.set)
        self.lb2 = tk.Listbox(self.root, yscrollcommand=self.vsb.set)
        self.vsb.pack(side="right",fill="y")
        self.lb1.pack(side="left",fill="x", expand=True)
        self.lb2.pack(side="left",fill="x", expand=True)
        self.lb1.bind("<MouseWheel>", self.OnMouseWheel)
        self.lb2.bind("<MouseWheel>", self.OnMouseWheel)
        for i in range(100):
            self.lb1.insert("end","item %s" % i)
            self.lb2.insert("end","item %s" % i)
        self.root.mainloop()

    def OnVsb(self, *args):
        self.lb1.yview(*args)
        self.lb2.yview(*args)

    def OnMouseWheel(self, event):
        self.lb1.yview("scroll", event.delta,"units")
        self.lb2.yview("scroll",event.delta,"units")
        # this prevents default bindings from firing, which
        # would end up scrolling the widget twice
        return "break"

app=App()