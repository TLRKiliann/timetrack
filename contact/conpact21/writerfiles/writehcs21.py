#!/usr/bin/python3
# -*- coding: utf-8 -*-


import tkinter as tk
import os


def careOneRec(self):
    """
        Display origin
    """
    try:
        with open('./contact/conpact21/hcscontact1.txt', 'w') as iofile:
            iofile.write(self.namentry.get())
            iofile.write("\n" + self.phonentry.get())
            iofile.write("\n" + self.mobilentry.get())
            iofile.write("\n" + self.addrentry.get())
            iofile.write("\n" + self.cityentry.get())
            iofile.write("\n" + self.entrymail.get())
    except FileNotFoundError as err_fnfe:
        print("[!] File hcscontact1.txt not found (Error_7) !", err_fnfe)

    try:
        if os.path.getsize('./contact/conpact21/finalhcs1.txt'):
            os.remove('./contact/conpact21/finalhcs1.txt')
    except FileNotFoundError as err_termin:
        print("[!] finalhcs1 not found (Error_8) !", err_termin)
        with open('./contact/conpact21/finalhcs1.txt', 'a+'):
            print("[+] finalhcs1.txt exist !")

    try:
        with open('./contact/conpact21/finalhcs1.txt', 'w') as terminfile:
            terminfile.write("Name : " + self.namentry.get())
            terminfile.write("\nPhone : " + self.phonentry.get())
            terminfile.write("\nPhone : " + self.mobilentry.get())
            terminfile.write("\nStreet : " + self.addrentry.get())
            terminfile.write("\nCity : " + self.cityentry.get())
            terminfile.write("\ne-mail : " + self.entrymail.get())
    except FileNotFoundError as err2_final:
        print("[!] finalhcs1.txt not created (Error_9) !", err2_final)

def careTwoRec(self):
    """
        Display origin
    """
    try:
        with open('./contact/conpact21/hcscontact2.txt', 'w') as copyfile:
            copyfile.write(self.name_twoentry.get())
            copyfile.write("\n" + self.twophonentry.get())
            copyfile.write("\n" + self.mobile_toentry.get())
            copyfile.write("\n" + self.addr_twoentry.get())
            copyfile.write("\n" + self.city_twoentry.get())
            copyfile.write("\n" + self.entry_twomail.get())
    except FileNotFoundError as fn:
        print("[!] File not found (Error_11) !", fn)

    try:
        if os.path.getsize('./contact/conpact21/finalhcs2.txt'):
            os.remove('./contact/conpact21/finalhcs2.txt')
    except FileNotFoundError as err_termin:
        print("[!] finalhcs2 not found (Error_12) !", err_termin)
        with open('./contact/conpact21/finalhcs2.txt', 'a+'):
            print("[+] finalhcs2.txt exist!")

    try:
        with open('./contact/conpact21/finalhcs2.txt', 'w') as secterfile:
            secterfile.write("Name : " + self.name_twoentry.get())
            secterfile.write("\nPhone : " + self.twophonentry.get())
            secterfile.write("\nPhone : " + self.mobile_toentry.get())
            secterfile.write("\nStreet : " + self.addr_twoentry.get())
            secterfile.write("\nCity : " + self.city_twoentry.get())
            secterfile.write("\ne-mail : " + self.entry_twomail.get())
    except FileNotFoundError as err2_final:
        print("[!] finalhcs2.txt not created (Error_13) !", err2_final)

def careThreeRec(self):
    """
        Display origin
    """
    try:
        with open('./contact/conpact21/hcscontact3.txt', 'w') as copyfile:
            copyfile.write(self.name_thirdentry.get())
            copyfile.write("\n" + self.thirdphonentry.get())
            copyfile.write("\n" + self.mobile_thirdentry.get())
            copyfile.write("\n" + self.addr_thirdentry.get())
            copyfile.write("\n" + self.city_thirdentry.get())
            copyfile.write("\n" + self.entry_thirdmail.get())
    except FileNotFoundError as err_hcs3:
        print("[!] File not found (Error_15) !", err_hcs3)

    try:
        if os.path.getsize('./contact/conpact21/finalhcs3.txt'):
            os.remove('./contact/conpact21/finalhcs3.txt')
    except FileNotFoundError as err_termin:
        print("[!] finalhcs3 not found (Error_16) !", err_termin)
        with open('./contact/conpact21/finalhcs3.txt', 'a+'):
            print("[+] finalhcs3.txt exist!")

    try:
        with open('./contact/conpact21/finalhcs3.txt', 'w') as secterfile:
            secterfile.write("Name : " + self.name_thirdentry.get())
            secterfile.write("\nPhone : " + self.thirdphonentry.get())
            secterfile.write("\nPhone : " + self.mobile_thirdentry.get())
            secterfile.write("\nStreet : " + self.addr_thirdentry.get())
            secterfile.write("\nCity : " + self.city_thirdentry.get())
            secterfile.write("\ne-mail : " + self.entry_thirdmail.get())
    except FileNotFoundError as err2_final3:
        print("[!] finalhcs3.txt not created (Error_17) !", err2_final3)
