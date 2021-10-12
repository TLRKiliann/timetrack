#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
    This script is use to copy reserves
    data into a json file and a text file.
"""


from tkinter import *
import tkinter as tk
import os
import json


def copyToReserve(self):
    """
        Write all data into intro_res.txt
    """
    with open('./ttt/doc_ttt22/intro_res.txt', '+a') as file_res:
        file_res.write(str("- Register : RESERVES -\n"))
        file_res.write(str("Date : "))
        file_res.write(self.textDate.get() + '\n')
        file_res.write(str("Hour : "))
        file_res.write(self.textHour.get() + '\n')
        file_res.write(str("Name : "))
        file_res.write(self.textName.get() + '\n')
        file_res.write(str("Date of introduction : "))
        file_res.write(self.comboDay.get())
        file_res.write(self.comboMonth.get())
        file_res.write(self.comboYear.get())
        file_res.write(str('\n'))
        file_res.write(str("Name of Reserve : "))
        file_res.write(self.textTreat.get() + '\n')
        file_res.write(str("Dosage : "))
        file_res.write(self.textDosage.get() + '\n')

        if self.CheckVar1.get() == 1:
            file_res.write(str("Reserve : "))
            file_res.write(str("yes\n"))
        elif self.CheckVar1.get() == 0:
            file_res.write(str("Reserve : "))
            file_res.write(str("no\n"))
        else:
            pass

        if self.CheckVar2.get() == 1:
            file_res.write(str("First-line : "))
            file_res.write(str("yes\n"))
        elif self.CheckVar2.get() == 0:
            file_res.write(str("First-line : "))
            file_res.write(str("no\n"))
        else:
            pass

        if self.CheckVar3.get() == 1:
            file_res.write(str("Second-line : "))
            file_res.write(str("yes\n"))
        elif self.CheckVar3.get() == 0:
            file_res.write(str("Second-line : "))
            file_res.write(str("no\n"))
        else:
            pass

        if self.Rnbre.get() == '':
            print("[!] Number per 24h not defined !")
        else:
            file_res.write(str("Number/24h : "))
            file_res.write(self.Rnbre.get() + '\n')
        if self.entreason.get() == '':
            print("[!] Reason is not defined !")
        else:
            file_res.write(str("Reason : "))
            file_res.write(self.entreason.get() + '\n')

        file_res.write(str("Date of end : "))
        file_res.write(self.comboFinishDay.get())
        file_res.write('/' + self.comboFinishMonth.get() + '/')
        file_res.write(self.comboFinishYear.get())
        file_res.write(str('\n'))
        file_res.write(str("Signature : "))
        file_res.write(self.textSign.get())
        file_res.write(str('\n\n'))

def toCopyJsonRes(self):
    """
        Manage convres.json file.
    """
    try:
        if os.path.getsize('./ttt/doc_ttt22/convres.json'):
            print("[+] File 'convres' exist !")
            with open('./ttt/doc_ttt22/convres.json', 'r') as datafile:
                datastore = json.load(datafile)
                print(datastore)
            dataDose = datastore
            dataDose['data'].append({'Date' : self.textDate.get(),
                'Date of introduction' : self.comboDay.get() + self.comboMonth.get() + \
                self.comboYear.get(), 'Date of end' : self.comboFinishDay.get() + \
                '/' + self.comboFinishMonth.get() + '/' + self.comboFinishYear.get(),
                'Treatment' : self.textTreat.get(), 'Dosage' : self.textDosage.get(),
                'Reserve' : self.CheckVar1.get(), 'First-line' : self.CheckVar2.get(),
                'Second-line' : self.CheckVar3.get(), 'Number/24h' : self.Rnbre.get(),
                'Reason' : self.entreason.get(), 'Signature' : self.textSign.get()})
            if self.textTreat.get() == "":
                print("\n--- No value 'Reserve' introduced ---\n")
            else:
                print("\n+++ Ok value 'Reserve' introduced +++\n")
                with open('./ttt/doc_ttt22/convres.json', 'w') as datafile2:
                    json.dump(dataDose, datafile2, indent=4, ensure_ascii=False)
    except FileNotFoundError as outcom:
        print('[!] Sorry, file convres.json does not exist !', outcom)
        print("[+] File convres.json created !")
        dataDose = {}
        dataDose['data'] = []
        dataDose['data'].append({'Date' : self.textDate.get(),
            'Date of introduction' : self.comboDay.get() + self.comboMonth.get() + \
            self.comboYear.get(), 'Date of end' : self.comboFinishDay.get() + \
            '/' + self.comboFinishMonth.get() + '/' + self.comboFinishYear.get(),
            'Treatment' : self.textTreat.get(), 'Dosage' : self.textDosage.get(),
            'Reserve' : self.CheckVar1.get(), 'First-line' : self.CheckVar2.get(),
            'Second-line' : self.CheckVar3.get(), 'Number/24h' : self.Rnbre.get(),
            'Reason' : self.entreason.get(), 'Signature' : self.textSign.get()})
        if self.textTreat.get() == "":
            print("[!] No value 'Treatment' introduced !")
        elif self.CheckVar2.get() == 0:
            print("[!] No First-line marked for reserve!")
        elif self.CheckVar2.get() != 0:
            print("[+] First-line reserve marked !")
        elif self.CheckVar3.get() == 0:
            print("[!] No Second-line marked for reserve !")
        elif self.CheckVar3.get() != 0:
            print("[+] Second-line reserve marked !")
        else:
            print("\n[!] Problem with 'Reserve' registration [!]\n")
        print("\n+++ Ok, value 'Reserve' introduced +++\n")
        with open('./ttt/doc_ttt22/convres.json', 'w') as datafile:
            json.dump(dataDose, datafile, indent=4, ensure_ascii=False)
