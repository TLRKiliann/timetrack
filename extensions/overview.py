#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
    Intermediate file of functions
    to call scripts from ./backup/
"""


import tkinter as tk
from tkinter import messagebox
import subprocess
from backapp import *

def overviewExtend(self, f):
    """
        To acces files into Backup folder.
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        backupFuncPatientX()
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()
    """
    if f == 1:
        #self.master.withdraw()
        backupFuncPatient(self)
        #self.master.deiconify()
    elif f == 2:
        #self.master.withdraw()
        backupFuncPatient2(self)
        #self.master.deiconify()
    elif f == 3:
        #self.master.withdraw()
        backupFuncPatient3(self)
        #self.master.deiconify()
    elif f == 4:
        #self.master.withdraw()
        backupFuncPatient4(self)
        #self.master.deiconify()
    elif f == 5:
        #self.master.withdraw()
        backupFuncPatient5(self)
        #self.master.deiconify()
    elif f == 6:
        #self.master.withdraw()
        backupFuncPatient6(self)
        #self.master.deiconify()
    elif f == 7:
        #self.master.withdraw()
        backupFuncPatient7(self)
        #self.master.deiconify()
    elif f == 8:
        #self.master.withdraw()
        backupFuncPatient8(self)
        #self.master.deiconify()
    elif f == 9:
        #self.master.withdraw()
        backupFuncPatient9(self)
        #self.master.deiconify()
    elif f == 10:
        #self.master.withdraw()
        backupFuncPatient10(self)
        #self.master.deiconify()
    elif f == 11:
        #self.master.withdraw()
        backupFuncPatient11(self)
        #self.master.deiconify()
    elif f == 12:
        #self.master.withdraw()
        backupFuncPatient12(self)
        #self.master.deiconify()
    elif f == 13:
        #self.master.withdraw()
        backupFuncPatient13(self)
        #self.master.deiconify()
    elif f == 14:
        #self.master.withdraw()
        backupFuncPatient14(self)
        #self.master.deiconify()
    elif f == 15:
        #self.master.withdraw()
        backupFuncPatient15(self)
        #self.master.deiconify()
    elif f == 16:
        #self.master.withdraw()
        backupFuncPatient16(self)
        #self.master.deiconify()
    elif f == 17:
        #self.master.withdraw()
        backupFuncPatient17(self)
        #self.master.deiconify()
    elif f == 18:
        #self.master.withdraw()
        backupFuncPatient18(self)
        #self.master.deiconify()
    elif f == 19:
        #self.master.withdraw()
        backupFuncPatient19(self)
        #self.master.deiconify()
    elif f == 20:
        #self.master.withdraw()
        backupFuncPatient20(self)
        #self.master.deiconify()
    elif f == 21:
        #self.master.withdraw()
        backupFuncPatient21(self)
        #self.master.deiconify()
    elif f == 22:
        #self.master.withdraw()
        backupFuncPatient22(self)
        #self.master.deiconify()
    elif f == 23:
        #self.master.withdraw()
        backupFuncPatient23(self)
        #self.master.deiconify()
    elif f == 24:
        #self.master.withdraw()
        backupFuncPatient24(self)
        #self.master.deiconify()
    else:
        print("[!] Error - maybe no backup maide !")
        tk.messagebox.showerror("Error",
            "Something wrong with subprocess...(backup extensions)")
