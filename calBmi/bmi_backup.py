#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
    This script was made to backup
    all parameters for every patient
    by month at first of every month.
"""


import tkinter
from tkinter import *
from tkinter import messagebox
import json
import os
import time
import shutil


def bmiBackToSave(self):
    """
        Backup for bmi7.txt/month
        Think to change date (4 update)!
    """
    listbmidate = []
    with open("./calBmi/updatebmi.json") as file_r:
        listbmidate = json.load(file_r)
        for index, value in listbmidate.items():
            for x in value:
                print(x)
                if time.strftime("%d/%m/%Y") == x:
                    print("------------------------------")
                    print("Today : ", x)
                    print("------------------------------")
                    print("[+] Backup of files of Vitals Parameters !")

                    try:
                        if os.path.exists('./calBmi/bmi1.txt'):
                            print("[+] Backup of file bmi1.txt !")
                            shutil.copy('./calBmi/bmi1.txt',
                                './Backup/Files1/bmi1.txt')
                    except FileNotFoundError as param1_err:
                        print("[!] Error file not found !", param1_err)

                    try:
                        if os.path.exists('./calBmi/bmi2.txt'):
                            print("[+] Backup of file bmi2.txt !")
                            shutil.copy('./calBmi/bmi2.txt',
                                './Backup/Files2/bmi2.txt')
                    except FileNotFoundError as param2_err:
                        print("[!] Error file not found !", param2_err)

                    try:
                        if os.path.exists('./calBmi/bmi3.txt'):
                            print("[+] Backup of file bmi3.txt !")
                            shutil.copy('./calBmi/bmi3.txt',
                                './Backup/Files3/bmi3.txt')
                    except FileNotFoundError as param3_err:
                        print("[!] Error file not found !", param3_err)

                    try:
                        if os.path.exists('./calBmi/bmi4.txt'):
                            print("[+] Backup of file bmi4.txt !")
                            shutil.copy('./calBmi/bmi4.txt',
                                './Backup/Files4/bmi4.txt')
                    except FileNotFoundError as param4_err:
                        print("[!] Error file not found !", param4_err)

                    try:
                        if os.path.exists('./calBmi/bmi5.txt'):
                            print("[+] Backup of file bmi5.txt !")
                            shutil.copy('./calBmi/bmi5.txt',
                                './Backup/Files5/bmi5.txt')
                    except FileNotFoundError as param5_err:
                        print("[!] Error file not found !", param5_err)

                    try:
                        if os.path.exists('./calBmi/bmi6.txt'):
                            print("[+] Backup of file bmi6.txt !")
                            shutil.copy('./calBmi/bmi6.txt',
                                './Backup/Files6/bmi6.txt')
                    except FileNotFoundError as param6_err:
                        print("[!] Error file not found !", param6_err)

                    try:
                        if os.path.exists('./calBmi/bmi7.txt'):
                            print("[+] Backup of file bmi7.txt !")
                            shutil.copy('./calBmi/bmi7.txt',
                                './Backup/Files7/bmi7.txt')
                    except FileNotFoundError as param7_err:
                        print("[!] Error file not found !", param7_err)

                    try:
                        if os.path.exists('./calBmi/bmi8.txt'):
                            print("[+] Backup of file bmi8.txt !")
                            shutil.copy('./calBmi/bmi8.txt',
                                './Backup/Files8/bmi8.txt')
                    except FileNotFoundError as param8_err:
                        print("[!] Error file not found !", param8_err)

                    try:
                        if os.path.exists('./calBmi/bmi9.txt'):
                            print("[+] Backup of file bmi9.txt !")
                            shutil.copy('./calBmi/bmi9.txt',
                                './Backup/Files9/bmi9.txt')
                    except FileNotFoundError as param9_err:
                        print("[!] Error file not found !", param9_err)

                    try:
                        if os.path.exists('./calBmi/bmi10.txt'):
                            print("[+] Backup of file bmi10.txt !")
                            shutil.copy('./calBmi/bmi10.txt',
                                './Backup/Files10/bmi10.txt')
                    except FileNotFoundError as param10_err:
                        print("[!] Error file not found !", param10_err)

                    try:
                        if os.path.exists('./calBmi/bmi11.txt'):
                            print("[+] Backup of file bmi11.txt !")
                            shutil.copy('./calBmi/bmi11.txt',
                                './Backup/Files11/bmi11.txt')
                    except FileNotFoundError as param11_err:
                        print("[!] Error file not found !", param11_err)

                    try:
                        if os.path.exists('./calBmi/bmi12.txt'):
                            print("[+] Backup of file bmi12.txt !")
                            shutil.copy('./calBmi/bmi12.txt',
                                './Backup/Files12/bmi12.txt')
                    except FileNotFoundError as param12_err:
                        print("[!] Error file not found !", param12_err)

                    try:
                        if os.path.exists('./calBmi/bmi13.txt'):
                            print("[+] Backup of file bmi13.txt !")
                            shutil.copy('./calBmi/bmi13.txt',
                                './Backup/Files13/bmi13.txt')
                    except FileNotFoundError as param13_err:
                        print("[!] Error file not found !", param13_err)

                    try:
                        if os.path.exists('./calBmi/bmi14.txt'):
                            print("[+] Backup of file bmi14.txt !")
                            shutil.copy('./calBmi/bmi14.txt',
                                './Backup/Files14/bmi14.txt')
                    except FileNotFoundError as param14_err:
                        print("[!] Error file not found !", param14_err)

                    try:
                        if os.path.exists('./calBmi/bmi15.txt'):
                            print("[+] Backup of file bmi15.txt !")
                            shutil.copy('./calBmi/bmi15.txt',
                                './Backup/Files15/bmi15.txt')
                    except FileNotFoundError as param15_err:
                        print("[!] Error file not found !", param15_err)

                    try:
                        if os.path.exists('./calBmi/bmi16.txt'):
                            print("[+] Backup of file bmi16.txt !")
                            shutil.copy('./calBmi/bmi16.txt',
                                './Backup/Files16/bmi16.txt')
                    except FileNotFoundError as param16_err:
                        print("[!] Error file not found !", param16_err)

                    try:
                        if os.path.exists('./calBmi/bmi17.txt'):
                            print("[+] Backup of file bmi17.txt !")
                            shutil.copy('./calBmi/bmi17.txt',
                                './Backup/Files17/bmi17.txt')
                    except FileNotFoundError as param17_err:
                        print("[!] Error file not found !", param17_err)

                    try:
                        if os.path.exists('./calBmi/bmi18.txt'):
                            print("[+] Backup of file bmi18.txt !")
                            shutil.copy('./calBmi/bmi18.txt',
                                './Backup/Files18/bmi18.txt')
                    except FileNotFoundError as param18_err:
                        print("[!] Error file not found !", param18_err)

                    try:
                        if os.path.exists('./calBmi/bmi19.txt'):
                            print("[+] Backup of file bmi19.txt !")
                            shutil.copy('./calBmi/bmi19.txt',
                                './Backup/Files19/bmi19.txt')
                    except FileNotFoundError as param19_err:
                        print("[!] Error file not found !", param19_err)

                    try:
                        if os.path.exists('./calBmi/bmi20.txt'):
                            print("[+] Backup of file bmi20.txt !")
                            shutil.copy('./calBmi/bmi20.txt',
                                './Backup/Files20/bmi20.txt')
                    except FileNotFoundError as param20_err:
                        print("[!] Error file not found !", param20_err)

                    try:
                        if os.path.exists('./calBmi/bmi21.txt'):
                            print("[+] Backup of file bmi21.txt !")
                            shutil.copy('./calBmi/bmi21.txt',
                                './Backup/Files21/bmi21.txt')
                    except FileNotFoundError as param21_err:
                        print("[!] Error file not found !", param21_err)

                    try:
                        if os.path.exists('./calBmi/bmi22.txt'):
                            print("[+] Backup of file bmi22.txt !")
                            shutil.copy('./calBmi/bmi22.txt',
                                './Backup/Files22/bmi22.txt')
                    except FileNotFoundError as param22_err:
                        print("[!] Error file not found !", param22_err)

                    try:
                        if os.path.exists('./calBmi/bmi23.txt'):
                            print("[+] Backup of file bmi23.txt !")
                            shutil.copy('./calBmi/bmi23.txt',
                                './Backup/Files23/bmi23.txt')
                    except FileNotFoundError as param23_err:
                        print("[!] Error file not found !", param23_err)

                    try:
                        if os.path.exists('./calBmi/bmi24.txt'):
                            print("[+] Backup of file bmi24.txt !")
                            shutil.copy('./calBmi/bmi24.txt',
                                './Backup/Files24/bmi24.txt')
                    except FileNotFoundError as param24_err:
                        print("[!] Error file not found !", param24_err)

                    x=str(x)
                    value.remove(x)
                    file_w = open("./calBmi/updatebmi.json", "w")
                    listbmidate = json.dump(listbmidate, file_w, indent=4)
                    print("Update for all BMI files done !")
                    messagebox.showinfo("Info", "Update for all BMI done !")
