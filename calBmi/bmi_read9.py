#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
    To read data recorded.
"""


import tkinter as tk
from tkinter import messagebox


fen = tk.Tk()
fen.title("Reader BMI")
fen.configure(background='DodgerBlue2')

top = tk.Frame(fen, bg='DodgerBlue2')
bottom = tk.Frame(fen, bg='DodgerBlue2')
top.pack(side=tk.TOP)
bottom.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

labelo = tk.Label(fen, text="BMI results : ", width=15,
    font='Times 18 bold', fg='white', bg='DodgerBlue2')
labelo.pack(in_=top, side=tk.LEFT, pady=20)

labelallergy = tk.Label(fen, text="Allergy",
    font='Arial 18 bold', fg='coral', bg='DodgerBlue2')
labelallergy.pack(padx=5, pady=5)

# To read name in Entry widget
with open('./newpatient/entryfile9.txt', 'r') as filename:
    line_a = filename.readline()
    line_b = filename.readline()
    line_c = filename.readline()

text_name = tk.StringVar()
text_name.set(line_a[:-1])
Entryname = tk.Entry(fen, textvariable=text_name)
Entryname.pack(in_=top, side=tk.LEFT, pady=20)

text_all = tk.StringVar()
text_all.set(line_c[:-1])
Entryall = tk.Entry(fen, textvariable=text_all, width=60)
Entryall.pack(padx=10, pady=5)

def importationFile(fichier, encodage="Utf-8"):
    file = open(fichier, 'r', encoding=encodage)
    content = file.readlines()
    file.close()
    for li in content:
        textBox.insert(tk.END, li)

def msgBox():
    tk.messagebox.showinfo('Info', 'File bmi9.txt does not exist')

textBox = tk.Text(fen, height=15, width=60, font=18)
textBox.pack(padx=30, pady=30)

buttonClose = tk.Button(fen, text="Quit", width=10, bd=3,
    fg='cyan', bg='RoyalBlue3', activebackground='pale turquoise',
    activeforeground='navy', highlightbackground='cyan',
    command=quit)
buttonClose.pack(side=tk.RIGHT, padx=10, pady=10)

try:
    importationFile('./calBmi/bmi9.txt', encodage="Utf-8")
except FileNotFoundError as error_call:
    print("+ Import bmi.txt for " + line_a + " failed !")
    msgBox()

fen.mainloop()
