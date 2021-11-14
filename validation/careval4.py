#!/usr/bin/python3
# -*- coding: utf-8 -*-


import tkinter as tk
from tkinter import ttk
import os
import time


def valFunc4(self):
    """
        Main function to define
        design for contact interface.
    """
    self.effacer()
    self.forgetVsb()

    self.photo = tk.PhotoImage(file='./syno_gif/tt_fontcolor.png')
    self.itemfirst = self.can.create_image((0,0), image=self.photo,
        anchor=tk.NW)

    def awayOut():
        try:
            self.effacer()
            self.showPatients()
        except (OSError, ValueError) as p_out:
            print("[!] Error to way out !!!", p_out)

    # button return
    self.x40, self.y40 = 80, 40
    self.butreturn = tk.Button(self.can, text="Return to main", width=10,
        fg='cyan', bg='RoyalBlue3', bd=3, highlightbackground='DodgerBlue2',
        activebackground='pale turquoise', command=awayOut)
    self.fbutreturn_window = self.can.create_window(self.x40, self.y40,
        window=self.butreturn)

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
            with open('./validation/valfiles1/validate_4.txt', 'a+') as wcarefile:
                wcarefile.write('\n' + time.strftime('%d/%m/%Y'))
                wcarefile.write('\n' + self.patname.get() + ' - ')
                wcarefile.write(self.healthenter.get() + ' - ')
                wcarefile.write(self.daystring.get() + ' - ')
                wcarefile.write('Date of end : ' + self.datenter.get() + ' - ')
                wcarefile.write(self.txtBox.get('1.0', tk.END))
                print("[+] Ok, data recorded into file validate_4.txt.")
        except FileNotFoundError as err_wc:
            print("[!] File validate_4.txt not found !", err_wc)
            with open('./validation/valfiles1/validate_4.txt', 'a+') as add_caref:
                add_caref.write('\n' + time.strftime('%d/%m/%Y'))
                add_caref.write('\n' + self.patname.get() + ' - ')
                add_caref.write(self.healthenter.get() + ' - ')
                add_caref.write(self.daystring.get() + ' - ')
                add_caref.write('Date of end : ' + self.datenter.get() + ' - ')
                add_caref.write(self.txtBox.get('1.0', tk.END))
                print("[+] File validate_4.txt created !")

    # Label title
    self.x1, self.y1 = 625, 50
    self.lbltitle = tk.Label(self.can, text="Validation",
        font=('MS Serif', 26, 'bold'), bg='DodgerBlue2', fg='white')
    self.wlbltitle_window = self.can.create_window(self.x1, self.y1,
        window = self.lbltitle)

    # Name lbl
    self.x2, self.y2 = 120, 120
    self.lblname = tk.Label(self.can, text="Patient Name :",
        font=('MS Serif', 14, 'bold'), bg='DodgerBlue2', fg='white')
    self.wlblname_window = self.can.create_window(self.x2, self.y2,
        window = self.lblname)

    # Patient 1
    try:
        with open('./newpatient/entryfile4.txt', 'r') as namefile:
            line1 = namefile.readline()
    except FileNotFoundError as callfile:
        print("[!] File entryfile4.txt doesn't exist !", callfile)

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
    self.lblcare = tk.Label(self.can, text="Heal Care :",
        font=('MS Serif', 14, 'bold'), bg='DodgerBlue2', fg='white')
    self.wlblcare_window = self.can.create_window(self.x4, self.y4,
        window = self.lblcare)

    self.x5, self.y5 = 320, 170
    self.healthenter = tk.StringVar()
    self.labhealth = tk.Entry(self.can, textvariable=self.healthenter,
        highlightbackground='grey', bd=2)
    self.healthenter.set("???")
    self.wlabhealth_window = self.can.create_window(self.x5, self.y5,
        window = self.labhealth)

    def callbackDay(event):
        print(self.daystring.get())

    # number of times per day label
    self.x6, self.y6 = 120, 220
    self.lblperday = tk.Label(self.can, text="Per day - Per week :",
        font=('MS Serif', 14, 'bold'), bg='DodgerBlue2', fg='white')
    self.wlblperday_window = self.can.create_window(self.x6, self.y6,
        window = self.lblperday)

    # number of times per day combobox
    def nbreperday():
        self.comboBoxpd['values']=['', '1x/d', '2x/d', '3x/d', '4x/d',
        '5x/d', '6x/d', '1x/week', '2x/week', '3x/week', '4x/week', '5x/week']

    self.daystring = tk.StringVar()
    self.comboBoxpd = ttk.Combobox(self.can, width=8, textvariable=self.daystring,
        values=['', '1x/d', '2x/d', '3x/d', '4x/d',
        '5x/d', '6x/d', '1x/week', '2x/week', '3x/week', '4x/week', '5x/week'],
        postcommand=nbreperday)

    self.comboBoxpd.bind("<<ComboboxSelected>>", callbackDay)
    self.comboBoxpd.current(0)
    self.fcomboBoxpd_window = self.can.create_window(277, 220, window=self.comboBoxpd)

    # until date entry
    self.x7, self.y7 = 120, 270
    self.lbluntil = tk.Label(self.can, text="Until (date) :",
        font=('MS Serif', 14, 'bold'), bg='DodgerBlue2', fg='white')
    self.wlbluntil_window = self.can.create_window(self.x7, self.y7,
        window = self.lbluntil)

    self.x8, self.y8 = 275, 270
    self.datenter = tk.StringVar()
    self.labentdate = tk.Entry(self.can, width=10, textvariable=self.datenter,
        highlightbackground='grey', bd=2)
    self.datenter.set(time.strftime("%d/%m/%Y"))
    self.wlabentdate_window = self.can.create_window(self.x8, self.y8,
        window = self.labentdate)

    self.x9, self.y9 = 120, 320
    self.lblcomment = tk.Label(self.can, text="Comments :",
        font=('MS Serif', 14, 'bold'), bg='DodgerBlue2', fg='white')
    self.wlblcomment_window = self.can.create_window(self.x9, self.y9,
        window = self.lblcomment)

    def regroupAll():
        """
            second textbox2
        """
        self.x20, self.y20 = 900, 460
        self.txtBox2 = tk.Text(self.can, height=20, width=60, font=18, relief=tk.SUNKEN)
        self.txtBox2.delete('1.0', tk.END)
        self.txtBox2.update()
        self.ftxtBox2_window = self.can.create_window(self.x20, self.y20,
            window=self.txtBox2)

        def importationTxtBox():
            """
                To import data from validate_4.txt
                and display in textbox2.
            """
            try:
                if os.path.getsize('./validation/valfiles1/validate_4.txt'):
                    print("[+] Ok, validate_4.txt exist")
            except FileNotFoundError as errfnf:
                print("[!] File validate_4.txt not found !", errfnf)
                with open('./validation/valfiles1/validate_4.txt', 'w'):
                    pass
                print("[+] File validate_4.txt created !")

            try:
                if os.path.exists('./validation/valfiles1/validate_4.txt'):
                    with open('./validation/valfiles1/validate_4.txt', 'r') as val_f:
                        nametxt = val_f.read()
            except (FileNotFoundError, UnboundLocalError) as err_nfvali:
                print("[!] File validate_4.txt not found !", err_nfvali)

            self.txtBox2.insert(tk.INSERT, "--- Heal Care ---\n")
            self.txtBox2.insert(tk.END, nametxt)

        importationTxtBox()

    regroupAll()

    # left button to save
    self.x21, self.y21 = 260, 620
    self.butsavechk = tk.Button(self.can, text="Save", width=20,
        fg='yellow', bg='RoyalBlue3', bd=3, highlightbackground='DodgerBlue2',
        activebackground='pale turquoise', command=lambda: ([stackvalidate(self),
            regroupAll()]))
    self.fbutsavechk_window = self.can.create_window(self.x21, self.y21,
        window=self.butsavechk)

    def validRightFrame(self):
        """
            Save everything from Right Frame.
        """
        print(self.firstcheck.get())
        if self.firstcheck.get() == 1:
            print("ok validate")
            with open('./validation/valfiles1/validate_4.txt', 'a+') as oneval:
                oneval.write('\n' + self.datetov.get() + '\n')
                oneval.write(self.tttovalid.get())
                oneval.write(" [+] validated")
                oneval.write(self.signval.get() + '\n')
        else:
            print("[---] Nothing validated.")

    self.x24, self.y24 = 680, 120
    self.datetov = tk.StringVar()
    self.entdatev = tk.Entry(self.can, width=18, textvariable=self.datetov,
        highlightbackground='grey', bd=2)
    self.datetov.set(time.strftime('%d/%m/%Y : %H:%M:%S'))
    self.wentdatev_window = self.can.create_window(self.x24, self.y24,
        window = self.entdatev)

    self.x30, self.y30 = 660, 170
    self.firstcheck = tk.IntVar()
    self.checkone = tk.Checkbutton(self.can, text="Validate", font=('MS Serif', 12),
        fg='navy', bg='cyan', variable=self.firstcheck, onvalue=1, offvalue=0,
        height=1, width=8, anchor=tk.W)
    self.fcheckone_window = self.can.create_window(self.x30, self.y30,
        window = self.checkone)

    self.x31, self.y31 = 820, 170
    self.tttovalid = tk.StringVar()
    self.entrytreat = tk.Entry(self.can, width=20, textvariable=self.tttovalid,
        highlightbackground='grey', bd=2)
    self.tttovalid.set('???')
    self.wentrytreat_window = self.can.create_window(self.x31, self.y31,
        window = self.entrytreat)

    # signature
    self.x32, self.y32 = 660, 220
    self.labsign = tk.Label(self.can, text="Signature :",
        font=('MS Serif', 14, 'bold'), bg='DodgerBlue2', fg='white')
    self.wlabsign_window = self.can.create_window(self.x32, self.y32,
        window = self.labsign)

    self.x33, self.y33 = 820, 220
    self.signval = tk.StringVar()
    self.entsign = tk.Entry(self.can, width=20, textvariable=self.signval,
        highlightbackground='grey', bd=2)
    self.fentsign_window = self.can.create_window(self.x33, self.y33,
        window = self.entsign)

    # right button to save
    self.x34, self.y34 = 1040, 220
    self.butrightchk = tk.Button(self.can, text="Save Validation", width=20,
        fg='yellow', bg='RoyalBlue3', bd=3, highlightbackground='DodgerBlue2',
        activebackground='pale turquoise', command=lambda: ([validRightFrame(self),
            regroupAll()]))
    self.fbutrightchk_window = self.can.create_window(self.x34, self.y34,
        window=self.butrightchk)

    self.can.configure(scrollregion=self.can.bbox(tk.ALL))
    self.can.bind("<Button-1>", self.delScroll)
