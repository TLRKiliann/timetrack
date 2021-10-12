#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
    It checks if the end date of the treatment corresponds
    to today's date. If yes, convdose.json is modify and
    upload to server.
"""


from tkinter import *
from tkinter import messagebox

import datetime
import json

from medic_upload.stop_ttt import uploadstopttt
from medic_upload.stop_ttt import upload2stopttt
from medic_upload.stop_ttt import upload3stopttt
from medic_upload.stop_ttt import upload4stopttt
from medic_upload.stop_ttt import upload5stopttt
from medic_upload.stop_ttt import upload6stopttt
from medic_upload.stop_ttt import upload7stopttt
from medic_upload.stop_ttt import upload8stopttt
from medic_upload.stop_ttt import upload9stopttt
from medic_upload.stop_ttt import upload10stopttt
from medic_upload.stop_ttt import upload11stopttt
from medic_upload.stop_ttt import upload12stopttt
from medic_upload.stop_ttt import upload13stopttt
from medic_upload.stop_ttt import upload14stopttt
from medic_upload.stop_ttt import upload15stopttt
from medic_upload.stop_ttt import upload16stopttt
from medic_upload.stop_ttt import upload17stopttt
from medic_upload.stop_ttt import upload18stopttt
from medic_upload.stop_ttt import upload19stopttt
from medic_upload.stop_ttt import upload20stopttt
from medic_upload.stop_ttt import upload21stopttt
from medic_upload.stop_ttt import upload22stopttt
from medic_upload.stop_ttt import upload23stopttt
from medic_upload.stop_ttt import upload24stopttt


def dispTttBox():
    """
        Stop medication on right date and write it into tab of medication
        (Treatments)
    """
    try:
        with open('./newpatient/entryfile.txt', 'r') as namefile:
            ttt_text1 = namefile.readline()
    except FileNotFoundError as fileout1:
        print("[!] No file entryfile.txt exist", fileout1)

    try:
        word_ttstop = (datetime.datetime.now() + \
            datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        file = open('./ttt/doc_ttt/convdose.json')
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
                        'Look at TTT, there is a ttt to stop at' + " " + \
                        word_ttstop + " " + 'for : ' + "\n" + ttt_text1 + \
                        "\n" + "Date of end : " + date_end + "\n" + name_treat + \
                        " " + dose_ttt)
                    MSGBOX = messagebox.askyesno("Ask", "Do you want to stop "\
                        "this reminder for the ttt : " + name_treat + " " + \
                        dose_ttt + " for " + ttt_text1 + " ?")
                    if MSGBOX == 1:
                        print("Reminder stop ttt !")
                        file = open('./ttt/doc_ttt/convdose.json')
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
                                    matin = (str(value[x]["Morning"]))
                                    midi = (str(value[x]["Midday"]))
                                    soir = (str(value[x]["Evening"]))
                                    nuit = (str(value[x]["Night"]))
                                    if value[x]["Date of end"] in word_ttstop:
                                        value[x]['Date of end'] = "! STOP ! -" + word_ttstop
                                    with open('./ttt/doc_ttt/convdose.json', 'w') as re_file:
                                        json.dump(data, re_file, indent=4)
                                    uploadstopttt()
                                    break
    except IndexError as error_ttt:
        print("[Err_1] No date of end has been found into file convdose.json (patient 1)",
            error_ttt)
    except FileNotFoundError as info_ttt:
        print("[Err_2] No date of end has been found into file convdose.json (patient 1)",
            info_ttt)
    else:
        print("[Err_3] It's not date of end for tttapp.py 1")

    try:
        with open('./newpatient/entryfile2.txt', 'r') as namefile2:
            ttt_text2 = namefile2.readline()
    except FileNotFoundError as fileout2:
        print("[!] No file entryfile2.txt exist", fileout2)

    try:
        word_ttstop2 = (datetime.datetime.now() + \
            datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        file2 = open('./ttt/doc_ttt2/convdose.json')
        data2 = json.load(file2)
        for (key, value) in data2.items():
            listdata_x2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            for x in listdata_x2:
                print(str(value[x]["Date of end"]))
                date_end2 = (str(value[x]["Date of end"]))
                if date_end2 == word_ttstop2:
                    print(date_end2)
                    name_treat2 = (str(value[x]["Treatment"]))
                    print(name_treat2)
                    dose_ttt2 = (str(value[x]["Dosage"]))
                    print(dose_ttt2)
                    MSBTTT2 = messagebox.showwarning('Warning',
                        'Look at TTT, there is a ttt to stop at' + " " + \
                        word_ttstop2 + " " + 'for : ' + "\n" + ttt_text2 + \
                        "\n" + "Date of end : " + date_end2 + "\n" + name_treat2 + \
                        " " + dose_ttt2)
                    MSGBOX = messagebox.askyesno("Ask", "Do you want to stop "\
                        "this reminder for the ttt : " + name_treat2 + " " + \
                        dose_ttt2 + " for " + ttt_text2 + " ?")
                    if MSGBOX == 1:
                        print("Reminder stop !")
                        file = open('./ttt/doc_ttt2/convdose.json')
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
                                    matin = (str(value[x]["Morning"]))
                                    midi = (str(value[x]["Midday"]))
                                    soir = (str(value[x]["Evening"]))
                                    nuit = (str(value[x]["Night"]))
                                    if value[x]["Date of end"] in word_ttstop:
                                        value[x]['Date of end'] = "! STOP ! -" + word_ttstop
                                    with open('./ttt/doc_ttt2/convdose.json', 'w') as re_file:
                                        json.dump(data, re_file, indent=4)
                                    upload2stopttt()
                                    break
    except IndexError as error_ttt2:
        print("[Err_1] No date of end has been found into file convdose.json (patient 2)",
            error_ttt2)
    except FileNotFoundError as info_ttt2:
        print("[Err_2] No date of end has been found into file convdose.json (patient 2)",
            info_ttt2)
    else:
        print("[Err_3] It's not date of end for tttapp.py 2")

    try:
        with open('./newpatient/entryfile3.txt', 'r') as namefile3:
            ttt_text3 = namefile3.readline()
    except FileNotFoundError as fileout3:
        print("[!] No file entryfile3.txt exist", fileout3)

    try:
        word_ttstop3 = (datetime.datetime.now() + \
            datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        file3 = open('./ttt/doc_ttt3/convdose.json')
        data3 = json.load(file3)
        for (key, value) in data3.items():
            listdata_x3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            for x in listdata_x3:
                print(str(value[x]["Date of end"]))
                date_end3 = (str(value[x]["Date of end"]))
                if date_end3 == word_ttstop3:
                    print(date_end3)
                    name_treat3 = (str(value[x]["Treatment"]))
                    print(name_treat3)
                    dose_ttt3 = (str(value[x]["Dosage"]))
                    print(dose_ttt3)
                    MSBTTT2 = messagebox.showwarning('Warning',
                        'Look at TTT, there is a ttt to stop at' + " " + \
                        word_ttstop3 + " " + 'for : ' + "\n" + ttt_text3 + \
                        "\n" + "Date of end : " + date_end3 + "\n" + name_treat3 + \
                        " " + dose_ttt3)
                    MSGBOX = messagebox.askyesno("Ask", "Do you want to stop "\
                        "this reminder for the ttt : " + name_treat3 + " " + \
                        dose_ttt3 + " for " + ttt_text3 + " ?")
                    if MSGBOX == 1:
                        print("Reminder stop !")
                        file = open('./ttt/doc_ttt3/convdose.json')
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
                                    matin = (str(value[x]["Morning"]))
                                    midi = (str(value[x]["Midday"]))
                                    soir = (str(value[x]["Evening"]))
                                    nuit = (str(value[x]["Night"]))
                                    if value[x]["Date of end"] in word_ttstop:
                                        value[x]['Date of end'] = "! STOP ! -" + word_ttstop
                                    with open('./ttt/doc_ttt3/convdose.json', 'w') as re_file:
                                        json.dump(data, re_file, indent=4)
                                    upload3stopttt()
                                    break
    except IndexError as error_ttt3:
        print("[Err_1] No date of end has been found into file convdose.json (patient 3)",
            error_ttt3)
    except FileNotFoundError as info_ttt3:
        print("[Err_2] No date of end has been found into file convdose.json (patient 3)",
            info_ttt3)
    else:
        print("[Err_3] It's not date of end for tttapp.py 3")

    try:
        with open('./newpatient/entryfile4.txt', 'r') as namefile4:
            ttt_text4 = namefile4.readline()
    except FileNotFoundError as fileout4:
        print("[!] No file entryfile4.txt exist", fileout4)

    try:
        word_ttstop4 = (datetime.datetime.now() + \
            datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        file4 = open('./ttt/doc_ttt4/convdose.json')
        data4 = json.load(file4)
        for (key, value) in data4.items():
            listdata_x4 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            for x in listdata_x4:
                print(str(value[x]["Date of end"]))
                date_end4 = (str(value[x]["Date of end"]))
                if date_end4 == word_ttstop4:
                    print(date_end4)
                    name_treat4 = (str(value[x]["Treatment"]))
                    print(name_treat4)
                    dose_ttt4 = (str(value[x]["Dosage"]))
                    print(dose_ttt4)
                    MSBTTT2 = messagebox.showwarning('Warning',
                        'Look at TTT, there is a ttt to stop at' + " " + \
                        word_ttstop4 + " " + 'for : ' + "\n" + ttt_text4 + \
                        "\n" + "Date of end : " + date_end4 + "\n" + name_treat4 + \
                        " " + dose_ttt4)
                    MSGBOX = messagebox.askyesno("Ask", "Do you want to stop "\
                        "this reminder for the ttt : " + name_treat4 + " " + \
                        dose_ttt4 + " for " + ttt_text4 + " ?")
                    if MSGBOX == 1:
                        print("Reminder stop !")
                        file = open('./ttt/doc_ttt4/convdose.json')
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
                                    matin = (str(value[x]["Morning"]))
                                    midi = (str(value[x]["Midday"]))
                                    soir = (str(value[x]["Evening"]))
                                    nuit = (str(value[x]["Night"]))
                                    if value[x]["Date of end"] in word_ttstop:
                                        value[x]['Date of end'] = "! STOP ! -" + word_ttstop
                                    with open('./ttt/doc_ttt4/convdose.json', 'w') as re_file:
                                        json.dump(data, re_file, indent=4)
                                    upload4stopttt()
                                    break
    except IndexError as error_ttt4:
        print("[Err_1] No date of end has been found into file convdose.json (patient 4)",
            error_ttt4)
    except FileNotFoundError as info_ttt4:
        print("[Err_2] No date of end has been found into file convdose.json (patient 4)",
            info_ttt4)
    else:
        print("[Err_3] It's not date of end for tttapp.py 4")

    try:
        with open('./newpatient/entryfile5.txt', 'r') as namefile5:
            ttt_text5 = namefile5.readline()
    except FileNotFoundError as fileout5:
        print("[!] No file entryfile5.txt exist", fileout5)

    try:
        word_ttstop5 = (datetime.datetime.now() + \
            datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        file5 = open('./ttt/doc_ttt5/convdose.json')
        data5 = json.load(file5)
        for (key, value) in data5.items():
            listdata_x5 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            for x in listdata_x5:
                print(str(value[x]["Date of end"]))
                date_end5 = (str(value[x]["Date of end"]))
                if date_end5 == word_ttstop5:
                    print(date_end5)
                    name_treat5 = (str(value[x]["Treatment"]))
                    print(name_treat5)
                    dose_ttt5 = (str(value[x]["Dosage"]))
                    print(dose_ttt5)
                    MSBTTT2 = messagebox.showwarning('Warning',
                        'Look at TTT, there is a ttt to stop at' + " " + \
                        word_ttstop5 + " " + 'for : ' + "\n" + ttt_text5 + \
                        "\n" + "Date of end : " + date_end5 + "\n" + name_treat5 + \
                        " " + dose_ttt5)
                    MSGBOX = messagebox.askyesno("Ask", "Do you want to stop "\
                        "this reminder for the ttt : " + name_treat5 + " " + \
                        dose_ttt5 + " for " + ttt_text5 + " ?")
                    if MSGBOX == 1:
                        print("Reminder stop !")
                        file = open('./ttt/doc_ttt5/convdose.json')
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
                                    matin = (str(value[x]["Morning"]))
                                    midi = (str(value[x]["Midday"]))
                                    soir = (str(value[x]["Evening"]))
                                    nuit = (str(value[x]["Night"]))
                                    if value[x]["Date of end"] in word_ttstop:
                                        value[x]['Date of end'] = "! STOP ! -" + word_ttstop
                                    with open('./ttt/doc_ttt5/convdose.json', 'w') as re_file:
                                        json.dump(data, re_file, indent=4)
                                    upload5stopttt()
                                    break
    except IndexError as error_ttt5:
        print("[Err_1] No date of end has been found into file convdose.json (patient 5)",
            error_ttt5)
    except FileNotFoundError as info_ttt5:
        print("[Err_2] No date of end has been found into file convdose.json (patient 5)",
            info_ttt5)
    else:
        print("[Err_3] It's not date of end for tttapp.py 5")

    try:
        with open('./newpatient/entryfile6.txt', 'r') as namefile6:
            ttt_text6 = namefile6.readline()
    except FileNotFoundError as fileout6:
        print("[!] No file entryfile6.txt exist", fileout6)

    try:
        word_ttstop6 = (datetime.datetime.now() + \
            datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        file6 = open('./ttt/doc_ttt6/convdose.json')
        data6 = json.load(file6)
        for (key, value) in data6.items():
            listdata_x6 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            for x in listdata_x6:
                print(str(value[x]["Date of end"]))
                date_end6 = (str(value[x]["Date of end"]))
                if date_end6 == word_ttstop6:
                    print(date_end6)
                    name_treat6 = (str(value[x]["Treatment"]))
                    print(name_treat6)
                    dose_ttt6 = (str(value[x]["Dosage"]))
                    print(dose_ttt6)
                    MSBTTT2 = messagebox.showwarning('Warning',
                        'Look at TTT, there is a ttt to stop at' + " " + \
                        word_ttstop6 + " " + 'for : ' + "\n" + ttt_text6 + \
                        "\n" + "Date of end : " + date_end6 + "\n" + name_treat6 + \
                        " " + dose_ttt6)
                    MSGBOX = messagebox.askyesno("Ask", "Do you want to stop "\
                        "this reminder for the ttt : " + name_treat6 + " " + \
                        dose_ttt6 + " for " + ttt_text6 + " ?")
                    if MSGBOX == 1:
                        print("Reminder stop !")
                        file = open('./ttt/doc_ttt6/convdose.json')
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
                                    matin = (str(value[x]["Morning"]))
                                    midi = (str(value[x]["Midday"]))
                                    soir = (str(value[x]["Evening"]))
                                    nuit = (str(value[x]["Night"]))
                                    if value[x]["Date of end"] in word_ttstop:
                                        value[x]['Date of end'] = "! STOP ! -" + word_ttstop
                                    with open('./ttt/doc_ttt6/convdose.json', 'w') as re_file:
                                        json.dump(data, re_file, indent=4)
                                    upload6stopttt()
                                    break
    except IndexError as error_ttt6:
        print("[Err_1] No date of end has been found into file convdose.json (patient 6)",
            error_ttt6)
    except FileNotFoundError as info_ttt6:
        print("[Err_2] No date of end has been found into file convdose.json (patient 6)",
            info_ttt6)
    else:
        print("[Err_3] It's not date of end for tttapp.py 6")

    try:
        with open('./newpatient/entryfile7.txt', 'r') as namefile7:
            ttt_text7 = namefile7.readline()
    except FileNotFoundError as fileout7:
        print("[!] No file entryfile7.txt exist", fileout7)

    try:
        word_ttstop7 = (datetime.datetime.now() + \
            datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        file7 = open('./ttt/doc_ttt7/convdose.json')
        data7 = json.load(file7)
        for (key, value) in data7.items():
            listdata_x7 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            for x in listdata_x7:
                print(str(value[x]["Date of end"]))
                date_end7 = (str(value[x]["Date of end"]))
                if date_end7 == word_ttstop7:
                    print(date_end7)
                    name_treat7 = (str(value[x]["Treatment"]))
                    print(name_treat7)
                    dose_ttt7 = (str(value[x]["Dosage"]))
                    print(dose_ttt7)
                    MSBTTT2 = messagebox.showwarning('Warning',
                        'Look at TTT, there is a ttt to stop at' + " " + \
                        word_ttstop7 + " " + 'for : ' + "\n" + ttt_text7 + \
                        "\n" + "Date of end : " + date_end7 + "\n" + name_treat7 + \
                        " " + dose_ttt7)
                    MSGBOX = messagebox.askyesno("Ask", "Do you want to stop "\
                        "this reminder for the ttt : " + name_treat7 + " " + \
                        dose_ttt7 + " for " + ttt_text7 + " ?")
                    if MSGBOX == 1:
                        print("Reminder stop !")
                        file = open('./ttt/doc_ttt7/convdose.json')
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
                                    matin = (str(value[x]["Morning"]))
                                    midi = (str(value[x]["Midday"]))
                                    soir = (str(value[x]["Evening"]))
                                    nuit = (str(value[x]["Night"]))
                                    if value[x]["Date of end"] in word_ttstop:
                                        value[x]['Date of end'] = "! STOP ! -" + word_ttstop
                                    with open('./ttt/doc_ttt7/convdose.json', 'w') as re_file:
                                        json.dump(data, re_file, indent=4)
                                    upload7stopttt()
                                    break
    except IndexError as error_ttt7:
        print("[Err_1] No date of end has been found into file convdose.json (patient 7)",
            error_ttt7)
    except FileNotFoundError as info_ttt7:
        print("[Err_2] No date of end has been found into file convdose.json (patient 7)",
            info_ttt7)
    else:
        print("[Err_3] It's not date of end for tttapp.py 7")

    try:
        with open('./newpatient/entryfile8.txt', 'r') as namefile8:
            ttt_text8 = namefile8.readline()
    except FileNotFoundError as fileout8:
        print("[!] No file entryfile8.txt exist", fileout8)

    try:
        word_ttstop8 = (datetime.datetime.now() + \
            datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        file8 = open('./ttt/doc_ttt8/convdose.json')
        data8 = json.load(file8)
        for (key, value) in data8.items():
            listdata_x8 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            for x in listdata_x8:
                print(str(value[x]["Date of end"]))
                date_end8 = (str(value[x]["Date of end"]))
                if date_end8 == word_ttstop8:
                    print(date_end8)
                    name_treat8 = (str(value[x]["Treatment"]))
                    print(name_treat8)
                    dose_ttt8 = (str(value[x]["Dosage"]))
                    print(dose_ttt8)
                    MSBTTT2 = messagebox.showwarning('Warning',
                        'Look at TTT, there is a ttt to stop at' + " " + \
                        word_ttstop8 + " " + 'for : ' + "\n" + ttt_text8 + \
                        "\n" + "Date of end : " + date_end8 + "\n" + name_treat8 + \
                        " " + dose_ttt8)
                    MSGBOX = messagebox.askyesno("Ask", "Do you want to stop "\
                        "this reminder for the ttt : " + name_treat8 + " " + \
                        dose_ttt8 + " for " + ttt_text8 + " ?")
                    if MSGBOX == 1:
                        print("Reminder stop !")
                        file = open('./ttt/doc_ttt8/convdose.json')
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
                                    matin = (str(value[x]["Morning"]))
                                    midi = (str(value[x]["Midday"]))
                                    soir = (str(value[x]["Evening"]))
                                    nuit = (str(value[x]["Night"]))
                                    if value[x]["Date of end"] in word_ttstop:
                                        value[x]['Date of end'] = "! STOP ! -" + word_ttstop
                                    with open('./ttt/doc_ttt8/convdose.json', 'w') as re_file:
                                        json.dump(data, re_file, indent=4)
                                    upload8stopttt()
                                    break
    except IndexError as error_ttt8:
        print("[Err_1] No date of end has been found into file convdose.json (patient 8)",
            error_ttt8)
    except FileNotFoundError as info_ttt8:
        print("[Err_2] No date of end has been found into file convdose.json (patient 8)",
            info_ttt8)
    else:
        print("[Err_3] It's not date of end for tttapp.py 8")

    try:
        with open('./newpatient/entryfile9.txt', 'r') as namefile9:
            ttt_text9 = namefile9.readline()
    except FileNotFoundError as fileout9:
        print("[!] No file entryfile9.txt exist", fileout9)

    try:
        word_ttstop9 = (datetime.datetime.now() + \
            datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        file9 = open('./ttt/doc_ttt9/convdose.json')
        data9 = json.load(file9)
        for (key, value) in data9.items():
            listdata_x9 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            for x in listdata_x9:
                print(str(value[x]["Date of end"]))
                date_end9 = (str(value[x]["Date of end"]))
                if date_end9 == word_ttstop9:
                    print(date_end9)
                    name_treat9 = (str(value[x]["Treatment"]))
                    print(name_treat9)
                    dose_ttt9 = (str(value[x]["Dosage"]))
                    print(dose_ttt9)
                    MSBTTT2 = messagebox.showwarning('Warning',
                        'Look at TTT, there is a ttt to stop at' + " " + \
                        word_ttstop9 + " " + 'for : ' + "\n" + ttt_text9 + \
                        "\n" + "Date of end : " + date_end9 + "\n" + name_treat9 + \
                        " " + dose_ttt9)
                    MSGBOX = messagebox.askyesno("Ask", "Do you want to stop "\
                        "this reminder for the ttt : " + name_treat9 + " " + \
                        dose_ttt9 + " for " + ttt_text9 + " ?")
                    if MSGBOX == 1:
                        print("Reminder stop !")
                        file = open('./ttt/doc_ttt9/convdose.json')
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
                                    matin = (str(value[x]["Morning"]))
                                    midi = (str(value[x]["Midday"]))
                                    soir = (str(value[x]["Evening"]))
                                    nuit = (str(value[x]["Night"]))
                                    if value[x]["Date of end"] in word_ttstop:
                                        value[x]['Date of end'] = "! STOP ! -" + word_ttstop
                                    with open('./ttt/doc_ttt9/convdose.json', 'w') as re_file:
                                        json.dump(data, re_file, indent=4)
                                    upload9stopttt()
                                    break
    except IndexError as error_ttt9:
        print("[Err_1] No date of end has been found into file convdose.json (patient 9)",
            error_ttt9)
    except FileNotFoundError as info_ttt9:
        print("[Err_2] No date of end has been found into file convdose.json (patient 9)",
            info_ttt9)
    else:
        print("[Err_3] It's not date of end for tttapp.py 9")

    try:
        with open('./newpatient/entryfile10.txt', 'r') as namefile10:
            ttt_text10 = namefile10.readline()
    except FileNotFoundError as fileout10:
        print("[!] No file entryfile10.txt exist", fileout10)

    try:
        word_ttstop10 = (datetime.datetime.now() + \
            datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        file10 = open('./ttt/doc_ttt10/convdose.json')
        data10 = json.load(file10)
        for (key, value) in data10.items():
            listdata_x10 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            for x in listdata_x10:
                print(str(value[x]["Date of end"]))
                date_end10 = (str(value[x]["Date of end"]))
                if date_end10 == word_ttstop10:
                    print(date_end10)
                    name_treat10 = (str(value[x]["Treatment"]))
                    print(name_treat10)
                    dose_ttt10 = (str(value[x]["Dosage"]))
                    print(dose_ttt10)
                    MSBTTT2 = messagebox.showwarning('Warning',
                        'Look at TTT, there is a ttt to stop at' + " " + \
                        word_ttstop10 + " " + 'for : ' + "\n" + ttt_text10 + \
                        "\n" + "Date of end : " + date_end10 + "\n" + name_treat10 + \
                        " " + dose_ttt10)
                    MSGBOX = messagebox.askyesno("Ask", "Do you want to stop "\
                        "this reminder for the ttt : " + name_treat10 + " " + \
                        dose_ttt10 + " for " + ttt_text10 + " ?")
                    if MSGBOX == 1:
                        print("Reminder stop !")
                        file = open('./ttt/doc_ttt10/convdose.json')
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
                                    matin = (str(value[x]["Morning"]))
                                    midi = (str(value[x]["Midday"]))
                                    soir = (str(value[x]["Evening"]))
                                    nuit = (str(value[x]["Night"]))
                                    if value[x]["Date of end"] in word_ttstop:
                                        value[x]['Date of end'] = "! STOP ! -" + word_ttstop
                                    with open('./ttt/doc_ttt10/convdose.json', 'w') as re_file:
                                        json.dump(data, re_file, indent=4)
                                    upload10stopttt()
                                    break
    except IndexError as error_ttt10:
        print("[Err_1] No date of end has been found into file convdose.json (patient 10)",
            error_ttt10)
    except FileNotFoundError as info_ttt10:
        print("[Err_2] No date of end has been found into file convdose.json (patient 10)",
            info_ttt10)
    else:
        print("[Err_3] It's not date of end for tttapp.py 10")

    try:
        with open('./newpatient/entryfile11.txt', 'r') as namefile11:
            ttt_text11 = namefile11.readline()
    except FileNotFoundError as fileout11:
        print("[!] No file entryfile11.txt exist", fileout11)

    try:
        word_ttstop11 = (datetime.datetime.now() + \
            datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        file11 = open('./ttt/doc_ttt11/convdose.json')
        data11 = json.load(file11)
        for (key, value) in data11.items():
            listdata_x11 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            for x in listdata_x11:
                print(str(value[x]["Date of end"]))
                date_end11 = (str(value[x]["Date of end"]))
                if date_end11 == word_ttstop11:
                    print(date_end11)
                    name_treat11 = (str(value[x]["Treatment"]))
                    print(name_treat11)
                    dose_ttt11 = (str(value[x]["Dosage"]))
                    print(dose_ttt11)
                    MSBTTT2 = messagebox.showwarning('Warning',
                        'Look at TTT, there is a ttt to stop at' + " " + \
                        word_ttstop11 + " " + 'for : ' + "\n" + ttt_text11 + \
                        "\n" + "Date of end : " + date_end11 + "\n" + name_treat11 + \
                        " " + dose_ttt11)
                    MSGBOX = messagebox.askyesno("Ask", "Do you want to stop "\
                        "this reminder for the ttt : " + name_treat11 + " " + \
                        dose_ttt11 + " for " + ttt_text11 + " ?")
                    if MSGBOX == 1:
                        print("Reminder stop !")
                        file = open('./ttt/doc_ttt11/convdose.json')
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
                                    matin = (str(value[x]["Morning"]))
                                    midi = (str(value[x]["Midday"]))
                                    soir = (str(value[x]["Evening"]))
                                    nuit = (str(value[x]["Night"]))
                                    if value[x]["Date of end"] in word_ttstop:
                                        value[x]['Date of end'] = "! STOP ! -" + word_ttstop
                                    with open('./ttt/doc_ttt11/convdose.json', 'w') as re_file:
                                        json.dump(data, re_file, indent=4)
                                    upload11stopttt()
                                    break
    except IndexError as error_ttt11:
        print("[Err_1] No date of end has been found into file convdose.json (patient 11)",
            error_ttt11)
    except FileNotFoundError as info_ttt11:
        print("[Err_2] No date of end has been found into file convdose.json (patient 11)",
            info_ttt11)
    else:
        print("[Err_3] It's not date of end for tttapp.py 11")

    try:
        with open('./newpatient/entryfile12.txt', 'r') as namefile12:
            ttt_text12 = namefile12.readline()
    except FileNotFoundError as fileout12:
        print("[!] No file entryfile12.txt exist", fileout12)

    try:
        word_ttstop12 = (datetime.datetime.now() + \
            datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        file12 = open('./ttt/doc_ttt12/convdose.json')
        data12 = json.load(file12)
        for (key, value) in data12.items():
            listdata_x12 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            for x in listdata_x12:
                print(str(value[x]["Date of end"]))
                date_end12 = (str(value[x]["Date of end"]))
                if date_end12 == word_ttstop12:
                    print(date_end12)
                    name_treat12 = (str(value[x]["Treatment"]))
                    print(name_treat12)
                    dose_ttt12 = (str(value[x]["Dosage"]))
                    print(dose_ttt12)
                    MSBTTT2 = messagebox.showwarning('Warning',
                        'Look at TTT, there is a ttt to stop at' + " " + \
                        word_ttstop12 + " " + 'for : ' + "\n" + ttt_text12 + \
                        "\n" + "Date of end : " + date_end12 + "\n" + name_treat12 + \
                        " " + dose_ttt12)
                    MSGBOX = messagebox.askyesno("Ask", "Do you want to stop "\
                        "this reminder for the ttt : " + name_treat12 + " " + \
                        dose_ttt12 + " for " + ttt_text12 + " ?")
                    if MSGBOX == 1:
                        print("Reminder stop !")
                        file = open('./ttt/doc_ttt12/convdose.json')
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
                                    matin = (str(value[x]["Morning"]))
                                    midi = (str(value[x]["Midday"]))
                                    soir = (str(value[x]["Evening"]))
                                    nuit = (str(value[x]["Night"]))
                                    if value[x]["Date of end"] in word_ttstop:
                                        value[x]['Date of end'] = "! STOP ! -" + word_ttstop
                                    with open('./ttt/doc_ttt12/convdose.json', 'w') as re_file:
                                        json.dump(data, re_file, indent=4)
                                    upload12stopttt()
                                    break
    except IndexError as error_ttt12:
        print("[Err_1] No date of end has been found into file convdose.json (patient 12)",
            error_ttt12)
    except FileNotFoundError as info_ttt12:
        print("[Err_2] No date of end has been found into file convdose.json (patient 12)",
            info_ttt12)
    else:
        print("[Err_3] It's not date of end for tttapp.py 12")

    try:
        with open('./newpatient/entryfile13.txt', 'r') as namefile13:
            ttt_text13 = namefile13.readline()
    except FileNotFoundError as fileout13:
        print("[!] No file entryfile13.txt exist", fileout13)

    try:
        word_ttstop13 = (datetime.datetime.now() + \
            datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        file13 = open('./ttt/doc_ttt13/convdose.json')
        data13 = json.load(file13)
        for (key, value) in data13.items():
            listdata_x13 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            for x in listdata_x13:
                print(str(value[x]["Date of end"]))
                date_end13 = (str(value[x]["Date of end"]))
                if date_end13 == word_ttstop13:
                    print(date_end13)
                    name_treat13 = (str(value[x]["Treatment"]))
                    print(name_treat13)
                    dose_ttt13 = (str(value[x]["Dosage"]))
                    print(dose_ttt13)
                    MSBTTT2 = messagebox.showwarning('Warning',
                        'Look at TTT, there is a ttt to stop at' + " " + \
                        word_ttstop13 + " " + 'for : ' + "\n" + ttt_text13 + \
                        "\n" + "Date of end : " + date_end13 + "\n" + name_treat13 + \
                        " " + dose_ttt13)
                    MSGBOX = messagebox.askyesno("Ask", "Do you want to stop "\
                        "this reminder for the ttt : " + name_treat13 + " " + \
                        dose_ttt13 + " for " + ttt_text13 + " ?")
                    if MSGBOX == 1:
                        print("Reminder stop !")
                        file = open('./ttt/doc_ttt13/convdose.json')
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
                                    matin = (str(value[x]["Morning"]))
                                    midi = (str(value[x]["Midday"]))
                                    soir = (str(value[x]["Evening"]))
                                    nuit = (str(value[x]["Night"]))
                                    if value[x]["Date of end"] in word_ttstop:
                                        value[x]['Date of end'] = "! STOP ! -" + word_ttstop
                                    with open('./ttt/doc_ttt13/convdose.json', 'w') as re_file:
                                        json.dump(data, re_file, indent=4)
                                    upload13stopttt()
                                    break
    except IndexError as error_ttt13:
        print("[Err_1] No date of end has been found into file convdose.json (patient 13)",
            error_ttt13)
    except FileNotFoundError as info_ttt13:
        print("[Err_2] No date of end has been found into file convdose.json (patient 13)",
            info_ttt13)
    else:
        print("[Err_3] It's not date of end for tttapp.py 13")

    try:
        with open('./newpatient/entryfile14.txt', 'r') as namefile14:
            ttt_text14 = namefile14.readline()
    except FileNotFoundError as fileout14:
        print("[!] No file entryfile14.txt exist", fileout14)

    try:
        word_ttstop14 = (datetime.datetime.now() + \
            datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        file14 = open('./ttt/doc_ttt14/convdose.json')
        data14 = json.load(file14)
        for (key, value) in data14.items():
            listdata_x14 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            for x in listdata_x14:
                print(str(value[x]["Date of end"]))
                date_end14 = (str(value[x]["Date of end"]))
                if date_end14 == word_ttstop14:
                    print(date_end14)
                    name_treat14 = (str(value[x]["Treatment"]))
                    print(name_treat14)
                    dose_ttt14 = (str(value[x]["Dosage"]))
                    print(dose_ttt14)
                    MSBTTT2 = messagebox.showwarning('Warning',
                        'Look at TTT, there is a ttt to stop at' + " " + \
                        word_ttstop14 + " " + 'for : ' + "\n" + ttt_text14 + \
                        "\n" + "Date of end : " + date_end14 + "\n" + name_treat14 + \
                        " " + dose_ttt14)
                    MSGBOX = messagebox.askyesno("Ask", "Do you want to stop "\
                        "this reminder for the ttt : " + name_treat14 + " " + \
                        dose_ttt14 + " for " + ttt_text14 + " ?")
                    if MSGBOX == 1:
                        print("Reminder stop !")
                        file = open('./ttt/doc_ttt14/convdose.json')
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
                                    matin = (str(value[x]["Morning"]))
                                    midi = (str(value[x]["Midday"]))
                                    soir = (str(value[x]["Evening"]))
                                    nuit = (str(value[x]["Night"]))
                                    if value[x]["Date of end"] in word_ttstop:
                                        value[x]['Date of end'] = "! STOP ! -" + word_ttstop
                                    with open('./ttt/doc_ttt14/convdose.json', 'w') as re_file:
                                        json.dump(data, re_file, indent=4)
                                    upload14stopttt()
                                    break
    except IndexError as error_ttt14:
        print("[Err_1] No date of end has been found into file convdose.json (patient 14)",
            error_ttt14)
    except FileNotFoundError as info_ttt14:
        print("[Err_2] No date of end has been found into file convdose.json (patient 14)",
            info_ttt14)
    else:
        print("[Err_3] It's not date of end for tttapp.py 14")

    try:
        with open('./newpatient/entryfile15.txt', 'r') as namefile15:
            ttt_text15 = namefile15.readline()
    except FileNotFoundError as fileout15:
        print("[!] No file entryfile15.txt exist", fileout15)

    try:
        word_ttstop15 = (datetime.datetime.now() + \
            datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        file15 = open('./ttt/doc_ttt15/convdose.json')
        data15 = json.load(file15)
        for (key, value) in data15.items():
            listdata_x15 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            for x in listdata_x15:
                print(str(value[x]["Date of end"]))
                date_end15 = (str(value[x]["Date of end"]))
                if date_end15 == word_ttstop15:
                    print(date_end15)
                    name_treat15 = (str(value[x]["Treatment"]))
                    print(name_treat15)
                    dose_ttt15 = (str(value[x]["Dosage"]))
                    print(dose_ttt15)
                    MSBTTT2 = messagebox.showwarning('Warning',
                        'Look at TTT, there is a ttt to stop at' + " " + \
                        word_ttstop15 + " " + 'for : ' + "\n" + ttt_text15 + \
                        "\n" + "Date of end : " + date_end15 + "\n" + name_treat15 + \
                        " " + dose_ttt15)
                    MSGBOX = messagebox.askyesno("Ask", "Do you want to stop "\
                        "this reminder for the ttt : " + name_treat15 + " " + \
                        dose_ttt15 + " for " + ttt_text15 + " ?")
                    if MSGBOX == 1:
                        print("Reminder stop !")
                        file = open('./ttt/doc_ttt15/convdose.json')
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
                                    matin = (str(value[x]["Morning"]))
                                    midi = (str(value[x]["Midday"]))
                                    soir = (str(value[x]["Evening"]))
                                    nuit = (str(value[x]["Night"]))
                                    if value[x]["Date of end"] in word_ttstop:
                                        value[x]['Date of end'] = "! STOP ! -" + word_ttstop
                                    with open('./ttt/doc_ttt15/convdose.json', 'w') as re_file:
                                        json.dump(data, re_file, indent=4)
                                    upload15stopttt()
                                    break
    except IndexError as error_ttt15:
        print("[Err_1] No date of end has been found into file convdose.json (patient 15)",
            error_ttt15)
    except FileNotFoundError as info_ttt15:
        print("[Err_2] No date of end has been found into file convdose.json (patient 15)",
            info_ttt15)
    else:
        print("[Err_3] It's not date of end for tttapp.py 15")

    try:
        with open('./newpatient/entryfile16.txt', 'r') as namefile16:
            ttt_text16 = namefile16.readline()
    except FileNotFoundError as fileout16:
        print("[!] No file entryfile16.txt exist", fileout16)

    try:
        word_ttstop16 = (datetime.datetime.now() + \
            datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        file16 = open('./ttt/doc_ttt16/convdose.json')
        data16 = json.load(file16)
        for (key, value) in data16.items():
            listdata_x16 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            for x in listdata_x16:
                print(str(value[x]["Date of end"]))
                date_end16 = (str(value[x]["Date of end"]))
                if date_end16 == word_ttstop16:
                    print(date_end16)
                    name_treat16 = (str(value[x]["Treatment"]))
                    print(name_treat16)
                    dose_ttt16 = (str(value[x]["Dosage"]))
                    print(dose_ttt16)
                    MSBTTT2 = messagebox.showwarning('Warning',
                        'Look at TTT, there is a ttt to stop at' + " " + \
                        word_ttstop16 + " " + 'for : ' + "\n" + ttt_text16 + \
                        "\n" + "Date of end : " + date_end16 + "\n" + name_treat16 + \
                        " " + dose_ttt16)
                    MSGBOX = messagebox.askyesno("Ask", "Do you want to stop "\
                        "this reminder for the ttt : " + name_treat16 + " " + \
                        dose_ttt16 + " for " + ttt_text16 + " ?")
                    if MSGBOX == 1:
                        print("Reminder stop !")
                        file = open('./ttt/doc_ttt16/convdose.json')
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
                                    matin = (str(value[x]["Morning"]))
                                    midi = (str(value[x]["Midday"]))
                                    soir = (str(value[x]["Evening"]))
                                    nuit = (str(value[x]["Night"]))
                                    if value[x]["Date of end"] in word_ttstop:
                                        value[x]['Date of end'] = "! STOP ! -" + word_ttstop
                                    with open('./ttt/doc_ttt16/convdose.json', 'w') as re_file:
                                        json.dump(data, re_file, indent=4)
                                    upload16stopttt()
                                    break
    except IndexError as error_ttt16:
        print("[Err_1] No date of end has been found into file convdose.json (patient 16)",
            error_ttt16)
    except FileNotFoundError as info_ttt16:
        print("[Err_2] No date of end has been found into file convdose.json (patient 16)",
            info_ttt16)
    else:
        print("[Err_3] It's not date of end for tttapp.py 16")

    try:
        with open('./newpatient/entryfile17.txt', 'r') as namefile17:
            ttt_text17 = namefile17.readline()
    except FileNotFoundError as fileout17:
        print("[!] No file entryfile17.txt exist", fileout17)

    try:
        word_ttstop17 = (datetime.datetime.now() + \
            datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        file17 = open('./ttt/doc_ttt17/convdose.json')
        data17 = json.load(file17)
        for (key, value) in data17.items():
            listdata_x17 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            for x in listdata_x17:
                print(str(value[x]["Date of end"]))
                date_end17 = (str(value[x]["Date of end"]))
                if date_end17 == word_ttstop17:
                    print(date_end17)
                    name_treat17 = (str(value[x]["Treatment"]))
                    print(name_treat17)
                    dose_ttt17 = (str(value[x]["Dosage"]))
                    print(dose_ttt17)
                    MSBTTT2 = messagebox.showwarning('Warning',
                        'Look at TTT, there is a ttt to stop at' + " " + \
                        word_ttstop17 + " " + 'for : ' + "\n" + ttt_text17 + \
                        "\n" + "Date of end : " + date_end17 + "\n" + name_treat17 + \
                        " " + dose_ttt17)
                    MSGBOX = messagebox.askyesno("Ask", "Do you want to stop "\
                        "this reminder for the ttt : " + name_treat17 + " " + \
                        dose_ttt17 + " for " + ttt_text17 + " ?")
                    if MSGBOX == 1:
                        print("Reminder stop !")
                        file = open('./ttt/doc_ttt17/convdose.json')
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
                                    matin = (str(value[x]["Morning"]))
                                    midi = (str(value[x]["Midday"]))
                                    soir = (str(value[x]["Evening"]))
                                    nuit = (str(value[x]["Night"]))
                                    if value[x]["Date of end"] in word_ttstop:
                                        value[x]['Date of end'] = "! STOP ! -" + word_ttstop
                                    with open('./ttt/doc_ttt17/convdose.json', 'w') as re_file:
                                        json.dump(data, re_file, indent=4)
                                    upload17stopttt()
                                    break
    except IndexError as error_ttt17:
        print("[Err_1] No date of end has been found into file convdose.json (patient 17)",
            error_ttt17)
    except FileNotFoundError as info_ttt17:
        print("[Err_2] No date of end has been found into file convdose.json (patient 17)",
            info_ttt17)
    else:
        print("[Err_3] It's not date of end for tttapp.py 17")

    try:
        with open('./newpatient/entryfile18.txt', 'r') as namefile18:
            ttt_text18 = namefile18.readline()
    except FileNotFoundError as fileout18:
        print("[!] No file entryfile18.txt exist", fileout18)

    try:
        word_ttstop18 = (datetime.datetime.now() + \
            datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        file18 = open('./ttt/doc_ttt18/convdose.json')
        data18 = json.load(file18)
        for (key, value) in data18.items():
            listdata_x18 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            for x in listdata_x18:
                print(str(value[x]["Date of end"]))
                date_end18 = (str(value[x]["Date of end"]))
                if date_end18 == word_ttstop18:
                    print(date_end18)
                    name_treat18 = (str(value[x]["Treatment"]))
                    print(name_treat18)
                    dose_ttt18 = (str(value[x]["Dosage"]))
                    print(dose_ttt18)
                    MSBTTT2 = messagebox.showwarning('Warning',
                        'Look at TTT, there is a ttt to stop at' + " " + \
                        word_ttstop18 + " " + 'for : ' + "\n" + ttt_text18 + \
                        "\n" + "Date of end : " + date_end18 + "\n" + name_treat18 + \
                        " " + dose_ttt18)
                    MSGBOX = messagebox.askyesno("Ask", "Do you want to stop "\
                        "this reminder for the ttt : " + name_treat18 + " " + \
                        dose_ttt18 + " for " + ttt_text18 + " ?")
                    if MSGBOX == 1:
                        print("Reminder stop !")
                        file = open('./ttt/doc_ttt18/convdose.json')
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
                                    matin = (str(value[x]["Morning"]))
                                    midi = (str(value[x]["Midday"]))
                                    soir = (str(value[x]["Evening"]))
                                    nuit = (str(value[x]["Night"]))
                                    if value[x]["Date of end"] in word_ttstop:
                                        value[x]['Date of end'] = "! STOP ! -" + word_ttstop
                                    with open('./ttt/doc_ttt18/convdose.json', 'w') as re_file:
                                        json.dump(data, re_file, indent=4)
                                    upload18stopttt()
                                    break
    except IndexError as error_ttt18:
        print("[Err_1] No date of end has been found into file convdose.json (patient 18)",
            error_ttt18)
    except FileNotFoundError as info_ttt18:
        print("[Err_2] No date of end has been found into file convdose.json (patient 18)",
            info_ttt18)
    else:
        print("[Err_3] It's not date of end for tttapp.py 18")

    try:
        with open('./newpatient/entryfile19.txt', 'r') as namefile19:
            ttt_text19 = namefile19.readline()
    except FileNotFoundError as fileout19:
        print("[!] No file entryfile19.txt exist", fileout19)

    try:
        word_ttstop19 = (datetime.datetime.now() + \
            datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        file19 = open('./ttt/doc_ttt19/convdose.json')
        data19 = json.load(file19)
        for (key, value) in data19.items():
            listdata_x19 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            for x in listdata_x19:
                print(str(value[x]["Date of end"]))
                date_end19 = (str(value[x]["Date of end"]))
                if date_end19 == word_ttstop19:
                    print(date_end19)
                    name_treat19 = (str(value[x]["Treatment"]))
                    print(name_treat19)
                    dose_ttt19 = (str(value[x]["Dosage"]))
                    print(dose_ttt19)
                    MSBTTT2 = messagebox.showwarning('Warning',
                        'Look at TTT, there is a ttt to stop at' + " " + \
                        word_ttstop19 + " " + 'for : ' + "\n" + ttt_text19 + \
                        "\n" + "Date of end : " + date_end19 + "\n" + name_treat19 + \
                        " " + dose_ttt19)
                    MSGBOX = messagebox.askyesno("Ask", "Do you want to stop "\
                        "this reminder for the ttt : " + name_treat19 + " " + \
                        dose_ttt19 + " for " + ttt_text19 + " ?")
                    if MSGBOX == 1:
                        print("Reminder stop !")
                        file = open('./ttt/doc_ttt19/convdose.json')
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
                                    matin = (str(value[x]["Morning"]))
                                    midi = (str(value[x]["Midday"]))
                                    soir = (str(value[x]["Evening"]))
                                    nuit = (str(value[x]["Night"]))
                                    if value[x]["Date of end"] in word_ttstop:
                                        value[x]['Date of end'] = "! STOP ! -" + word_ttstop
                                    with open('./ttt/doc_ttt19/convdose.json', 'w') as re_file:
                                        json.dump(data, re_file, indent=4)
                                    upload19stopttt()
                                    break
    except IndexError as error_ttt19:
        print("[Err_1] No date of end has been found into file convdose.json (patient 19)",
            error_ttt19)
    except FileNotFoundError as info_ttt19:
        print("[Err_2] No date of end has been found into file convdose.json (patient 19)",
            info_ttt19)
    else:
        print("[Err_3] It's not date of end for tttapp.py 19")

    try:
        with open('./newpatient/entryfile20.txt', 'r') as namefile20:
            ttt_text20 = namefile20.readline()
    except FileNotFoundError as fileout20:
        print("[!] No file entryfile20.txt exist", fileout20)

    try:
        word_ttstop20 = (datetime.datetime.now() + \
            datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        file20 = open('./ttt/doc_ttt20/convdose.json')
        data20 = json.load(file20)
        for (key, value) in data20.items():
            listdata_x20 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            for x in listdata_x20:
                print(str(value[x]["Date of end"]))
                date_end20 = (str(value[x]["Date of end"]))
                if date_end20 == word_ttstop20:
                    print(date_end20)
                    name_treat20 = (str(value[x]["Treatment"]))
                    print(name_treat20)
                    dose_ttt20 = (str(value[x]["Dosage"]))
                    print(dose_ttt20)
                    MSBTTT2 = messagebox.showwarning('Warning',
                        'Look at TTT, there is a ttt to stop at' + " " + \
                        word_ttstop20 + " " + 'for : ' + "\n" + ttt_text20 + \
                        "\n" + "Date of end : " + date_end20 + "\n" + name_treat20 + \
                        " " + dose_ttt20)
                    MSGBOX = messagebox.askyesno("Ask", "Do you want to stop "\
                        "this reminder for the ttt : " + name_treat20 + " " + \
                        dose_ttt20 + " for " + ttt_text20 + " ?")
                    if MSGBOX == 1:
                        print("Reminder stop !")
                        file = open('./ttt/doc_ttt20/convdose.json')
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
                                    matin = (str(value[x]["Morning"]))
                                    midi = (str(value[x]["Midday"]))
                                    soir = (str(value[x]["Evening"]))
                                    nuit = (str(value[x]["Night"]))
                                    if value[x]["Date of end"] in word_ttstop:
                                        value[x]['Date of end'] = "! STOP ! -" + word_ttstop
                                    with open('./ttt/doc_ttt20/convdose.json', 'w') as re_file:
                                        json.dump(data, re_file, indent=4)
                                    upload20stopttt()
                                    break
    except IndexError as error_ttt20:
        print("[Err_1] No date of end has been found into file convdose.json (patient 20)",
            error_ttt20)
    except FileNotFoundError as info_ttt20:
        print("[Err_2] No date of end has been found into file convdose.json (patient 20)",
            info_ttt20)
    else:
        print("[Err_3] It's not date of end for tttapp.py 20")

    try:
        with open('./newpatient/entryfile21.txt', 'r') as namefile21:
            ttt_text21 = namefile21.readline()
    except FileNotFoundError as fileout21:
        print("[!] No file entryfile21.txt exist", fileout21)

    try:
        word_ttstop21 = (datetime.datetime.now() + \
            datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        file21 = open('./ttt/doc_ttt21/convdose.json')
        data21 = json.load(file21)
        for (key, value) in data21.items():
            listdata_x21 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            for x in listdata_x21:
                print(str(value[x]["Date of end"]))
                date_end21 = (str(value[x]["Date of end"]))
                if date_end21 == word_ttstop21:
                    print(date_end21)
                    name_treat21 = (str(value[x]["Treatment"]))
                    print(name_treat21)
                    dose_ttt21 = (str(value[x]["Dosage"]))
                    print(dose_ttt21)
                    MSBTTT2 = messagebox.showwarning('Warning',
                        'Look at TTT, there is a ttt to stop at' + " " + \
                        word_ttstop21 + " " + 'for : ' + "\n" + ttt_text21 + \
                        "\n" + "Date of end : " + date_end21 + "\n" + name_treat21 + \
                        " " + dose_ttt21)
                    MSGBOX = messagebox.askyesno("Ask", "Do you want to stop "\
                        "this reminder for the ttt : " + name_treat21 + " " + \
                        dose_ttt21 + " for " + ttt_text21 + " ?")
                    if MSGBOX == 1:
                        print("Reminder stop !")
                        file = open('./ttt/doc_ttt21/convdose.json')
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
                                    matin = (str(value[x]["Morning"]))
                                    midi = (str(value[x]["Midday"]))
                                    soir = (str(value[x]["Evening"]))
                                    nuit = (str(value[x]["Night"]))
                                    if value[x]["Date of end"] in word_ttstop:
                                        value[x]['Date of end'] = "! STOP ! -" + word_ttstop
                                    with open('./ttt/doc_ttt21/convdose.json', 'w') as re_file:
                                        json.dump(data, re_file, indent=4)
                                    upload21stopttt()
                                    break
    except IndexError as error_ttt21:
        print("[Err_1] No date of end has been found into file convdose.json (patient 21)",
            error_ttt21)
    except FileNotFoundError as info_ttt21:
        print("[Err_2] No date of end has been found into file convdose.json (patient 21)",
            info_ttt21)
    else:
        print("[Err_3] It's not date of end for tttapp.py 21")

    try:
        with open('./newpatient/entryfile22.txt', 'r') as namefile22:
            ttt_text22 = namefile22.readline()
    except FileNotFoundError as fileout22:
        print("[!] No file entryfile22.txt exist", fileout22)

    try:
        word_ttstop22 = (datetime.datetime.now() + \
            datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        file22 = open('./ttt/doc_ttt22/convdose.json')
        data22 = json.load(file22)
        for (key, value) in data22.items():
            listdata_x22 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            for x in listdata_x22:
                print(str(value[x]["Date of end"]))
                date_end22 = (str(value[x]["Date of end"]))
                if date_end22 == word_ttstop22:
                    print(date_end22)
                    name_treat22 = (str(value[x]["Treatment"]))
                    print(name_treat22)
                    dose_ttt22 = (str(value[x]["Dosage"]))
                    print(dose_ttt22)
                    MSBTTT2 = messagebox.showwarning('Warning',
                        'Look at TTT, there is a ttt to stop at' + " " + \
                        word_ttstop22 + " " + 'for : ' + "\n" + ttt_text22 + \
                        "\n" + "Date of end : " + date_end22 + "\n" + name_treat22 + \
                        " " + dose_ttt22)
                    MSGBOX = messagebox.askyesno("Ask", "Do you want to stop "\
                        "this reminder for the ttt : " + name_treat22 + " " + \
                        dose_ttt22 + " for " + ttt_text22 + " ?")
                    if MSGBOX == 1:
                        print("Reminder stop !")
                        file = open('./ttt/doc_ttt22/convdose.json')
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
                                    matin = (str(value[x]["Morning"]))
                                    midi = (str(value[x]["Midday"]))
                                    soir = (str(value[x]["Evening"]))
                                    nuit = (str(value[x]["Night"]))
                                    if value[x]["Date of end"] in word_ttstop:
                                        value[x]['Date of end'] = "! STOP ! -" + word_ttstop
                                    with open('./ttt/doc_ttt22/convdose.json', 'w') as re_file:
                                        json.dump(data, re_file, indent=4)
                                    upload22stopttt()
                                    break
    except IndexError as error_ttt22:
        print("[Err_1] No date of end has been found into file convdose.json (patient 22)",
            error_ttt22)
    except FileNotFoundError as info_ttt22:
        print("[Err_2] No date of end has been found into file convdose.json (patient 22)",
            info_ttt22)
    else:
        print("[Err_3] It's not date of end for tttapp.py 22")

    try:
        with open('./newpatient/entryfile23.txt', 'r') as namefile23:
            ttt_text23 = namefile23.readline()
    except FileNotFoundError as fileout23:
        print("[!] No file entryfile23.txt exist", fileout23)

    try:
        word_ttstop23 = (datetime.datetime.now() + \
            datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        file23 = open('./ttt/doc_ttt23/convdose.json')
        data23 = json.load(file23)
        for (key, value) in data23.items():
            listdata_x23 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            for x in listdata_x23:
                print(str(value[x]["Date of end"]))
                date_end23 = (str(value[x]["Date of end"]))
                if date_end23 == word_ttstop23:
                    print(date_end23)
                    name_treat23 = (str(value[x]["Treatment"]))
                    print(name_treat23)
                    dose_ttt23 = (str(value[x]["Dosage"]))
                    print(dose_ttt23)
                    MSBTTT2 = messagebox.showwarning('Warning',
                        'Look at TTT, there is a ttt to stop at' + " " + \
                        word_ttstop23 + " " + 'for : ' + "\n" + ttt_text23 + \
                        "\n" + "Date of end : " + date_end23 + "\n" + name_treat23 + \
                        " " + dose_ttt23)
                    MSGBOX = messagebox.askyesno("Ask", "Do you want to stop "\
                        "this reminder for the ttt : " + name_treat23 + " " + \
                        dose_ttt23 + " for " + ttt_text23 + " ?")
                    if MSGBOX == 1:
                        print("Reminder stop !")
                        file = open('./ttt/doc_ttt23/convdose.json')
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
                                    matin = (str(value[x]["Morning"]))
                                    midi = (str(value[x]["Midday"]))
                                    soir = (str(value[x]["Evening"]))
                                    nuit = (str(value[x]["Night"]))
                                    if value[x]["Date of end"] in word_ttstop:
                                        value[x]['Date of end'] = "! STOP ! -" + word_ttstop
                                    with open('./ttt/doc_ttt23/convdose.json', 'w') as re_file:
                                        json.dump(data, re_file, indent=4)
                                    upload23stopttt()
                                    break
    except IndexError as error_ttt23:
        print("[Err_1] No date of end has been found into file convdose.json (patient 23)",
            error_ttt23)
    except FileNotFoundError as info_ttt23:
        print("[Err_2] No date of end has been found into file convdose.json (patient 23)",
            info_ttt23)
    else:
        print("[Err_3] It's not date of end for tttapp.py 23")

    try:
        with open('./newpatient/entryfile24.txt', 'r') as namefile24:
            ttt_text24 = namefile24.readline()
    except FileNotFoundError as fileout24:
        print("[!] No file entryfile24.txt exist", fileout24)

    try:
        word_ttstop24 = (datetime.datetime.now() + \
            datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        file24 = open('./ttt/doc_ttt24/convdose.json')
        data24 = json.load(file24)
        for (key, value) in data24.items():
            listdata_x24 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            for x in listdata_x24:
                print(str(value[x]["Date of end"]))
                date_end24 = (str(value[x]["Date of end"]))
                if date_end24 == word_ttstop24:
                    print(date_end24)
                    name_treat24 = (str(value[x]["Treatment"]))
                    print(name_treat24)
                    dose_ttt24 = (str(value[x]["Dosage"]))
                    print(dose_ttt24)
                    MSBTTT2 = messagebox.showwarning('Warning',
                        'Look at TTT, there is a ttt to stop at' + " " + \
                        word_ttstop24 + " " + 'for : ' + "\n" + ttt_text24 + \
                        "\n" + "Date of end : " + date_end24 + "\n" + name_treat24 + \
                        " " + dose_ttt24)
                    MSGBOX = messagebox.askyesno("Ask", "Do you want to stop "\
                        "this reminder for the ttt : " + name_treat24 + " " + \
                        dose_ttt24 + " for " + ttt_text24 + " ?")
                    if MSGBOX == 1:
                        print("Reminder stop !")
                        file = open('./ttt/doc_ttt24/convdose.json')
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
                                    matin = (str(value[x]["Morning"]))
                                    midi = (str(value[x]["Midday"]))
                                    soir = (str(value[x]["Evening"]))
                                    nuit = (str(value[x]["Night"]))
                                    if value[x]["Date of end"] in word_ttstop:
                                        value[x]['Date of end'] = "! STOP ! -" + word_ttstop
                                    with open('./ttt/doc_ttt24/convdose.json', 'w') as re_file:
                                        json.dump(data, re_file, indent=4)
                                    upload24stopttt()
                                    break
    except IndexError as error_ttt24:
        print("[Err_1] No date of end has been found into file convdose.json (patient 24)",
            error_ttt24)
    except FileNotFoundError as info_ttt24:
        print("[Err_2] No date of end has been found into file convdose.json (patient 24)",
            info_ttt24)
    else:
        print("[Err_3] It's not date of end for tttapp.py 24")
