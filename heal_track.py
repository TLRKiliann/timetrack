#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
    Main script to start the application.
    It call directly intro.py to validate
    access privileges.
"""


import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import scrolledtext
import os
import sys
import platform
import subprocess
import time
import json
from playsound import playsound

import starter.intro
from mainmod.boxapp import callBox
from mainmod.reminder import alarmThread
from mainmod.manualapp import instalpy
from mainmod.patcaps import callResident
from mainmod.backapp import *
from Backup.backupfile import dataBackToSave
from extensions.agenda_extension import extendAgenda
from extensions.case_extended import checkcaseExtend 
from extensions.health_ext import extendHealth
from extensions.param_extended import parameters
from param.backup_month import paramBackToSave
from calBmi.bmi_backup import bmiBackToSave
from extensions.bmi_extended import bmicalkilo
from extensions.medvisit_extended import medicalVisit
from extensions.nutri_extended import nutritionExtend
from extensions.overview import overviewExtend
from contact.patconfunc import callPatNum
from contact.famconfunc import callFamWind
from contact.doctorconfunc import callDoctorWind
from contact.homeconfunc import callHomecsWind


class ScrollCanvas(tk.Frame):
    """
        To prepare ScrollBar for main application.
    """
    def __init__(self, boss=None):
        tk.Frame.__init__(self, borderwidth=borderwidth, relief=relief)

        self.can = tk.Canvas(self, width=width, height=height, bd=bd, relief=relief)
        self.viewPort = tk.Frame(self.can)

        self.vsb = tk.Scrollbar(self, orient=tk.VERTICAL, command=self.can.yview)
        self.can.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(side=tk.RIGHT, fill=tk.Y)
        self.can.pack(side=tk.LEFT, fill=tk.BOTH, expand=1) 

        self.canvas_window = self.can.create_window((4,4), window=self.viewPort,
            anchor=tk.NW, tags="self.viewPort")

        self.viewPort.bind("<Configure>", self.onFrameConfigure)
        self.can.bind("<Configure>", self.onCanvasConfigure)

        self.viewPort.bind('<Enter>', self.onEnter)
        self.viewPort.bind('<Leave>', self.onLeave)

        self.onFrameConfigure(None)

class MenuBar(tk.Frame):
    """
        Wrapp down
    """
    def __init__(self, boss=None):
        tk.Frame.__init__(self, borderwidth=5, bg='RoyalBlue3', padx=0)

        fileMenu = tk.Menubutton(self, text='Menu', fg='white',
            font=('Times', 14), bg='grey30', relief=tk.GROOVE)

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
            command=lambda: boss.contact_num(h=1))
        me1.add_command(label='Relation - Family', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contactfamily(j=1))
        me1.add_command(label="Doctors' Data", font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contactdoctor(k=1))
        me1.add_command(label='Home care system', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contacthcsystem(l=1))
        contchck.add_cascade(label=new_text, underline=0, font=('Times 14'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me1)
        me2 = Menu(contchck)
        me2.add_command(label='Patient Data', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contact_num(h=2))
        me2.add_command(label='Relation - Family', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contactfamily(j=2))
        me2.add_command(label="Doctors' Data", font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contactdoctor(k=2))
        me2.add_command(label='Home care system', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contacthcsystem(l=2))
        contchck.add_cascade(label=new_text2, underline=0, font=('Times 14'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me2)
        me3 = Menu(contchck)
        me3.add_command(label='Patient Data', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contact_num(h=3))
        me3.add_command(label='Relation - Family', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contactfamily(j=3))
        me3.add_command(label="Doctors' Data", font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contactdoctor(k=3))
        me3.add_command(label='Home care system', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contacthcsystem(l=3))
        contchck.add_cascade(label=new_text3, underline=0, font=('Times 14'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me3)
        me4 = Menu(contchck)
        me4.add_command(label='Patient Data', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contact_num(h=4))
        me4.add_command(label='Relation - Family', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contactfamily(j=4))
        me4.add_command(label="Doctors' Data", font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contactdoctor(k=4))
        me4.add_command(label='Home care system', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contacthcsystem(l=4))
        contchck.add_cascade(label=new_text4, underline=0, font=('Times 14'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me4)
        me5 = Menu(contchck)
        me5.add_command(label='Patient Data', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contact_num(h=5))
        me5.add_command(label='Relation - Family', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contactfamily(j=5))
        me5.add_command(label="Doctors' Data", font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contactdoctor(k=5))
        me5.add_command(label='Home care system', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contacthcsystem(l=5))
        contchck.add_cascade(label=new_text5, underline=0, font=('Times 14'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me5)
        me6 = Menu(contchck)
        me6.add_command(label='Patient Data', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contact_num(h=6))
        me6.add_command(label='Relation - Family', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contactfamily(j=6))
        me6.add_command(label="Doctors' Data", font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contactdoctor(k=6))
        me6.add_command(label='Home care system', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contacthcsystem(l=6))
        contchck.add_cascade(label=new_text6, underline=0, font=('Times 14'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me6)
        me7 = Menu(contchck)
        me7.add_command(label='Patient Data', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contact_num(h=7))
        me7.add_command(label='Relation - Family', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contactfamily(j=7))
        me7.add_command(label="Doctors' Data", font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contactdoctor(k=7))
        me7.add_command(label='Home care system', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contacthcsystem(l=7))
        contchck.add_cascade(label=new_text7, underline=0, font=('Times 14'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me7)
        me8 = Menu(contchck)
        me8.add_command(label='Patient Data', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contact_num(h=8))
        me8.add_command(label='Relation - Family', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contactfamily(j=8))
        me8.add_command(label="Doctors' Data", font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contactdoctor(k=8))
        me8.add_command(label='Home care system', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contacthcsystem(l=8))
        contchck.add_cascade(label=new_text8, underline=0, font=('Times 14'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me8)
        me9 = Menu(contchck)
        me9.add_command(label='Patient Data', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contact_num(h=9))
        me9.add_command(label='Relation - Family', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contactfamily(j=9))
        me9.add_command(label="Doctors' Data", font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contactdoctor(k=9))
        me9.add_command(label='Home care system', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contacthcsystem(l=9))
        contchck.add_cascade(label=new_text9, underline=0, font=('Times 14'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me9)
        me10 = Menu(contchck)
        me10.add_command(label='Patient Data', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contact_num(h=10))
        me10.add_command(label='Relation - Family', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contactfamily(j=10))
        me10.add_command(label="Doctors' Data", font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contactdoctor(k=10))
        me10.add_command(label='Home care system', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contacthcsystem(l=10))
        contchck.add_cascade(label=new_text10, underline=0, font=('Times 14'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me10)
        me11 = Menu(contchck)
        me11.add_command(label='Patient Data', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contact_num(h=11))
        me11.add_command(label='Relation - Family', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contactfamily(j=11))
        me11.add_command(label="Doctors' Data", font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contactdoctor(k=11))
        me11.add_command(label='Home care system', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contacthcsystem(l=11))
        contchck.add_cascade(label=new_text11, underline=0, font=('Times 14'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me11)
        me12 = Menu(contchck)
        me12.add_command(label='Patient Data', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contact_num(h=12))
        me12.add_command(label='Relation - Family', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contactfamily(j=12))
        me12.add_command(label="Doctors' Data", font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contactdoctor(k=12))
        me12.add_command(label='Home care system', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contacthcsystem(l=12))
        contchck.add_cascade(label=new_text12, underline=0, font=('Times 14'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me12)
        me13 = Menu(contchck)
        me13.add_command(label='Patient Data', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contact_num(h=13))
        me13.add_command(label='Relation - Family', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contactfamily(j=13))
        me13.add_command(label="Doctors' Data", font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contactdoctor(k=13))
        me13.add_command(label='Home care system', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contacthcsystem(l=13))
        contchck.add_cascade(label=new_text13, underline=0, font=('Times 14'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me13)
        me14 = Menu(contchck)
        me14.add_command(label='Patient Data', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contact_num(h=14))
        me14.add_command(label='Relation - Family', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contactfamily(j=14))
        me14.add_command(label="Doctors' Data", font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contactdoctor(k=14))
        me14.add_command(label='Home care system', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contacthcsystem(l=14))
        contchck.add_cascade(label=new_text14, underline=0, font=('Times 14'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me14)
        me15 = Menu(contchck)
        me15.add_command(label='Patient Data', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contact_num(h=15))
        me15.add_command(label='Relation - Family', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contactfamily(j=15))
        me15.add_command(label="Doctors' Data", font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contactdoctor(k=15))
        me15.add_command(label='Home care system', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contacthcsystem(l=15))
        contchck.add_cascade(label=new_text15, underline=0, font=('Times 14'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me15)
        me16 = Menu(contchck)
        me16.add_command(label='Patient Data', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contact_num(h=16))
        me16.add_command(label='Relation - Family', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contactfamily(j=16))
        me16.add_command(label="Doctors' Data", font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contactdoctor(k=16))
        me16.add_command(label='Home care system', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contacthcsystem(l=16))
        contchck.add_cascade(label=new_text16, underline=0, font=('Times 14'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me16)
        me17 = Menu(contchck)
        me17.add_command(label='Patient Data', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contact_num(h=17))
        me17.add_command(label='Relation - Family', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contactfamily(j=17))
        me17.add_command(label="Doctors' Data", font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contactdoctor(k=17))
        me17.add_command(label='Home care system', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contacthcsystem(l=17))
        contchck.add_cascade(label=new_text17, underline=0, font=('Times 14'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me17)
        me18 = Menu(contchck)
        me18.add_command(label='Patient Data', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contact_num(h=18))
        me18.add_command(label='Relation - Family', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contactfamily(j=18))
        me18.add_command(label="Doctors' Data", font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contactdoctor(k=18))
        me18.add_command(label='Home care system', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contacthcsystem(l=18))
        contchck.add_cascade(label=new_text18, underline=0, font=('Times 14'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me18)
        me19 = Menu(contchck)
        me19.add_command(label='Patient Data', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contact_num(h=19))
        me19.add_command(label='Relation - Family', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contactfamily(j=19))
        me19.add_command(label="Doctors' Data", font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contactdoctor(k=19))
        me19.add_command(label='Home care system', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contacthcsystem(l=19))
        contchck.add_cascade(label=new_text19, underline=0, font=('Times 14'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me19)
        me20 = Menu(contchck)
        me20.add_command(label='Patient Data', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contact_num(h=20))
        me20.add_command(label='Relation - Family', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contactfamily(j=20))
        me20.add_command(label="Doctors' Data", font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contactdoctor(k=20))
        me20.add_command(label='Home care system', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contacthcsystem(l=20))
        contchck.add_cascade(label=new_text20, underline=0, font=('Times 14'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me20)
        me21 = Menu(contchck)
        me21.add_command(label='Patient Data', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contact_num(h=21))
        me21.add_command(label='Relation - Family', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contactfamily(j=21))
        me21.add_command(label="Doctors' Data", font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contactdoctor(k=21))
        me21.add_command(label='Home care system', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contacthcsystem(l=21))
        contchck.add_cascade(label=new_text21, underline=0, font=('Times 14'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me21)
        me22 = Menu(contchck)
        me22.add_command(label='Patient Data', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contact_num(h=22))
        me22.add_command(label='Relation - Family', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contactfamily(j=22))
        me22.add_command(label="Doctors' Data", font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contactdoctor(k=22))
        me22.add_command(label='Home care system', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contacthcsystem(l=22))
        contchck.add_cascade(label=new_text22, underline=0, font=('Times 14'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me22)
        me23 = Menu(contchck)
        me23.add_command(label='Patient Data', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contact_num(h=23))
        me23.add_command(label='Relation - Family', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contactfamily(j=23))
        me23.add_command(label="Doctors' Data", font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contactdoctor(k=23))
        me23.add_command(label='Home care system', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contacthcsystem(l=23))
        contchck.add_cascade(label=new_text23, underline=0, font=('Times 14'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me23)
        me24 = Menu(contchck)
        me24.add_command(label='Patient Data', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contact_num(h=24))
        me24.add_command(label='Relation - Family', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contactfamily(j=24))
        me24.add_command(label="Doctors' Data", font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contactdoctor(k=24))
        me24.add_command(label='Home care system', font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.contacthcsystem(l=24))
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
            command=lambda: boss.bmikilo(u=1))
        meBmi.add_command(label=new_text2, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.bmikilo(u=2))
        meBmi.add_command(label=new_text3, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.bmikilo(u=3))
        meBmi.add_command(label=new_text4, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.bmikilo(u=4))
        meBmi.add_command(label=new_text5, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.bmikilo(u=5))
        meBmi.add_command(label=new_text6, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.bmikilo(u=6))
        meBmi.add_command(label=new_text7, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.bmikilo(u=7))
        meBmi.add_command(label=new_text8, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.bmikilo(u=8))
        meBmi.add_command(label=new_text9, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.bmikilo(u=9))
        meBmi.add_command(label=new_text10, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.bmikilo(u=10))
        meBmi.add_command(label=new_text11, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.bmikilo(u=11))
        meBmi.add_command(label=new_text12, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.bmikilo(u=12))
        meBmi.add_command(label=new_text13, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.bmikilo(u=13))
        meBmi.add_command(label=new_text14, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.bmikilo(u=14))
        meBmi.add_command(label=new_text15, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.bmikilo(u=15))
        meBmi.add_command(label=new_text16, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.bmikilo(u=16))
        meBmi.add_command(label=new_text17, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.bmikilo(u=17))
        meBmi.add_command(label=new_text18, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.bmikilo(u=18))
        meBmi.add_command(label=new_text19, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.bmikilo(u=19))
        meBmi.add_command(label=new_text20, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.bmikilo(u=20))
        meBmi.add_command(label=new_text21, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.bmikilo(u=21))
        meBmi.add_command(label=new_text22, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.bmikilo(u=22))
        meBmi.add_command(label=new_text23, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.bmikilo(u=23))
        meBmi.add_command(label=new_text24, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.bmikilo(u=24))
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
            command=lambda: boss.visitMed(t=1))
        meVmed.add_command(label=new_text2, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.visitMed(t=2))
        meVmed.add_command(label=new_text3, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.visitMed(t=3))
        meVmed.add_command(label=new_text4, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.visitMed(t=4))
        meVmed.add_command(label=new_text5, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.visitMed(t=5))
        meVmed.add_command(label=new_text6, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.visitMed(t=6))
        meVmed.add_command(label=new_text7, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.visitMed(t=7))
        meVmed.add_command(label=new_text8, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.visitMed(t=8))
        meVmed.add_command(label=new_text9, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.visitMed(t=9))
        meVmed.add_command(label=new_text10, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.visitMed(t=10))
        meVmed.add_command(label=new_text11, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.visitMed(t=11))
        meVmed.add_command(label=new_text12, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.visitMed(t=12))
        meVmed.add_command(label=new_text13, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.visitMed(t=13))
        meVmed.add_command(label=new_text14, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.visitMed(t=14))
        meVmed.add_command(label=new_text15, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.visitMed(t=15))
        meVmed.add_command(label=new_text16, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.visitMed(t=16))
        meVmed.add_command(label=new_text17, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.visitMed(t=17))
        meVmed.add_command(label=new_text18, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.visitMed(t=18))
        meVmed.add_command(label=new_text19, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.visitMed(t=19))
        meVmed.add_command(label=new_text20, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.visitMed(t=20))
        meVmed.add_command(label=new_text21, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.visitMed(t=21))
        meVmed.add_command(label=new_text22, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.visitMed(t=22))
        meVmed.add_command(label=new_text23, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.visitMed(t=23))
        meVmed.add_command(label=new_text24, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=lambda: boss.visitMed(t=24))
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
        self.master.tk.call('wm', 'iconphoto', self.master._w, tk.PhotoImage(file='./syno_gif/YoRHa2.gif'))
        self.master.title('Time-Track Developed by ko@l@tr33')
        self.master.withdraw()
        # Update "requested size" from geometry manager
        self.master.update_idletasks()
        x = (self.master.winfo_screenwidth() / 3 - self.master.winfo_reqwidth()) / 2
        y = (self.master.winfo_screenheight() / 3 - self.master.winfo_reqheight()) / 2
        self.master.geometry("+%d+%d" % (x, y))
        self.master.deiconify()
        self.master.protocol("WM_DELETE_WINDOW", lambda arg=self.master: self.msgQuitapp(arg))

        self.mBar = MenuBar(self)
        self.mBar.pack(side=tk.TOP, fill=tk.X, expand=1)

        self.can = tk.Canvas(self, width=1250, height=700, bd=0, relief=tk.SUNKEN)

        self.clock_label = tk.Label(self, text="", fg="white", bg="RoyalBlue3",
            font=("Times", 18, 'bold'))
        self.clock_label.pack(side=tk.TOP, fill=tk.X, expand=1)
        self.clock_label.after(200, self.tick)

        self.viewPort = tk.Frame(self.can)
        self.canvas_window = self.can.create_window((4,4), window=self.viewPort,
            anchor=tk.NW, tags="self.viewPort")

        self.vsb = tk.Scrollbar(self, orient=tk.VERTICAL, command=self.can.yview,
            troughcolor='SteelBlue2', bg='RoyalBlue3', activebackground='pale turquoise')
        self.can.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(side=tk.RIGHT, fill=tk.Y)

        self.can.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        self.viewPort.bind("<Configure>", self.onFrameConfigure)
        self.can.bind("<Configure>", self.onCanvasConfigure)

        self.viewPort.bind('<Enter>', self.onEnter)
        self.viewPort.bind('<Leave>', self.onLeave)

        self.onFrameConfigure(None)

        self.pack()
        self.startPage()

    def tick(self):
        ''' Updates the display clock every 200 milliseconds '''
        self.new_time = time.strftime("%H:%M:%S %p")
        try:
            if self.new_time == self.new_time:
                self.time = self.new_time
                self.display_time = self.time
                self.clock_label.configure(text=self.display_time)
                self._job = self.clock_label.after(200, self.tick)
        except (ValueError, OSError) as val_err:
            print("[!] Error time --> ", val_err)

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.can.configure(scrollregion=self.can.bbox(tk.ALL))

    def onCanvasConfigure(self, event):
        '''Reset the canvas window to encompass inner frame when required'''
        canvas_width = event.width
        self.can.itemconfig(self.canvas_window, width=canvas_width)

    def onMouseWheel(self, event):
        """
            Some of Frame need to be scrolled.
        """
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

    def addScroll(self):
        ''' To add ScrollBar '''
        try:
            exists = self.vsb.winfo_exists()
            if exists == 1:
                self.vsb.pack(side=tk.RIGHT, fill=tk.Y)
                print("Ok, ScrollBar exist")
        except Exception as err_scrl:
            print("Scrollbar doesn't exist", err_scrl)
            self.vsb.pack(side=tk.RIGHT, fill=tk.Y)
            print("Ok, ScrollBar created")

    def reinitscroll(self, event):
        """
            Reinitialization of scrollbarcanvas
            and MouseWheelcanvas.
        """
        self.addScroll()
        print("ScrollBar appears again !")
        self.onEnter(event)
        print("MouseWheel reactivated for all !")
        self.master.focus()
        print('Master 1 :', self.master.focus())

    def onLeave(self, event):
        if platform.system() == 'Linux':
            self.can.unbind_all("<Button-4>")
            self.can.unbind_all("<Button-5>")
        else:
            self.can.unbind_all("<MouseWheel>")

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

    def delScroll(self, event):
        ''' To delete ScrollBar '''
        self.vsb.forget()
        print("ScrollBar deleted")
        self.onLeave(event)
        self.master.focus()
        print('Master 2 :', self.master.focus())

    def forgetVsb(self):
        ''' To delete ScrollBar '''
        try:
            exists = self.vsb.winfo_exists()
            if exists == 1:
                self.vsb.forget()
                print("Ok, ScrollBar delete.")
        except Exception as err_delscrol:
            print("Scrollbar doesn't exist", err_delscrol)
            self.vsb.forget()
            print("Ok, ScrollBar deleted.")

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
                playsound('./beep_sounds/sound101.wav')
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
                playsound('./beep_sounds/sound101.wav')
                #playsound('./beep_sounds/loop79.mp3')
        except OSError as err_quit:
            print("[!] Error 3 : time to quit !!!", err_quit)

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

    def startPage(self):
        """
            First page when you start app.
        """
        # Insert picture
        self.effacer()
        self.forgetVsb()

        self.photo = tk.PhotoImage(file='./syno_gif/fondcolorbg4.png')
        self.itemfirst = self.can.create_image((0,0), image=self.photo,
            anchor=tk.NW)

        # Insert text
        self.can.create_text(625, 350, anchor=tk.CENTER,
            text="Python 3.6 - Tkinter 8.6 - GIMP 2.8",
            font=('Times New Roman', 18, 'bold'), fill='turquoise')

        # Insert text
        self.can.create_text(1240, 670, anchor=tk.NE, text="ko@l@tr33",
            font=('Times', 12), fill='turquoise')

        # 3 buttons at first.
        self.button1 = tk.Button(self, text="Info", font=('Times', 14, 'bold'),
            bg='grey17', fg='cyan', command = self.frameInfo)
        self.button1.configure(width=10, bd=3, highlightbackground='grey10',
            activebackground='pale turquoise')
        self.fbutton1_window = self.can.create_window(75, 30, anchor=tk.CENTER,
            window=self.button1)

        # Connection to DB
        self.button2 = tk.Button(self, text="DATABASE", font=('Times', 18, 'bold'),
            bg='RoyalBlue3', fg='white', command = self.funcPyCon)
        self.button2.configure(width=15, bd=3, highlightbackground='RoyalBlue4',
            activebackground='pale turquoise')
        self.fbutton2_window = self.can.create_window(300, 450, anchor=tk.CENTER,
            window=self.button2)

        # Synopsis button
        self.button3 = tk.Button(self, text="EVENTBOX", font=('Times', 18, 'bold'),
            bg='RoyalBlue3', fg='white', command = self.showSynopsis)
        self.button3.configure(width=15, bd=3, highlightbackground='RoyalBlue4',
            activebackground='pale turquoise')
        self.fbutton3_window = self.can.create_window(625, 450, anchor=tk.CENTER,
            window=self.button3)

        # Patients button
        self.button4 = tk.Button(self, text="RESIDENTS", font=('Times', 18, 'bold'),
            bg='RoyalBlue3', fg='white', command = self.showPatients)
        self.button4.configure(width=15, bd=3, highlightbackground='RoyalBlue4',
            activebackground='pale turquoise')
        self.fbutton4_window = self.can.create_window(950, 450, anchor=tk.CENTER,
            window=self.button4)

        self.can.configure(scrollregion=self.can.bbox(tk.ALL))
        self.can.bind("<Button-1>", self.delScroll)

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
            Call param functions from extensions folder.
        """
        extendAgenda(self, a)

    def contact_num(self, h):
        """
            call contact patient
        """
        if h == h:
            print("h value : ", h)
            callPatNum(self, h)
        else:
            print("h seems to be inexistent...")

    def contactfamily(self, j):
        """
            call contact family
        """
        if j == j:
            print("j value : ", j)
            callFamWind(self, j)
        else:
            print("j seems to be inexistent...")

    def contactdoctor(self, k):
        """
            call contact doctor
        """
        if k == k:
            print("k value : ", k)
            callDoctorWind(self, k)
        else:
            print("k seems to be inexistent...")

    def contacthcsystem(self, l):
        """
            call contact hcsystem
        """
        if l == l:
            print("l value : ", l)
            callHomecsWind(self, l)
        else:
            print("l seems to be inexistent...")

    def besoinsCoche(self, b):
        """
            Call checkcase functions from extensions folder.
        """
        checkcaseExtend(self, b)

    def suiviSoins(self, s):
        """
            Call need's function.
            Hide background window and
            call script with subprocess.run()
        """
        extendHealth(self, s)

    def showParam(self, p):
        """
            Call param functions from extensions folder.
        """
        parameters(self, p)

    def bmikilo(self, u):
        """
            Call bmi functions from extensions folder.
        """
        bmicalkilo(self, u)

    def visitMed(self, t):
        """
            Hide the background window during vm_patient.py
            script is running.
        """
        medicalVisit(self, t)

    def nutritionMenu(self, n):
        """
            Call nutrition functions from extensions folder.
        """
        nutritionExtend(self, n)

    def manualFile(self):
        """
            Open manual in TXT and PDF format.
        """
        self.master.withdraw()
        subprocess.run('./manual/pdfopenmanual.py', check=True)
        self.master.deiconify()

    def allFilesBackup(self, f):
        """
            Call backup functions from extensions folder.
        """
        overviewExtend(self, f)

    def updateFiletxt(self):
        """
            It's time to backup !
            This function is called from boxapp.py (line 22)
            dataBackToSave(self) --> Backup/backupfile.py
            paramBackToSave(self) -- > param/backup_month.py
            bmiBackToSave(self) --> calBmi_backup.py
        """
        dataBackToSave(self)
        paramBackToSave(self)
        bmiBackToSave(self)

    def upDateAll(self):
        """
            To reset app by pressing refresh button.
            Close, open directly and update data from
            patcaps.py !
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
    Application(root).pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    root.mainloop()
