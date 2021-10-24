#!/usr/bin/python3
# -*- coding: utf-8 -*-


import tkinter as tk
from tkinter import messagebox
import os
import posixpath


fen=tk.Tk()
fen.title("Time-Track")
fen.configure(background='DodgerBlue2')
fen.resizable(False, False)

top = tk.Frame(fen, bg='DodgerBlue2')
top2 = tk.Frame(fen, bg='DodgerBlue2')
top3 = tk.Frame(fen, bg='SteelBlue2')
top4 = tk.Frame(fen, bg='SteelBlue2')
top5 = tk.Frame(fen, bg='DodgerBlue2')
bottom = tk.Frame(fen, bg='DodgerBlue2')
top.pack(side=tk.TOP)
top2.pack(side=tk.TOP)
top3.pack(side=tk.TOP)
top4.pack(side=tk.TOP)
top5.pack(side=tk.TOP)
bottom.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=tk.YES)

labelo = tk.Label(fen, text="Appointments",
    font='Arial 18 bold', fg='white', bg='DodgerBlue2')
labelo.pack(in_=top, side=tk.LEFT, pady=5)

with open('./newpatient/entryfile.txt', 'r') as filename:
    line1 = filename.readline()

textentry = tk.StringVar()
entrylab = tk.Entry(fen, textvariable=textentry, width=20, 
    highlightbackground='grey', bd=3)
textentry.set(line1[:-1])
entrylab.pack(in_=top, side=tk.RIGHT, padx=10, pady=10)

textBox = tk.Text(fen, height=20, width=60, font=18)
textBox.pack(in_=top2, padx=30, pady=10)

def janSearch():
    """
        To search by months and sort() date
    """
    for path, dirs, files in os.walk('./patient_agenda/'\
        'events/doc_events/fix_agenda/agenda_saved/'):
        for file in files:
            with open(os.path.join(path, file),'r') as jan_read:
                lines = jan_read.readlines()
                for i in range(0, len(lines)):
                    for line in lines:
                        line.replace('{', '')
                        line.replace('}', '')
                        line = lines[i]
                        if line[3:5] == "01":
                            textBox.insert(tk.INSERT, lines[i-1])
                            textBox.insert(tk.INSERT, lines[i])
                            textBox.insert(tk.INSERT, lines[i+1])
                            textBox.insert(tk.INSERT, lines[i+2])
                            textBox.insert(tk.INSERT, '\n')
                            print(lines[i])
                            break

buttonJan = tk.Button(fen, text="Jan", font='Arial 12 bold', bd=3,
    fg='white', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='pale turquoise', command=janSearch)
buttonJan.pack(in_=top3, side=tk.LEFT, padx=10, pady=10)

def febSearch():
    for path, dirs, files in os.walk('./patient_agenda/'\
        'events/doc_events/fix_agenda/agenda_saved/'):
        for file in files:
            with open(os.path.join(path, file),'r') as jan_read:
                lines = jan_read.readlines()
                for i in range(0, len(lines)):
                    for line in lines:
                        line.replace('{', '')
                        line.replace('}', '')
                        line = lines[i]
                        if line[3:5] == "02":
                            textBox.insert(tk.INSERT, lines[i-1])
                            textBox.insert(tk.INSERT, lines[i])
                            textBox.insert(tk.INSERT, lines[i+1])
                            textBox.insert(tk.INSERT, lines[i+2])
                            textBox.insert(tk.INSERT, '\n')
                            break

buttonFeb = tk.Button(fen, text="Feb", font='Arial 12 bold', bd=3,
    fg='white', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='pale turquoise', command=febSearch)
buttonFeb.pack(in_=top3, side=tk.LEFT, padx=10, pady=10)

def marSearch():
    for path, dirs, files in os.walk('./patient_agenda/'\
        'events/doc_events/fix_agenda/agenda_saved/'):
        for file in files:
            with open(os.path.join(path, file),'r') as jan_read:
                lines = jan_read.readlines()
                for i in range(0, len(lines)):
                    for line in lines:
                        line.replace('{', '')
                        line.replace('}', '')
                        line = lines[i]
                        if line[3:5] == "03":
                            textBox.insert(tk.INSERT, lines[i-1])
                            textBox.insert(tk.INSERT, lines[i])
                            textBox.insert(tk.INSERT, lines[i+1])
                            textBox.insert(tk.INSERT, lines[i+2])
                            textBox.insert(tk.INSERT, '\n')
                            break

buttonMar = tk.Button(fen, text="Mar", font='Arial 12 bold', bd=3,
    fg='white', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='pale turquoise', command=marSearch)
buttonMar.pack(in_=top3, side=tk.LEFT, padx=10, pady=10)

def avrSearch():
    for path, dirs, files in os.walk('./patient_agenda/'\
        'events/doc_events/fix_agenda/agenda_saved/'):
        for file in files:
            with open(os.path.join(path, file),'r') as jan_read:
                lines = jan_read.readlines()
                for i in range(0, len(lines)):
                    for line in lines:
                        line.replace('{', '')
                        line.replace('}', '')
                        line = lines[i]
                        if line[3:5] == "04":
                            textBox.insert(tk.INSERT, lines[i-1])
                            textBox.insert(tk.INSERT, lines[i])
                            textBox.insert(tk.INSERT, lines[i+1])
                            textBox.insert(tk.INSERT, lines[i+2])
                            textBox.insert(tk.INSERT, '\n')
                            break

buttonAvr = tk.Button(fen, text="Avr", font='Arial 12 bold', bd=3,
    fg='white', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='pale turquoise', command=avrSearch)
buttonAvr.pack(in_=top3, side=tk.LEFT, padx=10, pady=10)

def maiSearch():
    for path, dirs, files in os.walk('./patient_agenda/'\
        'events/doc_events/fix_agenda/agenda_saved/'):
        for file in files:
            with open(os.path.join(path, file),'r') as jan_read:
                lines = jan_read.readlines()
                for i in range(0, len(lines)):
                    for line in lines:
                        line.replace('{', '')
                        line.replace('}', '')
                        line = lines[i]
                        if line[3:5] == "05":
                            textBox.insert(tk.INSERT, lines[i-1])
                            textBox.insert(tk.INSERT, lines[i])
                            textBox.insert(tk.INSERT, lines[i+1])
                            textBox.insert(tk.INSERT, lines[i+2])
                            textBox.insert(tk.INSERT, '\n')
                            break

buttonMay = tk.Button(fen, text="May", font='Arial 12 bold', bd=3,
    fg='white', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='pale turquoise', command=maiSearch)
buttonMay.pack(in_=top3, side=tk.LEFT, padx=10, pady=10)

def junSearch():
    for path, dirs, files in os.walk('./patient_agenda/'\
        'events/doc_events/fix_agenda/agenda_saved/'):
        for file in files:
            with open(os.path.join(path, file),'r') as jan_read:
                lines = jan_read.readlines()
                for i in range(0, len(lines)):
                    for line in lines:
                        line.replace('{', '')
                        line.replace('}', '')
                        line = lines[i]
                        if line[3:5] == "06":
                            textBox.insert(tk.INSERT, lines[i-1])
                            textBox.insert(tk.INSERT, lines[i])
                            textBox.insert(tk.INSERT, lines[i+1])
                            textBox.insert(tk.INSERT, lines[i+2])
                            textBox.insert(tk.INSERT, '\n')
                            break

buttonJun = tk.Button(fen, text="Jun", font='Arial 12 bold', bd=3,
    fg='white', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='pale turquoise', command=junSearch)
buttonJun.pack(in_=top3, side=tk.LEFT, padx=10, pady=10)

def julSearch():
    for path, dirs, files in os.walk('./patient_agenda/'\
        'events/doc_events/fix_agenda/agenda_saved/'):
        for file in files:
            with open(os.path.join(path, file),'r') as jan_read:
                lines = jan_read.readlines()
                for i in range(0, len(lines)):
                    for line in lines:
                        line.replace('{', '')
                        line.replace('}', '')
                        line = lines[i]
                        if line[3:5] == "07":
                            textBox.insert(tk.INSERT, lines[i-1])
                            textBox.insert(tk.INSERT, lines[i])
                            textBox.insert(tk.INSERT, lines[i+1])
                            textBox.insert(tk.INSERT, lines[i+2])
                            textBox.insert(tk.INSERT, '\n')
                            break

buttonJul = tk.Button(fen, text="Jul", font='Arial 12 bold', bd=3,
    fg='white', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='pale turquoise', command=julSearch)
buttonJul.pack(in_=top4, side=tk.LEFT, padx=10, pady=10)

def augSearch():
    for path, dirs, files in os.walk('./patient_agenda/'\
        'events/doc_events/fix_agenda/agenda_saved/'):
        for file in files:
            with open(os.path.join(path, file),'r') as jan_read:
                lines = jan_read.readlines()
                for i in range(0, len(lines)):
                    for line in lines:
                        line.replace('{', '')
                        line.replace('}', '')
                        line = lines[i]
                        if line[3:5] == "08":
                            textBox.insert(tk.INSERT, lines[i-1])
                            textBox.insert(tk.INSERT, lines[i])
                            textBox.insert(tk.INSERT, lines[i+1])
                            textBox.insert(tk.INSERT, lines[i+2])
                            textBox.insert(tk.INSERT, '\n')
                            break

buttonAug = tk.Button(fen, text="Aug", font='Arial 12 bold', bd=3,
    fg='white', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='pale turquoise', command=augSearch)
buttonAug.pack(in_=top4, side=tk.LEFT, padx=10, pady=10)

def sepSearch():
    for path, dirs, files in os.walk('./patient_agenda/'\
        'events/doc_events/fix_agenda/agenda_saved/'):
        for file in files:
            with open(os.path.join(path, file),'r') as jan_read:
                lines = jan_read.readlines()
                for i in range(0, len(lines)):
                    for line in lines:
                        line.replace('{', '')
                        line.replace('}', '')
                        line = lines[i]
                        if line[3:5] == "09":
                            textBox.insert(tk.INSERT, lines[i-1])
                            textBox.insert(tk.INSERT, lines[i])
                            textBox.insert(tk.INSERT, lines[i+1])
                            textBox.insert(tk.INSERT, lines[i+2])
                            textBox.insert(tk.INSERT, '\n')
                            break

buttonSep = tk.Button(fen, text="Sep", font='Arial 12 bold', bd=3,
    fg='white', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='pale turquoise', command=sepSearch)
buttonSep.pack(in_=top4, side=tk.LEFT, padx=10, pady=10)

def octSearch():
    for path, dirs, files in os.walk('./patient_agenda/'\
        'events/doc_events/fix_agenda/agenda_saved/'):
        for file in files:
            with open(os.path.join(path, file),'r') as jan_read:
                lines = jan_read.readlines()
                for i in range(0, len(lines)):
                    for line in lines:
                        line.replace('{', '')
                        line.replace('}', '')
                        line = lines[i]
                        if line[3:5] == "10":
                            textBox.insert(tk.INSERT, lines[i-1])
                            textBox.insert(tk.INSERT, lines[i])
                            textBox.insert(tk.INSERT, lines[i+1])
                            textBox.insert(tk.INSERT, lines[i+2])
                            textBox.insert(tk.INSERT, '\n')
                            break

buttonOct = tk.Button(fen, text="Oct", font='Arial 12 bold', bd=3,
    fg='white', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='pale turquoise', command=octSearch)
buttonOct.pack(in_=top4, side=tk.LEFT, padx=10, pady=10)

def novSearch():
    for path, dirs, files in os.walk('./patient_agenda/'\
        'events/doc_events/fix_agenda/agenda_saved/'):
        for file in files:
            with open(os.path.join(path, file),'r') as jan_read:
                lines = jan_read.readlines()
                for i in range(0, len(lines)):
                    for line in lines:
                        line.replace('{', '')
                        line.replace('}', '')
                        line = lines[i]
                        if line[3:5] == "11":
                            textBox.insert(tk.INSERT, lines[i-1])
                            textBox.insert(tk.INSERT, lines[i])
                            textBox.insert(tk.INSERT, lines[i+1])
                            textBox.insert(tk.INSERT, lines[i+2])
                            textBox.insert(tk.INSERT, '\n')
                            break

buttonNov = tk.Button(fen, text="Nov", font='Arial 12 bold', bd=3,
    fg='white', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='pale turquoise', command=novSearch)
buttonNov.pack(in_=top4, side=tk.LEFT, padx=10, pady=10)

def decSearch():
    for path, dirs, files in os.walk('./patient_agenda/'\
        'events/doc_events/fix_agenda/agenda_saved/'):
        for file in files:
            with open(os.path.join(path, file),'r') as jan_read:
                lines = jan_read.readlines()
                for i in range(0, len(lines)):
                    for line in lines:
                        line.replace('{', '')
                        line.replace('}', '')
                        line = lines[i]
                        if line[3:5] == "12":
                            textBox.insert(tk.INSERT, lines[i-1])
                            textBox.insert(tk.INSERT, lines[i])
                            textBox.insert(tk.INSERT, lines[i+1])
                            textBox.insert(tk.INSERT, lines[i+2])
                            textBox.insert(tk.INSERT, '\n')
                            break

buttonDec = tk.Button(fen, text="Dec", font='Arial 12 bold', bd=3,
    fg='white', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='pale turquoise', command=decSearch)
buttonDec.pack(in_=top4, side=tk.LEFT, padx=10, pady=10)

def clearTextbox():
    textBox.delete('0.0', "end-1c")

buttonClear = tk.Button(fen, text="Clear", font='Arial 12 bold', 
    width=50, bd=3, fg='white', bg='RoyalBlue3',
    highlightbackground='cyan', activebackground='pale turquoise',
    command = clearTextbox)
buttonClear.pack(in_=top5, padx=10, pady=10)

def msgBox():
    tk.messagebox.showwarning('WARNING',
        'Error during function call for : ' + line1)

def importFilesFromDir():
    for path, dirs, files in os.walk('./patient_agenda/'\
        'events/doc_events/fix_agenda/agenda_saved/'):
        for file in files:
            read_f = open(os.path.join(path, file),'r')
            content = read_f.readlines()
            for li in content:
                li.replace('{', '')
                li.replace('}', '')
                textBox.insert(tk.END, li)

try:
    importFilesFromDir()
except OSError as io_err:
    print("[!] Error for calling function !")
    print(io_err)
    msgBox()

fen.mainloop()
