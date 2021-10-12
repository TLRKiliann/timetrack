#!/usr/bin/python3
# -*- coding: utf-8 -*-


from tkinter import *
import tkinter as tk
from tkinter import messagebox
import time
import os
import subprocess


root = tk.Tk()
root.title("Results of Medical Visit")
root.configure(background='DodgerBlue2')

# To place side by side labelo + entrylab
top = tk.Frame(root, bg='DodgerBlue2')
bottom = tk.Frame(root, bg='DodgerBlue2')
top.pack(side=tk.TOP)
bottom.pack(side=tk.BOTTOM, fill=BOTH, expand=YES)

labelo = tk.Label(root, text="Results of Medical Visit for : ",
    font='Arial 18 bold', fg='white', bg='DodgerBlue2')
labelo.pack(in_=top, side=tk.LEFT, padx=5, pady=20)

# To read name in Entry widget
with open('./newpatient/entryfile3.txt', 'r') as filename:
    line1=filename.readline()

text_name = tk.StringVar()
Entryname = tk.Entry(root, textvariable=text_name)
text_name.set(line1[:-1])
Entryname.pack(in_=top, side=tk.LEFT, padx=10, pady=20)

labelallergy = tk.Label(root, text="Allergy",
    font='Arial 18 bold', fg='coral', bg='DodgerBlue2')
labelallergy.pack(padx=5, pady=5)

# To read allergy in Entry widget
with open('./newpatient/entryfile3.txt', 'r') as allerfile:
    lineA1=allerfile.readline()
    lineA2=allerfile.readline()
    lineA3=allerfile.readline()

text_all = tk.StringVar()
text_all.set(lineA3[:-1])
Entryaller = tk.Entry(root, textvariable=text_all, width=60)
Entryaller.pack(padx=10, pady=5)

def saveData():
    """
        No need to test if file
        exist or not. Already test
        it before.
    """
    with open('./vmed/doc_vmed3/resultvmed3.txt', 'a+') as filerecord:
        filerecord.write(textBox.get("1.0", "end-1c"))
        filerecord.write(str('\n\n'))

def uploadfile():
    """
        To upload file on server
    """
    proc = subprocess.run(["scp", "./vmed/doc_vmed3/resultvmed3.txt",
        "pi@192.168.18.12:~/tt_doc/doc_txt3/Files3/resultvmed3.txt"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File resultvmed3.txt uploaded !")
        #messagebox.showinfo("INFO", "resultvmed3.txt uploaded...")
    else:
        print("+ No file to upload !")
        messagebox.showerror("Error", "No resultvmed3.txt to upload...")

def messFromSafeButt():
    """
        Message of confirmation
        with messagebox.
    """
    MsgBox = messagebox.askquestion("Confirm","Are you sure ?\n"
        "It will save all data !")
    if MsgBox == 'yes':
        saveData()
        uploadfile()
        textBox.insert(tk.INSERT, "\n---Data saved !---")
        print("+ Data saved !")
    else:
        textBox.insert(tk.INSERT, "Nothing has been saved !")
        print("+ Nothing has been saved !")

def readerFile():
    """
        To read into the txt file.
    """
    with open('./vmed/doc_vmed3/resultvmed3.txt', 'r') as filereader:
        print(filereader.read())
    subprocess.call('./vmed/doc_vmed3/vmed_read.py')

def addText():
    """
        Display text into widget Text
        before to add comment.
    """
    textBox.delete('1.0', tk.END)
    textBox.insert(tk.INSERT, "En date du : ")
    textBox.insert(tk.END, time.strftime("%d/%m/%Y à %H:%M:%S :") + '\n')
    textBox.update()

def importationFile(fichier, encodage="Utf-8"):
    """
        First display of txt file
        when the user start app.
    """
    file = open(fichier, 'r', encoding=encodage)
    content=file.readlines()
    file.close()
    for li in content:
        textBox.insert(tk.END, li)

textBox = tk.Text(root, height=15, width=80, font=18, relief=SUNKEN)
#textBox.insert(INSERT, "\nEn date du : ")
#textBox.insert(END, time.strftime("%d/%m/%Y à %H:%M:%S :\n"))
textBox.pack(padx=30, pady=30)

buttonLire = tk.Button(root, text="Read", width=8, bd=3,
    fg='cyan', bg='RoyalBlue3', highlightbackground='cyan',
    activebackground='pale turquoise', command=readerFile)
buttonLire.pack(side=tk.LEFT, padx=10, pady=10)

buttonEffacer = tk.Button(root, text="1-Add", width=8, bd=3,
    fg='yellow', bg='RoyalBlue3', highlightbackground='cyan',
    activebackground='pale turquoise', command=addText)
buttonEffacer.pack(side=tk.LEFT, padx=10, pady=10)

buttonEnter = tk.Button(root, text="2-Save", width=8, bd=3,
    fg='yellow', bg='RoyalBlue3', highlightbackground='cyan',
    activebackground='pale turquoise',
    command=messFromSafeButt)
buttonEnter.pack(side=tk.LEFT, padx=10, pady=10)

buttonQuitter = tk.Button(root, text="Quit", width=8, bd=3,
    fg='white', bg='RoyalBlue3', highlightbackground='cyan',
    activebackground='pale turquoise', command=quit)
buttonQuitter.pack(side=tk.RIGHT, padx=10, pady=10)

try:
    if os.path.getsize('./vmed/doc_vmed3/resultvmed3.txt'):
        importationFile('./vmed/doc_vmed3/resultvmed3.txt',
            encodage="Utf-8")
except FileNotFoundError as err_file:
    print("+ File not found !", err_file)
    messagebox.showwarning("WARNING", "File does not exist "
        "or not found !")

root.mainloop()
