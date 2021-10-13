#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
    call updatepatientX.py script from patcaps.py
"""

import tkinter as tk
import subprocess


def updateLink(self, g):
    """
        !!! Security : I'm not sure if that's good to let :
        shell=True
        because it could be a vulnerability !!!
        To update data for patient in txt entryfile and for DB.
    """
    if g == 1:
        subprocess.Popen('./update/updatepatient1.py', shell=True)
    elif g == 2:
        subprocess.Popen('./update/updatepatient2.py', shell=True)
    elif g == 3:
        subprocess.Popen('./update/updatepatient3.py', shell=True)
    elif g == 4:
        subprocess.Popen('./update/updatepatient4.py', shell=True)
    elif g == 5:
        subprocess.Popen('./update/updatepatient5.py', shell=True)
    elif g == 6:
        subprocess.Popen('./update/updatepatient6.py', shell=True)
    elif g == 7:
        subprocess.Popen('./update/updatepatient7.py', shell=True)
    elif g == 8:
        subprocess.Popen('./update/updatepatient8.py', shell=True)
    elif g == 9:
        subprocess.Popen('./update/updatepatient9.py', shell=True)
    elif g == 10:
        subprocess.Popen('./update/updatepatient10.py', shell=True)
    elif g == 11:
        subprocess.Popen('./update/updatepatient11.py', shell=True)
    elif g == 12:
        subprocess.Popen('./update/updatepatient12.py', shell=True)
    elif g == 13:
        subprocess.Popen('./update/updatepatient13.py', shell=True)
    elif g == 14:
        subprocess.Popen('./update/updatepatient14.py', shell=True)
    elif g == 15:
        subprocess.Popen('./update/updatepatient15.py', shell=True)
    elif g == 16:
        subprocess.Popen('./update/updatepatient16.py', shell=True)
    elif g == 17:
        subprocess.Popen('./update/updatepatient17.py', shell=True)
    elif g == 18:
        subprocess.Popen('./update/updatepatient18.py', shell=True)
    elif g == 19:
        subprocess.Popen('./update/updatepatient19.py', shell=True)
    elif g == 20:
        subprocess.Popen('./update/updatepatient20.py', shell=True)
    elif g == 21:
        subprocess.Popen('./update/updatepatient21.py', shell=True)
    elif g == 22:
        subprocess.Popen('./update/updatepatient22.py', shell=True)
    elif g == 23:
        subprocess.Popen('./update/updatepatient23.py', shell=True)
    elif g == 24:
        subprocess.Popen('./update/updatepatient24.py', shell=True)
    else:
        print("Error, with call_update.py script !")
