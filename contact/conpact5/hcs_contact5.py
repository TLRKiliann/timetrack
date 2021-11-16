#!/usr/bin/python3
# -*- coding: utf-8 -*-


import tkinter as tk
import os
from contact.conpact5.writerfiles.writehcs5 import careOneRec
from contact.conpact5.writerfiles.writehcs5 import careTwoRec
from contact.conpact5.writerfiles.writehcs5 import careThreeRec


def homecsWind5(self):
    """
        Main function to define 
        design for contact interface.
    """
    self.effacer()
    self.can.configure(background='DodgerBlue2')

    def careInSys():
        """
            First page
        """
        self.x1, self.y1 = 900, 330
        self.txtBox = tk.Text(self.can, height=13, width=40, font=18, relief=tk.SUNKEN)
        self.txtBox.delete('1.0', tk.END)
        self.txtBox.update()
        self.ftxtBox_window = self.can.create_window(self.x1, self.y1, window=self.txtBox)

        def sysCareOne():
            try:
                if os.path.getsize('./contact/conpact5/hcscontact1.txt'):
                    print("[+] Ok, hcscontact1.txt exist (t1)")
            except FileNotFoundError as errfnf:
                print("[!] File hcscontact1.txt doesn't exist (Error_1) !", errfnf)
                with open('./contact/conpact5/hcscontact1.txt', 'w') as testf:
                    print("[+] File hcscontact1.txt created !")

            try:
                if os.path.exists('./contact/conpact5/hcscontact1.txt'):
                    with open('./contact/conpact5/hcscontact1.txt', 'r') as policyfile:
                        line1 = policyfile.readline()
                        phone = policyfile.readline()
                        iphone2 = policyfile.readline()
                        street = policyfile.readline()
                        state = policyfile.readline()
                        email = policyfile.readline()
                    self.txtBox.insert(tk.INSERT, "--- Data Home Care System ---\n")
                    self.txtBox.insert(tk.END, "\nName : " + line1)
                    self.txtBox.insert(tk.END, "\nPhone : " + phone)
                    self.txtBox.insert(tk.END, "\nMobile : " + iphone2)
                    self.txtBox.insert(tk.END, "\nStreet : " + street)
                    self.txtBox.insert(tk.END, "\nCity : " + state)
                    self.txtBox.insert(tk.END, "\ne-mail : " + email)
                else:
                    pass
            except FileNotFoundError as err_r:
                print("[!] File hcscontact1.txt doesn't exist (Error_2) !", err_r)

        sysCareOne()

        self.x2, self.y2 = 900, 750
        self.txtBox2 = tk.Text(self.can, height=13, width=40, font=18, relief=tk.SUNKEN)
        self.txtBox2.delete('1.0', tk.END)
        self.txtBox2.update()
        self.ftxtBox2_window = self.can.create_window(self.x2, self.y2, window=self.txtBox2)

        def sysCareSec():
            try:
                if os.path.getsize('./contact/conpact5/hcscontact2.txt'):
                    print("[+] Ok, hcscontact2.txt exist.")
            except FileNotFoundError as errfnf2:
                print("[!] File hcscontact2.txt doesn't exist (Error_3) !", errfnf2)
                with open('./contact/conpact5/hcscontact2.txt', 'w') as testf:
                    print("[+] File hcscontact2.txt created !")

            try:
                if os.path.exists('./contact/conpact5/hcscontact2.txt'):
                    with open('./contact/conpact5/hcscontact2.txt', 'r') as secondfile:
                        nameline = secondfile.readline()
                        phone_line = secondfile.readline()
                        iphone_line= secondfile.readline()
                        street_line = secondfile.readline()
                        state_line = secondfile.readline()
                        email_line = secondfile.readline()
                    self.txtBox2.insert(tk.INSERT, "--- Data Home Care System 2 ---\n")
                    self.txtBox2.insert(tk.END, "\nName : " + nameline)
                    self.txtBox2.insert(tk.END, "\nPhone : " + phone_line)
                    self.txtBox2.insert(tk.END, "\nMobile : " + iphone_line)
                    self.txtBox2.insert(tk.END, "\nStreet : " + street_line)
                    self.txtBox2.insert(tk.END, "\nCity : " + state_line)
                    self.txtBox2.insert(tk.END, "\ne-mail : " + email_line)
                else:
                    pass
            except FileNotFoundError as err_line:
                print("[!] File hcscontact2.txt doesn't exist (Error_4) !", err_line)

        sysCareSec()

        self.x3, self.y3 = 900, 1170
        self.txtBox3 = tk.Text(self.can, height=13, width=40, font=18, relief=tk.SUNKEN)
        self.txtBox3.delete('1.0', tk.END)
        self.txtBox3.update()
        self.ftxtBox3_window = self.can.create_window(self.x3, self.y3, window=self.txtBox3)

        def sysCareThird():
            try:
                if os.path.getsize('./contact/conpact5/hcscontact3.txt'):
                    print("[+] Ok, hcscontact3.txt exist.")
            except FileNotFoundError as errfnf2:
                print("[!] File hcscontact3.txt doesn't exist (Error_5) !", errfnf2)
                with open('./contact/conpact5/hcscontact3.txt', 'w') as testf:
                    print("[+] File hcscontact3.txt created !")

            try:
                if os.path.exists('./contact/conpact5/hcscontact3.txt'):
                    with open('./contact/conpact5/hcscontact3.txt', 'r') as secondfile:
                        nameline3 = secondfile.readline()
                        phone_line3 = secondfile.readline()
                        iphone_line3= secondfile.readline()
                        street_line3 = secondfile.readline()
                        state_line3 = secondfile.readline()
                        email_line3 = secondfile.readline()
                    self.txtBox3.insert(tk.INSERT, "--- Data Home Care System 3 ---\n")
                    self.txtBox3.insert(tk.END, "\nName : " + nameline3)
                    self.txtBox3.insert(tk.END, "\nPhone : " + phone_line3)
                    self.txtBox3.insert(tk.END, "\nMobile : " + iphone_line3)
                    self.txtBox3.insert(tk.END, "\nStreet : " + street_line3)
                    self.txtBox3.insert(tk.END, "\nCity : " + state_line3)
                    self.txtBox3.insert(tk.END, "\ne-mail : " + email_line3)
                else:
                    pass
            except FileNotFoundError as err_line:
                print("[!] File hcscontact3.txt exist (Error_6) !", err_line)

        sysCareThird()

    careInSys()

    # Label ghost1
    self.x4, self.y4 = 250, 50
    self.firstghost = tk.Label(self.can, width=10, text="", bg='DodgerBlue2')
    self.wfirstghost_window = self.can.create_window(self.x4, self.y4,
        window = self.firstghost)

    # Label title
    self.x11, self.y11 = 250, 100
    self.lbltitle = tk.Label(self.can, text="Contact",
        font=('MS Serif', 30, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wlbltitle_window = self.can.create_window(self.x11, self.y11,
        window = self.lbltitle)

    # Label title2
    self.x12, self.y12 = 580, 100
    self.labtitle = tk.Label(self.can, text="Home Care System",
        font=('MS Serif', 30, 'bold'),
        bg='DodgerBlue2', fg='cyan')
    self.wlabtitle_window = self.can.create_window(self.x12, self.y12,
        window = self.labtitle)

    # Name
    self.x1, self.y1 = 250, 200
    self.labelname = tk.Label(self.can, text="Name :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wlabelname_window = self.can.create_window(self.x1, self.y1,
        window = self.labelname)

    try:
        with open('./contact/conpact5/hcscontact1.txt', 'r') as namefile:
            linex = namefile.readline()
            line2 = namefile.readline()
            line3 = namefile.readline()
            line4 = namefile.readline()
            line5 = namefile.readline()
            line6 = namefile.readline()
    except FileNotFoundError as callfile:
        print("[!] File hcscontact1.txt doesn't exist (Error_18) !", callfile)

    try:
        self.txt_pat = linex
        self.x2, self.y2 = 450, 200
        self.txt_pat = tk.StringVar()
        self.namentry = tk.Entry(self.can, textvariable=self.txt_pat,
            highlightbackground='grey', bd=2)
        self.txt_pat.set(linex[:-1])
        self.wnamentry_window = self.can.create_window(self.x2, self.y2,
            window = self.namentry)
    except UnboundLocalError as ub_error1:
        print("[!] File hcscontact1.txt empty... (Error_19) !", ub_error1)

    # Phone
    self.x20, self.y20 = 250, 250
    self.phonelabel = tk.Label(self.can, text="Phone :",
        font=('helvetica', 18, 'bold'),
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
    self.x20, self.y20 = 250, 300
    self.lblmobile = tk.Label(self.can, text="Mobile :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wlblmobile_window = self.can.create_window(self.x20, self.y20,
        window = self.lblmobile)

    self.txtmobile = line3
    self.x21, self.y21 = 450, 300
    self.txtmobile = tk.StringVar()
    self.mobilentry = tk.Entry(self.can, textvariable=self.txtmobile,
        highlightbackground='grey', bd=2)
    self.txtmobile.set(line3[:-1])
    self.wmobilentry_window = self.can.create_window(self.x21, self.y21,
        window = self.mobilentry)

    # Street
    self.x30, self.y30 = 250, 350
    self.addrlabel = tk.Label(self.can, text="Street :",
        font=('helvetica', 18, 'bold'),
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
        font=('helvetica', 18, 'bold'),
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
        font=('helvetica', 18, 'bold'),
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

    self.x52, self.y52 = 370, 520
    self.b52 = tk.Button(self.can, text="Save Modifications",
        font=('MS Serif', 14), width=26, bd=3, bg='RoyalBlue3',
        fg='cyan', highlightbackground='DodgerBlue2',
        activebackground='pale turquoise',
        command = lambda: ([careOneRec(self), careInSys()]))
    self.fb52_window = self.can.create_window(self.x52, self.y52, window=self.b52)

    # Name 2
    self.x101, self.y101 = 250, 620
    self.lblname2 = tk.Label(self.can, text="Name :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wlblname2_window = self.can.create_window(self.x101, self.y101,
        window = self.lblname2)

    try:
        with open('./contact/conpact5/hcscontact2.txt', 'r') as namefile:
           two_linex = namefile.readline()
           two_line2 = namefile.readline()
           two_line3 = namefile.readline()
           two_line4 = namefile.readline()
           two_line5 = namefile.readline()
           two_line6 = namefile.readline()
    except FileNotFoundError as callfile:
        print("[!] File hcscontact2.txt doesn't exist (Error_20) !", callfile)

    try:
        self.txt_twopat = two_linex
        self.x102, self.y102 = 450, 620
        self.txt_twopat = tk.StringVar()
        self.name_twoentry = tk.Entry(self.can, textvariable=self.txt_twopat,
            highlightbackground='grey', bd=2)
        self.txt_twopat.set(two_linex[:-1])
        self.wname_twoentry_window = self.can.create_window(self.x102, self.y102,
            window = self.name_twoentry)
    except UnboundLocalError as ub_error1:
        print("+ File 1 not created (Error16) !", ub_error1)

    # Phone
    self.x103, self.y103 = 250, 670
    self.lbl_phone = tk.Label(self.can, text="Phone :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wlbl_phone_window = self.can.create_window(self.x103, self.y103,
        window = self.lbl_phone)

    self.txt_twophone = two_line2
    self.x104, self.y104 = 450, 670
    self.txt_twophone = tk.StringVar()
    self.twophonentry = tk.Entry(self.can, textvariable=self.txt_twophone,
        highlightbackground='grey', bd=2)
    self.txt_twophone.set(two_line2[:-1])
    self.wtwophonentry_window = self.can.create_window(self.x104, self.y104,
        window = self.twophonentry)

    # Mobile
    self.x105, self.y105 = 250, 720
    self.twolbl_mobile = tk.Label(self.can, text="Mobile :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wtwolbl_mobile_window = self.can.create_window(self.x105, self.y105,
        window = self.twolbl_mobile)

    self.txt_twomobile = two_line3
    self.x106, self.y106 = 450, 720
    self.txt_twomobile = tk.StringVar()
    self.mobile_toentry = tk.Entry(self.can, textvariable=self.txt_twomobile,
        highlightbackground='grey', bd=2)
    self.txt_twomobile.set(two_line3[:-1])
    self.wmobile_toentry_window = self.can.create_window(self.x106, self.y106,
        window = self.mobile_toentry)

    # Street
    self.x110, self.y110 = 250, 770
    self.lbl_twoaddr = tk.Label(self.can, text="Street :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wlbl_twoaddr_window = self.can.create_window(self.x110, self.y110,
        window = self.lbl_twoaddr)

    self.addr_twotxt = two_line4
    self.x111, self.y111 = 450, 770
    self.addr_twotxt = tk.StringVar()
    self.addr_twoentry = tk.Entry(self.can, textvariable=self.addr_twotxt,
        highlightbackground='grey', bd=2)
    self.addr_twotxt.set(two_line4[:-1])
    self.waddr_twoentry_window = self.can.create_window(self.x111, self.y111,
        window = self.addr_twoentry)

    self.x112, self.y112 = 250, 820
    self.lbl_twocity = tk.Label(self.can, text="City :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wlbl_twocity_window = self.can.create_window(self.x112, self.y112,
        window = self.lbl_twocity)

    self.twocitytxt = two_line5
    self.x113, self.y113 = 450, 820
    self.twocitytxt = tk.StringVar()
    self.city_twoentry = tk.Entry(self.can, textvariable=self.twocitytxt,
        highlightbackground='grey', bd=2)
    self.twocitytxt.set(two_line5[:-1])
    self.wcity_twoentry_window = self.can.create_window(self.x113, self.y113,
        window = self.city_twoentry)

    # e-mail
    self.x114, self.y114 = 250, 870
    self.lblmail2 = tk.Label(self.can, text="e-mail :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wlblmail2_window = self.can.create_window(self.x114, self.y114,
        window = self.lblmail2)

    self.mail_twotxt = two_line6
    self.x115, self.y115 = 450, 870
    self.mail_twotxt = tk.StringVar()
    self.entry_twomail = tk.Entry(self.can, textvariable=self.mail_twotxt,
        highlightbackground='grey', bd=2)
    self.mail_twotxt.set(two_line6)
    self.wentry_twomail_window = self.can.create_window(self.x115, self.y115,
        window = self.entry_twomail)

    self.x116, self.y116 = 370, 940
    self.b116 = tk.Button(self.can, text="Save Modifications",
        font=('MS Serif', 14), width=26, bd=3, bg='RoyalBlue3',
        fg='cyan', highlightbackground='DodgerBlue2',
        activebackground='pale turquoise',
        command = lambda: ([careTwoRec(self), careInSys()]))
    self.fb116_window = self.can.create_window(self.x116, self.y116,
        window=self.b116)

    # Name 3
    self.x120, self.y120 = 250, 1040
    self.lblname2 = tk.Label(self.can, text="Name :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wlblname2_window = self.can.create_window(self.x120, self.y120,
        window = self.lblname2)

    try:
        with open('./contact/conpact5/hcscontact3.txt', 'r') as namefile3:
           third_linex = namefile3.readline()
           third_line2 = namefile3.readline()
           third_line3 = namefile3.readline()
           third_line4 = namefile3.readline()
           third_line5 = namefile3.readline()
           third_line6 = namefile3.readline()
    except FileNotFoundError as callfile3:
        print("[!] File hcscontact3.txt doesn't exist (Error_21) !", callfile3)

    try:
        self.txt_thirdpat = third_linex
        self.x121, self.y121 = 450, 1040
        self.txt_thirdpat = tk.StringVar()
        self.name_thirdentry = tk.Entry(self.can, textvariable=self.txt_thirdpat,
            highlightbackground='grey', bd=2)
        self.txt_thirdpat.set(third_linex[:-1])
        self.wname_thirdentry_window = self.can.create_window(self.x121, self.y121,
            window = self.name_thirdentry)
    except UnboundLocalError as ub_error3:
        print("+ File 1 not created (Error18) !", ub_error3)

    # Phone
    self.x122, self.y122 = 250, 1090
    self.lbl_thirdphone = tk.Label(self.can, text="Phone :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wlbl_thirdphone_window = self.can.create_window(self.x122, self.y122,
        window = self.lbl_thirdphone)

    self.txt_thirdphone = third_line2
    self.x123, self.y123 = 450, 1090
    self.txt_thirdphone = tk.StringVar()
    self.thirdphonentry = tk.Entry(self.can, textvariable=self.txt_thirdphone,
        highlightbackground='grey', bd=2)
    self.txt_thirdphone.set(third_line2[:-1])
    self.wthirdphonentry_window = self.can.create_window(self.x123, self.y123,
        window = self.thirdphonentry)

    # Mobile
    self.x124, self.y124 = 250, 1140
    self.thirdlbl_mobile = tk.Label(self.can, text="Mobile :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wthirdlbl_mobile_window = self.can.create_window(self.x124, self.y124,
        window = self.thirdlbl_mobile)

    self.txt_thirdmobile = third_line3
    self.x125, self.y125 = 450, 1140
    self.txt_thirdmobile = tk.StringVar()
    self.mobile_thirdentry = tk.Entry(self.can, textvariable=self.txt_thirdmobile,
        highlightbackground='grey', bd=2)
    self.txt_thirdmobile.set(third_line3[:-1])
    self.wmobile_thirdentry_window = self.can.create_window(self.x125, self.y125,
        window = self.mobile_thirdentry)

    # Street
    self.x126, self.y126 = 250, 1190
    self.lbl_thirdaddr = tk.Label(self.can, text="Street :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wlbl_thirdaddr_window = self.can.create_window(self.x126, self.y126,
        window = self.lbl_thirdaddr)

    self.addr_thirdtxt = third_line4
    self.x127, self.y127 = 450, 1190
    self.addr_thirdtxt = tk.StringVar()
    self.addr_thirdentry = tk.Entry(self.can, textvariable=self.addr_thirdtxt,
        highlightbackground='grey', bd=2)
    self.addr_thirdtxt.set(third_line4[:-1])
    self.waddr_thirdentry_window = self.can.create_window(self.x127, self.y127,
        window = self.addr_thirdentry)

    self.x128, self.y128 = 250, 1240
    self.lbl_thirdcity = tk.Label(self.can, text="City :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wlbl_thirdcity_window = self.can.create_window(self.x128, self.y128,
        window = self.lbl_thirdcity)

    self.thirdcitytxt = third_line5
    self.x129, self.y129 = 450, 1240
    self.thirdcitytxt = tk.StringVar()
    self.city_thirdentry = tk.Entry(self.can, textvariable=self.thirdcitytxt,
        highlightbackground='grey', bd=2)
    self.thirdcitytxt.set(third_line5[:-1])
    self.wcity_thirdentry_window = self.can.create_window(self.x129, self.y129,
        window = self.city_thirdentry)

    # e-mail
    self.x130, self.y130 = 250, 1290
    self.labelmail3 = tk.Label(self.can, text="e-mail :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wlabelmail3_window = self.can.create_window(self.x130, self.y130,
        window = self.labelmail3)

    self.mail_thirdtxt = third_line6
    self.x131, self.y131 = 450, 1290
    self.mail_thirdtxt = tk.StringVar()
    self.entry_thirdmail = tk.Entry(self.can, textvariable=self.mail_thirdtxt,
        highlightbackground='grey', bd=2)
    self.mail_thirdtxt.set(third_line6)
    self.wentry_thirdmail_window = self.can.create_window(self.x131, self.y131,
        window = self.entry_thirdmail)

    self.x132, self.y132 = 370, 1360
    self.b132 = tk.Button(self.can, text="Save Modifications",
        font=('MS Serif', 14), width=26, bd=3, bg='RoyalBlue3',
        fg='cyan', highlightbackground='DodgerBlue2',
        activebackground='pale turquoise',
        command = lambda: ([careThreeRec(self), careInSys()]))
    self.fb132_window = self.can.create_window(self.x132, self.y132,
        window=self.b132)

    # Label ghost1
    self.x140, self.y140 = 370, 1410
    self.secondghost = tk.Label(self.can, width=10, text="", bg='DodgerBlue2')
    self.fsecondghost_window = self.can.create_window(self.x140, self.y140,
        window = self.secondghost)

    self.can.configure(scrollregion=self.can.bbox(tk.ALL))
    self.can.bind("<Button-1>", self.reinitscroll)
    self.can.bind("<Button-3>", self.delScroll)
