#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
    This script is use to copy treatments
    data into a json file and a text file.
"""


from tkinter import *
import tkinter as tk
import os
import json


def toCopyJsonTreat(self):
    """
        Manage convdose.json file.
    """
    if self.CheckVarMatin.get() == 1:
        matsub = self.Entmatin.get()
    elif self.CheckVarMatin.get() == 0:
        matsub = '---'
    else:
        pass

    if self.CheckVarMidi.get() == 1:
        midsub = self.Entmidi.get()
    elif self.CheckVarMidi.get() == 0:
        midsub = '---'
    else:
        pass

    if self.CheckVarSoir.get() == 1:
        evsub = self.Entsoir.get()
    elif self.CheckVarSoir.get() == 0:
        evsub = '---'
    else:
        pass

    if self.CheckVarNuit.get() == 1:
        nisub = self.Entnuit.get()
    elif self.CheckVarNuit.get() == 0:
        nisub = '---'
    else:
        pass

    try:
        if os.path.getsize('./ttt/doc_ttt11/convdose.json'):
            print("[+] File 'convdose' exist !")
            with open('./ttt/doc_ttt11/convdose.json', 'r') as datafile:
                datastore = json.load(datafile)
                print(datastore)
            dataDose = datastore
            dataDose['data'].append({'Date' : self.textDate.get(),
                'Date of introduction' : self.comboDay.get() + self.comboMonth.get() + \
                self.comboYear.get(), 'Date of end' : self.comboFinishDay.get() + \
                '/' + self.comboFinishMonth.get() + '/' + self.comboFinishYear.get(),
                'Treatment' : self.textTreat.get(), 'Dosage' : self.textDosage.get(),
                'Morning' : matsub,
                'Midday' : midsub,
                'Evening' : evsub,
                'Night' : nisub,
                'Signature' : self.textSign.get()})
            if self.textTreat.get() == "":
                print("\n--- No value 'Treatment' introduced ---\n")
            else:
                print("\n+++ Ok value 'Treatment' introduced +++\n")
                with open('./ttt/doc_ttt11/convdose.json', 'w') as datafile2:
                    json.dump(dataDose, datafile2, indent=4, ensure_ascii=False)
    except FileNotFoundError as fnf:
        print('[!] Sorry, file convdose.json does not exist !', fnf)
        print("[+] File convdose.json created !")
        dataDose = {}
        dataDose['data'] = []
        dataDose['data'].append({'Date' : self.textDate.get(),
            'Date of introduction' : self.comboDay.get() + self.comboMonth.get() + \
            self.comboYear.get(), 'Date of end' : self.comboFinishDay.get() + \
            '/' + self.comboFinishMonth.get() + '/' + self.comboFinishYear.get(),
            'Treatment' : self.textTreat.get(), 'Dosage' : self.textDosage.get(),
            'Morning' : matsub,
            'Midday' : midsub,
            'Evening' : evsub,
            'Night' : nisub,
            'Signature' : self.textSign.get()})
        if self.textTreat.get() == "":
            print("\n--- No value 'Treatment' introduced ---\n")
        else:
            print("\n+++ Ok value 'Treatment' introduced +++\n")
            with open('./ttt/doc_ttt11/convdose.json', 'w') as datafile:
                json.dump(dataDose, datafile, indent=4, ensure_ascii=False)

def copyToTreat(self):
    """
        Write all data into intro_ttt.json
        file to reuse them after.
    """
    with open('./ttt/doc_ttt11/intro_ttt.txt', '+a') as file_ttt:
        file_ttt.write(str("- Register : TREATMENTS -\n"))
        file_ttt.write(str("Date : "))
        file_ttt.write(self.textDate.get() + '\n')
        file_ttt.write(str("Hour : "))
        file_ttt.write(self.textHour.get() + '\n')
        file_ttt.write(str("Name : "))
        file_ttt.write(self.textName.get() + '\n')
        file_ttt.write(str("Date of introduction : "))
        file_ttt.write(self.comboDay.get())
        file_ttt.write(self.comboMonth.get())
        file_ttt.write(self.comboYear.get())
        file_ttt.write(str('\n'))
        file_ttt.write(str("Name of ttt : "))
        file_ttt.write(self.textTreat.get() + '\n')
        file_ttt.write(str("Dosage : "))
        file_ttt.write(self.textDosage.get() + '\n')

        if self.CheckVarMatin.get() == 1:
            file_ttt.write(str("Morning : "))
            file_ttt.write(self.Entmatin.get() + '\n')
        elif self.CheckVarMatin.get() == 0:
            file_ttt.write(str("Morning : ---\n"))
        else:
            pass

        if self.CheckVarMidi.get() == 1:
            file_ttt.write(str("Midday : "))
            file_ttt.write(self.Entmidi.get() + '\n')
        elif self.CheckVarMidi.get() == 0:
            file_ttt.write(str("Midday : ---\n"))
        else:
            pass

        if self.CheckVarSoir.get() == 1:
            file_ttt.write(str("Evening : "))
            file_ttt.write(self.Entsoir.get() + '\n')
        elif self.CheckVarSoir.get() == 0:
            file_ttt.write(str("Evening : ---\n"))
        else:
            pass

        if self.CheckVarNuit.get() == 1:
            file_ttt.write(str("Night : "))
            file_ttt.write(self.Entnuit.get() + '\n')
        elif self.CheckVarNuit.get() == 0:
            file_ttt.write(str("Night : ---\n"))
        else:
            pass

        file_ttt.write(str("Date of end : "))
        file_ttt.write(self.comboFinishDay.get())
        file_ttt.write('/' + self.comboFinishMonth.get() + '/')
        file_ttt.write(self.comboFinishYear.get())
        file_ttt.write(str('\n'))
        file_ttt.write(str("Signature : "))
        file_ttt.write(self.textSign.get())
        file_ttt.write(str('\n\n'))
