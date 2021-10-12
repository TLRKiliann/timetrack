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
                                './Backup/Files1/Backup_param1.txt')
                    except FileNotFoundError as param1_err:
                        print("+ Error file not found !", param1_err)

                    try:
                        if os.path.exists('./param/paramdata2.txt'):
                            print("Backup of file paramdata2.txt !")
                            shutil.copy('./param/paramdata2.txt',
                                './Backup/Files2/Backup_param2.txt')
                    except FileNotFoundError as param2_err:
                        print("+ Error file not found !", param2_err)

                    try:
                        if os.path.exists('./param/paramdata3.txt'):
                            print("Backup of file paramdata3.txt !")
                            shutil.copy('./param/paramdata3.txt',
                                './Backup/Files3/Backup_param3.txt')
                    except FileNotFoundError as param3_err:
                        print("+ Error file not found !", param3_err)

                    try:
                        if os.path.exists('./param/paramdata4.txt'):
                            print("Backup of file paramdata4.txt !")
                            shutil.copy('./param/paramdata4.txt',
                                './Backup/Files4/Backup_param4.txt')
                    except FileNotFoundError as param4_err:
                        print("+ Error file not found !", param4_err)

                    try:
                        if os.path.exists('./param/paramdata5.txt'):
                            print("Backup of file paramdata5.txt !")
                            shutil.copy('./param/paramdata5.txt',
                                './Backup/Files5/Backup_param5.txt')
                    except FileNotFoundError as param5_err:
                        print("+ Error file not found !", param5_err)

                    try:
                        if os.path.exists('./param/paramdata6.txt'):
                            print("Backup of file paramdata6.txt !")
                            shutil.copy('./param/paramdata6.txt',
                                './Backup/Files6/Backup_param6.txt')
                    except FileNotFoundError as param6_err:
                        print("+ Error file not found !", param6_err)

                    try:
                        if os.path.exists('./param/paramdata7.txt'):
                            print("Backup of file paramdata7.txt !")
                            shutil.copy('./param/paramdata7.txt',
                                './Backup/Files7/Backup_param7.txt')
                    except FileNotFoundError as param7_err:
                        print("+ Error file not found !", param7_err)

                    try:
                        if os.path.exists('./param/paramdata8.txt'):
                            print("Backup of file paramdata8.txt !")
                            shutil.copy('./param/paramdata8.txt',
                                './Backup/Files8/Backup_param8.txt')
                    except FileNotFoundError as param8_err:
                        print("+ Error file not found !", param8_err)

                    try:
                        if os.path.exists('./param/paramdata9.txt'):
                            print("Backup of file paramdata9.txt !")
                            shutil.copy('./param/paramdata9.txt',
                                './Backup/Files9/Backup_param9.txt')
                    except FileNotFoundError as param9_err:
                        print("+ Error file not found !", param9_err)

                    try:
                        if os.path.exists('./param/paramdata10.txt'):
                            print("Backup of file paramdata10.txt !")
                            shutil.copy('./param/paramdata10.txt',
                                './Backup/Files10/Backup_param10.txt')
                    except FileNotFoundError as param10_err:
                        print("+ Error file not found !", param10_err)

                    try:
                        if os.path.exists('./param/paramdata11.txt'):
                            print("Backup of file paramdata11.txt !")
                            shutil.copy('./param/paramdata11.txt',
                                './Backup/Files11/Backup_param11.txt')
                    except FileNotFoundError as param11_err:
                        print("+ Error file not found !", param11_err)

                    try:
                        if os.path.exists('./param/paramdata12.txt'):
                            print("Backup of file paramdata12.txt !")
                            shutil.copy('./param/paramdata12.txt',
                                './Backup/Files12/Backup_param12.txt')
                    except FileNotFoundError as param12_err:
                        print("+ Error file not found !", param12_err)

                    try:
                        if os.path.exists('./param/paramdata13.txt'):
                            print("Backup of file paramdata13.txt !")
                            shutil.copy('./param/paramdata13.txt',
                                './Backup/Files13/Backup_param13.txt')
                    except FileNotFoundError as param13_err:
                        print("+ Error file not found !", param13_err)

                    try:
                        if os.path.exists('./param/paramdata14.txt'):
                            print("Backup of file paramdata14.txt !")
                            shutil.copy('./param/paramdata14.txt',
                                './Backup/Files14/Backup_param14.txt')
                    except FileNotFoundError as param14_err:
                        print("+ Error file not found !", param14_err)

                    try:
                        if os.path.exists('./param/paramdata15.txt'):
                            print("Backup of file paramdata15.txt !")
                            shutil.copy('./param/paramdata15.txt',
                                './Backup/Files15/Backup_param15.txt')
                    except FileNotFoundError as param15_err:
                        print("+ Error file not found !", param15_err)

                    try:
                        if os.path.exists('./param/paramdata16.txt'):
                            print("Backup of file paramdata16.txt !")
                            shutil.copy('./param/paramdata16.txt',
                                './Backup/Files16/Backup_param16.txt')
                    except FileNotFoundError as param16_err:
                        print("+ Error file not found !", param16_err)

                    try:
                        if os.path.exists('./param/paramdata17.txt'):
                            print("Backup of file paramdata17.txt !")
                            shutil.copy('./param/paramdata17.txt',
                                './Backup/Files17/Backup_param17.txt')
                    except FileNotFoundError as param17_err:
                        print("+ Error file not found !", param17_err)

                    try:
                        if os.path.exists('./param/paramdata18.txt'):
                            print("Backup of file paramdata18.txt !")
                            shutil.copy('./param/paramdata18.txt',
                                './Backup/Files18/Backup_param18.txt')
                    except FileNotFoundError as param18_err:
                        print("+ Error file not found !", param18_err)

                    try:
                        if os.path.exists('./param/paramdata19.txt'):
                            print("Backup of file paramdata19.txt !")
                            shutil.copy('./param/paramdata19.txt',
                                './Backup/Files19/Backup_param19.txt')
                    except FileNotFoundError as param19_err:
                        print("+ Error file not found !", param19_err)

                    try:
                        if os.path.exists('./param/paramdata20.txt'):
                            print("Backup of file paramdata20.txt !")
                            shutil.copy('./param/paramdata20.txt',
                                './Backup/Files20/Backup_param20.txt')
                    except FileNotFoundError as param20_err:
                        print("+ Error file not found !", param20_err)

                    try:
                        if os.path.exists('./param/paramdata21.txt'):
                            print("Backup of file paramdata21.txt !")
                            shutil.copy('./param/paramdata21.txt',
                                './Backup/Files21/Backup_param21.txt')
                    except FileNotFoundError as param21_err:
                        print("+ Error file not found !", param21_err)

                    try:
                        if os.path.exists('./param/paramdata22.txt'):
                            print("Backup of file paramdata22.txt !")
                            shutil.copy('./param/paramdata22.txt',
                                './Backup/Files22/Backup_param22.txt')
                    except FileNotFoundError as param22_err:
                        print("+ Error file not found !", param22_err)

                    try:
                        if os.path.exists('./param/paramdata23.txt'):
                            print("Backup of file paramdata23.txt !")
                            shutil.copy('./param/paramdata23.txt',
                                './Backup/Files23/Backup_param23.txt')
                    except FileNotFoundError as param23_err:
                        print("+ Error file not found !", param23_err)

                    try:
                        if os.path.exists('./param/paramdata24.txt'):
                            print("Backup of file paramdata24.txt !")
                            shutil.copy('./param/paramdata24.txt',
                                './Backup/Files24/Backup_param24.txt')
                    except FileNotFoundError as param24_err:
                        print("+ Error file not found !", param24_err)

                    x=str(x)
                    value.remove(x)
                    file_w = open("./param/updateparam.json", "w")
                    listofdate = json.dump(listofdate, file_w, indent=4)
                    eraserParam1()
                    eraserParam2()
                    eraserParam3()
                    eraserParam4()
                    eraserParam5()
                    eraserParam6()
                    eraserParam7()
                    eraserParam8()
                    eraserParam9()
                    eraserParam10()
                    eraserParam11()
                    eraserParam12()
                    eraserParam13()
                    eraserParam14()
                    eraserParam15()
                    eraserParam16()
                    eraserParam17()
                    eraserParam18()
                    eraserParam19()
                    eraserParam20()
                    eraserParam21()
                    eraserParam22()
                    eraserParam23()
                    eraserParam24()
                    print("Update for all vitals parameters done !")
                    messagebox.showinfo("Info", "Update for all vitals parameters done !")

def eraserParam1():
    try:
        if os.path.exists('./param/paramdata1.txt'):
            os.remove('./param/paramdata1.txt')
            print("paramdata1.txt file removed")
    except FileNotFoundError as err_main:
        print("Error file not found", err_main)

    try:
        if os.path.exists('./param/aspifile1/systol.json'):
            os.remove('./param/aspifile1/systol.json')
            print("systol.json file removed")
    except FileNotFoundError as err_syst:
        print("Error file not found", err_syst)

    try:
        if os.path.exists('./param/aspifile1/diastol.json'):
            os.remove('./param/aspifile1/diastol.json')
            print("diastol.json file removed")
    except FileNotFoundError as err_diast:
        print("Error file not found", err_diast)

    try:
        if os.path.exists('./param/aspifile1/temp.json'):
            os.remove('./param/aspifile1/temp.json')
            print("temp.json file removed")
    except FileNotFoundError as err_temp:
        print("Error file not found", err_temp)

    try:
        if os.path.exists('./param/aspifile1/dlr.json'):
            os.remove('./param/aspifile1/dlr.json')
            print("dlr.json file removed")
    except FileNotFoundError as err_dlr:
        print("Error file not found", err_dlr)

    try:
        if os.path.exists('./param/aspifile1/freq.json'):
            os.remove('./param/aspifile1/freq.json')
            print("freq.json file removed")
    except FileNotFoundError as err_freq:
        print("Error file not found", err_freq)

    try:
        if os.path.exists('./param/aspifile1/gly.json'):
            os.remove('./param/aspifile1/gly.json')
            print("gly.json file removed")
    except FileNotFoundError as err_gly:
        print("Error file not found", err_gly)

    try:
        if os.path.exists('./param/aspifile1/puls.json'):
            os.remove('./param/aspifile1/puls.json')
            print("puls.json file removed")
    except FileNotFoundError as err_puls:
        print("Error file not found", err_puls)

    try:
        if os.path.exists('./param/aspifile1/sat.json'):
            os.remove('./param/aspifile1/sat.json')
            print("sat.json file removed")
    except FileNotFoundError as err_sat:
        print("Error file not found", err_sat)

    try:
        if os.path.exists('./param/aspifile1/tensor.json'):
            os.remove('./param/aspifile1/tensor.json')
            print("tensor.json file removed")
    except FileNotFoundError as err_ta:
        print("Error file not found", err_ta)

def eraserParam2():
    try:
        if os.path.exists('./param/paramdata2.txt'):
            os.remove('./param/paramdata2.txt')
            print("paramdata2.txt file removed")
    except FileNotFoundError as err_main:
        print("Error file not found", err_main)

    try:
        if os.path.exists('./param/aspifile1/systol.json'):
            os.remove('./param/aspifile1/systol.json')
            print("systol.json file removed")
    except FileNotFoundError as err_syst:
        print("Error file not found", err_syst)

    try:
        if os.path.exists('./param/aspifile1/diastol.json'):
            os.remove('./param/aspifile1/diastol.json')
            print("diastol.json file removed")
    except FileNotFoundError as err_diast:
        print("Error file not found", err_diast)

    try:
        if os.path.exists('./param/aspifile2/temp.json'):
            os.remove('./param/aspifile2/temp.json')
            print("temp.json file removed")
    except FileNotFoundError as err_temp:
        print("Error file not found", err_temp)

    try:
        if os.path.exists('./param/aspifile2/dlr.json'):
            os.remove('./param/aspifile2/dlr.json')
            print("dlr.json file removed")
    except FileNotFoundError as err_dlr:
        print("Error file not found", err_dlr)

    try:
        if os.path.exists('./param/aspifile2/freq.json'):
            os.remove('./param/aspifile2/freq.json')
            print("freq.json file removed")
    except FileNotFoundError as err_freq:
        print("Error file not found", err_freq)

    try:
        if os.path.exists('./param/aspifile2/gly.json'):
            os.remove('./param/aspifile2/gly.json')
            print("gly.json file removed")
    except FileNotFoundError as err_gly:
        print("Error file not found", err_gly)

    try:
        if os.path.exists('./param/aspifile2/puls.json'):
            os.remove('./param/aspifile2/puls.json')
            print("puls.json file removed")
    except FileNotFoundError as err_puls:
        print("Error file not found", err_puls)

    try:
        if os.path.exists('./param/aspifile2/sat.json'):
            os.remove('./param/aspifile2/sat.json')
            print("sat.json file removed")
    except FileNotFoundError as err_sat:
        print("Error file not found", err_sat)

    try:
        if os.path.exists('./param/aspifile2/tensor.json'):
            os.remove('./param/aspifile2/tensor.json')
            print("tensor.json file removed")
    except FileNotFoundError as err_ta:
        print("Error file not found", err_ta)

def eraserParam3():
    try:
        if os.path.exists('./param/paramdata3.txt'):
            os.remove('./param/paramdata3.txt')
            print("paramdata3.txt file removed")
    except FileNotFoundError as err_main:
        print("Error file not found", err_main)

    try:
        if os.path.exists('./param/aspifile1/systol.json'):
            os.remove('./param/aspifile1/systol.json')
            print("systol.json file removed")
    except FileNotFoundError as err_syst:
        print("Error file not found", err_syst)

    try:
        if os.path.exists('./param/aspifile1/diastol.json'):
            os.remove('./param/aspifile1/diastol.json')
            print("diastol.json file removed")
    except FileNotFoundError as err_diast:
        print("Error file not found", err_diast)

    try:
        if os.path.exists('./param/aspifile3/temp.json'):
            os.remove('./param/aspifile3/temp.json')
            print("temp.json file removed")
    except FileNotFoundError as err_temp:
        print("Error file not found", err_temp)

    try:
        if os.path.exists('./param/aspifile3/dlr.json'):
            os.remove('./param/aspifile3/dlr.json')
            print("dlr.json file removed")
    except FileNotFoundError as err_dlr:
        print("Error file not found", err_dlr)

    try:
        if os.path.exists('./param/aspifile3/freq.json'):
            os.remove('./param/aspifile3/freq.json')
            print("freq.json file removed")
    except FileNotFoundError as err_freq:
        print("Error file not found", err_freq)

    try:
        if os.path.exists('./param/aspifile3/gly.json'):
            os.remove('./param/aspifile3/gly.json')
            print("gly.json file removed")
    except FileNotFoundError as err_gly:
        print("Error file not found", err_gly)

    try:
        if os.path.exists('./param/aspifile3/puls.json'):
            os.remove('./param/aspifile3/puls.json')
            print("puls.json file removed")
    except FileNotFoundError as err_puls:
        print("Error file not found", err_puls)

    try:
        if os.path.exists('./param/aspifile3/sat.json'):
            os.remove('./param/aspifile3/sat.json')
            print("sat.json file removed")
    except FileNotFoundError as err_sat:
        print("Error file not found", err_sat)

    try:
        if os.path.exists('./param/aspifile3/tensor.json'):
            os.remove('./param/aspifile3/tensor.json')
            print("tensor.json file removed")
    except FileNotFoundError as err_ta:
        print("Error file not found", err_ta)

def eraserParam4():
    try:
        if os.path.exists('./param/paramdata4.txt'):
            os.remove('./param/paramdata4.txt')
            print("paramdata4.txt file removed")
    except FileNotFoundError as err_main:
        print("Error file not found", err_main)

    try:
        if os.path.exists('./param/aspifile1/systol.json'):
            os.remove('./param/aspifile1/systol.json')
            print("systol.json file removed")
    except FileNotFoundError as err_syst:
        print("Error file not found", err_syst)

    try:
        if os.path.exists('./param/aspifile1/diastol.json'):
            os.remove('./param/aspifile1/diastol.json')
            print("diastol.json file removed")
    except FileNotFoundError as err_diast:
        print("Error file not found", err_diast)

    try:
        if os.path.exists('./param/aspifile4/temp.json'):
            os.remove('./param/aspifile4/temp.json')
            print("temp.json file removed")
    except FileNotFoundError as err_temp:
        print("Error file not found", err_temp)

    try:
        if os.path.exists('./param/aspifile4/dlr.json'):
            os.remove('./param/aspifile4/dlr.json')
            print("dlr.json file removed")
    except FileNotFoundError as err_dlr:
        print("Error file not found", err_dlr)

    try:
        if os.path.exists('./param/aspifile4/freq.json'):
            os.remove('./param/aspifile4/freq.json')
            print("freq.json file removed")
    except FileNotFoundError as err_freq:
        print("Error file not found", err_freq)

    try:
        if os.path.exists('./param/aspifile4/gly.json'):
            os.remove('./param/aspifile4/gly.json')
            print("gly.json file removed")
    except FileNotFoundError as err_gly:
        print("Error file not found", err_gly)

    try:
        if os.path.exists('./param/aspifile4/puls.json'):
            os.remove('./param/aspifile4/puls.json')
            print("puls.json file removed")
    except FileNotFoundError as err_puls:
        print("Error file not found", err_puls)

    try:
        if os.path.exists('./param/aspifile4/sat.json'):
            os.remove('./param/aspifile4/sat.json')
            print("sat.json file removed")
    except FileNotFoundError as err_sat:
        print("Error file not found", err_sat)

    try:
        if os.path.exists('./param/aspifile4/tensor.json'):
            os.remove('./param/aspifile4/tensor.json')
            print("tensor.json file removed")
    except FileNotFoundError as err_ta:
        print("Error file not found", err_ta)

def eraserParam5():
    try:
        if os.path.exists('./param/paramdata5.txt'):
            os.remove('./param/paramdata5.txt')
            print("paramdata5.txt file removed")
    except FileNotFoundError as err_main:
        print("Error file not found", err_main)

    try:
        if os.path.exists('./param/aspifile1/systol.json'):
            os.remove('./param/aspifile1/systol.json')
            print("systol.json file removed")
    except FileNotFoundError as err_syst:
        print("Error file not found", err_syst)

    try:
        if os.path.exists('./param/aspifile1/diastol.json'):
            os.remove('./param/aspifile1/diastol.json')
            print("diastol.json file removed")
    except FileNotFoundError as err_diast:
        print("Error file not found", err_diast)

    try:
        if os.path.exists('./param/aspifile5/temp.json'):
            os.remove('./param/aspifile5/temp.json')
            print("temp.json file removed")
    except FileNotFoundError as err_temp:
        print("Error file not found", err_temp)

    try:
        if os.path.exists('./param/aspifile5/dlr.json'):
            os.remove('./param/aspifile5/dlr.json')
            print("dlr.json file removed")
    except FileNotFoundError as err_dlr:
        print("Error file not found", err_dlr)

    try:
        if os.path.exists('./param/aspifile5/freq.json'):
            os.remove('./param/aspifile5/freq.json')
            print("freq.json file removed")
    except FileNotFoundError as err_freq:
        print("Error file not found", err_freq)

    try:
        if os.path.exists('./param/aspifile5/gly.json'):
            os.remove('./param/aspifile5/gly.json')
            print("gly.json file removed")
    except FileNotFoundError as err_gly:
        print("Error file not found", err_gly)

    try:
        if os.path.exists('./param/aspifile5/puls.json'):
            os.remove('./param/aspifile5/puls.json')
            print("puls.json file removed")
    except FileNotFoundError as err_puls:
        print("Error file not found", err_puls)

    try:
        if os.path.exists('./param/aspifile5/sat.json'):
            os.remove('./param/aspifile5/sat.json')
            print("sat.json file removed")
    except FileNotFoundError as err_sat:
        print("Error file not found", err_sat)

    try:
        if os.path.exists('./param/aspifile5/tensor.json'):
            os.remove('./param/aspifile5/tensor.json')
            print("tensor.json file removed")
    except FileNotFoundError as err_ta:
        print("Error file not found", err_ta)

def eraserParam6():
    try:
        if os.path.exists('./param/paramdata6.txt'):
            os.remove('./param/paramdata6.txt')
            print("paramdata6.txt file removed")
    except FileNotFoundError as err_main:
        print("Error file not found", err_main)

    try:
        if os.path.exists('./param/aspifile1/systol.json'):
            os.remove('./param/aspifile1/systol.json')
            print("systol.json file removed")
    except FileNotFoundError as err_syst:
        print("Error file not found", err_syst)

    try:
        if os.path.exists('./param/aspifile1/diastol.json'):
            os.remove('./param/aspifile1/diastol.json')
            print("diastol.json file removed")
    except FileNotFoundError as err_diast:
        print("Error file not found", err_diast)

    try:
        if os.path.exists('./param/aspifile6/temp.json'):
            os.remove('./param/aspifile6/temp.json')
            print("temp.json file removed")
    except FileNotFoundError as err_temp:
        print("Error file not found", err_temp)

    try:
        if os.path.exists('./param/aspifile6/dlr.json'):
            os.remove('./param/aspifile6/dlr.json')
            print("dlr.json file removed")
    except FileNotFoundError as err_dlr:
        print("Error file not found", err_dlr)

    try:
        if os.path.exists('./param/aspifile6/freq.json'):
            os.remove('./param/aspifile6/freq.json')
            print("freq.json file removed")
    except FileNotFoundError as err_freq:
        print("Error file not found", err_freq)

    try:
        if os.path.exists('./param/aspifile6/gly.json'):
            os.remove('./param/aspifile6/gly.json')
            print("gly.json file removed")
    except FileNotFoundError as err_gly:
        print("Error file not found", err_gly)

    try:
        if os.path.exists('./param/aspifile6/puls.json'):
            os.remove('./param/aspifile6/puls.json')
            print("puls.json file removed")
    except FileNotFoundError as err_puls:
        print("Error file not found", err_puls)

    try:
        if os.path.exists('./param/aspifile6/sat.json'):
            os.remove('./param/aspifile6/sat.json')
            print("sat.json file removed")
    except FileNotFoundError as err_sat:
        print("Error file not found", err_sat)

    try:
        if os.path.exists('./param/aspifile6/tensor.json'):
            os.remove('./param/aspifile6/tensor.json')
            print("tensor.json file removed")
    except FileNotFoundError as err_ta:
        print("Error file not found", err_ta)

def eraserParam7():
    try:
        if os.path.exists('./param/paramdata7.txt'):
            os.remove('./param/paramdata7.txt')
            print("paramdata7.txt file removed")
    except FileNotFoundError as err_main:
        print("Error file not found", err_main)

    try:
        if os.path.exists('./param/aspifile1/systol.json'):
            os.remove('./param/aspifile1/systol.json')
            print("systol.json file removed")
    except FileNotFoundError as err_syst:
        print("Error file not found", err_syst)

    try:
        if os.path.exists('./param/aspifile1/diastol.json'):
            os.remove('./param/aspifile1/diastol.json')
            print("diastol.json file removed")
    except FileNotFoundError as err_diast:
        print("Error file not found", err_diast)

    try:
        if os.path.exists('./param/aspifile7/temp.json'):
            os.remove('./param/aspifile7/temp.json')
            print("temp.json file removed")
    except FileNotFoundError as err_temp:
        print("Error file not found", err_temp)

    try:
        if os.path.exists('./param/aspifile7/dlr.json'):
            os.remove('./param/aspifile7/dlr.json')
            print("dlr.json file removed")
    except FileNotFoundError as err_dlr:
        print("Error file not found", err_dlr)

    try:
        if os.path.exists('./param/aspifile7/freq.json'):
            os.remove('./param/aspifile7/freq.json')
            print("freq.json file removed")
    except FileNotFoundError as err_freq:
        print("Error file not found", err_freq)

    try:
        if os.path.exists('./param/aspifile7/gly.json'):
            os.remove('./param/aspifile7/gly.json')
            print("gly.json file removed")
    except FileNotFoundError as err_gly:
        print("Error file not found", err_gly)

    try:
        if os.path.exists('./param/aspifile7/puls.json'):
            os.remove('./param/aspifile7/puls.json')
            print("puls.json file removed")
    except FileNotFoundError as err_puls:
        print("Error file not found", err_puls)

    try:
        if os.path.exists('./param/aspifile7/sat.json'):
            os.remove('./param/aspifile7/sat.json')
            print("sat.json file removed")
    except FileNotFoundError as err_sat:
        print("Error file not found", err_sat)

    try:
        if os.path.exists('./param/aspifile7/tensor.json'):
            os.remove('./param/aspifile7/tensor.json')
            print("tensor.json file removed")
    except FileNotFoundError as err_ta:
        print("Error file not found", err_ta)

def eraserParam8():
    try:
        if os.path.exists('./param/paramdata8.txt'):
            os.remove('./param/paramdata8.txt')
            print("paramdata8.txt file removed")
    except FileNotFoundError as err_main:
        print("Error file not found", err_main)

    try:
        if os.path.exists('./param/aspifile1/systol.json'):
            os.remove('./param/aspifile1/systol.json')
            print("systol.json file removed")
    except FileNotFoundError as err_syst:
        print("Error file not found", err_syst)

    try:
        if os.path.exists('./param/aspifile1/diastol.json'):
            os.remove('./param/aspifile1/diastol.json')
            print("diastol.json file removed")
    except FileNotFoundError as err_diast:
        print("Error file not found", err_diast)

    try:
        if os.path.exists('./param/aspifile8/temp.json'):
            os.remove('./param/aspifile8/temp.json')
            print("temp.json file removed")
    except FileNotFoundError as err_temp:
        print("Error file not found", err_temp)

    try:
        if os.path.exists('./param/aspifile8/dlr.json'):
            os.remove('./param/aspifile8/dlr.json')
            print("dlr.json file removed")
    except FileNotFoundError as err_dlr:
        print("Error file not found", err_dlr)

    try:
        if os.path.exists('./param/aspifile8/freq.json'):
            os.remove('./param/aspifile8/freq.json')
            print("freq.json file removed")
    except FileNotFoundError as err_freq:
        print("Error file not found", err_freq)

    try:
        if os.path.exists('./param/aspifile8/gly.json'):
            os.remove('./param/aspifile8/gly.json')
            print("gly.json file removed")
    except FileNotFoundError as err_gly:
        print("Error file not found", err_gly)

    try:
        if os.path.exists('./param/aspifile8/puls.json'):
            os.remove('./param/aspifile8/puls.json')
            print("puls.json file removed")
    except FileNotFoundError as err_puls:
        print("Error file not found", err_puls)

    try:
        if os.path.exists('./param/aspifile8/sat.json'):
            os.remove('./param/aspifile8/sat.json')
            print("sat.json file removed")
    except FileNotFoundError as err_sat:
        print("Error file not found", err_sat)

    try:
        if os.path.exists('./param/aspifile8/tensor.json'):
            os.remove('./param/aspifile8/tensor.json')
            print("tensor.json file removed")
    except FileNotFoundError as err_ta:
        print("Error file not found", err_ta)

def eraserParam9():
    try:
        if os.path.exists('./param/paramdata9.txt'):
            os.remove('./param/paramdata9.txt')
            print("paramdata9.txt file removed")
    except FileNotFoundError as err_main:
        print("Error file not found", err_main)

    try:
        if os.path.exists('./param/aspifile1/systol.json'):
            os.remove('./param/aspifile1/systol.json')
            print("systol.json file removed")
    except FileNotFoundError as err_syst:
        print("Error file not found", err_syst)

    try:
        if os.path.exists('./param/aspifile1/diastol.json'):
            os.remove('./param/aspifile1/diastol.json')
            print("diastol.json file removed")
    except FileNotFoundError as err_diast:
        print("Error file not found", err_diast)

    try:
        if os.path.exists('./param/aspifile9/temp.json'):
            os.remove('./param/aspifile9/temp.json')
            print("temp.json file removed")
    except FileNotFoundError as err_temp:
        print("Error file not found", err_temp)

    try:
        if os.path.exists('./param/aspifile9/dlr.json'):
            os.remove('./param/aspifile9/dlr.json')
            print("dlr.json file removed")
    except FileNotFoundError as err_dlr:
        print("Error file not found", err_dlr)

    try:
        if os.path.exists('./param/aspifile9/freq.json'):
            os.remove('./param/aspifile9/freq.json')
            print("freq.json file removed")
    except FileNotFoundError as err_freq:
        print("Error file not found", err_freq)

    try:
        if os.path.exists('./param/aspifile9/gly.json'):
            os.remove('./param/aspifile9/gly.json')
            print("gly.json file removed")
    except FileNotFoundError as err_gly:
        print("Error file not found", err_gly)

    try:
        if os.path.exists('./param/aspifile9/puls.json'):
            os.remove('./param/aspifile9/puls.json')
            print("puls.json file removed")
    except FileNotFoundError as err_puls:
        print("Error file not found", err_puls)

    try:
        if os.path.exists('./param/aspifile9/sat.json'):
            os.remove('./param/aspifile9/sat.json')
            print("sat.json file removed")
    except FileNotFoundError as err_sat:
        print("Error file not found", err_sat)

    try:
        if os.path.exists('./param/aspifile9/tensor.json'):
            os.remove('./param/aspifile9/tensor.json')
            print("tensor.json file removed")
    except FileNotFoundError as err_ta:
        print("Error file not found", err_ta)

def eraserParam10():
    try:
        if os.path.exists('./param/paramdata10.txt'):
            os.remove('./param/paramdata10.txt')
            print("paramdata10.txt file removed")
    except FileNotFoundError as err_main:
        print("Error file not found", err_main)

    try:
        if os.path.exists('./param/aspifile1/systol.json'):
            os.remove('./param/aspifile1/systol.json')
            print("systol.json file removed")
    except FileNotFoundError as err_syst:
        print("Error file not found", err_syst)

    try:
        if os.path.exists('./param/aspifile1/diastol.json'):
            os.remove('./param/aspifile1/diastol.json')
            print("diastol.json file removed")
    except FileNotFoundError as err_diast:
        print("Error file not found", err_diast)

    try:
        if os.path.exists('./param/aspifile10/temp.json'):
            os.remove('./param/aspifile10/temp.json')
            print("temp.json file removed")
    except FileNotFoundError as err_temp:
        print("Error file not found", err_temp)

    try:
        if os.path.exists('./param/aspifile10/dlr.json'):
            os.remove('./param/aspifile10/dlr.json')
            print("dlr.json file removed")
    except FileNotFoundError as err_dlr:
        print("Error file not found", err_dlr)

    try:
        if os.path.exists('./param/aspifile10/freq.json'):
            os.remove('./param/aspifile10/freq.json')
            print("freq.json file removed")
    except FileNotFoundError as err_freq:
        print("Error file not found", err_freq)

    try:
        if os.path.exists('./param/aspifile10/gly.json'):
            os.remove('./param/aspifile10/gly.json')
            print("gly.json file removed")
    except FileNotFoundError as err_gly:
        print("Error file not found", err_gly)

    try:
        if os.path.exists('./param/aspifile10/puls.json'):
            os.remove('./param/aspifile10/puls.json')
            print("puls.json file removed")
    except FileNotFoundError as err_puls:
        print("Error file not found", err_puls)

    try:
        if os.path.exists('./param/aspifile10/sat.json'):
            os.remove('./param/aspifile10/sat.json')
            print("sat.json file removed")
    except FileNotFoundError as err_sat:
        print("Error file not found", err_sat)

    try:
        if os.path.exists('./param/aspifile10/tensor.json'):
            os.remove('./param/aspifile10/tensor.json')
            print("tensor.json file removed")
    except FileNotFoundError as err_ta:
        print("Error file not found", err_ta)

def eraserParam11():
    try:
        if os.path.exists('./param/paramdata11.txt'):
            os.remove('./param/paramdata11.txt')
            print("paramdata11.txt file removed")
    except FileNotFoundError as err_main:
        print("Error file not found", err_main)

    try:
        if os.path.exists('./param/aspifile1/systol.json'):
            os.remove('./param/aspifile1/systol.json')
            print("systol.json file removed")
    except FileNotFoundError as err_syst:
        print("Error file not found", err_syst)

    try:
        if os.path.exists('./param/aspifile1/diastol.json'):
            os.remove('./param/aspifile1/diastol.json')
            print("diastol.json file removed")
    except FileNotFoundError as err_diast:
        print("Error file not found", err_diast)

    try:
        if os.path.exists('./param/aspifile11/temp.json'):
            os.remove('./param/aspifile11/temp.json')
            print("temp.json file removed")
    except FileNotFoundError as err_temp:
        print("Error file not found", err_temp)

    try:
        if os.path.exists('./param/aspifile11/dlr.json'):
            os.remove('./param/aspifile11/dlr.json')
            print("dlr.json file removed")
    except FileNotFoundError as err_dlr:
        print("Error file not found", err_dlr)

    try:
        if os.path.exists('./param/aspifile11/freq.json'):
            os.remove('./param/aspifile11/freq.json')
            print("freq.json file removed")
    except FileNotFoundError as err_freq:
        print("Error file not found", err_freq)

    try:
        if os.path.exists('./param/aspifile11/gly.json'):
            os.remove('./param/aspifile11/gly.json')
            print("gly.json file removed")
    except FileNotFoundError as err_gly:
        print("Error file not found", err_gly)

    try:
        if os.path.exists('./param/aspifile11/puls.json'):
            os.remove('./param/aspifile11/puls.json')
            print("puls.json file removed")
    except FileNotFoundError as err_puls:
        print("Error file not found", err_puls)

    try:
        if os.path.exists('./param/aspifile11/sat.json'):
            os.remove('./param/aspifile11/sat.json')
            print("sat.json file removed")
    except FileNotFoundError as err_sat:
        print("Error file not found", err_sat)

    try:
        if os.path.exists('./param/aspifile11/tensor.json'):
            os.remove('./param/aspifile11/tensor.json')
            print("tensor.json file removed")
    except FileNotFoundError as err_ta:
        print("Error file not found", err_ta)

def eraserParam12():
    try:
        if os.path.exists('./param/paramdata12.txt'):
            os.remove('./param/paramdata12.txt')
            print("paramdata12.txt file removed")
    except FileNotFoundError as err_main:
        print("Error file not found", err_main)

    try:
        if os.path.exists('./param/aspifile1/systol.json'):
            os.remove('./param/aspifile1/systol.json')
            print("systol.json file removed")
    except FileNotFoundError as err_syst:
        print("Error file not found", err_syst)

    try:
        if os.path.exists('./param/aspifile1/diastol.json'):
            os.remove('./param/aspifile1/diastol.json')
            print("diastol.json file removed")
    except FileNotFoundError as err_diast:
        print("Error file not found", err_diast)

    try:
        if os.path.exists('./param/aspifile12/temp.json'):
            os.remove('./param/aspifile12/temp.json')
            print("temp.json file removed")
    except FileNotFoundError as err_temp:
        print("Error file not found", err_temp)

    try:
        if os.path.exists('./param/aspifile12/dlr.json'):
            os.remove('./param/aspifile12/dlr.json')
            print("dlr.json file removed")
    except FileNotFoundError as err_dlr:
        print("Error file not found", err_dlr)

    try:
        if os.path.exists('./param/aspifile12/freq.json'):
            os.remove('./param/aspifile12/freq.json')
            print("freq.json file removed")
    except FileNotFoundError as err_freq:
        print("Error file not found", err_freq)

    try:
        if os.path.exists('./param/aspifile12/gly.json'):
            os.remove('./param/aspifile12/gly.json')
            print("gly.json file removed")
    except FileNotFoundError as err_gly:
        print("Error file not found", err_gly)

    try:
        if os.path.exists('./param/aspifile12/puls.json'):
            os.remove('./param/aspifile12/puls.json')
            print("puls.json file removed")
    except FileNotFoundError as err_puls:
        print("Error file not found", err_puls)

    try:
        if os.path.exists('./param/aspifile12/sat.json'):
            os.remove('./param/aspifile12/sat.json')
            print("sat.json file removed")
    except FileNotFoundError as err_sat:
        print("Error file not found", err_sat)

    try:
        if os.path.exists('./param/aspifile12/tensor.json'):
            os.remove('./param/aspifile12/tensor.json')
            print("tensor.json file removed")
    except FileNotFoundError as err_ta:
        print("Error file not found", err_ta)

def eraserParam13():
    try:
        if os.path.exists('./param/paramdata13.txt'):
            os.remove('./param/paramdata13.txt')
            print("paramdata13.txt file removed")
    except FileNotFoundError as err_main:
        print("Error file not found", err_main)

    try:
        if os.path.exists('./param/aspifile1/systol.json'):
            os.remove('./param/aspifile1/systol.json')
            print("systol.json file removed")
    except FileNotFoundError as err_syst:
        print("Error file not found", err_syst)

    try:
        if os.path.exists('./param/aspifile1/diastol.json'):
            os.remove('./param/aspifile1/diastol.json')
            print("diastol.json file removed")
    except FileNotFoundError as err_diast:
        print("Error file not found", err_diast)

    try:
        if os.path.exists('./param/aspifile13/temp.json'):
            os.remove('./param/aspifile13/temp.json')
            print("temp.json file removed")
    except FileNotFoundError as err_temp:
        print("Error file not found", err_temp)

    try:
        if os.path.exists('./param/aspifile13/dlr.json'):
            os.remove('./param/aspifile13/dlr.json')
            print("dlr.json file removed")
    except FileNotFoundError as err_dlr:
        print("Error file not found", err_dlr)

    try:
        if os.path.exists('./param/aspifile13/freq.json'):
            os.remove('./param/aspifile13/freq.json')
            print("freq.json file removed")
    except FileNotFoundError as err_freq:
        print("Error file not found", err_freq)

    try:
        if os.path.exists('./param/aspifile13/gly.json'):
            os.remove('./param/aspifile13/gly.json')
            print("gly.json file removed")
    except FileNotFoundError as err_gly:
        print("Error file not found", err_gly)

    try:
        if os.path.exists('./param/aspifile13/puls.json'):
            os.remove('./param/aspifile13/puls.json')
            print("puls.json file removed")
    except FileNotFoundError as err_puls:
        print("Error file not found", err_puls)

    try:
        if os.path.exists('./param/aspifile13/sat.json'):
            os.remove('./param/aspifile13/sat.json')
            print("sat.json file removed")
    except FileNotFoundError as err_sat:
        print("Error file not found", err_sat)

    try:
        if os.path.exists('./param/aspifile13/tensor.json'):
            os.remove('./param/aspifile13/tensor.json')
            print("tensor.json file removed")
    except FileNotFoundError as err_ta:
        print("Error file not found", err_ta)

def eraserParam14():
    try:
        if os.path.exists('./param/paramdata14.txt'):
            os.remove('./param/paramdata14.txt')
            print("paramdata14.txt file removed")
    except FileNotFoundError as err_main:
        print("Error file not found", err_main)

    try:
        if os.path.exists('./param/aspifile1/systol.json'):
            os.remove('./param/aspifile1/systol.json')
            print("systol.json file removed")
    except FileNotFoundError as err_syst:
        print("Error file not found", err_syst)

    try:
        if os.path.exists('./param/aspifile1/diastol.json'):
            os.remove('./param/aspifile1/diastol.json')
            print("diastol.json file removed")
    except FileNotFoundError as err_diast:
        print("Error file not found", err_diast)

    try:
        if os.path.exists('./param/aspifile14/temp.json'):
            os.remove('./param/aspifile14/temp.json')
            print("temp.json file removed")
    except FileNotFoundError as err_temp:
        print("Error file not found", err_temp)

    try:
        if os.path.exists('./param/aspifile14/dlr.json'):
            os.remove('./param/aspifile14/dlr.json')
            print("dlr.json file removed")
    except FileNotFoundError as err_dlr:
        print("Error file not found", err_dlr)

    try:
        if os.path.exists('./param/aspifile14/freq.json'):
            os.remove('./param/aspifile14/freq.json')
            print("freq.json file removed")
    except FileNotFoundError as err_freq:
        print("Error file not found", err_freq)

    try:
        if os.path.exists('./param/aspifile14/gly.json'):
            os.remove('./param/aspifile14/gly.json')
            print("gly.json file removed")
    except FileNotFoundError as err_gly:
        print("Error file not found", err_gly)

    try:
        if os.path.exists('./param/aspifile14/puls.json'):
            os.remove('./param/aspifile14/puls.json')
            print("puls.json file removed")
    except FileNotFoundError as err_puls:
        print("Error file not found", err_puls)

    try:
        if os.path.exists('./param/aspifile14/sat.json'):
            os.remove('./param/aspifile14/sat.json')
            print("sat.json file removed")
    except FileNotFoundError as err_sat:
        print("Error file not found", err_sat)

    try:
        if os.path.exists('./param/aspifile14/tensor.json'):
            os.remove('./param/aspifile14/tensor.json')
            print("tensor.json file removed")
    except FileNotFoundError as err_ta:
        print("Error file not found", err_ta)

def eraserParam15():
    try:
        if os.path.exists('./param/paramdata15.txt'):
            os.remove('./param/paramdata15.txt')
            print("paramdata15.txt file removed")
    except FileNotFoundError as err_main:
        print("Error file not found", err_main)

    try:
        if os.path.exists('./param/aspifile1/systol.json'):
            os.remove('./param/aspifile1/systol.json')
            print("systol.json file removed")
    except FileNotFoundError as err_syst:
        print("Error file not found", err_syst)

    try:
        if os.path.exists('./param/aspifile1/diastol.json'):
            os.remove('./param/aspifile1/diastol.json')
            print("diastol.json file removed")
    except FileNotFoundError as err_diast:
        print("Error file not found", err_diast)

    try:
        if os.path.exists('./param/aspifile15/temp.json'):
            os.remove('./param/aspifile15/temp.json')
            print("temp.json file removed")
    except FileNotFoundError as err_temp:
        print("Error file not found", err_temp)

    try:
        if os.path.exists('./param/aspifile15/dlr.json'):
            os.remove('./param/aspifile15/dlr.json')
            print("dlr.json file removed")
    except FileNotFoundError as err_dlr:
        print("Error file not found", err_dlr)

    try:
        if os.path.exists('./param/aspifile15/freq.json'):
            os.remove('./param/aspifile15/freq.json')
            print("freq.json file removed")
    except FileNotFoundError as err_freq:
        print("Error file not found", err_freq)

    try:
        if os.path.exists('./param/aspifile15/gly.json'):
            os.remove('./param/aspifile15/gly.json')
            print("gly.json file removed")
    except FileNotFoundError as err_gly:
        print("Error file not found", err_gly)

    try:
        if os.path.exists('./param/aspifile15/puls.json'):
            os.remove('./param/aspifile15/puls.json')
            print("puls.json file removed")
    except FileNotFoundError as err_puls:
        print("Error file not found", err_puls)

    try:
        if os.path.exists('./param/aspifile15/sat.json'):
            os.remove('./param/aspifile15/sat.json')
            print("sat.json file removed")
    except FileNotFoundError as err_sat:
        print("Error file not found", err_sat)

    try:
        if os.path.exists('./param/aspifile15/tensor.json'):
            os.remove('./param/aspifile15/tensor.json')
            print("tensor.json file removed")
    except FileNotFoundError as err_ta:
        print("Error file not found", err_ta)

def eraserParam16():
    try:
        if os.path.exists('./param/paramdata16.txt'):
            os.remove('./param/paramdata16.txt')
            print("paramdata16.txt file removed")
    except FileNotFoundError as err_main:
        print("Error file not found", err_main)

    try:
        if os.path.exists('./param/aspifile1/systol.json'):
            os.remove('./param/aspifile1/systol.json')
            print("systol.json file removed")
    except FileNotFoundError as err_syst:
        print("Error file not found", err_syst)

    try:
        if os.path.exists('./param/aspifile1/diastol.json'):
            os.remove('./param/aspifile1/diastol.json')
            print("diastol.json file removed")
    except FileNotFoundError as err_diast:
        print("Error file not found", err_diast)

    try:
        if os.path.exists('./param/aspifile16/temp.json'):
            os.remove('./param/aspifile16/temp.json')
            print("temp.json file removed")
    except FileNotFoundError as err_temp:
        print("Error file not found", err_temp)

    try:
        if os.path.exists('./param/aspifile16/dlr.json'):
            os.remove('./param/aspifile16/dlr.json')
            print("dlr.json file removed")
    except FileNotFoundError as err_dlr:
        print("Error file not found", err_dlr)

    try:
        if os.path.exists('./param/aspifile16/freq.json'):
            os.remove('./param/aspifile16/freq.json')
            print("freq.json file removed")
    except FileNotFoundError as err_freq:
        print("Error file not found", err_freq)

    try:
        if os.path.exists('./param/aspifile16/gly.json'):
            os.remove('./param/aspifile16/gly.json')
            print("gly.json file removed")
    except FileNotFoundError as err_gly:
        print("Error file not found", err_gly)

    try:
        if os.path.exists('./param/aspifile16/puls.json'):
            os.remove('./param/aspifile16/puls.json')
            print("puls.json file removed")
    except FileNotFoundError as err_puls:
        print("Error file not found", err_puls)

    try:
        if os.path.exists('./param/aspifile16/sat.json'):
            os.remove('./param/aspifile16/sat.json')
            print("sat.json file removed")
    except FileNotFoundError as err_sat:
        print("Error file not found", err_sat)

    try:
        if os.path.exists('./param/aspifile16/tensor.json'):
            os.remove('./param/aspifile16/tensor.json')
            print("tensor.json file removed")
    except FileNotFoundError as err_ta:
        print("Error file not found", err_ta)

def eraserParam17():
    try:
        if os.path.exists('./param/paramdata17.txt'):
            os.remove('./param/paramdata17.txt')
            print("paramdata17.txt file removed")
    except FileNotFoundError as err_main:
        print("Error file not found", err_main)

    try:
        if os.path.exists('./param/aspifile1/systol.json'):
            os.remove('./param/aspifile1/systol.json')
            print("systol.json file removed")
    except FileNotFoundError as err_syst:
        print("Error file not found", err_syst)

    try:
        if os.path.exists('./param/aspifile1/diastol.json'):
            os.remove('./param/aspifile1/diastol.json')
            print("diastol.json file removed")
    except FileNotFoundError as err_diast:
        print("Error file not found", err_diast)

    try:
        if os.path.exists('./param/aspifile17/temp.json'):
            os.remove('./param/aspifile17/temp.json')
            print("temp.json file removed")
    except FileNotFoundError as err_temp:
        print("Error file not found", err_temp)

    try:
        if os.path.exists('./param/aspifile17/dlr.json'):
            os.remove('./param/aspifile17/dlr.json')
            print("dlr.json file removed")
    except FileNotFoundError as err_dlr:
        print("Error file not found", err_dlr)

    try:
        if os.path.exists('./param/aspifile17/freq.json'):
            os.remove('./param/aspifile17/freq.json')
            print("freq.json file removed")
    except FileNotFoundError as err_freq:
        print("Error file not found", err_freq)

    try:
        if os.path.exists('./param/aspifile17/gly.json'):
            os.remove('./param/aspifile17/gly.json')
            print("gly.json file removed")
    except FileNotFoundError as err_gly:
        print("Error file not found", err_gly)

    try:
        if os.path.exists('./param/aspifile17/puls.json'):
            os.remove('./param/aspifile17/puls.json')
            print("puls.json file removed")
    except FileNotFoundError as err_puls:
        print("Error file not found", err_puls)

    try:
        if os.path.exists('./param/aspifile17/sat.json'):
            os.remove('./param/aspifile17/sat.json')
            print("sat.json file removed")
    except FileNotFoundError as err_sat:
        print("Error file not found", err_sat)

    try:
        if os.path.exists('./param/aspifile17/tensor.json'):
            os.remove('./param/aspifile17/tensor.json')
            print("tensor.json file removed")
    except FileNotFoundError as err_ta:
        print("Error file not found", err_ta)

def eraserParam18():
    try:
        if os.path.exists('./param/paramdata18.txt'):
            os.remove('./param/paramdata18.txt')
            print("paramdata18.txt file removed")
    except FileNotFoundError as err_main:
        print("Error file not found", err_main)

    try:
        if os.path.exists('./param/aspifile1/systol.json'):
            os.remove('./param/aspifile1/systol.json')
            print("systol.json file removed")
    except FileNotFoundError as err_syst:
        print("Error file not found", err_syst)

    try:
        if os.path.exists('./param/aspifile1/diastol.json'):
            os.remove('./param/aspifile1/diastol.json')
            print("diastol.json file removed")
    except FileNotFoundError as err_diast:
        print("Error file not found", err_diast)

    try:
        if os.path.exists('./param/aspifile18/temp.json'):
            os.remove('./param/aspifile18/temp.json')
            print("temp.json file removed")
    except FileNotFoundError as err_temp:
        print("Error file not found", err_temp)

    try:
        if os.path.exists('./param/aspifile18/dlr.json'):
            os.remove('./param/aspifile18/dlr.json')
            print("dlr.json file removed")
    except FileNotFoundError as err_dlr:
        print("Error file not found", err_dlr)

    try:
        if os.path.exists('./param/aspifile18/freq.json'):
            os.remove('./param/aspifile18/freq.json')
            print("freq.json file removed")
    except FileNotFoundError as err_freq:
        print("Error file not found", err_freq)

    try:
        if os.path.exists('./param/aspifile18/gly.json'):
            os.remove('./param/aspifile18/gly.json')
            print("gly.json file removed")
    except FileNotFoundError as err_gly:
        print("Error file not found", err_gly)

    try:
        if os.path.exists('./param/aspifile18/puls.json'):
            os.remove('./param/aspifile18/puls.json')
            print("puls.json file removed")
    except FileNotFoundError as err_puls:
        print("Error file not found", err_puls)

    try:
        if os.path.exists('./param/aspifile18/sat.json'):
            os.remove('./param/aspifile18/sat.json')
            print("sat.json file removed")
    except FileNotFoundError as err_sat:
        print("Error file not found", err_sat)

    try:
        if os.path.exists('./param/aspifile18/tensor.json'):
            os.remove('./param/aspifile18/tensor.json')
            print("tensor.json file removed")
    except FileNotFoundError as err_ta:
        print("Error file not found", err_ta)

def eraserParam19():
    try:
        if os.path.exists('./param/paramdata19.txt'):
            os.remove('./param/paramdata19.txt')
            print("paramdata19.txt file removed")
    except FileNotFoundError as err_main:
        print("Error file not found", err_main)

    try:
        if os.path.exists('./param/aspifile1/systol.json'):
            os.remove('./param/aspifile1/systol.json')
            print("systol.json file removed")
    except FileNotFoundError as err_syst:
        print("Error file not found", err_syst)

    try:
        if os.path.exists('./param/aspifile1/diastol.json'):
            os.remove('./param/aspifile1/diastol.json')
            print("diastol.json file removed")
    except FileNotFoundError as err_diast:
        print("Error file not found", err_diast)

    try:
        if os.path.exists('./param/aspifile19/temp.json'):
            os.remove('./param/aspifile19/temp.json')
            print("temp.json file removed")
    except FileNotFoundError as err_temp:
        print("Error file not found", err_temp)

    try:
        if os.path.exists('./param/aspifile19/dlr.json'):
            os.remove('./param/aspifile19/dlr.json')
            print("dlr.json file removed")
    except FileNotFoundError as err_dlr:
        print("Error file not found", err_dlr)

    try:
        if os.path.exists('./param/aspifile19/freq.json'):
            os.remove('./param/aspifile19/freq.json')
            print("freq.json file removed")
    except FileNotFoundError as err_freq:
        print("Error file not found", err_freq)

    try:
        if os.path.exists('./param/aspifile19/gly.json'):
            os.remove('./param/aspifile19/gly.json')
            print("gly.json file removed")
    except FileNotFoundError as err_gly:
        print("Error file not found", err_gly)

    try:
        if os.path.exists('./param/aspifile19/puls.json'):
            os.remove('./param/aspifile19/puls.json')
            print("puls.json file removed")
    except FileNotFoundError as err_puls:
        print("Error file not found", err_puls)

    try:
        if os.path.exists('./param/aspifile19/sat.json'):
            os.remove('./param/aspifile19/sat.json')
            print("sat.json file removed")
    except FileNotFoundError as err_sat:
        print("Error file not found", err_sat)

    try:
        if os.path.exists('./param/aspifile19/tensor.json'):
            os.remove('./param/aspifile19/tensor.json')
            print("tensor.json file removed")
    except FileNotFoundError as err_ta:
        print("Error file not found", err_ta)

def eraserParam20():
    try:
        if os.path.exists('./param/paramdata20.txt'):
            os.remove('./param/paramdata20.txt')
            print("paramdata20.txt file removed")
    except FileNotFoundError as err_main:
        print("Error file not found", err_main)

    try:
        if os.path.exists('./param/aspifile1/systol.json'):
            os.remove('./param/aspifile1/systol.json')
            print("systol.json file removed")
    except FileNotFoundError as err_syst:
        print("Error file not found", err_syst)

    try:
        if os.path.exists('./param/aspifile1/diastol.json'):
            os.remove('./param/aspifile1/diastol.json')
            print("diastol.json file removed")
    except FileNotFoundError as err_diast:
        print("Error file not found", err_diast)

    try:
        if os.path.exists('./param/aspifile20/temp.json'):
            os.remove('./param/aspifile20/temp.json')
            print("temp.json file removed")
    except FileNotFoundError as err_temp:
        print("Error file not found", err_temp)

    try:
        if os.path.exists('./param/aspifile20/dlr.json'):
            os.remove('./param/aspifile20/dlr.json')
            print("dlr.json file removed")
    except FileNotFoundError as err_dlr:
        print("Error file not found", err_dlr)

    try:
        if os.path.exists('./param/aspifile20/freq.json'):
            os.remove('./param/aspifile20/freq.json')
            print("freq.json file removed")
    except FileNotFoundError as err_freq:
        print("Error file not found", err_freq)

    try:
        if os.path.exists('./param/aspifile20/gly.json'):
            os.remove('./param/aspifile20/gly.json')
            print("gly.json file removed")
    except FileNotFoundError as err_gly:
        print("Error file not found", err_gly)

    try:
        if os.path.exists('./param/aspifile20/puls.json'):
            os.remove('./param/aspifile20/puls.json')
            print("puls.json file removed")
    except FileNotFoundError as err_puls:
        print("Error file not found", err_puls)

    try:
        if os.path.exists('./param/aspifile20/sat.json'):
            os.remove('./param/aspifile20/sat.json')
            print("sat.json file removed")
    except FileNotFoundError as err_sat:
        print("Error file not found", err_sat)

    try:
        if os.path.exists('./param/aspifile20/tensor.json'):
            os.remove('./param/aspifile20/tensor.json')
            print("tensor.json file removed")
    except FileNotFoundError as err_ta:
        print("Error file not found", err_ta)

def eraserParam21():
    try:
        if os.path.exists('./param/paramdata21.txt'):
            os.remove('./param/paramdata21.txt')
            print("paramdata21.txt file removed")
    except FileNotFoundError as err_main:
        print("Error file not found", err_main)

    try:
        if os.path.exists('./param/aspifile1/systol.json'):
            os.remove('./param/aspifile1/systol.json')
            print("systol.json file removed")
    except FileNotFoundError as err_syst:
        print("Error file not found", err_syst)

    try:
        if os.path.exists('./param/aspifile1/diastol.json'):
            os.remove('./param/aspifile1/diastol.json')
            print("diastol.json file removed")
    except FileNotFoundError as err_diast:
        print("Error file not found", err_diast)

    try:
        if os.path.exists('./param/aspifile21/temp.json'):
            os.remove('./param/aspifile21/temp.json')
            print("temp.json file removed")
    except FileNotFoundError as err_temp:
        print("Error file not found", err_temp)

    try:
        if os.path.exists('./param/aspifile21/dlr.json'):
            os.remove('./param/aspifile21/dlr.json')
            print("dlr.json file removed")
    except FileNotFoundError as err_dlr:
        print("Error file not found", err_dlr)

    try:
        if os.path.exists('./param/aspifile21/freq.json'):
            os.remove('./param/aspifile21/freq.json')
            print("freq.json file removed")
    except FileNotFoundError as err_freq:
        print("Error file not found", err_freq)

    try:
        if os.path.exists('./param/aspifile21/gly.json'):
            os.remove('./param/aspifile21/gly.json')
            print("gly.json file removed")
    except FileNotFoundError as err_gly:
        print("Error file not found", err_gly)

    try:
        if os.path.exists('./param/aspifile21/puls.json'):
            os.remove('./param/aspifile21/puls.json')
            print("puls.json file removed")
    except FileNotFoundError as err_puls:
        print("Error file not found", err_puls)

    try:
        if os.path.exists('./param/aspifile21/sat.json'):
            os.remove('./param/aspifile21/sat.json')
            print("sat.json file removed")
    except FileNotFoundError as err_sat:
        print("Error file not found", err_sat)

    try:
        if os.path.exists('./param/aspifile21/tensor.json'):
            os.remove('./param/aspifile21/tensor.json')
            print("tensor.json file removed")
    except FileNotFoundError as err_ta:
        print("Error file not found", err_ta)

def eraserParam22():
    try:
        if os.path.exists('./param/paramdata22.txt'):
            os.remove('./param/paramdata22.txt')
            print("paramdata22.txt file removed")
    except FileNotFoundError as err_main:
        print("Error file not found", err_main)

    try:
        if os.path.exists('./param/aspifile1/systol.json'):
            os.remove('./param/aspifile1/systol.json')
            print("systol.json file removed")
    except FileNotFoundError as err_syst:
        print("Error file not found", err_syst)

    try:
        if os.path.exists('./param/aspifile1/diastol.json'):
            os.remove('./param/aspifile1/diastol.json')
            print("diastol.json file removed")
    except FileNotFoundError as err_diast:
        print("Error file not found", err_diast)

    try:
        if os.path.exists('./param/aspifile22/temp.json'):
            os.remove('./param/aspifile22/temp.json')
            print("temp.json file removed")
    except FileNotFoundError as err_temp:
        print("Error file not found", err_temp)

    try:
        if os.path.exists('./param/aspifile22/dlr.json'):
            os.remove('./param/aspifile22/dlr.json')
            print("dlr.json file removed")
    except FileNotFoundError as err_dlr:
        print("Error file not found", err_dlr)

    try:
        if os.path.exists('./param/aspifile22/freq.json'):
            os.remove('./param/aspifile22/freq.json')
            print("freq.json file removed")
    except FileNotFoundError as err_freq:
        print("Error file not found", err_freq)

    try:
        if os.path.exists('./param/aspifile22/gly.json'):
            os.remove('./param/aspifile22/gly.json')
            print("gly.json file removed")
    except FileNotFoundError as err_gly:
        print("Error file not found", err_gly)

    try:
        if os.path.exists('./param/aspifile22/puls.json'):
            os.remove('./param/aspifile22/puls.json')
            print("puls.json file removed")
    except FileNotFoundError as err_puls:
        print("Error file not found", err_puls)

    try:
        if os.path.exists('./param/aspifile22/sat.json'):
            os.remove('./param/aspifile22/sat.json')
            print("sat.json file removed")
    except FileNotFoundError as err_sat:
        print("Error file not found", err_sat)

    try:
        if os.path.exists('./param/aspifile22/tensor.json'):
            os.remove('./param/aspifile22/tensor.json')
            print("tensor.json file removed")
    except FileNotFoundError as err_ta:
        print("Error file not found", err_ta)

def eraserParam23():
    try:
        if os.path.exists('./param/paramdata23.txt'):
            os.remove('./param/paramdata23.txt')
            print("paramdata23.txt file removed")
    except FileNotFoundError as err_main:
        print("Error file not found", err_main)

    try:
        if os.path.exists('./param/aspifile1/systol.json'):
            os.remove('./param/aspifile1/systol.json')
            print("systol.json file removed")
    except FileNotFoundError as err_syst:
        print("Error file not found", err_syst)

    try:
        if os.path.exists('./param/aspifile1/diastol.json'):
            os.remove('./param/aspifile1/diastol.json')
            print("diastol.json file removed")
    except FileNotFoundError as err_diast:
        print("Error file not found", err_diast)

    try:
        if os.path.exists('./param/aspifile23/temp.json'):
            os.remove('./param/aspifile23/temp.json')
            print("temp.json file removed")
    except FileNotFoundError as err_temp:
        print("Error file not found", err_temp)

    try:
        if os.path.exists('./param/aspifile23/dlr.json'):
            os.remove('./param/aspifile23/dlr.json')
            print("dlr.json file removed")
    except FileNotFoundError as err_dlr:
        print("Error file not found", err_dlr)

    try:
        if os.path.exists('./param/aspifile23/freq.json'):
            os.remove('./param/aspifile23/freq.json')
            print("freq.json file removed")
    except FileNotFoundError as err_freq:
        print("Error file not found", err_freq)

    try:
        if os.path.exists('./param/aspifile23/gly.json'):
            os.remove('./param/aspifile23/gly.json')
            print("gly.json file removed")
    except FileNotFoundError as err_gly:
        print("Error file not found", err_gly)

    try:
        if os.path.exists('./param/aspifile23/puls.json'):
            os.remove('./param/aspifile23/puls.json')
            print("puls.json file removed")
    except FileNotFoundError as err_puls:
        print("Error file not found", err_puls)

    try:
        if os.path.exists('./param/aspifile23/sat.json'):
            os.remove('./param/aspifile23/sat.json')
            print("sat.json file removed")
    except FileNotFoundError as err_sat:
        print("Error file not found", err_sat)

    try:
        if os.path.exists('./param/aspifile23/tensor.json'):
            os.remove('./param/aspifile23/tensor.json')
            print("tensor.json file removed")
    except FileNotFoundError as err_ta:
        print("Error file not found", err_ta)

def eraserParam24():
    try:
        if os.path.exists('./param/paramdata24.txt'):
            os.remove('./param/paramdata24.txt')
            print("paramdata24.txt file removed")
    except FileNotFoundError as err_main:
        print("Error file not found", err_main)

    try:
        if os.path.exists('./param/aspifile1/systol.json'):
            os.remove('./param/aspifile1/systol.json')
            print("systol.json file removed")
    except FileNotFoundError as err_syst:
        print("Error file not found", err_syst)

    try:
        if os.path.exists('./param/aspifile1/diastol.json'):
            os.remove('./param/aspifile1/diastol.json')
            print("diastol.json file removed")
    except FileNotFoundError as err_diast:
        print("Error file not found", err_diast)

    try:
        if os.path.exists('./param/aspifile24/temp.json'):
            os.remove('./param/aspifile24/temp.json')
            print("temp.json file removed")
    except FileNotFoundError as err_temp:
        print("Error file not found", err_temp)

    try:
        if os.path.exists('./param/aspifile24/dlr.json'):
            os.remove('./param/aspifile24/dlr.json')
            print("dlr.json file removed")
    except FileNotFoundError as err_dlr:
        print("Error file not found", err_dlr)

    try:
        if os.path.exists('./param/aspifile24/freq.json'):
            os.remove('./param/aspifile24/freq.json')
            print("freq.json file removed")
    except FileNotFoundError as err_freq:
        print("Error file not found", err_freq)

    try:
        if os.path.exists('./param/aspifile24/gly.json'):
            os.remove('./param/aspifile24/gly.json')
            print("gly.json file removed")
    except FileNotFoundError as err_gly:
        print("Error file not found", err_gly)

    try:
        if os.path.exists('./param/aspifile24/puls.json'):
            os.remove('./param/aspifile24/puls.json')
            print("puls.json file removed")
    except FileNotFoundError as err_puls:
        print("Error file not found", err_puls)

    try:
        if os.path.exists('./param/aspifile24/sat.json'):
            os.remove('./param/aspifile24/sat.json')
            print("sat.json file removed")
    except FileNotFoundError as err_sat:
        print("Error file not found", err_sat)

    try:
        if os.path.exists('./param/aspifile24/tensor.json'):
            os.remove('./param/aspifile24/tensor.json')
            print("tensor.json file removed")
    except FileNotFoundError as err_ta:
        print("Error file not found", err_ta)
