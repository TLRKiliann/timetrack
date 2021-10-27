#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
    checkb.py is a script to record what
    usr has checked among the 14 needs.
"""


import tkinter as tk
from tkinter import messagebox
import time
import subprocess


fen = tk.Tk()
fen.title("14 needs")
fen.configure(bg='DodgerBlue2')
fen.resizable(False, False)

labeltite = tk.Label(fen, text='14 NEEDS',
    font="Times 16 bold", width=10,
    height=3, bg='DodgerBlue2', fg='white')
labeltite.grid(sticky=tk.W, row=0, column=0, padx=20)

with open('./newpatient/entryfile20.txt', 'r') as filename:
    line1=filename.readline()

textname = tk.StringVar()
entryName = tk.Entry(fen, textvariable=textname)
textname.set(line1[:-1])
entryName.grid(sticky=tk.E, row=0, column=0, padx=30, pady=20)

def recordOption():
    """
        This function record data by writting a note
        for each requirement in file patientX_14b.txt.
    """
    print("[+] Date : " + time.strftime("%d/%m/%Y"))
    print("[+] Patient name : ", entryName.get())
    with open('./need/doc_suivi20/patient20_14b.txt', 'a+') as mfile:
        mfile.write("---####-|--- Display of the patient's needs to be monitored ---|-####---\n")
        mfile.write("\nFixed on : ")
        mfile.write(time.strftime("%d/%m/%Y at %H:%M:%S :") + '\n')
        mfile.write("Patient name : ")
        mfile.write(entryName.get() + "\n")

    if CheckVar1.get() == 1:
        print("Respiratory monitoring - required")
        with open('./need/doc_suivi20/patient20_14b.txt', 'a+') as respfile:
            respfile.write("[+] Respiratory monitoring - required\n")
    else:
        print("[---] Nothing to do")

    if CheckVar2.get() == 1:
        print("Temperature monitoring - required")
        with open('./need/doc_suivi20/patient20_14b.txt', 'a+') as tempfile:
            tempfile.write("[+] Temperature monitoring - required\n")
    else:
        print("[---] Nothing to do")

    print(CheckVar3.get())
    if CheckVar3.get() == 1:
        print("Dietary and/or hydration monitoring - required")
        with open('./need/doc_suivi20/patient20_14b.txt', 'a+') as hydrafile:
            hydrafile.write("[+] Dietary and/or hydration monitoring - required\n")
    else:
        print("[---] Nothing to do")

    print(CheckVar4.get())
    if CheckVar4.get() == 1:
        print("Urinary and/or fecal monitoring - required")
        with open('./need/doc_suivi20/patient20_14b.txt', 'a+') as elimfile:
            elimfile.write("[+] Urinary and/or fecal monitoring - required\n")
    else:
        print("[---] Nothing to do")

    print(CheckVar5.get())
    if CheckVar5.get() == 1:
        print("Sleep monitoring - required")
        with open('./need/doc_suivi20/patient20_14b.txt', 'a+') as somfile:
            somfile.write("[+] Sleep monitoring - required\n")
    else:
        print("[---] Nothing to do")

    print(CheckVar6.get())
    if CheckVar6.get() == 1:
        print("Postural and/or movement monitoring - required")
        with open('./need/doc_suivi20/patient20_14b.txt', 'a+') as mobfile:
            mobfile.write("[+] Postural and/or movement monitoring - required\n")
    else:
        print("[---] Nothing to do")

    print(CheckVar7.get())
    if CheckVar7.get() == 1:
        print("Monitoring to prevent hazards - required")
        with open('./need/doc_suivi20/patient20_14b.txt', 'a+') as dangerfile:
            dangerfile.write("[+] Monitoring to prevent hazards - required\n")
    else:
        print("[---] Nothing to do")

    print(CheckVar8.get())
    if CheckVar8.get() == 1:
        print("Cleanliness and/or integument monitoring - required")
        with open('./need/doc_suivi20/patient20_14b.txt', 'a+') as skinfile:
            skinfile.write("[+] Cleanliness and/or integument monitoring - required\n")
    else:
        print("[---] Nothing to do")

    print(CheckVar9.get())
    if CheckVar9.get() == 1:
        print("Supervision or assistance with dressing/undressing - required")
        with open('./need/doc_suivi20/patient20_14b.txt', 'a+') as wearfile:
            wearfile.write("[+] Supervision or assistance with dressing/undressing - required\n")
    else:
        print("[---] Nothing to do")

    print(CheckVar10.get())
    if CheckVar10.get() == 1:
        print("Stimulation or assistance with communication - required")
        with open('./need/doc_suivi20/patient20_14b.txt', 'a+') as speakfile:
            speakfile.write("[+] Stimulation or assistance with communication - required\n")
    else:
        print("[---] Nothing to do")

    print(CheckVar11.get())
    if CheckVar11.get() == 1:
        print("Helping the person to act on their values and beliefs")
        with open('./need/doc_suivi20/patient20_14b.txt', 'a+') as prayfile:
            prayfile.write("[+] Helping the person to act on their values and beliefs\n")
    else:
        print("[---] Nothing to do")

    print(CheckVar12.get())
    if CheckVar12.get() == 1:
        print("Accompany or help the person to realize himself")
        with open('./need/doc_suivi20/patient20_14b.txt', 'a+') as devfile:
            devfile.write("[+] Accompany or help the person to realize himself\n")
    else:
        print("[---] Nothing to do")

    print(CheckVar13.get())
    if CheckVar13.get() == 1:
        print("Accompany or help the person to recreate - required")
        with open('./need/doc_suivi20/patient20_14b.txt', 'a+') as resortfile:
            resortfile.write("[+] Accompany or help the person to recreate - required\n")
    else:
        print("[---] Nothing to do")

    print(CheckVar14.get())
    if CheckVar14.get() == 1:
        print("Accompany or assist the person in learning - required")
        with open('./need/doc_suivi20/patient20_14b.txt', 'a+') as learnfile:
            learnfile.write("[+] Accompany or assist the person in learning - required\n")
    else:
        print("[---] Nothing to do")

    with open('./need/doc_suivi20/patient20_14b.txt', 'a+') as writefile:
        writefile.write("---\n")

def confRec():
    """
        Launch subprocess to save data to ther server.
    """
    proc = subprocess.run(["scp", "./need/doc_suivi20/patient20_14b.txt",
        "pi@192.168.18.12:~/tt_doc/doc_txt20/Files20/patient20_14b.txt"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))

    if proc.stderr == b'':
        print("[Upload] File patient20_14b.txt uploaded !")
        tk.messagebox.showinfo("INFO", "patient20_14b.txt uploaded...")
    else:
        print("[!] No file patient20_14b.txt to upload !")
        tk.messagebox.showerror("Error", "No patient20_14b.txt to upload...")

    tk.messagebox.showinfo("Confirmation", "Record confirmed and finished !")

def recordTofile():
    """
        When usr click on <yes> button of msgbox,
        functions are called to save what has been
        checked with Checkbutton() widget.
    """
    MsgBox = tk.messagebox.askyesno('Record', 'Results will be saved into '\
        'Care and Monitoring, ok ?')
    if MsgBox == 1:
        recordOption()
        confRec()
        print("[+] Ok data saved")
        fen.destroy()
    else:
        tk.messagebox.showinfo('Info', 'Nothing has changed.')

CheckVar1 = tk.IntVar()
C1 = tk.Checkbutton(fen, text="Breath", fg='navy',
    bg='cyan', variable=CheckVar1,
    onvalue=1, offvalue=0, height=1,
    width=40, anchor=tk.W)
C1.grid(row=1, column=0)

CheckVar2 = tk.IntVar()
C2 = tk.Checkbutton(fen, text="Temperature", fg='navy',
    bg='cyan', variable=CheckVar2,
    onvalue=1, offvalue=0, height=1,
    width=40, anchor=tk.W)
C2.grid(row=2, column=0)

CheckVar3 = tk.IntVar()
C3 = tk.Checkbutton(fen, text="Drinking and eating", fg='navy',
    bg='cyan', variable=CheckVar3,
    onvalue=1, offvalue=0, height=1,
    width=40, anchor=tk.W)
C3.grid(row=3, column=0)

CheckVar4 = tk.IntVar()
C4 = tk.Checkbutton(fen, text="Eliminate", fg='navy',
    bg='cyan', variable=CheckVar4,
    onvalue=1, offvalue=0, height=1,
    width=40, anchor=tk.W)
C4.grid(row=4, column=0)

CheckVar5 = tk.IntVar()
C5 = tk.Checkbutton(fen, text="Sleep and rest", fg='navy',
    bg='cyan', variable=CheckVar5,
    onvalue=1, offvalue=0, height=1,
    width=40, anchor=tk.W)
C5.grid(row=5, column=0)

CheckVar6 = tk.IntVar()
C6 = tk.Checkbutton(fen, text="Move, maintain good posture",
    fg='navy', bg='cyan', variable=CheckVar6,
    onvalue=1, offvalue=0, height=1,
    width=40, anchor=tk.W)
C6.grid(row=6, column=0)

CheckVar7 = tk.IntVar()
C7 = tk.Checkbutton(fen, text="Avoiding hazards", fg='navy',
    bg='cyan', variable=CheckVar7,
    onvalue=1, offvalue=0, height=1,
    width=40, anchor=tk.W)
C7.grid(row=7, column=0)

CheckVar8 = tk.IntVar()
C8 = tk.Checkbutton(fen, text="To be clean, to protect its teguments",
    fg='navy', bg='cyan', variable=CheckVar8,
    onvalue=1, offvalue=0, height=1,
    width=40, anchor=tk.W)
C8.grid(row=8, column=0)

CheckVar9 = tk.IntVar()
C9 = tk.Checkbutton(fen, text="Dressing and undressing",
    fg='navy', bg='cyan', variable=CheckVar9,
    onvalue=1, offvalue=0, height=1,
    width=40, anchor=tk.W)
C9.grid(row=9, column=0)

CheckVar10 = tk.IntVar()
C10 = tk.Checkbutton(fen, text="Communicating with your peers",
    fg='navy', bg='cyan', variable=CheckVar10,
    onvalue=1, offvalue=0, height=1,
    width=40, anchor=tk.W)
C10.grid(row=10, column=0)

CheckVar11 = tk.IntVar()
C11 = tk.Checkbutton(fen, text="Act according to your values and beliefs",
    fg='navy', bg='cyan', variable=CheckVar11,
    onvalue=1, offvalue=0, height=1,
    width=40, anchor=tk.W)
C11.grid(row=11, column=0)

CheckVar12 = tk.IntVar()
C12 = tk.Checkbutton(fen, text="Keeping busy in order to be fulfilled",
    fg='navy', bg='cyan', variable=CheckVar12,
    onvalue=1, offvalue=0,
    height=1, width=40, anchor=tk.W)
C12.grid(row=12, column=0)

CheckVar13 = tk.IntVar()
C13 = tk.Checkbutton(fen, text="Recreating oneself",
    fg='navy', bg='cyan', variable=CheckVar13,
    onvalue=1, offvalue=0, height=1, width=40,
    anchor=tk.W)
C13.grid(row=13, column=0)

CheckVar14 = tk.IntVar()
C14 = tk.Checkbutton(fen, text="Learn", fg='navy',
    bg='cyan', variable=CheckVar14,
    onvalue=1, offvalue=0, height=1,
    width=40, anchor=tk.W)
C14.grid(row=14, column=0)

buttonTocheck = tk.Button(fen, text="Save", width=10, fg='yellow',
    bg='RoyalBlue3', bd=3, highlightbackground='light sky blue',
    activebackground='pale turquoise', command= recordTofile)
buttonTocheck.grid(sticky=tk.W, row=15, column=0, padx=20, pady=10)

buttonQuit = tk.Button(fen, text='Quit', width=10, fg='white',
    bg='RoyalBlue3', bd=3, highlightbackground='light sky blue',
    activebackground='pale turquoise', command=quit)
buttonQuit.grid(sticky=tk.E,row=15, column=0, padx=20, pady=10)

fen.mainloop()
