#!/usr/bin/python3
# -*- coding: utf-8 -*-


from tkinter import *
from tkinter import messagebox
import os


def importationFile(fichier, encodage="Utf-8"):
    file = open(fichier, 'r', encoding=encodage)
    content = file.readlines()
    file.close()
    for li in content:
        textBox.insert('end', li)
    textBox.insert('end', '\n\n')

def importationFile2(fichier2, encodage="Utf-8"):
    with open(fichier2, 'r', encoding=encodage) as file2:
        lines = file2.readlines()
        for li2 in lines:
            textBox.insert('end', li2)
        textBox.insert('end', '\n')

stptttr = Tk()
stptttr.title("Stopped ttt and R")
stptttr.configure(background='DodgerBlue2')

top = Frame(stptttr, bg='DodgerBlue2')
bottom = Frame(stptttr, bg='DodgerBlue2')
top.pack(side=TOP)
bottom.pack(side=BOTTOM, fill=BOTH, expand=YES)

labelo = Label(stptttr, text="Stopped ttt and R : ", width=20,
    font='Times 18 bold', fg='aquamarine', bg='DodgerBlue2')
labelo.pack(in_=top, side=LEFT, pady=20)

labelallergy = Label(stptttr, text="Allergy",
    font='Arial 18 bold', fg='coral', bg='DodgerBlue2')
labelallergy.pack(padx=5, pady=5)

with open('./newpatient/entryfile11.txt', 'r') as filename:
    line1=filename.readline()

text_name = StringVar()
Entryname = Entry(stptttr, textvariable=text_name)
text_name.set(line1[:-1])
Entryname.pack(in_=top, side=LEFT, pady=20)

with open('./newpatient/entryfile11.txt', 'r') as allerfile:
    lineA1 = allerfile.readline()
    lineA2 = allerfile.readline()
    lineA3 = allerfile.readline()

text_all = StringVar()
Entryall = Entry(stptttr, textvariable=text_all, width=60)
text_all.set(lineA3[:-1])
Entryall.pack(padx=10, pady=5)

textBox = Text(stptttr, height=15, width=60, font=18)
textBox.pack(padx=30, pady=30)

buttonClose = Button(stptttr, text="Quit", width=10, bd=3,
    fg='white', bg='RoyalBlue3', highlightbackground='cyan',
    activebackground='pale turquoise', activeforeground='navy',
    command=quit)
buttonClose.pack(side='right', padx=10, pady=10)

try:
    if os.path.getsize('./ttt/doc_ttt11/intro_ts.txt'):
        importationFile('./ttt/doc_ttt11/intro_ts.txt', encodage="Utf-8")
except FileNotFoundError as no_file1:
    print("[!] File intro_ts.txt not found !", no_file1)
    messagebox.showinfo('INFO', 'File intro_ts.txt not found !')

try:
    if os.path.getsize('./ttt/doc_ttt11/ires_rs.txt'):
        importationFile2('./ttt/doc_ttt11/ires_rs.txt', encodage="Utf-8")
except FileNotFoundError as no_file2:
    print("[!] File ires_rs.txt not found !", no_file2)
    messagebox.showinfo('INFO', 'File ires_rs.txt not found !')

stptttr.mainloop()
