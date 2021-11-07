#!/usr/bin/python3
# -*- coding: utf-8 -*-


import tkinter as tk


def valFunc1(self):
    """
        Main function to define 
        design for contact interface.
    """
    self.effacer()
    self.delScroll()
    self.photo = tk.PhotoImage(file='./syno_gif/tt_fontcolor.png')
    self.itemfirst = self.can.create_image((0,0), image=self.photo,
        anchor=tk.NW)

    # Label title
    self.x1, self.y1 = 625, 50
    self.lbltitle = tk.Label(self.can, text="Validation",
        font=('MS Serif', 30, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wlbltitle_window = self.can.create_window(self.x1, self.y1,
        window = self.lbltitle)

    # Name lbl
    self.x2, self.y2 = 120, 120
    self.lblname = tk.Label(self.can, text="Patient Name :",
        font=('MS Serif', 14, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wlblname_window = self.can.create_window(self.x2, self.y2,
        window = self.lblname)

    # Patient 1
    try:
        with open('./newpatient/entryfile.txt', 'r') as namefile:
            line1 = namefile.readline()
    except FileNotFoundError as callfile:
        print("[!] File entryfile.txt doesn't exist !", callfile)

    try:
        self.data_time = line1
        self.x3, self.y3 = 300, 120
        self.new_data1 = tk.StringVar()
        self.entread = tk.Entry(self.can,
            textvariable=self.new_data1,
            highlightbackground='grey', bd=2)
        if line1 == '-':
            line1 = line1
        else:
            line1 = line1[:-1]
        self.new_data1.set(line1)
        self.fentread_window = self.can.create_window(self.x3,
            self.y3, window=self.entread)
    except UnboundLocalError as ub_error1:
        print("[!] File 1 not created !", ub_error1)

    # Care lbl
    self.x4, self.y4 = 500, 120
    self.lblcare = tk.Label(self.can, text="Care to validate :",
        font=('MS Serif', 14, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wlblcare_window = self.can.create_window(self.x4, self.y4,
        window = self.lblcare)



    self.can.configure(scrollregion=self.can.bbox(tk.ALL))
    self.can.unbind_all("<Button-4>")
    self.can.unbind_all("<Button-5>")
