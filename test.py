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


from Tkinter import *

master = Tk()

scrollbar = Scrollbar(master)
scrollbar.pack(side=RIGHT, fill=Y)

listbox = Listbox(master, yscrollcommand=scrollbar.set)
for i in range(1000):
    listbox.insert(END, str(i))
listbox.pack(side=LEFT, fill=BOTH)

scrollbar.config(command=listbox.yview)

mainloop()