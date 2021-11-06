#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
    Intermediate file of functions
    to call scripts from ./need/checkbX.py
"""


import tkinter as tk
from tkinter import messagebox
import subprocess


def checkcaseExtend(self, b):
    """
        New window is open with subprocess.Popen()
        for checking 14 needs check options.
    """
    if b == 1:
        print("Patient n°", b)
        subprocess.Popen('./need/checkb.py', shell=False)
    elif b == 2:
        print("Patient n°", b)
        subprocess.Popen('./need/checkb2.py', shell=False)
    elif b == 3:
        print("Patient n°", b)
        subprocess.Popen('./need/checkb3.py', shell=False)
    elif b == 4:
        print("Patient n°", b)
        subprocess.Popen('./need/checkb4.py', shell=False)
    elif b == 5:
        print("Patient n°", b)
        subprocess.Popen('./need/checkb5.py', shell=False)
    elif b == 6:
        print("Patient n°", b)
        subprocess.Popen('./need/checkb6.py', shell=False)
    elif b == 7:
        print("Patient n°", b)
        subprocess.Popen('./need/checkb7.py', shell=False)
    elif b == 8:
        print("Patient n°", b)
        subprocess.Popen('./need/checkb8.py', shell=False)
    elif b == 9:
        print("Patient n°", b)
        subprocess.Popen('./need/checkb9.py', shell=False)
    elif b == 10:
        print("Patient n°", b)
        subprocess.Popen('./need/checkb10.py', shell=False)
    elif b == 11:
        print("Patient n°", b)
        subprocess.Popen('./need/checkb11.py', shell=False)
    elif b == 12:
        print("Patient n°", b)
        subprocess.Popen('./need/checkb12.py', shell=False)
    elif b == 13:
        print("Patient n°", b)
        subprocess.Popen('./need/checkb13.py', shell=False)
    elif b == 14:
        print("Patient n°", b)
        subprocess.Popen('./need/checkb14.py', shell=False)
    elif b == 15:
        print("Patient n°", b)
        subprocess.Popen('./need/checkb15.py', shell=False)
    elif b == 16:
        print("Patient n°", b)
        subprocess.Popen('./need/checkb16.py', shell=False)
    elif b == 17:
        print("Patient n°", b)
        subprocess.Popen('./need/checkb17.py', shell=False)
    elif b == 18:
        print("Patient n°", b)
        subprocess.Popen('./need/checkb18.py', shell=False)
    elif b == 19:
        print("Patient n°", b)
        subprocess.Popen('./need/checkb19.py', shell=False)
    elif b == 20:
        print("Patient n°", b)
        subprocess.Popen('./need/checkb20.py', shell=False)
    elif b == 21:
        print("Patient n°", b)
        subprocess.Popen('./need/checkb21.py', shell=False)
    elif b == 22:
        print("Patient n°", b)
        subprocess.Popen('./need/checkb22.py', shell=False)
    elif b == 23:
        print("Patient n°", b)
        subprocess.Popen('./need/checkb23.py', shell=False)
    elif b == 24:
        print("Patient n°", b)
        subprocess.Popen('./need/checkb24.py', shell=False)
    else:
        print("[!] Error, No checkbox has been found !")
        tk.messagebox.showerror("Error",
            "Something wrong with subprocess...(need/checkb extensions)")
