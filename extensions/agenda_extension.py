#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
    Intermediate file of functions
    to call scripts from ./param/
"""


import tkinter as tk
from tkinter import messagebox
import subprocess


def extendAgenda(self, a):
    """
        Function for calling param's subprocess.
        To decrease the opacity of the background window :
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        subprocess.run('...')
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()
    """
    if a == 1 :
        print("Patient n°", a)
        self.master.withdraw()
        subprocess.run('./patient_agenda/origin_agenda.py', check=True)
        self.master.deiconify()
    elif a == 2:
        print("Patient n°", a)
        self.master.withdraw()
        subprocess.run('./patient_agenda/origin_agenda2.py', check=True)
        self.master.deiconify()
    elif a == 3:
        print("Patient n°", a)
        self.master.withdraw()
        subprocess.run('./patient_agenda/origin_agenda3.py', check=True)
        self.master.deiconify()
    elif a == 4:
        print("Patient n°", a)
        self.master.withdraw()
        subprocess.run('./patient_agenda/origin_agenda4.py', check=True)
        self.master.deiconify()
    elif a == 5:
        print("Patient n°", a)
        self.master.withdraw()
        subprocess.run('./patient_agenda/origin_agenda5.py', check=True)
        self.master.deiconify()
    elif a == 6:
        print("Patient n°", a)
        self.master.withdraw()
        subprocess.run('./patient_agenda/origin_agenda6.py', check=True)
        self.master.deiconify()
    elif a == 7:
        print("Patient n°", a)
        self.master.withdraw()
        subprocess.run('./patient_agenda/origin_agenda7.py', check=True)
        self.master.deiconify()
    elif a == 8:
        print("Patient n°", a)
        self.master.withdraw()
        subprocess.run('./patient_agenda/origin_agenda8.py', check=True)
        self.master.deiconify()
    elif a == 9:
        print("Patient n°", a)
        self.master.withdraw()
        subprocess.run('./patient_agenda/origin_agenda9.py', check=True)
        self.master.deiconify()
    elif a == 10:
        print("Patient n°", a)
        self.master.withdraw()
        subprocess.run('./patient_agenda/origin_agenda10.py', check=True)
        self.master.deiconify()
    elif a == 11:
        print("Patient n°", a)
        self.master.withdraw()
        subprocess.run('./patient_agenda/origin_agenda11.py', check=True)
        self.master.deiconify()
    elif a == 12:
        print("Patient n°", a)
        self.master.withdraw()
        subprocess.run('./patient_agenda/origin_agenda12.py', check=True)
        self.master.deiconify()
    elif a == 13:
        print("Patient n°", a)
        self.master.withdraw()
        subprocess.run('./patient_agenda/origin_agenda13.py', check=True)
        self.master.deiconify()
    elif a == 14:
        print("Patient n°", a)
        self.master.withdraw()
        subprocess.run('./patient_agenda/origin_agenda14.py', check=True)
        self.master.deiconify()
    elif a == 15:
        print("Patient n°", a)
        self.master.withdraw()
        subprocess.run('./patient_agenda/origin_agenda15.py', check=True)
        self.master.deiconify()
    elif a == 16:
        print("Patient n°", a)
        self.master.withdraw()
        subprocess.run('./patient_agenda/origin_agenda16.py', check=True)
        self.master.deiconify()
    elif a == 17:
        print("Patient n°", a)
        self.master.withdraw()
        subprocess.run('./patient_agenda/origin_agenda17.py', check=True)
        self.master.deiconify()
    elif a == 18:
        print("Patient n°", a)
        self.master.withdraw()
        subprocess.run('./patient_agenda/origin_agenda18.py', check=True)
        self.master.deiconify()
    elif a == 18:
        print("Patient n°", a)
        self.master.withdraw()
        subprocess.run('./patient_agenda/origin_agenda18.py', check=True)
        self.master.deiconify()
    elif a == 19:
        print("Patient n°", a)
        self.master.withdraw()
        subprocess.run('./patient_agenda/origin_agenda19.py', check=True)
        self.master.deiconify()
    elif a == 20:
        print("Patient n°", a)
        self.master.withdraw()
        subprocess.run('./patient_agenda/origin_agenda20.py', check=True)
        self.master.deiconify()
    elif a == 21:
        print("Patient n°", a)
        self.master.withdraw()
        subprocess.run('./patient_agenda/origin_agenda21.py', check=True)
        self.master.deiconify()
    elif a == 22:
        print("Patient n°", a)
        self.master.withdraw()
        subprocess.run('./patient_agenda/origin_agenda22.py', check=True)
        self.master.deiconify()
    elif a == 23:
        print("Patient n°", a)
        self.master.withdraw()
        subprocess.run('./patient_agenda/origin_agenda23.py', check=True)
        self.master.deiconify()
    elif a == 24:
        print("Patient n°", a)
        self.master.withdraw()
        subprocess.run('./patient_agenda/origin_agenda24.py', check=True)
        self.master.deiconify()
    else:
        print("Nothing happened")
        tk.messagebox.showerror("Error",
            "Something wrong with subprocess...(agenda extensions)")
