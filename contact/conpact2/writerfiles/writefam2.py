#!/usr/bin/python3
# -*- coding: utf-8 -*-


import tkinter as tk
import os


def recorderFam(self):
    """
        Display origin
    """
    try:
        if os.path.getsize('./contact/conpact2/famycontact2.txt'):
            print("[+] Ok, famycontact2.txt exist (t2)")
    except FileNotFoundError as err_fnf:
        print("[!] No file famycontact2.txt exist", err_fnf)
        with open('./contact/conpact2/famycontact2.txt', 'w') as testf:
            print("[+] File famycontact2.txt created !")

    try:
        with open('./contact/conpact2/famycontact2.txt', 'w') as iofile:
            iofile.write(self.namentry.get())
            iofile.write("\n" + self.phonentry.get())
            iofile.write("\n" + self.mobilentry.get())
            iofile.write("\n" + self.addrentry.get())
            iofile.write("\n" + self.cityentry.get())
            iofile.write("\n" + self.entrymail.get())
    except FileNotFoundError as fn:
        print("[!] File famycontact2.txt not found !", fn)

    try:
        if os.path.getsize('./contact/conpact2/finalfam2.txt'):
            os.remove('./contact/conpact2/finalfam2.txt')
    except FileNotFoundError as err_termin:
        print("[!] finalfam1 not found !(t2)", err_termin)
        with open('./contact/conpact2/finalfam2.txt', 'a+'):
            print("[+] finalfam2.txt exist!")

    try:
        with open('./contact/conpact2/finalfam2.txt', 'w') as terminfile:
            terminfile.write("Name : " + self.namentry.get())
            terminfile.write("\nPhone : " + self.phonentry.get())
            terminfile.write("\nPhone : " + self.mobilentry.get())
            terminfile.write("\nStreet : " + self.addrentry.get())
            terminfile.write("\nCity : " + self.cityentry.get())
            terminfile.write("\ne-mail : " + self.entrymail.get())
    except FileNotFoundError as err2_final:
        print("[!] finalfam2.txt not created (t2)", err2_final)
