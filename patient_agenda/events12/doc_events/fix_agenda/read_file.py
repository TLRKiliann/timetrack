#!/usr/bin/python3
# -*- coding: utf-8 -*-


from tkinter import *
from tkinter import messagebox
import os
import posixpath


fen=Tk()
fen.title("Time-Track")
fen.configure(background='DodgerBlue2')

# To place side by side labelo + entrylab
top = Frame(fen, bg='DodgerBlue2')
top2 = Frame(fen, bg='DodgerBlue2')
top3 = Frame(fen, bg='SteelBlue2')
top4 = Frame(fen, bg='SteelBlue2')
top5 = Frame(fen, bg='DodgerBlue2')
bottom = Frame(fen, bg='DodgerBlue2')
top.pack(side=TOP)
top2.pack(side=TOP)
top3.pack(side=TOP)
top4.pack(side=TOP)
top5.pack(side=TOP)
bottom.pack(side=BOTTOM, fill=BOTH, expand=YES)

labelo = Label(fen, text="Appointments",
    font='Arial 18 bold', fg='white', bg='DodgerBlue2')
labelo.pack(in_=top, side=LEFT, pady=5)

with open('./newpatient/entryfile12.txt', 'r') as filename:
    line1 = filename.readline()

textentry = StringVar()
entrylab = Entry(fen, textvariable=textentry, width=20, 
    highlightbackground='grey', bd=3)
textentry.set(line1[:-1])
entrylab.pack(in_=top, side=RIGHT, padx=10, pady=10)

textBox = Text(fen, height=20, width=60, font=18)
textBox.pack(in_=top2, padx=30, pady=10)

def janSearch():
    """
        To search by months and sort() date
    """
    for path, dirs, files in os.walk('./patient_agenda/'\
        'events12/doc_events/fix_agenda/agenda_saved/'):
        for file in files:
            with open(os.path.join(path, file),'r') as jan_read:
                lines = jan_read.readlines()
                for i in range(0, len(lines)):
                    for line in lines:
                        line.replace('{', '')
                        line.replace('}', '')
                        line = lines[i]
                        if line[3:5] == "01":
                            textBox.insert(INSERT, lines[i-1])
                            textBox.insert(INSERT, lines[i])
                            textBox.insert(INSERT, lines[i+1])
                            textBox.insert(INSERT, lines[i+2])
                            textBox.insert(INSERT, '\n')
                            print(lines[i])
                            break

buttonJan = Button(fen, text="Jan", font='Arial 12 bold', bd=3,
    fg='white', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='pale turquoise', command=janSearch)
buttonJan.pack(in_=top3, side=LEFT, padx=10, pady=10)

def febSearch():
    for path, dirs, files in os.walk('./patient_agenda/'\
        'events12/doc_events/fix_agenda/agenda_saved/'):
        for file in files:
            with open(os.path.join(path, file),'r') as jan_read:
                lines = jan_read.readlines()
                for i in range(0, len(lines)):
                    for line in lines:
                        line.replace('{', '')
                        line.replace('}', '')
                        line = lines[i]
                        if line[3:5] == "02":
                            textBox.insert(INSERT, lines[i-1])
                            textBox.insert(INSERT, lines[i])
                            textBox.insert(INSERT, lines[i+1])
                            textBox.insert(INSERT, lines[i+2])
                            textBox.insert(INSERT, '\n')
                            break

buttonFeb = Button(fen, text="Feb", font='Arial 12 bold', bd=3,
    fg='white', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='pale turquoise',
    command=febSearch)
buttonFeb.pack(in_=top3, side=LEFT, padx=10, pady=10)

def marSearch():
    for path, dirs, files in os.walk('./patient_agenda/'\
        'events12/doc_events/fix_agenda/agenda_saved/'):
        for file in files:
            with open(os.path.join(path, file),'r') as jan_read:
                lines = jan_read.readlines()
                for i in range(0, len(lines)):
                    for line in lines:
                        line.replace('{', '')
                        line.replace('}', '')
                        line = lines[i]
                        if line[3:5] == "03":
                            textBox.insert(INSERT, lines[i-1])
                            textBox.insert(INSERT, lines[i])
                            textBox.insert(INSERT, lines[i+1])
                            textBox.insert(INSERT, lines[i+2])
                            textBox.insert(INSERT, '\n')
                            break

buttonMar = Button(fen, text="Mar", font='Arial 12 bold', bd=3,
    fg='white', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='pale turquoise',
    command=marSearch)
buttonMar.pack(in_=top3, side=LEFT, padx=10, pady=10)

def avrSearch():
    for path, dirs, files in os.walk('./patient_agenda/'\
        'events12/doc_events/fix_agenda/agenda_saved/'):
        for file in files:
            with open(os.path.join(path, file),'r') as jan_read:
                lines = jan_read.readlines()
                for i in range(0, len(lines)):
                    for line in lines:
                        line.replace('{', '')
                        line.replace('}', '')
                        line = lines[i]
                        if line[3:5] == "04":
                            textBox.insert(INSERT, lines[i-1])
                            textBox.insert(INSERT, lines[i])
                            textBox.insert(INSERT, lines[i+1])
                            textBox.insert(INSERT, lines[i+2])
                            textBox.insert(INSERT, '\n')
                            break

buttonAvr = Button(fen, text="Avr", font='Arial 12 bold', bd=3,
    fg='white', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='pale turquoise',
    command=avrSearch)
buttonAvr.pack(in_=top3, side=LEFT, padx=10, pady=10)

def maiSearch():
    for path, dirs, files in os.walk('./patient_agenda/'\
        'events12/doc_events/fix_agenda/agenda_saved/'):
        for file in files:
            with open(os.path.join(path, file),'r') as jan_read:
                lines = jan_read.readlines()
                for i in range(0, len(lines)):
                    for line in lines:
                        line.replace('{', '')
                        line.replace('}', '')
                        line = lines[i]
                        if line[3:5] == "05":
                            textBox.insert(INSERT, lines[i-1])
                            textBox.insert(INSERT, lines[i])
                            textBox.insert(INSERT, lines[i+1])
                            textBox.insert(INSERT, lines[i+2])
                            textBox.insert(INSERT, '\n')
                            break

buttonMay = Button(fen, text="May", font='Arial 12 bold', bd=3,
    fg='white', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='pale turquoise',
    command=maiSearch)
buttonMay.pack(in_=top3, side=LEFT, padx=10, pady=10)

def junSearch():
    for path, dirs, files in os.walk('./patient_agenda/'\
        'events12/doc_events/fix_agenda/agenda_saved/'):
        for file in files:
            with open(os.path.join(path, file),'r') as jan_read:
                lines = jan_read.readlines()
                for i in range(0, len(lines)):
                    for line in lines:
                        line.replace('{', '')
                        line.replace('}', '')
                        line = lines[i]
                        if line[3:5] == "06":
                            textBox.insert(INSERT, lines[i-1])
                            textBox.insert(INSERT, lines[i])
                            textBox.insert(INSERT, lines[i+1])
                            textBox.insert(INSERT, lines[i+2])
                            textBox.insert(INSERT, '\n')
                            break

buttonJun = Button(fen, text="Jun", font='Arial 12 bold', bd=3,
    fg='white', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='pale turquoise',
    command=junSearch)
buttonJun.pack(in_=top3, side=LEFT, padx=10, pady=10)

def julSearch():
    for path, dirs, files in os.walk('./patient_agenda/'\
        'events12/doc_events/fix_agenda/agenda_saved/'):
        for file in files:
            with open(os.path.join(path, file),'r') as jan_read:
                lines = jan_read.readlines()
                for i in range(0, len(lines)):
                    for line in lines:
                        line.replace('{', '')
                        line.replace('}', '')
                        line = lines[i]
                        if line[3:5] == "07":
                            textBox.insert(INSERT, lines[i-1])
                            textBox.insert(INSERT, lines[i])
                            textBox.insert(INSERT, lines[i+1])
                            textBox.insert(INSERT, lines[i+2])
                            textBox.insert(INSERT, '\n')
                            break

buttonJul = Button(fen, text="Jul", font='Arial 12 bold', bd=3,
    fg='white', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='pale turquoise',
    command=julSearch)
buttonJul.pack(in_=top4, side=LEFT, padx=10, pady=10)

def augSearch():
    for path, dirs, files in os.walk('./patient_agenda/'\
        'events12/doc_events/fix_agenda/agenda_saved/'):
        for file in files:
            with open(os.path.join(path, file),'r') as jan_read:
                lines = jan_read.readlines()
                for i in range(0, len(lines)):
                    for line in lines:
                        line.replace('{', '')
                        line.replace('}', '')
                        line = lines[i]
                        if line[3:5] == "08":
                            textBox.insert(INSERT, lines[i-1])
                            textBox.insert(INSERT, lines[i])
                            textBox.insert(INSERT, lines[i+1])
                            textBox.insert(INSERT, lines[i+2])
                            textBox.insert(INSERT, '\n')
                            break

buttonAug = Button(fen, text="Aug", font='Arial 12 bold', bd=3,
    fg='white', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='pale turquoise',
    command=augSearch)
buttonAug.pack(in_=top4, side=LEFT, padx=10, pady=10)

def sepSearch():
    for path, dirs, files in os.walk('./patient_agenda/'\
        'events12/doc_events/fix_agenda/agenda_saved/'):
        for file in files:
            with open(os.path.join(path, file),'r') as jan_read:
                lines = jan_read.readlines()
                for i in range(0, len(lines)):
                    for line in lines:
                        line.replace('{', '')
                        line.replace('}', '')
                        line = lines[i]
                        if line[3:5] == "09":
                            textBox.insert(INSERT, lines[i-1])
                            textBox.insert(INSERT, lines[i])
                            textBox.insert(INSERT, lines[i+1])
                            textBox.insert(INSERT, lines[i+2])
                            textBox.insert(INSERT, '\n')
                            break

buttonSep = Button(fen, text="Sep", font='Arial 12 bold', bd=3,
    fg='white', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='pale turquoise',
    command=sepSearch)
buttonSep.pack(in_=top4, side=LEFT, padx=10, pady=10)

def octSearch():
    for path, dirs, files in os.walk('./patient_agenda/'\
        'events12/doc_events/fix_agenda/agenda_saved/'):
        for file in files:
            with open(os.path.join(path, file),'r') as jan_read:
                lines = jan_read.readlines()
                for i in range(0, len(lines)):
                    for line in lines:
                        line.replace('{', '')
                        line.replace('}', '')
                        line = lines[i]
                        if line[3:5] == "10":
                            textBox.insert(INSERT, lines[i-1])
                            textBox.insert(INSERT, lines[i])
                            textBox.insert(INSERT, lines[i+1])
                            textBox.insert(INSERT, lines[i+2])
                            textBox.insert(INSERT, '\n')
                            break

buttonOct = Button(fen, text="Oct", font='Arial 12 bold', bd=3,
    fg='white', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='pale turquoise',
    command=octSearch)
buttonOct.pack(in_=top4, side=LEFT, padx=10, pady=10)

def novSearch():
    for path, dirs, files in os.walk('./patient_agenda/'\
        'events12/doc_events/fix_agenda/agenda_saved/'):
        for file in files:
            with open(os.path.join(path, file),'r') as jan_read:
                lines = jan_read.readlines()
                for i in range(0, len(lines)):
                    for line in lines:
                        line.replace('{', '')
                        line.replace('}', '')
                        line = lines[i]
                        if line[3:5] == "11":
                            textBox.insert(INSERT, lines[i-1])
                            textBox.insert(INSERT, lines[i])
                            textBox.insert(INSERT, lines[i+1])
                            textBox.insert(INSERT, lines[i+2])
                            textBox.insert(INSERT, '\n')
                            break

buttonNov = Button(fen, text="Nov", font='Arial 12 bold', bd=3,
    fg='white', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='pale turquoise',
    command=novSearch)
buttonNov.pack(in_=top4, side=LEFT, padx=10, pady=10)

def decSearch():
    for path, dirs, files in os.walk('./patient_agenda/'\
        'events12/doc_events/fix_agenda/agenda_saved/'):
        for file in files:
            with open(os.path.join(path, file),'r') as jan_read:
                lines = jan_read.readlines()
                for i in range(0, len(lines)):
                    for line in lines:
                        line.replace('{', '')
                        line.replace('}', '')
                        line = lines[i]
                        if line[3:5] == "12":
                            textBox.insert(INSERT, lines[i-1])
                            textBox.insert(INSERT, lines[i])
                            textBox.insert(INSERT, lines[i+1])
                            textBox.insert(INSERT, lines[i+2])
                            textBox.insert(INSERT, '\n')
                            break

buttonDec = Button(fen, text="Dec", font='Arial 12 bold', bd=3,
    fg='white', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='pale turquoise',
    command=decSearch)
buttonDec.pack(in_=top4, side=LEFT, padx=10, pady=10)

def clearTextbox():
    textBox.delete('0.0', "end-1c")

buttonClear = Button(fen, text="Clear", font='Arial 12 bold', 
    width=50, bd=3, fg='white', bg='RoyalBlue3',
    highlightbackground='light sky blue',
    activebackground='pale turquoise', command = clearTextbox)
buttonClear.pack(in_=top5, padx=10, pady=10)

def msgBox():
    messagebox.showwarning('WARNING',
        'Error during function call for : ' + line1)

def importFilesFromDir():
    for path, dirs, files in os.walk('./patient_agenda/'\
        'events12/doc_events/fix_agenda/agenda_saved/'):
        for file in files:
            read_f = open(os.path.join(path, file),'r')
            content = read_f.readlines()
            for li in content:
                li.replace('{', '')
                li.replace('}', '')
                textBox.insert(END, li)

try:
    importFilesFromDir()
except OSError as io_err:
    print("+ Error for calling function !")
    print(io_err)
    msgBox()

fen.mainloop()
