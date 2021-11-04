#!/usr/bin/python3
# -*- coding: utf-8 -*-


import tkinter as tk
import os


def docRecord(self):
    """
        Display origin
    """
    try:
        with open('./contact/conpact17/contactdoc1.txt', 'w') as iofile:
            iofile.write(self.namentry.get())
            iofile.write("\n" + self.specentry1.get())
            iofile.write("\n" + self.phonentry.get())
            iofile.write("\n" + self.mobilentry.get())
            iofile.write("\n" + self.addrentry.get())
            iofile.write("\n" + self.cityentry.get())
            iofile.write("\n" + self.entrymail.get())
            iofile.write("\n" + self.entryfax.get())
    except FileNotFoundError as fn:
        print("[!] File contactdoc1.txt not found !", fn)

    try:
        if os.path.getsize('./contact/conpact17/finaldoc1.txt'):
            os.remove('./contact/conpact17/finaldoc1.txt')
    except FileNotFoundError as err_termin:
        print("[!] finaldoc1 not found (Error_1)", err_termin)
        with open('./contact/conpact17/finaldoc1.txt', 'a+'):
            print("[+] finaldoc1.txt created!")

    try:
        with open('./contact/conpact17/finaldoc1.txt', 'w') as terminfile:
            terminfile.write("Doctor : " + self.namentry.get())
            terminfile.write("\nSpecialization : " + self.specentry1.get())
            terminfile.write("\nPhone : " + self.phonentry.get())
            terminfile.write("\nMobile : " + self.mobilentry.get())
            terminfile.write("\nStreet : " + self.addrentry.get())
            terminfile.write("\nCity : " + self.cityentry.get())
            terminfile.write("\ne-mail : " + self.entrymail.get())
            terminfile.write("\nFax : " + self.entryfax.get())
    except FileNotFoundError as err2_final:
        print("[!] finaldoc1.txt not created (Error_2)", err2_final)

def docTwoRecord(self):
    try:
        with open('./contact/conpact17/contactdoc2.txt', 'w') as datadoc:
            datadoc.write(self.namentry2.get())
            datadoc.write("\n" + self.specentry2.get())
            datadoc.write("\n" + self.phonentry2.get())
            datadoc.write("\n" + self.mobilentry2.get())
            datadoc.write("\n" + self.addrentry2.get())
            datadoc.write("\n" + self.cityentry2.get())
            datadoc.write("\n" + self.entrymail2.get())
            datadoc.write("\n" + self.entryfax2.get())
    except FileNotFoundError as fn2:
        print("[!] File contactdoc2.txt not found (Error_3)!", fn2)

    try:
        if os.path.getsize('./contact/conpact17/finaldoc2.txt'):
            os.remove('./contact/conpact17/finaldoc2.txt')
    except FileNotFoundError as err_termin2:
        print("[!] finaldoc2 not found !(Error_4)", err_termin2)
        with open('./contact/conpact17/finaldoc2.txt', 'a+'):
            print("[+] finaldoc2.txt created!")

    try:
        with open('./contact/conpact17/finaldoc2.txt', 'w') as finalf:
            finalf.write("Doctor : " + self.namentry2.get())
            finalf.write("\nSpecialization : " + self.specentry2.get())
            finalf.write("\nPhone : " + self.phonentry2.get())
            finalf.write("\nMobile : " + self.mobilentry2.get())
            finalf.write("\nStreet : " + self.addrentry2.get())
            finalf.write("\nCity : " + self.cityentry2.get())
            finalf.write("\ne-mail : " + self.entrymail2.get())
            finalf.write("\nFax : " + self.entryfax2.get())
    except FileNotFoundError as err_final2:
        print("[!] finaldoc2.txt not created (Error_5)", err_final2)

def docThreeRecord(self):
    try:
        with open('./contact/conpact17/contactdoc3.txt', 'w') as datadoc3:
            datadoc3.write(self.namentry3.get())
            datadoc3.write("\n" + self.specentry3.get())
            datadoc3.write("\n" + self.phonentry3.get())
            datadoc3.write("\n" + self.mobilentry3.get())
            datadoc3.write("\n" + self.addrentry3.get())
            datadoc3.write("\n" + self.cityentry3.get())
            datadoc3.write("\n" + self.entrymail3.get())
            datadoc3.write("\n" + self.entryfax3.get())
    except FileNotFoundError as fn3:
        print("[!] File contactdoc3.txt not found (Error_6)", fn3)

    try:
        if os.path.getsize('./contact/conpact17/finaldoc3.txt'):
            os.remove('./contact/conpact17/finaldoc3.txt')
    except FileNotFoundError as err_termin3:
        print("[!] File finaldoc3 not found (Error_7)", err_termin3)
        with open('./contact/conpact17/finaldoc3.txt', 'a+'):
            print("[+] File finaldoc3.txt created !")

    try:
        with open('./contact/conpact17/finaldoc3.txt', 'w') as finalf3:
            finalf3.write("Doctor : " + self.namentry3.get())
            finalf3.write("\nSpecialization : " + self.specentry3.get())
            finalf3.write("\nPhone : " + self.phonentry3.get())
            finalf3.write("\nMobile : " + self.mobilentry3.get())
            finalf3.write("\nStreet : " + self.addrentry3.get())
            finalf3.write("\nCity : " + self.cityentry3.get())
            finalf3.write("\ne-mail : " + self.entrymail3.get())
            finalf3.write("\nFax : " + self.entryfax3.get())
    except FileNotFoundError as err_final3:
        print("[!] finaldoc3.txt not created (Error_8)", err_final3)
