#!/usr/bin/python3
# -*- coding: utf-8 -*-


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

with open('./newpatient/entryfile4.txt', 'r') as filename:
    line1=filename.readline()

textname = tk.StringVar()
entryName = tk.Entry(fen, textvariable=textname)
textname.set(line1[:-1])
entryName.grid(sticky=tk.E, row=0, column=0, padx=30, pady=20)

def recordOption():
    print("+ Date : " + time.strftime("%d/%m/%Y"))
    print("+ Nom du patient : ", entryName.get())
    with open('./need/doc_suivi4/patient4_14b.txt', 'a+') as file:
        file.write("---####-|--- Affichage des besoins du patient à surveiller ---|-####---\n")
        file.write("\nEn date du : ")
        file.write(time.strftime("%d/%m/%Y à %H:%M:%S :") + '\n')
        file.write("Patient name : ")
        file.write(entryName.get() + "\n")

    print(CheckVar1.get())
    if CheckVar1.get() == 1:
        print("Surveillance respiratoire requise en ajout")
        with open('./need/doc_suivi4/patient4_14b.txt', 'a+') as file:
            file.write("+ Surveillance respiratoire requise\n")
    else:
        print("Nothing to do")

    print(CheckVar2.get())
    if CheckVar2.get() == 1:
        print("Surveillance de la température requise en ajout")
        with open('./need/doc_suivi4/patient4_14b.txt', 'a+') as file:
            file.write("+ Surveillance de la température requise\n")
    else:
        print("Nothing to do")

    print(CheckVar3.get())
    if CheckVar3.get() == 1:
        print("Surveillance alimentaire et/ou hydratation requise en ajout")
        with open('./need/doc_suivi4/patient4_14b.txt', 'a+') as file:
            file.write("+ Surveillance alimentaire et/ou hydratation requise\n")
    else:
        print("Nothing to do")

    print(CheckVar4.get())
    if CheckVar4.get() == 1:
        print("Surveillance urinaire et/ou fécale requise en ajout")
        with open('./need/doc_suivi4/patient4_14b.txt', 'a+') as file:
            file.write("+ Surveillance urinaire et/ou fécale requise\n")
    else:
        print("Nothing to do")

    print(CheckVar5.get())
    if CheckVar5.get() == 1:
        print("Surveillance du sommeil requise en ajout")
        with open('./need/doc_suivi4/patient4_14b.txt', 'a+') as file:
            file.write("+ Surveillance du sommeil requise\n")
    else:
        print("Nothing to do")

    print(CheckVar6.get())
    if CheckVar6.get() == 1:
        print("Surveillance posturale et/ou des déplacements requise en ajout")
        with open('./need/doc_suivi4/patient4_14b.txt', 'a+') as file:
            file.write("+ Surveillance posturale et/ou des déplacements requise\n")
    else:
        print("Nothing to do")

    print(CheckVar7.get())
    if CheckVar7.get() == 1:
        print("Surveillance pour éviter les dangers requise en ajout")
        with open('./need/doc_suivi4/patient4_14b.txt', 'a+') as file:
            file.write("+ Surveillance pour éviter les dangers requise\n")
    else:
        print("Nothing to do")

    print(CheckVar8.get())
    if CheckVar8.get() == 1:
        print("Surveillance propreté et/ou téguments requise en ajout")
        with open('./need/doc_suivi4/patient4_14b.txt', 'a+') as file:
            file.write("+ Surveillance propreté et/ou téguments requise\n")
    else:
        print("Nothing to do")

    print(CheckVar9.get())
    if CheckVar9.get() == 1:
        print("Surveillance ou aide pour l'habillage/déshabillage requise en ajout")
        with open('./need/doc_suivi4/patient4_14b.txt', 'a+') as file:
            file.write("+ Surveillance ou aide pour l'habillage/déshabillage requise\n")
    else:
        print("Nothing to do")

    print(CheckVar10.get())
    if CheckVar10.get() == 1:
        print("Stimulation ou aide pour la communication requise en ajout")
        with open('./need/doc_suivi4/patient4_14b.txt', 'a+') as file:
            file.write("+ Stimulation ou aide pour la communication requise\n")
    else:
        print("Nothing to do")

    print(CheckVar11.get())
    if CheckVar11.get() == 1:
        print("Agir pour aider la personne dans ses valeurs et croyances en ajout")
        with open('./need/doc_suivi4/patient4_14b.txt', 'a+') as file:
            file.write("+ Agir pour aider la personne dans ses valeurs et croyances\n")
    else:
        print("Nothing to do")

    print(CheckVar12.get())
    if CheckVar12.get() == 1:
        print("Accompagner ou aider la personne à se réaliser en ajout")
        with open('./need/doc_suivi4/patient4_14b.txt', 'a+') as file:
            file.write("+ Accompagner ou aider la personne à se réaliser\n")
    else:
        print("Nothing to do")

    print(CheckVar13.get())
    if CheckVar13.get() == 1:
        print("Accompagnement ou aide dans se recréer requis en ajout")
        with open('./need/doc_suivi4/patient4_14b.txt', 'a+') as file:
            file.write("+ Accompagnement ou aide dans se recréer requis\n")
    else:
        print("Nothing to do")

    print(CheckVar14.get())
    if CheckVar14.get() == 1:
        print("Accompagnement ou aide dans l'apprentissage requis en ajout")
        with open('./need/doc_suivi4/patient4_14b.txt', 'a+') as file:
            file.write("+ Accompagnement ou aide dans l'apprentissage requis\n")
    else:
        print("Nothing to do")

    with open('./need/doc_suivi4/patient4_14b.txt', 'a+') as file:
        file.write("---\n")

    proc = subprocess.run(["scp", "./need/doc_suivi4/patient4_14b.txt",
        "pi@192.168.18.12:~/tt_doc/doc_txt4/Files4/patient4_14b.txt"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File patient4_14b.txt uploaded !")
        tk.messagebox.showinfo("INFO", "patient4_14b.txt uploaded...")
    else:
        print("+ No file to upload !")
        tk.messagebox.showerror("Error", "No patient4_14b.txt to upload...")

def confRec():
    tk.messagebox.showinfo("Confirmation", "Record confirmed and finished !")

def recordTofile():
    MsgBox = tk.messagebox.askyesno('Record', 'Results will be saved into Care and Monitoring, ok ?')
    if MsgBox == 1:
        print("Ok data saved")
        recordOption()
        confRec()
        fen.destroy()
    else:
        tk.messagebox.showinfo('Return', 'You will return back')

CheckVar1 = tk.IntVar()
C1 = tk.Checkbutton(fen, text="Respirer", fg='navy', 
    bg='cyan', variable=CheckVar1, 
    onvalue=1, offvalue=0, height=1, 
    width=40, anchor=tk.W)
C1.grid(row=1, column=0)

CheckVar2 = tk.IntVar()
C2 = tk.Checkbutton(fen, text="Température", fg='navy', 
    bg='cyan', variable=CheckVar2, 
    onvalue=1, offvalue=0, height=1, 
    width=40, anchor=tk.W)
C2.grid(row=2, column=0)

CheckVar3 = tk.IntVar()
C3 = tk.Checkbutton(fen, text="Boire et manger", fg='navy', 
    bg='cyan', variable=CheckVar3, 
    onvalue=1, offvalue=0, height=1, 
    width=40, anchor=tk.W)
C3.grid(row=3, column=0)

CheckVar4 = tk.IntVar()
C4 = tk.Checkbutton(fen, text="Eliminer", fg='navy', 
    bg='cyan', variable=CheckVar4, 
    onvalue=1, offvalue=0, height=1, 
    width=40, anchor=tk.W)
C4.grid(row=4, column=0)

CheckVar5 = tk.IntVar()
C5 = tk.Checkbutton(fen, text="Dormir, se reposer", fg='navy', 
    bg='cyan', variable=CheckVar5, 
    onvalue=1, offvalue=0, height=1, 
    width=40, anchor=tk.W)
C5.grid(row=5, column=0)

CheckVar6 = tk.IntVar()
C6 = tk.Checkbutton(fen, text="Se mouvoir, maintenir une bonne posture", 
    fg='navy', bg='cyan', variable=CheckVar6, 
    onvalue=1, offvalue=0, height=1, 
    width=40, anchor=tk.W)
C6.grid(row=6, column=0)

CheckVar7 = tk.IntVar()
C7 = tk.Checkbutton(fen, text="Eviter les dangers", fg='navy', 
    bg='cyan', variable=CheckVar7, 
    onvalue=1, offvalue=0, height=1, 
    width=40, anchor=tk.W)
C7.grid(row=7, column=0)

CheckVar8 = tk.IntVar()
C8 = tk.Checkbutton(fen, text="Etre propre, protéger ses téguments", 
    fg='navy', bg='cyan', variable=CheckVar8, 
    onvalue=1, offvalue=0, height=1, 
    width=40, anchor=tk.W)
C8.grid(row=8, column=0)

CheckVar9 = tk.IntVar()
C9 = tk.Checkbutton(fen, text="Se vêtir et se dévêtir", 
    fg='navy', bg='cyan', variable=CheckVar9, 
    onvalue=1, offvalue=0, height=1, 
    width=40, anchor=tk.W)
C9.grid(row=9, column=0)

CheckVar10 = tk.IntVar()
C10 = tk.Checkbutton(fen, text="Communiquer avec ses semblables", 
    fg='navy', bg='cyan', variable=CheckVar10, 
    onvalue=1, offvalue=0, height=1, 
    width=40, anchor=tk.W)
C10.grid(row=10, column=0)

CheckVar11 = tk.IntVar()
C11 = tk.Checkbutton(fen, text="Agir selon ses valeurs et croyances", 
    fg='navy', bg='cyan', variable=CheckVar11, 
    onvalue=1, offvalue=0, height=1, 
    width=40, anchor=tk.W)
C11.grid(row=11, column=0)

CheckVar12 = tk.IntVar()
C12 = tk.Checkbutton(fen, text="S'occuper en vue de se réaliser", 
    fg='navy', bg='cyan', variable=CheckVar12, 
    onvalue=1, offvalue=0, 
    height=1, width=40, anchor=tk.W)
C12.grid(row=12, column=0)

CheckVar13 = tk.IntVar()
C13 = tk.Checkbutton(fen, text="Se recréer", 
    fg='navy', bg='cyan', variable=CheckVar13, 
    onvalue=1, offvalue=0, height=1, width=40,
    anchor=tk.W)
C13.grid(row=13, column=0)

CheckVar14 = tk.IntVar()
C14 = tk.Checkbutton(fen, text="Apprendre", fg='navy', 
    bg='cyan', variable=CheckVar14, 
    onvalue=1, offvalue=0, height=1,
    width=40, anchor=tk.W)
C14.grid(row=14, column=0)

buttonTocheck = tk.Button(fen, text="Save", width=10, fg='yellow',
    bg='RoyalBlue3', bd=3, highlightbackground='light sky blue',
    activebackground='pale turquoise', command=recordTofile)
buttonTocheck.grid(sticky=tk.W, row=15, column=0, padx=20, pady=10)

buttonQuit = tk.Button(fen, text='Quit', width=10, fg='white',
    bg='RoyalBlue3', bd=3, highlightbackground='light sky blue',
    activebackground='pale turquoise', command=quit)
buttonQuit.grid(sticky=tk.E,row=15, column=0, padx=20, pady=10)

fen.mainloop()
