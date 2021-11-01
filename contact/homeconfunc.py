#!/usr/bin/python3
# -*- coding: utf-8 -*-


import tkinter as tk
from tkinter import messagebox

from contact.conpact.hcs_contact1 import homecsWind
from contact.conpact2.hcs_contact2 import homecsWind2
from contact.conpact3.hcs_contact3 import homecsWind3
from contact.conpact4.hcs_contact4 import homecsWind4
from contact.conpact5.hcs_contact5 import homecsWind5
from contact.conpact6.hcs_contact6 import homecsWind6
from contact.conpact7.hcs_contact7 import homecsWind7
from contact.conpact8.hcs_contact8 import homecsWind8
from contact.conpact9.hcs_contact9 import homecsWind9
from contact.conpact10.hcs_contact10 import homecsWind10
from contact.conpact11.hcs_contact11 import homecsWind11
from contact.conpact12.hcs_contact12 import homecsWind12
from contact.conpact13.hcs_contact13 import homecsWind13
from contact.conpact14.hcs_contact14 import homecsWind14
from contact.conpact15.hcs_contact15 import homecsWind15
from contact.conpact16.hcs_contact16 import homecsWind16
from contact.conpact17.hcs_contact17 import homecsWind17
from contact.conpact18.hcs_contact18 import homecsWind18
from contact.conpact19.hcs_contact19 import homecsWind19
from contact.conpact20.hcs_contact20 import homecsWind20
from contact.conpact21.hcs_contact21 import homecsWind21
from contact.conpact22.hcs_contact22 import homecsWind22
from contact.conpact23.hcs_contact23 import homecsWind23
from contact.conpact24.hcs_contact24 import homecsWind24



def callHomecsWind(self, l):
    """
        For calling functions from conpact
    """
    if l == 1:
        homecsWind(self)
    elif l == 2:
        homecsWind2(self)
    elif l == 3:
        homecsWind3(self)
    elif l == 4:
        homecsWind4(self)
    elif l == 5:
        homecsWind5(self)
    elif l == 6:
        homecsWind6(self)
    elif l == 7:
        homecsWind7(self)
    elif l == 8:
        homecsWind8(self)
    elif l == 9:
        homecsWind9(self)
    elif l == 10:
        homecsWind10(self)
    elif l == 11:
        homecsWind11(self)
    elif l == 12:
        homecsWind12(self)
    elif l == 13:
        homecsWind13(self)
    elif l == 14:
        homecsWind14(self)
    elif l == 15:
        homecsWind15(self)
    elif l == 16:
        homecsWind16(self)
    elif l == 17:
        homecsWind17(self)
    elif l == 18:
        homecsWind18(self)
    elif l == 19:
        homecsWind19(self)
    elif l == 20:
        homecsWind20(self)
    elif l == 21:
        homecsWind21(self)
    elif l == 22:
        homecsWind22(self)
    elif l == 23:
        homecsWind23(self)
    elif l == 24:
        homecsWind24(self)
    else:
        print("There aren't links for binding functions (contact)")
        tk.messagebox.showerror("Error",
            "There is not links for binding functions (contact)")
