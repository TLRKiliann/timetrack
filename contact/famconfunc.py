#!/usr/bin/python3
# -*- coding: utf-8 -*-


import tkinter as tk
from tkinter import messagebox

from contact.conpact.family_contact1 import famWind
from contact.conpact2.family_contact2 import famWind2
from contact.conpact3.family_contact3 import famWind3
from contact.conpact4.family_contact4 import famWind4
from contact.conpact5.family_contact5 import famWind5
from contact.conpact6.family_contact6 import famWind6
from contact.conpact7.family_contact7 import famWind7
from contact.conpact8.family_contact8 import famWind8
from contact.conpact9.family_contact9 import famWind9
from contact.conpact10.family_contact10 import famWind10
from contact.conpact11.family_contact11 import famWind11
from contact.conpact12.family_contact12 import famWind12
from contact.conpact13.family_contact13 import famWind13
from contact.conpact14.family_contact14 import famWind14
from contact.conpact15.family_contact15 import famWind15
from contact.conpact16.family_contact16 import famWind16
from contact.conpact17.family_contact17 import famWind17
from contact.conpact18.family_contact18 import famWind18
from contact.conpact19.family_contact19 import famWind19
from contact.conpact20.family_contact20 import famWind20
from contact.conpact21.family_contact21 import famWind21
from contact.conpact22.family_contact22 import famWind22
from contact.conpact23.family_contact23 import famWind23
from contact.conpact24.family_contact24 import famWind24


def callFamWind(self, j):
    """
        For calling functions from conpact
    """
    if j == 1:
        famWind(self)
    elif j == 2:
        famWind2(self)
    elif j == 3:
        famWind3(self)
    elif j == 4:
        famWind4(self)
    elif j == 5:
        famWind5(self)
    elif j == 6:
        famWind6(self)
    elif j == 7:
        famWind7(self)
    elif j == 8:
        famWind8(self)
    elif j == 9:
        famWind9(self)
    elif j == 10:
        famWind10(self)
    elif j == 11:
        famWind11(self)
    elif j == 12:
        famWind12(self)
    elif j == 13:
        famWind13(self)
    elif j == 14:
        famWind14(self)
    elif j == 15:
        famWind15(self)
    elif j == 16:
        famWind16(self)
    elif j == 17:
        famWind17(self)
    elif j == 18:
        famWind18(self)
    elif j == 19:
        famWind19(self)
    elif j == 20:
        famWind20(self)
    elif j == 21:
        famWind21(self)
    elif j == 22:
        famWind22(self)
    elif j == 23:
        famWind23(self)
    elif j == 24:
        famWind24(self)
    else:
        print("There aren't links for binding functions (contact)")
        tk.messagebox.showerror("Error",
            "There is not links for binding functions (contact)")
