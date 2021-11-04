#!/usr/bin/python3
# -*- coding: utf-8 -*-


import tkinter as tk
import os


def recorderData(self, birthvar):
    """
        Display origin
    """
    try:
        with open('./contact/conpact24/contact24.txt', 'w') as iofile:
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
        if os.path.getsize('./contact/conpact24/finalfile24.txt'):
            os.remove('./contact/conpact24/finalfile24.txt')
    except FileNotFoundError as err_termin:
        print("[!] finalfile24.txt not found !(Error_3)", err_termin)
        with open('./contact/conpact24/finalfile24.txt', 'a+'):
            print("[+] File finalfile24.txt created!")

    try:
        with open('./contact/conpact24/finalfile24.txt', 'w') as terminfile:
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
        print("[!] finalfile24.txt not created (Error_4)", err2_final)
