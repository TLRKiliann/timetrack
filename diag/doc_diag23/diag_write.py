#!/usr/bin/python3
# -*- coding: utf-8 -*-


import tkinter as tk
from tkinter import messagebox
import time
import os
import subprocess
from uploadiag23 import diagupload


root = tk.Tk()
root.title("Diagnosis and ATCD 23")
root.configure(background='DodgerBlue2')

top = tk.Frame(root, bg='DodgerBlue2')
bottom = tk.Frame(root, bg='DodgerBlue2')
top.pack(side=tk.TOP)
bottom.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)

labelo = tk.Label(root, text="Diagnostics and ATCD for : ",
    font='Arial 18 bold', fg='white', bg='DodgerBlue2')
labelo.pack(in_=top, side=tk.LEFT, padx=5, pady=20)

with open('./newpatient/entryfile23.txt', 'r') as filename:
    line_a=filename.readline()
    line_b=filename.readline()
    line_c=filename.readline()

textname = tk.StringVar()
entryName = tk.Entry(root, textvariable=textname)
textname.set(line_a[:-1])
entryName.pack(in_=top, side=tk.LEFT, padx=10, pady=20)

labelallergy = tk.Label(root, text="Allergy",
    font='Arial 18 bold', fg='coral', bg='DodgerBlue2')
labelallergy.pack(padx=5, pady=10)

entrytext = tk.StringVar()
entrytext.set(line_c[:-1])
entryName = tk.Entry(root, textvariable=entrytext, width=60)
entryName.pack(padx=10, pady=10)

def retrieve_input():
    file = open('./diag/doc_diag23/diagrecap23.txt', 'w')
    file.write(textBox.get("1.0","end-1c") + "\n\n")
    file.close()

def retrieve_upload():
    diagupload()

def saveMyButt():
    MsgBox = tk.messagebox.askquestion("Confirm", "Are you sure ?\n"\
        "It will save all data !")
    if MsgBox == 'yes':
        retrieve_input()
        retrieve_upload()
        textBox.insert(tk.INSERT, "\n--- Data saved ! ---")
        print("[+] Data saved !")
    else:
        textBox.insert(tk.INSERT, "Nothing has been saved !")
        print("[!] Nothing has been saved !")

def importationFile(fichier, encodage="Utf-8"):
    file = open(fichier, 'r', encoding=encodage)
    content = file.readlines()
    file.close()
    for li in content:
        textBox.insert(tk.END, li)

textBox = tk.Text(root, height=15, width=60, font=18, relief=tk.SUNKEN)
#textBox.insert(tk.INSERT, "En date du : ")
#textBox.insert(tk.END, time.strftime("%d/%m/%Y à %H:%M:%S :\n"))
textBox.pack(padx=30, pady=30)

try:
    if os.path.getsize('./diag/doc_diag23/diagrecap23.txt'):
        importationFile('./diag/doc_diag23/diagrecap23.txt', 
            encodage="Utf-8")
except FileNotFoundError as err_file:
    print(err_file)
    messagebox.showwarning("WARNING", "File diagrecap23.txt does "\
        "not exist or file not found !")

def lectureFic():
    subprocess.call('./diag/doc_diag23/diag_read.py')

buttonLire = tk.Button(root, text="Read", width=10, bd=3,
    fg='cyan', bg='RoyalBlue3',
    activebackground='pale turquoise', activeforeground='navy',
    highlightbackground='light sky blue', command=lectureFic)
buttonLire.pack(side=tk.LEFT, padx=10, pady=10)

buttonEnter = tk.Button(root, text="Save", width=10, bd=3,
    fg='yellow', bg='RoyalBlue3',
    activebackground='pale turquoise', activeforeground='navy',
    highlightbackground='light sky blue', command=saveMyButt)
buttonEnter.pack(side=tk.LEFT, padx=10, pady=10)

buttonQuitter = tk.Button(root, text="Quit", width=10, bd=3,
    fg='white', bg='RoyalBlue3',
    activebackground='pale turquoise', activeforeground='navy',
    highlightbackground='light sky blue', command=quit)
buttonQuitter.pack(side=tk.RIGHT, padx=10, pady=10)

root.mainloop()
