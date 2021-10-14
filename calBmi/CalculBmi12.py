#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
    To calculate BMI if indice
    is too high or too low.
    The weight is recording too.
    It's possible to read results
    in txt file.
"""


import tkinter as tk
from functools import partial
from tkinter import messagebox
import time
import os
import subprocess
import json
from bmi_download.progresstask12 import downloadata
from bmi_upload.uploadbar import uploadmain
from bmi_upload.upload12 import uploadata


def tocallprogressbar():
    """
        To display progress bar with current download
    """
    downloadata()
tocallprogressbar()

gui = tk.Tk()
gui.title('Time-Track')
gui.configure(background='DodgerBlue2')
gui.resizable(False, False)

labelTitle = tk.Label(gui, text="BMI calculator", font=('Times', 18, 'bold'),
    fg='white', bg='DodgerBlue2')
labelTitle.grid(row=0, column=1, columnspan=2, pady=10)

textDate = tk.Label(gui, text="Date : ",
    font=18, width=20, fg='white', bg='DodgerBlue2', anchor=tk.E)
textDate.grid(row=1, column=1)

textHour = tk.Label(gui, text="Hour : ",
    font=18, width=20, fg='white', bg='DodgerBlue2', anchor=tk.E)
textHour.grid(row=2, column=1)

textName = tk.Label(gui, text="Patient Name : ",
    font=18, width=20, fg='white', bg='DodgerBlue2', anchor=tk.E)
textName.grid(row=3, column=1)

labelNum1 = tk.Label(gui, text="Enter Weight (Kg) : ",
    font=14, width=20, fg='white', bg='DodgerBlue2', anchor=tk.E)
labelNum1.grid(row=4, column=1)

labelNum2 = tk.Label(gui, text="Enter Height (M) : ",
    font=14, width=20, fg='white', bg='DodgerBlue2', anchor=tk.E)
labelNum2.grid(row=5, column=1)

def call_result(textBox, number1, number2):
    number1 = entryNum1.get()
    number2 = entryNum2.get()
    try:
        textBox.delete("0.0", tk.END)
        num1 = float(entryNum1.get())
        num2 = float(entryNum2.get())
        result = (num1)/(num2*num2)
        if result < 18.5:
            textBox.insert(tk.INSERT, "!!! Underweight !!!\n"
                "Your BMI (IMC) is : %s" % round(result, 3))
            return
        elif result >= 18.5 and result <= 24.9:
            textBox.insert(tk.INSERT, "BMI is in the standards.\n"
                "BMI (IMC) is : %s" % round(result, 3))
            return
        elif result >= 25 and result <= 29.9:
            textBox.insert(tk.INSERT, "! Overweight !\n"
                "BMI (IMC) is : %s" % round(result, 3))
            return
        else:
            textBox.insert(tk.INSERT, "!!! Obesity !!!\n"
                "BMI (IMC) is : %s" % round(result, 3))
            return
    except ValueError as val_err:
        print("[!] An error has occured !", val_err)
        tk.messagebox.showwarning("Warning", "Please, enter a valid number !")

def uploadfunc():
    uploadata()

def buttRecord():
    """
        To enter BMI in an text zone entry
    """
    num1 = float((entryNum1.get()))
    num2 = float((entryNum2.get()))
    result = (num1)/(num2*num2)
    bypass = round(result, 3)

    with open('./calBmi/bmi12.txt', 'a+') as file:
        file.write(str("Date : "))
        file.write(textDate.get() + "\n")
        file.write(str("Heure : "))
        file.write(textHour.get() + "\n")
        file.write(str("Prenom et Nom : "))
        file.write(textName.get() + "\n")
        file.write(str("Poids : "))
        file.write(entryNum1.get() + "\n")
        file.write(str("Taille : "))
        file.write(entryNum2.get() + "\n")
        file.write(str("BMI : "))
        file.write(str(bypass))
        file.write("\n\n")
        file.close()

    try:
        if os.path.getsize('./calBmi/doc_BMI12/file_bmi.json'):
            print("[+] File 'BMI' exist !")
            with open('./calBmi/doc_BMI12/file_bmi.json', 'r') as datafile:
                datastore = json.load(datafile)
                print(datastore)
            dataBmi = datastore
            dataBmi['data'].append({'Date' : textDate.get(), 'BMI' : bypass})
            with open('./calBmi/doc_BMI12/file_bmi.json', 'w') as datafile2:
                json.dump(dataBmi, datafile2, indent=4)
    except FileNotFoundError as outcom:
        print('[!] Sorry, file file_bmi.json not exist !')
        print(str(outcom))
        print("[+] File file_bmi.json created !")
        dataBmi = {}
        dataBmi['data'] = []
        dataBmi['data'].append({'Date' : textDate.get(), 'BMI' : bypass})
        with open('./calBmi/doc_BMI12/file_bmi.json', 'w') as datafile:
            json.dump(dataBmi, datafile, indent=4)

    try:
        if os.path.getsize('./calBmi/doc_BMI12/file_kg.json'):
            print("[+] File 'Kg' exist !")
            with open('./calBmi/doc_BMI12/file_kg.json', 'r') as datafile:
                datastore = json.load(datafile)
                print(datastore)
            dataBmi = datastore
            dataBmi['data'].append({'Date' : textDate.get(), 'Kg' : entryNum1.get()})
            with open('./calBmi/doc_BMI12/file_kg.json', 'w') as datafile2:
                json.dump(dataBmi, datafile2, indent=4)
    except FileNotFoundError as outcom:
        print('[!] Sorry, file file_kg.json not exist !')
        print(str(outcom))
        print("[+] File file_kg.json created !")
        dataBmi = {}
        dataBmi['data'] = []
        dataBmi['data'].append({'Date' : textDate.get(), 'Kg' : entryNum1.get()})
        with open('./calBmi/doc_BMI12/file_kg.json', 'w') as datafile:
            json.dump(dataBmi, datafile, indent=4)

    tk.messagebox.showinfo('Record', 'Data saved !')
    uploadfunc()

def viewGraphicBmi():
    try:
        if os.path.getsize('./calBmi/doc_BMI12/file_bmi.json'):
            subprocess.run('./calBmi/doc_BMI12/convert_bmilist.py', check=True)
    except FileNotFoundError as no_file:
        print("[!] No BMI file exist !", no_file)
        tk.messagebox.showinfo('INFO', 'BMI file not found !')

def viewGraphicKilo():
    try:
        if os.path.getsize('./calBmi/doc_BMI12/file_kg.json'):
            subprocess.run('./calBmi/doc_BMI12/convert_kg.py', check=True)
    except FileNotFoundError as no_file:
        print("[!] No kg file exist !", no_file)
        tk.messagebox.showinfo('INFO', 'Kg file not found !')

def readBmi():
    subprocess.run('./calBmi/bmi_read12.py', check=True)

def buttdel():
    """
        To earase last data if the usr would to delete it.
    """
    tk.messagebox.showwarning("Warning", "Are you sure to delete last record !")
    MSB_War = tk.messagebox.askyesno('Warning', '!!! Warning !!! If you' \
        'continue, last result will be delete !!!')
    if MSB_War == 1:
        try:
            if os.path.getsize('./calBmi/doc_BMI12/file_bmi.json'):
                with open('./calBmi/doc_BMI12/file_bmi.json', 'r') as file:
                    data = json.load(file)
                for key, value in data.items():
                    print("[del] Last value of bmi deleted")
                    print(value[-1])
                    del value[-1]
                with open('./calBmi/doc_BMI12/file_bmi.json', 'w') as file:
                    data = json.dump(data, file, indent=4)
                print("[del] Last value of 'file_bmi.json' has been deleted !")
        except FileNotFoundError:
            print('[!] Sorry, file asked not exist !')

        try:
            if os.path.getsize('./calBmi/doc_BMI12/file_kg.json'):
                with open('./calBmi/doc_BMI12/file_kg.json', 'r') as file:
                    data = json.load(file)
                for key, value in data.items():
                    print("[del] Last value of weight deleted")
                    print(value[-1])
                    del value[-1]
                with open('./calBmi/doc_BMI12/file_kg.json', 'w') as file:
                    data = json.dump(data, file, indent=4)
                print("[del] Last value of 'file_kg.json' has been deleted !")
        except FileNotFoundError:
            print('[!] Sorry, file asked not exist !')
    else:
        tk.messagebox.showinfo('Info', 'Ok, no data was deleted.')

time_string = tk.IntVar()
textDate = tk.Entry(gui, textvariable=time_string,
    highlightbackground='gray', bd=4)
time_string.set(time.strftime("%d-%m-%Y"))
textDate.grid(row=1, column=2, padx=10)

time_Htring = tk.IntVar()
textHour = tk.Entry(gui, textvariable=time_Htring,
    highlightbackground='gray', bd=4)
time_Htring.set(time.strftime("%H:%M:%S"))
textHour.grid(row=2, column=2, padx=10)

# To read name of patient for entry widget
with open('./newpatient/entryfile12.txt', 'r') as filename:
    line1=filename.readline()

name_text = tk.StringVar()
textName = tk.Entry(gui, textvariable=name_text,
    highlightbackground='gray', bd=4)
name_text.set(line1[:-1])
textName.grid(row=3, column=2, padx=10)

number1 = tk.StringVar()
entryNum1 = tk.Entry(gui, textvariable=number1,
    width=6, bd=3, highlightbackground='gray')
number1.set('ex : 75')
entryNum1.grid(sticky=tk.W, row=4, column=2, padx=10)

number2 = tk.StringVar()
entryNum2 = tk.Entry(gui, textvariable=number2,
    width=6, bd=3, highlightbackground='gray')
number2.set('1.00')
entryNum2.grid(sticky=tk.W, row=5, column=2, padx=10)

textBox = tk.Text(gui, height=2, width=25, font=12, relief=tk.SUNKEN)
textBox.grid(row=6, column=1, columnspan=2, padx=10, pady=10)

call_result = partial(call_result, textBox, number1, number2)

buttonCal = tk.Button(gui, text="Calculate", width=30, bd=3,
    fg='white', bg='RoyalBlue3', activeforeground='gray40',
    activebackground='pale turquoise', highlightbackground='cyan',
    command=call_result)
buttonCal.grid(row=7, column=1, columnspan=2, padx=10)

buttonSave = tk.Button(gui, text="Save", width=12, bd=3, 
    fg='yellow', bg='RoyalBlue3', activeforeground='gray40',
    activebackground='pale turquoise', highlightbackground='light sky blue',
    command=buttRecord)
buttonSave.grid(sticky=tk.W, row=10, column=1, padx=10, pady=10)

buttonCancel = tk.Button(gui, text="Cancel last check", width=12,
    bd=3, fg='coral', bg='RoyalBlue3', activeforeground='white',
    activebackground='red', highlightbackground='light sky blue',
    command=buttdel)
buttonCancel.grid(sticky=tk.W, row=11, column=1, padx=10)

buttonRead = tk.Button(gui, text="Read", width=12, bd=3,
    fg='cyan', bg='RoyalBlue3',
    activebackground='pale turquoise',
    highlightbackground='light sky blue', command=readBmi)
buttonRead.grid(sticky=tk.W, row=12, column=1, padx=10, pady=10)

buttonBmi = tk.Button(gui, text="Graph BMI", width=12, bd=3,
    fg='cyan', bg='RoyalBlue3', activeforeground='gray40',
    activebackground='pale turquoise', highlightbackground='light sky blue',
    command=viewGraphicBmi)
buttonBmi.grid(sticky=tk.E, row=10, column=2, padx=10, pady=10)

buttonWeight = tk.Button(gui, text="Graph Weight", width=12, bd=3,
    fg='cyan', bg='RoyalBlue3', activeforeground='gray40',
    activebackground='pale turquoise', highlightbackground='light sky blue',
    command=viewGraphicKilo)
buttonWeight.grid(sticky=tk.E, row=11, column=2, padx=10)

buttonQuit = tk.Button(gui, text="Quit", width=12, bd=3,
    fg='white', bg='RoyalBlue3', activebackground='pale turquoise',
    highlightbackground='light sky blue', command=quit)
buttonQuit.grid(sticky=tk.E, row=12, column=2, padx=10, pady=10)

gui.mainloop()
