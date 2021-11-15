#!/usr/bin/python3
# -*- coding: utf-8 -*-


import tkinter as tk
import os
from contact.conpact5.writerfiles.writefam5 import recorderFam


def famWind5(self):
    """
        Main function to define 
        design for contact interface.
    """
    self.effacer()
    self.forgetVsb()
    self.photo = tk.PhotoImage(file='./syno_gif/tt_fontcolor.png')
    self.itemfirst = self.can.create_image((0,0), image=self.photo,
        anchor=tk.NW)

    def familyData():
        """
            First page
        """
        self.x1, self.y1 = 900, 330
        self.txtBox = tk.Text(self.can, height=13, width=40, font=18, relief=tk.SUNKEN)
        self.txtBox.delete('1.0', tk.END)
        self.txtBox.update()
        self.ftxtBox_window = self.can.create_window(self.x1, self.y1, window=self.txtBox)

        def readerFamily():
            try:
                if os.path.getsize('./contact/conpact5/famycontact5.txt'):
                    print("[+] Ok, famycontact5.txt exist (t2)")
            except FileNotFoundError as err_fnf:
                print("[!] No file famycontact5.txt exist", err_fnf)
                with open('./contact/conpact5/famycontact5.txt', 'w') as testf:
                    print("[+] File famycontact5.txt created !")

            try:
                if os.path.exists('./contact/conpact5/famycontact5.txt'):
                    with open('./contact/conpact5/famycontact5.txt', 'r') as policyfile:
                        line1 = policyfile.readline()
                        phone = policyfile.readline()
                        iphone2 = policyfile.readline()
                        street = policyfile.readline()
                        state = policyfile.readline()
                        email = policyfile.readline()
            except FileNotFoundError as err_r:
                print("[!] No file famycontact5.txt exist", err_r)

            self.txtBox.insert(tk.INSERT, "--- Data Relationship ---\n")
            self.txtBox.insert(tk.END, "\nName : " + line1)
            self.txtBox.insert(tk.END, "\nPhone : " + phone)
            self.txtBox.insert(tk.END, "\nMobile : " + iphone2)
            self.txtBox.insert(tk.END, "\nStreet : " + street)
            self.txtBox.insert(tk.END, "\nCity : " + state)
            self.txtBox.insert(tk.END, "\ne-mail : " + email)

        readerFamily()

    familyData()

    # Label title
    self.x11, self.y11 = 250, 100
    self.lbltitle = tk.Label(self.can, text="Contact",
        font=('MS Serif', 30, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wlbltitle_window = self.can.create_window(self.x11, self.y11,
        window = self.lbltitle)

    # Label title2
    self.x12, self.y12 = 510, 100
    self.labtitle = tk.Label(self.can, text="Relationship",
        font=('MS Serif', 30, 'bold'),
        bg='DodgerBlue2', fg='cyan')
    self.wlabtitle_window = self.can.create_window(self.x12, self.y12,
        window = self.labtitle)

    # Name
    self.x13, self.y13 = 250, 200
    self.labelname = tk.Label(self.can, text="Name :",
        font=('Times New Roman', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wlabelname_window = self.can.create_window(self.x13, self.y13,
        window = self.labelname)

    try:
        with open('./contact/conpact5/famycontact5.txt', 'r') as namefile:
            linex = namefile.readline()
            line2 = namefile.readline()
            line3 = namefile.readline()
            line4 = namefile.readline()
            line5 = namefile.readline()
            line6 = namefile.readline()
    except FileNotFoundError as callfile:
        print("[!] File famycontact5.txt doesn't exist !", callfile)

    try:
        self.txt_pat = linex
        self.x14, self.y14 = 450, 200
        self.txt_pat = tk.StringVar()
        self.namentry = tk.Entry(self.can, textvariable=self.txt_pat,
            highlightbackground='grey', bd=2)
        self.txt_pat.set(linex[:-1])
        self.wnamentry_window = self.can.create_window(self.x14, self.y14,
            window = self.namentry)
    except UnboundLocalError as ub_error1:
        print("[!] File famycontact5.txt not created !", ub_error1)

    # Phone
    self.x20, self.y20 = 250, 250
    self.phonelabel = tk.Label(self.can, text="Phone :",
        font=('Times New Roman', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wphonelabel_window = self.can.create_window(self.x20, self.y20,
        window = self.phonelabel)

    self.txtphone = line2
    self.x21, self.y21 = 450, 250
    self.txtphone = tk.StringVar()
    self.phonentry = tk.Entry(self.can, textvariable=self.txtphone,
        highlightbackground='grey', bd=2)
    self.txtphone.set(line2[:-1])
    self.wphonentry_window = self.can.create_window(self.x21, self.y21,
        window = self.phonentry)

    # Mobile
    self.x22, self.y22 = 250, 300
    self.lblmobile = tk.Label(self.can, text="Mobile :",
        font=('Times New Roman', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wlblmobile_window = self.can.create_window(self.x22, self.y22,
        window = self.lblmobile)

    self.txtmobile = line3
    self.x23, self.y23 = 450, 300
    self.txtmobile = tk.StringVar()
    self.mobilentry = tk.Entry(self.can, textvariable=self.txtmobile,
        highlightbackground='grey', bd=2)
    self.txtmobile.set(line3[:-1])
    self.wmobilentry_window = self.can.create_window(self.x23, self.y23,
        window = self.mobilentry)

    # Address
    self.x30, self.y30 = 250, 350
    self.addrlabel = tk.Label(self.can, text="Street :",
        font=('Times New Roman', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.waddrlabel_window = self.can.create_window(self.x30, self.y30,
        window = self.addrlabel)

    self.addrtxt = line4
    self.x31, self.y31 = 450, 350
    self.addrtxt = tk.StringVar()
    self.addrentry = tk.Entry(self.can, textvariable=self.addrtxt,
        highlightbackground='grey', bd=2)
    self.addrtxt.set(line4[:-1])
    self.waddrentry_window = self.can.create_window(self.x31, self.y31,
        window = self.addrentry)

    self.x32, self.y32 = 250, 400
    self.labcity = tk.Label(self.can, text="City :",
        font=('Times New Roman', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wlabcity_window = self.can.create_window(self.x32, self.y32,
        window = self.labcity)

    self.citytxt = line5
    self.x33, self.y33 = 450, 400
    self.citytxt = tk.StringVar()
    self.cityentry = tk.Entry(self.can, textvariable=self.citytxt,
        highlightbackground='grey', bd=2)
    self.citytxt.set(line5[:-1])
    self.wcityentry_window = self.can.create_window(self.x33, self.y33,
        window = self.cityentry)

    # e-mail
    self.x40, self.y40 = 250, 450
    self.mailabel = tk.Label(self.can, text="e-mail :",
        font=('Times New Roman', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wmailabel_window = self.can.create_window(self.x40, self.y40,
        window = self.mailabel)

    self.mailtxt = line6
    self.x41, self.y41 = 450, 450
    self.mailtxt = tk.StringVar()
    self.entrymail = tk.Entry(self.can, textvariable=self.mailtxt,
        highlightbackground='grey', bd=2)
    self.mailtxt.set(line6)
    self.wentrymail_window = self.can.create_window(self.x41, self.y41,
        window = self.entrymail)

    self.x52, self.y52 = 370, 540
    self.b52 = tk.Button(self.can, text="Save Modifications", font=('MS Serif', 14),
        width=26, bd=3, bg='RoyalBlue3', fg='cyan',
        highlightbackground='DodgerBlue2',
        activebackground='pale turquoise',
        command = lambda: ([recorderFam(self), familyData()]))
    self.fb52_window = self.can.create_window(self.x52, self.y52, window=self.b52)

    self.can.configure(scrollregion=self.can.bbox(tk.ALL))
    self.can.bind("<Button-1>", self.delScroll)
