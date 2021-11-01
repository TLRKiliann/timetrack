#!/usr/bin/python3
# -*- coding: utf-8 -*-


import tkinter as tk
from tkinter import messagebox

from contact.conpact.doc_contact1 import doctorWind
from contact.conpact2.doc_contact2 import doctorWind2
from contact.conpact3.doc_contact3 import doctorWind3
from contact.conpact4.doc_contact4 import doctorWind4
from contact.conpact5.doc_contact5 import doctorWind5
from contact.conpact6.doc_contact6 import doctorWind6
from contact.conpact7.doc_contact7 import doctorWind7
from contact.conpact8.doc_contact8 import doctorWind8
from contact.conpact9.doc_contact9 import doctorWind9
from contact.conpact10.doc_contact10 import doctorWind10
from contact.conpact11.doc_contact11 import doctorWind11
from contact.conpact12.doc_contact12 import doctorWind12
from contact.conpact13.doc_contact13 import doctorWind13
from contact.conpact14.doc_contact14 import doctorWind14
from contact.conpact15.doc_contact15 import doctorWind15
from contact.conpact16.doc_contact16 import doctorWind16
from contact.conpact17.doc_contact17 import doctorWind17
from contact.conpact18.doc_contact18 import doctorWind18
from contact.conpact19.doc_contact19 import doctorWind19
from contact.conpact20.doc_contact20 import doctorWind20
from contact.conpact21.doc_contact21 import doctorWind21
from contact.conpact22.doc_contact22 import doctorWind22
from contact.conpact23.doc_contact23 import doctorWind23
from contact.conpact24.doc_contact24 import doctorWind24


def callDoctorWind(self, k):
    """
        For calling functions from conpact
    """
    if k == 1:
        doctorWind(self)
    elif k == 2:
        doctorWind2(self)
    elif k == 3:
        doctorWind3(self)
    elif k == 4:
        doctorWind4(self)
    elif k == 5:
        doctorWind5(self)
    elif k == 6:
        doctorWind6(self)
    elif k == 7:
        doctorWind7(self)
    elif k == 8:
        doctorWind8(self)
    elif k == 9:
        doctorWind9(self)
    elif k == 10:
        doctorWind10(self)
    elif k == 11:
        doctorWind11(self)
    elif k == 12:
        doctorWind12(self)
    elif k == 13:
        doctorWind13(self)
    elif k == 14:
        doctorWind14(self)
    elif k == 15:
        doctorWind15(self)
    elif k == 16:
        doctorWind16(self)
    elif k == 17:
        doctorWind17(self)
    elif k == 18:
        doctorWind18(self)
    elif k == 19:
        doctorWind19(self)
    elif k == 20:
        doctorWind20(self)
    elif k == 21:
        doctorWind21(self)
    elif k == 22:
        doctorWind22(self)
    elif k == 23:
        doctorWind23(self)
    elif k == 24:
        doctorWind24(self)
    else:
        print("There aren't links for binding functions (contact)")
        tk.messagebox.showerror("Error",
            "There is not links for binding functions (contact)")
