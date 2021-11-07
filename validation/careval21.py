#!/usr/bin/python3
# -*- coding: utf-8 -*-


import tkinter as tk


def valFunc21(self):
    """
        Main function to define 
        design for contact interface.
    """
    self.effacer()
    self.delScroll()
    self.photo = tk.PhotoImage(file='./syno_gif/tt_fontcolor.png')
    self.itemfirst = self.can.create_image((0,0), image=self.photo,
        anchor=tk.NW)

    self.can.configure(scrollregion=self.can.bbox(tk.ALL))
    self.can.unbind_all("<Button-4>")
    self.can.unbind_all("<Button-5>")
