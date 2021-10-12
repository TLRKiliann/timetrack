#!/usr/bin/python3
# -*- coding: utf-8 -*-


from tkinter import *
from tkinter import messagebox
import os
import subprocess


fen=Tk()
fen.title("Diagnosis and ATCD 22")
fen.configure(background='DodgerBlue2')

# To place side by side labelo + entrylab
top=Frame(fen, bg='DodgerBlue2')
bottom=Frame(fen, bg='DodgerBlue2')
top.pack(side=TOP)
bottom.pack(side=BOTTOM, fill=BOTH, expand=YES)

labelo=Label(fen, text="Diagnostics and ATCD for : ",
    font='Arial 18 bold', fg='white', bg='DodgerBlue2')
labelo.pack(in_=top, side=LEFT, padx=5, pady=20)

with open('./newpatient/entryfile22.txt', 'r') as filename:
    line_a=filename.readline()
    line_b=filename.readline()
    line_c=filename.readline()

entrytext=StringVar()
entrytext.set(line_a[:-1])
entryName=Entry(fen, textvariable=entrytext)
entryName.pack(in_=top, side=LEFT, padx=10, pady=20)

labelallergy=Label(fen, text="Allergy",
    font='Arial 18 bold', fg='coral', bg='DodgerBlue2')
labelallergy.pack(padx=5, pady=10)

entrytext=StringVar()
entrytext.set(line_c[:-1])
entryName=Entry(fen, textvariable=entrytext, width=60)
entryName.pack(padx=10, pady=10)

def importationFile(fichier, encodage="Utf-8"):
    file = open(fichier, 'r', encoding=encodage)
    content=file.readlines()
    file.close()
    for li in content:
        textBox.insert(END, li)

textBox=Text(fen, height=15, width=60, font=18, relief=SUNKEN)
textBox.pack(padx=30, pady=30)

try:
    if os.path.getsize('./diag/doc_diag22/diagrecap22.txt'):
        importationFile('./diag/doc_diag22/diagrecap22.txt',
            encodage="Utf-8")
except FileNotFoundError as err_file:
    print(err_file)
    messagebox.showwarning("WARNING", "File diagrecap22.txt "\
        "doesn't exist or file not found !")

buttonClose=Button(fen, text="Quit", width=10, bd=3,
    fg='white', bg='RoyalBlue3',
    activebackground='pale turquoise', activeforeground='navy',
    highlightbackground='light sky blue', command=quit)
buttonClose.pack(side='right', padx=10, pady=10)

fen.mainloop()
