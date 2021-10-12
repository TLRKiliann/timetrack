#!/usr/bin/python3
# -*- coding: utf-8 -*-


import tkinter
from tkinter import *
from tkinter import messagebox
import json
import time
import os
import subprocess
from itertools import *


gui = Tk()
gui.title("Time-Track")
gui.configure(background='DodgerBlue2')

top = Frame(gui, bg='DodgerBlue2')
top2 = Frame(gui, bg='SteelBlue2')
bottom = Frame(gui, bg='DodgerBlue2')
top.pack(side=TOP)
top2.pack(side=TOP)
bottom.pack(side=BOTTOM, fill=BOTH, expand=YES)

labelTit = Label(gui, text="Save changes !", font=("Arial 16 bold"),
    fg='white', bg='DodgerBlue2')
labelTit.pack(in_=top, side=LEFT, pady=10)

with open('./newpatient/entryfile18.txt', 'r') as filename:
    line1 = filename.readline()

textname = StringVar()
entryName = Entry(gui, textvariable=textname, width=20, 
    highlightbackground='grey', bd=3)
textname.set(line1[:-1])
entryName.pack(in_=top, side=LEFT, padx=10, pady=10)

labelDate = Label(gui, text='Search date to modify : ',
    font='Arial 14 bold', fg='white', bg='DodgerBlue2')
labelDate.pack(in_=top2, side=LEFT, padx=10, pady=10)

def searchExpress():
    """
        To read multiples files in a directory
    """
    try:
        hour_var = reachHour.get()
        oclock = reachHour.get()
        regexpi_var = reachDate.get()
        mot = reachDate.get()
        for path, dirs, files in os.walk('./patient_agenda/events18/'\
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
                                    textBox.insert(INSERT, lines[i-1])
                                    textBox.insert(INSERT, lines[i])
                                    textBox.insert(INSERT, lines[i+1])
                                    textBox.insert(INSERT, lines[i+2])
                                    textBox.insert(INSERT, '\n')
                                    break
    except IndexError as ind_err:
        print("+ Index out of range", ind_err)

regexpi_var = StringVar()
reachDate = Entry(gui, textvariable=regexpi_var, width=10, 
    highlightbackground='grey', bd=3)
regexpi_var.set("00/00/2021")
reachDate.pack(in_=top2, side=LEFT, pady=10)

labelhour = Label(gui, text='Hour : ',
    font='Arial 14 bold', fg='white', bg='DodgerBlue2')
labelhour.pack(in_=top2, side=LEFT, padx=10, pady=10)

hour_var = IntVar()
reachHour = Entry(gui, textvariable=hour_var, width=5,
    highlightbackground='grey', bd=3)
hour_var.set('00:00')
reachHour.pack(in_=top2, side=LEFT, pady=10)

buttonSearch = Button(gui, text='Search', width=8, bd=3,
    fg='white', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='pale turquoise', command=searchExpress)
buttonSearch.pack(in_=top2, side=LEFT, padx=10, pady=10)

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
    for path, dirs, files in os.walk('./patient_agenda/events18/'\
        'doc_events/fix_agenda/agenda_saved/'):
        for file in files:
            read_f = open(os.path.join(path, file), 'r')
            for line in read_f:
                for k in line:
                    noway = "Fixed on :"
                    if line[0:10] == noway:
                        print("+ There is noway : ")
                        print(line[0:10])
                    elif magicword in line:
                        if oclock in line:
                            print("+ It is magicword : ")
                            print(line[0:10])
                            print(line[13:21])
                            write_f = open(os.path.join(path, file), 'w')
                            write_f.writelines(textBox.get("0.0", "end-1c"))
                            print("Modification finish")
                            break
                    else:
                        print("None file has been writted")
                        break

    secproc = subprocess.run(["scp", "-r",
        "./patient_agenda/events18/doc_events/fix_agenda/agenda_saved",
        "pi@192.168.18.12:~/tt_doc/doc_txt18/Files18"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("+ './Backup/Files18' uploaded !")
    else:
        print("+ No file to upload !")
        messagebox.showerror("Error", "./Backup/Files18 not uploaded...")

def messFromSafeButt():
    MsgBox = messagebox.askquestion("Confirm","Are you sure ?\n"
        "It will save all data !")
    if MsgBox == 'yes':
        save_input()
        textBox.insert(INSERT, "\n---Data saved !---")
        print("+ Data saved !")
    else:
        textBox.insert(INSERT, "\n---Nothing has been saved !---")
        print("+ Nothing has been saved !")

def modifList():
    """
        To read file modifrdv.txt
    """
    subprocess.run('./patient_agenda/events18/doc_events/'\
        'fix_agenda/read_file.py', check=True)

def deleteTextbox():
    textBox.delete('0.0', "end-1c")

textBox = Text(gui, height=15, width=60, font=18)
textBox.pack(in_=bottom, padx=30, pady=10)

buttonSave = Button(gui, text="Save", width=8, bd=3,
    fg='yellow', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='pale turquoise', command = messFromSafeButt)
buttonSave.pack(in_=bottom, side=LEFT, padx=10, pady=10)

buttonModif = Button(gui, text="Read", width=8, bd=3,
    fg='cyan', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='pale turquoise', command = modifList)
buttonModif.pack(in_=bottom, side=LEFT, padx=10, pady=10)

buttonDelete = Button(gui, text="Clear", width=8, bd=3,
    fg='cyan', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='pale turquoise', command = deleteTextbox)
buttonDelete.pack(in_=bottom, side=LEFT, padx=10, pady=10)

buttonQuit = Button(gui, text='Quit', width=8, bd=3,
    fg='white', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='pale turquoise', command=quit)
buttonQuit.pack(in_=bottom, side=RIGHT, padx=10, pady=10)

gui.mainloop()
