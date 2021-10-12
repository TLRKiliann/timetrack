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


def paramBackToSave(self):
    """
        Backup for paramdata7.txt/month
        Think to change date (4 update)!
    """
    listofdate = []
    with open("./param/updateparam.json") as file_r:
        listofdate = json.load(file_r)
        for index, value in listofdate.items():
            for x in value:
                print(x)
                if time.strftime("%d/%m/%Y") == x:
                    print("------------------------------")
                    print("Today : ", x)
                    print("------------------------------")
                    print("Backup of files of Vitals Parameters !")

                    try:
                        if os.path.exists('./param/paramdata1.txt'):
                            print("Backup of file paramdata1.txt !")
                            shutil.copy('./param/paramdata1.txt',
                                './Backup/Files1/paramdata1.txt')
                    except FileNotFoundError as param1_err:
                        print("+ Error file not found !", param1_err)

                    try:
                        if os.path.exists('./param/paramdata2.txt'):
                            print("Backup of file paramdata2.txt !")
                            shutil.copy('./param/paramdata2.txt',
                                './Backup/Files2/paramdata2.txt')
                    except FileNotFoundError as param2_err:
                        print("+ Error file not found !", param2_err)

                    try:
                        if os.path.exists('./param/paramdata3.txt'):
                            print("Backup of file paramdata3.txt !")
                            shutil.copy('./param/paramdata3.txt',
                                './Backup/Files3/paramdata3.txt')
                    except FileNotFoundError as param3_err:
                        print("+ Error file not found !", param3_err)

                    try:
                        if os.path.exists('./param/paramdata4.txt'):
                            print("Backup of file paramdata4.txt !")
                            shutil.copy('./param/paramdata4.txt',
                                './Backup/Files4/paramdata4.txt')
                    except FileNotFoundError as param4_err:
                        print("+ Error file not found !", param4_err)

                    try:
                        if os.path.exists('./param/paramdata5.txt'):
                            print("Backup of file paramdata5.txt !")
                            shutil.copy('./param/paramdata5.txt',
                                './Backup/Files5/paramdata5.txt')
                    except FileNotFoundError as param5_err:
                        print("+ Error file not found !", param5_err)

                    try:
                        if os.path.exists('./param/paramdata6.txt'):
                            print("Backup of file paramdata6.txt !")
                            shutil.copy('./param/paramdata6.txt',
                                './Backup/Files6/paramdata6.txt')
                    except FileNotFoundError as param6_err:
                        print("+ Error file not found !", param6_err)

                    try:
                        if os.path.exists('./param/paramdata7.txt'):
                            print("Backup of file paramdata7.txt !")
                            shutil.copy('./param/paramdata7.txt',
                                './Backup/Files7/paramdata7.txt')
                    except FileNotFoundError as param7_err:
                        print("+ Error file not found !", param7_err)

                    try:
                        if os.path.exists('./param/paramdata8.txt'):
                            print("Backup of file paramdata8.txt !")
                            shutil.copy('./param/paramdata8.txt',
                                './Backup/Files8/paramdata8.txt')
                    except FileNotFoundError as param8_err:
                        print("+ Error file not found !", param8_err)

                    try:
                        if os.path.exists('./param/paramdata9.txt'):
                            print("Backup of file paramdata9.txt !")
                            shutil.copy('./param/paramdata9.txt',
                                './Backup/Files9/paramdata9.txt')
                    except FileNotFoundError as param9_err:
                        print("+ Error file not found !", param9_err)

                    try:
                        if os.path.exists('./param/paramdata10.txt'):
                            print("Backup of file paramdata10.txt !")
                            shutil.copy('./param/paramdata10.txt',
                                './Backup/Files10/paramdata10.txt')
                    except FileNotFoundError as param10_err:
                        print("+ Error file not found !", param10_err)

                    try:
                        if os.path.exists('./param/paramdata11.txt'):
                            print("Backup of file paramdata11.txt !")
                            shutil.copy('./param/paramdata11.txt',
                                './Backup/Files11/paramdata11.txt')
                    except FileNotFoundError as param11_err:
                        print("+ Error file not found !", param11_err)

                    try:
                        if os.path.exists('./param/paramdata12.txt'):
                            print("Backup of file paramdata12.txt !")
                            shutil.copy('./param/paramdata12.txt',
                                './Backup/Files12/paramdata12.txt')
                    except FileNotFoundError as param12_err:
                        print("+ Error file not found !", param12_err)

                    try:
                        if os.path.exists('./param/paramdata13.txt'):
                            print("Backup of file paramdata13.txt !")
                            shutil.copy('./param/paramdata13.txt',
                                './Backup/Files13/paramdata13.txt')
                    except FileNotFoundError as param13_err:
                        print("+ Error file not found !", param13_err)

                    try:
                        if os.path.exists('./param/paramdata14.txt'):
                            print("Backup of file paramdata14.txt !")
                            shutil.copy('./param/paramdata14.txt',
                                './Backup/Files14/paramdata14.txt')
                    except FileNotFoundError as param14_err:
                        print("+ Error file not found !", param14_err)

                    try:
                        if os.path.exists('./param/paramdata15.txt'):
                            print("Backup of file paramdata15.txt !")
                            shutil.copy('./param/paramdata15.txt',
                                './Backup/Files15/paramdata15.txt')
                    except FileNotFoundError as param15_err:
                        print("+ Error file not found !", param15_err)

                    try:
                        if os.path.exists('./param/paramdata16.txt'):
                            print("Backup of file paramdata16.txt !")
                            shutil.copy('./param/paramdata16.txt',
                                './Backup/Files16/paramdata16.txt')
                    except FileNotFoundError as param16_err:
                        print("+ Error file not found !", param16_err)

                    try:
                        if os.path.exists('./param/paramdata17.txt'):
                            print("Backup of file paramdata17.txt !")
                            shutil.copy('./param/paramdata17.txt',
                                './Backup/Files17/paramdata17.txt')
                    except FileNotFoundError as param17_err:
                        print("+ Error file not found !", param17_err)

                    try:
                        if os.path.exists('./param/paramdata18.txt'):
                            print("Backup of file paramdata18.txt !")
                            shutil.copy('./param/paramdata18.txt',
                                './Backup/Files18/paramdata18.txt')
                    except FileNotFoundError as param18_err:
                        print("+ Error file not found !", param18_err)

                    try:
                        if os.path.exists('./param/paramdata19.txt'):
                            print("Backup of file paramdata19.txt !")
                            shutil.copy('./param/paramdata19.txt',
                                './Backup/Files19/paramdata19.txt')
                    except FileNotFoundError as param19_err:
                        print("+ Error file not found !", param19_err)

                    try:
                        if os.path.exists('./param/paramdata20.txt'):
                            print("Backup of file paramdata20.txt !")
                            shutil.copy('./param/paramdata20.txt',
                                './Backup/Files20/paramdata20.txt')
                    except FileNotFoundError as param20_err:
                        print("+ Error file not found !", param20_err)

                    try:
                        if os.path.exists('./param/paramdata21.txt'):
                            print("Backup of file paramdata21.txt !")
                            shutil.copy('./param/paramdata21.txt',
                                './Backup/Files21/paramdata21.txt')
                    except FileNotFoundError as param21_err:
                        print("+ Error file not found !", param21_err)

                    try:
                        if os.path.exists('./param/paramdata22.txt'):
                            print("Backup of file paramdata22.txt !")
                            shutil.copy('./param/paramdata22.txt',
                                './Backup/Files22/paramdata22.txt')
                    except FileNotFoundError as param22_err:
                        print("+ Error file not found !", param22_err)

                    try:
                        if os.path.exists('./param/paramdata23.txt'):
                            print("Backup of file paramdata23.txt !")
                            shutil.copy('./param/paramdata23.txt',
                                './Backup/Files23/paramdata23.txt')
                    except FileNotFoundError as param23_err:
                        print("+ Error file not found !", param23_err)

                    try:
                        if os.path.exists('./param/paramdata24.txt'):
                            print("Backup of file paramdata24.txt !")
                            shutil.copy('./param/paramdata24.txt',
                                './Backup/Files24/paramdata24.txt')
                    except FileNotFoundError as param24_err:
                        print("+ Error file not found !", param24_err)

                    x=str(x)
                    value.remove(x)
                    file_w = open("./param/updateparam.json", "w")
                    listofdate = json.dump(listofdate, file_w, indent=4)
                    print("Update for all vitals parameters done !")
                    messagebox.showinfo("Info", "Update for all vitals parameters done !")
