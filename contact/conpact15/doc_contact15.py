#!/usr/bin/python3
# -*- coding: utf-8 -*-


from tkinter import *
import tkinter as tk
import os


def doctorWind15(self):
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
            if os.path.getsize('./contact/conpact15/contactdoc1.txt'):
                print("+ Ok, contactdoc1.txt exist (t1)")
        except FileNotFoundError as errfnf:
            print("+ No file contactdoc1.txt exist (Error1)", errfnf)
            with open('./contact/conpact15/contactdoc1.txt', 'w') as testf:
                print("+ File contactdoc1.txt created !", testf)

        self.x1, self.y1 = 900, 370
        self.txtBox = tk.Text(self.can, height=17, width=40, font=18, relief=SUNKEN)
        self.txtBox.delete('1.0', tk.END)
        self.txtBox.update()
        self.ftxtBox_window = self.can.create_window(self.x1, self.y1, window=self.txtBox)

        try:
            if os.path.exists('./contact/conpact15/contactdoc1.txt'):
                with open('./contact/conpact15/contactdoc1.txt', 'r') as policyfile:
                    line1 = policyfile.readline()
                    spec = policyfile.readline()
                    phone = policyfile.readline()
                    iphone2 = policyfile.readline()
                    street = policyfile.readline()
                    state = policyfile.readline()
                    email = policyfile.readline()
                    fax = policyfile.readline()
                self.txtBox.insert(tk.INSERT, "--- Data Doctor ---\n")
                self.txtBox.insert(tk.END, "\nDoctor : " + line1)
                self.txtBox.insert(tk.END, "\nSpecialization : " + spec)
                self.txtBox.insert(tk.END, "\nPhone : " + phone)
                self.txtBox.insert(tk.END, "\nMobile : " + iphone2)
                self.txtBox.insert(tk.END, "\nStreet : " + street)
                self.txtBox.insert(tk.END, "\nCity : " + state)
                self.txtBox.insert(tk.END, "\ne-mail : " + email)
                self.txtBox.insert(tk.END, "\nFax : " + fax)
            else:
                pass
        except FileNotFoundError as err_r:
            print("+ No file contactdoc1.txt exist (Error2)", err_r)

        try:
            if os.path.getsize('./contact/conpact15/contactdoc2.txt'):
                print("+ Ok, contactdoc2.txt exist (t2)")
        except FileNotFoundError as nfd2:
            print("+ No file contactdoc2.txt exist (Error3)", nfd2)
            with open('./contact/conpact15/contactdoc2.txt', 'w') as testfd2:
                print("+ File contactdoc2.txt created !", testfd2)

        self.x2, self.y2 = 900, 890
        self.txtBox2 = tk.Text(self.can, height=17, width=40, font=18, relief=SUNKEN)
        self.txtBox2.delete('1.0', tk.END)
        self.txtBox2.update()
        self.ftxtBox2_window = self.can.create_window(self.x2, self.y2, window=self.txtBox2)

        try:
            if os.path.exists('./contact/conpact15/contactdoc2.txt'):
                with open('./contact/conpact15/contactdoc2.txt', 'r') as policydoc:
                    docline1 = policydoc.readline()
                    docspecia = policydoc.readline()
                    docphone = policydoc.readline()
                    dociphone2 = policydoc.readline()
                    docstreet = policydoc.readline()
                    docstate = policydoc.readline()
                    docemail = policydoc.readline()
                    docfax = policydoc.readline()
                self.txtBox2.insert(tk.INSERT, "--- Data Doctor 2 ---\n")
                self.txtBox2.insert(tk.END, "\nDoctor : " + docline1)
                self.txtBox2.insert(tk.END, "\nSpecialization : " + docspecia)
                self.txtBox2.insert(tk.END, "\nPhone : " + docphone)
                self.txtBox2.insert(tk.END, "\nMobile : " + dociphone2)
                self.txtBox2.insert(tk.END, "\nStreet : " + docstreet)
                self.txtBox2.insert(tk.END, "\nCity : " + docstate)
                self.txtBox2.insert(tk.END, "\ne-mail : " + docemail)
                self.txtBox2.insert(tk.END, "\nFax : " + docfax)
            else:
                pass
        except FileNotFoundError as err_r3:
            print("+ No file contactdoc2.txt exist (Error4)", err_r3)

        try:
            if os.path.getsize('./contact/conpact15/contactdoc3.txt'):
                print("+ Ok, contactdoc3.txt exist (t3)")
        except FileNotFoundError as nfd3:
            print("+ No file contactdoc3.txt exist (Error5)", nfd3)
            with open('./contact/conpact15/contactdoc3.txt', 'w') as testfd3:
                print("+ File contactdoc3.txt created !", testfd3)

        self.x3, self.y3 = 900, 1410
        self.txtBox3 = tk.Text(self.can, height=17, width=40, font=18, relief=SUNKEN)
        self.txtBox3.delete('1.0', tk.END)
        self.txtBox3.update()
        self.ftxtBox3_window = self.can.create_window(self.x3, self.y3, window=self.txtBox3)

        try:
            if os.path.exists('./contact/conpact15/contactdoc3.txt'):
                with open('./contact/conpact15/contactdoc3.txt', 'r') as policydoc3:
                    doc3line1 = policydoc3.readline()
                    doc3special = policydoc3.readline()
                    doc3phone = policydoc3.readline()
                    doc3iphone2 = policydoc3.readline()
                    doc3street = policydoc3.readline()
                    doc3state = policydoc3.readline()
                    doc3email = policydoc3.readline()
                    doc3fax = policydoc3.readline()
                self.txtBox3.insert(tk.INSERT, "--- Data Doctor 3 ---\n")
                self.txtBox3.insert(tk.END, "\nDoctor : " + doc3line1)
                self.txtBox3.insert(tk.END, "\nSpecialization : " + doc3special)
                self.txtBox3.insert(tk.END, "\nPhone : " + doc3phone)
                self.txtBox3.insert(tk.END, "\nMobile : " + doc3iphone2)
                self.txtBox3.insert(tk.END, "\nStreet : " + doc3street)
                self.txtBox3.insert(tk.END, "\nCity : " + doc3state)
                self.txtBox3.insert(tk.END, "\ne-mail : " + doc3email)
                self.txtBox3.insert(tk.END, "\nFax : " + doc3fax)
            else:
                pass
        except FileNotFoundError as err_r3:
            print("+ No file contactdoc3.txt exist (Error6)", err_r3)

    def recorderData(namentry, txtspec1, specentry1, txtphone,
        phonentry, txtmobile, mobilentry, addrtxt, addrentry,
        citytxt, cityentry, mailtxt, entrymail, faxtxt, entryfax):
        """
            Display origin
        """
        try:
            if os.path.getsize('./contact/conpact15/contactdoc1.txt'):
                print("+ Ok, contactdoc1.txt exist")
        except FileNotFoundError as errfnf:
            print("+ No file contactdoc1.txt exist (Error7)", errfnf)
            with open('./contact/conpact15/contactdoc1.txt', 'w') as testf:
                print("+ File contactdoc1.txt created !")

        try:
            with open('./contact/conpact15/contactdoc1.txt', 'w') as iofile:
                iofile.write(namentry.get())
                iofile.write("\n" + specentry1.get())
                iofile.write("\n" + phonentry.get())
                iofile.write("\n" + mobilentry.get())
                iofile.write("\n" + addrentry.get())
                iofile.write("\n" + cityentry.get())
                iofile.write("\n" + entrymail.get())
                iofile.write("\n" + entryfax.get())
        except FileNotFoundError as fn:
            print("+ File not found !", fn)

        try:
            if os.path.getsize('./contact/conpact15/finaldoc1.txt'):
                os.remove('./contact/conpact15/finaldoc1.txt')
        except FileNotFoundError as err_termin:
            print("+ finaldoc1 not found !(Error8)", err_termin)
            with open('./contact/conpact15/finaldoc1.txt', 'a+'):
                print("+ finaldoc1.txt exist!")
        try:
            with open('./contact/conpact15/finaldoc1.txt', 'w') as terminfile:
                terminfile.write("Doctor : " + namentry.get())
                terminfile.write("\nSpecialization : " + specentry1.get())
                terminfile.write("\nPhone : " + phonentry.get())
                terminfile.write("\nMobile : " + mobilentry.get())
                terminfile.write("\nStreet : " + addrentry.get())
                terminfile.write("\nCity : " + cityentry.get())
                terminfile.write("\ne-mail : " + entrymail.get())
                terminfile.write("\nFax : " + entryfax.get())
        except FileNotFoundError as err2_final:
            print("+ finaldoc1.txt not created (Error9)", err2_final)

        allInData()

    def recorderDoc2(namentry2, txtspec2, specentry2, txtphone2,
        phonentry2, txtmobile2, mobilentry2, addrtxt2, addrentry2,
        citytxt2, cityentry2, mailtxt2, entrymail2, faxtxt2, entryfax2):

        try:
            if os.path.getsize('./contact/conpact15/contactdoc2.txt'):
                print("+ Ok, contactdoc2.txt exist")
        except FileNotFoundError as errfnf2:
            print("+ No file contactdoc2.txt exist (Error10)", errfnf2)
            with open('./contact/conpact15/contactdoc2.txt', 'w') as testf2:
                print("+ File contactdoc2.txt created !", testf2)

        try:
            with open('./contact/conpact15/contactdoc2.txt', 'w') as datadoc:
                datadoc.write(namentry2.get())
                datadoc.write("\n" + specentry2.get())
                datadoc.write("\n" + phonentry2.get())
                datadoc.write("\n" + mobilentry2.get())
                datadoc.write("\n" + addrentry2.get())
                datadoc.write("\n" + cityentry2.get())
                datadoc.write("\n" + entrymail2.get())
                datadoc.write("\n" + entryfax2.get())
        except FileNotFoundError as fn2:
            print("+ File not found !", fn2)

        try:
            if os.path.getsize('./contact/conpact15/finaldoc2.txt'):
                os.remove('./contact/conpact15/finaldoc2.txt')
        except FileNotFoundError as err_termin2:
            print("+ finaldoc2 not found !(Error11)", err_termin2)
            with open('./contact/conpact15/finaldoc2.txt', 'a+'):
                print("+ finaldoc2.txt exist!")
        try:
            with open('./contact/conpact15/finaldoc2.txt', 'w') as finalf:
                finalf.write("Doctor : " + namentry2.get())
                finalf.write("\nSpecialization : " + specentry2.get())
                finalf.write("\nPhone : " + phonentry2.get())
                finalf.write("\nMobile : " + mobilentry2.get())
                finalf.write("\nStreet : " + addrentry2.get())
                finalf.write("\nCity : " + cityentry2.get())
                finalf.write("\ne-mail : " + entrymail2.get())
                finalf.write("\nFax : " + entryfax2.get())
        except FileNotFoundError as err_final2:
            print("+ finaldoc2.txt not created (Error12)", err_final2)

        allInData()

    def recorderDoc3(namentry3, txtspec3, specentry3, txtphone3,
        phonentry3, txtmobile3, mobilentry3, addrtxt3, addrentry3,
        citytxt3, cityentry3, mailtxt3, entrymail3, faxtxt3, entryfax3):

        try:
            if os.path.getsize('./contact/conpact15/contactdoc3.txt'):
                print("+ Ok, contactdoc3.txt exist")
        except FileNotFoundError as errfnf3:
            print("+ No file contactdoc3.txt exist (Error13)", errfnf3)
            with open('./contact/conpact15/contactdoc3.txt', 'w') as testf3:
                print("+ File contactdoc3.txt created !", testf3)

        try:
            with open('./contact/conpact15/contactdoc3.txt', 'w') as datadoc3:
                datadoc3.write(namentry3.get())
                datadoc3.write("\n" + specentry3.get())
                datadoc3.write("\n" + phonentry3.get())
                datadoc3.write("\n" + mobilentry3.get())
                datadoc3.write("\n" + addrentry3.get())
                datadoc3.write("\n" + cityentry3.get())
                datadoc3.write("\n" + entrymail3.get())
                datadoc3.write("\n" + entryfax3.get())
        except FileNotFoundError as fn3:
            print("+ File not found !", fn3)

        try:
            if os.path.getsize('./contact/conpact15/finaldoc3.txt'):
                os.remove('./contact/conpact15/finaldoc3.txt')
        except FileNotFoundError as err_termin3:
            print("+ finaldoc3 not found !(Error14)", err_termin3)
            with open('./contact/conpact15/finaldoc3.txt', 'a+'):
                print("+ finaldoc3.txt exist!")
        try:
            with open('./contact/conpact15/finaldoc3.txt', 'w') as finalf3:
                finalf3.write("Doctor : " + namentry3.get())
                finalf3.write("\nSpecialization : " + specentry3.get())
                finalf3.write("\nPhone : " + phonentry3.get())
                finalf3.write("\nMobile : " + mobilentry3.get())
                finalf3.write("\nStreet : " + addrentry3.get())
                finalf3.write("\nCity : " + cityentry3.get())
                finalf3.write("\ne-mail : " + entrymail3.get())
                finalf3.write("\nFax : " + entryfax3.get())
        except FileNotFoundError as err_final3:
            print("+ finaldoc3.txt not created (Error15)", err_final3)

        allInData()
    # To display all textbox when opening window.
    allInData()

    # Label title
    self.x11, self.y11 = 250, 100
    self.lbltitle = tk.Label(self.can, text="Contact",
        font=('helvetica', 40, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wlbltitle_window = self.can.create_window(self.x11, self.y11,
        window = self.lbltitle)

    # Label title2
    self.x12, self.y12 = 460, 100
    self.labtitle = tk.Label(self.can, text="Doctors",
        font=('Times', 40, 'italic'),
        bg='DodgerBlue2', fg='coral')
    self.wlabtitle_window = self.can.create_window(self.x12, self.y12,
        window = self.labtitle)

    # Doctor 1
    self.x1, self.y1 = 250, 200
    self.labelname = tk.Label(self.can, text="Doctor :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wlabelname_window = self.can.create_window(self.x1, self.y1,
        window = self.labelname)

    try:
        with open('./contact/conpact15/contactdoc1.txt', 'r') as namefile:
            linex = namefile.readline()
            line2 = namefile.readline()
            line3 = namefile.readline()
            line4 = namefile.readline()
            line5 = namefile.readline()
            line6 = namefile.readline()
            line7 = namefile.readline()
            line8 = namefile.readline()
    except FileNotFoundError as callfile:
        print("+ File contactdoc1.txt doesn't exist ! (Error16)", callfile)

    try:
        self.txt_pat = linex
        self.x2, self.y2 = 450, 200
        self.txt_pat = tk.StringVar()
        self.namentry = tk.Entry(self.can, textvariable=self.txt_pat,
            highlightbackground='grey', bd=4)
        self.txt_pat.set(linex[:-1])
        self.wnamentry_window = self.can.create_window(self.x2, self.y2,
            window = self.namentry)
    except UnboundLocalError as ub_error1:
        print("+ File 1 not created ! (Error17)", ub_error1)

    # Specialization
    self.x20, self.y20 = 250, 250
    self.speclab1 = tk.Label(self.can, text="Specialization :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wspeclab1_window = self.can.create_window(self.x20, self.y20,
        window = self.speclab1)

    self.txtspec1 = line2
    self.x21, self.y21 = 450, 250
    self.txtspec1 = tk.StringVar()
    self.specentry1 = tk.Entry(self.can, textvariable=self.txtspec1,
        highlightbackground='grey', bd=3)
    self.txtspec1.set(line2[:-1])
    self.wspecentry1_window = self.can.create_window(self.x21, self.y21,
        window = self.specentry1)

    # Phone
    self.x22, self.y22 = 250, 300
    self.phonelabel = tk.Label(self.can, text="Phone :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wphonelabel_window = self.can.create_window(self.x22, self.y22,
        window = self.phonelabel)

    self.txtphone = line3
    self.x23, self.y23 = 450, 300
    self.txtphone = tk.StringVar()
    self.phonentry = tk.Entry(self.can, textvariable=self.txtphone,
        highlightbackground='grey', bd=3)
    self.txtphone.set(line3[:-1])
    self.wphonentry_window = self.can.create_window(self.x23, self.y23,
        window = self.phonentry)

    # Mobile
    self.x24, self.y24 = 250, 350
    self.lblmobile = tk.Label(self.can, text="Mobile :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wlblmobile_window = self.can.create_window(self.x24, self.y24,
        window = self.lblmobile)

    self.txtmobile = line4
    self.x25, self.y25 = 450, 350
    self.txtmobile = tk.StringVar()
    self.mobilentry = tk.Entry(self.can, textvariable=self.txtmobile,
        highlightbackground='grey', bd=3)
    self.txtmobile.set(line4[:-1])
    self.wmobilentry_window = self.can.create_window(self.x25, self.y25,
        window = self.mobilentry)

    # Street
    self.x30, self.y30 = 250, 400
    self.addrlabel = tk.Label(self.can, text="Street :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.waddrlabel_window = self.can.create_window(self.x30, self.y30,
        window = self.addrlabel)

    self.addrtxt = line5
    self.x31, self.y31 = 450, 400
    self.addrtxt = tk.StringVar()
    self.addrentry = tk.Entry(self.can, textvariable=self.addrtxt,
        highlightbackground='grey', bd=4)
    self.addrtxt.set(line5[:-1])
    self.waddrentry_window = self.can.create_window(self.x31, self.y31,
        window = self.addrentry)

    self.x32, self.y32 = 250, 450
    self.labcity = tk.Label(self.can, text="City :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wlabcity_window = self.can.create_window(self.x32, self.y32,
        window = self.labcity)

    self.citytxt = line6
    self.x33, self.y33 = 450, 450
    self.citytxt = tk.StringVar()
    self.cityentry = tk.Entry(self.can, textvariable=self.citytxt,
        highlightbackground='grey', bd=4)
    self.citytxt.set(line6[:-1])
    self.wcityentry_window = self.can.create_window(self.x33, self.y33,
        window = self.cityentry)

    # e-mail
    self.x40, self.y40 = 250, 500
    self.mailabel = tk.Label(self.can, text="e-mail :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wmailabel_window = self.can.create_window(self.x40, self.y40,
        window = self.mailabel)

    self.mailtxt = line7
    self.x41, self.y41 = 450, 500
    self.mailtxt = tk.StringVar()
    self.entrymail = tk.Entry(self.can, textvariable=self.mailtxt,
        highlightbackground='grey', bd=3)
    self.mailtxt.set(line7[:-1])
    self.wentrymail_window = self.can.create_window(self.x41, self.y41,
        window = self.entrymail)

    # Fax
    self.x50, self.y50 = 250, 550
    self.lblfax = tk.Label(self.can, text="Fax :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wlblfax_window = self.can.create_window(self.x50, self.y50,
        window = self.lblfax)

    self.faxtxt = line8
    self.x51, self.y51 = 450, 550
    self.faxtxt = tk.StringVar()
    self.entryfax = tk.Entry(self.can, textvariable=self.faxtxt,
        highlightbackground='grey', bd=3)
    self.faxtxt.set(line8)
    self.wentryfax_window = self.can.create_window(self.x51, self.y51,
        window = self.entryfax)

    self.x52, self.y52 = 350, 620
    self.b52 = tk.Button(self.can, text="Save Modifications", font=16,
        width=30, bd=3, bg='RoyalBlue3', fg='yellow',
        highlightbackground='cyan',
        activebackground='pale turquoise',
        command = lambda: recorderData(self.namentry, self.txtspec1,
            self.specentry1, self.txtphone, self.phonentry,
            self.txtmobile, self.mobilentry, self.addrtxt,
            self.addrentry, self.citytxt, self.cityentry,
            self.mailtxt, self.entrymail, self.faxtxt, self.entryfax))
    self.fb52_window = self.can.create_window(self.x52, self.y52,
        window=self.b52)

    # Doctor 2
    self.x60, self.y60 = 250, 720
    self.lbldocname = tk.Label(self.can, text="Doctor :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wlbldocname_window = self.can.create_window(self.x60, self.y60,
        window = self.lbldocname)

    try:
        with open('./contact/conpact15/contactdoc2.txt', 'r') as docfile2:
            docline1 = docfile2.readline()
            docline2 = docfile2.readline()
            docline3 = docfile2.readline()
            docline4 = docfile2.readline()
            docline5 = docfile2.readline()
            docline6 = docfile2.readline()
            docline7 = docfile2.readline()
            docline8 = docfile2.readline()
    except FileNotFoundError as callfiledoc2:
        print("+ File contactdoc2.txt doesn't exist ! (Error18)", callfiledoc2)

    try:
        self.txt_doc2 = docline1
        self.x62, self.y62 = 450, 720
        self.txt_doc2 = tk.StringVar()
        self.namentry2 = tk.Entry(self.can, textvariable=self.txt_doc2,
            highlightbackground='grey', bd=4)
        self.txt_doc2.set(docline1[:-1])
        self.wnamentry2_window = self.can.create_window(self.x62, self.y62,
            window = self.namentry2)
    except UnboundLocalError as err_doc2:
        print("+ File 1 not created ! (Error19)", err_doc2)

    # Specialization
    self.x63, self.y63 = 250, 770
    self.speclab2 = tk.Label(self.can, text="Specialization :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wspeclab2_window = self.can.create_window(self.x63, self.y63,
        window = self.speclab2)

    self.txtspec2 = docline2
    self.x64, self.y64 = 450, 770
    self.txtspec2 = tk.StringVar()
    self.specentry2 = tk.Entry(self.can, textvariable=self.txtspec2,
        highlightbackground='grey', bd=3)
    self.txtspec2.set(docline2[:-1])
    self.wspecentry2_window = self.can.create_window(self.x64, self.y64,
        window = self.specentry2)

    # Phone
    self.x65, self.y65 = 250, 820
    self.phonelabel2 = tk.Label(self.can, text="Phone :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wphonelabel2_window = self.can.create_window(self.x65, self.y65,
        window = self.phonelabel2)

    self.txtphone2 = docline3
    self.x66, self.y66 = 450, 820
    self.txtphone2 = tk.StringVar()
    self.phonentry2 = tk.Entry(self.can, textvariable=self.txtphone2,
        highlightbackground='grey', bd=3)
    self.txtphone2.set(docline3[:-1])
    self.wphonentry2_window = self.can.create_window(self.x66, self.y66,
        window = self.phonentry2)

    # Mobile
    self.x67, self.y67 = 250, 870
    self.lblmobile2 = tk.Label(self.can, text="Mobile :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wlblmobile2_window = self.can.create_window(self.x67, self.y67,
        window = self.lblmobile2)

    self.txtmobile2 = docline4
    self.x68, self.y68 = 450, 870
    self.txtmobile2 = tk.StringVar()
    self.mobilentry2 = tk.Entry(self.can, textvariable=self.txtmobile2,
        highlightbackground='grey', bd=3)
    self.txtmobile2.set(docline4[:-1])
    self.wmobilentry2_window = self.can.create_window(self.x68, self.y68,
        window = self.mobilentry2)

    # Street
    self.x69, self.y69 = 250, 920
    self.addrlabel2 = tk.Label(self.can, text="Street :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.waddrlabel2_window = self.can.create_window(self.x69, self.y69,
        window = self.addrlabel2)

    self.addrtxt2 = docline5
    self.x70, self.y70 = 450, 920
    self.addrtxt2 = tk.StringVar()
    self.addrentry2 = tk.Entry(self.can, textvariable=self.addrtxt2,
        highlightbackground='grey', bd=4)
    self.addrtxt2.set(docline5[:-1])
    self.waddrentry2_window = self.can.create_window(self.x70, self.y70,
        window = self.addrentry2)

    self.x71, self.y71 = 250, 970
    self.labcity2 = tk.Label(self.can, text="City :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wlabcity2_window = self.can.create_window(self.x71, self.y71,
        window = self.labcity2)

    self.citytxt2 = docline6
    self.x72, self.y72 = 450, 970
    self.citytxt2 = tk.StringVar()
    self.cityentry2 = tk.Entry(self.can, textvariable=self.citytxt2,
        highlightbackground='grey', bd=4)
    self.citytxt2.set(docline6[:-1])
    self.wcityentry2_window = self.can.create_window(self.x72, self.y72,
        window = self.cityentry2)

    # e-mail
    self.x73, self.y73 = 250, 1020
    self.mailabel2 = tk.Label(self.can, text="e-mail :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wmailabel2_window = self.can.create_window(self.x73, self.y73,
        window = self.mailabel2)

    self.mailtxt2 = docline7
    self.x74, self.y74 = 450, 1020
    self.mailtxt2 = tk.StringVar()
    self.entrymail2 = tk.Entry(self.can, textvariable=self.mailtxt2,
        highlightbackground='grey', bd=3)
    self.mailtxt2.set(docline7[:-1])
    self.wentrymail2_window = self.can.create_window(self.x74, self.y74,
        window = self.entrymail2)

    # Fax
    self.x75, self.y75 = 250, 1070
    self.lblfax2 = tk.Label(self.can, text="Fax :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wlblfax2_window = self.can.create_window(self.x75, self.y75,
        window = self.lblfax2)

    self.faxtxt2 = docline8
    self.x76, self.y76 = 450, 1070
    self.faxtxt2 = tk.StringVar()
    self.entryfax2 = tk.Entry(self.can, textvariable=self.faxtxt2,
        highlightbackground='grey', bd=3)
    self.faxtxt2.set(docline8)
    self.wentryfax2_window = self.can.create_window(self.x76, self.y76,
        window = self.entryfax2)

    self.x77, self.y77 = 350, 1140
    self.bat77 = tk.Button(self.can, text="Save Modifications", font=16,
        width=30, bd=3, bg='RoyalBlue3', fg='yellow',
        highlightbackground='cyan',
        activebackground='pale turquoise',
        command = lambda: recorderDoc2(self.namentry2,
            self.txtspec2, self.specentry2, self.txtphone2,
            self.phonentry2, self.txtmobile2, self.mobilentry2,
            self.addrtxt2, self.addrentry2, self.citytxt2,
            self.cityentry2, self.mailtxt2, self.entrymail2,
            self.faxtxt2, self.entryfax2))
    self.fbat77_window = self.can.create_window(self.x77,
        self.y77, window=self.bat77)

    # Doctor 3
    self.x80, self.y80 = 250, 1240
    self.lbldocname3 = tk.Label(self.can, text="Doctor :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wlbldocname3_window = self.can.create_window(self.x80, self.y80,
        window = self.lbldocname3)

    try:
        with open('./contact/conpact15/contactdoc3.txt', 'r') as docfile3:
            doc3line1 = docfile3.readline()
            doc3line2 = docfile3.readline()
            doc3line3 = docfile3.readline()
            doc3line4 = docfile3.readline()
            doc3line5 = docfile3.readline()
            doc3line6 = docfile3.readline()
            doc3line7 = docfile3.readline()
            doc3line8 = docfile3.readline()
    except FileNotFoundError as callfiledoc3:
        print("+ File contactdoc3.txt doesn't exist ! (Error20)", callfiledoc3)

    try:
        self.txt_doc3 = doc3line1
        self.x81, self.y81 = 450, 1240
        self.txt_doc3 = tk.StringVar()
        self.namentry3 = tk.Entry(self.can, textvariable=self.txt_doc3,
            highlightbackground='grey', bd=4)
        self.txt_doc3.set(doc3line1[:-1])
        self.wnamentry3_window = self.can.create_window(self.x81, self.y81,
            window = self.namentry3)
    except UnboundLocalError as err_doc3:
        print("+ File 1 not created ! (Error21)", err_doc3)

    self.x82, self.y82 = 250, 1290
    self.speclab3 = tk.Label(self.can, text="Specialization :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wspeclab3_window = self.can.create_window(self.x82, self.y82,
        window = self.speclab3)

    self.txtspec3 = doc3line2
    self.x83, self.y83 = 450, 1290
    self.txtspec3 = tk.StringVar()
    self.specentry3 = tk.Entry(self.can, textvariable=self.txtspec3,
        highlightbackground='grey', bd=3)
    self.txtspec3.set(doc3line2[:-1])
    self.wspecentry3_window = self.can.create_window(self.x83, self.y83,
        window = self.specentry3)

    # Phone
    self.x84, self.y84 = 250, 1340
    self.phonelabel3 = tk.Label(self.can, text="Phone :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wphonelabel3_window = self.can.create_window(self.x84, self.y84,
        window = self.phonelabel3)

    self.txtphone3 = doc3line3
    self.x85, self.y85 = 450, 1340
    self.txtphone3 = tk.StringVar()
    self.phonentry3 = tk.Entry(self.can, textvariable=self.txtphone3,
        highlightbackground='grey', bd=3)
    self.txtphone3.set(doc3line3[:-1])
    self.wphonentry3_window = self.can.create_window(self.x85, self.y85,
        window = self.phonentry3)

    # Mobile
    self.x86, self.y86 = 250, 1390
    self.lblmobile3 = tk.Label(self.can, text="Mobile :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wlblmobile3_window = self.can.create_window(self.x86, self.y86,
        window = self.lblmobile3)

    self.txtmobile3 = doc3line4
    self.x87, self.y87 = 450, 1390
    self.txtmobile3 = tk.StringVar()
    self.mobilentry3 = tk.Entry(self.can, textvariable=self.txtmobile3,
        highlightbackground='grey', bd=3)
    self.txtmobile3.set(doc3line4[:-1])
    self.wmobilentry3_window = self.can.create_window(self.x87, self.y87,
        window = self.mobilentry3)

    # Street
    self.x88, self.y88 = 250, 1440
    self.addrlabel3 = tk.Label(self.can, text="Street :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.waddrlabel3_window = self.can.create_window(self.x88, self.y88,
        window = self.addrlabel3)

    self.addrtxt3 = doc3line5
    self.x89, self.y89 = 450, 1440
    self.addrtxt3 = tk.StringVar()
    self.addrentry3 = tk.Entry(self.can, textvariable=self.addrtxt3,
        highlightbackground='grey', bd=4)
    self.addrtxt3.set(doc3line5[:-1])
    self.waddrentry3_window = self.can.create_window(self.x89, self.y89,
        window = self.addrentry3)

    self.x90, self.y90 = 250, 1490
    self.labcity3 = tk.Label(self.can, text="City :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wlabcity3_window = self.can.create_window(self.x90, self.y90,
        window = self.labcity3)

    self.citytxt3 = doc3line6
    self.x91, self.y91 = 450, 1490
    self.citytxt3 = tk.StringVar()
    self.cityentry3 = tk.Entry(self.can, textvariable=self.citytxt3,
        highlightbackground='grey', bd=4)
    self.citytxt3.set(doc3line6[:-1])
    self.wcityentry3_window = self.can.create_window(self.x91, self.y91,
        window = self.cityentry3)

    # e-mail
    self.x92, self.y92 = 250, 1540
    self.mailabel3 = tk.Label(self.can, text="e-mail :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wmailabel3_window = self.can.create_window(self.x92, self.y92,
        window = self.mailabel3)

    self.mailtxt3 = doc3line7
    self.x93, self.y93 = 450, 1540
    self.mailtxt3 = tk.StringVar()
    self.entrymail3 = tk.Entry(self.can, textvariable=self.mailtxt3,
        highlightbackground='grey', bd=3)
    self.mailtxt3.set(doc3line7[:-1])
    self.wentrymail3_window = self.can.create_window(self.x93, self.y93,
        window = self.entrymail3)

    # Fax
    self.x94, self.y94 = 250, 1590
    self.lblfax3 = tk.Label(self.can, text="Fax :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.wlblfax3_window = self.can.create_window(self.x94, self.y94,
        window = self.lblfax3)

    self.faxtxt3 = doc3line8
    self.x95, self.y95 = 450, 1590
    self.faxtxt3 = tk.StringVar()
    self.entryfax3 = tk.Entry(self.can, textvariable=self.faxtxt3,
        highlightbackground='grey', bd=3)
    self.faxtxt3.set(doc3line8)
    self.wentryfax3_window = self.can.create_window(self.x95, self.y95,
        window = self.entryfax3)

    self.x96, self.y96 = 350, 1670
    self.bat96 = tk.Button(self.can, text="Save Modifications", font=16,
        width=30, bd=3, bg='RoyalBlue3', fg='yellow',
        highlightbackground='cyan',
        activebackground='pale turquoise',
        command = lambda: recorderDoc3(self.namentry3,
            self.txtspec3, self.specentry3, self.txtphone3,
            self.phonentry3, self.txtmobile3, self.mobilentry3,
            self.addrtxt3, self.addrentry3, self.citytxt3,
            self.cityentry3, self.mailtxt3, self.entrymail3,
            self.faxtxt3, self.entryfax3))
    self.fbat96_window = self.can.create_window(self.x96, self.y96,
        window=self.bat96)

    self.can.configure(scrollregion=self.can.bbox(ALL))
