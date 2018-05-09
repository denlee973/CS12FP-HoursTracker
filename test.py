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


def reWriteFile():
    f = open('test.txt','r')
    text = f.readlines()
    f.close
    for i in range(len(text)-1):
        text[i] = text[i][0:len(text[i])-1]
    for j in range(len(text)):
        text[j] = text[j].split("/t")
    print text
    f = open('test.txt','w')
    for i in range(len(text)):
        line = ""
        for j in range(len(text[i])-1):
            line += str(text[i][j]) + "/t"
        line += str(text[i][len(text[i])])+"\n"
        print line

        f.write(line)
    f.close()
    
reWriteFile()