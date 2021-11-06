#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
    Intermediate file of functions
    to call scripts from ./calBmi/
"""


import tkinter as tk
from tkinter import messagebox
import subprocess


def bmicalkilo(self, u):
    """
        - Decreases opacity of background window
        during script CalculBmiX.py is running.
        - Function for calling BMI's subprocess.
        - To custom in another style :
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        subprocess.run('...', shell=False)
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()
    """
    if u == 1:
        print("Patient n°", u)
        subprocess.Popen("./calBmi/calculbmi.py", shell=False)
    elif u == 2:
        print("Patient n°", u)
        subprocess.Popen("./calBmi/calculbmi2.py", shell=False)
    elif u == 3:
        print("Patient n°", u)
        subprocess.Popen("./calBmi/calculbmi3.py", shell=False)
    elif u == 4:
        print("Patient n°", u)
        subprocess.Popen("./calBmi/calculbmi4.py", shell=False)
    elif u == 5:
        print("Patient n°", u)
        subprocess.Popen("./calBmi/calculbmi5.py", shell=False)
    elif u == 6:
        print("Patient n°", u)
        subprocess.Popen("./calBmi/calculbmi6.py", shell=False)
    elif u == 7:
        print("Patient n°", u)
        subprocess.Popen("./calBmi/calculbmi7.py", shell=False)
    elif u == 8:
        print("Patient n°", u)
        subprocess.Popen("./calBmi/calculbmi8.py", shell=False)
    elif u == 9:
        print("Patient n°", u)
        subprocess.Popen("./calBmi/calculbmi9.py", shell=False)
    elif u == 10:
        print("Patient n°", u)
        subprocess.Popen("./calBmi/calculbmi10.py", shell=False)
    elif u == 11:
        print("Patient n°", u)
        subprocess.Popen("./calBmi/calculbmi11.py", shell=False)
    elif u == 12:
        print("Patient n°", u)
        subprocess.Popen("./calBmi/calculbmi12.py", shell=False)
    elif u == 13:
        print("Patient n°", u)
        subprocess.Popen("./calBmi/calculbmi13.py", shell=False)
    elif u == 14:
        print("Patient n°", u)
        subprocess.Popen("./calBmi/calculbmi14.py", shell=False)
    elif u == 15:
        print("Patient n°", u)
        subprocess.Popen("./calBmi/calculbmi15.py", shell=False)
    elif u == 16:
        print("Patient n°", u)
        subprocess.Popen("./calBmi/calculbmi16.py", shell=False)
    elif u == 17:
        print("Patient n°", u)
        subprocess.Popen("./calBmi/calculbmi17.py", shell=False)
    elif u == 18:
        print("Patient n°", u)
        subprocess.Popen("./calBmi/calculbmi18.py", shell=False)
    elif u == 19:
        print("Patient n°", u)
        subprocess.Popen("./calBmi/calculbmi19.py", shell=False)
    elif u == 20:
        print("Patient n°", u)
        subprocess.Popen("./calBmi/calculbmi20.py", shell=False)
    elif u == 21:
        print("Patient n°", u)
        subprocess.Popen("./calBmi/calculbmi21.py", shell=False)
    elif u == 22:
        print("Patient n°", u)
        subprocess.Popen("./calBmi/calculbmi22.py", shell=False)
    elif u == 23:
        print("Patient n°", u)
        subprocess.Popen("./calBmi/calculbmi23.py", shell=False)
    elif u == 24:
        print("Patient n°", u)
        subprocess.Popen("./calBmi/calculbmi24.py", shell=False)
    else:
        print("[!] Error, to call ./calBmi/calculbmiX.py with subprocess.")
        tk.messagebox.showerror("Error",
            "Something wrong with subprocess...(bmi extensions)")
