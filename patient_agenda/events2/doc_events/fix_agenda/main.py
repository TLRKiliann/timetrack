#!/usr/bin/python3
# -*- coding: utf-8 -*-


import tkinter as tk
from tkinter import messagebox
import json
import time
import os
import subprocess
from itertools import *


gui = tk.Tk()
gui.title("Time-Track")
gui.configure(background='DodgerBlue2')
gui.resizable(False, False)

top = tk.Frame(gui, bg='DodgerBlue2')
top2 = tk.Frame(gui, bg='SteelBlue2')
bottom = tk.Frame(gui, bg='DodgerBlue2')
top.pack(side=tk.TOP)
top2.pack(side=tk.TOP)
bottom.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=tk.YES)

labelTit = tk.Label(gui, text="Save changes !", font=("Arial 16 bold"),
    fg='white', bg='DodgerBlue2')
labelTit.pack(in_=top, side=tk.LEFT, pady=10)

with open('./newpatient/entryfile2.txt', 'r') as filename:
    line1 = filename.readline()

textname = tk.StringVar()
entryName = tk.Entry(gui, textvariable=textname, width=20, 
    highlightbackground='grey', bd=3)
textname.set(line1[:-1])
entryName.pack(in_=top, side=tk.LEFT, padx=10, pady=10)

labelDate = tk.Label(gui, text='Search date to modify : ',
    font='Arial 14 bold', fg='white', bg='DodgerBlue2')
labelDate.pack(in_=top2, side=tk.LEFT, padx=10, pady=10)

def searchExpress():
    """
        To read multiples files in a directory
    """
    try:
        hour_var = reachHour.get()
        oclock = reachHour.get()
        regexpi_var = reachDate.get()
        mot = reachDate.get()

        for path, dirs, files in os.walk('./patient_agenda/events2/'\
            'doc_events/fix_agenda/agenda_saved/'):
            for file in files:
                with open(os.path.join(path, file), 'r') as read_f:
                    lines = read_f.readlines()
                    for i in range(0, len(lines)):
                        for line in lines:
                            line = lines[i]
                            if mot in line:
                                if oclock in line:
                                    print("Print line !")
                                    textBox.insert(tk.INSERT, lines[i-1])
                                    textBox.insert(tk.INSERT, lines[i])
                                    textBox.insert(tk.INSERT, lines[i+1])
                                    textBox.insert(tk.INSERT, lines[i+2])
                                    textBox.insert(tk.INSERT, '\n')
                                    break
    except IndexError as ind_err:
        print("[!] Index out of range", ind_err)

regexpi_var = tk.StringVar()
reachDate = tk.Entry(gui, textvariable=regexpi_var, width=10, 
    highlightbackground='grey', bd=3)
regexpi_var.set(time.strftime("%d/%m/%Y"))
reachDate.pack(in_=top2, side=tk.LEFT, pady=10)

labelhour = tk.Label(gui, text='Hour : ',
    font='Arial 14 bold', fg='white', bg='DodgerBlue2')
labelhour.pack(in_=top2, side=tk.LEFT, padx=10, pady=10)

hour_var = tk.IntVar()
reachHour = tk.Entry(gui, textvariable=hour_var, width=5,
    highlightbackground='grey', bd=3)
hour_var.set('00:00')
reachHour.pack(in_=top2, side=tk.LEFT, pady=10)

buttonSearch = tk.Button(gui, text='Search', width=8, bd=3,
    fg='white', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='pale turquoise', command=searchExpress)
buttonSearch.pack(in_=top2, side=tk.LEFT, padx=10, pady=10)

def save_input():
    """
        Save data from modification rdv textbox !
        To copy to a txt file of a directory
        since a read file and from text widget
        by lines ;) !
    """
    hour_var = reachHour.get()
    oclock = reachHour.get()
    regexpi_var = reachDate.get()
    magicword = reachDate.get()

    for path, dirs, files in os.walk('./patient_agenda/events2/'\
        'doc_events/fix_agenda/agenda_saved/'):
        for file in files:
            read_f = open(os.path.join(path, file), 'r')
            for line in read_f:
                noway = "Fixed on :"
                if line[0:10] == noway:
                    print("[!] There is noway : ")
                    print(line[0:10])
                elif magicword in line:
                    if oclock in line:
                        print("[+] It is magicword : ")
                        print(line[0:10])
                        print(line[13:21])
                        write_f = open(os.path.join(path, file), 'w')
                        write_f.writelines(textBox.get("0.0", "end-1c"))
                        print("[+] Modification finish")
                        break
                else:
                    print("None file has been writted")
                    break

    secproc = subprocess.run(["scp", "-r",
        "./patient_agenda/events2/doc_events/fix_agenda/agenda_saved",
        "pi@192.168.18.12:~/tt_doc/doc_txt2/Files2"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[Upload] './Backup/Files2' uploaded !")
    else:
        print("[!] No file to upload !")
        tk.messagebox.showerror("Error", "./Backup/Files2 not uploaded...")

def messFromSafeButt():
    MsgBox = tk.messagebox.askquestion("Confirm","Are you sure ?\n"
        "It will save all data !")
    if MsgBox == 'yes':
        save_input()
        textBox.insert(tk.INSERT, "\n---Data saved !---")
        print("[+] Data saved !")
    else:
        textBox.insert(tk.INSERT, "\n---Nothing has been saved !---")
        print("[!] Nothing has been saved !")

def modifList():
    """
        To read file modifrdv.txt
    """
    subprocess.run('./patient_agenda/events2/doc_events/'\
        'fix_agenda/read_file.py', check=True)

def deleteTextbox():
    textBox.delete('0.0', "end-1c")

textBox = tk.Text(gui, height=15, width=60, font=18)
textBox.pack(in_=bottom, padx=30, pady=10)

buttonSave = tk.Button(gui, text="Save", width=8, bd=3,
    fg='yellow', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='pale turquoise', command = messFromSafeButt)
buttonSave.pack(in_=bottom, side=tk.LEFT, padx=10, pady=10)

buttonModif = tk.Button(gui, text="Read", width=8, bd=3,
    fg='cyan', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='pale turquoise', command = modifList)
buttonModif.pack(in_=bottom, side=tk.LEFT, padx=10, pady=10)

buttonDelete = tk.Button(gui, text="Clear", width=8, bd=3,
    fg='cyan', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='pale turquoise', command = deleteTextbox)
buttonDelete.pack(in_=bottom, side=tk.LEFT, padx=10, pady=10)

buttonQuit = tk.Button(gui, text='Quit', width=8, bd=3,
    fg='white', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='pale turquoise', command=quit)
buttonQuit.pack(in_=bottom, side=tk.RIGHT, padx=10, pady=10)

gui.mainloop()
