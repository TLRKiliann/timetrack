#!/usr/bin/python3
# -*- coding: utf-8 -*-


from tkinter import *
import os


def homecsWind23(self):
    """
        Main function to define 
        design for contact interface.
    """
    self.can.delete(ALL)
    self.can.configure(background='DodgerBlue2')

    def allInData():
        """
            First page
        """
        try:
            if os.path.getsize('./contact/conpact23/hcscontact1.txt'):
                print("+ Ok, hcscontact1.txt exist (t1)")
        except FileNotFoundError as errfnf:
            print("+ No file hcscontact1.txt exist (Error1) !", errfnf)
            with open('./contact/conpact23/hcscontact1.txt', 'w') as testf:
                print("+ File hcscontact1.txt created !")

        self.x1, self.y1 = 900, 330
        self.txtBox = Text(self.can, height=13, width=40, font=18, relief=SUNKEN)
        self.txtBox.delete('1.0', END)
        self.txtBox.update()
        self.ftxtBox_window = self.can.create_window(self.x1, self.y1, window=self.txtBox)

        try:
            if os.path.exists('./contact/conpact23/hcscontact1.txt'):
                with open('./contact/conpact23/hcscontact1.txt', 'r') as policyfile:
                    line1 = policyfile.readline()
                    phone = policyfile.readline()
                    iphone2 = policyfile.readline()
                    street = policyfile.readline()
                    state = policyfile.readline()
                    email = policyfile.readline()
                self.txtBox.insert(INSERT, "--- Data Home Care System ---\n")
                self.txtBox.insert(END, "\nName : " + line1)
                self.txtBox.insert(END, "\nPhone : " + phone)
                self.txtBox.insert(END, "\nMobile : " + iphone2)
                self.txtBox.insert(END, "\nStreet : " + street)
                self.txtBox.insert(END, "\nCity : " + state)
                self.txtBox.insert(END, "\ne-mail : " + email)
            else:
                pass
        except FileNotFoundError as err_r:
            print("+ No file hcscontact1.txt exist (Error2) !", err_r)

        try:
            if os.path.getsize('./contact/conpact23/hcscontact2.txt'):
                print("+ Ok, hcscontact2.txt exist (t1)")
        except FileNotFoundError as errfnf2:
            print("+ No file hcscontact2.txt exist (Error3) !", errfnf2)
            with open('./contact/conpact23/hcscontact2.txt', 'w') as testf:
                print("+ File hcscontact2.txt created !")

        self.x2, self.y2 = 900, 750
        self.txtBox2 = Text(self.can, height=13, width=40, font=18, relief=SUNKEN)
        self.txtBox2.delete('1.0', END)
        self.txtBox2.update()
        self.ftxtBox2_window = self.can.create_window(self.x2, self.y2, window=self.txtBox2)

        try:
            if os.path.exists('./contact/conpact23/hcscontact2.txt'):
                with open('./contact/conpact23/hcscontact2.txt', 'r') as secondfile:
                    nameline = secondfile.readline()
                    phone_line = secondfile.readline()
                    iphone_line= secondfile.readline()
                    street_line = secondfile.readline()
                    state_line = secondfile.readline()
                    email_line = secondfile.readline()
                self.txtBox2.insert(INSERT, "--- Data Home Care System 2 ---\n")
                self.txtBox2.insert(END, "\nName : " + nameline)
                self.txtBox2.insert(END, "\nPhone : " + phone_line)
                self.txtBox2.insert(END, "\nMobile : " + iphone_line)
                self.txtBox2.insert(END, "\nStreet : " + street_line)
                self.txtBox2.insert(END, "\nCity : " + state_line)
                self.txtBox2.insert(END, "\ne-mail : " + email_line)
            else:
                pass
        except FileNotFoundError as err_line:
            print("+ No file hcscontact2.txt exist (Error4) !", err_line)

        try:
            if os.path.getsize('./contact/conpact23/hcscontact3.txt'):
                print("+ Ok, hcscontact3.txt exist (t1)")
        except FileNotFoundError as errfnf2:
            print("+ No file hcscontact3.txt exist (Error3) !", errfnf2)
            with open('./contact/conpact23/hcscontact3.txt', 'w') as testf:
                print("+ File hcscontact3.txt created !")

        self.x3, self.y3 = 900, 1170
        self.txtBox3 = Text(self.can, height=13, width=40, font=18, relief=SUNKEN)
        self.txtBox3.delete('1.0', END)
        self.txtBox3.update()
        self.ftxtBox3_window = self.can.create_window(self.x3, self.y3, window=self.txtBox3)

        try:
            if os.path.exists('./contact/conpact23/hcscontact3.txt'):
                with open('./contact/conpact23/hcscontact3.txt', 'r') as secondfile:
                    nameline3 = secondfile.readline()
                    phone_line3 = secondfile.readline()
                    iphone_line3= secondfile.readline()
                    street_line3 = secondfile.readline()
                    state_line3 = secondfile.readline()
                    email_line3 = secondfile.readline()
                self.txtBox3.insert(INSERT, "--- Data Home Care System 3 ---\n")
                self.txtBox3.insert(END, "\nName : " + nameline3)
                self.txtBox3.insert(END, "\nPhone : " + phone_line3)
                self.txtBox3.insert(END, "\nMobile : " + iphone_line3)
                self.txtBox3.insert(END, "\nStreet : " + street_line3)
                self.txtBox3.insert(END, "\nCity : " + state_line3)
                self.txtBox3.insert(END, "\ne-mail : " + email_line3)
            else:
                pass
        except FileNotFoundError as err_line:
            print("+ No file hcscontact3.txt exist (Error4) !", err_line)

    def recorderData(namentry, txtphone, phonentry, txtmobile,
        mobilentry, addrtxt, addrentry, citytxt, cityentry,
        mailtxt, entrymail):
        """
            Display origin
        """
        try:
            if os.path.getsize('./contact/conpact23/hcscontact1.txt'):
                print("+ Ok, hcscontact1.txt exist (t2)")
        except FileNotFoundError as errfnf:
            print("+ No file hcscontact1.txt exist (Error5) !", errfnf)
            with open('./contact/conpact23/hcscontact1.txt', 'w') as testf:
                print("+ File hcscontact1.txt created !")

        try:
            with open('./contact/conpact23/hcscontact1.txt', 'w') as iofile:
                iofile.write(namentry.get())
                iofile.write("\n" + phonentry.get())
                iofile.write("\n" + mobilentry.get())
                iofile.write("\n" + addrentry.get())
                iofile.write("\n" + cityentry.get())
                iofile.write("\n" + entrymail.get())
        except FileNotFoundError as fn:
            print("+ File hcscontact1.txt not found (Error6) !", fn)

        try:
            if os.path.getsize('./contact/conpact23/finalhcs1.txt'):
                os.remove('./contact/conpact23/finalhcs1.txt')
        except FileNotFoundError as err_termin:
            print("+ finalhcs1 not found (Error7) !", err_termin)
            with open('./contact/conpact23/finalhcs1.txt', 'a+'):
                print("+ finalhcs1.txt exist!")

        try:
            with open('./contact/conpact23/finalhcs1.txt', 'w') as terminfile:
                terminfile.write("Name : " + namentry.get())
                terminfile.write("\nPhone : " + phonentry.get())
                terminfile.write("\nPhone : " + mobilentry.get())
                terminfile.write("\nStreet : " + addrentry.get())
                terminfile.write("\nCity : " + cityentry.get())
                terminfile.write("\ne-mail : " + entrymail.get())
        except FileNotFoundError as err2_final:
            print("+ finalhcs1.txt not created (Error8) !", err2_final)

        allInData()

    def recordersecData(name_twoentry, txt_twophone, twophonentry,
        txt_twomobile, mobile_toentry, addr_twotxt, addr_twoentry,
        twocitytxt, city_twoentry, mail_twotxt, entry_twomail):
        """
            Display origin
        """
        try:
            if os.path.getsize('./contact/conpact23/hcscontact2.txt'):
                print("+ Ok, hcscontact2.txt exist (t3)")
        except FileNotFoundError as errfnf:
            print("+ No file hcscontact2.txt exist (Error9) !", errfnf)
            with open('./contact/conpact23/hcscontact2.txt', 'w') as testf:
                print("+ File hcscontact2.txt created !")

        try:
            with open('./contact/conpact23/hcscontact2.txt', 'w') as copyfile:
                copyfile.write(name_twoentry.get())
                copyfile.write("\n" + twophonentry.get())
                copyfile.write("\n" + mobile_toentry.get())
                copyfile.write("\n" + addr_twoentry.get())
                copyfile.write("\n" + city_twoentry.get())
                copyfile.write("\n" + entry_twomail.get())
        except FileNotFoundError as fn:
            print("+ File not found (Error10) !", fn)

        try:
            if os.path.getsize('./contact/conpact23/finalhcs2.txt'):
                os.remove('./contact/conpact23/finalhcs2.txt')
        except FileNotFoundError as err_termin:
            print("+ finalhcs2 not found (Error11) !", err_termin)
            with open('./contact/conpact23/finalhcs2.txt', 'a+'):
                print("+ finalhcs2.txt exist!")

        try:
            with open('./contact/conpact23/finalhcs2.txt', 'w') as secterfile:
                secterfile.write("Name : " + name_twoentry.get())
                secterfile.write("\nPhone : " + twophonentry.get())
                secterfile.write("\nPhone : " + mobile_toentry.get())
                secterfile.write("\nStreet : " + addr_twoentry.get())
                secterfile.write("\nCity : " + city_twoentry.get())
                secterfile.write("\ne-mail : " + entry_twomail.get())
        except FileNotFoundError as err2_final:
            print("+ finalhcs2.txt not created (Error12) !", err2_final)

        allInData()

    def recorderthirdData(name_thirdentry, txt_thirdphone, thirdphonentry,
        txt_thirdmobile, mobile_thirdentry, addr_thirdtxt, addr_thirdentry,
        thirdcitytxt, city_thirdentry, mail_thirdtxt, entry_thirdmail):
        """
            Display origin
        """
        try:
            if os.path.getsize('./contact/conpact23/hcscontact3.txt'):
                print("+ Ok, hcscontact3.txt exist (t3)")
        except FileNotFoundError as errfnf:
            print("+ No file hcscontact3.txt exist (Error13) !", errfnf)
            with open('./contact/conpact23/hcscontact3.txt', 'w') as testf:
                print("+ File hcscontact3.txt created !")

        try:
            with open('./contact/conpact23/hcscontact3.txt', 'w') as copyfile:
                copyfile.write(name_thirdentry.get())
                copyfile.write("\n" + thirdphonentry.get())
                copyfile.write("\n" + mobile_thirdentry.get())
                copyfile.write("\n" + addr_thirdentry.get())
                copyfile.write("\n" + city_thirdentry.get())
                copyfile.write("\n" + entry_thirdmail.get())
        except FileNotFoundError as fn:
            print("+ File not found (Error14) !", fn)

        try:
            if os.path.getsize('./contact/conpact23/finalhcs3.txt'):
                os.remove('./contact/conpact23/finalhcs3.txt')
        except FileNotFoundError as err_termin:
            print("+ finalhcs3 not found (Error15) !", err_termin)
            with open('./contact/conpact23/finalhcs3.txt', 'a+'):
                print("+ finalhcs3.txt exist!")

        try:
            with open('./contact/conpact23/finalhcs3.txt', 'w') as secterfile:
                secterfile.write("Name : " + name_thirdentry.get())
                secterfile.write("\nPhone : " + thirdphonentry.get())
                secterfile.write("\nPhone : " + mobile_thirdentry.get())
                secterfile.write("\nStreet : " + addr_thirdentry.get())
                secterfile.write("\nCity : " + city_thirdentry.get())
                secterfile.write("\ne-mail : " + entry_thirdmail.get())
        except FileNotFoundError as err2_final3:
            print("+ finalhcs3.txt not created (Error16) !", err2_final3)

        allInData()

    allInData()

    # Label title
    self.x11, self.y11 = 250, 100
    self.lbltitle = Label(self.can, text="Contact",
        font=('helvetica', 40, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wlbltitle_window = self.can.create_window(self.x11, self.y11,
        window = self.lbltitle)

    # Label title2
    self.x12, self.y12 = 580, 100
    self.labtitle = Label(self.can, text="Home Care System",
        font=('Times', 40, 'italic'),
        bg='DodgerBlue2', fg='coral')
    self.wlabtitle_window = self.can.create_window(self.x12, self.y12,
        window = self.labtitle)

    # Name
    self.x1, self.y1 = 250, 200
    self.labelname = Label(self.can, text="Name :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wlabelname_window = self.can.create_window(self.x1, self.y1,
        window = self.labelname)

    try:
        with open('./contact/conpact23/hcscontact1.txt', 'r') as namefile:
            linex = namefile.readline()
            line2 = namefile.readline()
            line3 = namefile.readline()
            line4 = namefile.readline()
            line5 = namefile.readline()
            line6 = namefile.readline()
    except FileNotFoundError as callfile:
        print("+ File hcscontact1.txt doesn't exist (Error13) !", callfile)

    try:
        self.txt_pat = linex
        self.x2, self.y2 = 450, 200
        self.txt_pat = StringVar()
        self.namentry = Entry(self.can, textvariable=self.txt_pat,
            highlightbackground='grey', bd=4)
        self.txt_pat.set(linex[:-1])
        self.wnamentry_window = self.can.create_window(self.x2, self.y2,
            window = self.namentry)
    except UnboundLocalError as ub_error1:
        print("+ File hcscontact1.txt empty... (Error14) !", ub_error1)

    # Phone
    self.x20, self.y20 = 250, 250
    self.phonelabel = Label(self.can, text="Phone :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wphonelabel_window = self.can.create_window(self.x20, self.y20,
        window = self.phonelabel)

    self.txtphone = line2
    self.x21, self.y21 = 450, 250
    self.txtphone = StringVar()
    self.phonentry = Entry(self.can, textvariable=self.txtphone,
        highlightbackground='grey', bd=3)
    self.txtphone.set(line2[:-1])
    self.wphonentry_window = self.can.create_window(self.x21, self.y21,
        window = self.phonentry)

    # Mobile
    self.x20, self.y20 = 250, 300
    self.lblmobile = Label(self.can, text="Mobile :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wlblmobile_window = self.can.create_window(self.x20, self.y20,
        window = self.lblmobile)

    self.txtmobile = line3
    self.x21, self.y21 = 450, 300
    self.txtmobile = StringVar()
    self.mobilentry = Entry(self.can, textvariable=self.txtmobile,
        highlightbackground='grey', bd=3)
    self.txtmobile.set(line3[:-1])
    self.wmobilentry_window = self.can.create_window(self.x21, self.y21,
        window = self.mobilentry)

    # Street
    self.x30, self.y30 = 250, 350
    self.addrlabel = Label(self.can, text="Street :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.waddrlabel_window = self.can.create_window(self.x30, self.y30,
        window = self.addrlabel)

    self.addrtxt = line4
    self.x31, self.y31 = 450, 350
    self.addrtxt = StringVar()
    self.addrentry = Entry(self.can, textvariable=self.addrtxt,
        highlightbackground='grey', bd=4)
    self.addrtxt.set(line4[:-1])
    self.waddrentry_window = self.can.create_window(self.x31, self.y31,
        window = self.addrentry)

    self.x32, self.y32 = 250, 400
    self.labcity = Label(self.can, text="City :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wlabcity_window = self.can.create_window(self.x32, self.y32,
        window = self.labcity)

    self.citytxt = line5
    self.x33, self.y33 = 450, 400
    self.citytxt = StringVar()
    self.cityentry = Entry(self.can, textvariable=self.citytxt,
        highlightbackground='grey', bd=4)
    self.citytxt.set(line5[:-1])
    self.wcityentry_window = self.can.create_window(self.x33, self.y33,
        window = self.cityentry)

    # e-mail
    self.x40, self.y40 = 250, 450
    self.mailabel = Label(self.can, text="e-mail :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wmailabel_window = self.can.create_window(self.x40, self.y40,
        window = self.mailabel)

    self.mailtxt = line6
    self.x41, self.y41 = 450, 450
    self.mailtxt = StringVar()
    self.entrymail = Entry(self.can, textvariable=self.mailtxt,
        highlightbackground='grey', bd=3)
    self.mailtxt.set(line6)
    self.wentrymail_window = self.can.create_window(self.x41, self.y41,
        window = self.entrymail)

    self.x52, self.y52 = 350, 520
    self.b52 = Button(self.can, text="Save Modifications", font=16,
        width=30, bd=3, bg='RoyalBlue3', fg='yellow',
        highlightbackground='cyan',
        activebackground='pale turquoise',
        command = lambda: recorderData(self.namentry, self.txtphone,
            self.phonentry, self.txtmobile, self.mobilentry,
            self.addrtxt, self.addrentry, self.citytxt, self.cityentry,
            self.mailtxt, self.entrymail))
    self.fb52_window = self.can.create_window(self.x52, self.y52, window=self.b52)

    # Name 2
    self.x101, self.y101 = 250, 620
    self.lblname2 = Label(self.can, text="Name :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wlblname2_window = self.can.create_window(self.x101, self.y101,
        window = self.lblname2)

    try:
        with open('./contact/conpact23/hcscontact2.txt', 'r') as namefile:
           two_linex = namefile.readline()
           two_line2 = namefile.readline()
           two_line3 = namefile.readline()
           two_line4 = namefile.readline()
           two_line5 = namefile.readline()
           two_line6 = namefile.readline()
    except FileNotFoundError as callfile:
        print("+ File hcscontact2.txt doesn't exist (Error15) !", callfile)

    try:
        self.txt_twopat = two_linex
        self.x102, self.y102 = 450, 620
        self.txt_twopat = StringVar()
        self.name_twoentry = Entry(self.can, textvariable=self.txt_twopat,
            highlightbackground='grey', bd=4)
        self.txt_twopat.set(two_linex[:-1])
        self.wname_twoentry_window = self.can.create_window(self.x102, self.y102,
            window = self.name_twoentry)
    except UnboundLocalError as ub_error1:
        print("+ File 1 not created (Error16) !", ub_error1)

    # Phone
    self.x103, self.y103 = 250, 670
    self.lbl_phone = Label(self.can, text="Phone :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wlbl_phone_window = self.can.create_window(self.x103, self.y103,
        window = self.lbl_phone)

    self.txt_twophone = two_line2
    self.x104, self.y104 = 450, 670
    self.txt_twophone = StringVar()
    self.twophonentry = Entry(self.can, textvariable=self.txt_twophone,
        highlightbackground='grey', bd=3)
    self.txt_twophone.set(two_line2[:-1])
    self.wtwophonentry_window = self.can.create_window(self.x104, self.y104,
        window = self.twophonentry)

    # Mobile
    self.x105, self.y105 = 250, 720
    self.twolbl_mobile = Label(self.can, text="Mobile :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wtwolbl_mobile_window = self.can.create_window(self.x105, self.y105,
        window = self.twolbl_mobile)

    self.txt_twomobile = two_line3
    self.x106, self.y106 = 450, 720
    self.txt_twomobile = StringVar()
    self.mobile_toentry = Entry(self.can, textvariable=self.txt_twomobile,
        highlightbackground='grey', bd=3)
    self.txt_twomobile.set(two_line3[:-1])
    self.wmobile_toentry_window = self.can.create_window(self.x106, self.y106,
        window = self.mobile_toentry)

    # Street
    self.x110, self.y110 = 250, 770
    self.lbl_twoaddr = Label(self.can, text="Street :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wlbl_twoaddr_window = self.can.create_window(self.x110, self.y110,
        window = self.lbl_twoaddr)

    self.addr_twotxt = two_line4
    self.x111, self.y111 = 450, 770
    self.addr_twotxt = StringVar()
    self.addr_twoentry = Entry(self.can, textvariable=self.addr_twotxt,
        highlightbackground='grey', bd=4)
    self.addr_twotxt.set(two_line4[:-1])
    self.waddr_twoentry_window = self.can.create_window(self.x111, self.y111,
        window = self.addr_twoentry)

    self.x112, self.y112 = 250, 820
    self.lbl_twocity = Label(self.can, text="City :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wlbl_twocity_window = self.can.create_window(self.x112, self.y112,
        window = self.lbl_twocity)

    self.twocitytxt = two_line5
    self.x113, self.y113 = 450, 820
    self.twocitytxt = StringVar()
    self.city_twoentry = Entry(self.can, textvariable=self.twocitytxt,
        highlightbackground='grey', bd=4)
    self.twocitytxt.set(two_line5[:-1])
    self.wcity_twoentry_window = self.can.create_window(self.x113, self.y113,
        window = self.city_twoentry)

    # e-mail
    self.x114, self.y114 = 250, 870
    self.lblmail2 = Label(self.can, text="e-mail :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wlblmail2_window = self.can.create_window(self.x114, self.y114,
        window = self.lblmail2)

    self.mail_twotxt = two_line6
    self.x115, self.y115 = 450, 870
    self.mail_twotxt = StringVar()
    self.entry_twomail = Entry(self.can, textvariable=self.mail_twotxt,
        highlightbackground='grey', bd=3)
    self.mail_twotxt.set(two_line6)
    self.wentry_twomail_window = self.can.create_window(self.x115, self.y115,
        window = self.entry_twomail)

    self.x116, self.y116 = 350, 940
    self.b116 = Button(self.can, text="Save Modifications", font=16,
        width=30, bd=3, bg='RoyalBlue3', fg='yellow',
        highlightbackground='cyan',
        activebackground='pale turquoise',
        command = lambda: recordersecData(self.name_twoentry, self.txt_twophone,
            self.twophonentry, self.txt_twomobile, self.mobile_toentry,
            self.addr_twotxt, self.addr_twoentry, self.twocitytxt, self.city_twoentry,
            self.mail_twotxt, self.entry_twomail))
    self.fb116_window = self.can.create_window(self.x116, self.y116,
        window=self.b116)

    # Name 3
    self.x120, self.y120 = 250, 1040
    self.lblname2 = Label(self.can, text="Name :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wlblname2_window = self.can.create_window(self.x120, self.y120,
        window = self.lblname2)

    try:
        with open('./contact/conpact23/hcscontact3.txt', 'r') as namefile3:
           third_linex = namefile3.readline()
           third_line2 = namefile3.readline()
           third_line3 = namefile3.readline()
           third_line4 = namefile3.readline()
           third_line5 = namefile3.readline()
           third_line6 = namefile3.readline()
    except FileNotFoundError as callfile3:
        print("+ File hcscontact3.txt doesn't exist (Error17) !", callfile3)

    try:
        self.txt_thirdpat = third_linex
        self.x121, self.y121 = 450, 1040
        self.txt_thirdpat = StringVar()
        self.name_thirdentry = Entry(self.can, textvariable=self.txt_thirdpat,
            highlightbackground='grey', bd=4)
        self.txt_thirdpat.set(third_linex[:-1])
        self.wname_thirdentry_window = self.can.create_window(self.x121, self.y121,
            window = self.name_thirdentry)
    except UnboundLocalError as ub_error3:
        print("+ File 1 not created (Error18) !", ub_error3)

    # Phone
    self.x122, self.y122 = 250, 1090
    self.lbl_thirdphone = Label(self.can, text="Phone :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wlbl_thirdphone_window = self.can.create_window(self.x122, self.y122,
        window = self.lbl_thirdphone)

    self.txt_thirdphone = third_line2
    self.x123, self.y123 = 450, 1090
    self.txt_thirdphone = StringVar()
    self.thirdphonentry = Entry(self.can, textvariable=self.txt_thirdphone,
        highlightbackground='grey', bd=3)
    self.txt_thirdphone.set(third_line2[:-1])
    self.wthirdphonentry_window = self.can.create_window(self.x123, self.y123,
        window = self.thirdphonentry)

    # Mobile
    self.x124, self.y124 = 250, 1140
    self.thirdlbl_mobile = Label(self.can, text="Mobile :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wthirdlbl_mobile_window = self.can.create_window(self.x124, self.y124,
        window = self.thirdlbl_mobile)

    self.txt_thirdmobile = third_line3
    self.x125, self.y125 = 450, 1140
    self.txt_thirdmobile = StringVar()
    self.mobile_thirdentry = Entry(self.can, textvariable=self.txt_thirdmobile,
        highlightbackground='grey', bd=3)
    self.txt_thirdmobile.set(third_line3[:-1])
    self.wmobile_thirdentry_window = self.can.create_window(self.x125, self.y125,
        window = self.mobile_thirdentry)

    # Street
    self.x126, self.y126 = 250, 1190
    self.lbl_thirdaddr = Label(self.can, text="Street :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wlbl_thirdaddr_window = self.can.create_window(self.x126, self.y126,
        window = self.lbl_thirdaddr)

    self.addr_thirdtxt = third_line4
    self.x127, self.y127 = 450, 1190
    self.addr_thirdtxt = StringVar()
    self.addr_thirdentry = Entry(self.can, textvariable=self.addr_thirdtxt,
        highlightbackground='grey', bd=4)
    self.addr_thirdtxt.set(third_line4[:-1])
    self.waddr_thirdentry_window = self.can.create_window(self.x127, self.y127,
        window = self.addr_thirdentry)

    self.x128, self.y128 = 250, 1240
    self.lbl_thirdcity = Label(self.can, text="City :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wlbl_thirdcity_window = self.can.create_window(self.x128, self.y128,
        window = self.lbl_thirdcity)

    self.thirdcitytxt = third_line5
    self.x129, self.y129 = 450, 1240
    self.thirdcitytxt = StringVar()
    self.city_thirdentry = Entry(self.can, textvariable=self.thirdcitytxt,
        highlightbackground='grey', bd=4)
    self.thirdcitytxt.set(third_line5[:-1])
    self.wcity_thirdentry_window = self.can.create_window(self.x129, self.y129,
        window = self.city_thirdentry)

    # e-mail
    self.x130, self.y130 = 250, 1290
    self.labelmail3 = Label(self.can, text="e-mail :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wlabelmail3_window = self.can.create_window(self.x130, self.y130,
        window = self.labelmail3)

    self.mail_thirdtxt = third_line6
    self.x131, self.y131 = 450, 1290
    self.mail_thirdtxt = StringVar()
    self.entry_thirdmail = Entry(self.can, textvariable=self.mail_thirdtxt,
        highlightbackground='grey', bd=3)
    self.mail_thirdtxt.set(third_line6)
    self.wentry_thirdmail_window = self.can.create_window(self.x131, self.y131,
        window = self.entry_thirdmail)

    self.x132, self.y132 = 350, 1360
    self.b132 = Button(self.can, text="Save Modifications", font=16,
        width=30, bd=3, bg='RoyalBlue3', fg='yellow',
        highlightbackground='cyan',
        activebackground='pale turquoise',
        command = lambda: recorderthirdData(self.name_thirdentry, self.txt_thirdphone,
            self.thirdphonentry, self.txt_thirdmobile, self.mobile_thirdentry,
            self.addr_thirdtxt, self.addr_thirdentry, self.thirdcitytxt,
            self.city_thirdentry, self.mail_thirdtxt, self.entry_thirdmail))
    self.fb132_window = self.can.create_window(self.x132, self.y132,
        window=self.b132)

    self.can.configure(scrollregion=self.can.bbox(ALL))
