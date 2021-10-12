#!/usr/bin/python3
# -*- coding:utf-8 -*-


"""
    To record intolerance in allergy file.
    It will appear in the text zone 'Allergy'
    of app with text zone of name.
"""


import tkinter as tk
from tkinter import messagebox
import subprocess


gui = tk.Tk()
gui.title("Intolerances")
gui.configure(bg='DodgerBlue2')
gui.resizable(False, False)

def recordOption():
    """
        To save checkbox option
    """
    print(CheckVar1.get())
    if CheckVar1.get()==1:
        print("Gluten intolerance")
        with open('./allergy/aller_drop4.txt', 'a+') as file:
            file.write("Gluten, ")
    else:
        print("[!] Nothing has changes (intolerances)")

    print(CheckVar2.get())
    if CheckVar2.get()==1:
        print("Lactose intolerance")
        with open('./allergy/aller_drop4.txt', 'a+') as file:
            file.write("Lactose, ")
    else:
        print("[!] Nothing has changes (intolerances)")

    print(CheckVar3.get())
    if CheckVar3.get()==1:
        print("Saccharose intolerance")
        with open('./allergy/aller_drop4.txt', 'a+') as file:
            file.write("Saccharose, ")
    else:
        print("[!] Nothing has changes (intolerances)")

    print(CheckVar4.get())
    if CheckVar4.get()==1:
        print("Fructose intolerance")
        with open('./allergy/aller_drop4.txt', 'a+') as file:
            file.write("Fructose, ")
    else:
        print("[!] Nothing has changes (intolerances)")

    print(CheckVar5.get())
    if CheckVar5.get()==1:
        print("Eggs")
        with open('./allergy/aller_drop4.txt', 'a+') as file:
            file.write("Eggs, ")
    else:
        print("[!] Nothing has changes (intolerances)")

    print(CheckVar6.get())
    if CheckVar6.get()==1:
        print("Fish")
        with open('./allergy/aller_drop4.txt', 'a+') as file:
            file.write("Fish, ")
    else:
        print("[!] Nothing has changes (intolerances)")


    print(CheckVar7.get())
    if CheckVar7.get()==1:
        print("Shellfish")
        with open('./allergy/aller_drop4.txt', 'a+') as file:
            file.write("Shellfish, ")
    else:
        print("[!] Nothing has changes (intolerances)")

    print(CheckVar8.get())
    if CheckVar8.get()==1:
        print("Molluscs")
        with open('./allergy/aller_drop4.txt', 'a+') as file:
            file.write("Molluscs, ")
    else:
        print("[!] Nothing has changes (intolerances)")

    print(CheckVar9.get())
    if CheckVar9.get()==1:
        print("Groundnut")
        with open('./allergy/aller_drop4.txt', 'a+') as file:
            file.write("Groundnut, ")
    else:
        print("[!] Nothing has changes (intolerances)")

    print(CheckVar10.get())
    if CheckVar10.get()==1:
        print("Oleaginous")
        with open('./allergy/aller_drop4.txt', 'a+') as file:
            file.write("Oleaginous, ")
    else:
        print("[!] Nothing has changes (intolerances)")

    print(CheckVar11.get())
    if CheckVar11.get()==1:
        print("Sesame")
        with open('./allergy/aller_drop4.txt', 'a+') as file:
            file.write("Sesame, ")
    else:
        print("[!] Nothing has changes (intolerances)")

    print(CheckVar12.get())
    if CheckVar12.get()==1:
        print("Soya")
        with open('./allergy/aller_drop4.txt', 'a+') as file:
            file.write("Soya, ")
    else:
        print("[!] Nothing has changes (intolerances)")

    print(CheckVar13.get())
    if CheckVar13.get()==1:
        print("Cereals")
        with open('./allergy/aller_drop4.txt', 'a+') as file:
            file.write("Cereals, ")
    else:
        print("[!] Nothing has changes (intolerances)")

    print(CheckVar14.get())
    if CheckVar14.get()==1:
        print("Latex")
        with open('./allergy/aller_drop4.txt', 'a+') as file:
            file.write("Latex, ")
    else:
        print("[!] Nothing has changes (intolerances)")

    print(CheckVar15.get())
    if CheckVar15.get()==1:
        print("Rosacea")
        with open('./allergy/aller_drop4.txt', 'a+') as file:
            file.write("Rosacea, ")
    else:
        print("[!] Nothing has changes (intolerances)")

    print(CheckVar16.get())
    if CheckVar16.get()==1:
        print("Umbellifers")
        with open('./allergy/aller_drop4.txt', 'a+') as file:
            file.write("Umbellifers, ")
    else:
        print("[!] Nothing has changes (intolerances)")
    subprocess.run('./nutrition/updatepatient4.py', check=True)

def confRec():
    """
        To confirm that rec is finish
    """
    tk.messagebox.showinfo("Confirmation", "Record confirmed and finished !")

def saveCheck():
    """
        To ask if user want save them choices
    """
    MSB = tk.messagebox.askyesno('Save Data', 'Do you want to save data ?')
    if MSB == 1:
        recordOption()
        confRec()
        print("[+] Ok, data saved !")
        gui.destroy()
    else:
        tk.messagebox.showinfo('Return', 'Data not saved !')

Intolabel = tk.Label(gui, text="Intolerances : ", font="Times 18 bold",
    width=14, fg='white', bg='DodgerBlue2')
Intolabel.grid(sticky='w', row=0, column=0, pady=10)

# To read name in Entry widget
with open('./newpatient/entryfile4.txt', 'r') as filename:
    line1=filename.readline()

text_entry = tk.StringVar()
entryName = tk.Entry(gui, textvariable=text_entry)
text_entry.set(line1[:-1])
entryName.grid(sticky='e', row=0, column=0, padx=10, pady=10)

CheckVar1 = tk.IntVar()
C1 = tk.Checkbutton(gui, text="Gluten", fg='navy',
    bg='dark turquoise', variable=CheckVar1,
    onvalue=1, offvalue=0, height=1,
    width=40, anchor="w")
C1.grid(row=2, column=0)

CheckVar2 = tk.IntVar()
C2 = tk.Checkbutton(gui, text="Lactose", fg='navy',
    bg='dark turquoise', variable=CheckVar2,
    onvalue=1, offvalue=0, height=1,
    width=40, anchor="w")
C2.grid(row=3, column=0)

CheckVar3 = tk.IntVar()
C3 = tk.Checkbutton(gui, text="Saccharose", fg='navy',
    bg='dark turquoise', variable=CheckVar3,
    onvalue=1, offvalue=0, height=1,
    width=40, anchor="w")
C3.grid(row=4, column=0)

CheckVar4 = tk.IntVar()
C4 = tk.Checkbutton(gui, text="Fructose", fg='navy',
    bg='dark turquoise', variable=CheckVar4,
    onvalue=1, offvalue=0, height=1,
    width=40, anchor="w")
C4.grid(row=5, column=0)

#Les allergies d’origine animale :
animallabel = tk.Label(gui, text="Animal allergy", font="Times 18 bold",
    fg='white', bg='DodgerBlue2')
animallabel.grid(row=6, column=0, pady=10)

CheckVar5 = tk.IntVar()
C5 = tk.Checkbutton(gui, text="Eggs", fg='navy',
    bg='dark turquoise', variable=CheckVar5,
    onvalue=1, offvalue=0, height=1,
    width=40, anchor="w")
C5.grid(row=7, column=0)

CheckVar6 = tk.IntVar()
C6 = tk.Checkbutton(gui, text="Fish", fg='navy',
    bg='dark turquoise', variable=CheckVar6,
    onvalue=1, offvalue=0, height=1,
    width=40, anchor="w")
C6.grid(row=8, column=0)

CheckVar7 = tk.IntVar()
C7 = tk.Checkbutton(gui, text="Shellfish", fg='navy',
    bg='dark turquoise', variable=CheckVar7,
    onvalue=1, offvalue=0, height=1,
    width=40, anchor="w")
C7.grid(row=9, column=0)

CheckVar8 = tk.IntVar()
C8 = tk.Checkbutton(gui, text="Molluscs", fg='navy',
    bg='dark turquoise', variable=CheckVar8,
    onvalue=1, offvalue=0, height=1,
    width=40, anchor="w")
C8.grid(row=10, column=0)

#Les allergies d’origine végétale :
vegetallabel = tk.Label(gui, text="Vegetable allergy",
    font="Times 18 bold", fg='white', bg='DodgerBlue2')
vegetallabel.grid(row=11, column=0, pady=10)

CheckVar9 = tk.IntVar()
C9 = tk.Checkbutton(gui, text="Groundnut", fg='navy',
    bg='dark turquoise', variable=CheckVar9,
    onvalue=1, offvalue=0, height=1,
    width=40, anchor="w")
C9.grid(row=12, column=0)

CheckVar10 = tk.IntVar()
C10 = tk.Checkbutton(gui, text="Oleaginous fruits", fg='navy',
    bg='dark turquoise', variable=CheckVar10,
    onvalue=1, offvalue=0, height=1,
    width=40, anchor="w")
C10.grid(row=13, column=0)

CheckVar11 = tk.IntVar()
C11 = tk.Checkbutton(gui, text="Sesame", fg='navy',
    bg='dark turquoise', variable=CheckVar11,
    onvalue=1, offvalue=0, height=1,
    width=40, anchor="w")
C11.grid(row=14, column=0)

CheckVar12 = tk.IntVar()
C12 = tk.Checkbutton(gui, text="Soya", fg='navy',
    bg='dark turquoise', variable=CheckVar12,
    onvalue=1, offvalue=0, height=1,
    width=40, anchor="w")
C12.grid(row=15, column=0)

CheckVar13 = tk.IntVar()
C13 = tk.Checkbutton(gui, text="Cereals (wheat, rye)", fg='navy',
    bg='dark turquoise', variable=CheckVar13,
    onvalue=1, offvalue=0, height=1,
    width=40, anchor="w")
C13.grid(row=16, column=0)

CheckVar14 = tk.IntVar()
C14 = tk.Checkbutton(gui, text="Latex fruits", fg='navy',
    bg='dark turquoise', variable=CheckVar14,
    onvalue=1, offvalue=0, height=1,
    width=40, anchor="w")
C14.grid(row=17, column=0)

latexlabel = tk.Label(gui, text="Latex fruits = avocado, banana, kiwi,"
    " fig, chestnut...", font="Times 12", fg='white',
    bg='DodgerBlue2')
latexlabel.grid(row=18, column=0, pady=10)

CheckVar15 = tk.IntVar()
C15 = tk.Checkbutton(gui, text="Rosacea",
    fg='navy', bg='dark turquoise', variable=CheckVar15,
    onvalue=1, offvalue=0, height=1,
    width=40, anchor="w")
C15.grid(row=19, column=0)

rosaclabel = tk.Label(gui, text="Rosacea = apricot, cherry, strawberry...",
    font="Times 12", fg='white', bg='DodgerBlue2')
rosaclabel.grid(row=20, column=0, pady=10)

CheckVar16 = tk.IntVar()
C16 = tk.Checkbutton(gui, text="Umbellifers", fg='navy',
    bg='dark turquoise', variable=CheckVar16,
    onvalue=1, offvalue=0, height=1,
    width=40, anchor="w")
C16.grid(row=21, column=0)

ombellabel = tk.Label(gui, text="Umbellifers = dill, carrot, celery,"
    " fennel, parsley...",
    font="Times 12", fg='white', bg='DodgerBlue2')
ombellabel.grid(row=22, column=0, pady=10)

buttSave = tk.Button(gui, text="Save", width=10, fg='yellow',
    bg='RoyalBlue3', bd=3, highlightbackground='light sky blue',
    activebackground='pale turquoise', command=saveCheck)
buttSave.grid(sticky='w', row=23, column=0, padx=20, pady=10)

buttQuit = tk.Button(gui, text='Quit', width=10, fg='white',
    bg='RoyalBlue3', bd=3, highlightbackground='light sky blue',
    activebackground='pale turquoise', command=quit)
buttQuit.grid(sticky='e', row=23, column=0, padx=20, pady=10)

gui.mainloop()
