#!/usr/bin/python3
# -*- coding: utf-8 -*-


from tkinter import *
import tkinter as tk
from tkinter import messagebox
import os
import time
import json
from ttt.uploadtreat.t_upload10 import tttupload


def writeStopTtt(self):
    """
        Write date of end when usr click on stop ttt.
    """
    try:
        word_ttt = "\nName of ttt : " + self.deleteTreat.get()
        dose_insert = self.deltttdose.get()
        with open('./ttt/doc_ttt10/stopped_ttt.txt', 'a+') as file_stopttt:
            file_stopttt.write(word_ttt + " " + dose_insert + " - stopped on : " + \
                time.strftime("%d/%m/%Y"))
    except OSError as infof_out:
        print("[Err_delttt] Found error : ", infof_out)
    print("[+] No error, file stopped_ttt.txt will be upload to server !")
    tttupload()

def delTreatment(self):
    """
        Stop all data of ttt choosen.
    """
    try:
        if os.path.getsize('./ttt/doc_ttt10/convdose.json'):
            print("[+] File 'convdose' exist !")
            with open('./ttt/doc_ttt10/convdose.json', 'r') as datafile:
                datadel = json.load(datafile)

            dataDose = datadel
            for key, value in dataDose.items():
                if self.deleteTreat.get() == value[0]['Treatment'] and \
                    self.deltttdose.get() == value[0]['Dosage']:
                    del value[0]

                elif self.deleteTreat.get() == value[1]['Treatment'] and \
                    self.deltttdose.get() == value[1]['Dosage']:
                    del value[1]

                elif self.deleteTreat.get() == value[2]['Treatment'] and \
                    self.deltttdose.get() == value[2]['Dosage']:
                    del value[2]

                elif self.deleteTreat.get() == value[3]['Treatment'] and \
                    self.deltttdose.get() == value[3]['Dosage']:
                    del value[3]

                elif self.deleteTreat.get() == value[4]['Treatment'] and \
                    self.deltttdose.get() == value[4]['Dosage']:
                    del value[4]

                elif self.deleteTreat.get() == value[5]['Treatment'] and \
                    self.deltttdose.get() == value[5]['Dosage']:
                    del value[5]

                elif self.deleteTreat.get() == value[6]['Treatment'] and \
                    self.deltttdose.get() == value[6]['Dosage']:
                    del value[6]

                elif self.deleteTreat.get() == value[7]['Treatment'] and \
                    self.deltttdose.get() == value[7]['Dosage']:
                    del value[7]

                elif self.deleteTreat.get() == value[8]['Treatment'] and \
                    self.deltttdose.get() == value[8]['Dosage']:
                    del value[8]

                elif self.deleteTreat.get() == value[9]['Treatment'] and \
                    self.deltttdose.get() == value[9]['Dosage']:
                    del value[9]

                elif self.deleteTreat.get() == value[10]['Treatment'] and \
                    self.deltttdose.get() == value[10]['Dosage']:
                    del value[10]

                elif self.deleteTreat.get() == value[11]['Treatment'] and \
                    self.deltttdose.get() == value[11]['Dosage']:
                    del value[11]

                elif self.deleteTreat.get() == value[12]['Treatment'] and \
                    self.deltttdose.get() == value[12]['Dosage']:
                    del value[12]

                elif self.deleteTreat.get() == value[13]['Treatment'] and \
                    self.deltttdose.get() == value[13]['Dosage']:
                    del value[13]

                elif self.deleteTreat.get() == value[14]['Treatment'] and \
                    self.deltttdose.get() == value[14]['Dosage']:
                    del value[14]

                print("+++ Ok 'TREATMENT' stopped +++")
                with open('./ttt/doc_ttt10/convdose.json', 'w') as datafile2:
                    json.dump(dataDose, datafile2, indent=4)

    except FileNotFoundError as fnfe:
        print('[!] Sorry, file convdose.json does not exist !', fnfe)
        messagebox.showerror('Error', 'File convdose.json does not exist !')

def stopTreatment(self):
    """
        Search Date of end and write value of the date of today,
        when usr click on <stop ttt> button.
    """
    MSBask = messagebox.askyesno('Delete ttt', 'Are you sure to delete it ?')
    if MSBask == 1:
        try:
            if os.path.getsize('./ttt/doc_ttt10/intro_ts.txt'):
                print("[+] File intro_ts.txt exist (2)!")
        except FileNotFoundError as no_finit:
            print("[!] File intro_ts.txt doesn't exist (2)!")
            with open('./ttt/doc_ttt10/intro_ts.txt', 'a+') as creat_f:
                creat_f.write(str("Stopped ttt :"))

        try:
            if os.path.getsize('./ttt/doc_ttt10/convdose.json'):
                print("[+] File 'convdose' exist !")
                with open('./ttt/doc_ttt10/convdose.json', 'r') as datafile:
                    datastore = json.load(datafile)

                dataDose = datastore
                for key, value in dataDose.items():
                    if self.deleteTreat.get() == value[0]['Treatment'] and \
                        self.deltttdose.get() == value[0]['Dosage']:
                        value[0]["Date of end"] = time.strftime("%d/%m/%Y")
                        with open('./ttt/doc_ttt10/intro_ts.txt', 'a+') as file_j:
                            json.dump(value[0], file_j, indent=4)

                    elif self.deleteTreat.get() == value[1]['Treatment'] and \
                        self.deltttdose.get() == value[1]['Dosage']:
                        value[1]["Date of end"] = time.strftime("%d/%m/%Y")
                        with open('./ttt/doc_ttt10/intro_ts.txt', 'a+') as file_j:
                            json.dump(value[1], file_j, indent=4)

                    elif self.deleteTreat.get() == value[2]['Treatment'] and \
                        self.deltttdose.get() == value[2]['Dosage']:
                        value[2]["Date of end"] = time.strftime("%d/%m/%Y")
                        with open('./ttt/doc_ttt10/intro_ts.txt', 'a+') as file_j:
                            json.dump(value[2], file_j, indent=4)

                    elif self.deleteTreat.get() == value[3]['Treatment'] and \
                        self.deltttdose.get() == value[3]['Dosage']:
                        value[3]["Date of end"] = time.strftime("%d/%m/%Y")
                        with open('./ttt/doc_ttt10/intro_ts.txt', 'a+') as file_j:
                            json.dump(value[3], file_j, indent=4)

                    elif self.deleteTreat.get() == value[4]['Treatment'] and \
                        self.deltttdose.get() == value[4]['Dosage']:
                        value[4]["Date of end"] = time.strftime("%d/%m/%Y")
                        with open('./ttt/doc_ttt10/intro_ts.txt', 'a+') as file_j:
                            json.dump(value[4], file_j, indent=4)

                    elif self.deleteTreat.get() == value[5]['Treatment'] and \
                        self.deltttdose.get() == value[5]['Dosage']:
                        value[5]["Date of end"] = time.strftime("%d/%m/%Y")
                        with open('./ttt/doc_ttt10/intro_ts.txt', 'a+') as file_j:
                            json.dump(value[5], file_j, indent=4)

                    elif self.deleteTreat.get() == value[6]['Treatment'] and \
                        self.deltttdose.get() == value[6]['Dosage']:
                        value[6]["Date of end"] = time.strftime("%d/%m/%Y")
                        with open('./ttt/doc_ttt10/intro_ts.txt', 'a+') as file_j:
                            json.dump(value[6], file_j, indent=4)

                    elif self.deleteTreat.get() == value[7]['Treatment'] and \
                        self.deltttdose.get() == value[7]['Dosage']:
                        value[7]["Date of end"] = time.strftime("%d/%m/%Y")
                        with open('./ttt/doc_ttt10/intro_ts.txt', 'a+') as file_j:
                            json.dump(value[7], file_j, indent=4)

                    elif self.deleteTreat.get() == value[8]['Treatment'] and \
                        self.deltttdose.get() == value[8]['Dosage']:
                        value[8]["Date of end"] = time.strftime("%d/%m/%Y")
                        with open('./ttt/doc_ttt10/intro_ts.txt', 'a+') as file_j:
                            json.dump(value[8], file_j, indent=4)

                    elif self.deleteTreat.get() == value[9]['Treatment'] and \
                        self.deltttdose.get() == value[9]['Dosage']:
                        value[9]["Date of end"] = time.strftime("%d/%m/%Y")
                        with open('./ttt/doc_ttt10/intro_ts.txt', 'a+') as file_j:
                            json.dump(value[9], file_j, indent=4)

                    elif self.deleteTreat.get() == value[10]['Treatment'] and \
                        self.deltttdose.get() == value[10]['Dosage']:
                        value[10]["Date of end"] = time.strftime("%d/%m/%Y")
                        with open('./ttt/doc_ttt10/intro_ts.txt', 'a+') as file_j:
                            json.dump(value[10], file_j, indent=4)

                    elif self.deleteTreat.get() == value[11]['Treatment'] and \
                        self.deltttdose.get() == value[11]['Dosage']:
                        value[11]["Date of end"] = time.strftime("%d/%m/%Y")
                        with open('./ttt/doc_ttt10/intro_ts.txt', 'a+') as file_j:
                            json.dump(value[11], file_j, indent=4)

                    elif self.deleteTreat.get() == value[12]['Treatment'] and \
                        self.deltttdose.get() == value[12]['Dosage']:
                        value[12]["Date of end"] = time.strftime("%d/%m/%Y")
                        with open('./ttt/doc_ttt10/intro_ts.txt', 'a+') as file_j:
                            json.dump(value[12], file_j, indent=4)

                    elif self.deleteTreat.get() == value[13]['Treatment'] and \
                        self.deltttdose.get() == value[13]['Dosage']:
                        value[13]["Date of end"] = time.strftime("%d/%m/%Y")
                        with open('./ttt/doc_ttt10/intro_ts.txt', 'a+') as file_j:
                            json.dump(value[13], file_j, indent=4)

                    elif self.deleteTreat.get() == value[14]['Treatment'] and \
                        self.deltttdose.get() == value[14]['Dosage']:
                        value[14]["Date of end"] = time.strftime("%d/%m/%Y")
                        with open('./ttt/doc_ttt10/intro_ts.txt', 'a+') as file_j:
                            json.dump(value[14], file_j, indent=4)

                    print("+++ Ok 'TREATMENT' stopped +++")
                    with open('./ttt/doc_ttt10/convdose.json', 'w') as dataft:
                        json.dump(dataDose, dataft, indent=4)

                    delTreatment(self)
                    writeStopTtt(self)

        except FileNotFoundError as fnfe:
            print('[!] Sorry, file convdose.json does not exist !', fnfe)
            messagebox.showerror('Error', 'File convdose.json does not exist !')
        except IndexError as ittt_err:
            print('[!] Sorry, treatment is not present into medication !', ittt_err)
            messagebox.showerror('Error', 'Treatment is not present into medication !')
    else:
        messagebox.showinfo('Return', 'Treatment has not been earased.')
