#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
    It checks if the end date of the reserve corresponds
    to today's date. If yes, convdose.json is modify and
    upload to server.
"""


from tkinter import *
from tkinter import messagebox
from medic_upload.stop_res import uploadstopres
from medic_upload.stop_res import upload2stopres
from medic_upload.stop_res import upload3stopres
from medic_upload.stop_res import upload4stopres
from medic_upload.stop_res import upload5stopres
from medic_upload.stop_res import upload6stopres
from medic_upload.stop_res import upload7stopres
from medic_upload.stop_res import upload8stopres
from medic_upload.stop_res import upload9stopres
from medic_upload.stop_res import upload10stopres
from medic_upload.stop_res import upload11stopres
from medic_upload.stop_res import upload12stopres
from medic_upload.stop_res import upload13stopres
from medic_upload.stop_res import upload14stopres
from medic_upload.stop_res import upload15stopres
from medic_upload.stop_res import upload16stopres
from medic_upload.stop_res import upload17stopres
from medic_upload.stop_res import upload18stopres
from medic_upload.stop_res import upload19stopres
from medic_upload.stop_res import upload20stopres
from medic_upload.stop_res import upload21stopres
from medic_upload.stop_res import upload22stopres
from medic_upload.stop_res import upload23stopres
from medic_upload.stop_res import upload24stopres
import json
import os
import subprocess
import time
import datetime


def dispResBox():
    """
        To search the end date into the intro_res.txt
        and display alert to stop reserve !
    """
    try:
        with open('./newpatient/entryfile.txt', 'r') as namefile:
            res_text1 = namefile.readline()
    except FileNotFoundError as callfile:
        print("[!] File entryfile.txt doesn't exist !", callfile)

    try:
        word_ttstop = (datetime.datetime.now() + \
            datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        file = open('./ttt/doc_ttt/convres.json')
        data = json.load(file)
        for (key, value) in data.items():
            listdata_x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            for x in listdata_x:
                print(str(value[x]["Date of end"]))
                date_end = (str(value[x]["Date of end"]))
                if date_end == word_ttstop:
                    print(date_end)
                    name_treat = (str(value[x]["Treatment"]))
                    print(name_treat)
                    dose_ttt = (str(value[x]["Dosage"]))
                    print(dose_ttt)
                    MSBTTT2 = messagebox.showwarning('Warning',
                        'Look at Reserve, there is a reserve to stop at' + " " + \
                        word_ttstop + " " + "for : " + res_text1 + \
                        "\n" + "Date of end : " + date_end + "\n" + name_treat + \
                        " " + dose_ttt)
                    MSGBOX = messagebox.askyesno("Ask", "Do you want to stop "\
                        "this reminder for the Reserve : " + name_treat + " " + \
                        dose_ttt + " of " + res_text1 + " ?")
                    if MSGBOX == 1:
                        print("Reminder stop R !")
                        file = open('./ttt/doc_ttt/convres.json')
                        data = json.load(file)
                        for (key, value) in data.items():
                            listdata_x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
                            for x in listdata_x:
                                date_end = (str(value[x]["Date of end"]))
                                if date_end == word_ttstop:
                                    print(date_end)
                                    intro_date = (str(value[x]["Date of introduction"]))
                                    name_treat = (str(value[x]["Treatment"]))
                                    print(name_treat)
                                    dose_ttt = (str(value[x]["Dosage"]))
                                    print(dose_ttt)
                                    if value[x]["Date of end"] in word_ttstop:
                                        value[x]['Date of end'] = "! STOP ! - " + word_ttstop
                                    with open('./ttt/doc_ttt/convres.json', 'w') as re_file:
                                        json.dump(data, re_file, indent=4)
                                    uploadstopres()
                                    break
    except IndexError as error_ttt:
        print("[!] No date of end has been found into file convres.json (patient 1)",
            error_ttt)
    except FileNotFoundError as info_ttt:
        print("[!] No date of end has been found into file convres.json (patient 1)",
            info_ttt)
    else:
        print("[Err_3] It's not date of end for resapp.py 1")

    try:
        with open('./newpatient/entryfile2.txt', 'r') as namefile2:
            res_text2 = namefile2.readline()
    except FileNotFoundError as callfile2:
        print("[!] File entryfile2.txt doesn't exist !", callfile2)

    try:
        word_ttstop2 = (datetime.datetime.now() + \
            datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        file2 = open('./ttt/doc_ttt2/convres.json')
        data2 = json.load(file2)
        for (key, value) in data2.items():
            listdata2_x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            for x in listdata2_x:
                print(str(value[x]["Date of end"]))
                date_end2 = (str(value[x]["Date of end"]))
                if date_end2 == word_ttstop2:
                    print(date_end2)
                    name_treat2 = (str(value[x]["Treatment"]))
                    print(name_treat2)
                    dose_ttt2 = (str(value[x]["Dosage"]))
                    print(dose_ttt2)
                    MSBTTT2 = messagebox.showwarning('Warning',
                        'Look at Reserve, there is a reserve to stop at' + " " + \
                        word_ttstop2 + " " + "for : " + res_text2 + \
                        "\n" + "Date of end : " + date_end2 + "\n" + name_treat2 + \
                        " " + dose_ttt2)
                    MSGBOX = messagebox.askyesno("Ask", "Do you want to stop "\
                        "this reminder for the Reserve : " + name_treat2 + " " + \
                        dose_ttt2 + " of " + res_text2 + " ?")
                    if MSGBOX == 1:
                        print("Reminder stop !")
                        file = open('./ttt/doc_ttt2/convres.json')
                        data = json.load(file)
                        for (key, value) in data.items():
                            listdata_x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
                            for x in listdata_x:
                                date_end = (str(value[x]["Date of end"]))
                                if date_end == word_ttstop:
                                    print(date_end)
                                    intro_date = (str(value[x]["Date of introduction"]))
                                    name_treat = (str(value[x]["Treatment"]))
                                    print(name_treat)
                                    dose_ttt = (str(value[x]["Dosage"]))
                                    print(dose_ttt)
                                    if value[x]["Date of end"] in word_ttstop:
                                        value[x]['Date of end'] = "! STOP ! - " + word_ttstop
                                    with open('./ttt/doc_ttt2/convres.json', 'w') as re_file:
                                        json.dump(data, re_file, indent=4)
                                    upload2stopres()
                                    break
    except IndexError as error_ttt2:
        print("[!] No date of end has been found into file convres.json (patient 2)",
            error_ttt2)
    except FileNotFoundError as info_ttt2:
        print("[!] No date of end has been found into file convres.json (patient 2)",
            info_ttt2)
    else:
        print("[Err_3] It's not date of end for resapp.py 2")

    try:
        with open('./newpatient/entryfile3.txt', 'r') as namefile3:
            res_text3 = namefile3.readline()
    except FileNotFoundError as callfile3:
        print("[!] File entryfile3.txt doesn't exist !", callfile3)

    try:
        word_ttstop3 = (datetime.datetime.now() + \
            datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        file3 = open('./ttt/doc_ttt3/convres.json')
        data3 = json.load(file3)
        for (key, value) in data3.items():
            listdata3_x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            for x in listdata3_x:
                print(str(value[x]["Date of end"]))
                date_end3 = (str(value[x]["Date of end"]))
                if date_end3 == word_ttstop3:
                    print(date_end3)
                    name_treat3 = (str(value[x]["Treatment"]))
                    print(name_treat3)
                    dose_ttt3 = (str(value[x]["Dosage"]))
                    print(dose_ttt3)
                    MSBTTT3 = messagebox.showwarning('Warning',
                        'Look at Reserve, there is a reserve to stop at' + " " + \
                        word_ttstop3 + " " + "for : " + res_text3 + \
                        "\n" + "Date of end : " + date_end3 + "\n" + name_treat3 + \
                        " " + dose_ttt3)
                    MSGBOX = messagebox.askyesno("Ask", "Do you want to stop "\
                        "this reminder for the Reserve : " + name_treat3 + " " + \
                        dose_ttt3 + " of " + res_text3 + " ?")
                    if MSGBOX == 1:
                        print("Reminder stop !")
                        file = open('./ttt/doc_ttt3/convres.json')
                        data = json.load(file)
                        for (key, value) in data.items():
                            listdata_x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
                            for x in listdata_x:
                                date_end = (str(value[x]["Date of end"]))
                                if date_end == word_ttstop:
                                    print(date_end)
                                    intro_date = (str(value[x]["Date of introduction"]))
                                    name_treat = (str(value[x]["Treatment"]))
                                    print(name_treat)
                                    dose_ttt = (str(value[x]["Dosage"]))
                                    print(dose_ttt)
                                    if value[x]["Date of end"] in word_ttstop:
                                        value[x]['Date of end'] = "! STOP ! - " + word_ttstop
                                    with open('./ttt/doc_ttt3/convres.json', 'w') as re_file:
                                        json.dump(data, re_file, indent=4)
                                    upload3stopres()
                                    break
    except IndexError as error_ttt3:
        print("[!] No date of end has been found into file convres.json (patient 3)",
            error_ttt3)
    except FileNotFoundError as info_ttt3:
        print("[!] No date of end has been found into file convres.json (patient 3)",
            info_ttt3)
    else:
        print("[Err_3] It's not date of end for resapp.py 3")

    try:
        with open('./newpatient/entryfile4.txt', 'r') as namefile4:
            res_text4 = namefile4.readline()
    except FileNotFoundError as callfile4:
        print("[!] File entryfile4.txt doesn't exist !", callfile4)

    try:
        word_ttstop4 = (datetime.datetime.now() + \
            datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        file4 = open('./ttt/doc_ttt4/convres.json')
        data4 = json.load(file4)
        for (key, value) in data4.items():
            listdata4_x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            for x in listdata4_x:
                print(str(value[x]["Date of end"]))
                date_end4 = (str(value[x]["Date of end"]))
                if date_end4 == word_ttstop4:
                    print(date_end4)
                    name_treat4 = (str(value[x]["Treatment"]))
                    print(name_treat4)
                    dose_ttt4 = (str(value[x]["Dosage"]))
                    print(dose_ttt4)
                    MSBTTT4 = messagebox.showwarning('Warning',
                        'Look at Reserve, there is a reserve to stop at' + " " + \
                        word_ttstop4 + " " + "for : " + res_text4 + \
                        "\n" + "Date of end : " + date_end4 + "\n" + name_treat4 + \
                        " " + dose_ttt4)
                    MSGBOX = messagebox.askyesno("Ask", "Do you want to stop "\
                        "this reminder for the Reserve : " + name_treat4 + " " + \
                        dose_ttt4 + " of " + res_text4 + " ?")
                    if MSGBOX == 1:
                        print("Reminder stop !")
                        file = open('./ttt/doc_ttt4/convres.json')
                        data = json.load(file)
                        for (key, value) in data.items():
                            listdata_x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
                            for x in listdata_x:
                                date_end = (str(value[x]["Date of end"]))
                                if date_end == word_ttstop:
                                    print(date_end)
                                    intro_date = (str(value[x]["Date of introduction"]))
                                    name_treat = (str(value[x]["Treatment"]))
                                    print(name_treat)
                                    dose_ttt = (str(value[x]["Dosage"]))
                                    print(dose_ttt)
                                    if value[x]["Date of end"] in word_ttstop:
                                        value[x]['Date of end'] = "! STOP ! - " + word_ttstop
                                    with open('./ttt/doc_ttt4/convres.json', 'w') as re_file:
                                        json.dump(data, re_file, indent=4)
                                    upload4stopres()
                                    break
    except IndexError as error_ttt4:
        print("[!] No date of end has been found into file convres.json (patient 4)",
            error_ttt4)
    except FileNotFoundError as info_ttt4:
        print("[!] No date of end has been found into file convres.json (patient 4)",
            info_ttt4)
    else:
        print("[Err_3] It's not date of end for resapp.py 4")

    try:
        with open('./newpatient/entryfile5.txt', 'r') as namefile5:
            res_text5 = namefile5.readline()
    except FileNotFoundError as callfile5:
        print("[!] File entryfile5.txt doesn't exist !", callfile5)

    try:
        word_ttstop5 = (datetime.datetime.now() + \
            datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        file5 = open('./ttt/doc_ttt5/convres.json')
        data5 = json.load(file5)
        for (key, value) in data5.items():
            listdata5_x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            for x in listdata5_x:
                print(str(value[x]["Date of end"]))
                date_end5 = (str(value[x]["Date of end"]))
                if date_end5 == word_ttstop5:
                    print(date_end5)
                    name_treat5 = (str(value[x]["Treatment"]))
                    print(name_treat5)
                    dose_ttt5 = (str(value[x]["Dosage"]))
                    print(dose_ttt5)
                    MSBTTT5 = messagebox.showwarning('Warning',
                        'Look at Reserve, there is a reserve to stop at' + " " + \
                        word_ttstop5 + " " + "for : " + res_text5 + \
                        "\n" + "Date of end : " + date_end5 + "\n" + name_treat5 + \
                        " " + dose_ttt5)
                    MSGBOX = messagebox.askyesno("Ask", "Do you want to stop "\
                        "this reminder for the Reserve : " + name_treat5 + " " + \
                        dose_ttt5 + " of " + res_text5 + " ?")
                    if MSGBOX == 1:
                        print("Reminder stop !")
                        file = open('./ttt/doc_ttt5/convres.json')
                        data = json.load(file)
                        for (key, value) in data.items():
                            listdata_x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
                            for x in listdata_x:
                                date_end = (str(value[x]["Date of end"]))
                                if date_end == word_ttstop:
                                    print(date_end)
                                    intro_date = (str(value[x]["Date of introduction"]))
                                    name_treat = (str(value[x]["Treatment"]))
                                    print(name_treat)
                                    dose_ttt = (str(value[x]["Dosage"]))
                                    print(dose_ttt)
                                    if value[x]["Date of end"] in word_ttstop:
                                        value[x]['Date of end'] = "! STOP ! - " + word_ttstop
                                    with open('./ttt/doc_ttt5/convres.json', 'w') as re_file:
                                        json.dump(data, re_file, indent=4)
                                    upload5stopres()
                                    break
    except IndexError as error_ttt5:
        print("[!] No date of end has been found into file convres.json (patient 5)",
            error_ttt5)
    except FileNotFoundError as info_ttt5:
        print("[!] No date of end has been found into file convres.json (patient 5)",
            info_ttt5)
    else:
        print("[Err_3] It's not date of end for resapp.py 5")

    try:
        with open('./newpatient/entryfile6.txt', 'r') as namefile6:
            res_text6 = namefile6.readline()
    except FileNotFoundError as callfile6:
        print("[!] File entryfile6.txt doesn't exist !", callfile6)

    try:
        word_ttstop6 = (datetime.datetime.now() + \
            datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        file6 = open('./ttt/doc_ttt6/convres.json')
        data6 = json.load(file6)
        for (key, value) in data6.items():
            listdata6_x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            for x in listdata6_x:
                print(str(value[x]["Date of end"]))
                date_end6 = (str(value[x]["Date of end"]))
                if date_end6 == word_ttstop6:
                    print(date_end6)
                    name_treat6 = (str(value[x]["Treatment"]))
                    print(name_treat6)
                    dose_ttt6 = (str(value[x]["Dosage"]))
                    print(dose_ttt6)
                    MSBTTT6 = messagebox.showwarning('Warning',
                        'Look at Reserve, there is a reserve to stop at' + " " + \
                        word_ttstop6 + " " + "for : " + res_text6 + \
                        "\n" + "Date of end : " + date_end6 + "\n" + name_treat6 + \
                        " " + dose_ttt6)
                    MSGBOX = messagebox.askyesno("Ask", "Do you want to stop "\
                        "this reminder for the Reserve : " + name_treat6 + " " + \
                        dose_ttt6 + " of " + res_text6 + " ?")
                    if MSGBOX == 1:
                        print("Reminder stop !")
                        file = open('./ttt/doc_ttt6/convres.json')
                        data = json.load(file)
                        for (key, value) in data.items():
                            listdata_x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
                            for x in listdata_x:
                                date_end = (str(value[x]["Date of end"]))
                                if date_end == word_ttstop:
                                    print(date_end)
                                    intro_date = (str(value[x]["Date of introduction"]))
                                    name_treat = (str(value[x]["Treatment"]))
                                    print(name_treat)
                                    dose_ttt = (str(value[x]["Dosage"]))
                                    print(dose_ttt)
                                    if value[x]["Date of end"] in word_ttstop:
                                        value[x]['Date of end'] = "! STOP ! - " + word_ttstop
                                    with open('./ttt/doc_ttt6/convres.json', 'w') as re_file:
                                        json.dump(data, re_file, indent=4)
                                    upload6stopres()
                                    break
    except IndexError as error_ttt6:
        print("[!] No date of end has been found into file convres.json (patient 6)",
            error_ttt6)
    except FileNotFoundError as info_ttt6:
        print("[!] No date of end has been found into file convres.json (patient 6)",
            info_ttt6)
    else:
        print("[Err_3] It's not date of end for resapp.py 6")

    try:
        with open('./newpatient/entryfile7.txt', 'r') as namefile7:
            res_text7 = namefile7.readline()
    except FileNotFoundError as callfile7:
        print("[!] File entryfile7.txt doesn't exist !", callfile7)

    try:
        word_ttstop7 = (datetime.datetime.now() + \
            datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        file7 = open('./ttt/doc_ttt7/convres.json')
        data7 = json.load(file7)
        for (key, value) in data7.items():
            listdata7_x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            for x in listdata7_x:
                print(str(value[x]["Date of end"]))
                date_end7 = (str(value[x]["Date of end"]))
                if date_end7 == word_ttstop7:
                    print(date_end7)
                    name_treat7 = (str(value[x]["Treatment"]))
                    print(name_treat7)
                    dose_ttt7 = (str(value[x]["Dosage"]))
                    print(dose_ttt7)
                    MSBTTT7 = messagebox.showwarning('Warning',
                        'Look at Reserve, there is a reserve to stop at' + " " + \
                        word_ttstop7 + " " + "for : " + res_text7 + \
                        "\n" + "Date of end : " + date_end7 + "\n" + name_treat7 + \
                        " " + dose_ttt7)
                    MSGBOX = messagebox.askyesno("Ask", "Do you want to stop "\
                        "this reminder for the Reserve : " + name_treat7 + " " + \
                        dose_ttt7 + " of " + res_text7 + " ?")
                    if MSGBOX == 1:
                        print("Reminder stop !")
                        file = open('./ttt/doc_ttt7/convres.json')
                        data = json.load(file)
                        for (key, value) in data.items():
                            listdata_x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
                            for x in listdata_x:
                                date_end = (str(value[x]["Date of end"]))
                                if date_end == word_ttstop:
                                    print(date_end)
                                    intro_date = (str(value[x]["Date of introduction"]))
                                    name_treat = (str(value[x]["Treatment"]))
                                    print(name_treat)
                                    dose_ttt = (str(value[x]["Dosage"]))
                                    print(dose_ttt)
                                    if value[x]["Date of end"] in word_ttstop:
                                        value[x]['Date of end'] = "! STOP ! - " + word_ttstop
                                    with open('./ttt/doc_ttt7/convres.json', 'w') as re_file:
                                        json.dump(data, re_file, indent=4)
                                    upload7stopres()
                                    break
    except IndexError as error_ttt7:
        print("[!] No date of end has been found into file convres.json (patient 7)",
            error_ttt7)
    except FileNotFoundError as info_ttt7:
        print("[!] No date of end has been found into file convres.json (patient 7)",
            info_ttt7)
    else:
        print("[Err_3] It's not date of end for resapp.py 7")

    try:
        with open('./newpatient/entryfile8.txt', 'r') as namefile8:
            res_text8 = namefile8.readline()
    except FileNotFoundError as callfile8:
        print("[!] File entryfile8.txt doesn't exist !", callfile8)

    try:
        word_ttstop8 = (datetime.datetime.now() + \
            datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        file8 = open('./ttt/doc_ttt8/convres.json')
        data8 = json.load(file8)
        for (key, value) in data8.items():
            listdata8_x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            for x in listdata8_x:
                print(str(value[x]["Date of end"]))
                date_end8 = (str(value[x]["Date of end"]))
                if date_end8 == word_ttstop8:
                    print(date_end8)
                    name_treat8 = (str(value[x]["Treatment"]))
                    print(name_treat8)
                    dose_ttt8 = (str(value[x]["Dosage"]))
                    print(dose_ttt8)
                    MSBTTT8 = messagebox.showwarning('Warning',
                        'Look at Reserve, there is a reserve to stop at' + " " + \
                        word_ttstop8 + " " + "for : " + res_text8 + \
                        "\n" + "Date of end : " + date_end8 + "\n" + name_treat8 + \
                        " " + dose_ttt8)
                    MSGBOX = messagebox.askyesno("Ask", "Do you want to stop "\
                        "this reminder for the Reserve : " + name_treat8 + " " + \
                        dose_ttt8 + " of " + res_text8 + " ?")
                    if MSGBOX == 1:
                        print("Reminder stop !")
                        file = open('./ttt/doc_ttt8/convres.json')
                        data = json.load(file)
                        for (key, value) in data.items():
                            listdata_x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
                            for x in listdata_x:
                                date_end = (str(value[x]["Date of end"]))
                                if date_end == word_ttstop:
                                    print(date_end)
                                    intro_date = (str(value[x]["Date of introduction"]))
                                    name_treat = (str(value[x]["Treatment"]))
                                    print(name_treat)
                                    dose_ttt = (str(value[x]["Dosage"]))
                                    print(dose_ttt)
                                    if value[x]["Date of end"] in word_ttstop:
                                        value[x]['Date of end'] = "! STOP ! - " + word_ttstop
                                    with open('./ttt/doc_ttt8/convres.json', 'w') as re_file:
                                        json.dump(data, re_file, indent=4)
                                    upload8stopres()
                                    break
    except IndexError as error_ttt8:
        print("[!] No date of end has been found into file convres.json (patient 8)",
            error_ttt8)
    except FileNotFoundError as info_ttt8:
        print("[!] No date of end has been found into file convres.json (patient 8)",
            info_ttt8)
    else:
        print("[Err_3] It's not date of end for resapp.py 8")

    try:
        with open('./newpatient/entryfile9.txt', 'r') as namefile9:
            res_text9 = namefile9.readline()
    except FileNotFoundError as callfile9:
        print("[!] File entryfile9.txt doesn't exist !", callfile9)

    try:
        word_ttstop9 = (datetime.datetime.now() + \
            datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        file9 = open('./ttt/doc_ttt9/convres.json')
        data9 = json.load(file9)
        for (key, value) in data9.items():
            listdata9_x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            for x in listdata9_x:
                print(str(value[x]["Date of end"]))
                date_end9 = (str(value[x]["Date of end"]))
                if date_end9 == word_ttstop9:
                    print(date_end9)
                    name_treat9 = (str(value[x]["Treatment"]))
                    print(name_treat9)
                    dose_ttt9 = (str(value[x]["Dosage"]))
                    print(dose_ttt9)
                    MSBTTT9 = messagebox.showwarning('Warning',
                        'Look at Reserve, there is a reserve to stop at' + " " + \
                        word_ttstop9 + " " + "for : " + res_text9 + \
                        "\n" + "Date of end : " + date_end9 + "\n" + name_treat9 + \
                        " " + dose_ttt9)
                    MSGBOX = messagebox.askyesno("Ask", "Do you want to stop "\
                        "this reminder for the Reserve : " + name_treat9 + " " + \
                        dose_ttt9 + " of " + res_text9 + " ?")
                    if MSGBOX == 1:
                        print("Reminder stop !")
                        file = open('./ttt/doc_ttt9/convres.json')
                        data = json.load(file)
                        for (key, value) in data.items():
                            listdata_x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
                            for x in listdata_x:
                                date_end = (str(value[x]["Date of end"]))
                                if date_end == word_ttstop:
                                    print(date_end)
                                    intro_date = (str(value[x]["Date of introduction"]))
                                    name_treat = (str(value[x]["Treatment"]))
                                    print(name_treat)
                                    dose_ttt = (str(value[x]["Dosage"]))
                                    print(dose_ttt)
                                    if value[x]["Date of end"] in word_ttstop:
                                        value[x]['Date of end'] = "! STOP ! - " + word_ttstop
                                    with open('./ttt/doc_ttt9/convres.json', 'w') as re_file:
                                        json.dump(data, re_file, indent=4)
                                    upload9stopres()
                                    break
    except IndexError as error_ttt9:
        print("[!] No date of end has been found into file convres.json (patient 9)",
            error_ttt9)
    except FileNotFoundError as info_ttt9:
        print("[!] No date of end has been found into file convres.json (patient 9)",
            info_ttt9)
    else:
        print("[Err_3] It's not date of end for resapp.py 9")

    try:
        with open('./newpatient/entryfile10.txt', 'r') as namefile10:
            res_text10 = namefile10.readline()
    except FileNotFoundError as callfile10:
        print("[!] File entryfile10.txt doesn't exist !", callfile10)

    try:
        word_ttstop10 = (datetime.datetime.now() + \
            datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        file10 = open('./ttt/doc_ttt10/convres.json')
        data10 = json.load(file10)
        for (key, value) in data10.items():
            listdata10_x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            for x in listdata10_x:
                print(str(value[x]["Date of end"]))
                date_end10 = (str(value[x]["Date of end"]))
                if date_end10 == word_ttstop10:
                    print(date_end10)
                    name_treat10 = (str(value[x]["Treatment"]))
                    print(name_treat10)
                    dose_ttt10 = (str(value[x]["Dosage"]))
                    print(dose_ttt10)
                    MSBTTT10 = messagebox.showwarning('Warning',
                        'Look at Reserve, there is a reserve to stop at' + " " + \
                        word_ttstop10 + " " + "for : " + res_text10 + \
                        "\n" + "Date of end : " + date_end10 + "\n" + name_treat10 + \
                        " " + dose_ttt10)
                    MSGBOX = messagebox.askyesno("Ask", "Do you want to stop "\
                        "this reminder for the Reserve : " + name_treat10 + " " + \
                        dose_ttt10 + " of " + res_text10 + " ?")
                    if MSGBOX == 1:
                        print("Reminder stop !")
                        file = open('./ttt/doc_ttt10/convres.json')
                        data = json.load(file)
                        for (key, value) in data.items():
                            listdata_x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
                            for x in listdata_x:
                                date_end = (str(value[x]["Date of end"]))
                                if date_end == word_ttstop:
                                    print(date_end)
                                    intro_date = (str(value[x]["Date of introduction"]))
                                    name_treat = (str(value[x]["Treatment"]))
                                    print(name_treat)
                                    dose_ttt = (str(value[x]["Dosage"]))
                                    print(dose_ttt)
                                    if value[x]["Date of end"] in word_ttstop:
                                        value[x]['Date of end'] = "! STOP ! - " + word_ttstop
                                    with open('./ttt/doc_ttt10/convres.json', 'w') as re_file:
                                        json.dump(data, re_file, indent=4)
                                    upload10stopres()
                                    break
    except IndexError as error_ttt10:
        print("[!] No date of end has been found into file convres.json (patient 10)",
            error_ttt10)
    except FileNotFoundError as info_ttt10:
        print("[!] No date of end has been found into file convres.json (patient 10)",
            info_ttt10)
    else:
        print("[Err_3] It's not date of end for resapp.py 10")

    try:
        with open('./newpatient/entryfile11.txt', 'r') as namefile11:
            res_text11 = namefile11.readline()
    except FileNotFoundError as callfile11:
        print("[!] File entryfile11.txt doesn't exist !", callfile11)

    try:
        word_ttstop11 = (datetime.datetime.now() + \
            datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        file11 = open('./ttt/doc_ttt11/convres.json')
        data11 = json.load(file11)
        for (key, value) in data11.items():
            listdata11_x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            for x in listdata11_x:
                print(str(value[x]["Date of end"]))
                date_end11 = (str(value[x]["Date of end"]))
                if date_end11 == word_ttstop11:
                    print(date_end11)
                    name_treat11 = (str(value[x]["Treatment"]))
                    print(name_treat11)
                    dose_ttt11 = (str(value[x]["Dosage"]))
                    print(dose_ttt11)
                    MSBTTT11 = messagebox.showwarning('Warning',
                        'Look at Reserve, there is a reserve to stop at' + " " + \
                        word_ttstop11 + " " + "for : " + res_text11 + \
                        "\n" + "Date of end : " + date_end11 + "\n" + name_treat11 + \
                        " " + dose_ttt11)
                    MSGBOX = messagebox.askyesno("Ask", "Do you want to stop "\
                        "this reminder for the Reserve : " + name_treat11 + " " + \
                        dose_ttt11 + " of " + res_text11 + " ?")
                    if MSGBOX == 1:
                        print("Reminder stop !")
                        file = open('./ttt/doc_ttt11/convres.json')
                        data = json.load(file)
                        for (key, value) in data.items():
                            listdata_x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
                            for x in listdata_x:
                                date_end = (str(value[x]["Date of end"]))
                                if date_end == word_ttstop:
                                    print(date_end)
                                    intro_date = (str(value[x]["Date of introduction"]))
                                    name_treat = (str(value[x]["Treatment"]))
                                    print(name_treat)
                                    dose_ttt = (str(value[x]["Dosage"]))
                                    print(dose_ttt)
                                    if value[x]["Date of end"] in word_ttstop:
                                        value[x]['Date of end'] = "! STOP ! - " + word_ttstop
                                    with open('./ttt/doc_ttt11/convres.json', 'w') as re_file:
                                        json.dump(data, re_file, indent=4)
                                    upload11stopres()
                                    break
    except IndexError as error_ttt11:
        print("[!] No date of end has been found into file convres.json (patient 11)",
            error_ttt11)
    except FileNotFoundError as info_ttt11:
        print("[!] No date of end has been found into file convres.json (patient 11)",
            info_ttt11)
    else:
        print("[Err_3] It's not date of end for resapp.py 11")

    try:
        with open('./newpatient/entryfile12.txt', 'r') as namefile12:
            res_text12 = namefile12.readline()
    except FileNotFoundError as callfile12:
        print("[!] File entryfile12.txt doesn't exist !", callfile12)

    try:
        word_ttstop12 = (datetime.datetime.now() + \
            datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        file12 = open('./ttt/doc_ttt12/convres.json')
        data12 = json.load(file12)
        for (key, value) in data12.items():
            listdata12_x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            for x in listdata12_x:
                print(str(value[x]["Date of end"]))
                date_end12 = (str(value[x]["Date of end"]))
                if date_end12 == word_ttstop12:
                    print(date_end12)
                    name_treat12 = (str(value[x]["Treatment"]))
                    print(name_treat12)
                    dose_ttt12 = (str(value[x]["Dosage"]))
                    print(dose_ttt12)
                    MSBTTT12 = messagebox.showwarning('Warning',
                        'Look at Reserve, there is a reserve to stop at' + " " + \
                        word_ttstop12 + " " + "for : " + res_text12 + \
                        "\n" + "Date of end : " + date_end12 + "\n" + name_treat12 + \
                        " " + dose_ttt12)
                    MSGBOX = messagebox.askyesno("Ask", "Do you want to stop "\
                        "this reminder for the Reserve : "\
                        + name_treat12 + " " + dose_ttt12 + " of " + res_text12 + " ?")
                    if MSGBOX == 1:
                        print("Reminder stop !")
                        file = open('./ttt/doc_ttt12/convres.json')
                        data = json.load(file)
                        for (key, value) in data.items():
                            listdata_x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
                            for x in listdata_x:
                                date_end = (str(value[x]["Date of end"]))
                                if date_end == word_ttstop:
                                    print(date_end)
                                    intro_date = (str(value[x]["Date of introduction"]))
                                    name_treat = (str(value[x]["Treatment"]))
                                    print(name_treat)
                                    dose_ttt = (str(value[x]["Dosage"]))
                                    print(dose_ttt)
                                    if value[x]["Date of end"] in word_ttstop:
                                        value[x]['Date of end'] = "! STOP ! - " + word_ttstop
                                    with open('./ttt/doc_ttt12/convres.json', 'w') as re_file:
                                        json.dump(data, re_file, indent=4)
                                    upload12stopres()
                                    break
    except IndexError as error_ttt12:
        print("[!] No date of end has been found into file convres.json (patient 12)",
            error_ttt12)
    except FileNotFoundError as info_ttt12:
        print("[!] No date of end has been found into file convres.json (patient 12)",
            info_ttt12)
    else:
        print("[Err_3] It's not date of end for resapp.py 12")

    try:
        with open('./newpatient/entryfile13.txt', 'r') as namefile13:
            res_text13 = namefile13.readline()
    except FileNotFoundError as callfile13:
        print("[!] File entryfile13.txt doesn't exist !", callfile13)

    try:
        word_ttstop13 = (datetime.datetime.now() + \
            datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        file13 = open('./ttt/doc_ttt13/convres.json')
        data13 = json.load(file13)
        for (key, value) in data13.items():
            listdata13_x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            for x in listdata13_x:
                print(str(value[x]["Date of end"]))
                date_end13 = (str(value[x]["Date of end"]))
                if date_end13 == word_ttstop13:
                    print(date_end13)
                    name_treat13 = (str(value[x]["Treatment"]))
                    print(name_treat13)
                    dose_ttt13 = (str(value[x]["Dosage"]))
                    print(dose_ttt13)
                    MSBTTT13 = messagebox.showwarning('Warning',
                        'Look at Reserve, there is a reserve to stop at' + " " + \
                        word_ttstop13 + " " + "for : " + res_text13 + \
                        "\n" + "Date of end : " + date_end13 + "\n" + name_treat13 + \
                        " " + dose_ttt13)
                    MSGBOX = messagebox.askyesno("Ask", "Do you want to stop "\
                        "this reminder for the Reserve : " + name_treat13 + " " + \
                        dose_ttt13 + " of " + res_text13 + " ?")
                    if MSGBOX == 1:
                        print("Reminder stop !")
                        file = open('./ttt/doc_ttt13/convres.json')
                        data = json.load(file)
                        for (key, value) in data.items():
                            listdata_x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
                            for x in listdata_x:
                                date_end = (str(value[x]["Date of end"]))
                                if date_end == word_ttstop:
                                    print(date_end)
                                    intro_date = (str(value[x]["Date of introduction"]))
                                    name_treat = (str(value[x]["Treatment"]))
                                    print(name_treat)
                                    dose_ttt = (str(value[x]["Dosage"]))
                                    print(dose_ttt)
                                    if value[x]["Date of end"] in word_ttstop:
                                        value[x]['Date of end'] = "! STOP ! - " + word_ttstop
                                    with open('./ttt/doc_ttt13/convres.json', 'w') as re_file:
                                        json.dump(data, re_file, indent=4)
                                    upload13stopres()
                                    break
    except IndexError as error_ttt13:
        print("[!] No date of end has been found into file convres.json (patient 13)",
            error_ttt13)
    except FileNotFoundError as info_ttt13:
        print("[!] No date of end has been found into file convres.json (patient 13)",
            info_ttt13)
    else:
        print("[Err_3] It's not date of end for resapp.py 13")

    try:
        with open('./newpatient/entryfile14.txt', 'r') as namefile14:
            res_text14 = namefile14.readline()
    except FileNotFoundError as callfile14:
        print("[!] File entryfile14.txt doesn't exist !", callfile14)

    try:
        word_ttstop14 = (datetime.datetime.now() + \
            datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        file14 = open('./ttt/doc_ttt14/convres.json')
        data14 = json.load(file14)
        for (key, value) in data14.items():
            listdata14_x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            for x in listdata14_x:
                print(str(value[x]["Date of end"]))
                date_end14 = (str(value[x]["Date of end"]))
                if date_end14 == word_ttstop14:
                    print(date_end14)
                    name_treat14 = (str(value[x]["Treatment"]))
                    print(name_treat14)
                    dose_ttt14 = (str(value[x]["Dosage"]))
                    print(dose_ttt14)
                    MSBTTT14 = messagebox.showwarning('Warning',
                        'Look at Reserve, there is a reserve to stop at' + " " + \
                        word_ttstop14 + " " + "for : " + res_text14 + \
                        "\n" + "Date of end : " + date_end14 + "\n" + name_treat14 + \
                        " " + dose_ttt14)
                    MSGBOX = messagebox.askyesno("Ask", "Do you want to stop "\
                        "this reminder for the Reserve : " + name_treat14 + " " + \
                        dose_ttt14 + " of " + res_text14 + " ?")
                    if MSGBOX == 1:
                        print("Reminder stop !")
                        file = open('./ttt/doc_ttt14/convres.json')
                        data = json.load(file)
                        for (key, value) in data.items():
                            listdata_x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
                            for x in listdata_x:
                                date_end = (str(value[x]["Date of end"]))
                                if date_end == word_ttstop:
                                    print(date_end)
                                    intro_date = (str(value[x]["Date of introduction"]))
                                    name_treat = (str(value[x]["Treatment"]))
                                    print(name_treat)
                                    dose_ttt = (str(value[x]["Dosage"]))
                                    print(dose_ttt)
                                    if value[x]["Date of end"] in word_ttstop:
                                        value[x]['Date of end'] = "! STOP ! - " + word_ttstop
                                    with open('./ttt/doc_ttt14/convres.json', 'w') as re_file:
                                        json.dump(data, re_file, indent=4)
                                    upload14stopres()
                                    break
    except IndexError as error_ttt14:
        print("[!] No date of end has been found into file convres.json (patient 14)",
            error_ttt14)
    except FileNotFoundError as info_ttt14:
        print("[!] No date of end has been found into file convres.json (patient 14)",
            info_ttt14)
    else:
        print("[Err_3] It's not date of end for resapp.py 14")

    try:
        with open('./newpatient/entryfile15.txt', 'r') as namefile15:
            res_text15 = namefile15.readline()
    except FileNotFoundError as callfile15:
        print("[!] File entryfile15.txt doesn't exist !", callfile15)

    try:
        word_ttstop15 = (datetime.datetime.now() + \
            datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        file15 = open('./ttt/doc_ttt15/convres.json')
        data15 = json.load(file15)
        for (key, value) in data15.items():
            listdata15_x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            for x in listdata15_x:
                print(str(value[x]["Date of end"]))
                date_end15 = (str(value[x]["Date of end"]))
                if date_end15 == word_ttstop15:
                    print(date_end15)
                    name_treat15 = (str(value[x]["Treatment"]))
                    print(name_treat15)
                    dose_ttt15 = (str(value[x]["Dosage"]))
                    print(dose_ttt15)
                    MSBTTT15 = messagebox.showwarning('Warning',
                        'Look at Reserve, there is a reserve to stop at' + " " + \
                        word_ttstop15 + " " + "for : " + res_text15 + \
                        "\n" + "Date of end : " + date_end15 + "\n" + name_treat15 + \
                        " " + dose_ttt15)
                    MSGBOX = messagebox.askyesno("Ask", "Do you want to stop "\
                        "this reminder for the Reserve : " + name_treat15 + " " + \
                        dose_ttt15 + " of " + res_text15 + " ?")
                    if MSGBOX == 1:
                        print("Reminder stop !")
                        file = open('./ttt/doc_ttt15/convres.json')
                        data = json.load(file)
                        for (key, value) in data.items():
                            listdata_x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
                            for x in listdata_x:
                                date_end = (str(value[x]["Date of end"]))
                                if date_end == word_ttstop:
                                    print(date_end)
                                    intro_date = (str(value[x]["Date of introduction"]))
                                    name_treat = (str(value[x]["Treatment"]))
                                    print(name_treat)
                                    dose_ttt = (str(value[x]["Dosage"]))
                                    print(dose_ttt)
                                    if value[x]["Date of end"] in word_ttstop:
                                        value[x]['Date of end'] = "! STOP ! - " + word_ttstop
                                    with open('./ttt/doc_ttt15/convres.json', 'w') as re_file:
                                        json.dump(data, re_file, indent=4)
                                    upload15stopres()
                                    break
    except IndexError as error_ttt15:
        print("[!] No date of end has been found into file convres.json (patient 15)",
            error_ttt15)
    except FileNotFoundError as info_ttt15:
        print("[!] No date of end has been found into file convres.json (patient 15)",
            info_ttt15)
    else:
        print("[Err_3] It's not date of end for resapp.py 15")

    try:
        with open('./newpatient/entryfile16.txt', 'r') as namefile16:
            res_text16 = namefile16.readline()
    except FileNotFoundError as callfile16:
        print("[!] File entryfile16.txt doesn't exist !", callfile16)

    try:
        word_ttstop16 = (datetime.datetime.now() + \
            datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        file16 = open('./ttt/doc_ttt16/convres.json')
        data16 = json.load(file16)
        for (key, value) in data16.items():
            listdata16_x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            for x in listdata16_x:
                print(str(value[x]["Date of end"]))
                date_end16 = (str(value[x]["Date of end"]))
                if date_end16 == word_ttstop16:
                    print(date_end16)
                    name_treat16 = (str(value[x]["Treatment"]))
                    print(name_treat16)
                    dose_ttt16 = (str(value[x]["Dosage"]))
                    print(dose_ttt16)
                    MSBTTT16 = messagebox.showwarning('Warning',
                        'Look at Reserve, there is a reserve to stop at' + " " + \
                        word_ttstop16 + " " + "for : " + res_text16 + \
                        "\n" + "Date of end : " + date_end16 + "\n" + name_treat16 + \
                        " " + dose_ttt16)
                    MSGBOX = messagebox.askyesno("Ask", "Do you want to stop "\
                        "this reminder for the Reserve : " + name_treat16 + " " + \
                        dose_ttt16 + " of " + res_text16 + " ?")
                    if MSGBOX == 1:
                        print("Reminder stop !")
                        file = open('./ttt/doc_ttt16/convres.json')
                        data = json.load(file)
                        for (key, value) in data.items():
                            listdata_x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
                            for x in listdata_x:
                                date_end = (str(value[x]["Date of end"]))
                                if date_end == word_ttstop:
                                    print(date_end)
                                    intro_date = (str(value[x]["Date of introduction"]))
                                    name_treat = (str(value[x]["Treatment"]))
                                    print(name_treat)
                                    dose_ttt = (str(value[x]["Dosage"]))
                                    print(dose_ttt)
                                    if value[x]["Date of end"] in word_ttstop:
                                        value[x]['Date of end'] = "! STOP ! - " + word_ttstop
                                    with open('./ttt/doc_ttt16/convres.json', 'w') as re_file:
                                        json.dump(data, re_file, indent=4)
                                    upload16stopres()
                                    break
    except IndexError as error_ttt16:
        print("[!] No date of end has been found into file convres.json (patient 16)",
            error_ttt16)
    except FileNotFoundError as info_ttt16:
        print("[!] No date of end has been found into file convres.json (patient 16)",
            info_ttt16)
    else:
        print("[Err_3] It's not date of end for resapp.py 16")

    try:
        with open('./newpatient/entryfile17.txt', 'r') as namefile17:
            res_text17 = namefile17.readline()
    except FileNotFoundError as callfile17:
        print("[!] File entryfile17.txt doesn't exist !", callfile17)

    try:
        word_ttstop17 = (datetime.datetime.now() + \
            datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        file17 = open('./ttt/doc_ttt17/convres.json')
        data17 = json.load(file17)
        for (key, value) in data17.items():
            listdata17_x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            for x in listdata17_x:
                print(str(value[x]["Date of end"]))
                date_end17 = (str(value[x]["Date of end"]))
                if date_end17 == word_ttstop17:
                    print(date_end17)
                    name_treat17 = (str(value[x]["Treatment"]))
                    print(name_treat17)
                    dose_ttt17 = (str(value[x]["Dosage"]))
                    print(dose_ttt17)
                    MSBTTT17 = messagebox.showwarning('Warning',
                        'Look at Reserve, there is a reserve to stop at' + " " + \
                        word_ttstop17 + " " + "for : " + res_text17 + \
                        "\n" + "Date of end : " + date_end17 + "\n" + name_treat17 + \
                        " " + dose_ttt17)
                    MSGBOX = messagebox.askyesno("Ask", "Do you want to stop "\
                        "this reminder for the Reserve : " + name_treat17 + " " + \
                        dose_ttt17 + " of " + res_text17 + " ?")
                    if MSGBOX == 1:
                        print("Reminder stop !")
                        file = open('./ttt/doc_ttt17/convres.json')
                        data = json.load(file)
                        for (key, value) in data.items():
                            listdata_x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
                            for x in listdata_x:
                                date_end = (str(value[x]["Date of end"]))
                                if date_end == word_ttstop:
                                    print(date_end)
                                    intro_date = (str(value[x]["Date of introduction"]))
                                    name_treat = (str(value[x]["Treatment"]))
                                    print(name_treat)
                                    dose_ttt = (str(value[x]["Dosage"]))
                                    print(dose_ttt)
                                    if value[x]["Date of end"] in word_ttstop:
                                        value[x]['Date of end'] = "! STOP ! - " + word_ttstop
                                    with open('./ttt/doc_ttt17/convres.json', 'w') as re_file:
                                        json.dump(data, re_file, indent=4)
                                    upload17stopres()
                                    break
    except IndexError as error_ttt17:
        print("[!] No date of end has been found into file convres.json (patient 17)",
            error_ttt17)
    except FileNotFoundError as info_ttt17:
        print("[!] No date of end has been found into file convres.json (patient 17)",
            info_ttt17)
    else:
        print("[Err_3] It's not date of end for resapp.py 17")

    try:
        with open('./newpatient/entryfile18.txt', 'r') as namefile18:
            res_text18 = namefile18.readline()
    except FileNotFoundError as callfile18:
        print("[!] File entryfile18.txt doesn't exist !", callfile18)

    try:
        word_ttstop18 = (datetime.datetime.now() + \
            datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        file18 = open('./ttt/doc_ttt18/convres.json')
        data18 = json.load(file18)
        for (key, value) in data18.items():
            listdata18_x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            for x in listdata18_x:
                print(str(value[x]["Date of end"]))
                date_end18 = (str(value[x]["Date of end"]))
                if date_end18 == word_ttstop18:
                    print(date_end18)
                    name_treat18 = (str(value[x]["Treatment"]))
                    print(name_treat18)
                    dose_ttt18 = (str(value[x]["Dosage"]))
                    print(dose_ttt18)
                    MSBTTT18 = messagebox.showwarning('Warning',
                        'Look at Reserve, there is a reserve to stop at' + " " + \
                        word_ttstop18 + " " + "for : " + res_text18 + \
                        "\n" + "Date of end : " + date_end18 + "\n" + name_treat18 + \
                        " " + dose_ttt18)
                    MSGBOX = messagebox.askyesno("Ask", "Do you want to stop "\
                        "this reminder for the Reserve : " + name_treat18 + " " + \
                        dose_ttt18 + " of " + res_text18 + " ?")
                    if MSGBOX == 1:
                        print("Reminder stop !")
                        file = open('./ttt/doc_ttt18/convres.json')
                        data = json.load(file)
                        for (key, value) in data.items():
                            listdata_x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
                            for x in listdata_x:
                                date_end = (str(value[x]["Date of end"]))
                                if date_end == word_ttstop:
                                    print(date_end)
                                    intro_date = (str(value[x]["Date of introduction"]))
                                    name_treat = (str(value[x]["Treatment"]))
                                    print(name_treat)
                                    dose_ttt = (str(value[x]["Dosage"]))
                                    print(dose_ttt)
                                    if value[x]["Date of end"] in word_ttstop:
                                        value[x]['Date of end'] = "! STOP ! - " + word_ttstop
                                    with open('./ttt/doc_ttt18/convres.json', 'w') as re_file:
                                        json.dump(data, re_file, indent=4)
                                    upload18stopres()
                                    break
    except IndexError as error_ttt18:
        print("[!] No date of end has been found into file convres.json (patient 18)",
            error_ttt18)
    except FileNotFoundError as info_ttt18:
        print("[!] No date of end has been found into file convres.json (patient 18)",
            info_ttt18)
    else:
        print("[Err_3] It's not date of end for resapp.py 18")

    try:
        with open('./newpatient/entryfile19.txt', 'r') as namefile19:
            res_text19 = namefile19.readline()
    except FileNotFoundError as callfile19:
        print("[!] File entryfile19.txt doesn't exist !", callfile19)

    try:
        word_ttstop19 = (datetime.datetime.now() + \
            datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        file19 = open('./ttt/doc_ttt19/convres.json')
        data19 = json.load(file19)
        for (key, value) in data19.items():
            listdata19_x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            for x in listdata19_x:
                print(str(value[x]["Date of end"]))
                date_end19 = (str(value[x]["Date of end"]))
                if date_end19 == word_ttstop19:
                    print(date_end19)
                    name_treat19 = (str(value[x]["Treatment"]))
                    print(name_treat19)
                    dose_ttt19 = (str(value[x]["Dosage"]))
                    print(dose_ttt19)
                    MSBTTT19 = messagebox.showwarning('Warning',
                        'Look at Reserve, there is a reserve to stop at' + " " + \
                        word_ttstop19 + " " + "for : " + res_text19 + \
                        "\n" + "Date of end : " + date_end19 + "\n" + name_treat19 + \
                        " " + dose_ttt19)
                    MSGBOX = messagebox.askyesno("Ask", "Do you want to stop "\
                        "this reminder for the Reserve : " + name_treat19 + " " + \
                        dose_ttt19 + " of " + res_text19 + " ?")
                    if MSGBOX == 1:
                        print("Reminder stop !")
                        file = open('./ttt/doc_ttt19/convres.json')
                        data = json.load(file)
                        for (key, value) in data.items():
                            listdata_x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
                            for x in listdata_x:
                                date_end = (str(value[x]["Date of end"]))
                                if date_end == word_ttstop:
                                    print(date_end)
                                    intro_date = (str(value[x]["Date of introduction"]))
                                    name_treat = (str(value[x]["Treatment"]))
                                    print(name_treat)
                                    dose_ttt = (str(value[x]["Dosage"]))
                                    print(dose_ttt)
                                    if value[x]["Date of end"] in word_ttstop:
                                        value[x]['Date of end'] = "! STOP ! - " + word_ttstop
                                    with open('./ttt/doc_ttt19/convres.json', 'w') as re_file:
                                        json.dump(data, re_file, indent=4)
                                    upload19stopres()
                                    break
    except IndexError as error_ttt19:
        print("[!] No date of end has been found into file convres.json (patient 19)",
            error_ttt19)
    except FileNotFoundError as info_ttt19:
        print("[!] No date of end has been found into file convres.json (patient 19)",
            info_ttt19)
    else:
        print("[Err_3] It's not date of end for resapp.py 19")

    # Patient 20
    try:
        with open('./newpatient/entryfile20.txt', 'r') as namefile20:
            res_text20 = namefile20.readline()
    except FileNotFoundError as callfile20:
        print("[!] File entryfile20.txt doesn't exist !", callfile20)

    try:
        word_ttstop20 = (datetime.datetime.now() + \
            datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        file20 = open('./ttt/doc_ttt20/convres.json')
        data20 = json.load(file20)
        for (key, value) in data20.items():
            listdata20_x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            for x in listdata20_x:
                print(str(value[x]["Date of end"]))
                date_end20 = (str(value[x]["Date of end"]))
                if date_end20 == word_ttstop20:
                    print(date_end20)
                    name_treat20 = (str(value[x]["Treatment"]))
                    print(name_treat20)
                    dose_ttt20 = (str(value[x]["Dosage"]))
                    print(dose_ttt20)
                    MSBTTT20 = messagebox.showwarning('Warning',
                        'Look at Reserve, there is a reserve to stop at' + " " + \
                        word_ttstop20 + " " + "for : " + res_text20 + \
                        "\n" + "Date of end : " + date_end20 + "\n" + name_treat20 + \
                        " " + dose_ttt20)
                    MSGBOX = messagebox.askyesno("Ask", "Do you want to stop "\
                        "this reminder for the Reserve : " + name_treat20 + " " + \
                        dose_ttt20 + " of " + res_text20 + " ?")
                    if MSGBOX == 1:
                        print("Reminder stop !")
                        file = open('./ttt/doc_ttt20/convres.json')
                        data = json.load(file)
                        for (key, value) in data.items():
                            listdata_x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
                            for x in listdata_x:
                                date_end = (str(value[x]["Date of end"]))
                                if date_end == word_ttstop:
                                    print(date_end)
                                    intro_date = (str(value[x]["Date of introduction"]))
                                    name_treat = (str(value[x]["Treatment"]))
                                    print(name_treat)
                                    dose_ttt = (str(value[x]["Dosage"]))
                                    print(dose_ttt)
                                    if value[x]["Date of end"] in word_ttstop:
                                        value[x]['Date of end'] = "! STOP ! - " + word_ttstop
                                    with open('./ttt/doc_ttt20/convres.json', 'w') as re_file:
                                        json.dump(data, re_file, indent=4)
                                    upload20stopres()
                                    break
    except IndexError as error_ttt20:
        print("[!] No date of end has been found into file convres.json (patient 20)",
            error_ttt20)
    except FileNotFoundError as info_ttt20:
        print("[!] No date of end has been found into file convres.json (patient 20)",
            info_ttt20)
    else:
        print("[Err_3] It's not date of end for resapp.py 20")

    try:
        with open('./newpatient/entryfile21.txt', 'r') as namefile21:
            res_text21 = namefile21.readline()
    except FileNotFoundError as callfile21:
        print("[!] File entryfile21.txt doesn't exist !", callfile21)

    try:
        word_ttstop21 = (datetime.datetime.now() + \
            datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        file21 = open('./ttt/doc_ttt21/convres.json')
        data21 = json.load(file21)
        for (key, value) in data21.items():
            listdata21_x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            for x in listdata21_x:
                print(str(value[x]["Date of end"]))
                date_end21 = (str(value[x]["Date of end"]))
                if date_end21 == word_ttstop21:
                    print(date_end21)
                    name_treat21 = (str(value[x]["Treatment"]))
                    print(name_treat21)
                    dose_ttt21 = (str(value[x]["Dosage"]))
                    print(dose_ttt21)
                    MSBTTT21 = messagebox.showwarning('Warning',
                        'Look at Reserve, there is a reserve to stop at' + " " + \
                        word_ttstop21 + " " + "for : " + res_text21 + \
                        "\n" + "Date of end : " + date_end21 + "\n" + name_treat21 + \
                        " " + dose_ttt21)
                    MSGBOX = messagebox.askyesno("Ask", "Do you want to stop "\
                        "this reminder for the Reserve : " + name_treat21 + " " + \
                        dose_ttt21 + " of " + res_text21 + " ?")
                    if MSGBOX == 1:
                        print("Reminder stop !")
                        file = open('./ttt/doc_ttt21/convres.json')
                        data = json.load(file)
                        for (key, value) in data.items():
                            listdata_x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
                            for x in listdata_x:
                                date_end = (str(value[x]["Date of end"]))
                                if date_end == word_ttstop:
                                    print(date_end)
                                    intro_date = (str(value[x]["Date of introduction"]))
                                    name_treat = (str(value[x]["Treatment"]))
                                    print(name_treat)
                                    dose_ttt = (str(value[x]["Dosage"]))
                                    print(dose_ttt)
                                    if value[x]["Date of end"] in word_ttstop:
                                        value[x]['Date of end'] = "! STOP ! - " + word_ttstop
                                    with open('./ttt/doc_ttt21/convres.json', 'w') as re_file:
                                        json.dump(data, re_file, indent=4)
                                    upload21stopres()
                                    break
    except IndexError as error_ttt21:
        print("[!] No date of end has been found into file convres.json (patient 21)",
            error_ttt21)
    except FileNotFoundError as info_ttt21:
        print("[!] No date of end has been found into file convres.json (patient 21)",
            info_ttt21)
    else:
        print("[Err_3] It's not date of end for resapp.py 21")

    try:
        with open('./newpatient/entryfile22.txt', 'r') as namefile22:
            res_text22 = namefile22.readline()
    except FileNotFoundError as callfile22:
        print("[!] File entryfile22.txt doesn't exist !", callfile22)

    try:
        word_ttstop22 = (datetime.datetime.now() + \
            datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        file22 = open('./ttt/doc_ttt22/convres.json')
        data22 = json.load(file22)
        for (key, value) in data22.items():
            listdata22_x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            for x in listdata22_x:
                print(str(value[x]["Date of end"]))
                date_end22 = (str(value[x]["Date of end"]))
                if date_end22 == word_ttstop22:
                    print(date_end22)
                    name_treat22 = (str(value[x]["Treatment"]))
                    print(name_treat22)
                    dose_ttt22 = (str(value[x]["Dosage"]))
                    print(dose_ttt22)
                    MSBTTT22 = messagebox.showwarning('Warning',
                        'Look at Reserve, there is a reserve to stop at' + " " + \
                        word_ttstop22 + " " + "for : " + res_text22 + \
                        "\n" + "Date of end : " + date_end22 + "\n" + name_treat22 + \
                        " " + dose_ttt22)
                    MSGBOX = messagebox.askyesno("Ask", "Do you want to stop "\
                        "this reminder for the Reserve : " + name_treat22 + " " + \
                        dose_ttt22 + " of " + res_text22 + " ?")
                    if MSGBOX == 1:
                        print("Reminder stop !")
                        file = open('./ttt/doc_ttt22/convres.json')
                        data = json.load(file)
                        for (key, value) in data.items():
                            listdata_x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
                            for x in listdata_x:
                                date_end = (str(value[x]["Date of end"]))
                                if date_end == word_ttstop:
                                    print(date_end)
                                    intro_date = (str(value[x]["Date of introduction"]))
                                    name_treat = (str(value[x]["Treatment"]))
                                    print(name_treat)
                                    dose_ttt = (str(value[x]["Dosage"]))
                                    print(dose_ttt)
                                    if value[x]["Date of end"] in word_ttstop:
                                        value[x]['Date of end'] = "! STOP ! - " + word_ttstop
                                    with open('./ttt/doc_ttt22/convres.json', 'w') as re_file:
                                        json.dump(data, re_file, indent=4)
                                    upload22stopres()
                                    break
    except IndexError as error_ttt22:
        print("[!] No date of end has been found into file convres.json (patient 22)",
            error_ttt22)
    except FileNotFoundError as info_ttt22:
        print("[!] No date of end has been found into file convres.json (patient 22)",
            info_ttt22)
    else:
        print("[Err_3] It's not date of end for resapp.py 22")

    try:
        with open('./newpatient/entryfile23.txt', 'r') as namefile23:
            res_text23 = namefile23.readline()
    except FileNotFoundError as callfile23:
        print("[!] File entryfile23.txt doesn't exist !", callfile23)

    try:
        word_ttstop23 = (datetime.datetime.now() + \
            datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        file23 = open('./ttt/doc_ttt23/convres.json')
        data23 = json.load(file23)
        for (key, value) in data23.items():
            listdata23_x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            for x in listdata23_x:
                print(str(value[x]["Date of end"]))
                date_end23 = (str(value[x]["Date of end"]))
                if date_end23 == word_ttstop23:
                    print(date_end23)
                    name_treat23 = (str(value[x]["Treatment"]))
                    print(name_treat23)
                    dose_ttt23 = (str(value[x]["Dosage"]))
                    print(dose_ttt23)
                    MSBTTT23 = messagebox.showwarning('Warning',
                        'Look at Reserve, there is a reserve to stop at' + " " + \
                        word_ttstop23 + " " + "for : " + res_text23 + \
                        "\n" + "Date of end : " + date_end23 + "\n" + name_treat23 + \
                        " " + dose_ttt23)
                    MSGBOX = messagebox.askyesno("Ask", "Do you want to stop "\
                        "this reminder for the Reserve : " + name_treat23 + " " + \
                        dose_ttt23 + " of " + res_text23 + " ?")
                    if MSGBOX == 1:
                        print("Reminder stop !")
                        file = open('./ttt/doc_ttt23/convres.json')
                        data = json.load(file)
                        for (key, value) in data.items():
                            listdata_x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
                            for x in listdata_x:
                                date_end = (str(value[x]["Date of end"]))
                                if date_end == word_ttstop:
                                    print(date_end)
                                    intro_date = (str(value[x]["Date of introduction"]))
                                    name_treat = (str(value[x]["Treatment"]))
                                    print(name_treat)
                                    dose_ttt = (str(value[x]["Dosage"]))
                                    print(dose_ttt)
                                    if value[x]["Date of end"] in word_ttstop:
                                        value[x]['Date of end'] = "! STOP ! - " + word_ttstop
                                    with open('./ttt/doc_ttt23/convres.json', 'w') as re_file:
                                        json.dump(data, re_file, indent=4)
                                    upload23stopres()
                                    break
    except IndexError as error_ttt23:
        print("[!] No date of end has been found into file convres.json (patient 23)",
            error_ttt23)
    except FileNotFoundError as info_ttt23:
        print("[!] No date of end has been found into file convres.json (patient 23)",
            info_ttt23)
    else:
        print("[Err_3] It's not date of end for resapp.py 23")

    try:
        with open('./newpatient/entryfile24.txt', 'r') as namefile24:
            res_text24 = namefile24.readline()
    except FileNotFoundError as callfile24:
        print("[!] File entryfile24.txt doesn't exist !", callfile24)

    try:
        word_ttstop24 = (datetime.datetime.now() + \
            datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        file24 = open('./ttt/doc_ttt24/convres.json')
        data24 = json.load(file24)
        for (key, value) in data24.items():
            listdata24_x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            for x in listdata24_x:
                print(str(value[x]["Date of end"]))
                date_end24 = (str(value[x]["Date of end"]))
                if date_end24 == word_ttstop24:
                    print(date_end24)
                    name_treat24 = (str(value[x]["Treatment"]))
                    print(name_treat24)
                    dose_ttt24 = (str(value[x]["Dosage"]))
                    print(dose_ttt24)
                    MSBTTT24 = messagebox.showwarning('Warning',
                        'Look at Reserve, there is a reserve to stop at' + " " + \
                        word_ttstop24 + " " + "for : " + res_text24 + \
                        "\n" + "Date of end : " + date_end24 + "\n" + name_treat24 + \
                        " " + dose_ttt24)
                    MSGBOX = messagebox.askyesno("Ask", "Do you want to stop "\
                        "this reminder for the Reserve : " + name_treat24 + " " + \
                        dose_ttt24 + " of " + res_text24 + " ?")
                    if MSGBOX == 1:
                        print("Reminder stop !")
                        file = open('./ttt/doc_ttt24/convres.json')
                        data = json.load(file)
                        for (key, value) in data.items():
                            listdata_x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
                            for x in listdata_x:
                                date_end = (str(value[x]["Date of end"]))
                                if date_end == word_ttstop:
                                    print(date_end)
                                    intro_date = (str(value[x]["Date of introduction"]))
                                    name_treat = (str(value[x]["Treatment"]))
                                    print(name_treat)
                                    dose_ttt = (str(value[x]["Dosage"]))
                                    print(dose_ttt)
                                    if value[x]["Date of end"] in word_ttstop:
                                        value[x]['Date of end'] = "! STOP ! - " + word_ttstop
                                    with open('./ttt/doc_ttt24/convres.json', 'w') as re_file:
                                        json.dump(data, re_file, indent=4)
                                    upload24stopres()
                                    break
    except IndexError as error_ttt24:
        print("[!] No date of end has been found into file convres.json (patient 24)",
            error_ttt24)
    except FileNotFoundError as info_ttt24:
        print("[!] No date of end has been found into file convres.json (patient 24)",
            info_ttt24)
    else:
        print("[Err_3] It's not date of end for resapp.py 24")
