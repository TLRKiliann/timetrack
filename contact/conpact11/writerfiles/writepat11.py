#!/usr/bin/python3
# -*- coding: utf-8 -*-


import tkinter as tk
import os


def recorderData(self, birthvar):
    """
        Display origin
    """
    try:
        if os.path.getsize('./contact/conpact11/contact11.txt'):
            print("[+] Ok, contact11.txt exist")
    except FileNotFoundError as errfnf:
        print("[!] File contact11.txt doesn't exist (Error2)", errfnf)
        with open('./contact/conpact11/contact11.txt', 'w') as testf:
            print("[+] File contact11.txt created !")

    try:
        with open('./contact/conpact11/contact11.txt', 'w') as iofile:
            iofile.write(self.namentry.get())
            iofile.write("\n" + birthvar)
            iofile.write("\n" + self.nativaentry.get())
            iofile.write("\n" + self.phonentry.get())
            iofile.write("\n" + self.addrentry.get())
            iofile.write("\n" + self.cityentry.get())
            iofile.write("\n" + self.entrymail.get())
            iofile.write("\n" + self.entryassu.get())
            iofile.write("\n" + self.entrypolicy.get())
            iofile.write("\n" + self.entrycivil.get())
            iofile.write("\n" + self.entryconfess.get())
    except FileNotFoundError as fn:
        print("[!] File not found !", fn)

    try:
        if os.path.getsize('./contact/conpact11/finalfile11.txt'):
            os.remove('./contact/conpact11/finalfile11.txt')
    except FileNotFoundError as err_termin:
        print("[!] finalfile11.txt not found !(Error3)", err_termin)
        with open('./contact/conpact11/finalfile11.txt', 'a+'):
            print("[+] File finalfile11.txt exist!")

    try:
        with open('./contact/conpact11/finalfile11.txt', 'w') as terminfile:
            terminfile.write("Patient name : " + self.namentry.get())
            terminfile.write("\nBirthdate : " + birthvar)
            terminfile.write("\nNative : " + self.nativaentry.get())
            terminfile.write("\nPhone : " + self.phonentry.get())
            terminfile.write("\nStreet : " + self.addrentry.get())
            terminfile.write("\nCity : " + self.cityentry.get())
            terminfile.write("\ne-mail : " + self.entrymail.get())
            terminfile.write("\nInsurance : " + self.entryassu.get())
            terminfile.write("\nPolicy : " + self.entrypolicy.get())
            terminfile.write("\nCivil status : " + self.entrycivil.get())
            terminfile.write("\nConfession : " + self.entryconfess.get())
    except FileNotFoundError as err2_final:
        print("[!] finalfile11.txt not created (Error4)", err2_final)
