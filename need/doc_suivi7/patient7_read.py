#!/usr/bin/python3
# -*- coding: utf-8 -*-


import tkinter as tk
from tkinter import messagebox
import os


fen = tk.Tk()
fen.title("Time-Track")
fen.configure(background='DodgerBlue2')
fen.resizable(False, False)

top = tk.Frame(fen, bg='DodgerBlue2')
bottom = tk.Frame(fen, bg='DodgerBlue2')
top.pack(side=tk.TOP)
bottom.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

labelo = tk.Label(fen, text="Care and monitoring : ",
    font='Times 18 bold', fg='navy', bg='DodgerBlue2')
labelo.pack(in_=top, side=tk.LEFT, padx=5, pady=20)

# To read name in Entry widget
with open('./newpatient/entryfile7.txt', 'r') as filename:
    line_a=filename.readline()
    line_b=filename.readline()
    line_c=filename.readline()

text_name = tk.StringVar()
text_name.set(line_a[:-1])
Entryname = tk.Entry(fen, textvariable=text_name)
Entryname.pack(in_=top, side=tk.LEFT, padx=10, pady=20)

labelallergy = tk.Label(fen, text="Allergy",
    font='Arial 18 bold', fg='coral', bg='DodgerBlue2')
labelallergy.pack(padx=5, pady=5)

text_all = tk.StringVar()
text_all.set(line_c[:-1])
Entryall = tk.Entry(fen, textvariable=text_all, width=60)
Entryall.pack(padx=10, pady=5)

def importationFile(fichier, encodage="Utf-8"):
    file = open(fichier, 'r', encoding=encodage)
    content=file.readlines()
    file.close()
    for li in content:
        textBox.insert(tk.END, li)

textBox = tk.Text(fen, height=20, width=80, font=18, relief=tk.SUNKEN)
textBox.pack(padx=30, pady=30)

buttonClose = tk.Button(fen, text="Quit", width=10, bd=3,
    fg='white', bg='RoyalBlue3',
    activebackground='pale turquoise', activeforeground='navy',
    highlightbackground='light sky blue', command=quit)
buttonClose.pack(side=tk.RIGHT, padx=10, pady=10)

try:
    if os.path.getsize('./need/doc_suivi7/main_14b.txt'):
        importationFile('./need/doc_suivi7/main_14b.txt',
            encodage="Utf-8")
except FileNotFoundError as err_nffile:
    print(err_nffile)
    tk.messagebox.showwarning("WARNING", "File does not exist or "
        "file not found !")

fen.mainloop()
