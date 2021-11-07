#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
    Intermediate file of functions
    to call scripts from ./nutrition/
"""


import tkinter as tk
from tkinter import messagebox
import subprocess


def nutritionExtend(self, n):
    """
        Function for calling nutrition subprocess.
    """
    if n == 1:
        self.master.withdraw()
        subprocess.run('./nutrition/nutrit_patient1.py', check=True)
        self.master.deiconify()
    elif n == 2:
        self.master.withdraw()
        subprocess.run('./nutrition/nutrit_patient2.py', check=True)
        self.master.deiconify()
    elif n == 3:
        self.master.withdraw()
        subprocess.run('./nutrition/nutrit_patient3.py', check=True)
        self.master.deiconify()
    elif n == 4:
        self.master.withdraw()
        subprocess.run('./nutrition/nutrit_patient4.py', check=True)
        self.master.deiconify()
    elif n == 5:
        self.master.withdraw()
        subprocess.run('./nutrition/nutrit_patient5.py', check=True)
        self.master.deiconify()
    elif n == 6:
        self.master.withdraw()
        subprocess.run('./nutrition/nutrit_patient6.py', check=True)
        self.master.deiconify()
    elif n == 7:
        self.master.withdraw()
        subprocess.run('./nutrition/nutrit_patient7.py', check=True)
        self.master.deiconify()
    elif n == 8:
        self.master.withdraw()
        subprocess.run('./nutrition/nutrit_patient8.py', check=True)
        self.master.deiconify()
    elif n == 9:
        self.master.withdraw()
        subprocess.run('./nutrition/nutrit_patient9.py', check=True)
        self.master.deiconify()
    elif n == 10:
        self.master.withdraw()
        subprocess.run('./nutrition/nutrit_patient10.py', check=True)
        self.master.deiconify()
    elif n == 11:
        self.master.withdraw()
        subprocess.run('./nutrition/nutrit_patient11.py', check=True)
        self.master.deiconify()
    elif n == 12:
        self.master.withdraw()
        subprocess.run('./nutrition/nutrit_patient12.py', check=True)
        self.master.deiconify()
    elif n == 13:
        self.master.withdraw()
        subprocess.run('./nutrition/nutrit_patient13.py', check=True)
        self.master.deiconify()
    elif n == 14:
        self.master.withdraw()
        subprocess.run('./nutrition/nutrit_patient14.py', check=True)
        self.master.deiconify()
    elif n == 15:
        self.master.withdraw()
        subprocess.run('./nutrition/nutrit_patient15.py', check=True)
        self.master.deiconify()
    elif n == 16:
        self.master.withdraw()
        subprocess.run('./nutrition/nutrit_patient16.py', check=True)
        self.master.deiconify()
    elif n == 17:
        self.master.withdraw()
        subprocess.run('./nutrition/nutrit_patient17.py', check=True)
        self.master.deiconify()
    elif n == 18:
        self.master.withdraw()
        subprocess.run('./nutrition/nutrit_patient18.py', check=True)
        self.master.deiconify()
    elif n == 19:
        self.master.withdraw()
        subprocess.run('./nutrition/nutrit_patient19.py', check=True)
        self.master.deiconify()
    elif n == 20:
        self.master.withdraw()
        subprocess.run('./nutrition/nutrit_patient20.py', check=True)
        self.master.deiconify()
    elif n == 21:
        self.master.withdraw()
        subprocess.run('./nutrition/nutrit_patient21.py', check=True)
        self.master.deiconify()
    elif n == 22:
        self.master.withdraw()
        subprocess.run('./nutrition/nutrit_patient22.py', check=True)
        self.master.deiconify()
    elif n == 23:
        self.master.withdraw()
        subprocess.run('./nutrition/nutrit_patient23.py', check=True)
        self.master.deiconify()
    elif n == 24:
        self.master.withdraw()
        subprocess.run('./nutrition/nutrit_patient24.py', check=True)
        self.master.deiconify()
    else:
        print("[!] Error to call ./nutrition/nutrit_patientX.py with subprocess.")
        tk.messagebox.showerror("Error",
            "Something wrong with subprocess...(nutrition extensions)")
