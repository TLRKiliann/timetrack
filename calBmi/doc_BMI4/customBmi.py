#!/usr/bin/python3
# -*- coding: utf-8 -*-


from tkinter import *
from tkinter import messagebox
import os


def get(monthVal, month_start, monthEnd, month_end):
    """
        Entry at first time
        a patient with entry button
    """
    MsgBox = messagebox.askyesno('Enter dates', 'Do you want to enter these dates ?')
    if MsgBox == 1:
        monthVal = month_start.get()
        monthEnd = month_end.get()
        print(monthVal)
        print(monthEnd)
        try:
            if os.path.getsize('./calBmi/doc_BMI4/custom_kg.txt'):
                print("+ File 'custom_kg.txt' exist !")
                with open('./calBmi/doc_BMI4/custom_kg.txt', 'w+') as namefile:
                    namefile.write(monthVal)
                    namefile.write('\n')
                    namefile.write(monthEnd)
        except FileNotFoundError as outcom1:
            print("+ Sorry, file 'custom_kg.txt' not exist !")
            print(str(outcom1))
            print("+ File 'custom_kg.txt' created !")
            with open('./calBmi/doc_BMI4/custom_kg.txt', 'w+') as namefile:
                namefile.write(monthVal)
                namefile.write('\n')
                namefile.write(monthEnd)

    gui.destroy()

gui = Tk()
gui.title("Enter date")
gui.configure(bg='DodgerBlue2')

labelName = Label(gui)
labelName = Label(text='Enter date of start : ',
    font="Times 14 bold",
    fg='white', bg='DodgerBlue2')
labelName.pack(pady=10)

monthVal=StringVar()
month_start = Entry(gui, textvariable=monthVal,
    highlightbackground='light sky blue', bd=4)
monthVal.set("00-00-2021")
month_start.pack()

labelName = Label(gui)
labelName = Label(text='Enter date of end : ',
    font="Times 14 bold",
    fg='white', bg='DodgerBlue2')
labelName.pack(pady=10)

monthEnd=StringVar()
month_end = Entry(gui, textvariable=monthEnd,
    highlightbackground='light sky blue', bd=4)
monthEnd.set("00-00-2021")
month_end.pack()

bouton1 = Button(gui, text="Enter", width=8, bd=3,
    fg='yellow', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='pale turquoise',
    command = lambda: get(monthVal, month_start, monthEnd, month_end))
bouton1.pack(side=LEFT, padx=10, pady=20)

buttQuit=Button(gui, text="Quit", width=8, bd=3,
    fg='cyan', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='pale turquoise', command=quit)
buttQuit.pack(side=LEFT, padx=10, pady=20)

gui.mainloop()
