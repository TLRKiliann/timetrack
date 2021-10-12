#!/usr/bin/python3
# -*- coding: utf-8 -*-


from tkinter import *
import os


def famWind20(self):
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
            if os.path.getsize('./contact/conpact20/famycontact1.txt'):
                print("+ Ok, famycontact1.txt exist (t1)")
        except FileNotFoundError as errfnf:
            print("+ No file famycontact1.txt exist", errfnf)
            with open('./contact/conpact20/famycontact1.txt', 'w') as testf:
                print("+ File famycontact1.txt created !")

        self.x1, self.y1 = 900, 330
        self.txtBox = Text(self.can, height=13, width=40, font=18, relief=SUNKEN)
        self.txtBox.delete('1.0', END)
        self.txtBox.update()
        self.ftxtBox_window = self.can.create_window(self.x1, self.y1, window=self.txtBox)

        try:
            if os.path.exists('./contact/conpact20/famycontact1.txt'):
                with open('./contact/conpact20/famycontact1.txt', 'r') as policyfile:
                    line1 = policyfile.readline()
                    phone = policyfile.readline()
                    iphone2 = policyfile.readline()
                    street = policyfile.readline()
                    state = policyfile.readline()
                    email = policyfile.readline()
                self.txtBox.insert(INSERT, "--- Data Relationship ---\n")
                self.txtBox.insert(END, "\nName : " + line1)
                self.txtBox.insert(END, "\nPhone : " + phone)
                self.txtBox.insert(END, "\nMobile : " + iphone2)
                self.txtBox.insert(END, "\nStreet : " + street)
                self.txtBox.insert(END, "\nCity : " + state)
                self.txtBox.insert(END, "\ne-mail : " + email)
            else:
                pass
        except FileNotFoundError as err_r:
            print("+ No file famycontact1.txt exist", err_r)

    def recorderData(namentry, txtphone, phonentry, txtmobile,
        mobilentry, addrtxt, addrentry, citytxt, cityentry,
        mailtxt, entrymail):
        """
            Display origin
        """
        try:
            if os.path.getsize('./contact/conpact20/famycontact1.txt'):
                print("+ Ok, famycontact1.txt exist (t2)")
        except FileNotFoundError as errfnf:
            print("+ No file famycontact1.txt exist", errfnf)
            with open('./contact/conpact20/famycontact1.txt', 'w') as testf:
                print("+ File famycontact1.txt created !")

        try:
            with open('./contact/conpact20/famycontact1.txt', 'w') as iofile:
                iofile.write(namentry.get())
                iofile.write("\n" + phonentry.get())
                iofile.write("\n" + mobilentry.get())
                iofile.write("\n" + addrentry.get())
                iofile.write("\n" + cityentry.get())
                iofile.write("\n" + entrymail.get())
        except FileNotFoundError as fn:
            print("+ File not found !", fn)

        try:
            if os.path.getsize('./contact/conpact20/finalfam1.txt'):
                os.remove('./contact/conpact20/finalfam1.txt')
        except FileNotFoundError as err_termin:
            print("+ finalfam1 not found !(t2)", err_termin)
            with open('./contact/conpact20/finalfam1.txt', 'a+'):
                print("+ finalfam1.txt exist!")
        try:
            with open('./contact/conpact20/finalfam1.txt', 'w') as terminfile:
                terminfile.write("Name : " + namentry.get())
                terminfile.write("\nPhone : " + phonentry.get())
                terminfile.write("\nPhone : " + mobilentry.get())
                terminfile.write("\nStreet : " + addrentry.get())
                terminfile.write("\nCity : " + cityentry.get())
                terminfile.write("\ne-mail : " + entrymail.get())
        except FileNotFoundError as err2_final:
            print("+ finalfam1.txt not created (t2)", err2_final)

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
    self.x12, self.y12 = 510, 100
    self.labtitle = Label(self.can, text="Relationship",
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
        with open('./contact/conpact20/famycontact1.txt', 'r') as namefile:
            linex = namefile.readline()
            line2 = namefile.readline()
            line3 = namefile.readline()
            line4 = namefile.readline()
            line5 = namefile.readline()
            line6 = namefile.readline()
    except FileNotFoundError as callfile:
        print("+ File famycontact1.txt doesn't exist !", callfile)

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
        print("+ File 1 not created !", ub_error1)

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

    self.can.configure(scrollregion=self.can.bbox(ALL))
