#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
    Main script to start.
    It call directly passw.py to validate access
    privileges.
"""


import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import scrolledtext

import os
import sys
import platform
import time
import json
from playsound import playsound

#import intro

from boxapp import callBox
from cpfoldtrans import loaderfile

from reminder import alarmThread
from manualapp import instalpy
from patcaps import callResident

from backapp import *
from Backup.backupfile import dataBackToSave

from need.needownload.refdlneed import *
from param.backup_month import paramBackToSave
from calBmi.bmi_backup import bmiBackToSave
from vmed.medload import *

from contact.conpact.pat_contact1 import Window
from contact.conpact.doc_contact1 import doctorWind
from contact.conpact.family_contact1 import famWind
from contact.conpact.hcs_contact1 import homecsWind
from contact.conpact2.pat_contact2 import Window2
from contact.conpact2.doc_contact2 import doctorWind2
from contact.conpact2.family_contact2 import famWind2
from contact.conpact2.hcs_contact2 import homecsWind2
from contact.conpact3.pat_contact3 import Window3
from contact.conpact3.doc_contact3 import doctorWind3
from contact.conpact3.family_contact3 import famWind3
from contact.conpact3.hcs_contact3 import homecsWind3
from contact.conpact4.pat_contact4 import Window4
from contact.conpact4.doc_contact4 import doctorWind4
from contact.conpact4.family_contact4 import famWind4
from contact.conpact4.hcs_contact4 import homecsWind4
from contact.conpact5.pat_contact5 import Window5
from contact.conpact5.doc_contact5 import doctorWind5
from contact.conpact5.family_contact5 import famWind5
from contact.conpact5.hcs_contact5 import homecsWind5
from contact.conpact6.pat_contact6 import Window6
from contact.conpact6.doc_contact6 import doctorWind6
from contact.conpact6.family_contact6 import famWind6
from contact.conpact6.hcs_contact6 import homecsWind6
from contact.conpact7.pat_contact7 import Window7
from contact.conpact7.doc_contact7 import doctorWind7
from contact.conpact7.family_contact7 import famWind7
from contact.conpact7.hcs_contact7 import homecsWind7
from contact.conpact8.pat_contact8 import Window8
from contact.conpact8.doc_contact8 import doctorWind8
from contact.conpact8.family_contact8 import famWind8
from contact.conpact8.hcs_contact8 import homecsWind8
from contact.conpact9.pat_contact9 import Window9
from contact.conpact9.doc_contact9 import doctorWind9
from contact.conpact9.family_contact9 import famWind9
from contact.conpact9.hcs_contact9 import homecsWind9
from contact.conpact10.pat_contact10 import Window10
from contact.conpact10.doc_contact10 import doctorWind10
from contact.conpact10.family_contact10 import famWind10
from contact.conpact10.hcs_contact10 import homecsWind10
from contact.conpact11.pat_contact11 import Window11
from contact.conpact11.doc_contact11 import doctorWind11
from contact.conpact11.family_contact11 import famWind11
from contact.conpact11.hcs_contact11 import homecsWind11
from contact.conpact12.pat_contact12 import Window12
from contact.conpact12.doc_contact12 import doctorWind12
from contact.conpact12.family_contact12 import famWind12
from contact.conpact12.hcs_contact12 import homecsWind12
from contact.conpact13.pat_contact13 import Window13
from contact.conpact13.doc_contact13 import doctorWind13
from contact.conpact13.family_contact13 import famWind13
from contact.conpact13.hcs_contact13 import homecsWind13
from contact.conpact14.pat_contact14 import Window14
from contact.conpact14.doc_contact14 import doctorWind14
from contact.conpact14.family_contact14 import famWind14
from contact.conpact14.hcs_contact14 import homecsWind14
from contact.conpact15.pat_contact15 import Window15
from contact.conpact15.doc_contact15 import doctorWind15
from contact.conpact15.family_contact15 import famWind15
from contact.conpact15.hcs_contact15 import homecsWind15
from contact.conpact16.pat_contact16 import Window16
from contact.conpact16.doc_contact16 import doctorWind16
from contact.conpact16.family_contact16 import famWind16
from contact.conpact16.hcs_contact16 import homecsWind16
from contact.conpact17.pat_contact17 import Window17
from contact.conpact17.doc_contact17 import doctorWind17
from contact.conpact17.family_contact17 import famWind17
from contact.conpact17.hcs_contact17 import homecsWind17
from contact.conpact18.pat_contact18 import Window18
from contact.conpact18.doc_contact18 import doctorWind18
from contact.conpact18.family_contact18 import famWind18
from contact.conpact18.hcs_contact18 import homecsWind18
from contact.conpact19.pat_contact19 import Window19
from contact.conpact19.doc_contact19 import doctorWind19
from contact.conpact19.family_contact19 import famWind19
from contact.conpact19.hcs_contact19 import homecsWind19
from contact.conpact20.pat_contact20 import Window20
from contact.conpact20.doc_contact20 import doctorWind20
from contact.conpact20.family_contact20 import famWind20
from contact.conpact20.hcs_contact20 import homecsWind20
from contact.conpact21.pat_contact21 import Window21
from contact.conpact21.doc_contact21 import doctorWind21
from contact.conpact21.family_contact21 import famWind21
from contact.conpact21.hcs_contact21 import homecsWind21
from contact.conpact22.pat_contact22 import Window22
from contact.conpact22.doc_contact22 import doctorWind22
from contact.conpact22.family_contact22 import famWind22
from contact.conpact22.hcs_contact22 import homecsWind22
from contact.conpact23.pat_contact23 import Window23
from contact.conpact23.doc_contact23 import doctorWind23
from contact.conpact23.family_contact23 import famWind23
from contact.conpact23.hcs_contact23 import homecsWind23
from contact.conpact24.pat_contact24 import Window24
from contact.conpact24.doc_contact24 import doctorWind24
from contact.conpact24.family_contact24 import famWind24
from contact.conpact24.hcs_contact24 import homecsWind24


def tocopyfiles():
    """
        Load 24 folders when app start.
    """
    loaderfile()
tocopyfiles()

class ScrollCanvas(tk.Frame):
    """
        To prepare ScrollBar for main application.
    """
    def __init__(self, boss=None):
        tk.Frame.__init__(self, borderwidth=borderwidth, relief=relief)

        self.can = tk.Canvas(self, width=width, height=height, bd=bd,
            bg=bg, relief=relief)
        self.viewPort = tk.Frame(self.can)
        self.vsb = tk.Scrollbar(self, orient=tk.VERTICAL, command=self.can.yview)
        self.can.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(side=tk.RIGHT, fill=tk.Y)
        self.can.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        self.canvas_window=self.can.create_window((4,4), window=self.viewPort,
            anchor=tk.NW, tags="self.viewPort")

        self.viewPort.bind("<Configure>", self.onFrameConfigure)
        self.can.bind("<Configure>", self.onCanvasConfigure)
        self.viewPort.bind('<Enter>', self.onEnter)
        self.viewPort.bind('<Leave>', self.onLeave)

class MenuBar(tk.Frame):
    """
        Wrapp down
    """
    def __init__(self, boss=None):
        tk.Frame.__init__(self, borderwidth=5, bg='RoyalBlue3', padx=0)

        fileMenu = tk.Menubutton(self, text='Menu', fg='white',
            font=("Times 14"), bg='grey30', relief=tk.GROOVE)

        new_text = tk.StringVar()
        try:
            with open('./newpatient/entryfile.txt', 'r') as namefile:
                line1 = namefile.readline()
                new_text = line1
                if new_text == '-':
                    new_text = new_text
                else:
                    new_text = new_text[:-1]
        except FileNotFoundError as fileout:
            print("[!] File entryfile.txt not found to instantiate"\
                " name in labels of menu bar", fileout)

        new_text2 = tk.StringVar()
        try:
            with open('./newpatient/entryfile2.txt', 'r') as namefile2:
                line2 = namefile2.readline()
                new_text2 = line2
                if new_text2 == '--':
                    new_text2 = new_text2
                else:
                    new_text2 = new_text2[:-1]
        except FileNotFoundError as fileout2:
            print("[!] File entryfile2.txt not found to instantiate"\
                " name in labels of menu bar", fileout2)

        new_text3 = tk.StringVar()
        try:
            with open('./newpatient/entryfile3.txt', 'r') as namefile3:
                line3 = namefile3.readline()
                new_text3 = line3
                if new_text3 == '---':
                    new_text3 = new_text3
                else:
                    new_text3 = new_text3[:-1]
        except FileNotFoundError as fileout3:
            print("[!] File entryfile3.txt not found to instantiate"\
                " name in labels of menu bar", fileout3)

        new_text4 = tk.StringVar()
        try:
            with open('./newpatient/entryfile4.txt', 'r') as namefile4:
                line4 = namefile4.readline()
                new_text4 = line4
                if new_text4 == '----':
                    new_text4 = new_text4
                else:
                    new_text4 = new_text4[:-1]
        except FileNotFoundError as fileout4:
            print("[!] File entryfile4.txt not found to instantiate"\
                " name in labels of menu bar", fileout4)

        new_text5 = tk.StringVar()
        try:
            with open('./newpatient/entryfile5.txt', 'r') as namefile5:
                line5 = namefile5.readline()
                new_text5 = line5
                if new_text5 == '-----':
                    new_text5 = new_text5
                else:
                    new_text5 = new_text5[:-1]
        except FileNotFoundError as fileout5:
            print("[!] File entryfile5.txt not found to instantiate"\
                " name in labels of menu bar", fileout5)

        new_text6 = tk.StringVar()
        try:
            with open('./newpatient/entryfile6.txt', 'r') as namefile6:
                line6 = namefile6.readline()
                new_text6 = line6
                if new_text6 == '------':
                    new_text6 = new_text6
                else:
                    new_text6 = new_text6[:-1]
        except FileNotFoundError as fileout6:
            print("[!] File entryfile6.txt not found to instantiate"\
                " name in labels of menu bar", fileout6)

        new_text7 = tk.StringVar()
        try:
            with open('./newpatient/entryfile7.txt', 'r') as namefile7:
                line7 = namefile7.readline()
                new_text7 = line7
                if new_text7 == '-------':
                    new_text7 = new_text7
                else:
                    new_text7 = new_text7[:-1]
        except FileNotFoundError as fileout7:
            print("[!] File entryfile7.txt not found to instantiate"\
                " name in labels of menu bar", fileout7)

        new_text8 = tk.StringVar()
        try:
            with open('./newpatient/entryfile8.txt', 'r') as namefile8:
                line8 = namefile8.readline()
                new_text8 = line8
                if new_text8 == '--------':
                    new_text8 = new_text8
                else:
                    new_text8 = new_text8[:-1]
        except FileNotFoundError as fileout8:
            print("[!] File entryfile8.txt not found to instantiate"\
                " name in labels of menu bar", fileout8)

        new_text9 = tk.StringVar()
        try:
            with open('./newpatient/entryfile9.txt', 'r') as namefile9:
                line9 = namefile9.readline()
                new_text9 = line9
                if new_text9 == '---------':
                    new_text9 = new_text9
                else:
                    new_text9 = new_text9[:-1]
        except FileNotFoundError as fileout9:
            print("[!] File entryfile9.txt not found to instantiate"\
                " name in labels of menu bar", fileout9)

        new_text10 = tk.StringVar()
        try:
            with open('./newpatient/entryfile10.txt', 'r') as namefile10:
                line10 = namefile10.readline()
                new_text10 = line10
                if new_text10 == '----------':
                    new_text10 = new_text10
                else:
                    new_text10 = new_text10[:-1]
        except FileNotFoundError as fileout10:
            print("[!] File entryfile10.txt not found to instantiate"\
                " name in labels of menu bar", fileout10)

        new_text11 = tk.StringVar()
        try:
            with open('./newpatient/entryfile11.txt', 'r') as namefile11:
                line11 = namefile11.readline()
                new_text11 = line11
                if new_text11 == '-----------':
                    new_text11 = new_text11
                else:
                    new_text11 = new_text11[:-1]
        except FileNotFoundError as fileout11:
            print("[!] File entryfile11.txt not found to instantiate"\
                " name in labels of menu bar", fileout11)

        new_text12 = tk.StringVar()
        try:
            with open('./newpatient/entryfile12.txt', 'r') as namefile12:
                line12 = namefile12.readline()
                new_text12 = line12
                if new_text12 == '------------':
                    new_text12 = new_text12
                else:
                    new_text12 = new_text12[:-1]
        except FileNotFoundError as fileout12:
            print("[!] File entryfile12.txt not found to instantiate"\
                " name in labels of menu bar", fileout12)

        new_text13 = tk.StringVar()
        try:
            with open('./newpatient/entryfile13.txt', 'r') as namefile13:
                line13 = namefile13.readline()
                new_text13 = line13
                if new_text13 == '-------------':
                    new_text13 = new_text13
                else:
                    new_text13 = new_text13[:-1]
        except FileNotFoundError as fileout13:
            print("[!] File entryfile13.txt not found to instantiate"\
                " name in labels of menu bar", fileout13)

        new_text14 = tk.StringVar()
        try:
            with open('./newpatient/entryfile14.txt', 'r') as namefile14:
                line14 = namefile14.readline()
                new_text14 = line14
                if new_text14 == '--------------':
                    new_text14 = new_text14
                else:
                    new_text14 = new_text14[:-1]
        except FileNotFoundError as fileout14:
            print("[!] File entryfile14.txt not found to instantiate"\
                " name in labels of menu bar", fileout14)

        new_text15 = tk.StringVar()
        try:
            with open('./newpatient/entryfile15.txt', 'r') as namefile15:
                line15 = namefile15.readline()
                new_text15 = line15
                if new_text15 == '---------------':
                    new_text15 = new_text15
                else:
                    new_text15 = new_text15[:-1]
        except FileNotFoundError as fileout15:
            print("[!] File entryfile15.txt not found to instantiate"\
                " name in labels of menu bar", fileout15)

        new_text16 = tk.StringVar()
        try:
            with open('./newpatient/entryfile16.txt', 'r') as namefile16:
                line16 = namefile16.readline()
                new_text16 = line16
                if new_text16 == '----------------':
                    new_text16 = new_text16
                else:
                    new_text16 = new_text16[:-1]
        except FileNotFoundError as fileout16:
            print("[!] File entryfile16.txt not found to instantiate"\
                " name in labels of menu bar", fileout16)

        new_text17 = tk.StringVar()
        try:
            with open('./newpatient/entryfile17.txt', 'r') as namefile17:
                line17 = namefile17.readline()
                new_text17 = line17
                if new_text17 == '-----------------':
                    new_text17 = new_text17
                else:
                    new_text17 = new_text17[:-1]
        except FileNotFoundError as fileout17:
            print("[!] File entryfile17.txt not found to instantiate"\
                " name in labels of menu bar", fileout17)

        new_text18 = tk.StringVar()
        try:
            with open('./newpatient/entryfile18.txt', 'r') as namefile18:
                line18 = namefile18.readline()
                new_text18 = line18
                if new_text18 == '------------------':
                    new_text18 = new_text18
                else:
                    new_text18 = new_text18[:-1]
        except FileNotFoundError as fileout18:
            print("[!] File entryfile18.txt not found to instantiate"\
                " name in labels of menu bar", fileout18)

        new_text19 = tk.StringVar()
        try:
            with open('./newpatient/entryfile19.txt', 'r') as namefile19:
                line19 = namefile19.readline()
                new_text19 = line19
                if new_text19 == '-------------------':
                    new_text19 = new_text19
                else:
                    new_text19 = new_text19[:-1]
        except FileNotFoundError as fileout19:
            print("[!] File entryfile19.txt not found to instantiate"\
                " name in labels of menu bar", fileout19)

        new_text20 = tk.StringVar()
        try:
            with open('./newpatient/entryfile20.txt', 'r') as namefile20:
                line20 = namefile20.readline()
                new_text20 = line20
                if new_text20 == '--------------------':
                    new_text20 = new_text20
                else:
                    new_text20 = new_text20[:-1]
        except FileNotFoundError as fileout20:
            print("[!] File entryfile20.txt not found to instantiate"\
                " name in labels of menu bar", fileout20)

        new_text21 = tk.StringVar()
        try:
            with open('./newpatient/entryfile21.txt', 'r') as namefile21:
                line21 = namefile21.readline()
                new_text21 = line21
                if new_text21 == '---------------------':
                    new_text21 = new_text21
                else:
                    new_text21 = new_text21[:-1]
        except FileNotFoundError as fileout21:
            print("[!] File entryfile21.txt not found to instantiate"\
                " name in labels of menu bar", fileout21)

        new_text22 = tk.StringVar()
        try:
            with open('./newpatient/entryfile22.txt', 'r') as namefile22:
                line22 = namefile22.readline()
                new_text22 = line22
                if new_text22 == '----------------------':
                    new_text22 = new_text22
                else:
                    new_text22 = new_text22[:-1]
        except FileNotFoundError as fileout22:
            print("[!] File entryfile22.txt not found to instantiate"\
                " name in labels of menu bar", fileout22)

        new_text23 = tk.StringVar()
        try:
            with open('./newpatient/entryfile23.txt', 'r') as namefile23:
                line23 = namefile23.readline()
                new_text23 = line23
                if new_text23 == '-----------------------':
                    new_text23 = new_text23
                else:
                    new_text23 = new_text23[:-1]
        except FileNotFoundError as fileout23:
            print("[!] File entryfile23.txt not found to instantiate"\
                " name in labels of menu bar", fileout23)

        new_text24 = tk.StringVar()
        try:
            with open('./newpatient/entryfile24.txt', 'r') as namefile24:
                line24 = namefile24.readline()
                new_text24 = line24
                if new_text24 == '------------------------':
                    new_text24 = new_text24
                else:
                    new_text24 = new_text24[:-1]
        except FileNotFoundError as fileout24:
            print("[!] File entryfile24.txt not found to instantiate"\
                " name in labels of menu bar", fileout24)

        fileMenu.pack(side=tk.LEFT, padx=3)
        # Menubar
        me1 = Menu(fileMenu, tearoff=0)
        me1.add_command(label='Alarm', font=("Times 14 bold"),
            background='black', activebackground='aquamarine',
            foreground='coral', activeforeground='black',
            command=boss.alarmProg)
        me1.add_command(label='Start Page', underline=0, font=("Times 14 bold"),
            background='black', activebackground='aquamarine',
            foreground='aquamarine', activeforeground='black',
            command=boss.startPage)
        me1.add_command(label="EventBox", underline=0, font=("Times 14 bold"),
            background='black', activebackground='aquamarine',
            foreground='aquamarine', activeforeground='black',
            command=boss.showSynopsis)
        me1.add_command(label="Residents", underline=0, font=("Times 14 bold"),
            background='black', activebackground='aquamarine',
            foreground='aquamarine', activeforeground='black',
            command=boss.showPatients)
        me1.add_command(label='DataBase', font=("Times 14 bold"),
            background='black', activebackground='aquamarine',
            foreground='white', activeforeground='black',
            command=boss.funcPyCon)
        me1.add_command(label='Tutorial', font=("Times 14 bold"),
            background='black', activebackground='aquamarine',
            foreground='yellow', activeforeground='black',
            command=boss.mapApp)
        me1.add_command(label='Quit', font=("Times 14 bold"),
            background='black', activebackground='red',
            foreground='coral', activeforeground='white',
            command=boss.msgExit)
        # Integration of 1st menu
        fileMenu.configure(activeforeground='black', activebackground='cyan',
            menu=me1)

        # Agenda menu
        cmd_agenda = tk.Menubutton(self, text='Agenda', font=("Times 14"),
            fg='cyan', bg='grey30', relief=tk.GROOVE)
        cmd_agenda.pack(side=tk.LEFT, padx=3)
        me3 = Menu(cmd_agenda)
        # Wrapped menu agenda
        me3.add_command(label=new_text, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.patientAgenda(a=1))
        me3.add_command(label=new_text2, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.patientAgenda(a=2))
        me3.add_command(label=new_text3, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.patientAgenda(a=3))
        me3.add_command(label=new_text4, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.patientAgenda(a=4))
        me3.add_command(label=new_text5, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.patientAgenda(a=5))
        me3.add_command(label=new_text6, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.patientAgenda(a=6))
        me3.add_command(label=new_text7, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.patientAgenda(a=7))
        me3.add_command(label=new_text8, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.patientAgenda(a=8))
        me3.add_command(label=new_text9, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.patientAgenda(a=9))
        me3.add_command(label=new_text10, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.patientAgenda(a=10))
        me3.add_command(label=new_text11, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.patientAgenda(a=11))
        me3.add_command(label=new_text12, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.patientAgenda(a=12))
        me3.add_command(label=new_text13, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.patientAgenda(a=13))
        me3.add_command(label=new_text14, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.patientAgenda(a=14))
        me3.add_command(label=new_text15, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.patientAgenda(a=15))
        me3.add_command(label=new_text16, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.patientAgenda(a=16))
        me3.add_command(label=new_text17, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.patientAgenda(a=17))
        me3.add_command(label=new_text18, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.patientAgenda(a=18))
        me3.add_command(label=new_text19, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.patientAgenda(a=19))
        me3.add_command(label=new_text20, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.patientAgenda(a=20))
        me3.add_command(label=new_text21, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.patientAgenda(a=21))
        me3.add_command(label=new_text22, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.patientAgenda(a=22))
        me3.add_command(label=new_text23, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.patientAgenda(a=23))
        me3.add_command(label=new_text24, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.patientAgenda(a=24))
        # Integration of agenda menu
        cmd_agenda.configure(activeforeground='black', activebackground='cyan',
            menu=me3)

        # Contact menu
        contact = tk.Menubutton(self, text='Contact', font=("Times 14"),
            fg='cyan', bg='grey30', relief=tk.GROOVE)
        contact.pack(side=tk.LEFT, padx=3)
        contchck = Menu(contact)
        me1 = Menu(contchck)
        me1.add_command(label='Patient Data', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num1)
        me1.add_command(label='Relation - Family', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactfamily_1)
        me1.add_command(label="Doctors' Data", font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactdoctor_1)
        me1.add_command(label='Home care system', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contacthcsystem_1)
        contchck.add_cascade(label=new_text, underline=0, font=('Times 14'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me1)
        me2 = Menu(contchck)
        me2.add_command(label='Patient Data', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num2)
        me2.add_command(label='Relation - Family', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactfamily_2)
        me2.add_command(label="Doctors' Data", font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactdoctor_2)
        me2.add_command(label='Home care system', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contacthcsystem_2)
        contchck.add_cascade(label=new_text2, underline=0, font=('Times 14'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me2)
        me3 = Menu(contchck)
        me3.add_command(label='Patient Data', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num3)
        me3.add_command(label='Relation - Family', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactfamily_3)
        me3.add_command(label="Doctors' Data", font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactdoctor_3)
        me3.add_command(label='Home care system', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contacthcsystem_3)
        contchck.add_cascade(label=new_text3, underline=0, font=('Times 14'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me3)
        me4 = Menu(contchck)
        me4.add_command(label='Patient Data', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num4)
        me4.add_command(label='Relation - Family', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactfamily_4)
        me4.add_command(label="Doctors' Data", font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactdoctor_4)
        me4.add_command(label='Home care system', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contacthcsystem_4)
        contchck.add_cascade(label=new_text4, underline=0, font=('Times 14'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me4)
        me5 = Menu(contchck)
        me5.add_command(label='Patient Data', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num5)
        me5.add_command(label='Relation - Family', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactfamily_5)
        me5.add_command(label="Doctors' Data", font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactdoctor_5)
        me5.add_command(label='Home care system', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contacthcsystem_5)
        contchck.add_cascade(label=new_text5, underline=0, font=('Times 14'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me5)
        me6 = Menu(contchck)
        me6.add_command(label='Patient Data', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num6)
        me6.add_command(label='Relation - Family', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactfamily_6)
        me6.add_command(label="Doctors' Data", font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactdoctor_6)
        me6.add_command(label='Home care system', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contacthcsystem_6)
        contchck.add_cascade(label=new_text6, underline=0, font=('Times 14'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me6)
        me7 = Menu(contchck)
        me7.add_command(label='Patient Data', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num7)
        me7.add_command(label='Relation - Family', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactfamily_7)
        me7.add_command(label="Doctors' Data", font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactdoctor_7)
        me7.add_command(label='Home care system', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contacthcsystem_7)
        contchck.add_cascade(label=new_text7, underline=0, font=('Times 14'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me7)
        me8 = Menu(contchck)
        me8.add_command(label='Patient Data', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num8)
        me8.add_command(label='Relation - Family', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactfamily_8)
        me8.add_command(label="Doctors' Data", font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactdoctor_8)
        me8.add_command(label='Home care system', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contacthcsystem_8)
        contchck.add_cascade(label=new_text8, underline=0, font=('Times 14'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me8)
        me9 = Menu(contchck)
        me9.add_command(label='Patient Data', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num9)
        me9.add_command(label='Relation - Family', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactfamily_9)
        me9.add_command(label="Doctors' Data", font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactdoctor_9)
        me9.add_command(label='Home care system', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contacthcsystem_9)
        contchck.add_cascade(label=new_text9, underline=0, font=('Times 14'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me9)
        me10 = Menu(contchck)
        me10.add_command(label='Patient Data', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num10)
        me10.add_command(label='Relation - Family', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactfamily_10)
        me10.add_command(label="Doctors' Data", font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactdoctor_10)
        me10.add_command(label='Home care system', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contacthcsystem_10)
        contchck.add_cascade(label=new_text10, underline=0, font=('Times 14'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me10)
        me11 = Menu(contchck)
        me11.add_command(label='Patient Data', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num11)
        me11.add_command(label='Relation - Family', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactfamily_11)
        me11.add_command(label="Doctors' Data", font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactdoctor_11)
        me11.add_command(label='Home care system', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contacthcsystem_11)
        contchck.add_cascade(label=new_text11, underline=0, font=('Times 14'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me11)
        me12 = Menu(contchck)
        me12.add_command(label='Patient Data', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num12)
        me12.add_command(label='Relation - Family', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactfamily_12)
        me12.add_command(label="Doctors' Data", font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactdoctor_12)
        me12.add_command(label='Home care system', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contacthcsystem_12)
        contchck.add_cascade(label=new_text12, underline=0, font=('Times 14'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me12)
        me13 = Menu(contchck)
        me13.add_command(label='Patient Data', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num13)
        me13.add_command(label='Relation - Family', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactfamily_13)
        me13.add_command(label="Doctors' Data", font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactdoctor_13)
        me13.add_command(label='Home care system', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contacthcsystem_13)
        contchck.add_cascade(label=new_text13, underline=0, font=('Times 14'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me13)
        me14 = Menu(contchck)
        me14.add_command(label='Patient Data', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num14)
        me14.add_command(label='Relation - Family', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactfamily_14)
        me14.add_command(label="Doctors' Data", font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactdoctor_14)
        me14.add_command(label='Home care system', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contacthcsystem_14)
        contchck.add_cascade(label=new_text14, underline=0, font=('Times 14'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me14)
        me15 = Menu(contchck)
        me15.add_command(label='Patient Data', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num15)
        me15.add_command(label='Relation - Family', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactfamily_15)
        me15.add_command(label="Doctors' Data", font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactdoctor_15)
        me15.add_command(label='Home care system', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contacthcsystem_15)
        contchck.add_cascade(label=new_text15, underline=0, font=('Times 14'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me15)
        me16 = Menu(contchck)
        me16.add_command(label='Patient Data', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num16)
        me16.add_command(label='Relation - Family', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactfamily_16)
        me16.add_command(label="Doctors' Data", font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactdoctor_16)
        me16.add_command(label='Home care system', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contacthcsystem_16)
        contchck.add_cascade(label=new_text16, underline=0, font=('Times 14'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me16)
        me17 = Menu(contchck)
        me17.add_command(label='Patient Data', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num17)
        me17.add_command(label='Relation - Family', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactfamily_17)
        me17.add_command(label="Doctors' Data", font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactdoctor_17)
        me17.add_command(label='Home care system', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contacthcsystem_17)
        contchck.add_cascade(label=new_text17, underline=0, font=('Times 14'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me17)
        me18 = Menu(contchck)
        me18.add_command(label='Patient Data', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num18)
        me18.add_command(label='Relation - Family', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactfamily_18)
        me18.add_command(label="Doctors' Data", font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactdoctor_18)
        me18.add_command(label='Home care system', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contacthcsystem_18)
        contchck.add_cascade(label=new_text18, underline=0, font=('Times 14'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me18)
        me19 = Menu(contchck)
        me19.add_command(label='Patient Data', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num19)
        me19.add_command(label='Relation - Family', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactfamily_19)
        me19.add_command(label="Doctors' Data", font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactdoctor_19)
        me19.add_command(label='Home care system', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contacthcsystem_19)
        contchck.add_cascade(label=new_text19, underline=0, font=('Times 14'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me19)
        me20 = Menu(contchck)
        me20.add_command(label='Patient Data', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num20)
        me20.add_command(label='Relation - Family', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactfamily_20)
        me20.add_command(label="Doctors' Data", font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactdoctor_20)
        me20.add_command(label='Home care system', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contacthcsystem_20)
        contchck.add_cascade(label=new_text20, underline=0, font=('Times 14'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me20)
        me21 = Menu(contchck)
        me21.add_command(label='Patient Data', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num21)
        me21.add_command(label='Relation - Family', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactfamily_21)
        me21.add_command(label="Doctors' Data", font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactdoctor_21)
        me21.add_command(label='Home care system', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contacthcsystem_21)
        contchck.add_cascade(label=new_text21, underline=0, font=('Times 14'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me21)
        me22 = Menu(contchck)
        me22.add_command(label='Patient Data', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num22)
        me22.add_command(label='Relation - Family', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactfamily_22)
        me22.add_command(label="Doctors' Data", font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactdoctor_22)
        me22.add_command(label='Home care system', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contacthcsystem_22)
        contchck.add_cascade(label=new_text22, underline=0, font=('Times 14'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me22)
        me23 = Menu(contchck)
        me23.add_command(label='Patient Data', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num23)
        me23.add_command(label='Relation - Family', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactfamily_23)
        me23.add_command(label="Doctors' Data", font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactdoctor_23)
        me23.add_command(label='Home care system', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contacthcsystem_23)
        contchck.add_cascade(label=new_text23, underline=0, font=('Times 14'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me23)
        me24 = Menu(contchck)
        me24.add_command(label='Patient Data', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num24)
        me24.add_command(label='Relation - Family', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactfamily_24)
        me24.add_command(label="Doctors' Data", font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactdoctor_24)
        me24.add_command(label='Home care system', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contacthcsystem_24)
        contchck.add_cascade(label=new_text24, underline=0, font=('Times 14'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me24)
        contact.configure(activeforeground='black', activebackground='cyan', menu=contchck)

        # 14 besoins menu
        cmd_Besoins = tk.Menubutton(self, text='14 Needs', font=("Times 14"),
            fg='cyan', bg='grey30', relief=tk.GROOVE)
        cmd_Besoins.pack(side=tk.LEFT, padx=3)
        # Partie déroulante du menu 14b
        me4 = Menu(cmd_Besoins)
        me4.add_command(label=new_text, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.besoinsCoche(b=1))
        #me4.add_separator()
        me4.add_command(label=new_text2, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.besoinsCoche(b=2))
        #me4.add_separator()
        me4.add_command(label=new_text3, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.besoinsCoche(b=3))
        #me4.add_separator()
        me4.add_command(label=new_text4, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.besoinsCoche(b=4))
        #me4.add_separator()
        me4.add_command(label=new_text5, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.besoinsCoche(b=5))
        #me4.add_separator()
        me4.add_command(label=new_text6, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.besoinsCoche(b=6))
        #me4.add_separator()
        me4.add_command(label=new_text7, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.besoinsCoche(b=7))
        #me4.add_separator()
        me4.add_command(label=new_text8, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.besoinsCoche(b=8))
        #me4.add_separator()
        me4.add_command(label=new_text9, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.besoinsCoche(b=9))
        #me4.add_separator()
        me4.add_command(label=new_text10, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.besoinsCoche(b=10))
        #me4.add_separator()
        me4.add_command(label=new_text11, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.besoinsCoche(b=11))
        #me4.add_separator()
        me4.add_command(label=new_text12, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.besoinsCoche(b=12))
        #me4.add_separator()
        me4.add_command(label=new_text13, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.besoinsCoche(b=13))
        #me4.add_separator()
        me4.add_command(label=new_text14, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.besoinsCoche(b=14))
        #me4.add_separator()
        me4.add_command(label=new_text15, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.besoinsCoche(b=15))
        #me4.add_separator()
        me4.add_command(label=new_text16, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.besoinsCoche(b=16))
        #me4.add_separator()
        me4.add_command(label=new_text17, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.besoinsCoche(b=17))
        #me4.add_separator()
        me4.add_command(label=new_text18, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.besoinsCoche(b=18))
        #me4.add_separator()
        me4.add_command(label=new_text19, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.besoinsCoche(b=19))
        #me4.add_separator()
        me4.add_command(label=new_text20, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.besoinsCoche(b=20))
        #me4.add_separator()
        me4.add_command(label=new_text21, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.besoinsCoche(b=21))
        #me4.add_separator()
        me4.add_command(label=new_text22, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.besoinsCoche(b=22))
        #me4.add_separator()
        me4.add_command(label=new_text23, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.besoinsCoche(b=23))
        #me4.add_separator()
        me4.add_command(label=new_text24, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.besoinsCoche(b=24))
        # Integration of 14b menu
        cmd_Besoins.configure(activeforeground='black', activebackground='cyan',
            menu=me4)

        # Helth and care menu
        cmd_Soins = tk.Menubutton(self, text='Care and monitoring', font=("Times 14"),
            fg='cyan', bg='grey30', relief=tk.GROOVE)
        cmd_Soins.pack(side=tk.LEFT, padx=3)
        # Partie déroulante du menu health and care
        meSoins = Menu(cmd_Soins)
        meSoins.add_command(label=new_text, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.suiviSoins(s=1))
        #meSoins.add_separator()
        meSoins.add_command(label=new_text2, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.suiviSoins(s=2))
        #meSoins.add_separator()
        meSoins.add_command(label=new_text3, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.suiviSoins(s=3))
        #meSoins.add_separator()
        meSoins.add_command(label=new_text4, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.suiviSoins(s=4))
        #meSoins.add_separator()
        meSoins.add_command(label=new_text5, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.suiviSoins(s=5))
        #meSoins.add_separator()
        meSoins.add_command(label=new_text6, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.suiviSoins(s=6))
        #meSoins.add_separator()
        meSoins.add_command(label=new_text7, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.suiviSoins(s=7))
        #meSoins.add_separator()
        meSoins.add_command(label=new_text8, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.suiviSoins(s=8))
        #meSoins.add_separator()
        meSoins.add_command(label=new_text9, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.suiviSoins(s=9))
        #meSoins.add_separator()
        meSoins.add_command(label=new_text10, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.suiviSoins(s=10))
        #meSoins.add_separator()
        meSoins.add_command(label=new_text11, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.suiviSoins(s=11))
        #meSoins.add_separator()
        meSoins.add_command(label=new_text12, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.suiviSoins(s=12))
        #meSoins.add_separator()
        meSoins.add_command(label=new_text13, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.suiviSoins(s=13))
        #meSoins.add_separator()
        meSoins.add_command(label=new_text14, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.suiviSoins(s=14))
        #meSoins.add_separator()
        meSoins.add_command(label=new_text15, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.suiviSoins(s=15))
        #meSoins.add_separator()
        meSoins.add_command(label=new_text16, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.suiviSoins(s=16))
        #meSoins.add_separator()
        meSoins.add_command(label=new_text17, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.suiviSoins(s=17))
        #meSoins.add_separator()
        meSoins.add_command(label=new_text18, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.suiviSoins(s=18))
        #meSoins.add_separator()
        meSoins.add_command(label=new_text19, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.suiviSoins(s=19))
        #meSoins.add_separator()
        meSoins.add_command(label=new_text20, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.suiviSoins(s=20))
        #meSoins.add_separator()
        meSoins.add_command(label=new_text21, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.suiviSoins(s=21))
        #meSoins.add_separator()
        meSoins.add_command(label=new_text22, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.suiviSoins(s=22))
        #meSoins.add_separator()
        meSoins.add_command(label=new_text23, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.suiviSoins(s=23))
        #meSoins.add_separator()
        meSoins.add_command(label=new_text24, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.suiviSoins(s=24))
        # Integration of health and care menu
        cmd_Soins.configure(activeforeground='black', activebackground='cyan',
            menu=meSoins)

        # Vital parameters menu
        self.cmd_Param = tk.Menubutton(self, text='Vital Parameters', font=("Times 14"),
            fg='cyan', bg='grey30', relief=tk.GROOVE)
        self.cmd_Param.pack(side=tk.LEFT, padx=3)
        # Partie déroulante du menu param
        menuParam = Menu(self.cmd_Param)
        menuParam.add_command(label=new_text, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.showParam(p=1))
        #menuParam.add_separator()
        menuParam.add_command(label=new_text2, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.showParam(p=2))
        #menuParam.add_separator()
        menuParam.add_command(label=new_text3, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.showParam(p=3))
        #menuParam.add_separator()
        menuParam.add_command(label=new_text4, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.showParam(p=4))
        #menuParam.add_separator()
        menuParam.add_command(label=new_text5, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.showParam(p=5))
        #menuParam.add_separator()
        menuParam.add_command(label=new_text6, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.showParam(p=6))
        #menuParam.add_separator()
        menuParam.add_command(label=new_text7, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.showParam(p=7))
        #menuParam.add_separator()
        menuParam.add_command(label=new_text8, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.showParam(p=8))
        #menuParam.add_separator()
        menuParam.add_command(label=new_text9, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.showParam(p=9))
        #menuParam.add_separator()
        menuParam.add_command(label=new_text10, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.showParam(p=10))
        #menuParam.add_separator()
        menuParam.add_command(label=new_text11, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.showParam(p=11))
        #menuParam.add_separator()
        menuParam.add_command(label=new_text12, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.showParam(p=12))
        #menuParam.add_separator()
        menuParam.add_command(label=new_text13, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.showParam(p=13))
        #menuParam.add_separator()
        menuParam.add_command(label=new_text14, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.showParam(p=14))
        #menuParam.add_separator()
        menuParam.add_command(label=new_text15, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.showParam(p=15))
        #menuParam.add_separator()
        menuParam.add_command(label=new_text16, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.showParam(p=16))
        #menuParam.add_separator()
        menuParam.add_command(label=new_text17, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.showParam(p=17))
        #menuParam.add_separator()
        menuParam.add_command(label=new_text18, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.showParam(p=18))
        #menuParam.add_separator()
        menuParam.add_command(label=new_text19, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.showParam(p=19))
        #menuParam.add_separator()
        menuParam.add_command(label=new_text20, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.showParam(p=20))
        #menuParam.add_separator()
        menuParam.add_command(label=new_text21, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.showParam(p=21))
        #menuParam.add_separator()
        menuParam.add_command(label=new_text22, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.showParam(p=22))
        #menuParam.add_separator()
        menuParam.add_command(label=new_text23, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.showParam(p=23))
        #menuParam.add_separator()
        menuParam.add_command(label=new_text24, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.showParam(p=24))
        # Integration of Vital parameters menu
        self.cmd_Param.configure(activeforeground='black', activebackground='cyan',
            menu=menuParam)

        # BMI menu
        cmd_BMI = tk.Menubutton(self, text='Body Mass Indice', font=("Times 14"),
            fg='cyan', bg='grey30', relief=tk.GROOVE)
        cmd_BMI.pack(side=tk.LEFT, padx=3)
        # drop-down portion of BMI menu
        meBmi = Menu(cmd_BMI)
        meBmi.add_command(label=new_text, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.calculB(u=1))
        meBmi.add_command(label=new_text2, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.calculB(u=2))
        meBmi.add_command(label=new_text3, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.calculB(u=3))
        meBmi.add_command(label=new_text4, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.calculB(u=4))
        meBmi.add_command(label=new_text5, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.calculB(u=5))
        meBmi.add_command(label=new_text6, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.calculB(u=6))
        meBmi.add_command(label=new_text7, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.calculB(u=7))
        meBmi.add_command(label=new_text8, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.calculB(u=8))
        meBmi.add_command(label=new_text9, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.calculB(u=9))
        meBmi.add_command(label=new_text10, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.calculB(u=10))
        meBmi.add_command(label=new_text11, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.calculB(u=11))
        meBmi.add_command(label=new_text12, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.calculB(u=12))
        meBmi.add_command(label=new_text13, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.calculB(u=13))
        meBmi.add_command(label=new_text14, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.calculB(u=14))
        meBmi.add_command(label=new_text15, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.calculB(u=15))
        meBmi.add_command(label=new_text16, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.calculB(u=16))
        meBmi.add_command(label=new_text17, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.calculB(u=17))
        meBmi.add_command(label=new_text18, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.calculB(u=18))
        meBmi.add_command(label=new_text19, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.calculB(u=19))
        meBmi.add_command(label=new_text20, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.calculB(u=20))
        meBmi.add_command(label=new_text21, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.calculB(u=21))
        meBmi.add_command(label=new_text22, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.calculB(u=22))
        meBmi.add_command(label=new_text23, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.calculB(u=23))
        meBmi.add_command(label=new_text24, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.calculB(u=24))
        # Integration of 3rd menu
        cmd_BMI.configure(activeforeground='black', activebackground='cyan',
            menu=meBmi)

        # Medical Visit
        cmd_Vmed = tk.Menubutton(self, text='Medical Visit', font=("Times 14"),
            fg='cyan', bg='grey30', relief=tk.GROOVE)
        cmd_Vmed.pack(side=tk.LEFT, padx=3)
        # drop-down portion of vmed
        meVmed = Menu(cmd_Vmed)
        meVmed.add_command(label=new_text, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed)
        meVmed.add_command(label=new_text2, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed2)
        meVmed.add_command(label=new_text3, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed3)
        meVmed.add_command(label=new_text4, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed4)
        meVmed.add_command(label=new_text5, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed5)
        meVmed.add_command(label=new_text6, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed6)
        meVmed.add_command(label=new_text7, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed7)
        meVmed.add_command(label=new_text8, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed8)
        meVmed.add_command(label=new_text9, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed9)
        meVmed.add_command(label=new_text10, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed10)
        meVmed.add_command(label=new_text11, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed11)
        meVmed.add_command(label=new_text12, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed12)
        meVmed.add_command(label=new_text13, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed13)
        meVmed.add_command(label=new_text14, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed14)
        meVmed.add_command(label=new_text15, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed15)
        meVmed.add_command(label=new_text16, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed16)
        meVmed.add_command(label=new_text17, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed17)
        meVmed.add_command(label=new_text18, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed18)
        meVmed.add_command(label=new_text19, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed19)
        meVmed.add_command(label=new_text20, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed20)
        meVmed.add_command(label=new_text21, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed21)
        meVmed.add_command(label=new_text22, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed22)
        meVmed.add_command(label=new_text23, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed23)
        meVmed.add_command(label=new_text24, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed24)
        # Integration of 3rd menu
        cmd_Vmed.configure(activeforeground='black', activebackground='cyan',
            menu=meVmed)

        # Nutrition menu for intolerance and hate meals
        cmd_Print = tk.Menubutton(self, text='Intolerance All.', font=("Times 14"),
            fg='cyan', bg='grey30', relief=tk.GROOVE)
        cmd_Print.pack(side=tk.LEFT, padx=3)
        # drop-down portion of nutrition
        mePrint = Menu(cmd_Print)
        mePrint.add_command(label=new_text, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.nutritionMenu(n=1))
        mePrint.add_command(label=new_text2, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.nutritionMenu(n=2))
        mePrint.add_command(label=new_text3, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.nutritionMenu(n=3))
        mePrint.add_command(label=new_text4, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.nutritionMenu(n=4))
        mePrint.add_command(label=new_text5, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.nutritionMenu(n=5))
        mePrint.add_command(label=new_text6, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.nutritionMenu(n=6))
        mePrint.add_command(label=new_text7, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.nutritionMenu(n=7))
        mePrint.add_command(label=new_text8, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.nutritionMenu(n=8))
        mePrint.add_command(label=new_text9, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.nutritionMenu(n=9))
        mePrint.add_command(label=new_text10, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.nutritionMenu(n=10))
        mePrint.add_command(label=new_text11, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.nutritionMenu(n=11))
        mePrint.add_command(label=new_text12, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.nutritionMenu(n=12))
        mePrint.add_command(label=new_text13, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.nutritionMenu(n=13))
        mePrint.add_command(label=new_text14, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.nutritionMenu(n=14))
        mePrint.add_command(label=new_text15, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.nutritionMenu(n=15))
        mePrint.add_command(label=new_text16, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.nutritionMenu(n=16))
        mePrint.add_command(label=new_text17, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.nutritionMenu(n=17))
        mePrint.add_command(label=new_text18, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.nutritionMenu(n=18))
        mePrint.add_command(label=new_text19, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.nutritionMenu(n=19))
        mePrint.add_command(label=new_text20, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.nutritionMenu(n=20))
        mePrint.add_command(label=new_text21, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.nutritionMenu(n=21))
        mePrint.add_command(label=new_text22, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.nutritionMenu(n=22))
        mePrint.add_command(label=new_text23, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.nutritionMenu(n=23))
        mePrint.add_command(label=new_text24, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.nutritionMenu(n=24))
        # Integration of nutrition menu
        cmd_Print.configure(activeforeground='black', activebackground='cyan',
            menu=mePrint)

        # Manuals Nurse
        self.cmd_manu=tk.Menubutton(self, text='Manuals', font=('Times 14'), fg='cyan',
            bg='grey30', relief=tk.GROOVE)
        self.cmd_manu.pack(side=tk.LEFT, padx=3)
        # drop-down portion of Manuals Nurse
        memanu = Menu(self.cmd_manu)
        memanu.add_command(label='Click on it', font=('Times 16'),
            background='black', activebackground='cyan', foreground='cyan',
            activeforeground='black', command=boss.manualFile)
        # Integration of Manuals Nurse
        self.cmd_manu.configure(activeforeground='black', activebackground='cyan',
            menu=memanu)

        # Menu for showing all Folder togather per patient
        cmd_backup = tk.Menubutton(self, text='Global', font=("Times 14"), fg='cyan',
            bg='grey30', relief=tk.GROOVE)
        cmd_backup.pack(side=tk.LEFT, padx=3)
        # drop-down portion of menu
        me1 = Menu(cmd_backup)
        me2 = Menu(me1)
        me2.add_command(label='All Files.txt', underline=0, font=('Times 14'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black',
            command=lambda: boss.allFilesBackup(f=1))
        me1.add_cascade(label=new_text, underline=0, font=('Times 14'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me2)
        me3=Menu(me1)
        me3.add_command(label='All Files.txt', underline=0, font=('Times 14'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black',
            command=lambda: boss.allFilesBackup(f=2))
        me1.add_cascade(label=new_text2, underline=0, font=('Times 14'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me3)
        me4=Menu(me1)
        me4.add_command(label='All Files.txt', underline=0, font=('Times 14'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black',
            command=lambda: boss.allFilesBackup(f=3))
        me1.add_cascade(label=new_text3, underline=0, font=('Times 14'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me4)
        me5=Menu(me1)
        me5.add_command(label='All Files.txt', underline=0, font=('Times 14'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black',
            command=lambda: boss.allFilesBackup(f=4))
        me1.add_cascade(label=new_text4, underline=0, font=('Times 14'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me5)
        me6=Menu(me1)
        me6.add_command(label='All Files.txt', underline=0, font=('Times 14'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black',
            command=lambda: boss.allFilesBackup(f=5))
        me1.add_cascade(label=new_text5, underline=0, font=('Times 14'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me6)
        me7=Menu(me1)
        me7.add_command(label='All Files.txt', underline=0, font=('Times 14'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black',
            command=lambda: boss.allFilesBackup(f=6))
        me1.add_cascade(label=new_text6, underline=0, font=('Times 14'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me7)
        me8=Menu(me1)
        me8.add_command(label='All Files.txt', underline=0, font=('Times 14'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black',
            command=lambda: boss.allFilesBackup(f=7))
        me1.add_cascade(label=new_text7, underline=0, font=('Times 14'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me8)
        me9=Menu(me1)
        me9.add_command(label='All Files.txt', underline=0, font=('Times 14'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black',
            command=lambda: boss.allFilesBackup(f=8))
        me1.add_cascade(label=new_text8, underline=0, font=('Times 14'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me9)
        me10=Menu(me1)
        me10.add_command(label='All Files.txt', underline=0, font=('Times 14'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black',
            command=lambda: boss.allFilesBackup(f=9))
        me1.add_cascade(label=new_text9, underline=0, font=('Times 14'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me10)
        me11=Menu(me1)
        me11.add_command(label='All Files.txt', underline=0, font=('Times 14'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black',
            command=lambda: boss.allFilesBackup(f=10))
        me1.add_cascade(label=new_text10, underline=0, font=('Times 14'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me11)
        me12=Menu(me1)
        me12.add_command(label='All Files.txt', underline=0, font=('Times 14'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black',
            command=lambda: boss.allFilesBackup(f=11))
        me1.add_cascade(label=new_text11, underline=0, font=('Times 14'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me12)
        me13=Menu(me1)
        me13.add_command(label='All Files.txt', underline=0, font=('Times 14'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black',
            command=lambda: boss.allFilesBackup(f=12))
        me1.add_cascade(label=new_text12, underline=0, font=('Times 14'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me13)
        me14=Menu(me1)
        me14.add_command(label='All Files.txt', underline=0, font=('Times 14'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black',
            command=lambda: boss.allFilesBackup(f=13))
        me1.add_cascade(label=new_text13, underline=0, font=('Times 14'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me14)
        me15=Menu(me1)
        me15.add_command(label='All Files.txt', underline=0, font=('Times 14'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black',
            command=lambda: boss.allFilesBackup(f=14))
        me1.add_cascade(label=new_text14, underline=0, font=('Times 14'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me15)
        me16=Menu(me1)
        me16.add_command(label='All Files.txt', underline=0, font=('Times 14'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black',
            command=lambda: boss.allFilesBackup(f=15))
        me1.add_cascade(label=new_text15, underline=0, font=('Times 14'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me16)
        me17=Menu(me1)
        me17.add_command(label='All Files.txt', underline=0, font=('Times 14'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black',
            command=lambda: boss.allFilesBackup(f=16))
        me1.add_cascade(label=new_text16, underline=0, font=('Times 14'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me17)
        me18=Menu(me1)
        me18.add_command(label='All Files.txt', underline=0, font=('Times 14'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black',
            command=lambda: boss.allFilesBackup(f=17))
        me1.add_cascade(label=new_text17, underline=0, font=('Times 14'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me18)
        me19=Menu(me1)
        me19.add_command(label='All Files.txt', underline=0, font=('Times 14'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black',
            command=lambda: boss.allFilesBackup(f=18))
        me1.add_cascade(label=new_text18, underline=0, font=('Times 14'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me19)
        me20=Menu(me1)
        me20.add_command(label='All Files.txt', underline=0, font=('Times 14'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black',
            command=lambda: boss.allFilesBackup(f=19))
        me1.add_cascade(label=new_text19, underline=0, font=('Times 14'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me20)
        me21=Menu(me1)
        me21.add_command(label='All Files.txt', underline=0, font=('Times 14'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black',
            command=lambda: boss.allFilesBackup(f=20))
        me1.add_cascade(label=new_text20, underline=0, font=('Times 14'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me21)
        me22=Menu(me1)
        me22.add_command(label='All Files.txt', underline=0, font=('Times 14'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black',
            command=lambda: boss.allFilesBackup(f=21))
        me1.add_cascade(label=new_text21, underline=0, font=('Times 14'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me22)
        me23=Menu(me1)
        me23.add_command(label='All Files.txt', underline=0, font=('Times 14'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black',
            command=lambda: boss.allFilesBackup(f=22))
        me1.add_cascade(label=new_text22, underline=0, font=('Times 14'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me23)
        me24=Menu(me1)
        me24.add_command(label='All Files.txt', underline=0, font=('Times 14'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black',
            command=lambda: boss.allFilesBackup(f=23))
        me1.add_cascade(label=new_text23, underline=0, font=('Times 14'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me24)
        me25=Menu(me1)
        me25.add_command(label='All Files.txt', underline=0, font=('Times 14'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black',
            command=lambda: boss.allFilesBackup(f=24))
        me1.add_cascade(label=new_text24, underline=0, font=('Times 14'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me25)
        # Integration of Graph menu
        cmd_backup.configure(activeforeground='black', activebackground='cyan', menu=me1)

class Application(tk.Frame):
    """
        Main app to display first page.
    """
    def __init__(self, boss=None):
        tk.Frame.__init__(self, borderwidth=0, bg='RoyalBlue4', padx=20, pady=20, relief=tk.GROOVE)
        self.master.title('Time-Track Developed by ko@l@tr33')
        self.master.withdraw()
        self.master.update_idletasks()  # Update "requested size" from geometry manager
        x = (self.master.winfo_screenwidth() / 3 - self.master.winfo_reqwidth()) / 2
        y = (self.master.winfo_screenheight() / 3 - self.master.winfo_reqheight()) / 2
        self.master.geometry("+%d+%d" % (x, y))
        self.master.deiconify()
        self.master.protocol("WM_DELETE_WINDOW", lambda arg=self.master: self.msgQuitapp(arg))

        self.mBar = MenuBar(self)
        self.mBar.pack(side=tk.TOP, fill=tk.X, expand=1)

        self.can = tk.Canvas(self, width=1250, height=700, bg='black')
        self.viewPort = tk.Frame(self.can)

        # ScrollCanvas limited by area of ScrollBar 1250 - 700
        self.vsb = tk.Scrollbar(self, orient=tk.VERTICAL, command=self.can.yview)
        self.can.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(side=tk.RIGHT, fill=tk.Y)

        # clock_label to display time
        self.clock_label = tk.Label(self, text="", fg="white", bg="RoyalBlue3",
            font=("helvetica", 18, 'bold'))
        self.clock_label.pack(side=tk.TOP, fill=tk.X, expand=1)
        self.clock_label.after(200, self.tick)

        # Frame size configuration
        self.can.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        self.canvas_window = self.can.create_window((4,4), window=self.viewPort,
            anchor=tk.NW, tags="self.viewPort")

        #self.frame.bind("<Configure>", self.onFrameConfigure)
        self.viewPort.bind("<Configure>", self.onFrameConfigure)
        #self.onFrameConfigure(None)
        self.pack()
        self.startPage()

    def startPage(self):
        """
            First page when you start app.
        """
        # Insert picture
        self.effacer()
        self.delScroll()
        self.photo = tk.PhotoImage(file='./syno_gif/fondcolorbg4.png')
        self.itemfirst = self.can.create_image(625, 350, image=self.photo)

        # Insert text
        self.can.create_text(625, 350, anchor=tk.CENTER,
            text="Python 3.6 - Tkinter 8.6 - GIMP 2.8",
            font=('Times New Roman', 18, 'bold'), fill='turquoise')

        # Insert text
        self.can.create_text(1240, 670, anchor=tk.NE, text="ko@l@tr33",
            font=('Times', 12), fill='turquoise')

        # 3 buttons at first.
        self.button1 = tk.Button(self, text="Info", font=('Times 14 bold'),
            bg='grey17', fg='cyan', command = self.frameInfo)
        self.button1.configure(width=10, bd=3, highlightbackground='grey10',
            activebackground='pale turquoise')
        self.button1_window = self.can.create_window(75, 30, anchor=tk.CENTER,
            window=self.button1)

        # Connection to DB
        self.button2 = tk.Button(self, text="DATABASE", font=('Times 18 bold'),
            bg='RoyalBlue3', fg='white', command = self.funcPyCon)
        self.button2.configure(width=15, bd=3, highlightbackground='RoyalBlue4',
            activebackground='pale turquoise')
        self.button2_window = self.can.create_window(300, 450, anchor=tk.CENTER,
            window=self.button2)

        # Synopsis button
        self.button3 = tk.Button(self, text="EVENTBOX", font=('Times 18 bold'),
            bg='RoyalBlue3', fg='white', command = self.showSynopsis)
        self.button3.configure(width=15, bd=3, highlightbackground='RoyalBlue4',
            activebackground='pale turquoise')
        self.button3_window = self.can.create_window(625, 450, anchor=tk.CENTER,
            window=self.button3)

        # Patients button
        self.button4 = tk.Button(self, text="RESIDENTS", font=('Times 18 bold'),
            bg='RoyalBlue3', fg='white', command = self.showPatients)
        self.button4.configure(width=15, bd=3, highlightbackground='RoyalBlue4',
            activebackground='pale turquoise')
        self.button4_window = self.can.create_window(950, 450, anchor=tk.CENTER,
            window=self.button4)
        #self.pack()
        self.can.configure(scrollregion=self.can.bbox(tk.ALL))

    def tick(self):
        """ Updates the display clock every 200 milliseconds """
        self.new_time = time.strftime("%H:%M:%S %p")
        try:
            if self.new_time == self.new_time:
                self.time = self.new_time
                self.display_time = self.time
                self.clock_label.configure(text=self.display_time)
                self._job = self.clock_label.after(200, self.tick)
        except (ValueError, OSError) as val_err:
            print("[!] Error time --> ", val_err)

    def onMouseWheel(self, event):
        if platform.system() == 'Windows':
            self.can.yview_scroll(int(-1* (event.delta/120)), "units")
        elif platform.system() == 'Darwin':
            self.can.yview_scroll(int(-1 * event.delta), "units")
        else:
            if event.num == 4:
                self.can.yview_scroll(-1, "units")
            elif event.num == 5:
                self.can.yview_scroll(1, "units")

    def onEnter(self, event):
        if platform.system() == 'Linux':
            self.can.bind_all("<Button-4>", self.onMouseWheel)
            self.can.bind_all("<Button-5>", self.onMouseWheel)
        else:
            self.can.bind_all("<MouseWheel>", self.onMouseWheel)

    def onLeave(self, event):
        if platform.system() == 'Linux':
            self.can.unbind_all("<Button-4>")
            self.can.unbind_all("<Button-5>")
        else:
            self.can.unbind_all("<MouseWheel>")

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.can.configure(scrollregion=self.can.bbox(tk.ALL))

    def onCanvasConfigure(self, event):
        '''Reset the canvas window to encompass inner frame when required'''
        canvas_width = event.width
        self.can.itemconfig(self.canvas_window, width = canvas_width)

    def alarmProg(self):
        """
            Usr set an alarm to remind him something.
        """
        alarmThread(self)

    def showSynopsis(self):
        """
            Call synopsis boxapp.py for
            reading data one day before.
        """
        callBox(self)

    def showPatients(self):
        """
            Call functions in patcaps.py.
            Main frame with all patients.
        """
        callResident(self)

    def funcPyCon(self):
        """
            Display data from mysql database.
        """
        self.master.withdraw()
        subprocess.run('./accessDB.py', check=True)
        self.master.deiconify()

    def mapApp(self):
        """
            Explanations about application.
        """
        instalpy(self)

    def effacer(self):
        '''Reinitialize canvas when we pass through another'''
        self.can.delete(tk.ALL)

        try:
            exists = self.item.winfo_exists()
            if exists == 1:
                self.item.pack_forget()
        except Exception as err_tk:
            print("item doesn't exist", err_tk)

        try:
            existext = self.text_area.winfo_exists()
            if existext == 1:
                self.text_area.pack_forget()
        except Exception as err_ex:
            print("text_area doesn't exist", err_ex)

    def delScroll(self):
        """ To delete ScrollBar """
        self.vsb.pack_forget()

    def addScroll(self):
        """ To add ScrollBar """
        try:
            exists = self.vsb.winfo_exists()
            if exists == 1:
                self.vsb.pack(side=tk.RIGHT, fill=tk.Y)
                print("Ok, ScrollBar exist")
        except Exception as err_scrl:
            print("Scrollbar doesn't exist", err_scrl)
            self.vsb.pack(side=tk.RIGHT, fill=tk.Y)

    def msgQuitapp(self, arg):
        """
            If usr want to quit, a question
            into a msgbox appear.
        """
        try:
            MsgBox = tk.messagebox.askyesno('Quit system', 'Do you want to quit ?')
            if MsgBox == 1:
                playsound('./beep_sounds/monitor.wav')
                self.master.destroy()
            else:
                playsound('./beep_sounds/loop79.mp3')
        except OSError as err_exit:
            print("[!] Error 2 : time to quit !!!", err_exit)

    def msgExit(self):
        """
            If usr want to quit, a question
            into a msgbox appear.
        """
        try:
            MsgBoxapp = tk.messagebox.askyesno('Quit system', 'Do you want to quit ?')
            if MsgBoxapp == 1:
                playsound('./beep_sounds/monitor.wav')
                self.master.destroy()
            else:
                playsound('./beep_sounds/loop79.mp3')
        except OSError as err_quit:
            print("[!] Error 3 : time to quit !!!", err_quit)

    def frameInfo(self):
        """
            Button info on intro (first page)
        """
        self.lab = tk.Tk()
        self.lab.title("ATCD")
        self.lab.configure(bg="grey22")
        self.lab.resizable(False, False)

        self.labFra = tk.LabelFrame(self.lab, text="\nWelcome !",
            font=("Arial 12"),fg='cyan', bg='grey22')
        self.labFra.pack(padx=5, pady=5)
        self.separator = tk.Frame(self.labFra, height=2, bd=1,
            relief=tk.SUNKEN)

        self.lab4 = tk.Label(self.labFra, text="\nInfo",
            font=('Times 16 bold'), fg='cyan', bg='grey22').pack()
        self.separator = tk.Frame(self.labFra, height=2, bd=1, relief=tk.SUNKEN)
        self.separator.pack(fill=tk.X, padx=100, pady=3)

        self.lab5 = tk.Label(self.labFra, justify=tk.LEFT, fg='cyan',
            bg='grey22', font=('Times', 14),
            text="\nMenu Bar, DB, Textbox and Residents are the most usefull skills\n"
            "to perform onto this app ! If you need help, you can go to Tutorial to\n"
            "understand how to use this app.\n\n"
            "Enjoy it !\n").pack(padx=10)
        self.separator = tk.Frame(self.labFra, height=2, bd=1, relief=tk.SUNKEN)
        self.separator.pack(fill=tk.X, padx=30, pady=3)
        self.lab6 = tk.Label(self.labFra, justify=tk.LEFT, fg='cyan',
            bg='grey22', font=('Times', 14),
            text="Path : Menu Bar --> Menu --> Tutorial").pack(padx=10, pady=10)

    def callPatient1(self):
        """
            Enter new patient (admission).
        """
        subprocess.Popen('./newpatient/entrypytientfile.py', shell=True)

    def delEverPat(self):
        """
            Delete patient who usr choose.
        """
        subprocess.Popen('./deletepatient/deleverything.py', shell=True)

    def addPatientAfter(self):
        """
            Add new patient after delete one of them before.
        """
        subprocess.Popen('./newpatient/torecord.py', shell=True)

    def patientAgenda(self, a):
        """
            Multiples possibilities with next cmd :
            self.master.withdraw()
            self.master.overrideredirect(True)
            self.master.deiconify()
            self.master.lift()
            self.master.focus_force()
        """
        if a == 1 :
            print("Patient n°", a)
            self.master.withdraw()
            subprocess.run('./patient_agenda/origin_agenda.py', check=True)
            self.master.deiconify()
        elif a == 2:
            print("Patient n° 2")
            self.master.withdraw()
            subprocess.run('./patient_agenda/origin_agenda2.py', check=True)
            self.master.deiconify()
        elif a == 3:
            print("Patient n° 3")
            self.master.withdraw()
            subprocess.run('./patient_agenda/origin_agenda3.py', check=True)
            self.master.deiconify()
        elif a == 4:
            print("Patient n° 4")
            self.master.withdraw()
            subprocess.run('./patient_agenda/origin_agenda4.py', check=True)
            self.master.deiconify()
        elif a == 5:
            print("Patient n° 5")
            self.master.withdraw()
            subprocess.run('./patient_agenda/origin_agenda5.py', check=True)
            self.master.deiconify()
        elif a == 6:
            print("Patient n° 6")
            self.master.withdraw()
            subprocess.run('./patient_agenda/origin_agenda6.py', check=True)
            self.master.deiconify()
        elif a == 7:
            print("Patient n° 7")
            self.master.withdraw()
            subprocess.run('./patient_agenda/origin_agenda7.py', check=True)
            self.master.deiconify()
        elif a == 8:
            print("Patient n° 8")
            self.master.withdraw()
            subprocess.run('./patient_agenda/origin_agenda8.py', check=True)
            self.master.deiconify()
        elif a == 9:
            print("Patient n° 9")
            self.master.withdraw()
            subprocess.run('./patient_agenda/origin_agenda9.py', check=True)
            self.master.deiconify()
        elif a == 10:
            print("Patient n° 10")
            self.master.withdraw()
            subprocess.run('./patient_agenda/origin_agenda10.py', check=True)
            self.master.deiconify()
        elif a == 11:
            print("Patient n° 11")
            self.master.withdraw()
            subprocess.run('./patient_agenda/origin_agenda11.py', check=True)
            self.master.deiconify()
        elif a == 12:
            print("Patient n° 12")
            self.master.withdraw()
            subprocess.run('./patient_agenda/origin_agenda12.py', check=True)
            self.master.deiconify()
        elif a == 13:
            print("Patient n° 13")
            self.master.withdraw()
            subprocess.run('./patient_agenda/origin_agenda13.py', check=True)
            self.master.deiconify()
        elif a == 14:
            print("Patient n° 14")
            self.master.withdraw()
            subprocess.run('./patient_agenda/origin_agenda14.py', check=True)
            self.master.deiconify()
        elif a == 15:
            print("Patient n° 15")
            self.master.withdraw()
            subprocess.run('./patient_agenda/origin_agenda15.py', check=True)
            self.master.deiconify()
        elif a == 16:
            print("Patient n° 16")
            self.master.withdraw()
            subprocess.run('./patient_agenda/origin_agenda16.py', check=True)
            self.master.deiconify()
        elif a == 17:
            print("Patient n° 17")
            self.master.withdraw()
            subprocess.run('./patient_agenda/origin_agenda17.py', check=True)
            self.master.deiconify()
        elif a == 18:
            print("Patient n° 18")
            self.master.withdraw()
            subprocess.run('./patient_agenda/origin_agenda18.py', check=True)
            self.master.deiconify()
        elif a == 18:
            print("Patient n° 18")
            self.master.withdraw()
            subprocess.run('./patient_agenda/origin_agenda18.py', check=True)
            self.master.deiconify()
        elif a == 19:
            print("Patient n° 19")
            self.master.withdraw()
            subprocess.run('./patient_agenda/origin_agenda19.py', check=True)
            self.master.deiconify()
        elif a == 20:
            print("Patient n° 20")
            self.master.withdraw()
            subprocess.run('./patient_agenda/origin_agenda20.py', check=True)
            self.master.deiconify()
        elif a == 21:
            print("Patient n° 21")
            self.master.withdraw()
            subprocess.run('./patient_agenda/origin_agenda21.py', check=True)
            self.master.deiconify()
        elif a == 22:
            print("Patient n° 22")
            self.master.withdraw()
            subprocess.run('./patient_agenda/origin_agenda22.py', check=True)
            self.master.deiconify()
        elif a == 23:
            print("Patient n° 23")
            self.master.withdraw()
            subprocess.run('./patient_agenda/origin_agenda23.py', check=True)
            self.master.deiconify()
        elif a == 24:
            print("Patient n° 24")
            self.master.withdraw()
            subprocess.run('./patient_agenda/origin_agenda24.py', check=True)
            self.master.deiconify()
        else:
            print("Nothing happened")
            tk.messagebox.showerror('Error', 'Something went wrong with : '\
            './patient_agenda/origin_agenda23.py ')

    # Contact patientX functions
    def contact_num1(self):
        """
            Opened since menu items
        """
        Window(self)

    def contactfamily_1(self):
        famWind(self)

    def contactdoctor_1(self):
        doctorWind(self)

    def contacthcsystem_1(self):
        homecsWind(self)

    # Contact patient 2
    def contact_num2(self):
        Window2(self)

    def contactfamily_2(self):
        famWind2(self)

    def contactdoctor_2(self):
        doctorWind2(self)

    def contacthcsystem_2(self):
        homecsWind2(self)

    # Contact patient 3
    def contact_num3(self):
        Window3(self)

    def contactfamily_3(self):
        famWind3(self)

    def contactdoctor_3(self):
        doctorWind3(self)

    def contacthcsystem_3(self):
        homecsWind3(self)

    # Contact patient 4
    def contact_num4(self):
        Window4(self)

    def contactfamily_4(self):
        famWind4(self)

    def contactdoctor_4(self):
        doctorWind4(self)

    def contacthcsystem_4(self):
        homecsWind4(self)

    # Contact patient 5
    def contact_num5(self):
        Window5(self)

    def contactfamily_5(self):
        famWind5(self)

    def contactdoctor_5(self):
        doctorWind5(self)

    def contacthcsystem_5(self):
        homecsWind5(self)

    # Contact patient 6
    def contact_num6(self):
        Window6(self)

    def contactfamily_6(self):
        famWind6(self)

    def contactdoctor_6(self):
        doctorWind6(self)

    def contacthcsystem_6(self):
        homecsWind6(self)

    # Contact patient 7
    def contact_num7(self):
        Window7(self)

    def contactfamily_7(self):
        famWind7(self)

    def contactdoctor_7(self):
        doctorWind7(self)

    def contacthcsystem_7(self):
        homecsWind7(self)

    # Contact patient 8
    def contact_num8(self):
        Window8(self)

    def contactfamily_8(self):
        famWind8(self)

    def contactdoctor_8(self):
        doctorWind8(self)

    def contacthcsystem_8(self):
        homecsWind8(self)

    # Contact patient 9
    def contact_num9(self):
        Window9(self)

    def contactfamily_9(self):
        famWind9(self)

    def contactdoctor_9(self):
        doctorWind9(self)

    def contacthcsystem_9(self):
        homecsWind9(self)

    # Contact patient 10
    def contact_num10(self):
        Window10(self)

    def contactfamily_10(self):
        famWind10(self)

    def contactdoctor_10(self):
        doctorWind10(self)

    def contacthcsystem_10(self):
        homecsWind10(self)

    # Contact patient 11
    def contact_num11(self):
        Window11(self)

    def contactfamily_11(self):
        famWind11(self)

    def contactdoctor_11(self):
        doctorWind11(self)

    def contacthcsystem_11(self):
        homecsWind11(self)

    # Contact patient 12
    def contact_num12(self):
        Window12(self)

    def contactfamily_12(self):
        famWind12(self)

    def contactdoctor_12(self):
        doctorWind12(self)

    def contacthcsystem_12(self):
        homecsWind12(self)

    # Contact patient 13
    def contact_num13(self):
        Window13(self)

    def contactfamily_13(self):
        famWind13(self)

    def contactdoctor_13(self):
        doctorWind13(self)

    def contacthcsystem_13(self):
        homecsWind13(self)

    # Contact patient 14
    def contact_num14(self):
        Window14(self)

    def contactfamily_14(self):
        famWind14(self)

    def contactdoctor_14(self):
        doctorWind14(self)

    def contacthcsystem_14(self):
        homecsWind14(self)

    # Contact patient 15
    def contact_num15(self):
        Window15(self)

    def contactfamily_15(self):
        famWind15(self)

    def contactdoctor_15(self):
        doctorWind15(self)

    def contacthcsystem_15(self):
        homecsWind15(self)

    # Contact patient 16
    def contact_num16(self):
        Window16(self)

    def contactfamily_16(self):
        famWind16(self)

    def contactdoctor_16(self):
        doctorWind16(self)

    def contacthcsystem_16(self):
        homecsWind16(self)

    # Contact patient 17
    def contact_num17(self):
        Window17(self)

    def contactfamily_17(self):
        famWind17(self)

    def contactdoctor_17(self):
        doctorWind17(self)

    def contacthcsystem_17(self):
        homecsWind17(self)

    # Contact patient 18
    def contact_num18(self):
        Window18(self)

    def contactfamily_18(self):
        famWind18(self)

    def contactdoctor_18(self):
        doctorWind18(self)

    def contacthcsystem_18(self):
        homecsWind18(self)

    # Contact patient 19
    def contact_num19(self):
        Window19(self)

    def contactfamily_19(self):
        famWind19(self)

    def contactdoctor_19(self):
        doctorWind19(self)

    def contacthcsystem_19(self):
        homecsWind19(self)

    # Contact patient 20
    def contact_num20(self):
        Window20(self)

    def contactfamily_20(self):
        famWind20(self)

    def contactdoctor_20(self):
        doctorWind20(self)

    def contacthcsystem_20(self):
        homecsWind20(self)

    # Contact patient 21
    def contact_num21(self):
        Window21(self)

    def contactfamily_21(self):
        famWind21(self)

    def contactdoctor_21(self):
        doctorWind21(self)

    def contacthcsystem_21(self):
        homecsWind21(self)

    # Contact patient 22
    def contact_num22(self):
        Window22(self)

    def contactfamily_22(self):
        famWind22(self)

    def contactdoctor_22(self):
        doctorWind22(self)

    def contacthcsystem_22(self):
        homecsWind22(self)

    # Contact patient 23
    def contact_num23(self):
        Window23(self)

    def contactfamily_23(self):
        famWind23(self)

    def contactdoctor_23(self):
        doctorWind23(self)

    def contacthcsystem_23(self):
        homecsWind23(self)

    # Contact patient 24
    def contact_num24(self):
        Window24(self)

    def contactfamily_24(self):
        famWind24(self)

    def contactdoctor_24(self):
        doctorWind24(self)

    def contacthcsystem_24(self):
        homecsWind24(self)

    # CheckBox 14 needs (functions)
    def besoinsCoche(self, b):
        """
            New window is open with
            subprocess.Popen()
        """
        if b == 1:
            subprocess.Popen('./need/checkb.py', shell=False)
        elif b == 2:
            subprocess.Popen('./need/checkb2.py', shell=False)
        elif b == 3:
            subprocess.Popen('./need/checkb3.py', shell=False)
        elif b == 4:
            subprocess.Popen('./need/checkb4.py', shell=False)
        elif b == 5:
            subprocess.Popen('./need/checkb5.py', shell=False)
        elif b == 6:
            subprocess.Popen('./need/checkb6.py', shell=False)
        elif b == 7:
            subprocess.Popen('./need/checkb7.py', shell=False)
        elif b == 8:
            subprocess.Popen('./need/checkb8.py', shell=False)
        elif b == 9:
            subprocess.Popen('./need/checkb9.py', shell=False)
        elif b == 10:
            subprocess.Popen('./need/checkb10.py', shell=False)
        elif b == 11:
            subprocess.Popen('./need/checkb11.py', shell=False)
        elif b == 12:
            subprocess.Popen('./need/checkb12.py', shell=False)
        elif b == 13:
            subprocess.Popen('./need/checkb13.py', shell=False)
        elif b == 14:
            subprocess.Popen('./need/checkb14.py', shell=False)
        elif b == 15:
            subprocess.Popen('./need/checkb15.py', shell=False)
        elif b == 16:
            subprocess.Popen('./need/checkb16.py', shell=False)
        elif b == 17:
            subprocess.Popen('./need/checkb17.py', shell=False)
        elif b == 18:
            subprocess.Popen('./need/checkb18.py', shell=False)
        elif b == 19:
            subprocess.Popen('./need/checkb19.py', shell=False)
        elif b == 20:
            subprocess.Popen('./need/checkb20.py', shell=False)
        elif b == 21:
            subprocess.Popen('./need/checkb21.py', shell=False)
        elif b == 22:
            subprocess.Popen('./need/checkb22.py', shell=False)
        elif b == 23:
            subprocess.Popen('./need/checkb23.py', shell=False)
        elif b == 24:
            subprocess.Popen('./need/checkb24.py', shell=False)
        else:
            print("[!] Error, No checkbox has been found !")

    def suiviSoins(self, s):
        """
            Call need's function.
            Hide background window and
            call script with subprocess.run()
        """
        if s == 1:
            needload1()
            self.master.withdraw()
            subprocess.run("./need/suivi_patient_1.py", check=True)
            self.master.deiconify()
        elif s == 2:
            needload2()
            self.master.withdraw()
            subprocess.run("./need/suivi_patient_2.py", check=True)
            self.master.deiconify()
        elif s == 3:
            needload3()
            self.master.withdraw()
            subprocess.run("./need/suivi_patient_3.py", check=True)
            self.master.deiconify()
        elif s == 4:
            needload4()
            self.master.withdraw()
            subprocess.run("./need/suivi_patient_4.py", check=True)
            self.master.deiconify()
        elif s == 5:
            needload5()
            self.master.withdraw()
            subprocess.run("./need/suivi_patient_5.py", check=True)
            self.master.deiconify()
        elif s == 6:
            needload6()
            self.master.withdraw()
            subprocess.run("./need/suivi_patient_6.py", check=True)
            self.master.deiconify()
        elif s == 7:
            needload7()
            self.master.withdraw()
            subprocess.run("./need/suivi_patient_7.py", check=True)
            self.master.deiconify()
        elif s == 8:
            needload8()
            self.master.withdraw()
            subprocess.run("./need/suivi_patient_8.py", check=True)
            self.master.deiconify()
        elif s == 9:
            needload9()
            self.master.withdraw()
            subprocess.run("./need/suivi_patient_9.py", check=True)
            self.master.deiconify()
        elif s == 10:
            needload10()
            self.master.withdraw()
            subprocess.run("./need/suivi_patient_10.py", check=True)
            self.master.deiconify()
        elif s == 11:
            needload11()
            self.master.withdraw()
            subprocess.run("./need/suivi_patient_11.py", check=True)
            self.master.deiconify()
        elif s == 12:
            needload12()
            self.master.withdraw()
            subprocess.run("./need/suivi_patient_12.py", check=True)
            self.master.deiconify()
        elif s == 13:
            needload13()
            self.master.withdraw()
            subprocess.run("./need/suivi_patient_13.py", check=True)
            self.master.deiconify()
        elif s == 14:
            needload14()
            self.master.withdraw()
            subprocess.run("./need/suivi_patient_14.py", check=True)
            self.master.deiconify()
        elif s == 15:
            needload15()
            self.master.withdraw()
            subprocess.run("./need/suivi_patient_15.py", check=True)
            self.master.deiconify()
        elif s == 16:
            needload16()
            self.master.withdraw()
            subprocess.run("./need/suivi_patient_16.py", check=True)
            self.master.deiconify()
        elif s == 17:
            needload17()
            self.master.withdraw()
            subprocess.run("./need/suivi_patient_17.py", check=True)
            self.master.deiconify()
        elif s == 18:
            needload18()
            self.master.withdraw()
            subprocess.run("./need/suivi_patient_18.py", check=True)
            self.master.deiconify()
        elif s == 19:
            needload19()
            self.master.withdraw()
            subprocess.run("./need/suivi_patient_19.py", check=True)
            self.master.deiconify()
        elif s == 20:
            needload20()
            self.master.withdraw()
            subprocess.run("./need/suivi_patient_20.py", check=True)
            self.master.deiconify()
        elif s == 21:
            needload21()
            self.master.withdraw()
            subprocess.run("./need/suivi_patient_21.py", check=True)
            self.master.deiconify()
        elif s == 22:
            needload22()
            self.master.withdraw()
            subprocess.run("./need/suivi_patient_22.py", check=True)
            self.master.deiconify()
        elif s == 23:
            needload23()
            self.master.withdraw()
            subprocess.run("./need/suivi_patient_23.py", check=True)
            self.master.deiconify()
        elif s == 24:
            needload24()
            self.master.withdraw()
            subprocess.run("./need/suivi_patient_24.py", check=True)
            self.master.deiconify()
        else:
            print("[!] Error, to call ./need/suivi_patient_X.py with subprocess")

    def showParam(self, p):
        """
            Decreases the opacity of
            the background window
            and run subprocess.run()
            to call Vital Parameters.
            self.master.wm_attributes('-alpha', 0.8)
            self.master.update()
            cmd()
            self.master.wm_attributes('-alpha', 1.0)
            self.master.update()
        """
        if p == 1:
            subprocess.Popen("./param/fencap.py", shell=False)
        elif p == 2:
            subprocess.Popen("./param/fencap2.py", shell=False)
        elif p == 3:
            subprocess.Popen("./param/fencap3.py", shell=False)
        elif p == 4:
            subprocess.Popen("./param/fencap4.py", shell=False)
        elif p == 5:
            subprocess.Popen("./param/fencap5.py", shell=False)
        elif p == 6:
            subprocess.Popen("./param/fencap6.py", shell=False)
        elif p == 7:
            subprocess.Popen("./param/fencap7.py", shell=False)
        elif p == 8:
            subprocess.Popen("./param/fencap8.py", shell=False)
        elif p == 9:
            subprocess.Popen("./param/fencap9.py", shell=False)
        elif p == 10:
            subprocess.Popen("./param/fencap10.py", shell=False)
        elif p == 11:
            subprocess.Popen("./param/fencap11.py", shell=False)
        elif p == 12:
            subprocess.Popen("./param/fencap12.py", shell=False)
        elif p == 13:
            subprocess.Popen("./param/fencap13.py", shell=False)
        elif p == 14:
            subprocess.Popen("./param/fencap14.py", shell=False)
        elif p == 15:
            subprocess.Popen("./param/fencap15.py", shell=False)
        elif p == 16:
            subprocess.Popen("./param/fencap16.py", shell=False)
        elif p == 17:
            subprocess.Popen("./param/fencap17.py", shell=False)
        elif p == 18:
            subprocess.Popen("./param/fencap18.py", shell=False)
        elif p == 19:
            subprocess.Popen("./param/fencap19.py", shell=False)
        elif p == 20:
            subprocess.Popen("./param/fencap20.py", shell=False)
        elif p == 21:
            subprocess.Popen("./param/fencap21.py", shell=False)
        elif p == 22:
            subprocess.Popen("./param/fencap22.py", shell=False)
        elif p == 23:
            subprocess.Popen("./param/fencap23.py", shell=False)
        elif p == 24:
            subprocess.Popen("./param/fencap24.py", shell=False)
        else:
            print("Errro, to call ./param/fencapX.py with subprocess")

    def calculB(self, u):
        """
            Decreases opacity of background window
            during script CalculBmiX.py is running.
            Call a BMI frame.
            self.master.wm_attributes('-alpha', 0.8)
            self.master.update()
            self.master.wm_attributes('-alpha', 1.0)
            self.master.update()
        """
        if u == 1:
            subprocess.Popen("./calBmi/CalculBmi.py", shell=False)
        elif u == 2:
            subprocess.Popen("./calBmi/CalculBmi2.py", shell=False)
        elif u == 3:
            subprocess.Popen("./calBmi/CalculBmi3.py", shell=False)
        elif u == 4:
            subprocess.Popen("./calBmi/CalculBmi4.py", shell=False)
        elif u == 5:
            subprocess.Popen("./calBmi/CalculBmi5.py", shell=False)
        elif u == 6:
            subprocess.Popen("./calBmi/CalculBmi6.py", shell=False)
        elif u == 7:
            subprocess.Popen("./calBmi/CalculBmi7.py", shell=False)
        elif u == 8:
            subprocess.Popen("./calBmi/CalculBmi8.py", shell=False)
        elif u == 9:
            subprocess.Popen("./calBmi/CalculBmi9.py", shell=False)
        elif u == 10:
            subprocess.Popen("./calBmi/CalculBmi10.py", shell=False)
        elif u == 11:
            subprocess.Popen("./calBmi/CalculBmi11.py", shell=False)
        elif u == 12:
            subprocess.Popen("./calBmi/CalculBmi12.py", shell=False)
        elif u == 13:
            subprocess.Popen("./calBmi/CalculBmi13.py", shell=False)
        elif u == 14:
            subprocess.Popen("./calBmi/CalculBmi14.py", shell=False)
        elif u == 15:
            subprocess.Popen("./calBmi/CalculBmi15.py", shell=False)
        elif u == 16:
            subprocess.Popen("./calBmi/CalculBmi16.py", shell=False)
        elif u == 17:
            subprocess.Popen("./calBmi/CalculBmi17.py", shell=False)
        elif u == 18:
            subprocess.Popen("./calBmi/CalculBmi18.py", shell=False)
        elif u == 19:
            subprocess.Popen("./calBmi/CalculBmi19.py", shell=False)
        elif u == 20:
            subprocess.Popen("./calBmi/CalculBmi20.py", shell=False)
        elif u == 21:
            subprocess.Popen("./calBmi/CalculBmi21.py", shell=False)
        elif u == 22:
            subprocess.Popen("./calBmi/CalculBmi22.py", shell=False)
        elif u == 23:
            subprocess.Popen("./calBmi/CalculBmi23.py", shell=False)
        elif u == 24:
            subprocess.Popen("./calBmi/CalculBmi24.py", shell=False)
        else:
            print("[!] Error, to call ./calBmi/CalculBmiX.py with subprocess.")

    def visitMed(self):
        """
            Hide the background window
            during vm_patient.py script
            is running
        """
        medownload1()
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient1.py", check=True)
        self.master.deiconify()
    def visitMed2(self):
        medownload2()
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient2.py", check=True)
        self.master.deiconify()
    def visitMed3(self):
        medownload3()
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient3.py", check=True)
        self.master.deiconify()
    def visitMed4(self):
        medownload4()
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient4.py", check=True)
        self.master.deiconify()
    def visitMed5(self):
        medownload5()
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient5.py", check=True)
        self.master.deiconify()
    def visitMed6(self):
        medownload6()
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient6.py", check=True)
        self.master.deiconify()
    def visitMed7(self):
        medownload7()
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient7.py", check=True)
        self.master.deiconify()
    def visitMed8(self):
        medownload8()
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient8.py", check=True)
        self.master.deiconify()
    def visitMed9(self):
        medownload9()
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient9.py", check=True)
        self.master.deiconify()
    def visitMed10(self):
        medownload10()
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient10.py", check=True)
        self.master.deiconify()
    def visitMed11(self):
        medownload11()
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient11.py", check=True)
        self.master.deiconify()
    def visitMed12(self):
        medownload12()
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient12.py", check=True)
        self.master.deiconify()
    def visitMed13(self):
        medownload13()
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient13.py", check=True)
        self.master.deiconify()
    def visitMed14(self):
        medownload14()
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient14.py", check=True)
        self.master.deiconify()
    def visitMed15(self):
        medownload15()
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient15.py", check=True)
        self.master.deiconify()
    def visitMed16(self):
        medownload16()
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient16.py", check=True)
        self.master.deiconify()
    def visitMed17(self):
        medownload17()
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient17.py", check=True)
        self.master.deiconify()
    def visitMed18(self):
        medownload18()
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient18.py", check=True)
        self.master.deiconify()
    def visitMed19(self):
        medownload19()
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient19.py", check=True)
        self.master.deiconify()
    def visitMed20(self):
        medownload20()
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient20.py", check=True)
        self.master.deiconify()
    def visitMed21(self):
        medownload21()
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient21.py", check=True)
        self.master.deiconify()
    def visitMed22(self):
        medownload22()
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient22.py", check=True)
        self.master.deiconify()
    def visitMed23(self):
        medownload23()
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient23.py", check=True)
        self.master.deiconify()
    def visitMed24(self):
        medownload24()
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient24.py", check=True)
        self.master.deiconify()

    def nutritionMenu(self, n):
        """
            Hide the background window
            during nutrit_patient script
            is running
        """
        if n == 1:
            self.master.withdraw()
            subprocess.run('./nutrition/nutrit_patient1.py', check=True)
            self.master.deiconify()
        elif n == 2:
            self.master.withdraw()
            subprocess.run('./nutrition/nutrit_patient2.py', check=True)
            self.master.deiconify()
        elif n == 3:
            self.master.withdraw()
            subprocess.run('./nutrition/nutrit_patient3.py', check=True)
            self.master.deiconify()
        elif n == 4:
            self.master.withdraw()
            subprocess.run('./nutrition/nutrit_patient4.py', check=True)
            self.master.deiconify()
        elif n == 5:
            self.master.withdraw()
            subprocess.run('./nutrition/nutrit_patient5.py', check=True)
            self.master.deiconify()
        elif n == 6:
            self.master.withdraw()
            subprocess.run('./nutrition/nutrit_patient6.py', check=True)
            self.master.deiconify()
        elif n == 7:
            self.master.withdraw()
            subprocess.run('./nutrition/nutrit_patient7.py', check=True)
            self.master.deiconify()
        elif n == 8:
            self.master.withdraw()
            subprocess.run('./nutrition/nutrit_patient8.py', check=True)
            self.master.deiconify()
        elif n == 9:
            self.master.withdraw()
            subprocess.run('./nutrition/nutrit_patient9.py', check=True)
            self.master.deiconify()
        elif n == 10:
            self.master.withdraw()
            subprocess.run('./nutrition/nutrit_patient10.py', check=True)
            self.master.deiconify()
        elif n == 11:
            self.master.withdraw()
            subprocess.run('./nutrition/nutrit_patient11.py', check=True)
            self.master.deiconify()
        elif n == 12:
            self.master.withdraw()
            subprocess.run('./nutrition/nutrit_patient12.py', check=True)
            self.master.deiconify()
        elif n == 13:
            self.master.withdraw()
            subprocess.run('./nutrition/nutrit_patient13.py', check=True)
            self.master.deiconify()
        elif n == 14:
            self.master.withdraw()
            subprocess.run('./nutrition/nutrit_patient14.py', check=True)
            self.master.deiconify()
        elif n == 15:
            self.master.withdraw()
            subprocess.run('./nutrition/nutrit_patient15.py', check=True)
            self.master.deiconify()
        elif n == 16:
            self.master.withdraw()
            subprocess.run('./nutrition/nutrit_patient16.py', check=True)
            self.master.deiconify()
        elif n == 17:
            self.master.withdraw()
            subprocess.run('./nutrition/nutrit_patient17.py', check=True)
            self.master.deiconify()
        elif n == 18:
            self.master.withdraw()
            subprocess.run('./nutrition/nutrit_patient18.py', check=True)
            self.master.deiconify()
        elif n == 19:
            self.master.withdraw()
            subprocess.run('./nutrition/nutrit_patient19.py', check=True)
            self.master.deiconify()
        elif n == 20:
            self.master.withdraw()
            subprocess.run('./nutrition/nutrit_patient20.py', check=True)
            self.master.deiconify()
        elif n == 21:
            self.master.withdraw()
            subprocess.run('./nutrition/nutrit_patient21.py', check=True)
            self.master.deiconify()
        elif n == 22:
            self.master.withdraw()
            subprocess.run('./nutrition/nutrit_patient22.py', check=True)
            self.master.deiconify()
        elif n == 23:
            self.master.withdraw()
            subprocess.run('./nutrition/nutrit_patient23.py', check=True)
            self.master.deiconify()
        elif n == 24:
            self.master.withdraw()
            subprocess.run('./nutrition/nutrit_patient24.py', check=True)
            self.master.deiconify()
        else:
            print("[!] Error to call ./nutrition/nutrit_patient24.py with subprocess.")

    def manualFile(self):
        """
            To consult TXT and PDF
            files (manual)
        """
        self.master.withdraw()
        subprocess.run('./manual/pdfopenmanual.py', check=True)
        self.master.deiconify()

    def allFilesBackup(self, f):
        """
            To acces files into Backup folder
        """
        if f == 1:
            self.master.wm_attributes('-alpha', 0.8)
            self.master.update()
            backupFuncPatient(self)
            self.master.wm_attributes('-alpha', 1.0)
            self.master.update()
        elif f == 2:
            self.master.wm_attributes('-alpha', 0.8)
            self.master.update()
            backupFuncPatient2(self)
            self.master.wm_attributes('-alpha', 1.0)
            self.master.update()
        elif f == 2:
            self.master.wm_attributes('-alpha', 0.8)
            self.master.update()
            backupFuncPatient3(self)
            self.master.wm_attributes('-alpha', 1.0)
            self.master.update()
        elif f == 2:
            self.master.wm_attributes('-alpha', 0.8)
            self.master.update()
            backupFuncPatient4(self)
            self.master.wm_attributes('-alpha', 1.0)
            self.master.update()
        elif f == 2:
            self.master.wm_attributes('-alpha', 0.8)
            self.master.update()
            backupFuncPatient5(self)
            self.master.wm_attributes('-alpha', 1.0)
            self.master.update()
        elif f == 2:
            self.master.wm_attributes('-alpha', 0.8)
            self.master.update()
            backupFuncPatient6(self)
            self.master.wm_attributes('-alpha', 1.0)
            self.master.update()
        elif f == 2:
            self.master.wm_attributes('-alpha', 0.8)
            self.master.update()
            backupFuncPatient7(self)
            self.master.wm_attributes('-alpha', 1.0)
            self.master.update()
        elif f == 2:
            self.master.wm_attributes('-alpha', 0.8)
            self.master.update()
            backupFuncPatient8(self)
            self.master.wm_attributes('-alpha', 1.0)
            self.master.update()
        elif f == 2:
            self.master.wm_attributes('-alpha', 0.8)
            self.master.update()
            backupFuncPatient9(self)
            self.master.wm_attributes('-alpha', 1.0)
            self.master.update()
        elif f == 2:
            self.master.wm_attributes('-alpha', 0.8)
            self.master.update()
            backupFuncPatient10(self)
            self.master.wm_attributes('-alpha', 1.0)
            self.master.update()
        elif f == 2:
            self.master.wm_attributes('-alpha', 0.8)
            self.master.update()
            backupFuncPatient11(self)
            self.master.wm_attributes('-alpha', 1.0)
            self.master.update()
        elif f == 2:
            self.master.wm_attributes('-alpha', 0.8)
            self.master.update()
            backupFuncPatient12(self)
            self.master.wm_attributes('-alpha', 1.0)
            self.master.update()
        elif f == 2:
            self.master.wm_attributes('-alpha', 0.8)
            self.master.update()
            backupFuncPatient13(self)
            self.master.wm_attributes('-alpha', 1.0)
            self.master.update()
        elif f == 2:
            self.master.wm_attributes('-alpha', 0.8)
            self.master.update()
            backupFuncPatient14(self)
            self.master.wm_attributes('-alpha', 1.0)
            self.master.update()
        elif f == 2:
            self.master.wm_attributes('-alpha', 0.8)
            self.master.update()
            backupFuncPatient15(self)
            self.master.wm_attributes('-alpha', 1.0)
            self.master.update()
        elif f == 2:
            self.master.wm_attributes('-alpha', 0.8)
            self.master.update()
            backupFuncPatient16(self)
            self.master.wm_attributes('-alpha', 1.0)
            self.master.update()
        elif f == 2:
            self.master.wm_attributes('-alpha', 0.8)
            self.master.update()
            backupFuncPatient17(self)
            self.master.wm_attributes('-alpha', 1.0)
            self.master.update()
        elif f == 2:
            self.master.wm_attributes('-alpha', 0.8)
            self.master.update()
            backupFuncPatient18(self)
            self.master.wm_attributes('-alpha', 1.0)
            self.master.update()
        elif f == 2:
            self.master.wm_attributes('-alpha', 0.8)
            self.master.update()
            backupFuncPatient19(self)
            self.master.wm_attributes('-alpha', 1.0)
            self.master.update()
        elif f == 2:
            self.master.wm_attributes('-alpha', 0.8)
            self.master.update()
            backupFuncPatient20(self)
            self.master.wm_attributes('-alpha', 1.0)
            self.master.update()
        elif f == 2:
            self.master.wm_attributes('-alpha', 0.8)
            self.master.update()
            backupFuncPatient21(self)
            self.master.wm_attributes('-alpha', 1.0)
            self.master.update()
        elif f == 2:
            self.master.wm_attributes('-alpha', 0.8)
            self.master.update()
            backupFuncPatient22(self)
            self.master.wm_attributes('-alpha', 1.0)
            self.master.update()
        elif f == 2:
            self.master.wm_attributes('-alpha', 0.8)
            self.master.update()
            backupFuncPatient23(self)
            self.master.wm_attributes('-alpha', 1.0)
            self.master.update()
        elif f == 2:
            self.master.wm_attributes('-alpha', 0.8)
            self.master.update()
            backupFuncPatient24(self)
            self.master.wm_attributes('-alpha', 1.0)
            self.master.update()
        else:
            print("[!] Error - maybe no backup maide !")

    def updateFiletxt(self):
        """
            It's time to backup !
            This function is called
            from boxapp.py (line 22)
            dataBackToSave(self) --> Backup/backupfile.py
            paramBackToSave(self) -- > param/backup_month.py
            bmiBackToSave(self) --> calBmi_backup.py
        """
        dataBackToSave(self)
        paramBackToSave(self)
        bmiBackToSave(self)

    def upDateAll(self):
        """
            To reset app by pressing
            refresh button. Close,
            open directly and update
            data from patcaps.py !
        """
        try:
            if self._job is not None:
                self.clock_label.after_cancel(self._job)
                self._job = None
                self.master.destroy()
                Application.__init__(self)
                self.showPatients()
        except (OSError, ValueError) as p_out:
            print("[!] Error with refresh...", p_out)

if __name__=='__main__':
    root = tk.Tk()
    root.resizable(False, False)
    Application(root).pack()
    root.mainloop()
