#!/usr/bin/python3
# -*- coding: utf-8 -*-


import tkinter as tk
import os


def funcDoc(self):
    """
        Function called when usr arrived at page doctor contact.
    """
    self.x2, self.y2 = 900, 370
    self.txtBox = tk.Text(self.can, height=17, width=40, font=18,
        relief=tk.SUNKEN)
    self.txtBox.delete('1.0', tk.END)
    self.txtBox.update()
    self.ftxtBox_window = self.can.create_window(self.x2, self.y2,
        window=self.txtBox)

    def numberOneDox(self):
        """
            First textbox of doctor data.
        """
        try:
            if os.path.getsize('./contact/conpact/contactdoc1.txt'):
                print("[+] Ok, contactdoc1.txt exist")
        except FileNotFoundError as errfnf:
            print("[!] File contactdoc1.txt not found (Error7)", errfnf)
            with open('./contact/conpact/contactdoc1.txt', 'w') as testf:
                print("[+] File contactdoc1.txt created !")

        try:
            if os.path.exists('./contact/conpact/contactdoc1.txt'):
                with open('./contact/conpact/contactdoc1.txt', 'r') as policyfile:
                    line1 = policyfile.readline()
                    spec = policyfile.readline()
                    phone = policyfile.readline()
                    iphone2 = policyfile.readline()
                    street = policyfile.readline()
                    state = policyfile.readline()
                    email = policyfile.readline()
                    fax = policyfile.readline()
        except FileNotFoundError as err_r:
            print("[!] File contactdoc1.txt not found (Error_1)", err_r)

        self.txtBox.insert(tk.INSERT, "--- Data Doctor ---\n")
        self.txtBox.insert(tk.END, "\nDoctor : " + line1)
        self.txtBox.insert(tk.END, "\nSpecialization : " + spec)
        self.txtBox.insert(tk.END, "\nPhone : " + phone)
        self.txtBox.insert(tk.END, "\nMobile : " + iphone2)
        self.txtBox.insert(tk.END, "\nStreet : " + street)
        self.txtBox.insert(tk.END, "\nCity : " + state)
        self.txtBox.insert(tk.END, "\ne-mail : " + email)
        self.txtBox.insert(tk.END, "\nFax : " + fax)

    numberOneDox(self)

    self.x3, self.y3 = 900, 890
    self.txtBox2 = tk.Text(self.can, height=17, width=40, font=18, relief=tk.SUNKEN)
    self.txtBox2.delete('1.0', tk.END)
    self.txtBox2.update()
    self.ftxtBox2_window = self.can.create_window(self.x3, self.y3, window=self.txtBox2)

    def numberTwoDox(self):
        """
            Second textbox of doctor data.
        """
        try:
            if os.path.getsize('./contact/conpact/contactdoc2.txt'):
                print("[+] Ok, contactdoc2.txt exist")
        except FileNotFoundError as errfnf2:
            print("[!] File contactdoc2.txt not found (Error10)", errfnf2)
            with open('./contact/conpact/contactdoc2.txt', 'w') as testf2:
                print("[+] File contactdoc2.txt created !", testf2)

        try:
            if os.path.exists('./contact/conpact/contactdoc2.txt'):
                with open('./contact/conpact/contactdoc2.txt', 'r') as policydoc:
                    docline1 = policydoc.readline()
                    docspecia = policydoc.readline()
                    docphone = policydoc.readline()
                    dociphone2 = policydoc.readline()
                    docstreet = policydoc.readline()
                    docstate = policydoc.readline()
                    docemail = policydoc.readline()
                    docfax = policydoc.readline()
        except FileNotFoundError as err_r3:
            print("[!] File contactdoc2.txt not found (Error_2)", err_r3)

        self.txtBox2.insert(tk.INSERT, "--- Data Doctor 2 ---\n")
        self.txtBox2.insert(tk.END, "\nDoctor : " + docline1)
        self.txtBox2.insert(tk.END, "\nSpecialization : " + docspecia)
        self.txtBox2.insert(tk.END, "\nPhone : " + docphone)
        self.txtBox2.insert(tk.END, "\nMobile : " + dociphone2)
        self.txtBox2.insert(tk.END, "\nStreet : " + docstreet)
        self.txtBox2.insert(tk.END, "\nCity : " + docstate)
        self.txtBox2.insert(tk.END, "\ne-mail : " + docemail)
        self.txtBox2.insert(tk.END, "\nFax : " + docfax)

    numberTwoDox(self)

    self.x4, self.y4 = 900, 1410
    self.txtBox3 = tk.Text(self.can, height=17, width=40, font=18, relief=tk.SUNKEN)
    self.txtBox3.delete('1.0', tk.END)
    self.txtBox3.update()
    self.ftxtBox3_window = self.can.create_window(self.x4, self.y4, window=self.txtBox3)

    def numbThreeDox(self):
        """
            Third textbox of doctor data.
        """
        try:
            if os.path.getsize('./contact/conpact/contactdoc3.txt'):
                print("[+] Ok, contactdoc3.txt exist")
        except FileNotFoundError as errfnf3:
            print("[!] File contactdoc3.txt not found (Error13)", errfnf3)
            with open('./contact/conpact/contactdoc3.txt', 'w') as testf3:
                print("[+] File contactdoc3.txt created !", testf3)

        try:
            if os.path.exists('./contact/conpact/contactdoc3.txt'):
                with open('./contact/conpact/contactdoc3.txt', 'r') as policydoc3:
                    doc3line1 = policydoc3.readline()
                    doc3special = policydoc3.readline()
                    doc3phone = policydoc3.readline()
                    doc3iphone2 = policydoc3.readline()
                    doc3street = policydoc3.readline()
                    doc3state = policydoc3.readline()
                    doc3email = policydoc3.readline()
                    doc3fax = policydoc3.readline()
        except FileNotFoundError as err_r3:
            print("[!] File contactdoc3.txt not found (Error_3)", err_r3)

        self.txtBox3.insert(tk.INSERT, "--- Data Doctor 3 ---\n")
        self.txtBox3.insert(tk.END, "\nDoctor : " + doc3line1)
        self.txtBox3.insert(tk.END, "\nSpecialization : " + doc3special)
        self.txtBox3.insert(tk.END, "\nPhone : " + doc3phone)
        self.txtBox3.insert(tk.END, "\nMobile : " + doc3iphone2)
        self.txtBox3.insert(tk.END, "\nStreet : " + doc3street)
        self.txtBox3.insert(tk.END, "\nCity : " + doc3state)
        self.txtBox3.insert(tk.END, "\ne-mail : " + doc3email)
        self.txtBox3.insert(tk.END, "\nFax : " + doc3fax)

    numbThreeDox(self)
