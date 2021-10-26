#!/usr/bin/python3
# -*- coding: utf-8 -*-


import tkinter as tk
from tkinter import messagebox
import os
import subprocess
import time
import shutil


fen = tk.Tk()
fen.title("Time-Track")
fen.configure(background='DodgerBlue2')
fen.resizable(False, False)

top = tk.Frame(fen, bg='DodgerBlue2')
top2 = tk.Frame(fen, bg='SteelBlue2')
bottom = tk.Frame(fen, bg='DodgerBlue2')
top.pack(side=tk.TOP)
top2.pack(side=tk.TOP)
bottom.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=tk.YES)

labelo = tk.Label(fen, text="Agenda",
    font='Arial 18 bold',
    fg='white', bg='DodgerBlue2')
labelo.pack(in_=top, side=tk.LEFT, pady=10)

with open('./newpatient/entryfile14.txt', 'r') as filename:
    line1 = filename.readline()

textname = tk.StringVar()
entryName = tk.Entry(fen, textvariable=textname, width=20, 
    highlightbackground='grey', bd=3)
textname.set(line1[:-1])
entryName.pack(in_=top, side=tk.LEFT, padx=10, pady=5)

labelhour = tk.Label(fen, text="Appointment time : ",
    font='Arial 14 bold', fg='white', bg='DodgerBlue2')
labelhour.pack(in_=top2, side=tk.LEFT, padx=10, pady=10)

def callRefresh():
    textBox.delete('2.13', tk.END)
    textBox.update()
    textBox.insert('2.14', entrimehour.get() + \
        ' <--- RDV --- fixed !\n')

hourentr = tk.IntVar()
entrimehour = tk.Entry(fen, textvariable=hourentr, width=5, 
    highlightbackground='grey', bd=3)
hourentr.set("00:00")
entrimehour.pack(in_=top2, side=tk.LEFT, pady=10)

buttonhour = tk.Button(fen, text="Enter", width=8, bd=3,
    fg="white", bg="RoyalBlue3",
    highlightbackground='light sky blue',
    activebackground='pale turquoise', command=callRefresh)
buttonhour.pack(in_=top2, side=tk.LEFT, padx=10, pady=10)

def importationFile(fichier):
    file = open(fichier, 'r')
    content = file.readlines()
    file.close()
    for li in content:
        textBox.insert(tk.END, li)
        textBox.insert(tk.END, '\n')
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
    file_w = open('./patient_agenda/events14/doc_events/'\
        'fix_agenda/fixed_rdv.txt', 'w')
    file_w.write(textBox.get("1.0", "end-1c") + '\n\n')
    file_w.close()

    # Create the directory 
    # 'agenda_saved' in 
    # './patient_agenda/events14/doc_events/fix_agenda' 
    topath = './patient_agenda/events14/doc_events/'\
    'fix_agenda/agenda_saved'

    try:
        os.mkdir(topath)
    except OSError as err_alert:
        print(err_alert)
    
    origin_path = './patient_agenda/events14/doc_events/'\
    'fix_agenda/fixed_rdv.txt'
    main_path = './patient_agenda/events14/doc_events/'\
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
        os.remove('./patient_agenda/events14/doc_events/fix_agenda/fixed_rdv.txt')
        os.remove('./patient_agenda/events14/doc_events/fix_agenda/patient_value.json')
        os.remove('./patient_agenda/events14/doc_events/patient_rdv.json')
        os.remove('./patient_agenda/events14/patient_calendar.txt')
    except (OSError, FileNotFoundError) as err_rm:
        print("[Error] os.remove doesn't work for agenda 14", err_rm)

    print("[+] os.listdir after new file created : ")
    print(os.listdir('./patient_agenda/events14/doc_events/'\
        'fix_agenda/agenda_saved/'))

    # To difine file for next try
    try:
        for path, dirs, files in os.walk('./patient_agenda/events14/'
            'doc_events/fix_agenda/agenda_saved/'):
            for file in files:
                with open(os.path.join(path, file), 'r') as read_f:
                    lines = read_f.readlines()
    except (OSError, FileNotFoundError) as err_loop:
        print("[!] Loop for agenda 14 doesn't work !", err_loop)

    # To copy to ./Backup/Files10
    try:
        src14 = r'./patient_agenda/events14/doc_events/fix_agenda/agenda_saved'
        dst14 = r'./Backup/Files14'
        shutil.copy(os.path.join(src14, file), dst14)
    except (OSError, FileNotFoundError) as e14:
        print("[!] No files from agenda_14 copied !!!", e14)

    secproc = subprocess.run(["scp", "-r", "-C",
        "./patient_agenda/events14/doc_events/fix_agenda/agenda_saved",
        "pi@192.168.18.12:~/tt_doc/doc_txt14/Files14"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[Upload] './Backup/Files14' uploaded !")
    else:
        print("[!] No file to upload !")
        tk.messagebox.showerror("Error", "./Backup/Files14 not uploaded...")

def messFromSafeButt():
    """
        To save data when user
        click button save.
    """
    MsgBox = tk.messagebox.askquestion("Confirm","Are you sure ?\n"
        "It will save all data !")
    if MsgBox == 'yes':
        retrieve_input()
        textBox.insert(tk.INSERT, "\n---Data saved !---")
        print("[+] Data saved !")
    else:
        textBox.insert(tk.INSERT, "\n---Nothing has been saved !---")
        print("[!] Nothing has been saved !")

def readerFile():
    """
        To read file, app open
        file fixed rdv to read on it.
    """
    subprocess.run('./patient_agenda/events14/doc_events/'\
        'fix_agenda/read_file.py', check=True)

def changeText():
    """
        To modify rdv in agenda.
    """
    subprocess.run('./patient_agenda/events14/doc_events/'\
        'fix_agenda/main.py', check=True)

textBox = tk.Text(fen, height=15, width=60, font=18)
textBox.insert(tk.INSERT, "Fixed on : ")
textBox.insert(tk.END, time.strftime("%d/%m/%Y, %H:%M:%S") + ' :\n')
textBox.pack(in_=bottom, padx=30, pady=10)

try:
    if os.path.getsize('./patient_agenda/events14/doc_events/'\
        'fix_agenda/patient_value.json'):
        print("[+] File 'patient_value.json exist' !")
        importationFile('./patient_agenda/events14/doc_events/'\
            'fix_agenda/patient_value.json')
except FileNotFoundError as nf_file:
    print("[!] File 'patient_value.json' does not exist !")
    print(nf_file)

buttonSave = tk.Button(fen, text="Save", width=8, bd=3,
    fg='yellow', bg='RoyalBlue3',activebackground='pale turquoise',
    highlightbackground='light sky blue', command=messFromSafeButt)
buttonSave.pack(in_=bottom, side=tk.LEFT, padx=10, pady=10)

buttonRead = tk.Button(fen, text="Read", width=8, bd=3,
    fg='cyan', bg='RoyalBlue3', activebackground='pale turquoise',
    highlightbackground='light sky blue', command=readerFile)
buttonRead.pack(in_=bottom, side=tk.LEFT, padx=10, pady=10)

buttonDel = tk.Button(fen, text="Modify RDV", width=10, bd=3,
    fg='cyan', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='pale turquoise', command=changeText)
buttonDel.pack(in_=bottom, side=tk.LEFT, padx=10, pady=10)

buttonClose = tk.Button(fen, text="Quit", width=8, bd=3,
    fg='white', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='pale turquoise', command=quit)
buttonClose.pack(in_=bottom, side=tk.RIGHT, padx=10, pady=10)

fen.mainloop()
