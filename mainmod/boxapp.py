#!/usr/bin/python3
# -*- coding: utf-8 -*-


import tkinter as tk
from tkinter import messagebox
import subprocess
import os
import time
import datetime
from backapp import *
#from mainmod.patcaps import callResident
from agendapp import dispAgBox
from tttapp import dispTttBox
from resapp import dispResBox


def callBox(self):
    """
        Everything that is current and to update.
        Call a reminder if date is equal to today.
    """
    self.effacer()
    self.delScroll()
    self.can.configure(background='DodgerBlue2')

    self.photo = tk.PhotoImage(file='./syno_gif/fontalarmbg2.png')
    self.item = self.can.create_image(625, 350, image=self.photo)
    # Compare date !
    self.updateFiletxt()
    dispAgBox()
    dispTttBox()
    dispResBox()
    # Display date
    self.x1, self.y1 = 1140, 40
    self.data_time = tk.StringVar()
    self.Date_write = tk.Entry(self.can, textvariable=self.data_time, 
        width=9, bd=3, highlightbackground='grey')
    self.data_time.set(time.strftime("%d/%m/%Y"))
    self.Date_write=self.can.create_window(self.x1, self.y1,
        window=self.Date_write)
    # To go to resident page
    self.x6, self.y6 = 100, 40
    self.b6 = tk.Button(self.can, width=10, font=16, bd=3, bg='RoyalBlue3', fg='white', 
        highlightbackground='cyan', activebackground='pale turquoise',
        activeforeground='white', text="Resident page", command=self.showPatients)
    self.fb6=self.can.create_window(self.x6, self.y6, window=self.b6)
    # TextBox
    self.x7, self.y7 = 625, 350
    self.tbox99 = tk.Text(self.can, height=34, width=80, font=18, relief=tk.SUNKEN)
    self.tbox99.insert(INSERT, "Previously (yesterday) : ")
    self.tbox99.insert(END, (datetime.datetime.now() + \
        datetime.timedelta(days=-1)).strftime('%d/%m/%Y'))
    self.wintbox99_window=self.can.create_window(self.x7, self.y7, window=self.tbox99)

    # Patient 1
    try:
        with open('./newpatient/entryfile.txt', 'r') as namefile:
            line1=namefile.readline()
    except FileNotFoundError as callfile:
        print("[!] File entryfile.txt doesn't exist !", callfile)

    # Display text in textbox from 14 Needs files
    try:
        datesearch = (datetime.datetime.now() - datetime.timedelta(\
            days=1)).strftime('%d/%m/%Y')
        with open('./need/doc_suivi/main_14b.txt', 'r') as filedate:
            lines = filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if datesearch in line:
                    self.tbox99.insert(END, "\n\n==> " + line1)
                    self.tbox99.insert(INSERT, line)
                    self.tbox99.insert(INSERT, lines[i+1])
                    self.tbox99.insert(INSERT, lines[i+2])
                    self.tbox99.insert(INSERT,
                        "Look at care and monitoring...")
                else:
                    pass
    except FileNotFoundError as infofileout:
        print("[Err_1] File main_14b.txt for patient 1 has not been found",
        infofileout)
    except IndexError as inforange:
        print("[Err_2] List 1 got less than 6 lines", inforange)
    else:
        print("[Err_3] Error unknow boxapp.py 1")

    # Patient 2
    try:
        with open('./newpatient/entryfile2.txt', 'r') as namefile:
            line2=namefile.readline()
    except FileNotFoundError as callfile2:
        print("[!] File entryfile2.txt doesn't exist !", callfile2)

    try:
        datesearch = (datetime.datetime.now() - datetime.timedelta(\
            days=1)).strftime('%d/%m/%Y')
        with open('./need/doc_suivi2/main_14b.txt', 'r') as filedate:
            lines = filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if datesearch in line:
                    self.tbox99.insert(END, "\n\n==> " + line2)
                    self.tbox99.insert(INSERT, line)
                    self.tbox99.insert(INSERT, lines[i+1])
                    self.tbox99.insert(INSERT, lines[i+2])
                    self.tbox99.insert(INSERT,
                        "Look at care and monitoring...")
                else:
                    pass
    except FileNotFoundError as infofileout1:
        print("[Err_1] File main_14b.txt for patient 2 has not been found",
        infofileout1)
    except IndexError as inforange2:
        print("[Err_2] List 2 got less than 6 lines", inforange2)
    else:
        print("[Err_3] Error unknow boxapp.py 2")

    # Patient 3
    try:
        with open('./newpatient/entryfile3.txt', 'r') as namefile:
            line3=namefile.readline()
    except FileNotFoundError as callfile3:
        print("[!] File entryfile3.txt doesn't exist !", callfile3)

    try:
        datesearch = (datetime.datetime.now() - datetime.timedelta(\
            days=1)).strftime('%d/%m/%Y')
        with open('./need/doc_suivi3/main_14b.txt', 'r') as filedate:
            lines = filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if datesearch in line:
                    self.tbox99.insert(END, "\n\n==> " + line3)
                    self.tbox99.insert(INSERT, line)
                    self.tbox99.insert(INSERT, lines[i+1])
                    self.tbox99.insert(INSERT, lines[i+2])
                    self.tbox99.insert(INSERT,
                        "Look at care and monitoring...")
                else:
                    pass
    except FileNotFoundError as infofileout3:
        print("[Err_1] File main_14b.txt for patient 3 has not been found",
        infofileout3)
    except IndexError as inforange3:
        print("[Err_2] List 3 got less than 6 lines", inforange3)
    else:
        print("[Err_3] Error unknow boxapp.py 3")

    # Patient 4
    try:
        with open('./newpatient/entryfile4.txt', 'r') as namefile:
            line4=namefile.readline()
    except FileNotFoundError as callfile4:
        print("[!] File entryfile4.txt doesn't exist !", callfile4)

    try:
        datesearch = (datetime.datetime.now() - datetime.timedelta(\
            days=1)).strftime('%d/%m/%Y')
        with open('./need/doc_suivi4/main_14b.txt', 'r') as filedate:
            lines = filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if datesearch in line:
                    self.tbox99.insert(END, "\n\n==> " + line4)
                    self.tbox99.insert(INSERT, line)
                    self.tbox99.insert(INSERT, lines[i+1])
                    self.tbox99.insert(INSERT, lines[i+2])
                    self.tbox99.insert(INSERT,
                        "Look at care and monitoring...")
                else:
                    pass
    except FileNotFoundError as infofileout4:
        print("[Err_1] File main_14b.txt for patient 4 has not been found",
        infofileout4)
    except IndexError as inforange4:
        print("[Err_2] List 4 got less than 6 lines", inforange4)
    else:
        print("[Err_3] Error unknow boxapp.py 4")

    # Patient 5
    try:
        with open('./newpatient/entryfile5.txt', 'r') as namefile:
            line5=namefile.readline()
    except FileNotFoundError as callfile5:
        print("[!] File entryfile5.txt doesn't exist !", callfile5)

    try:
        datesearch = (datetime.datetime.now() - datetime.timedelta(\
            days=1)).strftime('%d/%m/%Y')
        with open('./need/doc_suivi5/main_14b.txt', 'r') as filedate:
            lines = filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if datesearch in line:
                    self.tbox99.insert(END, "\n\n==> " + line5)
                    self.tbox99.insert(INSERT, line)
                    self.tbox99.insert(INSERT, lines[i+1])
                    self.tbox99.insert(INSERT, lines[i+2])
                    self.tbox99.insert(INSERT,
                        "Look at care and monitoring...")
                else:
                    pass
    except FileNotFoundError as infofileout5:
        print("[Err_1] File main_14b.txt for patient 5 has not been found",
        infofileout5)
    except IndexError as inforange5:
        print("[Err_2] List 5 got less than 6 lines", inforange5)
    else:
        print("[Err_3] Error unknow boxapp.py 5")

    # Patient 6
    try:
        with open('./newpatient/entryfile6.txt', 'r') as namefile:
            line6=namefile.readline()
    except FileNotFoundError as callfile6:
        print("[!] File entryfile6.txt doesn't exist !", callfile6)

    try:
        datesearch = (datetime.datetime.now() - datetime.timedelta(\
            days=1)).strftime('%d/%m/%Y')
        with open('./need/doc_suivi6/main_14b.txt', 'r') as filedate:
            lines = filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if datesearch in line:
                    self.tbox99.insert(END, "\n\n==> " + line6)
                    self.tbox99.insert(INSERT, line)
                    self.tbox99.insert(INSERT, lines[i+1])
                    self.tbox99.insert(INSERT, lines[i+2])
                    self.tbox99.insert(INSERT,
                        "Look at care and monitoring...")
                else:
                    pass
    except FileNotFoundError as infofileout6:
        print("[Err_1] File main_14b.txt for patient 6 has not been found",
        infofileout6)
    except IndexError as inforange6:
        print("[Err_2] List 6 got less than 6 lines", inforange6)
    else:
        print("[Err_3] Error unknow boxapp.py 6")

    # Patient 7
    try:
        with open('./newpatient/entryfile7.txt', 'r') as namefile:
            line7=namefile.readline()
    except FileNotFoundError as callfile7:
        print("[!] File entryfile7.txt doesn't exist !", callfile7)

    try:
        datesearch = (datetime.datetime.now() - datetime.timedelta(\
            days=1)).strftime('%d/%m/%Y')
        with open('./need/doc_suivi7/main_14b.txt', 'r') as filedate:
            lines = filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if datesearch in line:
                    self.tbox99.insert(END, "\n\n==> " + line7)
                    self.tbox99.insert(INSERT, line)
                    self.tbox99.insert(INSERT, lines[i+1])
                    self.tbox99.insert(INSERT, lines[i+2])
                    self.tbox99.insert(INSERT,
                        "Look at care and monitoring...")
                else:
                    pass
    except FileNotFoundError as infofileout7:
        print("[Err_1] File main_14b.txt for patient 7 has not been found",
        infofileout7)
    except IndexError as inforange7:
        print("[Err_2] List 7 got less than 6 lines", inforange7)
    else:
        print("[Err_3] Error unknow boxapp.py 7")

    # Patient 8
    try:
        with open('./newpatient/entryfile8.txt', 'r') as namefile:
            line8=namefile.readline()
    except FileNotFoundError as callfile8:
        print("[!] File entryfile8.txt doesn't exist !", callfile8)

    try:
        datesearch = (datetime.datetime.now() - datetime.timedelta(\
            days=1)).strftime('%d/%m/%Y')
        with open('./need/doc_suivi8/main_14b.txt', 'r') as filedate:
            lines = filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if datesearch in line:
                    self.tbox99.insert(END, "\n\n==> " + line8)
                    self.tbox99.insert(INSERT, line)
                    self.tbox99.insert(INSERT, lines[i+1])
                    self.tbox99.insert(INSERT, lines[i+2])
                    self.tbox99.insert(INSERT,
                        "Look at care and monitoring...")
                else:
                    pass
    except FileNotFoundError as infofileout8:
        print("[Err_1] File main_14b.txt for patient 8 has not been found",
        infofileout8)
    except IndexError as inforange8:
        print("[Err_2] List 8 got less than 6 lines", inforange8)
    else:
        print("[Err_3] Error unknow boxapp.py 8")

    # Patient 9
    try:
        with open('./newpatient/entryfile9.txt', 'r') as namefile:
            line9=namefile.readline()
    except FileNotFoundError as callfile9:
        print("[!] File entryfile9.txt doesn't exist !", callfile9)

    try:
        datesearch = (datetime.datetime.now() - datetime.timedelta(\
            days=1)).strftime('%d/%m/%Y')
        with open('./need/doc_suivi9/main_14b.txt', 'r') as filedate:
            lines = filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if datesearch in line:
                    self.tbox99.insert(END, "\n\n==> " + line9)
                    self.tbox99.insert(INSERT, line)
                    self.tbox99.insert(INSERT, lines[i+1])
                    self.tbox99.insert(INSERT, lines[i+2])
                    self.tbox99.insert(INSERT,
                        "Look at care and monitoring...")
                else:
                    pass
    except FileNotFoundError as infofileout9:
        print("[Err_1] File main_14b.txt for patient 9 has not been found",
        infofileout9)
    except IndexError as inforange9:
        print("[Err_2] List 9 got less than 6 lines", inforange9)
    else:
        print("[Err_3] Error unknow boxapp.py 9")

    # Patient 10
    try:
        with open('./newpatient/entryfile10.txt', 'r') as namefile:
            line10=namefile.readline()
    except FileNotFoundError as callfile10:
        print("[!] File entryfile10.txt doesn't exist !", callfile10)

    try:
        datesearch = (datetime.datetime.now() - datetime.timedelta(\
            days=1)).strftime('%d/%m/%Y')
        with open('./need/doc_suivi10/main_14b.txt', 'r') as filedate:
            lines = filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if datesearch in line:
                    self.tbox99.insert(END, "\n\n==> " + line10)
                    self.tbox99.insert(INSERT, line)
                    self.tbox99.insert(INSERT, lines[i+1])
                    self.tbox99.insert(INSERT, lines[i+2])
                    self.tbox99.insert(INSERT,
                        "Look at care and monitoring...")
                else:
                    pass
    except FileNotFoundError as infofileout10:
        print("[Err_1] File main_14b.txt for patient 10 has not been found",
        infofileout10)
    except IndexError as inforange10:
        print("[Err_2] List 10 got less than 6 lines", inforange10)
    else:
        print("[Err_3] Error unknow boxapp.py 10")

    # Patient 11
    try:
        with open('./newpatient/entryfile11.txt', 'r') as namefile:
            line11=namefile.readline()
    except FileNotFoundError as callfile11:
        print("[!] File entryfile11.txt doesn't exist !", callfile11)

    try:
        datesearch = (datetime.datetime.now() - datetime.timedelta(\
            days=1)).strftime('%d/%m/%Y')
        with open('./need/doc_suivi11/main_14b.txt', 'r') as filedate:
            lines = filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if datesearch in line:
                    self.tbox99.insert(END, "\n\n==> " + line11)
                    self.tbox99.insert(INSERT, line)
                    self.tbox99.insert(INSERT, lines[i+1])
                    self.tbox99.insert(INSERT, lines[i+2])
                    self.tbox99.insert(INSERT,
                        "Look at care and monitoring...")
                else:
                    pass
    except FileNotFoundError as infofileout11:
        print("[Err_1] File main_14b.txt for patient 11 has not been found",
        infofileout11)
    except IndexError as inforange11:
        print("[Err_2] List 11 got less than 6 lines", inforange11)
    else:
        print("[Err_3] Error unknow boxapp.py 11")

    # Patient 12
    try:
        with open('./newpatient/entryfile12.txt', 'r') as namefile:
            line12=namefile.readline()
    except FileNotFoundError as callfile12:
        print("[!] File entryfile12.txt doesn't exist !", callfile12)

    try:
        datesearch = (datetime.datetime.now() - datetime.timedelta(\
            days=1)).strftime('%d/%m/%Y')
        with open('./need/doc_suivi12/main_14b.txt', 'r') as filedate:
            lines = filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if datesearch in line:
                    self.tbox99.insert(END, "\n\n==> " + line12)
                    self.tbox99.insert(INSERT, line)
                    self.tbox99.insert(INSERT, lines[i+1])
                    self.tbox99.insert(INSERT, lines[i+2])
                    self.tbox99.insert(INSERT,
                        "Look at care and monitoring...")
                else:
                    pass
    except FileNotFoundError as infofileout12:
        print("[Err_1] File main_14b.txt for patient 12 has not been found",
        infofileout12)
    except IndexError as inforange12:
        print("[Err_2] List 12 got less than 6 lines", inforange12)
    else:
        print("[Err_3] Error unknow boxapp.py 12")

    # Patient 13
    try:
        with open('./newpatient/entryfile13.txt', 'r') as namefile:
            line13=namefile.readline()
    except FileNotFoundError as callfile13:
        print("[!] File entryfile13.txt doesn't exist !", callfile13)

    try:
        datesearch = (datetime.datetime.now() - datetime.timedelta(\
            days=1)).strftime('%d/%m/%Y')
        with open('./need/doc_suivi13/main_14b.txt', 'r') as filedate:
            lines = filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if datesearch in line:
                    self.tbox99.insert(END, "\n\n==> " + line13)
                    self.tbox99.insert(INSERT, line)
                    self.tbox99.insert(INSERT, lines[i+1])
                    self.tbox99.insert(INSERT, lines[i+2])
                    self.tbox99.insert(INSERT,
                        "Look at care and monitoring...")
                else:
                    pass
    except FileNotFoundError as infofileout13:
        print("[Err_1] File main_14b.txt for patient 13 has not been found",
        infofileout13)
    except IndexError as inforange13:
        print("[Err_2] List 13 got less than 6 lines", inforange13)
    else:
        print("[Err_3] Error unknow boxapp.py 13")

    # Patient 14
    try:
        with open('./newpatient/entryfile14.txt', 'r') as namefile:
            line14=namefile.readline()
    except FileNotFoundError as callfile14:
        print("[!] File entryfile14.txt doesn't exist !", callfile14)

    try:
        datesearch = (datetime.datetime.now() - datetime.timedelta(\
            days=1)).strftime('%d/%m/%Y')
        with open('./need/doc_suivi14/main_14b.txt', 'r') as filedate:
            lines = filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if datesearch in line:
                    self.tbox99.insert(END, "\n\n==> " + line14)
                    self.tbox99.insert(INSERT, line)
                    self.tbox99.insert(INSERT, lines[i+1])
                    self.tbox99.insert(INSERT, lines[i+2])
                    self.tbox99.insert(INSERT,
                        "Look at care and monitoring...")
                else:
                    pass
    except FileNotFoundError as infofileout14:
        print("[Err_1] File main_14b.txt for patient 14 has not been found",
        infofileout14)
    except IndexError as inforange14:
        print("[Err_2] List 14 got less than 6 lines", inforange14)
    else:
        print("[Err_3] Error unknow boxapp.py 14")

    # Patient 15
    try:
        with open('./newpatient/entryfile15.txt', 'r') as namefile:
            line15=namefile.readline()
    except FileNotFoundError as callfile15:
        print("[!] File entryfile15.txt doesn't exist !", callfile15)

    try:
        datesearch = (datetime.datetime.now() - datetime.timedelta(\
            days=1)).strftime('%d/%m/%Y')
        with open('./need/doc_suivi15/main_14b.txt', 'r') as filedate:
            lines = filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if datesearch in line:
                    self.tbox99.insert(END, "\n\n==> " + line15)
                    self.tbox99.insert(INSERT, line)
                    self.tbox99.insert(INSERT, lines[i+1])
                    self.tbox99.insert(INSERT, lines[i+2])
                    self.tbox99.insert(INSERT,
                        "Look at care and monitoring...")
                else:
                    pass
    except FileNotFoundError as infofileout15:
        print("[Err_1] File main_14b.txt for patient 15 has not been found",
        infofileout15)
    except IndexError as inforange15:
        print("[Err_2] List 15 got less than 6 lines", inforange15)
    else:
        print("[Err_3] Error unknow boxapp.py 15")

    # Patient 16
    try:
        with open('./newpatient/entryfile16.txt', 'r') as namefile:
            line16=namefile.readline()
    except FileNotFoundError as callfile16:
        print("[!] File entryfile16.txt doesn't exist !", callfile16)

    try:
        datesearch = (datetime.datetime.now() - datetime.timedelta(\
            days=1)).strftime('%d/%m/%Y')
        with open('./need/doc_suivi16/main_14b.txt', 'r') as filedate:
            lines = filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if datesearch in line:
                    self.tbox99.insert(END, "\n\n==> " + line16)
                    self.tbox99.insert(INSERT, line)
                    self.tbox99.insert(INSERT, lines[i+1])
                    self.tbox99.insert(INSERT, lines[i+2])
                    self.tbox99.insert(INSERT,
                        "Look at care and monitoring...")
                else:
                    pass
    except FileNotFoundError as infofileout16:
        print("[Err_1] File main_14b.txt for patient 16 has not been found",
        infofileout16)
    except IndexError as inforange16:
        print("[Err_2] List 16 got less than 6 lines", inforange16)
    else:
        print("[Err_3] Error unknow boxapp.py 16")

    # Patient 17
    try:
        with open('./newpatient/entryfile17.txt', 'r') as namefile:
            line17=namefile.readline()
    except FileNotFoundError as callfile17:
        print("[!] File entryfile17.txt doesn't exist !", callfile17)

    try:
        datesearch = (datetime.datetime.now() - datetime.timedelta(\
            days=1)).strftime('%d/%m/%Y')
        with open('./need/doc_suivi17/main_14b.txt', 'r') as filedate:
            lines = filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if datesearch in line:
                    self.tbox99.insert(END, "\n\n==> " + line17)
                    self.tbox99.insert(INSERT, line)
                    self.tbox99.insert(INSERT, lines[i+1])
                    self.tbox99.insert(INSERT, lines[i+2])
                    self.tbox99.insert(INSERT,
                        "Look at care and monitoring...")
                else:
                    pass
    except FileNotFoundError as infofileout17:
        print("[Err_1] File main_14b.txt for patient 17 has not been found",
        infofileout17)
    except IndexError as inforange17:
        print("[Err_2] List 17 got less than 6 lines", inforange17)
    else:
        print("[Err_3] Error unknow boxapp.py 17")

    # Patient 18
    try:
        with open('./newpatient/entryfile18.txt', 'r') as namefile:
            line18=namefile.readline()
    except FileNotFoundError as callfile18:
        print("[!] File entryfile18.txt doesn't exist !", callfile18)

    try:
        datesearch = (datetime.datetime.now() - datetime.timedelta(\
            days=1)).strftime('%d/%m/%Y')
        with open('./need/doc_suivi18/main_14b.txt', 'r') as filedate:
            lines = filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if datesearch in line:
                    self.tbox99.insert(END, "\n\n==> " + line18)
                    self.tbox99.insert(INSERT, line)
                    self.tbox99.insert(INSERT, lines[i+1])
                    self.tbox99.insert(INSERT, lines[i+2])
                    self.tbox99.insert(INSERT,
                        "Look at care and monitoring...")
                else:
                    pass
    except FileNotFoundError as infofileout18:
        print("[Err_1] File main_14b.txt for patient 18 has not been found",
        infofileout18)
    except IndexError as inforange18:
        print("[Err_2] List 18 got less than 6 lines", inforange18)
    else:
        print("[Err_3] Error unknow boxapp.py 18")

    # Patient 19
    try:
        with open('./newpatient/entryfile19.txt', 'r') as namefile:
            line19=namefile.readline()
    except FileNotFoundError as callfile19:
        print("[!] File entryfile19.txt doesn't exist !", callfile19)

    try:
        datesearch = (datetime.datetime.now() - datetime.timedelta(\
            days=1)).strftime('%d/%m/%Y')
        with open('./need/doc_suivi19/main_14b.txt', 'r') as filedate:
            lines = filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if datesearch in line:
                    self.tbox99.insert(END, "\n\n==> " + line19)
                    self.tbox99.insert(INSERT, line)
                    self.tbox99.insert(INSERT, lines[i+1])
                    self.tbox99.insert(INSERT, lines[i+2])
                    self.tbox99.insert(INSERT,
                        "Look at care and monitoring...")
                else:
                    pass
    except FileNotFoundError as infofileout19:
        print("[Err_1] File main_14b.txt for patient 19 has not been found",
        infofileout19)
    except IndexError as inforange19:
        print("[Err_2] List 19 got less than 6 lines", inforange19)
    else:
        print("[Err_3] Error unknow boxapp.py 19")

    # Patient 20
    try:
        with open('./newpatient/entryfile20.txt', 'r') as namefile:
            line20=namefile.readline()
    except FileNotFoundError as callfile20:
        print("[!] File entryfile20.txt doesn't exist !", callfile20)

    try:
        datesearch = (datetime.datetime.now() - datetime.timedelta(\
            days=1)).strftime('%d/%m/%Y')
        with open('./need/doc_suivi20/main_14b.txt', 'r') as filedate:
            lines = filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if datesearch in line:
                    self.tbox99.insert(END, "\n\n==> " + line20)
                    self.tbox99.insert(INSERT, line)
                    self.tbox99.insert(INSERT, lines[i+1])
                    self.tbox99.insert(INSERT, lines[i+2])
                    self.tbox99.insert(INSERT,
                        "Look at care and monitoring...")
                else:
                    pass
    except FileNotFoundError as infofileout20:
        print("[Err_1] File main_14b.txt for patient 20 has not been found",
        infofileout20)
    except IndexError as inforange20:
        print("[Err_2] List 20 got less than 6 lines", inforange20)
    else:
        print("[Err_3] Error unknow boxapp.py 20")

    # Patient 21
    try:
        with open('./newpatient/entryfile21.txt', 'r') as namefile:
            line21=namefile.readline()
    except FileNotFoundError as callfile21:
        print("[!] File entryfile21.txt doesn't exist !", callfile21)

    try:
        datesearch = (datetime.datetime.now() - datetime.timedelta(\
            days=1)).strftime('%d/%m/%Y')
        with open('./need/doc_suivi21/main_14b.txt', 'r') as filedate:
            lines = filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if datesearch in line:
                    self.tbox99.insert(END, "\n\n==> " + line21)
                    self.tbox99.insert(INSERT, line)
                    self.tbox99.insert(INSERT, lines[i+1])
                    self.tbox99.insert(INSERT, lines[i+2])
                    self.tbox99.insert(INSERT,
                        "Look at care and monitoring...")
                else:
                    pass
    except FileNotFoundError as infofileout21:
        print("[Err_1] File main_14b.txt for patient 21 has not been found",
        infofileout21)
    except IndexError as inforange21:
        print("[Err_2] List 21 got less than 6 lines", inforange21)
    else:
        print("[Err_3] Error unknow boxapp.py 21")

    # Patient 22
    try:
        with open('./newpatient/entryfile22.txt', 'r') as namefile:
            line22=namefile.readline()
    except FileNotFoundError as callfile22:
        print("[!] File entryfile22.txt doesn't exist !", callfile22)

    try:
        datesearch = (datetime.datetime.now() - datetime.timedelta(\
            days=1)).strftime('%d/%m/%Y')
        with open('./need/doc_suivi22/main_14b.txt', 'r') as filedate:
            lines = filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if datesearch in line:
                    self.tbox99.insert(END, "\n\n==> " + line22)
                    self.tbox99.insert(INSERT, line)
                    self.tbox99.insert(INSERT, lines[i+1])
                    self.tbox99.insert(INSERT, lines[i+2])
                    self.tbox99.insert(INSERT,
                        "Look at care and monitoring...")
                else:
                    pass
    except FileNotFoundError as infofileout22:
        print("[Err_1] File main_14b.txt for patient 22 has not been found",
        infofileout22)
    except IndexError as inforange22:
        print("[Err_2] List 22 got less than 6 lines", inforange22)
    else:
        print("[Err_3] Error unknow boxapp.py 22")

    # Patient 23
    try:
        with open('./newpatient/entryfile23.txt', 'r') as namefile:
            line23=namefile.readline()
    except FileNotFoundError as callfile23:
        print("[!] File entryfile23.txt doesn't exist !", callfile23)

    try:
        datesearch = (datetime.datetime.now() - datetime.timedelta(\
            days=1)).strftime('%d/%m/%Y')
        with open('./need/doc_suivi23/main_14b.txt', 'r') as filedate:
            lines = filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if datesearch in line:
                    self.tbox99.insert(END, "\n\n==> " + line23)
                    self.tbox99.insert(INSERT, line)
                    self.tbox99.insert(INSERT, lines[i+1])
                    self.tbox99.insert(INSERT, lines[i+2])
                    self.tbox99.insert(INSERT,
                        "Look at care and monitoring...")
                else:
                    pass
    except FileNotFoundError as infofileout23:
        print("[Err_1] File main_14b.txt for patient 23 has not been found",
        infofileout23)
    except IndexError as inforange23:
        print("[Err_2] List 23 got less than 6 lines", inforange23)
    else:
        print("[Err_3] Error unknow boxapp.py 23")

    # Patient 24
    try:
        with open('./newpatient/entryfile24.txt', 'r') as namefile:
            line24=namefile.readline()
    except FileNotFoundError as callfile24:
        print("[!] File entryfile24.txt doesn't exist !", callfile24)

    try:
        datesearch = (datetime.datetime.now() - datetime.timedelta(\
            days=1)).strftime('%d/%m/%Y')
        with open('./need/doc_suivi24/main_14b.txt', 'r') as filedate:
            lines = filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if datesearch in line:
                    self.tbox99.insert(END, "\n\n==> " + line24)
                    self.tbox99.insert(INSERT, line)
                    self.tbox99.insert(INSERT, lines[i+1])
                    self.tbox99.insert(INSERT, lines[i+2])
                    self.tbox99.insert(INSERT,
                        "Look at care and monitoring...")
                else:
                    pass
    except FileNotFoundError as infofileout24:
        print("[Err_1] File main_14b.txt for patient 24 has not been found",
        infofileout24)
    except IndexError as inforange24:
        print("[Err_2] List 24 got less than 6 lines", inforange24)
    else:
        print("[Err_3] Error unknow boxapp.py 24")
        
    self.can.configure(scrollregion=self.can.bbox(tk.ALL))
    self.can.unbind_all("<Button-4>")
    self.can.unbind_all("<Button-5>")
