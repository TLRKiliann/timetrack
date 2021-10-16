#!/usr/bin/python3
# -*- coding: utf-8 -*-


import tkinter as tk
import os


def get(monthVal, month_start, monthEnd, month_end):
    """
        Entry at first time
        a patient with entry button
    """
    monthVal = month_start.get()
    monthEnd = month_end.get()
    print(monthVal)
    print(monthEnd)
    try:
        if os.path.getsize('./calBmi/doc_BMI11/custom_kg.txt'):
            print("+ File 'custom_kg.txt' exist !")
            with open('./calBmi/doc_BMI11/custom_kg.txt', 'w+') as namefile:
                namefile.write(monthVal)
                namefile.write('\n')
                namefile.write(monthEnd)
    except FileNotFoundError as outcom1:
        print("+ Sorry, file 'custom_kg.txt' not exist !")
        print(str(outcom1))
        print("+ File 'custom_kg.txt' created !")
        with open('./calBmi/doc_BMI11/custom_kg.txt', 'w+') as namefile:
            namefile.write(monthVal)
            namefile.write('\n')
            namefile.write(monthEnd)

    gui.destroy()

gui = tk.Tk()
gui.title("Enter date")
gui.configure(bg='DodgerBlue2')
gui.resizable(False, False)

labelName = tk.Label(gui, text='Enter date of start : ',
    font="Times 14 bold",
    fg='white', bg='DodgerBlue2')
labelName.pack(pady=10)

monthVal = tk.StringVar()
month_start = tk.Entry(gui, textvariable=monthVal,
    highlightbackground='light sky blue', bd=4)
monthVal.set("01/01/2021")
month_start.pack()

labelName = tk.Label(gui, text='Enter date of end : ',
    font="Times 14 bold",
    fg='white', bg='DodgerBlue2')
labelName.pack(pady=10)

monthEnd = tk.StringVar()
month_end = tk.Entry(gui, textvariable=monthEnd,
    highlightbackground='light sky blue', bd=4)
monthEnd.set("31/12/2021")
month_end.pack()

bouton1 = tk.Button(gui, text="Enter", width=8, bd=3,
    fg='yellow', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='pale turquoise',
    command = lambda: get(monthVal, month_start, monthEnd, month_end))
bouton1.pack(side=tk.LEFT, padx=50, pady=20)

gui.mainloop()
