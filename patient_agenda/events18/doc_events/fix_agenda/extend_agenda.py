#!/usr/bin/python3
# -*- coding: utf-8 -*-


import tkinter
from tkinter import *
from tkinter import messagebox
import os
import subprocess
import time
import shutil


fen = Tk()
fen.title("Time-Track")
fen.configure(background='DodgerBlue2')

# To place side by side labelo + entrylab
top = Frame(fen, bg='DodgerBlue2')
top2 = Frame(fen, bg='SteelBlue2')
bottom = Frame(fen, bg='DodgerBlue2')
top.pack(side=TOP)
top2.pack(side=TOP)
bottom.pack(side=BOTTOM, fill=BOTH, expand=YES)

labelo = Label(fen, text="Agenda",
    font='Arial 18 bold',
    fg='white', bg='DodgerBlue2')
labelo.pack(in_=top, side=LEFT, pady=10)

with open('./newpatient/entryfile18.txt', 'r') as filename:
    line1 = filename.readline()

textname = StringVar()
entryName = Entry(fen, textvariable=textname, width=20, 
    highlightbackground='grey', bd=3)
textname.set(line1[:-1])
entryName.pack(in_=top, side=LEFT, padx=10, pady=5)

labelhour = Label(fen, text="Appointment time : ",
    font='Arial 14 bold', fg='white', bg='DodgerBlue2')
labelhour.pack(in_=top2, side=LEFT, padx=10, pady=10)

def callRefresh():
    textBox.delete('2.13', END)
    textBox.update()
    textBox.insert('2.14', entrimehour.get() + \
        ' <--- RDV --- fixed !\n')

hourentr = IntVar()
entrimehour = Entry(fen, textvariable=hourentr, width=5, 
    highlightbackground='grey', bd=3)
hourentr.set("00:00")
entrimehour.pack(in_=top2, side=LEFT, pady=10)

buttonhour = Button(fen, text="Enter", width=8, bd=3,
    fg="white", bg="RoyalBlue3",
    highlightbackground='light sky blue',
    activebackground='pale turquoise', command=callRefresh)
buttonhour.pack(in_=top2, side=LEFT, padx=10, pady=10)

def importationFile(fichier):
    file = open(fichier, 'r')
    content = file.readlines()
    file.close()
    for li in content:
        textBox.insert(END, li)
        textBox.insert(END, '\n')
        textBox.delete('2.0')
        textBox.delete('end-3c')
        textBox.insert('2.14', 'Change time and press enter !')
        textBox.insert('3.0', "(Don't use more than 2 lines for writting !)")
        textBox.update()

def retrieve_input():
    """
        To retrieve data from messFromSafeButt() function
        to create a copy after backup and remove all files 
        that were used to create it.
    """
    inputValue = textBox.get("1.0", "end-1c" + '\n')
    print(inputValue)
    file_w = open('./patient_agenda/events18/doc_events/'\
        'fix_agenda/fixed_rdv.txt', 'w')
    file_w.write(textBox.get("1.0", "end-1c") + '\n\n')
    file_w.close()

    # Create the directory 
    # 'agenda_saved' in 
    # './patient_agenda/events18/doc_events/fix_agenda' 
    topath = './patient_agenda/events18/doc_events/'\
    'fix_agenda/agenda_saved'

    try:
        os.mkdir(topath)
    except OSError as err_alert:
        print(err_alert)
    
    origin_path = './patient_agenda/events18/doc_events/'\
    'fix_agenda/fixed_rdv.txt'
    main_path = './patient_agenda/events18/doc_events/'\
    'fix_agenda/agenda_saved/'

    allfiles = [None] * 1000
    for x in range(0, 1000):
        allfiles[x] = "file" + str(x) + ".txt"
        if not os.path.exists(main_path + allfiles[x]):
            shutil.copy(origin_path, main_path + allfiles[x])
            break
        elif os.path.exists(main_path + allfiles[x]):
            x += 1
        else:
            print("[!] Out of range !!! (more than 1000 files)")
            break

    try:
        os.remove('./patient_agenda/events18/doc_events/fix_agenda/fixed_rdv.txt')
        os.remove('./patient_agenda/events18/doc_events/fix_agenda/patient_value.json')
        os.remove('./patient_agenda/events18/doc_events/patient_rdv.json')
        os.remove('./patient_agenda/events18/patient_calendar.txt')
    except (OSError, FileNotFoundError) as err_rm:
        print("[Error] os.remove doesn't work for agenda 18", err_rm)

    print("[+] os.listdir after new file created : ")
    print(os.listdir('./patient_agenda/events18/doc_events/'\
        'fix_agenda/agenda_saved/'))

    # To difine file for next try
    try:
        for path, dirs, files in os.walk('./patient_agenda/events18/'
            'doc_events/fix_agenda/agenda_saved/'):
            for file in files:
                with open(os.path.join(path, file), 'r') as read_f:
                    lines = read_f.readlines()
    except (OSError, FileNotFoundError) as err_loop:
        print("[!] Loop for agenda 18 doesn't work !", err_loop)

    # To copy to ./Backup/Files10
    try:
        src18 = r'./patient_agenda/events18/doc_events/fix_agenda/agenda_saved'
        dst18 = r'./Backup/Files18'
        shutil.copy(os.path.join(src18, file), dst18)
    except (OSError, FileNotFoundError) as e18:
        print("[!] No files from agenda_18 copied !!!", e18)

    secproc = subprocess.run(["scp", "-r", "-C",
        "./patient_agenda/events18/doc_events/fix_agenda/agenda_saved",
        "pi@192.168.18.12:~/tt_doc/doc_txt18/Files18"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[Upload] './Backup/Files18' uploaded !")
    else:
        print("[!] No file to upload !")
        messagebox.showerror("Error", "./Backup/Files18 not uploaded...")

def messFromSafeButt():
    """
        To save data when user
        click button save.
    """
    MsgBox = messagebox.askquestion("Confirm","Are you sure ?\n"
        "It will save all data !")
    if MsgBox == 'yes':
        retrieve_input()
        textBox.insert(INSERT, "\n---Data saved !---")
        print("[+] Data saved !")
    else:
        textBox.insert(INSERT, "\n---Nothing has been saved !---")
        print("[!] Nothing has been saved !")

def readerFile():
    """
        To read file, app open
        file fixed rdv to read on it.
    """
    subprocess.run('./patient_agenda/events18/doc_events/'\
        'fix_agenda/read_file.py', check=True)

def changeText():
    """
        To modify rdv in agenda.
    """
    subprocess.run('./patient_agenda/events18/doc_events/'\
        'fix_agenda/main.py', check=True)

textBox = Text(fen, height=15, width=60, font=18)
textBox.insert(INSERT, "Fixed on : ")
textBox.insert(END, time.strftime("%d/%m/%Y, %H:%M:%S") + ' :\n')
textBox.pack(in_=bottom, padx=30, pady=10)

try:
    if os.path.getsize('./patient_agenda/events18/doc_events/'\
        'fix_agenda/patient_value.json'):
        print("[+] File 'patient_value.json exist' !")
        importationFile('./patient_agenda/events18/doc_events/'\
            'fix_agenda/patient_value.json')
except FileNotFoundError as nf_file:
    print("[!] File 'patient_value.json' does not exist !")
    print(nf_file)

buttonSave = Button(fen, text="Save", width=8, bd=3,
    fg='yellow', bg='RoyalBlue3',activebackground='pale turquoise',
    highlightbackground='light sky blue', command=messFromSafeButt)
buttonSave.pack(in_=bottom, side=LEFT, padx=10, pady=10)

buttonRead = Button(fen, text="Read", width=8, bd=3,
    fg='cyan', bg='RoyalBlue3', activebackground='pale turquoise',
    highlightbackground='light sky blue', command=readerFile)
buttonRead.pack(in_=bottom, side=LEFT, padx=10, pady=10)

buttonDel = Button(fen, text="Modify RDV", width=10, bd=3,
    fg='cyan', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='pale turquoise', command=changeText)
buttonDel.pack(in_=bottom, side=LEFT, padx=10, pady=10)

buttonClose = Button(fen, text="Quit", width=8, bd=3,
    fg='white', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='pale turquoise', command=quit)
buttonClose.pack(in_=bottom, side=RIGHT, padx=10, pady=10)

fen.mainloop()
