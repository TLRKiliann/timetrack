#!/usr/bin/python3
# -*- coding: utf-8 -*-


from tkinter import *
import os


def Window20(self):
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
            if os.path.getsize('./contact/conpact20/contact1.txt'):
                print("+ Ok, contact1.txt exist (t1)")
        except FileNotFoundError as errfnf:
            print("+ No file contact1.txt exist", errfnf)
            with open('./contact/conpact20/contact1.txt', 'w') as testf:
                print("+ File contact1.txt created !")

        self.x1, self.y1 = 900, 420
        self.txtBox = Text(self.can, height=23, width=40, font=18, relief=SUNKEN)
        self.txtBox.delete('1.0', END)
        self.txtBox.update()
        self.ftxtBox_window = self.can.create_window(self.x1, self.y1, window=self.txtBox)

        try:
            if os.path.exists('./contact/conpact20/contact1.txt'):
                with open('./contact/conpact20/contact1.txt', 'r') as policyfile:
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
                self.txtBox.insert(INSERT, "--- Data Patient ---\n")
                self.txtBox.insert(END, "\nPatient name : " + line1)
                self.txtBox.insert(END, "\nBirthdate : " + line2)
                self.txtBox.insert(END, "\nNative : " + native)
                self.txtBox.insert(END, "\nPhone : " + phone)
                self.txtBox.insert(END, "\nStreet : " + street)
                self.txtBox.insert(END, "\nCity : " + state)
                self.txtBox.insert(END, "\ne-mail : " + email)
                self.txtBox.insert(END, "\nInsurance : " + assu)
                self.txtBox.insert(END, "\nPolicy : " + polins)
                self.txtBox.insert(END, "\nCivil status : " + civilstat)
                self.txtBox.insert(END, "\nConfession : " + confessionstat)
            else:
                pass
        except FileNotFoundError as err_r:
            print("+ No file contact1.txt exist (Error1)", err_r)

    def recorderData(namentry, birthvar, native, nativaentry, txtphone, phonentry,
        addrtxt, addrentry, citytxt, cityentry, mailtxt, entrymail, assurance, entryassu,
        policy, entrypolicy, civil, entrycivil, confess, entryconfess):
        """
            Display origin
        """
        try:
            if os.path.getsize('./contact/conpact20/contact1.txt'):
                print("+ Ok, contact1.txt exist")
        except FileNotFoundError as errfnf:
            print("+ No file contact1.txt exist (Error2)", errfnf)
            with open('./contact/conpact20/contact1.txt', 'w') as testf:
                print("+ File contact1.txt created !")

        try:
            with open('./contact/conpact20/contact1.txt', 'w') as iofile:
                iofile.write(namentry.get())
                iofile.write("\n" + birthvar)
                iofile.write("\n" + nativaentry.get())
                iofile.write("\n" + phonentry.get())
                iofile.write("\n" + addrentry.get())
                iofile.write("\n" + cityentry.get())
                iofile.write("\n" + entrymail.get())
                iofile.write("\n" + entryassu.get())
                iofile.write("\n" + entrypolicy.get())
                iofile.write("\n" + entrycivil.get())
                iofile.write("\n" + entryconfess.get())
        except FileNotFoundError as fn:
            print("+ File not found !", fn)

        try:
            if os.path.getsize('./contact/conpact20/finalfile1.txt'):
                os.remove('./contact/conpact20/finalfile1.txt')
        except FileNotFoundError as err_termin:
            print("+ finalfile1 not found !(Error3)", err_termin)
            with open('./contact/conpact20/finalfile1.txt', 'a+'):
                print("+ finalfile1.txt exist!")
        try:
            with open('./contact/conpact20/finalfile1.txt', 'w') as terminfile:
                terminfile.write("Patient name : " + namentry.get())
                terminfile.write("\nBirthdate : " + birthvar)
                terminfile.write("\nNative : " + nativaentry.get())
                terminfile.write("\nPhone : " + phonentry.get())
                terminfile.write("\nStreet : " + addrentry.get())
                terminfile.write("\nCity : " + cityentry.get())
                terminfile.write("\ne-mail : " + entrymail.get())
                terminfile.write("\nInsurance : " + entryassu.get())
                terminfile.write("\nPolicy : " + entrypolicy.get())
                terminfile.write("\nCivil status : " + entrycivil.get())
                terminfile.write("\nConfession : " + entryconfess.get())
        except FileNotFoundError as err2_final:
            print("+ finalfile1.txt not created (Error4)", err2_final)

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
    self.x12, self.y12 = 450, 100
    self.labtitle = Label(self.can, text="Patient",
        font=('Times', 40, 'italic'),
        bg='DodgerBlue2', fg='coral')
    self.wlabtitle_window = self.can.create_window(self.x12, self.y12,
        window = self.labtitle)

    # Name
    self.x1, self.y1 = 250, 200
    self.labelname = Label(self.can, text="Patient Name :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wlabelname_window = self.can.create_window(self.x1, self.y1,
        window = self.labelname)

    try:
        with open('./newpatient/entryfile20.txt', 'r') as namefile:
            line1 = namefile.readline()
            line2 = namefile.readline()
            txt_pat = line1
            birthvar = line2[:-1]
    except FileNotFoundError as callfile:
        print("+ File entryfile.txt doesn't exist !", callfile)

    try:
        self.txt_pat = line1
        self.x2, self.y2 = 450, 200
        self.txt_pat = StringVar()
        self.namentry = Entry(self.can, textvariable=self.txt_pat,
            highlightbackground='grey', bd=4)
        self.txt_pat.set(line1[:-1])
        self.wnamentry_window = self.can.create_window(self.x2, self.y2,
            window = self.namentry)
    except UnboundLocalError as ub_error1:
        print("+ File 1 not created !", ub_error1)

    try:
        with open('./contact/conpact20/contact1.txt', 'r') as namefile:
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
        print("+ File contact1.txt doesn't exist ! (Error5)", callfile)

    # Native
    self.x15, self.y15 = 250, 250
    self.nativelab = Label(self.can, text="Native :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wnativelab_window = self.can.create_window(self.x15, self.y15,
        window = self.nativelab)

    self.native = line3
    self.x16, self.y16 = 450, 250
    self.native = StringVar()
    self.nativaentry = Entry(self.can, textvariable=self.native,
        highlightbackground='grey', bd=3)
    self.native.set(line3[:-1])
    self.wnativaentry_window = self.can.create_window(self.x16, self.y16,
        window = self.nativaentry)

    # Phone
    self.x20, self.y20 = 250, 300
    self.phonelabel = Label(self.can, text="Phone Number :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wphonelabel_window = self.can.create_window(self.x20, self.y20,
        window = self.phonelabel)

    self.txtphone = line4
    self.x21, self.y21 = 450, 300
    self.txtphone = StringVar()
    self.phonentry = Entry(self.can, textvariable=self.txtphone,
        highlightbackground='grey', bd=3)
    self.txtphone.set(line4[:-1])
    self.wphonentry_window = self.can.create_window(self.x21, self.y21,
        window = self.phonentry)

    # Street
    self.x30, self.y30 = 250, 350
    self.addrlabel = Label(self.can, text="Street :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.waddrlabel_window = self.can.create_window(self.x30, self.y30,
        window = self.addrlabel)

    self.addrtxt = line5
    self.x31, self.y31 = 450, 350
    self.addrtxt = StringVar()
    self.addrentry = Entry(self.can, textvariable=self.addrtxt,
        highlightbackground='grey', bd=4)
    self.addrtxt.set(line5[:-1])
    self.waddrentry_window = self.can.create_window(self.x31, self.y31,
        window = self.addrentry)

    self.x32, self.y32 = 250, 400
    self.labcity = Label(self.can, text="City :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wlabcity_window = self.can.create_window(self.x32, self.y32,
        window = self.labcity)

    self.citytxt = line6
    self.x33, self.y33 = 450, 400
    self.citytxt = StringVar()
    self.cityentry = Entry(self.can, textvariable=self.citytxt,
        highlightbackground='grey', bd=4)
    self.citytxt.set(line6[:-1])
    self.wcityentry_window = self.can.create_window(self.x33, self.y33,
        window = self.cityentry)

    # e-mail
    self.x40, self.y40 = 250, 450
    self.mailabel = Label(self.can, text="e-mail :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wmailabel_window = self.can.create_window(self.x40, self.y40,
        window = self.mailabel)

    self.mailtxt = line7
    self.x41, self.y41 = 450, 450
    self.mailtxt = StringVar()
    self.entrymail = Entry(self.can, textvariable=self.mailtxt,
        highlightbackground='grey', bd=3)
    self.mailtxt.set(line7[:-1])
    self.wentrymail_window = self.can.create_window(self.x41, self.y41,
        window = self.entrymail)

    # Assurance
    self.x50, self.y50 = 250, 500
    self.mailabel = Label(self.can, text="Insurance :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wmailabel_window = self.can.create_window(self.x50, self.y50,
        window = self.mailabel)

    self.assurance = line8
    self.x51, self.y51 = 450, 500
    self.assurance = StringVar()
    self.entryassu = Entry(self.can, textvariable=self.assurance,
        highlightbackground='grey', bd=3)
    self.assurance.set(line8[:-1])
    self.wentryassu_window = self.can.create_window(self.x51, self.y51,
        window = self.entryassu)

    # Police
    self.x50, self.y50 = 250, 550
    self.mailabel = Label(self.can, text="Policy Number :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wmailabel_window = self.can.create_window(self.x50, self.y50,
        window = self.mailabel)

    self.policy = line9
    self.x51, self.y51 = 450, 550
    self.policy = StringVar()
    self.entrypolicy = Entry(self.can, textvariable=self.policy,
        highlightbackground='grey', bd=3)
    self.policy.set(line9[:-1])
    self.wentrypolicy_window = self.can.create_window(self.x51, self.y51,
        window = self.entrypolicy)

    # Civil status
    self.x52, self.y52 = 250, 600
    self.labcivil = Label(self.can, text="Civil Status :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wlabcivil_window = self.can.create_window(self.x52, self.y52,
        window = self.labcivil)

    self.civil = line10
    self.x53, self.y53 = 450, 600
    self.civil = StringVar()
    self.entrycivil = Entry(self.can, textvariable=self.civil,
        highlightbackground='grey', bd=3)
    self.civil.set(line10[:-1])
    self.wentrycivil_window = self.can.create_window(self.x53, self.y53,
        window = self.entrycivil)

    # Religious Confession
    self.x54, self.y54 = 250, 650
    self.labconfess = Label(self.can, text="Confession :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wlabconfess_window = self.can.create_window(self.x54, self.y54,
        window = self.labconfess)

    self.confess = line11
    self.x55, self.y55 = 450, 650
    self.confess = StringVar()
    self.entryconfess = Entry(self.can, textvariable=self.confess,
        highlightbackground='grey', bd=3)
    self.confess.set(line11)
    self.wentryconfess_window = self.can.create_window(self.x55, self.y55,
        window = self.entryconfess)

    self.x56, self.y56 = 350, 720
    self.b56 = Button(self.can, text="Save Modifications", font=16,
        width=30, bd=3, bg='RoyalBlue3', fg='yellow',
        highlightbackground='cyan',
        activebackground='pale turquoise',
        command = lambda: recorderData(self.namentry, birthvar,
            self.native, self.nativaentry, self.txtphone, self.phonentry,
            self.addrtxt, self.addrentry, self.citytxt, self.cityentry,
            self.mailtxt, self.entrymail, self.assurance, self.entryassu,
            self.policy, self.entrypolicy, self.civil, self.entrycivil,
            self.confess, self.entryconfess))
    self.fb56_window = self.can.create_window(self.x56, self.y56, window=self.b56)

    self.can.configure(scrollregion=self.can.bbox(ALL))
