#!/usr/bin/python3
# -*- coding: utf-8 -*-


from tkinter import *
from tkinter import messagebox
import os


fen = Tk()
fen.title("Vital parameters")
fen.configure(background='DodgerBlue2')

top = Frame(fen, bg='DodgerBlue2')
bottom = Frame(fen, bg='DodgerBlue2')
top.pack(side=TOP)
bottom.pack(side=BOTTOM, fill=BOTH, expand=YES)

labelo = Label(fen, text="Vital parameters : ", width=20,
    font='Times 18 bold', fg='cyan', bg='DodgerBlue2')
labelo.pack(in_=top, side=LEFT, pady=20)

labelallergy = Label(fen, text="Allergy",
    font='Arial 18 bold', fg='coral', bg='DodgerBlue2')
labelallergy.pack(padx=5, pady=5)

with open('./newpatient/entryfile9.txt', 'r') as filename:
    line1 = filename.readline()

text_name = StringVar()
Entryname = Entry(fen, textvariable=text_name)
text_name.set(line1[:-1])
Entryname.pack(in_=top, side=LEFT, pady=20)

with open('./allergy/allergyfile9.txt', 'r') as allerfile:
    line_a = allerfile.readline()

text_all = StringVar()
Entryall = Entry(fen, textvariable=text_all, width=60)
text_all.set(line_a)
Entryall.pack(padx=10, pady=5)

textBox = Text(fen, height=15, width=60, font=18)
textBox.pack(padx=30, pady=30)

def importationFile(fichier, encodage="Utf-8"):
    file = open(fichier, 'r', encoding=encodage)
    content=file.readlines()
    file.close()
    for li in content:
        textBox.insert(END, li)

buttonClose = Button(fen, text="Quit", width=10, fg='white',
    bg='RoyalBlue3', activebackground='pale turquoise',
    activeforeground='navy', command=quit)
buttonClose.pack(side='right', padx=10, pady=10)

try:
    if os.path.getsize('./param/paramdata9.txt'):
        importationFile('./param/paramdata9.txt', encodage="Utf-8")
except FileNotFoundError as nf_file:
    print("+ File paramdata9 not found !", nf_file)
    messagebox.showwarning('Warning', 'No recorded data !')

fen.mainloop()
