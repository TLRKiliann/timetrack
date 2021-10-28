#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
    This script run many functions to introduce or to stop
    medication. Usr can manage treatments and/or reserves
    and watch results using 5 files and various presentations.
    I've used exceptions, msgbox and shell to assume the good
    process of this script.
"""


import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import os
import time
from playsound import playsound

from ttt.msgmed.verifmsg6 import showTreat
from ttt.msgmed.verifmsg6 import showReserve
from ttt.msgmed.verifmsg6 import readTttStory
from ttt.msgmed.verifmsg6 import readResStory
from ttt.msgmed.verifmsg6 import readFileStory
from ttt.msgmed.verifmsg6 import showStopMed

from ttt.copymed.tttmanager6 import copyToTreat
from ttt.copymed.tttmanager6 import toCopyJsonTreat

from ttt.copyres.resmanager6 import copyToReserve
from ttt.copyres.resmanager6 import toCopyJsonRes

from ttt.stopmed.tttstop6 import stopTreatment
from ttt.stopres.resstop6 import stopReserve

from ttt.uploadtreat.t_upload6 import tttupload
from ttt.uploadres.r_upload6 import resupload

from ttt.printview.printmed6 import tttviewnprint
from ttt.printview.printmed6 import resviewnprint
from ttt.printview.printmed6 import ttt_stpview
from ttt.printview.printmed6 import res_stpview


def callTreatment6(self):
    """
        Call Medication Manager configuration for patient 1.
        You can introduce, stop, traitement(s) and/or reserve(s).
        5 files are managed by this script to appreciate results.
    """
    self.effacer()
    self.delScroll()
    self.photo = tk.PhotoImage(file='./syno_gif/tt_fontcolor.png')
    self.itemfirst = self.can.create_image((0,0), image=self.photo,
        anchor=tk.NW)

    s = ttk.Style()
    s.theme_use('default')

    self.x10, self.y10 = 625, 30
    self.textLab = tk.Label(self.can, text="Medication Manager",
        font=('serif', 22, 'bold'), fg='aquamarine', bg='DodgerBlue2')
    self.textLab_window = self.can.create_window(self.x10, self.y10,
        window=self.textLab)

    self.x20, self.y20 = 410, 80
    self.labelallergy = tk.Label(self.can, text="Allergy : ",
        font=('Arial', 18, 'bold'), fg='coral', bg='DodgerBlue2')
    self.labelallergy_window = self.can.create_window(self.x20, self.y20,
        window=self.labelallergy)

    # Read allergy for entry widget
    with open('./newpatient/entryfile6.txt', 'r') as filename2:
        line1 = filename2.readline()
        line2 = filename2.readline()
        line3 = filename2.readline()

    self.x30, self.y30 = 670, 80
    self.entrytext = tk.StringVar()
    self.entryName = tk.Entry(self.can, textvariable=self.entrytext, width=50)
    self.entrytext.set(line3[:-1])
    self.entryName_window = self.can.create_window(self.x30, self.y30,
        window=self.entryName)

    self.x31, self.y31 = 990, 50
    self.buttprint = tk.Button(self.can, text="View ttt", fg='white',
        bg='RoyalBlue2', bd=3, width=10, highlightbackground='DodgerBlue2',
        activebackground='pale turquoise', command = tttviewnprint)
    self.buttprint_window = self.can.create_window(self.x31, self.y31,
        window=self.buttprint)

    self.x32, self.y32 = 1130, 50
    self.buttresprint = tk.Button(self.can, text="View R", fg='white',
        bg='RoyalBlue2', bd=3, width=10, highlightbackground='DodgerBlue2',
        activebackground='pale turquoise', command = resviewnprint)
    self.buttresprint_window = self.can.create_window(self.x32, self.y32,
        window=self.buttresprint)

    self.x33, self.y33 = 990, 105
    self.buttprint = tk.Button(self.can, text="View stop ttt", fg='white',
        bg='RoyalBlue2', bd=3, width=10, highlightbackground='DodgerBlue2',
        activebackground='pale turquoise', command = ttt_stpview)
    self.buttprint_window = self.can.create_window(self.x33, self.y33,
        window=self.buttprint)

    self.x34, self.y34 = 1130, 105
    self.buttresprint = tk.Button(self.can, text="View stop R", fg='white',
        bg='RoyalBlue2', bd=3, width=10, highlightbackground='DodgerBlue2',
        activebackground='pale turquoise', command = res_stpview)
    self.buttresprint_window = self.can.create_window(self.x34, self.y34,
        window=self.buttresprint)

    self.x40, self.y40 = 120, 150
    self.LabDate = tk.Label(self.can, text="Date : ", width=15, font=12,
        fg='white', bg='DodgerBlue2', anchor='e')
    self.LabDate_window = self.can.create_window(self.x40, self.y40,
        window=self.LabDate)

    self.x50, self.y50 = 120, 180
    self.LabHour = tk.Label(self.can, text="Hour : ", width=15, font=12,
        fg='white', bg='DodgerBlue2', anchor='e')
    self.LabHour_window = self.can.create_window(self.x50, self.y50,
        window=self.LabHour)

    self.x60, self.y60 = 120, 210
    self.LabName = tk.Label(self.can, text="Patient name : ", width=15, font=12,
        fg='white', bg='DodgerBlue2', anchor='e')
    self.LabName_window = self.can.create_window(self.x60, self.y60,
        window=self.LabName)

    self.x70, self.y70 = 120, 240
    self.LabTreat = tk.Label(self.can, text='Name of drug : ', width=15,
        font=12, fg='white', bg='DodgerBlue2', anchor='e')
    self.LabTreat_window = self.can.create_window(self.x70, self.y70,
        window=self.LabTreat)

    self.x80, self.y80 = 120, 270
    self.LabDose = tk.Label(self.can, text="Dose : ", width=15, font=12,
        fg='white', bg='DodgerBlue2', anchor='e')
    self.LabDose_window = self.can.create_window(self.x80, self.y80,
        window=self.LabDose)

    self.x90, self.y90 = 300, 150
    self.time_string = tk.IntVar()
    self.textDate = tk.Entry(self.can, textvariable=self.time_string,
        highlightbackground='grey', bd=4)
    self.time_string.set(time.strftime("%d/%m/%Y"))
    self.textDate_window = self.can.create_window(self.x90, self.y90,
        window=self.textDate)

    self.x100, self.y100 = 300, 180
    self.time_Htring = tk.IntVar()
    self.textHour = tk.Entry(self.can, textvariable=self.time_Htring,
        highlightbackground='grey', bd=4)
    self.time_Htring.set(time.strftime("%H:%M:%S"))
    self.textHour_window = self.can.create_window(self.x100, self.y100,
        window=self.textHour)

    # Read name of patient for entry widget
    with open('./newpatient/entryfile6.txt', 'r') as filename:
        line1 = filename.readline()

    self.x110, self.y110 = 300, 210
    self.name_text = tk.StringVar()
    self.textName = tk.Entry(self.can, textvariable=self.name_text,
        highlightbackground='grey', bd=4)
    self.name_text.set(line1[:-1])
    self.textName_window = self.can.create_window(self.x110, self.y110,
        window=self.textName)

    self.x120, self.y120 = 300, 240
    self.ttt_name = tk.StringVar()
    self.textTreat = tk.Entry(self.can, textvariable=self.ttt_name,
        highlightbackground='grey', bd=4)
    self.ttt_name.set("Drug")
    self.textTreat_window = self.can.create_window(self.x120, self.y120,
        window=self.textTreat)

    self.x130, self.y130 = 300, 270
    self.tttDosage = tk.StringVar()
    self.textDosage = tk.Entry(self.can, textvariable=self.tttDosage,
        highlightbackground='grey', bd=4)
    self.tttDosage.set("mcg/ml/mg/UI/gttes")
    self.textDosage_window = self.can.create_window(self.x130, self.y130,
        window=self.textDosage)

    def callbackDay(event):
        print(self.comboDay.get())

    def callbackMonth(event):
        print(self.comboMonth.get())

    def callbackYear(event):
        print(self.comboYear.get())

    def callbackFinishDay(event):
        print(self.comboFinishDay.get())

    def callbackFinishMonth(event):
        print(self.comboFinishMonth.get())

    def callbackFinishYear(event):
        print(self.comboFinishYear.get())

    def creatttstop():
        """
            Create stopped_ttt.txt if it doesn't exist.
        """
        try:
            if os.path.getsize("./ttt/doc_ttt6/stopped_ttt.txt"):
                print("[+] File stopped_ttt.txt exist.")
        except FileNotFoundError as nf_stopttt:
            print("[!] File stopped_ttt.txt does not exist !", nf_stopttt)
            with open("./ttt/doc_ttt6/stopped_ttt.txt", "w") as creattt_file:
                creattt_file.write("> TREATMENT stopped by date :\n")
                creattt_file.write("-------------------------------------------")
            print("[+] File stopped_ttt.txt created !")

    creatttstop()

    def createrestop():
        """
            Create stopped_res.txt if it doesn't exist.
        """
        try:
            if os.path.getsize("./ttt/doc_ttt6/stopped_res.txt"):
                print("[+] File stopped_res.txt exist.")
        except FileNotFoundError as nf_resttt:
            print("[!] File stopped_res.txt does not exist !")
            with open("./ttt/doc_ttt6/stopped_res.txt", "w") as creares_file:
                creares_file.write("\n\n> RESERVE stopped by date :\n")
                creares_file.write("---------------------------------------")
            print("[+] File stopped_res.txt created !")

    createrestop()

    def mainCopyTreat(self):
        """
            MsgBox to confirm that everything is done.
            Call function to upload ttt files.
        """
        playsound('./beep_sounds/c4_plant2.wav')
        MsgBoxayes = messagebox.askyesno('Record', 'Do you want to save ?')
        if MsgBoxayes == 1:
            print("[Test_ttt] Just before executing copyToTreat() function !")
            copyToTreat(self)
            print("[Test_ttt] Just before executing toCopyJsonTreat() function !")
            toCopyJsonTreat(self)
            print("[Test_ttt] Just before executing tttupload() function !")
            tttupload()
            #app.destroy()
        else:
            messagebox.showinfo('Return', 'You will return to the application')

    def mainCopyRes(self):
        """
            MsgBox to confirm that everything is done.
            Call function to upload reserve files.
        """
        playsound('./beep_sounds/c4_plant2.wav')
        MsgBoxayn = messagebox.askyesno('Record', 'Do you want to save ?')
        if MsgBoxayn == 1:
            print("[Test_res] Just before executing copyToReserve() function !")
            copyToReserve(self)
            print("[Test_res] Just before executing toCopyJsonRes() function !")
            toCopyJsonRes(self)
            print("[Test_res] Just before executing resupload() function !")
            resupload()
            #app.destroy()
        else:
            messagebox.showinfo('Return', 'You will return to main application.')

    self.x140, self.y140 = 500, 140
    self.buttShowttt = tk.Button(self.can, text="ttt Tab", width=10,
        fg='aquamarine', bg='RoyalBlue3', bd=3, highlightbackground='DodgerBlue2',
        activebackground='pale turquoise', command=showTreat)
    self.buttShowttt_window = self.can.create_window(self.x140, self.y140,
        window=self.buttShowttt)

    self.x150, self.y150 = 500, 190
    self.buttShowres = tk.Button(self.can, text="R Tab", width=10,
        fg='aquamarine', bg='RoyalBlue3', bd=3, highlightbackground='DodgerBlue2',
        activebackground='pale turquoise', command=showReserve)
    self.buttShowres_window = self.can.create_window(self.x150, self.y150,
        window=self.buttShowres)

    self.x160, self.y160 = 500, 240
    self.buttHisttt = tk.Button(self.can, text="ttt History", width=10,
        fg='white', bg='RoyalBlue3', bd=3, highlightbackground='DodgerBlue2',
        activebackground='pale turquoise', command=readTttStory)
    self.buttHisttt_window = self.can.create_window(self.x160, self.y160,
        window=self.buttHisttt)

    self.x170, self.y170 = 500, 290
    self.buttHistres = tk.Button(self.can, text="R History", width=10,
        fg='white', bg='RoyalBlue3', bd=3, highlightbackground='DodgerBlue2',
        activebackground='pale turquoise', command=readResStory)
    self.buttHistres_window = self.can.create_window(self.x170, self.y170,
        window=self.buttHistres)

    self.x180, self.y180 = 220, 340
    self.buttHistp = tk.Button(self.can, text="Stopped", width=10,
        fg='white', bg='RoyalBlue3', bd=3, highlightbackground='DodgerBlue2',
        activebackground='pale turquoise', command=showStopMed)
    self.buttHistp_window = self.can.create_window(self.x180, self.y180,
        window=self.buttHistp)

    self.x190, self.y190 = 360, 340
    self.buttFullstp = tk.Button(self.can, text="Resume Stop", width=10,
        fg='white', bg='RoyalBlue3', bd=3, highlightbackground='DodgerBlue2',
        activebackground='pale turquoise', command=readFileStory)
    self.buttFullstp_window = self.can.create_window(self.x190, self.y190,
        window=self.buttFullstp)

    self.x200, self.y200 = 800, 140
    self.textProcess = tk.Label(self.can, text="Processing start date :",
        font=('serif', 12, 'bold'), fg='aquamarine', bg='DodgerBlue2',
        width=40, anchor='w')
    self.textProcess_window = self.can.create_window(self.x200, self.y200,
        window=self.textProcess)

    def changeDay():
        self.comboDay['values']=['', '01', '02', '03', '04',
        '05', '06', '07', '08',
        '09', '10', '11', '12',
        '13', '14', '15', '16',
        '17', '18', '19', '20',
        '21', '22', '23', '24',
        '25', '26', '27', '28',
        '29', '30', '31']

    self.labelDay = tk.Label(self.can,
        text = "Choose the day :", font=12, fg='white', bg='DodgerBlue2')
    self.labelDay_window = self.can.create_window(700, 180, window=self.labelDay)

    self.mystring = tk.StringVar()
    self.comboDay = ttk.Combobox(self.can, textvariable=self.mystring,
        values=['', '01', '02', '03', '04',
        '05', '06', '07', '08',
        '09', '10', '11', '12',
        '13', '14', '15', '16',
        '17', '18', '19', '20',
        '21', '22', '23', '24',
        '25', '26', '27', '28',
        '29', '30', '31'], postcommand=changeDay)

    self.comboDay.bind("<<ComboboxSelected>>", callbackDay)
    self.comboDay.current(0)
    self.comboDay_window = self.can.create_window(700, 220, window=self.comboDay)

    def changeMonth():
        self.comboMonth["values"] = ['',
        ' January',
        ' February',
        ' March',
        ' April',
        ' May',
        ' June',
        ' July',
        ' August',
        ' September',
        ' October',
        ' November',
        ' December']

    self.x230, self.y230 = 900, 180
    self.labelMonth = tk.Label(self.can,
        text = "Choose the month :", font=12, fg='white', bg='DodgerBlue2')
    self.labelMonth_window = self.can.create_window(self.x230, self.y230,
        window=self.labelMonth)

    self.x240, self.y240 = 900, 220
    self.mystring2 = tk.StringVar()
    self.comboMonth = ttk.Combobox(self.can, textvariable=self.mystring2,
        values=['',
        ' January',
        ' February',
        ' March',
        ' April',
        ' May',
        ' June',
        ' July',
        ' August',
        ' September',
        ' October',
        ' November',
        ' December'], postcommand=changeMonth)

    self.comboMonth.bind("<<ComboboxSelected>>", callbackMonth)
    self.comboMonth.current(0)
    self.comboMonth_window = self.can.create_window(self.x240, self.y240,
        window=self.comboMonth)

    def changeYear():
        self.comboYear["values"] = ['', ' 2000', ' 2001', ' 2002', ' 2003',
        ' 2004', ' 2005', ' 2006', ' 2007',
        ' 2008', ' 2009', ' 2010', ' 2011',
        ' 2012', ' 2013', ' 2014', ' 2015',
        ' 2016', ' 2017', ' 2018', ' 2019',
        ' 2020', ' 2021', ' 2022', ' 2023',
        ' 2024', ' 2025', ' 2026', ' 2027',
        ' 2028', ' 2029', ' 2030', ' 2031',
        ' 2032', ' 2033', ' 2034', ' 2035']

    self.x250, self.y250 = 1100, 180
    self.labelYear = tk.Label(self.can,
        text = "Choose the year :", font=12, fg='white', bg='DodgerBlue2')
    self.labelYear_window = self.can.create_window(self.x250, self.y250,
        window=self.labelYear)

    self.x260, self.y260 = 1100, 220
    self.mystring3 = tk.StringVar()
    self.comboYear = ttk.Combobox(self.can, textvariable=self.mystring3,
        values=['', ' 2000', ' 2001', ' 2002', ' 2003',
        ' 2004', ' 2005', ' 2006', ' 2007',
        ' 2008', ' 2009', ' 2010', ' 2011',
        ' 2012', ' 2013', ' 2014', ' 2015',
        ' 2016', ' 2017', ' 2018', ' 2019',
        ' 2020', ' 2021', ' 2022', ' 2023',
        ' 2024', ' 2025', ' 2026', ' 2027',
        ' 2028', ' 2029', ' 2030', ' 2031',
        ' 2032', ' 2033', ' 2034', ' 2035'], postcommand=changeYear)

    self.comboYear.bind("<<ComboboxSelected>>", callbackYear)
    self.comboYear.current(0)
    self.comboYear_window = self.can.create_window(self.x260, self.y260,
        window=self.comboYear)

    # Date of finish
    self.x270, self.y270 = 800, 270
    self.txtfinishdate = tk.Label(self.can, text="Processing end date :",
        font=('serif', 12, 'bold'), fg='aquamarine', bg='DodgerBlue2',
        width=40, anchor='w')
    self.txtfinishdate_window = self.can.create_window(self.x270, self.y270,
        window=self.txtfinishdate)

    def finishDay():
        self.comboFinishDay["values"] = ['', '01', '02', '03', '04',
        '05', '06', '07', '08',
        '09', '10', '11', '12',
        '13', '14', '15', '16',
        '17', '18', '19', '20',
        '21', '22', '23', '24',
        '25', '26', '27', '28',
        '29', '30', '31']

    self.x280, self.y280 = 700, 310
    self.labelFinishDay = tk.Label(self.can,
        text = "Choose the day :", font=12, fg='white', bg='DodgerBlue2')
    self.labelFinishDay_window = self.can.create_window(self.x280, self.y280,
        window=self.labelFinishDay)

    self.x290, self.y290 = 700, 350
    self.mystring4 = tk.StringVar()
    self.comboFinishDay = ttk.Combobox(self.can, textvariable=self.mystring4,
        values=['', '01', '02', '03', '04',
        '05', '06', '07', '08',
        '09', '10', '11', '12',
        '13', '14', '15', '16',
        '17', '18', '19', '20',
        '21', '22', '23', '24',
        '25', '26', '27', '28',
        '29', '30', '31'], postcommand=finishDay)

    self.comboFinishDay.bind("<<ComboboxSelected>>", callbackFinishDay)
    self.comboFinishDay.current(0)
    self.comboFinishDay_window = self.can.create_window(self.x290, self.y290,
        window=self.comboFinishDay)

    def finishMonth():
        self.comboFinishMonth["values"] = ['', '01', '02', '03', '04',
        '05', '06', '07', '08',
        '09', '10', '11', '12']

    self.x300, self.y300 = 900, 310
    self.labelMonth = tk.Label(self.can,
        text = "Choose the month :", font=12, fg='white', bg='DodgerBlue2')
    self.labelMonth_window = self.can.create_window(self.x300, self.y300,
        window=self.labelMonth)

    self.x310, self.y310 = 900, 350
    self.mystring5 = tk.StringVar()
    self.comboFinishMonth = ttk.Combobox(self.can, textvariable=self.mystring5,
        values=['',
        '01',
        '02',
        '03',
        '04',
        '05',
        '06',
        '07',
        '08',
        '09',
        '10',
        '11',
        '12'], postcommand=finishMonth)

    self.comboFinishMonth.bind("<<ComboboxSelected>>", callbackFinishMonth)
    self.comboFinishMonth.current(0)
    self.comboFinishMonth_window = self.can.create_window(self.x310, self.y310,
        window=self.comboFinishMonth)

    def finishYear():
        self.comboFinishYear["values"] = ['', '2021', '2022', '2023',
        '2024', '2025', '2026', '2027',
        '2028', '2029', '2030', '2031',
        '2032', '2033', '2034', '2035']

    self.x320, self.y320 = 1100, 310
    self.labelFinishYear = tk.Label(self.can,
        text = "Choose the year :", font=12, fg='white', bg='DodgerBlue2')
    self.labelFinishYear_window = self.can.create_window(self.x320, self.y320,
        window=self.labelFinishYear)

    self.x330, self.y330 = 1100, 350
    self.mystring6 = tk.StringVar()
    self.comboFinishYear = ttk.Combobox(self.can, textvariable=self.mystring6,
        values=['', '2021', '2022', '2023',
        '2024', '2025', '2026', '2027',
        '2028', '2029', '2030', '2031',
        '2032', '2033', '2034', '2035'], postcommand=finishYear)

    self.comboFinishYear.bind("<<ComboboxSelected>>", callbackFinishYear)
    self.comboFinishYear.current(0)
    self.comboFinishYear_window = self.can.create_window(self.x330, self.y330,
        window=self.comboFinishYear)

    self.x340, self.y340 = 100, 380
    self.checkLab = tk.Label(self.can, text="Doses :",
        font=('serif', 14, 'bold'), fg='aquamarine', bg='DodgerBlue2')
    self.checkLab_window = self.can.create_window(self.x340, self.y340,
        window=self.checkLab)

    self.x350, self.y350 = 100, 420
    self.CheckVarMatin = tk.IntVar()
    self.Cma = tk.Checkbutton(self.can, text="Morning --->", fg='navy',
        bg='cyan', variable=self.CheckVarMatin,
        onvalue=1, offvalue=0, height=1,
        width=15, anchor='w')
    self.Cma_window = self.can.create_window(self.x350, self.y350,
        window=self.Cma)

    self.x360, self.y360 = 300, 420
    self.LabDose = tk.Label(self.can, text='Morning take : ', font=12,
        width=20, fg='white', bg='DodgerBlue2')
    self.LabDose_window = self.can.create_window(self.x360, self.y360,
        window=self.LabDose)

    self.x370, self.y370 = 500, 380
    self.titlunit = tk.Label(self.can, text="Unity :",
        font=('serif', 14, 'bold'), fg='aquamarine', bg='DodgerBlue2')
    self.titlunit_window = self.can.create_window(self.x370, self.y370,
        window=self.titlunit)

    self.x380, self.y380 = 500, 420
    self.Entmatin = tk.Entry(self.can, highlightbackground='grey', bd=4)
    self.Entmatin_window = self.can.create_window(self.x380, self.y380,
        window=self.Entmatin)

    self.x390, self.y390 = 100, 460
    self.CheckVarMidi = tk.IntVar()
    self.Cmi = tk.Checkbutton(self.can, text="Noon --->", fg='navy',
        bg='cyan', variable=self.CheckVarMidi,
        onvalue=1, offvalue=0, height=1,
        width=15, anchor='w')
    self.Cmi_window = self.can.create_window(self.x390, self.y390,
        window=self.Cmi)

    self.x400, self.y400 = 300, 460
    self.Lunchtime = tk.Label(self.can, text='Midday take : ', font=12,
        width=20, fg='white', bg='DodgerBlue2')
    self.Lunchtime_window = self.can.create_window(self.x400, self.y400,
        window=self.Lunchtime)

    self.x410, self.y410 = 500, 460
    self.Entmidi = tk.Entry(self.can, highlightbackground='grey', bd=4)
    self.Entmidi_window = self.can.create_window(self.x410, self.y410,
        window=self.Entmidi)

    self.x420, self.y420 = 100, 500
    self.CheckVarSoir = tk.IntVar()
    self.Csoir = tk.Checkbutton(self.can, text="Evening --->", fg='navy',
        bg='cyan', variable=self.CheckVarSoir,
        onvalue=1, offvalue=0, height=1,
        width=15, anchor='w')
    self.Csoir_window = self.can.create_window(self.x420, self.y420,
        window=self.Csoir)

    self.x430, self.y430 = 300, 500
    self.Eventake = tk.Label(self.can, text='Evening take : ', font=12,
        width=20, fg='white', bg='DodgerBlue2')
    self.Eventake_window = self.can.create_window(self.x430, self.y430,
        window=self.Eventake)

    self.x440, self.y440 = 500, 500
    self.Entsoir = tk.Entry(self.can, highlightbackground='grey', bd=4)
    self.Entsoir_window = self.can.create_window(self.x440, self.y440,
        window=self.Entsoir)

    self.x450, self.y450 = 100, 540
    self.CheckVarNuit = tk.IntVar()
    self.Cnuit = tk.Checkbutton(self.can, text="Night --->", fg='navy',
        bg='cyan', variable=self.CheckVarNuit,
        onvalue=1, offvalue=0, height=1,
        width=15, anchor='w')
    self.Cnuit_window = self.can.create_window(self.x450, self.y450,
        window=self.Cnuit)

    self.x460, self.y460 = 300, 540
    self.Nightlab = tk.Label(self.can, text='Night take : ', font=12,
        width=20, fg='white', bg='DodgerBlue2')
    self.Nightlab_window = self.can.create_window(self.x460, self.y460,
        window=self.Nightlab)

    self.x470, self.y470 = 500, 540
    self.Entnuit = tk.Entry(self.can, highlightbackground='grey', bd=4)
    self.Entnuit_window = self.can.create_window(self.x470, self.y470,
        window=self.Entnuit)

    self.x480, self.y480 = 500, 600
    self.LabSign = tk.Label(self.can, text='Signature :',
        font=14, width=15, fg='navy', bg='aquamarine')
    self.LabSign_window = self.can.create_window(self.x480, self.y480,
        window=self.LabSign)

    self.x490, self.y490 = 700, 600
    self.textSign = tk.Entry(self.can, highlightbackground='grey', bd=4)
    self.textSign_window = self.can.create_window(self.x490, self.y490,
        window=self.textSign)

    self.x500, self.y500 = 1020, 600
    self.buttsavettt = tk.Button(self.can, text="Save as ttt", width=40,
        fg='yellow', bg='RoyalBlue3', bd=3, highlightbackground='DodgerBlue2',
        activebackground='pale turquoise', command = lambda: mainCopyTreat(self))
    self.buttsavettt_window = self.can.create_window(self.x500, self.y500,
        window=self.buttsavettt)

    self.x510, self.y510 = 873, 420
    self.Labelifchoice = tk.Label(self.can,
        text="If medication is a RESERVE make your choice below :",
        font=('serif', 12, 'bold'), fg='aquamarine', bg='DodgerBlue2')
    self.Labelifchoice_window = self.can.create_window(self.x510, self.y510,
        window=self.Labelifchoice)

    self.x520, self.y520 = 700, 460
    self.CheckVar1 = tk.IntVar()
    self.C1 = tk.Checkbutton(self.can, text="Reserve", fg='navy',
        bg='pale green', variable=self.CheckVar1,
        onvalue=1, offvalue=0, height=1, width=16, anchor='w')
    self.C1_window = self.can.create_window(self.x520, self.y520, window=self.C1)

    self.x530, self.y530 = 900, 460
    self.labelresd = tk.Label(self.can, text='Number of R/24h : ', font=12,
        width=15, fg='white', bg='DodgerBlue2')
    self.labelresd_window = self.can.create_window(self.x530, self.y530,
        window=self.labelresd)

    self.x540, self.y540 = 1100, 460
    self.Rnbre = tk.Entry(self.can, bd=4, highlightbackground='grey')
    self.Rnbre_window = self.can.create_window(self.x540, self.y540,
        window=self.Rnbre)

    self.x550, self.y550 = 900, 500
    self.lblreason = tk.Label(self.can, text='Reason : ', font=12,
        width=15, fg='white', bg='DodgerBlue2', anchor='e')
    self.lblreason_window = self.can.create_window(self.x550, self.y550,
        window=self.lblreason)

    self.x560, self.y560 = 1100, 500
    self.entreason = tk.Entry(self.can, bd=4, highlightbackground='grey')
    self.entreason_window = self.can.create_window(self.x560, self.y560,
        window=self.entreason)

    self.x570, self.y570 = 700, 500
    self.CheckVar2 = tk.IntVar()
    self.C2 = tk.Checkbutton(self.can, text="First-line", fg='navy',
        bg='pale green', variable=self.CheckVar2,
        onvalue=1, offvalue=0, height=1, width=16, anchor='w')
    self.C2_window = self.can.create_window(self.x570, self.y570, window=self.C2)

    self.x580, self.y580 = 700, 540
    self.CheckVar3 = tk.IntVar()
    self.C3 = tk.Checkbutton(self.can, text="Second-line", fg='navy',
        bg='pale green', variable=self.CheckVar3,
        onvalue=1, offvalue=0, height=1, width=16, anchor='w')
    self.C3_window = self.can.create_window(self.x580, self.y580, window=self.C3)

    self.x590, self.y590 = 1020, 650
    self.buttsaveres = tk.Button(self.can, text="Save as R", fg='yellow',
        bg='RoyalBlue3', bd=3, width=40, highlightbackground='DodgerBlue2',
        activebackground='pale turquoise', command = lambda: mainCopyRes(self))
    self.buttsaveres_window = self.can.create_window(self.x590, self.y590,
        window=self.buttsaveres)

    self.x591, self.y591 = 110, 600
    self.delttt = tk.StringVar()
    self.deleteTreat = tk.Entry(self.can, bd=4, textvariable=self.delttt,
        highlightbackground='red')
    self.delttt.set("Enter ttt to stop")
    self.deleteTreat_window = self.can.create_window(self.x591, self.y591,
        window=self.deleteTreat)

    self.x592, self.y592 = 250, 600
    self.deldose_ttt = tk.StringVar()
    self.deltttdose = tk.Entry(self.can, textvariable=self.deldose_ttt,
        width=10, bd=4, highlightbackground='red')
    self.deldose_ttt.set("Dosage")
    self.deltttdose_window = self.can.create_window(self.x592, self.y592,
        window=self.deltttdose)

    self.x593, self.y593 = 355, 600
    self.buttStopttt = tk.Button(self.can, text="Stop ttt", fg='yellow',
        bg='red', bd=3, width=8, highlightbackground='cyan',
        activebackground='coral', command = lambda: stopTreatment(self))
    self.buttStopttt_window = self.can.create_window(self.x593, self.y593,
        window=self.buttStopttt)

    self.x594, self.y594 = 110, 650
    self.delete_res = tk.StringVar()
    self.delete_res.set("Enter R to stop")
    self.delRestop = tk.Entry(self.can, bd=4, textvariable=self.delete_res,
        highlightbackground='red')
    self.delRestop_window = self.can.create_window(self.x594, self.y594,
        window=self.delRestop)

    self.x595, self.y595 = 250, 650
    self.deldose_res = tk.StringVar()
    self.deldose_res.set("Dosage")
    self.delresdose = tk.Entry(self.can, textvariable=self.deldose_res,
        width=10, bd=4, highlightbackground='red')
    self.delresdose_window = self.can.create_window(self.x595, self.y595,
        window=self.delresdose)

    self.x600, self.y600 = 355, 650
    self.buttStopttt = tk.Button(self.can, text="Stop R", fg='yellow',
        bg='red', bd=3, width=8, highlightbackground='cyan',
        activebackground='coral', command = lambda: stopReserve(self))
    self.buttStopttt_window = self.can.create_window(self.x600, self.y600,
        window=self.buttStopttt)

    def awayOut():
        try:
            self.effacer()
            self.showPatients()
        except (OSError, ValueError) as p_out:
            print("[!] Error from <patienttt1.py> to way out !!!", p_out)

    self.x610, self.y610 = 600, 650
    self.buttQuit = tk.Button(self.can, text="Return to main menu", width=20,
        fg='white', bg='RoyalBlue2', bd=3, highlightbackground='DodgerBlue2',
        activebackground='pale turquoise', command=awayOut)
    self.buttQuit_window = self.can.create_window(self.x610, self.y610,
        window=self.buttQuit)
    
    self.can.configure(scrollregion=self.can.bbox(tk.ALL))
    self.can.unbind_all("<Button-4>")
    self.can.unbind_all("<Button-5>")
