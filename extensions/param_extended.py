#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
    Intermediate file of functions
    to call scripts from ./param/
"""


import tkinter as tk
from tkinter import messagebox
import subprocess


def parameters(self, p):
    """
        Function for calling param's subprocess.
        To decrease the opacity of the background window :
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        subprocess.run('...')
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()
    """
    if p == 1:
        print("Patient n°", p)
        subprocess.Popen("./param/fencap.py", shell=False)
    elif p == 2:
        print("Patient n°", p)
        subprocess.Popen("./param/fencap2.py", shell=False)
    elif p == 3:
        print("Patient n°", p)
        subprocess.Popen("./param/fencap3.py", shell=False)
    elif p == 4:
        print("Patient n°", p)
        subprocess.Popen("./param/fencap4.py", shell=False)
    elif p == 5:
        print("Patient n°", p)
        subprocess.Popen("./param/fencap5.py", shell=False)
    elif p == 6:
        print("Patient n°", p)
        subprocess.Popen("./param/fencap6.py", shell=False)
    elif p == 7:
        print("Patient n°", p)
        subprocess.Popen("./param/fencap7.py", shell=False)
    elif p == 8:
        print("Patient n°", p)
        subprocess.Popen("./param/fencap8.py", shell=False)
    elif p == 9:
        print("Patient n°", p)
        subprocess.Popen("./param/fencap9.py", shell=False)
    elif p == 10:
        print("Patient n°", p)
        subprocess.Popen("./param/fencap10.py", shell=False)
    elif p == 11:
        print("Patient n°", p)
        subprocess.Popen("./param/fencap11.py", shell=False)
    elif p == 12:
        print("Patient n°", p)
        subprocess.Popen("./param/fencap12.py", shell=False)
    elif p == 13:
        print("Patient n°", p)
        subprocess.Popen("./param/fencap13.py", shell=False)
    elif p == 14:
        print("Patient n°", p)
        subprocess.Popen("./param/fencap14.py", shell=False)
    elif p == 15:
        print("Patient n°", p)
        subprocess.Popen("./param/fencap15.py", shell=False)
    elif p == 16:
        print("Patient n°", p)
        subprocess.Popen("./param/fencap16.py", shell=False)
    elif p == 17:
        print("Patient n°", p)
        subprocess.Popen("./param/fencap17.py", shell=False)
    elif p == 18:
        print("Patient n°", p)
        subprocess.Popen("./param/fencap18.py", shell=False)
    elif p == 19:
        print("Patient n°", p)
        subprocess.Popen("./param/fencap19.py", shell=False)
    elif p == 20:
        print("Patient n°", p)
        subprocess.Popen("./param/fencap20.py", shell=False)
    elif p == 21:
        print("Patient n°", p)
        subprocess.Popen("./param/fencap21.py", shell=False)
    elif p == 22:
        print("Patient n°", p)
        subprocess.Popen("./param/fencap22.py", shell=False)
    elif p == 23:
        print("Patient n°", p)
        subprocess.Popen("./param/fencap23.py", shell=False)
    elif p == 24:
        print("Patient n°", p)
        subprocess.Popen("./param/fencap24.py", shell=False)
    else:
        print("[!] Error, to call ./param/fencapX.py with subprocess")
        tk.messagebox.showerror("Error",
            "Something wrong with subprocess...(parameters extensions)")
