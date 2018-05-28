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


# from Tkinter import *
# 
# root = Tk()
# 
# def hello():
#     print "hello!"
# 
# menubar = Menu(root)
# 
# # create a pulldown menu, and add it to the menu bar
# filemenu = Menu(menubar, tearoff=0)
# filemenu.add_command(label="Open", command=hello)
# filemenu.add_command(label="Save", command=hello)
# filemenu.add_separator()
# filemenu.add_command(label="Exit", command=root.quit)
# menubar.add_cascade(label="File", menu=filemenu)
# 
# # create more pulldown menus
# editmenu = Menu(menubar, tearoff=0)
# editmenu.add_command(label="Cut", command=hello)
# editmenu.add_command(label="Copy", command=hello)
# editmenu.add_command(label="Paste", command=hello)
# menubar.add_cascade(label="Edit", menu=editmenu)
# 
# helpmenu = Menu(menubar, tearoff=0)
# helpmenu.add_command(label="About", command=hello)
# menubar.add_cascade(label="Help", menu=helpmenu)
# 
# # display the menu
# root.config(menu=menubar)
# 
# root.mainloop()
# Try to import Python 2 name
try:
    import Tkinter as tk
# Fall back to Python 3 if import fails
except ImportError:
    import tkinter as tk

# open('test.txt', 'w').close()

# import os
# dir_path = os.path.dirname(os.path.realpath(__file__))
# for file in os.listdir(dir_path):
#     if file.endswith(".txt"):
#         print(os.path.join(dir_path, file))


# class Example(tk.Frame):
#     def __init__(self, root):
#         tk.Frame.__init__(self, root)
#         menubar = tk.Menu(self)
#         fileMenu = tk.Menu(self)
#         recentMenu = tk.Menu(self)
# 
#         menubar.add_cascade(label="File", menu=fileMenu)
#         fileMenu.add_cascade(label="Open Recent", menu=recentMenu)
#         for name in ("file1.txt", "file2.txt", "file3.txt"):
#             recentMenu.add_command(label=name)
# 
# 
#         root.configure(menu=menubar)
#         root.geometry("200x200")
# 
# if __name__ == "__main__":
#     root = tk.Tk()
#     Example(root).pack(fill="both", expand=True)
#     root.mainloop()


# class Application:
#     def __init__(self, master):
#         self.frame = tk.Frame(master)
#         self.frame.pack()    
#         self.okButton = tk.Button(self.frame, text="OK",
#                                   command=self.window_maker).pack()
#         self.quitButton = tk.Button(self.frame, text="Close",
#                                     command=self.frame.quit).pack()
#     def window_maker(self):
#         MakeWindow("A message to Toplevel")
# 
# 
# class MakeWindow(tk.Toplevel):
#     def __init__(self, message):
#         tk.Toplevel.__init__(self) #instead of super
#         self.message = message
#         self.display = tk.Label(self, text=message)
#         self.display.pack()
# 
# 
# if __name__ == '__main__':
#     root = tk.Tk()
#     app = Application(root)
#     root.mainloop()


# import xlsxwriter
# 
# 
# # Create an new Excel file and add a worksheet.
# workbook = xlsxwriter.Workbook('demo.xlsx')
# worksheet = workbook.add_worksheet()
# 
# # Widen the first column to make the text clearer.
# worksheet.set_column('A:A', 20)
# 
# # Add a bold format to use to highlight cells.
# bold = workbook.add_format({'bold': True})
# 
# # Write some simple text.
# worksheet.write('A1', 'Hello')
# 
# # Text with formatting.
# worksheet.write('A2', 'World', bold)
# 
# # Write some numbers, with row/column notation.
# worksheet.write(2, 0, 123)
# worksheet.write(3, 0, 123.456)
# 
# # Insert an image.
# # worksheet.insert_image('B5', 'logo.png')
# 
# workbook.close()
# import datetime
# print datetime.date.today()