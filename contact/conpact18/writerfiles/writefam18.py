#!/usr/bin/python3
# -*- coding: utf-8 -*-


import tkinter as tk
import os


def recorderFam(self):
    """
        Display origin
    """
    try:
        with open('./contact/conpact18/famycontact18.txt', 'w') as iofile:
            iofile.write(self.namentry.get())
            iofile.write("\n" + self.phonentry.get())
            iofile.write("\n" + self.mobilentry.get())
            iofile.write("\n" + self.addrentry.get())
            iofile.write("\n" + self.cityentry.get())
            iofile.write("\n" + self.entrymail.get())
    except FileNotFoundError as fn:
        print("[!] File famycontact18.txt not found !", fn)

    try:
        if os.path.getsize('./contact/conpact18/finalfam18.txt'):
            os.remove('./contact/conpact18/finalfam18.txt')
    except FileNotFoundError as err_termin:
        print("[!] finalfam18.txt not found !(t2)", err_termin)
        with open('./contact/conpact18/finalfam18.txt', 'a+'):
            print("[+] finalfam18.txt exist!")

    try:
        with open('./contact/conpact18/finalfam18.txt', 'w') as terminfile:
            terminfile.write("Name : " + self.namentry.get())
            terminfile.write("\nPhone : " + self.phonentry.get())
            terminfile.write("\nPhone : " + self.mobilentry.get())
            terminfile.write("\nStreet : " + self.addrentry.get())
            terminfile.write("\nCity : " + self.cityentry.get())
            terminfile.write("\ne-mail : " + self.entrymail.get())
    except FileNotFoundError as err2_final:
        print("[!] finalfam18.txt not created (t2)", err2_final)
