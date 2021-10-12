#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
    call diag_patientX.py script from patcaps.py
"""


import tkinter as tk
from diag.diagdownload import *


def diagstic(self, d):
    """
        Hide background window and
        call script with subprocess.run()
    """
    if d == 1:
        diagloading1()
        self.master.withdraw()
        subprocess.run("./diag/diag_patient1.py", check=True)
        self.master.deiconify()
    elif d == 2:
        diagloading2()
        self.master.withdraw()
        subprocess.run("./diag/diag_patient2.py", check=True)
        self.master.deiconify()
    elif d == 3:
        diagloading3()
        self.master.withdraw()
        subprocess.run("./diag/diag_patient3.py", check=True)
        self.master.deiconify()
    elif d == 4:
        diagloading4()
        self.master.withdraw()
        subprocess.run("./diag/diag_patient4.py", check=True)
        self.master.deiconify()
    elif d == 5:
        diagloading5()
        self.master.withdraw()
        subprocess.run("./diag/diag_patient5.py", check=True)
        self.master.deiconify()
    elif d == 6:
        diagloading6()
        self.master.withdraw()
        subprocess.run("./diag/diag_patient6.py", check=True)
        self.master.deiconify()
    elif d == 7:
        diagloading7()
        self.master.withdraw()
        subprocess.run("./diag/diag_patient7.py", check=True)
        self.master.deiconify()
    elif d == 8:
        diagloading8()
        self.master.withdraw()
        subprocess.run("./diag/diag_patient8.py", check=True)
        self.master.deiconify()
    elif d == 9:
        diagloading9()
        self.master.withdraw()
        subprocess.run("./diag/diag_patient9.py", check=True)
        self.master.deiconify()
    elif d == 10:
        diagloading10()
        self.master.withdraw()
        subprocess.run("./diag/diag_patient10.py", check=True)
        self.master.deiconify()
    elif d == 11:
        diagloading11()
        self.master.withdraw()
        subprocess.run("./diag/diag_patient11.py", check=True)
        self.master.deiconify()
    elif d == 12:
        diagloading12()
        self.master.withdraw()
        subprocess.run("./diag/diag_patient12.py", check=True)
        self.master.deiconify()
    elif d == 13:
        diagloading13()
        self.master.withdraw()
        subprocess.run("./diag/diag_patient13.py", check=True)
        self.master.deiconify()
    elif d == 14:
        diagloading14()
        self.master.withdraw()
        subprocess.run("./diag/diag_patient14.py", check=True)
        self.master.deiconify()
    elif d == 15:
        diagloading15()
        self.master.withdraw()
        subprocess.run("./diag/diag_patient15.py", check=True)
        self.master.deiconify()
    elif d == 16:
        diagloading16()
        self.master.withdraw()
        subprocess.run("./diag/diag_patient16.py", check=True)
        self.master.deiconify()
    elif d == 17:
        diagloading17()
        self.master.withdraw()
        subprocess.run("./diag/diag_patient17.py", check=True)
        self.master.deiconify()
    elif d == 18:
        diagloading18()
        self.master.withdraw()
        subprocess.run("./diag/diag_patient18.py", check=True)
        self.master.deiconify()
    elif d == 19:
        diagloading19()
        self.master.withdraw()
        subprocess.run("./diag/diag_patient19.py", check=True)
        self.master.deiconify()
    elif d == 20:
        diagloading20()
        self.master.withdraw()
        subprocess.run("./diag/diag_patient20.py", check=True)
        self.master.deiconify()
    elif d == 21:
        diagloading21()
        self.master.withdraw()
        subprocess.run("./diag/diag_patient21.py", check=True)
        self.master.deiconify()
    elif d == 22:
        diagloading22()
        self.master.withdraw()
        subprocess.run("./diag/diag_patient22.py", check=True)
        self.master.deiconify()
    elif d == 23:
        diagloading23()
        self.master.withdraw()
        subprocess.run("./diag/diag_patient23.py", check=True)
        self.master.deiconify()
    elif d == 24:
        diagloading24()
        self.master.withdraw()
        subprocess.run("./diag/diag_patient24.py", check=True)
        self.master.deiconify()
    else:
        print("Error, with script named : call_diag.py")
