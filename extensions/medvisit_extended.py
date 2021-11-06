#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
    Intermediate file of functions
    to call scripts from ./param/
"""


import tkinter as tk
from tkinter import messagebox
import subprocess
from vmed.medload import *


def medicalVisit(self, t):
    """
        New window is open with subprocess.run()
        for checking 14 needs check options.
    """
    if t == 1:
        print("Patient n°", t)
        medownload1()
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient1.py", check=True)
        self.master.deiconify()
    elif t == 2:
        print("Patient n°", t)
        medownload2()
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient2.py", check=True)
        self.master.deiconify()
    elif t == 3:
        print("Patient n°", t)
        medownload3()
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient3.py", check=True)
        self.master.deiconify()
    elif t == 4:
        print("Patient n°", t)
        medownload4()
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient4.py", check=True)
        self.master.deiconify()
    elif t == 5:
        print("Patient n°", t)
        medownload5()
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient5.py", check=True)
        self.master.deiconify()
    elif t == 6:
        print("Patient n°", t)
        medownload6()
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient6.py", check=True)
        self.master.deiconify()
    elif t == 7:
        print("Patient n°", t)
        medownload7()
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient7.py", check=True)
        self.master.deiconify()
    elif t == 8:
        print("Patient n°", t)
        medownload8()
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient8.py", check=True)
        self.master.deiconify()
    elif t == 9:
        print("Patient n°", t)
        medownload9()
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient9.py", check=True)
        self.master.deiconify()
    elif t == 10:
        print("Patient n°", t)
        medownload10()
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient10.py", check=True)
        self.master.deiconify()
    elif t == 11:
        print("Patient n°", t)
        medownload11()
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient11.py", check=True)
        self.master.deiconify()
    elif t == 12:
        print("Patient n°", t)
        medownload12()
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient12.py", check=True)
        self.master.deiconify()
    elif t == 13:
        print("Patient n°", t)
        medownload13()
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient13.py", check=True)
        self.master.deiconify()
    elif t == 14:
        print("Patient n°", t)
        medownload14()
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient14.py", check=True)
        self.master.deiconify()
    elif t == 15:
        print("Patient n°", t)
        medownload15()
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient15.py", check=True)
        self.master.deiconify()
    elif t == 16:
        print("Patient n°", t)
        medownload16()
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient16.py", check=True)
        self.master.deiconify()
    elif t == 17:
        print("Patient n°", t)
        medownload17()
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient17.py", check=True)
        self.master.deiconify()
    elif t == 18:
        print("Patient n°", t)
        medownload18()
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient18.py", check=True)
        self.master.deiconify()
    elif t == 19:
        print("Patient n°", t)
        medownload19()
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient19.py", check=True)
        self.master.deiconify()
    elif t == 20:
        print("Patient n°", t)
        medownload20()
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient20.py", check=True)
        self.master.deiconify()
    elif t == 21:
        print("Patient n°", t)
        medownload21()
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient21.py", check=True)
        self.master.deiconify()
    elif t == 22:
        print("Patient n°", t)
        medownload22()
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient22.py", check=True)
        self.master.deiconify()
    elif t == 23:
        print("Patient n°", t)
        medownload23()
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient23.py", check=True)
        self.master.deiconify()
    elif t == 24:
        print("Patient n°", t)
        medownload24()
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient24.py", check=True)
        self.master.deiconify()
    else:
        print("Errro, to call ./vmed/ with subprocess")
        tk.messagebox.showerror("Error",
            "Something wrong with subprocess...(medicalVisit extensions)")
