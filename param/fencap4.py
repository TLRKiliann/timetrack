#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
    This main app introduce parameters
    and send back graphical matplotlib
    representations.
"""


import tkinter as tk
from tkinter import messagebox
import json
import os
import subprocess
import time
from downloader.progresstask4 import downloadata
from uploader.uploadbar import uploadmain
from uploader.upload4 import uploadata


def tocallprogressbar():
    """
        To display progress bar with current download
    """
    downloadata()
tocallprogressbar()

def writeData(textDate, textHour, textName, textTa, textDia,
        textPuls, textSa, textFr, textTemp, textHgt, textDlrs):
    """
        To export data in a json file
        and launching aspiFile4.py
    """
    try:
        if os.path.getsize('./param/paramdata4.txt'):
            print("[+] File 'paramdata4.txt' exist !")
    except FileNotFoundError as info:
        print("[!] F]ile : 'paramdata4.txt' doesn't exist !", info)
        print("[+] File 'paramdata4.txt' created !")
    finally:
        with open('./param/paramdata4.txt', 'a+') as file:
            file.write(str("Date : "))
            file.write(textDate.get() + '\n')
            file.write(str("Hour : "))
            file.write(textHour.get() + '\n')
            file.write(str("Name and Surname : "))
            file.write(textName.get() + '\n')
            file.write(str("TA : "))
            file.write(textTa.get() + '/')
            file.write(textDia.get() + "mmHg\n")
            file.write(str("Puls : "))
            file.write(textPuls.get() + "/min\n")
            file.write(str("SaO2 : "))
            file.write(textSa.get() + "%\n")
            file.write(str("FR : "))
            file.write(textFr.get() + "/min\n")
            file.write(str("Temperature : "))
            file.write(textTemp.get() + "°C\n")
            file.write(str("Glycemie : "))
            file.write(textHgt.get() + " mmol/l\n")
            file.write(str("Douleurs (Pain) : "))
            file.write(textDlrs.get() +"/10\n\n")

    try:
        if os.path.getsize('./param/aspifile4/systol.json'):
            print("[+] File 'systol' exist !")
            with open('./param/aspifile4/systol.json', 'r') as datafile:
                datastore = json.load(datafile)
                print(datastore)
            dataTa = datastore
            dataTa['data'].append({'Date' : textDate.get() + ' : ' + textHour.get(),
                'Systol' : textTa.get()})
            if textTa.get() == "":
                print("[!] No 'Systol' saved !")
            else:
                print("[rec] Ok 'Systol' saved !")
                with open('./param/aspifile4/systol.json', 'w') as datafile2:
                    json.dump(dataTa, datafile2, indent=4)
    except FileNotFoundError as outcom:
        print('[!] Sorry, file systol.json not exist !')
        print(str(outcom))
        print("[+] File systol.json created !")
        dataTa = {}
        dataTa['data'] = []
        dataTa['data'].append({'Date' : textDate.get() + ' : ' + textHour.get(),
            'Systol' : textTa.get()})
        if textTa.get() == "":
            print("[!] No 'Systol' saved !")
        else:
            print("[rec] Ok 'Systol' saved !")
            with open('./param/aspifile4/systol.json', 'w') as datafile:
                json.dump(dataTa, datafile, indent=4)

    try:
        if os.path.getsize('./param/aspifile4/diastol.json'):
            print("[+] File 'diastol' exist !")
            with open('./param/aspifile4/diastol.json', 'r') as datafile:
                datastore = json.load(datafile)
                print(datastore)
            dataDia = datastore
            dataDia['data'].append({'Date' : textDate.get() + ' : ' + textHour.get(),
                'Diastol' : textDia.get()})
            if textDia.get() == "":
                print("[!] No 'Diastol' saved !")
            else:
                print("[rec] Ok 'Diastol' saved !")
                with open('./param/aspifile4/diastol.json', 'w') as datafile2:
                    json.dump(dataDia, datafile2, indent=4)
    except FileNotFoundError as outcom:
        print('[!] Sorry, file diastol.json not exist !')
        print(str(outcom))
        print("[+] File diastol.json created !")
        dataDia = {}
        dataDia['data'] = []
        dataDia['data'].append({'Date' : textDate.get() + ' : ' + textHour.get(),
            'Diastol' : textDia.get()})
        if textDia.get() == "":
            print("[!] No 'Diastol' saved !")
        else:
            print("[rec] Ok 'Diastol' saved !")
            with open('./param/aspifile4/diastol.json', 'w') as datafile:
                json.dump(dataDia, datafile, indent=4)

    try:
        if os.path.getsize('./param/aspifile4/puls.json'):
            print("[+] File 'puls' exist !")
            with open('./param/aspifile4/puls.json', 'r') as datapuls:
                datastore = json.load(datapuls)
                print(datastore)
            dataP = datastore
            dataP['data'].append({'Date' : textDate.get() + ' : ' + textHour.get(),
                'Puls' : textPuls.get()})
            if textPuls.get() == "":
                print("[!] No 'Puls' saved !")
            else:
                print("[rec] Ok 'Puls' saved !")
                with open('./param/aspifile4/puls.json', 'w') as datapuls2:
                    json.dump(dataP, datapuls2, indent=4)
    except FileNotFoundError as errorfile1:
        print('[!] Sorry, file puls.json not exist !')
        print(str(errorfile1))
        print("[+] File puls.json created !")
        dataP = {}
        dataP['data'] = []
        dataP['data'].append({'Date' : textDate.get() + ' : ' + textHour.get(),
            'Puls' : textPuls.get()})
        if textPuls.get() == "":
            print("[!] No 'Puls' saved !")
        else:
            print("[rec] Ok 'Puls' saved !")
            with open('./param/aspifile4/puls.json', 'w') as datapuls3:
                json.dump(dataP, datapuls3, indent=4)

    try:
        if os.path.getsize('./param/aspifile4/sat.json'):
            print("[+] File 'sat' exist !")
            with open('./param/aspifile4/sat.json', 'r') as datasat:
                datastore = json.load(datasat)
                print(datastore)
            dataS = datastore
            dataS['data'].append({'Date' : textDate.get() + ' : ' + textHour.get(),
                'SaO2' : textSa.get()})
            if textSa.get() == "":
                print("[!] No 'SaO2' saved !")
            else:
                print("[rec] Ok 'SaO2' saved !")
                with open('./param/aspifile4/sat.json', 'w') as datasat2:
                    json.dump(dataS, datasat2, indent=4)
    except FileNotFoundError as errorfile2:
        print('[!] Sorry, file sat.json not exist !')
        print(str(errorfile2))
        print("[+] File sat.json created !")
        dataS = {}
        dataS['data'] = []
        dataS['data'].append({'Date' : textDate.get() + ' : ' + textHour.get(),
            'SaO2' : textSa.get()})
        if textSa.get() == "":
            print("[!] No 'SaO2' saved !")
        else:
            print("[rec] Ok 'SaO2' saved !")
            with open('./param/aspifile4/sat.json', 'w') as datasat3:
                json.dump(dataS, datasat3, indent=4)

    try:
        if os.path.getsize('./param/aspifile4/freq.json'):
            print("[+] File 'freq' exist !")
            with open('./param/aspifile4/freq.json', 'r') as datafreq:
                datastore = json.load(datafreq)
                print(datastore)
            dataF = datastore
            dataF['data'].append({'Date' : textDate.get() + ' : ' + textHour.get(),
                'FR' : textFr.get()})
            if textFr.get() == "":
                print("[!] No 'FR' saved !")
            else:
                print("[rec] Ok 'FR' saved !")
                with open('./param/aspifile4/freq.json', 'w') as datafreq2:
                    json.dump(dataF, datafreq2, indent=4)
    except FileNotFoundError as errorfile3:
        print('[!] Sorry, file freq.json not exist !')
        print(str(errorfile3))
        print("[+] File freq.json created !")
        dataF = {}
        dataF['data'] = []
        dataF['data'].append({'Date' : textDate.get() + ' : ' + textHour.get(),
            'FR' : textFr.get()})
        if textFr.get() == "":
            print("[!] No 'FR' saved !")
        else:
            print("[rec] Ok 'FR' saved !")
            with open('./param/aspifile4/freq.json', 'w') as datafreq3:
                json.dump(dataF, datafreq3, indent=4)

    try:
        if os.path.getsize('./param/aspifile4/temp.json'):
            print("[+] File 'temp' exist !")
            with open('./param/aspifile4/temp.json', 'r') as datatemp:
                datastore = json.load(datatemp)
                print(datastore)
            dataTe2 = datastore
            dataTe2['data'].append({'Date' : textDate.get() + ' : ' + textHour.get(),
                'Temperature' : textTemp.get()})
            if textTemp.get() == "":
                print("[!] No 'Temperature' saved !")
            else:
                print("[rec] Ok 'Temperature' saved !")
                with open('./param/aspifile4/temp.json', 'w') as datatemp2:
                    json.dump(dataTe2, datatemp2, indent=4)
    except FileNotFoundError as errorfile4:
        print('[!] Sorry, file temp.json not exist !')
        print(str(errorfile4))
        print("[+] File temp.json created !")
        dataTe2 = {}
        dataTe2['data'] = []
        dataTe2['data'].append({'Date' : textDate.get() + ' : ' + textHour.get(),
            'Temperature' : textTemp.get()})
        if textTemp.get() == "":
            print("[!] No 'Temperature' saved !")
        else:
            print("[rec] Ok 'Temperature' saved !")
            with open('./param/aspifile4/temp.json', 'w') as datatemp3:
                json.dump(dataTe2, datatemp3, indent=4)

    try:
        if os.path.getsize('./param/aspifile4/gly.json'):
            print("[+] File 'gly' exist !")
            with open('./param/aspifile4/gly.json', 'r') as datagly:
                datastore = json.load(datagly)
                print(datastore)
            dataG = datastore
            dataG['data'].append({'Date' : textDate.get() + ' : ' + textHour.get(),
                'Glycemie' : textHgt.get()})
            if textHgt.get() == "":
                print("[!] No 'Glycemie' saved !")
            else:
                print("[rec] Ok 'Glycemie' saved !")
                with open('./param/aspifile4/gly.json', 'w') as datagly2:
                    json.dump(dataG, datagly2, indent=4)
    except FileNotFoundError as errorfile5:
        print('[!] Sorry, file gly.json not exist !')
        print(str(errorfile5))
        print("[+] File gly.json created !")
        dataG = {}
        dataG['data'] = []
        dataG['data'].append({'Date' : textDate.get() + ' : ' + textHour.get(),
            'Glycemie' : textHgt.get()})
        if textHgt.get() == "":
            print("[!] No 'Glycemie' saved !")
        else:
            print("[rec] Ok 'Glycemie' saved !")
            with open('./param/aspifile4/gly.json', 'w') as datagly3:
                json.dump(dataG, datagly3, indent=4)

    try:
        if os.path.getsize('./param/aspifile4/dlr.json'):
            print("[+] File 'dlr' exist !")
            with open('./param/aspifile4/dlr.json', 'r') as datadlr:
                datastore = json.load(datadlr)
                print(datastore)
            dataD = datastore
            dataD['data'].append({'Date' : textDate.get() + ' : ' + textHour.get(),
                'Douleurs' : textDlrs.get()})
            if textDlrs.get() == "":
                print("[!] No 'Douleurs' saved !")
            else:
                print("[rec] Ok 'Douleurs' saved !")
                with open('./param/aspifile4/dlr.json', 'w') as datadlr2:
                    json.dump(dataD, datadlr2, indent=4)
    except FileNotFoundError as errorfile6:
        print('[!] Sorry, file dlr.json not exist !')
        print(str(errorfile6))
        print("[+] File dlr.json created !")
        dataD = {}
        dataD['data'] = []
        dataD['data'].append({'Date' : textDate.get() + ' : ' + textHour.get(),
            'Douleurs' : textDlrs.get()})
        if textDlrs.get() == "":
            print("[!] No 'Douleurs' saved !")
        else:
            print("[rec] Ok 'Douleurs' saved !")
            with open('./param/aspifile4/dlr.json', 'w') as datadlr3:
                json.dump(dataD, datadlr3, indent=4)

    label['text'] = ("Date: " + textDate.get() +
        "\nNom: " + textName.get() +
        "\nTension: " + textTa.get() + '/' + textDia.get() +
        " -- " + "Puls: " + textPuls.get() +
        "\nSaO2: " + textSa.get() +" -- "+ "FR: " + textFr.get() +
        "\nTemperature: " + textTemp.get() +
        "\nGlycemie: " + textHgt.get() +
        "\nDouleurs: " + textDlrs.get() +
        "\nAll data have been added in json files. Press < Graph > button to upload data !")

    uploadfunc()

def uploadfunc():
    uploadata()

def mainRead():
    try:
        if os.path.getsize('./param/main_read4.py'):
            subprocess.run('./param/main_read4.py', check=True)
    except FileNotFoundError as fnfe_read:
        print("[!] Sorry, file main_read4.py not found !")
        label['text'] = "Sorry, file main_read4.py not found !"

def appelTens(textDate, textName, textTa, textDia):
    """
        to call aspidata.py for recapt data
        and launching matplotlib graph
    """
    try:
        if os.path.getsize('./param/aspifile4/systol.json'):
            uploadcall()
            subprocess.run('./param/aspifile4/aspidata.py', check=True)
            label['text'] = ("Date: " + textDate.get() +
                "\nNom: " + textName.get() +
                "\nTension: " + textTa.get() + '/' + textDia.get())
    except FileNotFoundError as errorgraph1:
        print('[!] Sorry the TA plot doesn\'t work ! Data missing !', errorgraph1)
        label['text'] = "Sorry the TA plot doesn\'t work ! Data missing !"

def appelPuls(textDate, textName, textPuls):
    """
        to call aspipuls.py for recapt data
        and launching matplotlib graph
    """
    try:
        if os.path.getsize('./param/aspifile4/puls.json'):
            uploadcall()
            subprocess.run('./param/aspifile4/aspipuls.py', check=True)
            label['text'] = ("Date: " + textDate.get() +
                "\nNom: " + textName.get() +
                "\nPulsations: " + textPuls.get())
    except FileNotFoundError as errorgraph2:
        print('[!] Sorry the Puls plot doesn\'t work ! Data missing !', errorgraph2)
        label['text'] = "Sorry the Puls plot doesn\'t work ! Data missing !"

def appelSat(textDate, textName, textSa):
    """
        to call aspisat.py for recapt data
        and launching matplotlib graph
    """
    try:
        if os.path.getsize('./param/aspifile4/sat.json'):
            uploadcall()
            subprocess.run('./param/aspifile4/aspisat.py', check=True)
            label['text'] = ("Date: " + textDate.get() +
                "\nNom: " + textName.get() +
                "\nSaO2: " + textSa.get())
    except FileNotFoundError as errorgraph3:
        print('[!] Sorry the SaO2 plot doesn\'t work ! Data missing !', errorgraph3)
        label['text'] = "Sorry the SaO2 plot doesn\'t work ! Data missing !"

def appelFreq(textDate, textName, textFr):
    """
        to call aspifreq.py for recapt data
        and launching matplotlib graph
    """
    try:
        if os.path.getsize('./param/aspifile4/freq.json'):
            uploadcall()
            subprocess.run('./param/aspifile4/aspifreq.py', check=True)
            label['text'] = ("Date: " + textDate.get() +
                "\nNom: " + textName.get() +
                "\nFrequ. resp.: " + textFr.get())
    except FileNotFoundError as errorgraph4:
        print('[!] Sorry the FR plot doesn\'t work ! Data missing !', errorgraph4)
        label['text'] = "Sorry the FR plot doesn\'t work ! Data missing !"

def appelTemp(textDate, textName, textTemp):
    """
        to call aspitemp.py for recapt data
        and launching matplotlib graph
    """
    try:
        if os.path.getsize('./param/aspifile4/temp.json'):
            uploadcall()
            subprocess.run('./param/aspifile4/aspitemp.py', check=True)
            label['text'] = ("Date: " + textDate.get() +
                "\nNom: " + textName.get() +
                "\nTemperature: " + textTemp.get())
    except FileNotFoundError as errorgraph5:
        print('[!] Sorry the Temp plot doesn\'t work ! Data missing !', errorgraph5)
        label['text'] = "Sorry the Temp plot doesn\'t work ! Data missing !"

def appelGly(textDate, textName, textHgt):
    """
        to call aspigly.py for recapt data
        and launching matplotlib graph
    """
    try:
        if os.path.getsize('./param/aspifile4/gly.json'):
            uploadcall()
            subprocess.run('./param/aspifile4/aspigly.py', check=True)
            label['text'] = ("Date: " + textDate.get() +
                "\nNom: " + textName.get() +
                "\nGlycémie: " + textHgt.get())
    except FileNotFoundError as errorgraph6:
        print('[!] Sorry the Hgt plot doesn\'t work ! Data missing !', errorgraph6)
        label['text'] = "Sorry the Hgt plot doesn\'t work ! Data missing !"

def appelDlr(textDate, textName, textDlrs):
    """
        to call aspidlr.py for recapt data
        and launching matplotlib graph
    """
    try:
        if os.path.getsize('./param/aspifile4/dlr.json'):
            uploadcall()
            subprocess.run('./param/aspifile4/aspidlr.py', check=True)
            label['text'] = ("Date: " + textDate.get() +
                "\nNom: " + textName.get() +
                "\nDouleurs: " + textDlrs.get())
    except FileNotFoundError as errorgraph7:
        print('[!] Sorry the Dlrs plot doesn\'t work ! Data missing !', errorgraph7)
        label['text'] = "Sorry the Dlrs plot doesn\'t work ! Data missing !"

def uploadcall():
    uploadmain()

def delSystolDia():
    """
        To erase last line
        of systol.json
    """
    try:
        if os.path.getsize('./param/aspifile4/systol.json'):
            with open('./param/aspifile4/systol.json', 'r') as filesys:
                data = json.load(filesys)
            for key, value in data.items():
                print("[del] Last systol deleted")
                print(value[-1])
                del value[-1]
            with open('./param/aspifile4/systol.json', 'w') as file:
                json.dump(data, file, indent=4)
            label['text'] = "Last value of 'systol.json' has been deleted !"
            print("[del] Last 'systol.json' has been deleted !")
    except (FileNotFoundError, IndexError) as out_ta:
        label['text'] = "Sorry, file asked not exist !"
        print('[!] Sorry, file asked not exist !', out_ta)
    """
        To erase last line
        of diastol.json
    """
    try:
        if os.path.getsize('./param/aspifile4/diastol.json'):
            with open('./param/aspifile4/diastol.json', 'r') as filedia:
                data = json.load(filedia)
            for key, value in data.items():
                print("[del] Last diastol deleted")
                print(value[-1])
                del value[-1]
            with open('./param/aspifile4/diastol.json', 'w') as file:
                json.dump(data, file, indent=4)
            label['text'] = "Last value of 'diastol.json' has been deleted !"
            print("[del] Last 'diastol.json' has been deleted !")
    except (FileNotFoundError, IndexError) as out_dia:
        label['text'] = "Sorry, file asked not exist !"
        print('[!] Sorry, file asked not exist !', out_dia)

def delPuls():
    """
        To erase last line
        of puls.json
    """
    try:
        if os.path.getsize('./param/aspifile4/puls.json'):
            with open('./param/aspifile4/puls.json', 'r') as file:
                data = json.load(file)
            for key, value in data.items():
                print("[del] Last Puls deleted")
                print(value[-1])
                del value[-1]
            with open('./param/aspifile4/puls.json', 'w') as file:
                json.dump(data, file, indent=4)
            label['text'] = "Last value of 'puls.json' has been deleted !"
            print("[del] Last 'puls.json' has been deleted !")
    except (FileNotFoundError, IndexError) as out_puls:
        label['text'] = "Sorry, file asked not exist !"
        print('[!] Sorry, asked not exist !', out_puls)

def delSat():
    """
        To erase last line
        of sat.json
    """
    try:
        if os.path.getsize('./param/aspifile4/sat.json'):
            with open('./param/aspifile4/sat.json', 'r') as file:
                data = json.load(file)
            for key, value in data.items():
                print("[del] Last SaO2 deleted")
                print(value[-1])
                del value[-1]
            with open('./param/aspifile4/sat.json', 'w') as file:
                json.dump(data, file, indent=4)
            label['text'] = "Last value of 'sat.json' has been deleted !"
            print("[del] Last 'sat.json' has been deleted !")
    except (FileNotFoundError, IndexError) as out_sat:
        label['text'] = "Sorry, file asked not exist !"
        print('[!] Sorry, file asked not exist !', out_sat)

def delFreq():
    """
        To erase last line
        of freq.json
    """
    try:
        if os.path.getsize('./param/aspifile4/freq.json'):
            with open('./param/aspifile4/freq.json', 'r') as file:
                data = json.load(file)
            for key, value in data.items():
                print("[del] Last FR deleted")
                print(value[-1])
                del value[-1]
            with open('./param/aspifile4/freq.json', 'w') as file:
                json.dump(data, file, indent=4)
            label['text'] = "Last value of 'freq.json' has been deleted !"
            print("[del] Last 'freq.json' has been deleted !")
    except (FileNotFoundError, IndexError) as out_freq:
        label['text'] = "Sorry, file asked not exist !"
        print('[!] Sorry, file asked not exist !', out_freq)

def delTemp():
    """
        To erase last line
        of temp.json
    """
    try:
        if os.path.getsize('./param/aspifile4/temp.json'):
            with open('./param/aspifile4/temp.json', 'r') as file:
                data = json.load(file)
            for key, value in data.items():
                print("[del] Last Temp deleted")
                print(value[-1])
                del value[-1]
            with open('./param/aspifile4/temp.json', 'w') as file:
                json.dump(data, file, indent=4)
            label['text'] = "Last value of 'temp.json' has been deleted !"
            print("[del] Last 'temp.json' has been deleted !")
    except (FileNotFoundError, IndexError) as out_temp:
        label['text'] = "Sorry, file asked not exist !"
        print('[!] Sorry, file asked not exist !', out_temp)

def delGly():
    """
        To erase last line
        of gly.json
    """
    try:
        if os.path.getsize('./param/aspifile4/gly.json'):
            with open('./param/aspifile4/gly.json', 'r') as file:
                data = json.load(file)
            for key, value in data.items():
                print("[del] Last Gly deleted")
                print(value[-1])
                del value[-1]
            with open('./param/aspifile4/gly.json', 'w') as file:
                json.dump(data, file, indent=4)
            label['text'] = "Last value of 'gly.json' has been deleted !"
            print("[del] Last 'gly.json' has been deleted !")
    except (FileNotFoundError, IndexError) as out_gly:
        label['text'] = "Sorry, file asked not exist !"
        print('[!] Sorry, file asked not exist !', out_gly)

def delDlr():
    """
        To erase last line
        of dlr.json
    """
    try:
        if os.path.getsize('./param/aspifile4/dlr.json'):
            with open('./param/aspifile4/dlr.json', 'r') as file:
                data = json.load(file)
            for key, value in data.items():
                print("[del] Last Pain deleted")
                print(value[-1])
                del value[-1]
            with open('./param/aspifile4/dlr.json', 'w') as file:
                json.dump(data, file, indent=4)
            label['text'] = "Last value of 'dlr.json' has been deleted !"
            print("[del] Last 'dlr.json' has been deleted !")
    except (FileNotFoundError, IndexError) as out_dlr:
        label['text'] = "Sorry, file asked not exist !"
        print('[!] Sorry, file asked not exist !', out_dlr)

def delEvery():
    """
        To delete all json files
    """
    MsgBox = messagebox.askquestion("Confirm", "Are you sure ?\n"
        "All the last recorded values will be erased !")
    if MsgBox == 1:
        delSystolDia()
        delPuls()
        delSat()
        delFreq()
        delTemp()
        delGly()
        delDlr()
        label['text'] = "All json files have been deleted !"
        print("[del] All json files have been deleted !")
    else:
        label['text'] = "Nothing has been deleted !"
        print("[!] Nothing has been deleted !")

# To read name of patient for entry widget
with open('./newpatient/entryfile4.txt', 'r') as filename:
    line1=filename.readline()

gui = tk.Tk()
gui.title("Time-Track")
gui.configure(background='DodgerBlue2')
gui.geometry('650x600')
gui.resizable(False, False)

labelTitle = tk.Label(gui, text="Vital Parameters",
    font=('Times 22 bold'), bg='DodgerBlue2', fg='white')
labelTitle.grid(row=0, column=1, columnspan=4, pady=10)

label = tk.Label(gui, text='Date : ', font=('Times', 14),
    fg='white', bg='DodgerBlue2', width=15, anchor=tk.E)
label.grid(row=1, column=1)

label = tk.Label(gui, text='Hour : ', font=('Times', 14),
    fg='white', bg='DodgerBlue2', width=15, anchor=tk.E)
label.grid(row=2, column=1)

label1 = tk.Label(gui, text='Enter Name : ', font=('Times', 14),
    fg='white', bg='DodgerBlue2', width=15, anchor=tk.E)
label1.grid(row=3, column=1)

label2 = tk.Label(gui, text='Enter Systolic : ', font=('Times', 14),
    fg='white', bg='DodgerBlue2', width=15, anchor=tk.E)
label2.grid(sticky=tk.E, row=4, column=1)

labelDia = tk.Label(gui, text='Diastolic : ', font=('Times', 14),
    fg='white', bg='DodgerBlue2', width=10, anchor=tk.E)
labelDia.grid(row=4, column=2)

label3 = tk.Label(gui, text='Enter Puls : ', font=('Times', 14),
    fg='white', bg='DodgerBlue2', width=15, anchor=tk.E)
label3.grid(row=5, column=1)

label4 = tk.Label(gui, text='Enter SaO2 : ', font=('Times', 14),
    fg='white', bg='DodgerBlue2', width=15, anchor=tk.E)
label4.grid(row=6, column=1)

label5 = tk.Label(gui, text='Enter FR : ', font=('Times', 14),
    fg='white', bg='DodgerBlue2', width=15, anchor=tk.E)
label5.grid(row=7, column=1)

label6 = tk.Label(gui, text='Enter T°C : ', font=('Times', 14),
    fg='white', bg='DodgerBlue2', width=15, anchor=tk.E)
label6.grid(row=8, column=1)

label7 = tk.Label(gui, text='Enter Hgt : ', font=('Times', 14),
    fg='white', bg='DodgerBlue2', width=15, anchor=tk.E)
label7.grid(row=9, column=1)

label8 = tk.Label(gui, text='Eva dlrs/10 : ', font=('Times', 14),
    fg='white', bg='DodgerBlue2', width=15, anchor=tk.E)
label8.grid(row=10, column=1)

time_string = tk.IntVar()
textDate = tk.Entry(gui, textvariable=time_string,
    highlightbackground='gray', bd=4)
time_string.set(time.strftime("%d/%m/%Y"))
textDate.grid(row=1, column=2)

time_Htring = tk.IntVar()
textHour = tk.Entry(gui, textvariable=time_Htring,
    highlightbackground='gray', bd=4)
time_Htring.set(time.strftime("%H:%M:%S"))
textHour.grid(row=2, column=2)

name_text = tk.StringVar()
textName = tk.Entry(gui, textvariable=name_text,
    highlightbackground='gray', bd=4)
name_text.set(line1[:-1])
textName.grid(row=3, column=2)

textsvta = tk.StringVar()
textTa = tk.Entry(gui, textvariable=textsvta, highlightbackground='gray',
    width=4, bd=4)
textTa.grid(sticky=tk.W, row=4, column=2)

textsvdia = tk.StringVar()
textDia = tk.Entry(gui, textvariable=textsvdia, highlightbackground='gray',
    width=4, bd=4)
textDia.grid(sticky=tk.E, row=4, column=2)

textsvpuls = tk.StringVar()
textPuls = tk.Entry(gui, textvariable=textsvpuls, highlightbackground='gray', bd=4)
textPuls.grid(row=5, column=2)

textsvsa = tk.StringVar()
textSa = tk.Entry(gui, textvariable=textsvsa, highlightbackground='gray', bd=4)
textSa.grid(row=6, column=2)

textsvfr = tk.StringVar()
textFr = tk.Entry(gui, textvariable=textsvfr, highlightbackground='gray', bd=4)
textFr.grid(row=7, column=2)

textsvtemp = tk.StringVar()
textTemp = tk.Entry(gui, textvariable=textsvtemp, highlightbackground='gray', bd=4)
textTemp.grid(row=8, column=2)

textsvhgt = tk.StringVar()
textHgt = tk.Entry(gui, textvariable=textsvhgt, highlightbackground='gray', bd=4)
textHgt.grid(row=9, column=2)

textsvdlrs = tk.StringVar()
textDlrs = tk.Entry(gui, textvariable=textsvdlrs, highlightbackground='gray', bd=4)
textDlrs.grid(row=10, column=2)

button2Write = tk.Button(gui)
button2Write.config(text='Quit', width=15,
    fg='navy', bg='lightblue',
    activebackground='pale turquoise',
    activeforeground='gray40',
    command=quit)
button2Write.grid(row=1, column=3)

buttonDel = tk.Button(gui)
buttonDel.config(text='Cancel ALL LAST', width=15,
    bg='coral', fg='yellow', activebackground='red',
    activeforeground='white', command=delEvery)
buttonDel.grid(row=1, column=4)

buttonWrite = tk.Button(gui)
buttonWrite.config(text='CAPTURE DATA', width=33,
    fg='navy', bg='lightblue',
    activeforeground='gray40',
    activebackground='pale turquoise',
    command = lambda : writeData(textDate, textHour, textName, textTa, textDia, textPuls,
        textSa, textFr, textTemp, textHgt, textDlrs))
buttonWrite.grid(row=2, column=3, columnspan=4)

buttonMainlec = tk.Button(gui)
buttonMainlec.config(text='Read All Data', width=33,
    bg='lightblue', fg='navy', activebackground='pale turquoise',
    activeforeground='gray40', command=mainRead)
buttonMainlec.grid(row=3, column=3, columnspan=4)

button3Write = tk.Button(gui)
button3Write.config(text='Graph TA', width=15,
    bg='lightblue', fg='navy', activebackground='pale turquoise',
    activeforeground='gray40',
    command = lambda : appelTens(textDate, textName, textTa, textDia))
button3Write.grid(row=4, column=3)

button4Write = tk.Button(gui)
button4Write.config(text='Graph Puls', width=15,
    bg='lightblue', fg='navy', activebackground='pale turquoise',
    activeforeground='gray40', command = lambda : appelPuls(textDate, textName, textPuls))
button4Write.grid(row=5, column=3)

button5Write = tk.Button(gui)
button5Write.config(text='Graph SaO2', width=15,
    bg='lightblue', fg='navy', activebackground='pale turquoise',
    activeforeground='gray40', command = lambda : appelSat(textDate, textName, textSa))
button5Write.grid(row=6, column=3)

button6Write = tk.Button(gui)
button6Write.config(text='Graph FR', width=15,
    bg='lightblue', fg='navy', activebackground='pale turquoise',
    activeforeground='gray40', command = lambda : appelFreq(textDate, textName, textFr))
button6Write.grid(row=7, column=3)

button7Write = tk.Button(gui)
button7Write.config(text='Graph T°C', width=15,
    bg='lightblue', fg='navy',activebackground='pale turquoise',
    activeforeground='gray40', command = lambda : appelTemp(textDate, textName, textTemp))
button7Write.grid(row=8, column=3)

button8Write = tk.Button(gui)
button8Write.config(text='Graph Hgt', width=15,
    bg='lightblue', fg='navy',activebackground='pale turquoise',
    activeforeground='gray40', command = lambda : appelGly(textDate, textName, textHgt))
button8Write.grid(row=9, column=3)

button9Write = tk.Button(gui)
button9Write.config(text='Graph Dlrs', width=15,
    bg='lightblue', fg='navy',activebackground='pale turquoise',
    activeforeground='gray40', command = lambda : appelDlr(textDate, textName, textDlrs))
button9Write.grid(row=10, column=3)

button1Del = tk.Button(gui)
button1Del.config(text='Cancel last TA', width=15,
    bg='coral', fg='yellow', activeforeground='white',
    activebackground='red', command = delSystolDia)
button1Del.grid(row=4, column=4)

button2Del = tk.Button(gui)
button2Del.config(text='Cancel last Puls', width=15,
    bg='coral', fg='yellow', activeforeground='white',
    activebackground='red', command=delPuls)
button2Del.grid(row=5, column=4)

button3Del = tk.Button(gui)
button3Del.config(text='Cancel last SaO2', width=15,
    bg='coral', fg='yellow', activeforeground='white',
    activebackground='red', command=delSat)
button3Del.grid(row=6, column=4)

button4Del = tk.Button(gui)
button4Del.config(text='Cancel last FR', width=15,
    bg='coral', fg='yellow', activeforeground='white',
    activebackground='red', command=delFreq)
button4Del.grid(row=7, column=4)

button5Del = tk.Button(gui)
button5Del.config(text='Cancel last T°C', width=15,
    bg='coral', fg='yellow', activeforeground='white',
    activebackground='red', command=delTemp)
button5Del.grid(row=8, column=4)

button6Del = tk.Button(gui)
button6Del.config(text='Cancel last Hgt', width=15,
    bg='coral', fg='yellow', activeforeground='white',
    activebackground='red', command=delGly)
button6Del.grid(row=9, column=4)

button7Del = tk.Button(gui)
button7Del.config(text='Cancel last Dlrs', width=15,
    bg='coral', fg='yellow', activeforeground='white',
    activebackground='red', command=delDlr)
button7Del.grid(row=10, column=4)

lower_frame = tk.Frame(gui, bg='DodgerBlue2', bd=10, relief='groove')
lower_frame.place(relx=0.5, rely=0.66, relwidth=0.9,
    relheight=0.3, anchor=tk.N)

label = tk.Label(lower_frame, text=" ", font=('Arial', 12),
    bg='white', anchor=tk.NW, justify=tk.LEFT)
label.place(relwidth=1, relheight=1)

gui.mainloop()
