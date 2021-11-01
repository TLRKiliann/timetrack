#!/usr/bin/python3
# -*- coding: utf-8 -*-


import tkinter as tk
from tkinter import messagebox

from contact.conpact.pat_contact1 import Window
from contact.conpact2.pat_contact2 import Window2
from contact.conpact3.pat_contact3 import Window3
from contact.conpact4.pat_contact4 import Window4
from contact.conpact5.pat_contact5 import Window5
from contact.conpact6.pat_contact6 import Window6
from contact.conpact7.pat_contact7 import Window7
from contact.conpact8.pat_contact8 import Window8
from contact.conpact9.pat_contact9 import Window9
from contact.conpact10.pat_contact10 import Window10
from contact.conpact11.pat_contact11 import Window11
from contact.conpact12.pat_contact12 import Window12
from contact.conpact13.pat_contact13 import Window13
from contact.conpact14.pat_contact14 import Window14
from contact.conpact15.pat_contact15 import Window15
from contact.conpact16.pat_contact16 import Window16
from contact.conpact17.pat_contact17 import Window17
from contact.conpact18.pat_contact18 import Window18
from contact.conpact19.pat_contact19 import Window19
from contact.conpact20.pat_contact20 import Window20
from contact.conpact21.pat_contact21 import Window21
from contact.conpact22.pat_contact22 import Window22
from contact.conpact23.pat_contact23 import Window23
from contact.conpact24.pat_contact24 import Window24


def callPatNum(self, h):
    """
        For calling functions from conpact
    """
    if h == 1:
        Window(self)
    elif h == 2:
        Window2(self)
    elif h == 3:
        Window3(self)
    elif h == 4:
        Window4(self)
    elif h == 5:
        Window5(self)
    elif h == 6:
        Window6(self)
    elif h == 7:
        Window7(self)
    elif h == 8:
        Window8(self)
    elif h == 9:
        Window9(self)
    elif h == 10:
        Window10(self)
    elif h == 11:
        Window11(self)
    elif h == 12:
        Window12(self)
    elif h == 13:
        Window13(self)
    elif h == 14:
        Window14(self)
    elif h == 15:
        Window15(self)
    elif h == 16:
        Window16(self)
    elif h == 17:
        Window17(self)
    elif h == 18:
        Window18(self)
    elif h == 19:
        Window19(self)
    elif h == 20:
        Window20(self)
    elif h == 21:
        Window21(self)
    elif h == 22:
        Window22(self)
    elif h == 23:
        Window23(self)
    elif h == 24:
        Window24(self)
    else:
        print("There aren't links for binding functions (contact)")
        tk.messagebox.showerror("Error",
            "There is not links for binding functions (contact)")
