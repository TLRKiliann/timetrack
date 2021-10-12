#!/usr/bin/python3
# -*- coding: utf-8 -*-


from tkinter import *
import tkinter as tk
from tkinter import messagebox
import os
import time
import json
from ttt.uploadres.r_upload11 import resupload


def writeStoppedRes(self):
    """
        Write date of end when usr click on <stop R> button.
    """
    try:
        word_res = "\nName of Reserve : " + self.delRestop.get()
        resdose_insert = self.delresdose.get()
        with open('./ttt/doc_ttt11/stopped_res.txt', 'a+') as file_stopr:
            file_stopr.write(word_res + " " + resdose_insert + " - stopped on : " + \
                time.strftime("%d/%m/%Y"))
    except FileNotFoundError as file_err:
        print("[Err_delres] Found error : ", file_err)
    print("[+] No error, file (2) stopped_res.txt will be upload to server !")
    resupload()

def deleteReserve(self):
    """
        Delete all data of Reserve choosen.
    """
    try:
        if os.path.getsize('./ttt/doc_ttt11/convres.json'):
            print("[+] File (2) 'convres.json' exist !")
            with open('./ttt/doc_ttt11/convres.json', 'r') as datar:
                datadelres = json.load(datar)

            dataRes = datadelres
            for key, value in dataRes.items():
                if self.delRestop.get() == value[0]['Treatment'] and \
                    self.delresdose.get() == value[0]['Dosage']:
                    del value[0]

                elif self.delRestop.get() == value[1]['Treatment'] and \
                    self.delresdose.get() == value[1]['Dosage']:
                    del value[1]

                elif self.delRestop.get() == value[2]['Treatment'] and \
                    self.delresdose.get() == value[2]['Dosage']:
                    del value[2]

                elif self.delRestop.get() == value[3]['Treatment'] and \
                    self.delresdose.get() == value[3]['Dosage']:
                    del value[3]

                elif self.delRestop.get() == value[4]['Treatment'] and \
                    self.delresdose.get() == value[4]['Dosage']:
                    del value[4]

                elif self.delRestop.get() == value[5]['Treatment'] and \
                    self.delresdose.get() == value[5]['Dosage']:
                    del value[5]

                elif self.delRestop.get() == value[6]['Treatment'] and \
                    self.delresdose.get() == value[6]['Dosage']:
                    del value[6]

                elif self.delRestop.get() == value[7]['Treatment'] and \
                    self.delresdose.get() == value[7]['Dosage']:
                    del value[7]

                elif self.delRestop.get() == value[8]['Treatment'] and \
                    self.delresdose.get() == value[8]['Dosage']:
                    del value[8]

                elif self.delRestop.get() == value[9]['Treatment'] and \
                    self.delresdose.get() == value[9]['Dosage']:
                    del value[9]

                elif self.delRestop.get() == value[10]['Treatment'] and \
                    self.delresdose.get() == value[10]['Dosage']:
                    del value[10]

                elif self.delRestop.get() == value[11]['Treatment'] and \
                    self.delresdose.get() == value[11]['Dosage']:
                    del value[11]

                elif self.delRestop.get() == value[12]['Treatment'] and \
                    self.delresdose.get() == value[12]['Dosage']:
                    del value[12]

                elif self.delRestop.get() == value[13]['Treatment'] and \
                    self.delresdose.get() == value[13]['Dosage']:
                    del value[13]

                elif self.delRestop.get() == value[14]['Treatment'] and \
                    self.delresdose.get() == value[14]['Dosage']:
                    del value[14]

                print("---Ok 'RESERVE' earased---")
                with open('./ttt/doc_ttt11/convres.json', 'w') as datafirse:
                    json.dump(dataRes, datafirse, indent=4)

    except FileNotFoundError as fnfe:
        print('[!] Sorry, file convres.json does not exist !', fnfe)
        messagebox.showerror('Error', 'File convres.json does not exist !')

def stopReserve(self):
    """
        Search Date of end and write value of the date of today,
        when usr click on <stop R> button.
    """
    MSB2asno = messagebox.askyesno('Delete Reserve', 'Are you sure to delete it ?')
    if MSB2asno == 1:
        try:
            if os.path.getsize('./ttt/doc_ttt11/ires_rs.txt'):
                print("[+] File ires_rs.txt exist (2)!")
        except FileNotFoundError as no_finit:
            print("[!] File ires_rs.txt doesn't exist (2)!")
            with open('./ttt/doc_ttt11/ires_rs.txt', 'a+') as creat_f:
                creat_f.write(str("Stopped R :"))

        try:
            if os.path.getsize('./ttt/doc_ttt11/convres.json'):
                print("[+] File 'convres' exist !")
                with open('./ttt/doc_ttt11/convres.json', 'r') as datafiler:
                    datadelr = json.load(datafiler)

                dataRes = datadelr
                for key, value in dataRes.items():
                    if self.delRestop.get() == value[0]['Treatment'] and \
                        self.delresdose.get() == value[0]['Dosage']:
                        value[0]["Date of end"] = time.strftime("%d/%m/%Y")
                        with open('./ttt/doc_ttt11/ires_rs.txt', 'a+') as file_r:
                            json.dump(value[0], file_r, indent=4)

                    elif self.delRestop.get() == value[1]['Treatment'] and \
                        self.delresdose.get() == value[1]['Dosage']:
                        value[1]["Date of end"] = time.strftime("%d/%m/%Y")
                        with open('./ttt/doc_ttt11/ires_rs.txt', 'a+') as file_r:
                            json.dump(value[1], file_r, indent=4)

                    elif self.delRestop.get() == value[2]['Treatment'] and \
                        self.delresdose.get() == value[2]['Dosage']:
                        value[2]["Date of end"] = time.strftime("%d/%m/%Y")
                        with open('./ttt/doc_ttt11/ires_rs.txt', 'a+') as file_r:
                            json.dump(value[2], file_r, indent=4)

                    elif self.delRestop.get() == value[3]['Treatment'] and \
                        self.delresdose.get() == value[3]['Dosage']:
                        value[3]["Date of end"] = time.strftime("%d/%m/%Y")
                        with open('./ttt/doc_ttt11/ires_rs.txt', 'a+') as file_r:
                            json.dump(value[3], file_r, indent=4)

                    elif self.delRestop.get() == value[4]['Treatment'] and \
                        self.delresdose.get() == value[4]['Dosage']:
                        value[4]["Date of end"] = time.strftime("%d/%m/%Y")
                        with open('./ttt/doc_ttt11/ires_rs.txt', 'a+') as file_r:
                            json.dump(value[4], file_r, indent=4)

                    elif self.delRestop.get() == value[5]['Treatment'] and \
                        self.delresdose.get() == value[5]['Dosage']:
                        value[5]["Date of end"] = time.strftime("%d/%m/%Y")
                        with open('./ttt/doc_ttt11/ires_rs.txt', 'a+') as file_r:
                            json.dump(value[5], file_r, indent=4)

                    elif self.delRestop.get() == value[6]['Treatment'] and \
                        self.delresdose.get() == value[6]['Dosage']:
                        value[6]["Date of end"] = time.strftime("%d/%m/%Y")
                        with open('./ttt/doc_ttt11/ires_rs.txt', 'a+') as file_r:
                            json.dump(value[6], file_r, indent=4)

                    elif self.delRestop.get() == value[7]['Treatment'] and \
                        self.delresdose.get() == value[7]['Dosage']:
                        value[7]["Date of end"] = time.strftime("%d/%m/%Y")
                        with open('./ttt/doc_ttt11/ires_rs.txt', 'a+') as file_r:
                            json.dump(value[7], file_r, indent=4)

                    elif self.delRestop.get() == value[8]['Treatment'] and \
                        self.delresdose.get() == value[8]['Dosage']:
                        value[8]["Date of end"] = time.strftime("%d/%m/%Y")
                        with open('./ttt/doc_ttt11/ires_rs.txt', 'a+') as file_r:
                            json.dump(value[8], file_r, indent=4)

                    elif self.delRestop.get() == value[9]['Treatment'] and \
                        self.delresdose.get() == value[9]['Dosage']:
                        value[9]["Date of end"] = time.strftime("%d/%m/%Y")
                        with open('./ttt/doc_ttt11/ires_rs.txt', 'a+') as file_r:
                            json.dump(value[9], file_r, indent=4)

                    elif self.delRestop.get() == value[10]['Treatment'] and \
                        self.delresdose.get() == value[10]['Dosage']:
                        value[10]["Date of end"] = time.strftime("%d/%m/%Y")
                        with open('./ttt/doc_ttt11/ires_rs.txt', 'a+') as file_r:
                            json.dump(value[10], file_r, indent=4)

                    elif self.delRestop.get() == value[11]['Treatment'] and \
                        self.delresdose.get() == value[11]['Dosage']:
                        value[11]["Date of end"] = time.strftime("%d/%m/%Y")
                        with open('./ttt/doc_ttt11/ires_rs.txt', 'a+') as file_r:
                            json.dump(value[11], file_r, indent=4)

                    elif self.delRestop.get() == value[12]['Treatment'] and \
                        self.delresdose.get() == value[12]['Dosage']:
                        value[12]["Date of end"] = time.strftime("%d/%m/%Y")
                        with open('./ttt/doc_ttt11/ires_rs.txt', 'a+') as file_r:
                            json.dump(value[12], file_r, indent=4)

                    elif self.delRestop.get() == value[13]['Treatment'] and \
                        self.delresdose.get() == value[13]['Dosage']:
                        value[13]["Date of end"] = time.strftime("%d/%m/%Y")
                        with open('./ttt/doc_ttt11/ires_rs.txt', 'a+') as file_r:
                            json.dump(value[13], file_r, indent=4)

                    elif self.delRestop.get() == value[14]['Treatment'] and \
                        self.delresdose.get() == value[14]['Dosage']:
                        value[14]["Date of end"] = time.strftime("%d/%m/%Y")
                        with open('./ttt/doc_ttt11/ires_rs.txt', 'a+') as file_r:
                            json.dump(value[14], file_r, indent=4)

                    print("---Ok 'RESERVE' earased---")
                    with open('./ttt/doc_ttt11/convres.json', 'w') as datafile2:
                        json.dump(dataRes, datafile2, indent=4)

                    deleteReserve(self)
                    writeStoppedRes(self)

        except FileNotFoundError as fnf_erres:
            print('[!] Sorry, file convres.json does not exist !', fnf_erres)
            messagebox.showerror('Error', 'File convres.json does not exist !')
        except IndexError as ie_res:
            print('[!] Sorry, reserve is not present into medication !', ie_res)
            messagebox.showerror('Error', 'Reserve is not present into medication !')
    else:
        messagebox.showinfo('Info', 'Reserve has not been earased.')
