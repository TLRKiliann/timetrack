#!/usr/bin/python3
# -*- coding: utf-8 -*-


from tkinter import *
from tkinter import messagebox
import os


def importationFile(fichier, encodage="Utf-8"):
    file = open(fichier, 'r', encoding=encodage)
    content=file.readlines()
    file.close()
    for li in content:
        textBox.insert(END, li)

def importationFile2(fichier2, encodage="Utf-8"):
    file2 = open(fichier2, 'r', encoding=encodage)
    content=file2.readlines()
    file2.close()
    for li2 in content:
        textBox.insert(END, li2)

fen=Tk()
fen.title("Historic of ttt")
fen.configure(background='DodgerBlue2')

# To place side by side labelo + entrylab
top = Frame(fen, bg='DodgerBlue2')
bottom = Frame(fen, bg='DodgerBlue2')
top.pack(side=TOP)
bottom.pack(side=BOTTOM, fill=BOTH, expand=YES)

labelo=Label(fen, text="Historic of ttt : ", width=15,
    font='Times 18 bold', fg='aquamarine', bg='DodgerBlue2')
labelo.pack(in_=top, side=LEFT, pady=20)

labelallergy=Label(fen, text="Allergy",
    font='Arial 18 bold', fg='coral', bg='DodgerBlue2')
labelallergy.pack(padx=5, pady=5)

# To read name in Entry widget
with open('./newpatient/entryfile12.txt', 'r') as filename:
    line1=filename.readline()

text_name=StringVar()
Entryname=Entry(fen, textvariable=text_name)
text_name.set(line1[:-1])
Entryname.pack(in_=top, side=LEFT, pady=20)

# To read allergy in Entry widget
with open('./newpatient/entryfile12.txt', 'r') as allerfile:
    lineA1=allerfile.readline()
    lineA2=allerfile.readline()
    lineA3=allerfile.readline()

text_all=StringVar()
Entryall=Entry(fen, textvariable=text_all, width=60)
text_all.set(lineA3[:-1])
Entryall.pack(padx=10, pady=5)

textBox=Text(fen, height=15, width=60, font=18)
textBox.pack(padx=30, pady=30)

buttonClose=Button(fen, text="Quit", width=10, bd=3, fg='white', 
    bg='RoyalBlue3', highlightbackground='cyan',
    activebackground='pale turquoise', 
    activeforeground='navy', command=quit)
buttonClose.pack(side='right', padx=10, pady=10)

try:
    if os.path.getsize('./ttt/doc_ttt12/intro_ttt.txt'):
        importationFile('./ttt/doc_ttt12/intro_ttt.txt', encodage="Utf-8")
except FileNotFoundError as no_file2:
    print("[!] File intro_ttt.txt not found !", no_file2)
    messagebox.showinfo('INFO', 'File intro_ttt.txt not found !')

try:
    if os.path.getsize('./ttt/doc_ttt12/stopped_ttt.txt'):
        importationFile2('./ttt/doc_ttt12/stopped_ttt.txt', encodage="Utf-8")
except FileNotFoundError as no_file2:
    print("[!] File stopped_ttt.txt not found !", no_file2)
    messagebox.showinfo('INFO', 'File stopped_ttt.txt not found !')

fen.mainloop()
