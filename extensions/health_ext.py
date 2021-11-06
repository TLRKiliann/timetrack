#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
    Intermediate file of functions
    to call scripts from ./need/suiviX.py
"""


import tkinter as tk
from tkinter import messagebox
import subprocess
from need.needownload.refdlneed import *


def extendHealth(self, s):
    """
        New window is open with subprocess.Popen()
        for checking 14 needs check options.
    """
    if s == 1:
        print("Patient n°", s)
        needload1()
        self.master.withdraw()
        subprocess.run("./need/suivi_patient_1.py", check=True)
        self.master.deiconify()
    elif s == 2:
        print("Patient n°", s)
        needload2()
        self.master.withdraw()
        subprocess.run("./need/suivi_patient_2.py", check=True)
        self.master.deiconify()
    elif s == 3:
        print("Patient n°", s)
        needload3()
        self.master.withdraw()
        subprocess.run("./need/suivi_patient_3.py", check=True)
        self.master.deiconify()
    elif s == 4:
        print("Patient n°", s)
        needload4()
        self.master.withdraw()
        subprocess.run("./need/suivi_patient_4.py", check=True)
        self.master.deiconify()
    elif s == 5:
        print("Patient n°", s)
        needload5()
        self.master.withdraw()
        subprocess.run("./need/suivi_patient_5.py", check=True)
        self.master.deiconify()
    elif s == 6:
        print("Patient n°", s)
        needload6()
        self.master.withdraw()
        subprocess.run("./need/suivi_patient_6.py", check=True)
        self.master.deiconify()
    elif s == 7:
        print("Patient n°", s)
        needload7()
        self.master.withdraw()
        subprocess.run("./need/suivi_patient_7.py", check=True)
        self.master.deiconify()
    elif s == 8:
        print("Patient n°", s)
        needload8()
        self.master.withdraw()
        subprocess.run("./need/suivi_patient_8.py", check=True)
        self.master.deiconify()
    elif s == 9:
        print("Patient n°", s)
        needload9()
        self.master.withdraw()
        subprocess.run("./need/suivi_patient_9.py", check=True)
        self.master.deiconify()
    elif s == 10:
        print("Patient n°", s)
        needload10()
        self.master.withdraw()
        subprocess.run("./need/suivi_patient_10.py", check=True)
        self.master.deiconify()
    elif s == 11:
        print("Patient n°", s)
        needload11()
        self.master.withdraw()
        subprocess.run("./need/suivi_patient_11.py", check=True)
        self.master.deiconify()
    elif s == 12:
        print("Patient n°", s)
        needload12()
        self.master.withdraw()
        subprocess.run("./need/suivi_patient_12.py", check=True)
        self.master.deiconify()
    elif s == 13:
        print("Patient n°", s)
        needload13()
        self.master.withdraw()
        subprocess.run("./need/suivi_patient_13.py", check=True)
        self.master.deiconify()
    elif s == 14:
        print("Patient n°", s)
        needload14()
        self.master.withdraw()
        subprocess.run("./need/suivi_patient_14.py", check=True)
        self.master.deiconify()
    elif s == 15:
        print("Patient n°", s)
        needload15()
        self.master.withdraw()
        subprocess.run("./need/suivi_patient_15.py", check=True)
        self.master.deiconify()
    elif s == 16:
        print("Patient n°", s)
        needload16()
        self.master.withdraw()
        subprocess.run("./need/suivi_patient_16.py", check=True)
        self.master.deiconify()
    elif s == 17:
        print("Patient n°", s)
        needload17()
        self.master.withdraw()
        subprocess.run("./need/suivi_patient_17.py", check=True)
        self.master.deiconify()
    elif s == 18:
        print("Patient n°", s)
        needload18()
        self.master.withdraw()
        subprocess.run("./need/suivi_patient_18.py", check=True)
        self.master.deiconify()
    elif s == 19:
        print("Patient n°", s)
        needload19()
        self.master.withdraw()
        subprocess.run("./need/suivi_patient_19.py", check=True)
        self.master.deiconify()
    elif s == 20:
        print("Patient n°", s)
        needload20()
        self.master.withdraw()
        subprocess.run("./need/suivi_patient_20.py", check=True)
        self.master.deiconify()
    elif s == 21:
        print("Patient n°", s)
        needload21()
        self.master.withdraw()
        subprocess.run("./need/suivi_patient_21.py", check=True)
        self.master.deiconify()
    elif s == 22:
        print("Patient n°", s)
        needload22()
        self.master.withdraw()
        subprocess.run("./need/suivi_patient_22.py", check=True)
        self.master.deiconify()
    elif s == 23:
        print("Patient n°", s)
        needload23()
        self.master.withdraw()
        subprocess.run("./need/suivi_patient_23.py", check=True)
        self.master.deiconify()
    elif s == 24:
        print("Patient n°", s)
        needload24()
        self.master.withdraw()
        subprocess.run("./need/suivi_patient_24.py", check=True)
        self.master.deiconify()
    else:
        print("[!] Error, to call ./need/suivi_patient_X.py with subprocess")
        tk.messagebox.showerror("Error",
            "Something wrong with subprocess...(need/suivi extensions)")
