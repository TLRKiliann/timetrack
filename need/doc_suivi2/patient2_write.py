#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
    Script for choosing care to give.
    Usr can add lines to write.
"""


import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os
import subprocess
import time
from upload2 import needuploadata


root = tk.Tk()
root.title("Time-Track")
root.configure(background='DodgerBlue2')
root.resizable(False, False)

top = tk.Frame(root, bg='DodgerBlue2')
top2 = tk.Frame(root, bg='DodgerBlue2')
top3 = tk.Frame(root, bg='DodgerBlue2')
bottom = tk.Frame(root, bg='DodgerBlue2')
top.pack(side=tk.TOP)
top2.pack(side=tk.TOP)
top3.pack(side=tk.TOP)
bottom.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)

labelo = tk.Label(root, text="Care and monitoring : ",
    font='Times 18 bold', fg='navy', bg='DodgerBlue2')
labelo.pack(in_=top, side=tk.LEFT, padx=5, pady=20)

with open('./newpatient/entryfile2.txt', 'r') as filename:
    line_a = filename.readline()
    line_b = filename.readline()
    line_c = filename.readline()

text_name = tk.StringVar()
entryname = tk.Entry(root, textvariable=text_name)
text_name.set(line_a[:-1])
entryname.pack(in_=top, side=tk.LEFT, padx=10, pady=20)

labelallergy = tk.Label(root, text="Allergy :",
    font='Arial 18 bold', fg='coral', bg='DodgerBlue2')
labelallergy.pack(in_=top2, side=tk.LEFT, padx=5)

text_aller = tk.StringVar()
entryaller = tk.Entry(root, textvariable=text_aller, width=60)
text_aller.set(line_c[:-1])
entryaller.pack(in_=top2, side=tk.LEFT, padx=10)

def callbackItem(event):
    """
        Verify if value was caught
        and to write it into texbox.
    """
    print(itempsmt.get())
    textBox.insert(tk.END, itempsmt.get() + " :\n")

def callbackapp(event):
    textBox.insert(tk.END, itemapp.get() + " :\n")

def callbacksoins(event):
    textBox.insert(tk.END, itemsoins.get() + " :\n")

def changeitempsmt():
    """
        Permit user to choose a care with
        a ttk.Combobox() !
    """
    itempsmt["values"] = ["",
                            "Bandage",
                            "Wound dressing protocol",
                            "Repair of bandages",
                            "Meching of a wound",
                            "Stitches"]

mystring = tk.StringVar()
itempsmt = ttk.Combobox(root, textvariable=mystring, width=20,
    values=["Bandage",
            "Bandage",
            "Wound dressing protocol",
            "Repair of bandages",
            "Meching of a wound",
            "Stitches"], postcommand=changeitempsmt)

itempsmt.bind("<<ComboboxSelected>>", callbackItem)
itempsmt.current(0)
itempsmt.pack(in_=top3, side=tk.LEFT, padx=10, pady=20)

def changeitemapp():
    """
        Permit user to choose a care with
        a ttk.Combobox() !
    """
    itemapp["values"] = ["",
                            "Equipment",
                            "Vein-flon installation",
                            "Vein-flon change",
                            "Probe placement",
                            "Probe care",
                            "Probe change",
                            "Removal of probe",
                            "Collector bag return",
                            "Drain installation",
                            "Drain care",
                            "Drain change",
                            "Removal of drain",
                            "Pleurevac",
                            "Liquid appearance",
                            "Quantity of liquids",
                            "Cultivation",
                            "CIPAP",
                            "Nose cannula O²",
                            "Insulin pump",
                            "Anthalgic pump",
                            "VAC (escarre)",
                            "Pacemaker",
                            "Holter"]

mystring2 = tk.StringVar()
itemapp = ttk.Combobox(root, textvariable=mystring2, width=20,
    values=["Equipment/Sondes",
            "Equipment",
            "Vein-flon installation",
            "Vein-flon change",
            "Probe placement",
            "Probe care",
            "Probe change",
            "Removal of probe",
            "Collector bag return",
            "Drain installation",
            "Drain care",
            "Drain change",
            "Removal of drain",
            "Pleurevac",
            "Liquid appearance",
            "Quantity of liquids",
            "Cultivation",
            "CIPAP",
            "Nose cannula O²",
            "Insulin pump",
            "Anthalgic pump",
            "VAC (escarre)",
            "Pacemaker",
            "Holter"], postcommand=changeitemapp)

itemapp.bind("<<ComboboxSelected>>", callbackapp)
itemapp.current(0)
itemapp.pack(in_=top3, side=tk.LEFT, padx=10, pady=20)

def changeitemsoins():
    """
        Permit user to choose a care with
        a ttk.Combobox() !
    """
    itemsoins["values"] = ["",
                            "Exams",
                            "Water balance",
                            "Diuresis",
                            "Stix (combo)",
                            "Coproculture",
                            "Hygiene care",
                            "Care and Monitoring"]

mystring3 = tk.StringVar()
itemsoins = ttk.Combobox(root, textvariable=mystring3, width=20,
    values=["Exams",
            "Exams",
            "Water balance",
            "Diuresis",
            "Stix (combo)",
            "Coproculture",
            "Hygiene care",
            "Care and Monitoring"], postcommand=changeitemsoins)

itemsoins.bind("<<ComboboxSelected>>", callbacksoins)
itemsoins.current(0)
itemsoins.pack(in_=top3, side=tk.LEFT, padx=10, pady=20)

def ajouterText():
    """
        Retrieve data from initial textBox()
    """
    textBox.delete('0.0', tk.END)
    textBox.insert(tk.INSERT, "Implemented as : ")
    textBox.insert(tk.END, time.strftime("%d/%m/%Y at %H:%M:%S :\n"))
    textBox.update()

def suiteBackup():
    """
        Save data into file patienx_14b.txt
        'ajouterText()' function is called at the end.
    """
    with open('./need/doc_suivi2/patient2_14b.txt', 'w') as namefile:
        namefile.write("Implemented as : ")
        namefile.write(time.strftime("%d/%m/%Y at %H:%M:%S :\n"))
    tk.messagebox.showinfo("INFO", "Data saved !")
    print("[+] Data saved !")
    ajouterText()

def uploadfunc():
    needuploadata()

def saveData():
    """
        Test if file main_14b.txt exist and write data.
        A msg into textbox appear to informate user that
        data have been saved.
        'suiteBackup()' function is called at the end.
    """
    try:
        if os.path.getsize('./need/doc_suivi2/main_14b.txt'):
            print("[+] File 'main_14b.txt' exist !")
            with open('./need/doc_suivi2/main_14b.txt', 'a+') as namefile:
                namefile.write(textBox.get("0.0", "end-1c") + '\n\n')
    except FileNotFoundError as outcom:
        print("[!] Sorry, file 'main_14b.txt' not found !", outcom)
        print("[+] File 'main_14b.txt' created !")
        with open('./need/doc_suivi2/main_14b.txt', 'a+') as namefile:
            namefile.write(textBox.get("0.0", "end-1c") + '\n\n')
    textBox.insert(tk.INSERT, "\n---Data saved !---")
    suiteBackup()
    uploadfunc()

def messFromSafeButt():
    """
        Save data with button 'save' and to get function 'saveData()'
        if user wish to save. Else, user will be informed that data
        aren't saved.
    """
    MsgBox = tk.messagebox.askquestion("Confirm","Are you sure ?\n"
        "It will save all data !")
    if MsgBox == 'yes':
        saveData()
    else:
        textBox.insert(tk.INSERT, "\n---Nothing has been saved !---")
        print("[-] Nothing has been saved !")

def lectureFic():
    """
        To read file.
    """
    with open('./need/doc_suivi2/patient2_14b.txt', 'r') as f1read:
        print(f1read.read())
    subprocess.run('./need/doc_suivi2/patient2_read.py', check=True)

def importationFile(fichier, encodage="Utf-8"):
    """
        Import patientx_14b.txt file and read it.
    """
    try:
        if os.path.getsize(fichier):
            print("[+] File 'patient2_14b.txt' exist !")
            with open(fichier, 'r', encoding=encodage) as fileneeds:
                content = fileneeds.readlines()
                for li in content:
                    textBox.insert(tk.END, li)
    except FileNotFoundError as out_err:
        print("[!] Sorry, file 'main_14b.txt' not found !", out_err)

textBox = tk.Text(root, height=15, width=80, font=18, relief=tk.SUNKEN)
#textBox.insert(INSERT, "En date du : ")
#textBox.insert(END, time.strftime("%d/%m/%Y à %H:%M:%S :"))
textBox.pack(padx=30, pady=10)

buttonLire = tk.Button(root, text="Read", bd=3, width=10,
    fg='cyan', bg='RoyalBlue3', activebackground='pale turquoise',
    activeforeground='navy', highlightbackground='light sky blue',
    command=lectureFic)
buttonLire.pack(side=tk.LEFT, padx=10, pady=10)

buttonEnter = tk.Button(root, text="Save", bd=3, width=10,
    fg='yellow', bg='RoyalBlue3', activebackground='pale turquoise',
    activeforeground='navy', highlightbackground='light sky blue',
    command=messFromSafeButt)
buttonEnter.pack(side=tk.LEFT, padx=10, pady=10)

buttonQuitter = tk.Button(root, text="Quit", bd=3, width=10,
    fg='white', bg='RoyalBlue3', activebackground='pale turquoise',
    activeforeground='navy', highlightbackground='light sky blue',
    command=quit)
buttonQuitter.pack(side=tk.RIGHT, padx=10, pady=10)

try:
    if os.path.getsize('./need/doc_suivi2/patient2_14b.txt'):
        importationFile('./need/doc_suivi2/patient2_14b.txt',
            encodage='Utf-8')
except FileNotFoundError as err_nffile:
    print(err_nffile)
    tk.messagebox.showwarning("WARNING", "File does not found !")

root.mainloop()
