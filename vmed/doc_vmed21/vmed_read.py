#!/usr/bin/python3
# -*- coding: utf-8 -*-


from tkinter import *
from tkinter import messagebox
import os
import subprocess


fen=Tk()
fen.title("Results of Medical Visit")
fen.configure(background='DodgerBlue2')

# To place side by side labelo + entrylab
top = Frame(fen, bg='DodgerBlue2')
bottom = Frame(fen, bg='DodgerBlue2')
top.pack(side=TOP)
bottom.pack(side=BOTTOM, fill=BOTH, expand=YES)

labelo=Label(fen, text="Results of Medical Visit for : ",
    font='Arial 18 bold', fg='white', bg='DodgerBlue2')
labelo.pack(in_=top, side=LEFT, padx=5, pady=20)

# To display name in Entry widget
with open('./newpatient/entryfile21.txt', 'r') as filename:
    line1=filename.readline()

text_name=StringVar()
text_name.set(line1[:-1])
Entryname=Entry(fen, textvariable=text_name)
Entryname.pack(in_=top, side=LEFT, padx=10, pady=20)

labelallergy=Label(fen, text="Allergy",
    font='Arial 18 bold', fg='coral', bg='DodgerBlue2')
labelallergy.pack(padx=5, pady=5)

# To display allergy in Entry widget
with open('./newpatient/entryfile21.txt', 'r') as allerfile:
    lineA1=allerfile.readline()
    lineA2=allerfile.readline()
    lineA3=allerfile.readline()

text_aller=StringVar()
text_aller.set(lineA3[:-1])
Entryall=Entry(fen, textvariable=text_aller, width=60)
Entryall.pack(padx=10, pady=5)

def importationFile(fichier, encodage="Utf-8"):
    with open(fichier, 'r', encoding=encodage) as filer:
        content = filer.readlines()
        for li in content:
            textBox.insert(END, li)

textBox=Text(fen, height=15, width=80, font=18, relief=SUNKEN)
textBox.pack(padx=30, pady=30)

buttonClose=Button(fen, text="Quit", width=8, bd=3,
    fg='cyan', bg='RoyalBlue3', highlightbackground='cyan',
    activebackground='pale turquoise', command=quit)
buttonClose.pack(side='right', padx=10, pady=10)

try:
    if os.path.getsize('./vmed/doc_vmed21/resultvmed21.txt'):
        importationFile('./vmed/doc_vmed21/resultvmed21.txt',
            encodage="Utf-8")
except FileNotFoundError as err_file:
    print("+ File not found !", err_file)
    messagebox.showwarning("WARNING", "File does not exist or "
        "file not found !")

fen.mainloop()
