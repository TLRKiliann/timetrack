#!/usr/bin/python3
# -*- coding: utf-8 -*-


import tkinter as tk
import os
from contact.conpact11.writerfiles.writepat11 import recorderData


def Window11(self):
    """
        Main function to define 
        design for contact interface.
    """
    self.effacer()
    self.forgetVsb()
    self.photo = tk.PhotoImage(file='./syno_gif/tt_fontcolor.png')
    self.itemfirst = self.can.create_image((0,0), image=self.photo,
        anchor=tk.NW)

    def allInData():
        """
            First page
        """
        self.x1, self.y1 = 900, 345
        self.txtBox = tk.Text(self.can, height=23, width=40, font=18, relief=tk.SUNKEN)
        self.txtBox.delete('1.0', tk.END)
        self.txtBox.update()
        self.ftxtBox_window = self.can.create_window(self.x1, self.y1, window=self.txtBox)

        def importationFile():
            try:
                if os.path.getsize('./contact/conpact11/contact11.txt'):
                    print("[+] Ok, contact11.txt exist")
            except FileNotFoundError as errfnf:
                print("[!] File contact11.txt doesn't exist (Error2)", errfnf)
                with open('./contact/conpact11/contact11.txt', 'w') as testf:
                    print("[+] File contact11.txt created !")

            try:
                if os.path.exists('./contact/conpact11/contact11.txt'):
                    with open('./contact/conpact11/contact11.txt', 'r') as policyfile:
                        line1 = policyfile.readline()
                        line2 = policyfile.readline()
                        native = policyfile.readline()
                        phone = policyfile.readline()
                        street = policyfile.readline()
                        state = policyfile.readline()
                        email = policyfile.readline()
                        assu = policyfile.readline()
                        polins = policyfile.readline()
                        civilstat = policyfile.readline()
                        confessionstat = policyfile.readline()
            except FileNotFoundError as err_r:
                print("[!] File contact11.txt doesn't exist (Error_1)", err_r)

            self.txtBox.insert(tk.INSERT, "--- Data Patient ---\n")
            self.txtBox.insert(tk.END, "\nPatient name : " + line1)
            self.txtBox.insert(tk.END, "\nBirthdate : " + line2)
            self.txtBox.insert(tk.END, "\nNative : " + native)
            self.txtBox.insert(tk.END, "\nPhone : " + phone)
            self.txtBox.insert(tk.END, "\nStreet : " + street)
            self.txtBox.insert(tk.END, "\nCity : " + state)
            self.txtBox.insert(tk.END, "\ne-mail : " + email)
            self.txtBox.insert(tk.END, "\nInsurance : " + assu)
            self.txtBox.insert(tk.END, "\nPolicy : " + polins)
            self.txtBox.insert(tk.END, "\nCivil status : " + civilstat)
            self.txtBox.insert(tk.END, "\nConfession : " + confessionstat)

        importationFile()

    allInData()

    # Label title
    self.x2, self.y2 = 520, 50
    self.lbltitle = tk.Label(self.can, text="Contact",
        font=('MS Serif', 30, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wlbltitle_window = self.can.create_window(self.x2, self.y2,
        window = self.lbltitle)

    # Label title2
    self.x3, self.y3 = 710, 50
    self.lblsectitle = tk.Label(self.can, text="Patient",
        font=('MS Serif', 30, 'bold'),
        bg='DodgerBlue2', fg='cyan')
    self.wlblsectitle_window = self.can.create_window(self.x3, self.y3,
        window = self.lblsectitle)

    # Name
    self.x4, self.y4 = 250, 120
    self.labelname = tk.Label(self.can, text="Patient Name :",
        font=('Times New Roman', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wlabelname_window = self.can.create_window(self.x4, self.y4,
        window = self.labelname)

    try:
        with open('./newpatient/entryfile11.txt', 'r') as namefile:
            line1 = namefile.readline()
            line2 = namefile.readline()
            txt_pat = line1
            birthvar = line2[:-1]
    except FileNotFoundError as callfile:
        print("[+] File entryfile11.txt doesn't exist !", callfile)

    try:
        self.txt_pat = line1
        self.x5, self.y5 = 450, 120
        self.txt_pat = tk.StringVar()
        self.namentry = tk.Entry(self.can, textvariable=self.txt_pat,
            highlightbackground='grey', bd=2)
        self.txt_pat.set(line1[:-1])
        self.wnamentry_window = self.can.create_window(self.x5, self.y5,
            window = self.namentry)
    except UnboundLocalError as ub_error1:
        print("[!] File 1 not created !", ub_error1)

    try:
        with open('./contact/conpact11/contact11.txt', 'r') as namefile:
            linex = namefile.readline()
            liney = namefile.readline()
            line3 = namefile.readline()
            line4 = namefile.readline()
            line5 = namefile.readline()
            line6 = namefile.readline()
            line7 = namefile.readline()
            line8 = namefile.readline()
            line9 = namefile.readline()
            line10 = namefile.readline()
            line11 = namefile.readline()
    except FileNotFoundError as callfile:
        print("[!] File contact11.txt doesn't exist ! (Error_2)", callfile)

    # Native
    self.x6, self.y6 = 250, 170
    self.nativelab = tk.Label(self.can, text="Native :",
        font=('Times New Roman', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wnativelab_window = self.can.create_window(self.x6, self.y6,
        window = self.nativelab)

    self.native = line3
    self.x7, self.y7 = 450, 170
    self.native = tk.StringVar()
    self.nativaentry = tk.Entry(self.can, textvariable=self.native,
        highlightbackground='grey', bd=2)
    self.native.set(line3[:-1])
    self.wnativaentry_window = self.can.create_window(self.x7, self.y7,
        window = self.nativaentry)

    # Phone
    self.x10, self.y10 = 250, 220
    self.phonelabel = tk.Label(self.can, text="Phone Number :",
        font=('Times New Roman', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wphonelabel_window = self.can.create_window(self.x10, self.y10,
        window = self.phonelabel)

    self.txtphone = line4
    self.x11, self.y11 = 450, 220
    self.txtphone = tk.StringVar()
    self.phonentry = tk.Entry(self.can, textvariable=self.txtphone,
        highlightbackground='grey', bd=2)
    self.txtphone.set(line4[:-1])
    self.wphonentry_window = self.can.create_window(self.x11, self.y11,
        window = self.phonentry)

    # Address
    self.x12, self.y12 = 250, 270
    self.addrlabel = tk.Label(self.can, text="Street :",
        font=('Times New Roman', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.waddrlabel_window = self.can.create_window(self.x12, self.y12,
        window = self.addrlabel)

    self.addrtxt = line5
    self.x20, self.y20 = 450, 270
    self.addrtxt = tk.StringVar()
    self.addrentry = tk.Entry(self.can, textvariable=self.addrtxt,
        highlightbackground='grey', bd=2)
    self.addrtxt.set(line5[:-1])
    self.waddrentry_window = self.can.create_window(self.x20, self.y20,
        window = self.addrentry)

    self.x30, self.y30 = 250, 320
    self.labcity = tk.Label(self.can, text="City :",
        font=('Times New Roman', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wlabcity_window = self.can.create_window(self.x30, self.y30,
        window = self.labcity)

    self.citytxt = line6
    self.x33, self.y33 = 450, 320
    self.citytxt = tk.StringVar()
    self.cityentry = tk.Entry(self.can, textvariable=self.citytxt,
        highlightbackground='grey', bd=2)
    self.citytxt.set(line6[:-1])
    self.wcityentry_window = self.can.create_window(self.x33, self.y33,
        window = self.cityentry)

    # e-mail
    self.x40, self.y40 = 250, 370
    self.mailabel = tk.Label(self.can, text="e-mail :",
        font=('Times New Roman', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wmailabel_window = self.can.create_window(self.x40, self.y40,
        window = self.mailabel)

    self.mailtxt = line7
    self.x41, self.y41 = 450, 370
    self.mailtxt = tk.StringVar()
    self.entrymail = tk.Entry(self.can, textvariable=self.mailtxt,
        highlightbackground='grey', bd=2)
    self.mailtxt.set(line7[:-1])
    self.wentrymail_window = self.can.create_window(self.x41, self.y41,
        window = self.entrymail)

    # Assurance
    self.x50, self.y50 = 250, 420
    self.mailabel = tk.Label(self.can, text="Insurance :",
        font=('Times New Roman', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wmailabel_window = self.can.create_window(self.x50, self.y50,
        window = self.mailabel)

    self.assurance = line8
    self.x51, self.y51 = 450, 420
    self.assurance = tk.StringVar()
    self.entryassu = tk.Entry(self.can, textvariable=self.assurance,
        highlightbackground='grey', bd=2)
    self.assurance.set(line8[:-1])
    self.wentryassu_window = self.can.create_window(self.x51, self.y51,
        window = self.entryassu)

    # Police
    self.x52, self.y52 = 250, 470
    self.mailabel = tk.Label(self.can, text="Policy Number :",
        font=('Times New Roman', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wmailabel_window = self.can.create_window(self.x52, self.y52,
        window = self.mailabel)

    self.policy = line9
    self.x53, self.y53 = 450, 470
    self.policy = tk.StringVar()
    self.entrypolicy = tk.Entry(self.can, textvariable=self.policy,
        highlightbackground='grey', bd=2)
    self.policy.set(line9[:-1])
    self.wentrypolicy_window = self.can.create_window(self.x53, self.y53,
        window = self.entrypolicy)

    # Civil status
    self.x60, self.y60 = 250, 520
    self.labcivil = tk.Label(self.can, text="Civil Status :",
        font=('Times New Roman', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wlabcivil_window = self.can.create_window(self.x60, self.y60,
        window = self.labcivil)

    self.civil = line10
    self.x61, self.y61 = 450, 520
    self.civil = tk.StringVar()
    self.entrycivil = tk.Entry(self.can, textvariable=self.civil,
        highlightbackground='grey', bd=2)
    self.civil.set(line10[:-1])
    self.wentrycivil_window = self.can.create_window(self.x61, self.y61,
        window = self.entrycivil)

    # Religious Confession
    self.x62, self.y62 = 250, 570
    self.labconfess = tk.Label(self.can, text="Confession :",
        font=('Times New Roman', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wlabconfess_window = self.can.create_window(self.x62, self.y62,
        window = self.labconfess)

    self.confess = line11
    self.x63, self.y63 = 450, 570
    self.confess = tk.StringVar()
    self.entryconfess = tk.Entry(self.can, textvariable=self.confess,
        highlightbackground='grey', bd=2)
    self.confess.set(line11)
    self.wentryconfess_window = self.can.create_window(self.x63, self.y63,
        window = self.entryconfess)

    # Button save
    self.x64, self.y64 = 350, 640
    self.b64 = tk.Button(self.can, text="Save Modifications", font=('MS Serif', 14),
        width=28, bd=3, bg='RoyalBlue3', fg='cyan',
        highlightbackground='DodgerBlue2',
        activebackground='pale turquoise',
        command = lambda: ([recorderData(self, birthvar), allInData()]))
    self.fb64_window = self.can.create_window(self.x64, self.y64, window=self.b64)

    self.can.configure(scrollregion=self.can.bbox(tk.ALL))
    self.can.bind("<Button-1>", self.delScroll)
