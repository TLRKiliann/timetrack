#!/usr/bin/python3
# -*- coding: utf-8 -*-


import tkinter as tk
from tkinter import messagebox
import os


fen = tk.Tk()
fen.title("Vital parameters")
fen.configure(background='DodgerBlue2')

top = tk.Frame(fen, bg='DodgerBlue2')
bottom = tk.Frame(fen, bg='DodgerBlue2')
top.pack(side=tk.TOP)
bottom.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=tk.YES)

labelo = tk.Label(fen, text="Vital parameters : ", width=20,
    font='Times 18 bold', fg='cyan', bg='DodgerBlue2')
labelo.pack(in_=top, side=tk.LEFT, pady=20)

labelallergy = tk.Label(fen, text="Allergy",
    font='Arial 18 bold', fg='coral', bg='DodgerBlue2')
labelallergy.pack(padx=5, pady=5)

with open('./newpatient/entryfile21.txt', 'r') as filename:
    line1 = filename.readline()

text_name = tk.StringVar()
Entryname = tk.Entry(fen, textvariable=text_name)
text_name.set(line1[:-1])
Entryname.pack(in_=top, side=tk.LEFT, pady=20)

with open('./allergy/allergyfile21.txt', 'r') as allerfile:
    line_a = allerfile.readline()

text_all = tk.StringVar()
Entryall = tk.Entry(fen, textvariable=text_all, width=60)
text_all.set(line_a[:-1])
Entryall.pack(padx=10, pady=5)

textBox = tk.Text(fen, height=15, width=60, font=18)
textBox.pack(padx=30, pady=30)

def importationFile(fichier, encodage="Utf-8"):
    file = open(fichier, 'r', encoding=encodage)
    content = file.readlines()
    file.close()
    for li in content:
        textBox.insert(tk.END, li)

buttonClose = tk.Button(fen, text="Quit",
    width=10, bd=3, 
    fg='white', bg='RoyalBlue3',
    highlightbackground='DodgerBlue2',
    activebackground='pale turquoise',
    activeforeground='navy', command=quit)
buttonClose.pack(side=tk.RIGHT, padx=10, pady=10)

try:
    if os.path.getsize('./param/paramdata21.txt'):
        importationFile('./param/paramdata21.txt', encodage="Utf-8")
except FileNotFoundError as nf_file:
    print("[!] File paramdata21 not found !", nf_file)
    messagebox.showwarning('Warning', 'No recorded data !')

fen.mainloop()
