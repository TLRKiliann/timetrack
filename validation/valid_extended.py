#!/usr/bin/python3
# -*- coding: utf-8 -*-


import tkinter as tk
from tkinter import messagebox

from validation.careval1 import valFunc1
from validation.careval2 import valFunc2
from validation.careval3 import valFunc3
from validation.careval4 import valFunc4
from validation.careval5 import valFunc5
from validation.careval6 import valFunc6
from validation.careval7 import valFunc7
from validation.careval8 import valFunc8
from validation.careval9 import valFunc9
from validation.careval10 import valFunc10
from validation.careval11 import valFunc11
from validation.careval12 import valFunc12
from validation.careval13 import valFunc13
from validation.careval14 import valFunc14
from validation.careval15 import valFunc15
from validation.careval16 import valFunc16
from validation.careval17 import valFunc17
from validation.careval18 import valFunc18
from validation.careval19 import valFunc19
from validation.careval20 import valFunc20
from validation.careval21 import valFunc21
from validation.careval22 import valFunc22
from validation.careval23 import valFunc23
from validation.careval24 import valFunc24


def callCareVal(self, v):
    """
        For calling functions from conpact
    """
    if v == 1:
        valFunc1(self)
    elif v == 2:
        valFunc2(self)
    elif v == 3:
        valFunc3(self)
    elif v == 4:
        valFunc4(self)
    elif v == 5:
        valFunc5(self)
    elif v == 6:
        valFunc6(self)
    elif v == 7:
        valFunc7(self)
    elif v == 8:
        valFunc8(self)
    elif v == 9:
        valFunc9(self)
    elif v == 10:
        valFunc10(self)
    elif v == 11:
        valFunc11(self)
    elif v == 12:
        valFunc12(self)
    elif v == 13:
        valFunc13(self)
    elif v == 14:
        valFunc14(self)
    elif v == 15:
        valFunc15(self)
    elif v == 16:
        valFunc16(self)
    elif v == 17:
        valFunc17(self)
    elif v == 18:
        valFunc18(self)
    elif v == 19:
        valFunc19(self)
    elif v == 20:
        valFunc20(self)
    elif v == 21:
        valFunc21(self)
    elif v == 22:
        valFunc22(self)
    elif v == 23:
        valFunc23(self)
    elif v == 24:
        valFunc24(self)
    else:
        print("There aren't links for binding functions (contact)")
        tk.messagebox.showerror("Error",
            "There is not links for binding functions (contact)")
