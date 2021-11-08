#!/usr/bin/python3
# -*- coding: utf-8 -*-


import tkinter as tk
from tkinter import messagebox
import os
import subprocess


fen = tk.Tk()
fen.title("Diagnosis and ATCD 23")
fen.configure(background='DodgerBlue2')

top = tk.Frame(fen, bg='DodgerBlue2')
bottom = tk.Frame(fen, bg='DodgerBlue2')
top.pack(side=tk.TOP)
bottom.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)

labelo = tk.Label(fen, text="Diagnostics and ATCD for : ",
    font='Arial 18 bold', fg='white', bg='DodgerBlue2')
labelo.pack(in_=top, side=tk.LEFT, padx=5, pady=20)

with open('./newpatient/entryfile23.txt', 'r') as filename:
    line_a = filename.readline()
    line_b = filename.readline()
    line_c = filename.readline()

entrytext = tk.StringVar()
entrytext.set(line_a[:-1])
entryName = tk.Entry(fen, textvariable=entrytext)
entryName.pack(in_=top, side=tk.LEFT, padx=10, pady=20)

labelallergy = tk.Label(fen, text="Allergy",
    font='Arial 18 bold', fg='coral', bg='DodgerBlue2')
labelallergy.pack(padx=5, pady=10)

entrytext = tk.StringVar()
entrytext.set(line_c[:-1])
entryName = tk.Entry(fen, textvariable=entrytext, width=60)
entryName.pack(padx=10, pady=10)

def importationFile(fichier, encodage="Utf-8"):
    file = open(fichier, 'r', encoding=encodage)
    content = file.readlines()
    file.close()
    for li in content:
        textBox.insert(tk.END, li)

textBox = tk.Text(fen, height=15, width=60, font=18, relief=tk.SUNKEN)
textBox.pack(padx=30, pady=30)

try:
    if os.path.getsize('./diag/doc_diag23/diagrecap23.txt'):
        importationFile('./diag/doc_diag23/diagrecap23.txt',
            encodage="Utf-8")
except FileNotFoundError as err_file:
    print(err_file)
    tk.messagebox.showwarning("WARNING", "File diagrecap23.txt "\
        "doesn't exist or file not found !")

buttonClose = tk.Button(fen, text="Quit", width=10, bd=3,
    fg='white', bg='RoyalBlue3',
    activebackground='pale turquoise', activeforeground='navy',
    highlightbackground='light sky blue', command=quit)
buttonClose.pack(side=tk.RIGHT, padx=10, pady=10)

fen.mainloop()
