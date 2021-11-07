#!/usr/bin/python3
# -*- coding: utf-8 -*-


import tkinter as tk
from tkinter import ttk
import os
import time


def valFunc1(self):
    """
        Main function to define 
        design for contact interface.
    """
    self.effacer()
    self.delScroll()
    self.photo = tk.PhotoImage(file='./syno_gif/tt_fontcustom.png')
    self.itemfirst = self.can.create_image((0,0), image=self.photo,
        anchor=tk.NW)

    def regroupAll():
        """
            second textbox2
        """
        self.x11, self.y11 = 900, 480
        self.txtBox2 = tk.Text(self.can, height=12, width=60, font=18, relief=tk.SUNKEN)
        self.txtBox2.delete('1.0', tk.END)
        self.txtBox2.update()
        self.ftxtBox2_window = self.can.create_window(self.x11, self.y11, window=self.txtBox2)

        def importationTxtBox():
            """
                To import data from validate_1.txt
                and display in textbox2.
            """
            try:
                if os.path.getsize('./validation/valfiles1/validate_1.txt'):
                    print("[+] Ok, validate_1.txt exist")
            except FileNotFoundError as errfnf:
                print("[!] File validate_1.txt not found !", errfnf)
                with open('./validation/valfiles1/validate_1.txt', 'w') as testf:
                    print("[+] File validate_1.txt created !")

            try:
                if os.path.exists('./validation/valfiles1/validate_1.txt'):
                    with open('./validation/valfiles1/validate_1.txt', 'r') as val_f:
                        nametxt = val_f.read()
            except (FileNotFoundError, UnboundLocalError) as err_nfvali:
                print("[!] File validate_1.txt not found !", err_nfvali)

            self.txtBox2.insert(tk.INSERT, "--- Heal-Care ---\n")
            self.txtBox2.insert(tk.END, nametxt)

        importationTxtBox()

    regroupAll()

    # first textbox
    self.x10, self.y10 = 260, 460
    self.txtBox = tk.Text(self.can, height=10, width=40, font=18, relief=tk.SUNKEN)
    self.txtBox.delete('1.0', tk.END)
    self.txtBox.update()
    self.ftxtBox_window = self.can.create_window(self.x10, self.y10, window=self.txtBox)

    def stackvalidate(self):
        """
            To save data from left frame.
        """
        try:
            with open('./validation/valfiles1/validate_1.txt', 'a+') as wcarefile:
                wcarefile.write('\n' + self.patname.get() + ' - ')
                wcarefile.write(self.healthenter.get() + ' - ')
                wcarefile.write(self.daystring.get() + ' - ')
                wcarefile.write('Date of end : ' + self.datenter.get() + ' - ')
                wcarefile.write(self.txtBox.get('1.0', tk.END))
                print("[+] Ok, data recorded into file validate_1.txt.")
        except FileNotFoundError as err_wc:
            print("[!] File validate_1.txt not found !", err_wc)
            with open('./validation/valfiles1/validate_1.txt', 'a+') as add_caref:
                add_caref.write('\n' + self.patname.get() + ' - ')
                add_caref.write(self.healthenter.get() + ' - ')
                add_caref.write(self.daystring.get() + ' - ')
                add_caref.write('Date of end : ' + self.datenter.get() + ' - ')
                add_caref.write(self.txtBox.get('1.0', tk.END))
                print("[+] File validate_1.txt created !")

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
        self.patname = line1
        self.x3, self.y3 = 320, 120
        self.patname = tk.StringVar()
        self.entread = tk.Entry(self.can,
            textvariable=self.patname,
            highlightbackground='grey', bd=2)
        if line1 == '-':
            line1 = line1
        else:
            line1 = line1[:-1]
        self.patname.set(line1)
        self.fentread_window = self.can.create_window(self.x3,
            self.y3, window=self.entread)
    except UnboundLocalError as ub_error1:
        print("[!] File 1 not created !", ub_error1)

    # Care lbl
    self.x4, self.y4 = 120, 170
    self.lblcare = tk.Label(self.can, text="Care to validate :",
        font=('MS Serif', 14, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wlblcare_window = self.can.create_window(self.x4, self.y4,
        window = self.lblcare)

    self.x5, self.y5 = 320, 170
    self.healthenter = tk.StringVar()
    self.labhealth = tk.Entry(self.can, textvariable=self.healthenter,
        highlightbackground='grey', bd=2)
    self.healthenter.set("care heal")
    self.wlabhealth_window = self.can.create_window(self.x5, self.y5,
        window = self.labhealth)

    def callbackDay(event):
        print(self.daystring.get())

    # number of times per day label
    self.x6, self.y6 = 120, 220
    self.lblperday = tk.Label(self.can, text="Per day :",
        font=('MS Serif', 14, 'bold'), bg='DodgerBlue2', fg='white')
    self.wlblperday_window = self.can.create_window(self.x6, self.y6,
        window = self.lblperday)

    # number of times per day combobox
    def nbreperday():
        self.comboBoxpd['values']=['', '1x/d', '2x/d', '3x/d', '4x/d',
        '5x/d', '6x/d']

    self.daystring = tk.StringVar()
    self.comboBoxpd = ttk.Combobox(self.can, width=4, textvariable=self.daystring,
        values=['', '1x/d', '2x/d', '3x/d', '4x/d',
        '5x/d', '6x/d'], postcommand=nbreperday)

    self.comboBoxpd.bind("<<ComboboxSelected>>", callbackDay)
    self.comboBoxpd.current(0)
    self.fcomboBoxpd_window = self.can.create_window(260, 220, window=self.comboBoxpd)

    # until date entry
    self.x7, self.y7 = 120, 270
    self.lbluntil = tk.Label(self.can, text="Until (date) :",
        font=('MS Serif', 14, 'bold'), bg='DodgerBlue2', fg='white')
    self.wlbluntil_window = self.can.create_window(self.x7, self.y7,
        window = self.lbluntil)

    self.x8, self.y8 = 275, 270
    self.datenter = tk.StringVar()
    self.labentdate = tk.Entry(self.can, width=9, textvariable=self.datenter,
        highlightbackground='grey', bd=2)
    self.datenter.set(time.strftime("%d/%m/%Y"))
    self.wlabentdate_window = self.can.create_window(self.x8, self.y8,
        window = self.labentdate)

    self.x9, self.y9 = 120, 320
    self.lblcomment = tk.Label(self.can, text="Comments :",
        font=('MS Serif', 14, 'bold'), bg='DodgerBlue2', fg='white')
    self.wlblcomment_window = self.can.create_window(self.x9, self.y9,
        window = self.lblcomment)

    # enter button
    self.x11, self.y11 = 260, 620
    self.butsavechk = tk.Button(self.can, text="Save", width=20,
        fg='yellow', bg='RoyalBlue3', bd=3, highlightbackground='DodgerBlue2',
        activebackground='pale turquoise', command=lambda: ([stackvalidate(self), regroupAll()]))
    self.fbutsavechk_window = self.can.create_window(self.x11, self.y11,
        window=self.butsavechk)

    # textbox textbox

    self.can.configure(scrollregion=self.can.bbox(tk.ALL))
    self.can.unbind_all("<Button-4>")
    self.can.unbind_all("<Button-5>")
