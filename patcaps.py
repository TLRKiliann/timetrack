#!/usr/bin/python3
# -*- coding: utf-8 -*-


import tkinter as tk
import time

#from backapp import *
from agendapp import dispAgBox
from tttapp import dispTttBox
from resapp import dispResBox

from diag.call_diag import *
from ttt.call_medic import *
from labo.callabo import *
from auxequip.call_aux import *
from dmst_doc.call_dmst import *
from update.call_update import *


def callResident(self):
    """
        Main function called since main app
        heal_track.py for displaying patients
        with theirs names and more.
    """
    #self.can.delete(tk.ALL)
    self.effacer()
    self.addScroll()
    self.can.configure(background='DodgerBlue2')

    self.photo = tk.PhotoImage(file='./syno_gif/title_tt3.png')
    self.item_image = self.can.create_image(625, 85, image=self.photo)

    # Display date
    self.x1, self.y1 = 1140, 40
    self.data_time = tk.StringVar()
    self.datew = tk.Entry(self.can, textvariable=self.data_time,
        width=9, bd=3, highlightbackground='grey')
    self.data_time.set(time.strftime("%d/%m/%Y"))
    self.fdatew_window = self.can.create_window(self.x1, self.y1,
        window=self.datew)

    # To introduce a new pytient
    self.x3, self.y3 = 125, 160
    self.buttnewentry = tk.Button(self.can, text="New Entry", font=16,
        width=10, bd=3, bg='RoyalBlue3', fg='white',
        highlightbackground='pale turquoise',
        activebackground='pale turquoise',
        command=self.callPatient1)
    self.fbuttnewentry_window = self.can.create_window(self.x3,
        self.y3, window=self.buttnewentry)

    # To add one patient and files
    self.x4, self.y4 = 325, 160
    self.buttadd = tk.Button(self.can, text="Add patient", font=16,
        width=10, bd=3, bg='RoyalBlue3', fg='white',
        highlightbackground='pale turquoise',
        activebackground='pale turquoise',
        command=self.addPatientAfter)
    self.fbuttadd_window = self.can.create_window(self.x4,
        self.y4, window=self.buttadd)

    # To refresh canvas + menu bar
    self.x5, self.y5 = 525, 160
    self.buttup = tk.Button(self.can, text="Refresh", font=16,
        width=10, bd=3, bg='RoyalBlue3', fg='SpringGreen2',
        highlightbackground='pale turquoise',
        activebackground='pale turquoise',
        command=self.upDateAll)
    self.fbuttup_window = self.can.create_window(self.x5,
        self.y5, window=self.buttup)

    # To delete one patient and all files
    self.x6, self.y6 = 725, 160
    self.buttdel = tk.Button(self.can, text="Delete patient", font=16,
        width=10, bd=3, bg='RoyalBlue3', fg='coral',
        highlightbackground='pale turquoise',
        activebackground='red',
        activeforeground='white', command=self.delEverPat)
    self.fbuttdel_window = self.can.create_window(self.x6,
        self.y6, window=self.buttdel)

    # To go to resident page
    self.x6, self.y6 = 925, 160
    self.buttsynopsis = tk.Button(self.can, text="EventBox", font=16,
        width=10, bd=3, bg='RoyalBlue3', fg='white',
        highlightbackground='pale turquoise',
        activebackground='pale turquoise',
        command=self.showSynopsis)
    self.fbuttsynopsis_window = self.can.create_window(self.x6,
        self.y6, window=self.buttsynopsis)

    # DB
    self.x7, self.y7 = 1125, 160
    self.buttconn = tk.Button(self.can, text="DataBase", font=16,
        width=10, bd=3, bg='RoyalBlue3', fg='white',
        highlightbackground='pale turquoise',
        activebackground='pale turquoise',
        command=self.funcPyCon)
    self.fbuttconn_window = self.can.create_window(self.x7,
        self.y7, window=self.buttconn)

    # Patient 1
    try:
        with open('./newpatient/entryfile.txt', 'r') as namefile:
            line1 = namefile.readline()
    except FileNotFoundError as callfile:
        print("[!] File entryfile.txt doesn't exist !", callfile)

    try:
        self.data_time = line1
        self.x10, self.y10 = 144, 230
        self.new_data1 = tk.StringVar()
        self.entread = tk.Entry(self.can,
            textvariable=self.new_data1,
            highlightbackground='grey', bd=4)
        if line1 == '-':
            line1 = line1
        else:
            line1 = line1[:-1]
        self.new_data1.set(line1)
        self.fentread_window = self.can.create_window(self.x10,
            self.y10, window=self.entread)
    except UnboundLocalError as ub_error1:
        print("[!] File 1 not created !", ub_error1)

    self.x11, self.y11 = 286, 230
    self.buttpatup = tk.Button(self.can, text="Update", font=16,
        width=8, fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=lambda: updateLink(self, g=1))
    self.fbuttpatup_window = self.can.create_window(self.x11,
        self.y11, window=self.buttpatup)

    self.x12, self.y12 = 444, 230
    self.buttdiag = tk.Button(self.can, text="Diagnostic + ATCD",
        font=16, width=18, fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=lambda: diagstic(self, d=1))
    self.fbuttdiag_window = self.can.create_window(self.x12,
        self.y12, window=self.buttdiag)

    self.x13, self.y13 = 612, 230
    self.buttt = tk.Button(self.can, text="Treatments",
        font=16, width=10, fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=lambda: tttMed1(self))
    self.fbuttt_window = self.can.create_window(self.x13,
        self.y13, window=self.buttt)

    self.x14, self.y14 = 740, 230
    self.buttlabo = tk.Button(self.can, text="Laboratory",
        font=16, width=10, fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=lambda: laboResult(self))
    self.fbuttlabo_window = self.can.create_window(self.x14,
        self.y14, window=self.buttlabo)

    self.x15, self.y15 = 868, 230
    self.buttvm = tk.Button(self.can, text="Medical Visit",
        font=16, width=10, fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=self.visitMed)
    self.fbuttvm_window = self.can.create_window(self.x15,
        self.y15, window=self.buttvm)

    self.x16, self.y16 = 996, 230
    self.buttaux = tk.Button(self.can, text="Aux. Equip.",
        font=16, width=10, fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=lambda: aux1(self))
    self.fbuttaux_window = self.can.create_window(self.x16,
        self.y16, window=self.buttaux)

    self.x17, self.y17 = 1124, 230
    self.buttdmst = tk.Button(self.can, text="DMST",
        font=16, width=10, fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=lambda: dmst1(self))
    self.fbuttdmst_window = self.can.create_window(self.x17,
        self.y17, window=self.buttdmst)

    # Patient 2
    try:
        with open('./newpatient/entryfile2.txt', 'r') as namefile:
            line2 = namefile.readline()
    except FileNotFoundError as callfile2:
        print("[!] File entryfile2.txt doesn't exist !", callfile2)

    try:
        self.new_data2 = line2
        self.x20, self.y20 = 144, 262
        self.new_data2 = tk.StringVar()
        self.entrpatf = tk.Entry(self.can, textvariable=self.new_data2,
            highlightbackground='grey', bd=4)
        if line2 == '--':
            line2 = line2
        else:
            line2 = line2[:-1]
        self.new_data2.set(line2)
        self.fentrpatf_window = self.can.create_window(self.x20,
            self.y20, window=self.entrpatf)
    except UnboundLocalError as ub_error2:
        print("[!] File 2 not created !", ub_error2)

    self.x21, self.y21 = 286, 262
    self.buttpatup2 = tk.Button(self.can, text="Update 2", font=16,
        width=8, fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=lambda: updateLink(self, g=2))
    self.fbuttpatup2_window = self.can.create_window(self.x21,
        self.y21, window=self.buttpatup2)

    self.x22, self.y22 = 444, 262
    self.butt2diag = tk.Button(self.can, text="Diagnostic + ATCD 2",
        font=16, width=18, fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=lambda: diagstic(self, d=2))
    self.fbutt2diag_window = self.can.create_window(self.x22,
        self.y22, window=self.butt2diag)

    self.x23, self.y23 = 612, 262
    self.buttt2med = tk.Button(self.can, text="Treatments 2",
        font=16, width=10, fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=lambda: tttMed2(self))
    self.fbuttt2med_window = self.can.create_window(self.x23,
        self.y23, window=self.buttt2med)

    self.x24, self.y24 = 740, 262
    self.butt2labo = tk.Button(self.can, text="Laboratory 2",
        font=16, width=10, fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=lambda: laboResult2(self))
    self.fbutt2labo_window = self.can.create_window(self.x24,
        self.y24, window=self.butt2labo)

    self.x25, self.y25 = 868, 262
    self.butt2vm = tk.Button(self.can, text="Medical Visit2",
        font=16, width=10, fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=self.visitMed2)
    self.fbutt2vm_window = self.can.create_window(self.x25,
        self.y25, window=self.butt2vm)

    self.x26, self.y26 = 996, 262
    self.butt2aux = tk.Button(self.can, text="Aux. Equip.2",
        font=16, width=10, fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=lambda: aux2(self))
    self.fbutt2aux_window = self.can.create_window(self.x26,
        self.y26, window=self.butt2aux)

    self.x27, self.y27 = 1124, 262
    self.butt2dmst = tk.Button(self.can, text="DMST 2",
        font=16, width=10, fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=lambda: dmst2(self))
    self.fbutt2dmst_window = self.can.create_window(self.x27,
        self.y27, window=self.butt2dmst)

    # Patient 3
    try:
        with open('./newpatient/entryfile3.txt', 'r') as namefile:
            line3 = namefile.readline()
    except FileNotFoundError as callfile3:
        print("[!] File entryfile3.txt doesn't exist !", callfile3)

    try:
        self.new_data3 = line3
        self.x30, self.y30 = 144, 294
        self.new_data3 = tk.StringVar()
        self.entrpat3f = tk.Entry(self.can, textvariable=self.new_data3,
            highlightbackground='grey', bd=4)
        if line3 == '---':
            line3 = line3
        else:
            line3 = line3[:-1]
        self.new_data3.set(line3)
        self.fentrpat3f_window = self.can.create_window(self.x30,
            self.y30, window=self.entrpat3f)
    except UnboundLocalError as ub_error3:
        print("[!] File 3 not created !", ub_error3)

    self.x31, self.y31 = 286, 294
    self.buttpat3up = tk.Button(self.can, text="Update 3", font=16,
        width=8, fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=lambda: updateLink(self, g=3))
    self.fbuttpat3up_window = self.can.create_window(self.x31,
        self.y31, window=self.buttpat3up)

    self.x32, self.y32 = 444, 294
    self.butt3diag = tk.Button(self.can, text="Diagnostic + ATCD 3",
        font=16, width=18, fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=lambda: diagstic(self, d=3))
    self.fbutt3diag_window = self.can.create_window(self.x32,
        self.y32, window=self.butt3diag)

    self.x33, self.y33 = 612, 294
    self.butt3med = tk.Button(self.can, text="Treatments 3",
        font=16, width=10, fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=lambda: tttMed3(self))
    self.fbutt3med_window = self.can.create_window(self.x33,
        self.y33, window=self.butt3med)

    self.x34, self.y34 = 740, 294
    self.butt3labo = tk.Button(self.can, text="Laboratory 3",
        font=16, width=10, fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=lambda: laboResult3(self))
    self.fbutt3labo_window = self.can.create_window(self.x34,
        self.y34, window=self.butt3labo)

    self.x35, self.y35 = 868, 294
    self.butt3vm = tk.Button(self.can, text="Medical Visit3",
        font=16, width=10, fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=self.visitMed3)
    self.fbutt3vm_window = self.can.create_window(self.x35,
        self.y35, window=self.butt3vm)

    self.x36, self.y36 = 996, 294
    self.butt3aux = tk.Button(self.can, text="Aux. Equip.3",
        font=16, width=10, fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=lambda: aux3(self))
    self.fbutt3aux_window = self.can.create_window(self.x36,
        self.y36, window=self.butt3aux)

    self.x37, self.y37 = 1124, 294
    self.butt3dmst = tk.Button(self.can, text="DMST 3",
        font=16, width=10, fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=lambda: dmst3(self))
    self.fbutt3dmst_window = self.can.create_window(self.x37,
        self.y37, window=self.butt3dmst)

    # Patient 4
    try:
        with open('./newpatient/entryfile4.txt', 'r') as namefile:
            line4 = namefile.readline()
    except FileNotFoundError as callfile4:
        print("[!] File entryfile4.txt doesn't exist !", callfile4)

    try:
        self.new_data4 = line4
        self.x40, self.y40 = 144, 326
        self.new_data4 = tk.StringVar()
        self.entrpat4f = tk.Entry(self.can,
            textvariable=self.new_data4,
            highlightbackground='grey', bd=4)
        if line4 == '----':
            line4 = line4
        else:
            line4 = line4[:-1]
        self.new_data4.set(line4)
        self.fentrpat4f_window = self.can.create_window(self.x40,
            self.y40, window=self.entrpat4f)
    except UnboundLocalError as ub_error4:
        print("[!] File 4 not created !", ub_error4)

    self.x41, self.y41 = 286, 326
    self.buttpat4up = tk.Button(self.can, text="Update 4",
        font=16, width=8, fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=lambda: updateLink(self, g=4))
    self.fbuttpat4up_window = self.can.create_window(self.x41,
        self.y41, window=self.buttpat4up)

    self.x42, self.y42 = 444, 326
    self.butt4diag = tk.Button(self.can, text="Diagnostic + ATCD 4",
        font=16, width=18, fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=lambda: diagstic(self, d=4))
    self.fbutt4diag_window = self.can.create_window(self.x42,
        self.y42, window=self.butt4diag)

    self.x43, self.y43 = 612, 326
    self.butt4med = tk.Button(self.can, text="Treatments 4",
        font=16, width=10, fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=lambda: tttMed4(self))
    self.fbutt4med_window = self.can.create_window(self.x43,
        self.y43, window=self.butt4med)

    self.x44, self.y44 = 740, 326
    self.butt4labo = tk.Button(self.can, text="Laboratory 4",
        font=16, width=10, fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=lambda: laboResult4(self))
    self.fbutt4labo_window = self.can.create_window(self.x44,
        self.y44, window=self.butt4labo)

    self.x45, self.y45 = 868, 326
    self.butt4vm = tk.Button(self.can, text="Medical Visit4",
        font=16, width=10, fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=self.visitMed4)
    self.fbutt4vm_window = self.can.create_window(self.x45,
        self.y45, window=self.butt4vm)

    self.x46, self.y46 = 996, 326
    self.butt4aux = tk.Button(self.can, text="Aux. Equip.4",
        font=16, width=10, fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=lambda: aux4(self))
    self.fbutt4aux_window = self.can.create_window(self.x46,
        self.y46, window=self.butt4aux)

    self.x47, self.y47 = 1124, 326
    self.butt4dmst = tk.Button(self.can, text="DMST 4",
        font=16, width=10, fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=lambda: dmst4(self))
    self.fbutt4dmst_window = self.can.create_window(self.x47,
        self.y47, window=self.butt4dmst)

    # Patient 5
    try:
        with open('./newpatient/entryfile5.txt', 'r') as namefile:
            line5 = namefile.readline()
    except FileNotFoundError as callfile5:
        print("[!] File entryfile5.txt doesn't exist !", callfile5)

    try:
        self.new_data5 = line5
        self.x50, self.y50 = 144, 358
        self.new_data5 = tk.StringVar()
        self.entrpat5f = tk.Entry(self.can,
            textvariable=self.new_data5,
            highlightbackground='grey', bd=4)
        if line5 == '-----':
            line5 = line5
        else:
            line5 = line5[:-1]
        self.new_data5.set(line5)
        self.fentrpat5f_window = self.can.create_window(self.x50,
            self.y50, window=self.entrpat5f)
    except UnboundLocalError as ub_error5:
        print("[!] File 5 not created !", ub_error5)

    self.x51, self.y51 = 286, 358
    self.buttpat5up = tk.Button(self.can, text="Update 5", font=16,
        width=8, fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=lambda: updateLink(self, g=5))
    self.fbuttpat5up_window = self.can.create_window(self.x51,
        self.y51, window=self.buttpat5up)

    self.x52, self.y52 = 444, 358
    self.butt5diag = tk.Button(self.can, text="Diagnostic + ATCD 5", font=16,
        width=18, fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=lambda: diagstic(self, d=5))
    self.fbutt5diag_window = self.can.create_window(self.x52,
        self.y52, window=self.butt5diag)

    self.x53, self.y53 = 612, 358
    self.butt5med = tk.Button(self.can, text="Treatments 5", font=16,
        width=10, fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=lambda: tttMed5(self))
    self.fbutt5med_window = self.can.create_window(self.x53,
        self.y53, window=self.butt5med)

    self.x54, self.y54 = 740, 358
    self.butt5labo = tk.Button(self.can, text="Laboratory 5", font=16,
        width=10, fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=lambda: laboResult5(self))
    self.fbutt5labo_window = self.can.create_window(self.x54,
        self.y54, window=self.butt5labo)

    self.x55, self.y55 = 868, 358
    self.butt5vm = tk.Button(self.can, text="Medical Visit5", font=16,
        width=10, fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=self.visitMed5)
    self.fbutt5vm_window = self.can.create_window(self.x55,
        self.y55, window=self.butt5vm)

    self.x56, self.y56 = 996, 358
    self.butt5aux = tk.Button(self.can, text="Aux. Equip.5", font=16,
        width=10, fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=lambda: aux5(self))
    self.fbutt5aux_window = self.can.create_window(self.x56,
        self.y56, window=self.butt5aux)

    self.x57, self.y57 = 1124, 358
    self.butt5dmst = tk.Button(self.can, text="DMST 5", font=16,
        width=10, fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=lambda: dmst5(self))
    self.fbutt5dmst_window = self.can.create_window(self.x57,
        self.y57, window=self.butt5dmst)

    # Patient 6
    try:
        with open('./newpatient/entryfile6.txt', 'r') as namefile:
            line6 = namefile.readline()
    except FileNotFoundError as callfile6:
        print("[!] File entryfile6.txt doesn't exist !", callfile6)

    try:
        self.new_data6 = line6
        self.x60, self.y60 = 144, 390
        self.new_data6 = tk.StringVar()
        self.entrpat6f = tk.Entry(self.can, textvariable=self.new_data6,
            highlightbackground='grey', bd=4)
        if line6 == '------':
            line6 = line6
        else:
            line6 = line6[:-1]
        self.new_data6.set(line6)
        self.fentrpat6f_window = self.can.create_window(self.x60,
            self.y60, window=self.entrpat6f)
    except UnboundLocalError as ub_error6:
        print("[!] File 6 not created !", ub_error6)

    self.x61, self.y61 = 286, 390
    self.buttpat6up = tk.Button(self.can, text="Update 6", font=16,
        width=8, fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=lambda: updateLink(self, g=6))
    self.fbuttpat6up_window = self.can.create_window(self.x61,
        self.y61, window=self.buttpat6up)

    self.x62, self.y62 = 444, 390
    self.butt6diag = tk.Button(self.can, text="Diagnostic + ATCD 6",
        font=16, width=18, fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=lambda: diagstic(self, d=6))
    self.fbutt6diag_window = self.can.create_window(self.x62,
        self.y62, window=self.butt6diag)

    self.x64, self.y64 = 612, 390
    self.butt6med = tk.Button(self.can, text="Treatments 6", font=16,
        width=10, fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=lambda: tttMed6(self))
    self.fbutt6med_window = self.can.create_window(self.x64,
        self.y64, window=self.butt6med)

    self.x65, self.y65 = 740, 390
    self.butt6labo = tk.Button(self.can, text="Laboratory 6", font=16,
        width=10, fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=lambda: laboResult6(self))
    self.fbutt6labo_window = self.can.create_window(self.x65,
        self.y65, window=self.butt6labo)

    self.x66, self.y66 = 868, 390
    self.butt6vm = tk.Button(self.can, text="Medical Visit6", font=16,
        width=10, fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=self.visitMed6)
    self.fbutt6vm_window = self.can.create_window(self.x66,
        self.y66, window=self.butt6vm)

    self.x67, self.y67 = 996, 390
    self.butt6aux = tk.Button(self.can, text="Aux. Equip.6", font=16,
        width=10, fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=lambda: aux6(self))
    self.fbutt6aux_window = self.can.create_window(self.x67,
        self.y67, window=self.butt6aux)

    self.x68, self.y68 = 1124, 390
    self.butt6dmst = tk.Button(self.can, text="DMST 6", font=16,
        width=10, fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=lambda: dmst6(self))
    self.fbutt6dmst_window = self.can.create_window(self.x68,
        self.y68, window=self.butt6dmst)

    # Patient 7
    try:
        with open('./newpatient/entryfile7.txt', 'r') as namefile:
            line7 = namefile.readline()
    except FileNotFoundError as callfile7:
        print("[!] File entryfile7.txt doesn't exist !", callfile7)

    try:
        self.new_data7 = line7
        self.x70, self.y70 = 144, 422
        self.new_data7 = tk.StringVar()
        self.entrpat7f = tk.Entry(self.can, textvariable=self.new_data7,
            highlightbackground='grey', bd=4)
        if line7 == '-------':
            line7 = line7
        else:
            line7 = line7[:-1]
        self.new_data7.set(line7)
        self.fentrpat7f_window = self.can.create_window(self.x70,
            self.y70, window=self.entrpat7f)
    except UnboundLocalError as ub_error7:
        print("[!] File 7 not created !", ub_error7)

    self.x71, self.y71 = 286, 422
    self.buttpat7up = tk.Button(self.can, text="Update 7", font=16,
        width=8, fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=lambda: updateLink(self, g=7))
    self.fbuttpat7up_window = self.can.create_window(self.x71,
        self.y71, window=self.buttpat7up)

    self.x72, self.y72 = 444, 422
    self.butt7diag = tk.Button(self.can, text="Diagnostic + ATCD 7",
        font=16, width=18, fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=lambda: diagstic(self, d=7))
    self.fbutt7diag_window = self.can.create_window(self.x72,
        self.y72, window=self.butt7diag)

    self.x73, self.y73 = 612, 422
    self.butt7med = tk.Button(self.can, text="Treatments 7",
        font=16, width=10, fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=lambda: tttMed7(self))
    self.fbutt7med_window = self.can.create_window(self.x73,
        self.y73, window=self.butt7med)

    self.x74, self.y74 = 740, 422
    self.butt7labo = tk.Button(self.can, text="Laboratory 7",
        font=16, width=10, fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=lambda: laboResult7(self))
    self.fbutt7labo_window = self.can.create_window(self.x74,
        self.y74, window=self.butt7labo)

    self.x75, self.y75 = 868, 422
    self.butt7vm = tk.Button(self.can, text="Medical Visit7",
        font=16, width=10, fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=self.visitMed7)
    self.fbutt7vm_window = self.can.create_window(self.x75,
        self.y75, window=self.butt7vm)

    self.x76, self.y76 = 996, 422
    self.butt7aux = tk.Button(self.can, text="Aux. Equip.7",
        font=16, width=10, fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=lambda: aux7(self))
    self.fbutt7aux_window = self.can.create_window(self.x76,
        self.y76, window=self.butt7aux)

    self.x77, self.y77 = 1124, 422
    self.butt7dmst = tk.Button(self.can, text="DMST 7", font=16,
        width=10, fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=lambda: dmst7(self))
    self.fbutt7dmst_window = self.can.create_window(self.x77,
        self.y77, window=self.butt7dmst)

    # Patient 8
    try:
        with open('./newpatient/entryfile8.txt', 'r') as namefile:
            line8 = namefile.readline()
    except FileNotFoundError as callfile8:
        print("[!] File entryfile8.txt doesn't exist !", callfile8)

    try:
        self.new_data8 = line8
        self.x80, self.y80 = 144, 454
        self.new_data8 = tk.StringVar()
        self.entrpat8f = tk.Entry(self.can, textvariable=self.new_data8,
            highlightbackground='grey', bd=4)
        if line8 == '--------':
            line8 = line8
        else:
            line8 = line8[:-1]
        self.new_data8.set(line8)
        self.fentrpat8f_window = self.can.create_window(self.x80,
            self.y80, window=self.entrpat8f)
    except UnboundLocalError as ub_error8:
        print("[!] File 8 not created !", ub_error8)

    self.x81, self.y81 = 286, 454
    self.buttpat8up = tk.Button(self.can, text="Update 8", font=16,
        width=8, fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=lambda: updateLink(self, g=8))
    self.fbuttpat8up_window = self.can.create_window(self.x81,
        self.y81, window=self.buttpat8up)

    self.x82, self.y82 = 444, 454
    self.butt8diag = tk.Button(self.can, text="Diagnostic + ATCD 8",
        font=16, width=18, fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=lambda: diagstic(self, d=8))
    self.fbutt8diag_window = self.can.create_window(self.x82,
        self.y82, window=self.butt8diag)

    self.x83, self.y83 = 612, 454
    self.butt8med = tk.Button(self.can, text="Treatments 8", font=16,
        width=10, fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=lambda: tttMed8(self))
    self.fbutt8med_window = self.can.create_window(self.x83,
        self.y83, window=self.butt8med)

    self.x84, self.y84 = 740, 454
    self.butt8labo = tk.Button(self.can, text="Laboratory 8", font=16,
        width=10, fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=lambda: laboResult8(self))
    self.fbutt8labo_window = self.can.create_window(self.x84,
        self.y84, window=self.butt8labo)

    self.x85, self.y85 = 868, 454
    self.butt8vm = tk.Button(self.can, text="Medical Visit8", font=16,
        width=10, fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=self.visitMed8)
    self.fbutt8vm_window = self.can.create_window(self.x85,
        self.y85, window=self.butt8vm)

    self.x86, self.y86 = 996, 454
    self.butt8aux = tk.Button(self.can, text="Aux. Equip.8", font=16,
        width=10, fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=lambda: aux8(self))
    self.fbutt8aux_window = self.can.create_window(self.x86,
        self.y86, window=self.butt8aux)

    self.x87, self.y87 = 1124, 454
    self.butt8dmst = tk.Button(self.can, text="DMST 8", font=16,
        width=10, fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=lambda: dmst8(self))
    self.fbutt8dmst_window = self.can.create_window(self.x87,
        self.y87, window=self.butt8dmst)

    # Patient 9
    try:
        with open('./newpatient/entryfile9.txt', 'r') as namefile:
            line9 = namefile.readline()
    except FileNotFoundError as callfile9:
        print("[!] File entryfile9.txt doesn't exist !", callfile9)

    try:
        self.new_data9 = line9
        self.x90, self.y90 = 144, 486
        self.new_data9 = tk.StringVar()
        self.entrpat9f = tk.Entry(self.can, textvariable=self.new_data9,
            highlightbackground='grey', bd=4)
        if line9 == '---------':
            line9 = line9
        else:
            line9 = line9[:-1]
        self.new_data9.set(line9)
        self.fentrpat9f_window = self.can.create_window(self.x90,
            self.y90, window=self.entrpat9f)
    except UnboundLocalError as ub_error9:
        print("[!] File 9 not created !", ub_error9)

    self.x91, self.y91 = 286, 486
    self.buttpat9up = tk.Button(self.can, text="Update 9",
        font=16, width=8, fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=lambda: updateLink(self, g=9))
    self.fbuttpat9up_window = self.can.create_window(self.x91,
        self.y91, window=self.buttpat9up)

    self.x92, self.y92 = 444, 486
    self.butt9diag = tk.Button(self.can, text="Diagnostic + ATCD 9",
        font=16, width=18, fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=lambda: diagstic(self, d=9))
    self.fbutt9diag_window = self.can.create_window(self.x92,
        self.y92, window=self.butt9diag)

    self.x93, self.y93 = 612, 486
    self.butt9med = tk.Button(self.can, text="Treatments 9",
        font=16, width=10, fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=lambda: tttMed9(self))
    self.fbutt9med_window = self.can.create_window(self.x93,
        self.y93, window=self.butt9med)

    self.x94, self.y94 = 740, 486
    self.butt9labo = tk.Button(self.can, text="Laboratory 9",
        font=16, width=10, fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=lambda: laboResult9(self))
    self.fbutt9labo_window = self.can.create_window(self.x94,
        self.y94, window=self.butt9labo)

    self.x95, self.y95 = 868, 486
    self.butt9vm = tk.Button(self.can, text="Medical Visit9",
        font=16, width=10, fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=self.visitMed9)
    self.fbutt9vm_window = self.can.create_window(self.x95,
        self.y95, window=self.butt9vm)

    self.x96, self.y96 = 996, 486
    self.butt9aux = tk.Button(self.can, text="Aux. Equip.9",
        font=16, width=10, fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=lambda: aux9(self))
    self.fbutt9aux_window = self.can.create_window(self.x96,
        self.y96, window=self.butt9aux)

    self.x97, self.y97 = 1124, 486
    self.butt9dmst = tk.Button(self.can, text="DMST 9",
        font=16, width=10, fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=lambda: dmst9(self))
    self.fbutt9dmst_window = self.can.create_window(self.x97,
        self.y97, window=self.butt9dmst)

    # Patient 10
    try:
        with open('./newpatient/entryfile10.txt', 'r') as namefile:
            line10 = namefile.readline()
    except FileNotFoundError as callfile10:
        print("[!] File entryfile10.txt doesn't exist !", callfile10)

    try:
        self.new_data10 = line10
        self.x100, self.y100 = 144, 518
        self.new_data10 = tk.StringVar()
        self.entrpat10f = tk.Entry(self.can, textvariable=self.new_data10,
            highlightbackground='grey', bd=4)
        if line10 == '----------':
            line10 = line10
        else:
            line10 = line10[:-1]
        self.new_data10.set(line10)
        self.fentrpat10f_window = self.can.create_window(self.x100,
            self.y100, window=self.entrpat10f)
    except UnboundLocalError as ub_error10:
        print("[!] File 10 not created !", ub_error10)

    self.x101, self.y101 = 286, 518
    self.buttpat10up = tk.Button(self.can, text="Update 10", font=16, width=8,
        fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=lambda: updateLink(self, g=10))
    self.fbuttpat10up_window = self.can.create_window(self.x101,
        self.y101, window=self.buttpat10up)

    self.x102, self.y102 = 444, 518
    self.butt10diag = tk.Button(self.can, text="Diagnostic + ATCD 10",
        font=16, width=18, fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=lambda: diagstic(self, d=10))
    self.fbutt10diag_window = self.can.create_window(self.x102,
        self.y102, window=self.butt10diag)

    self.x103, self.y103 = 612, 518
    self.butt10med = tk.Button(self.can, text="Treatments 10", font=16,
        width=10, fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=lambda: tttMed10(self))
    self.fbutt10med_window = self.can.create_window(self.x103,
        self.y103, window=self.butt10med)

    self.x104, self.y104 = 740, 518
    self.butt10labo = tk.Button(self.can, text="Laboratory 10", font=16,
        width=10, fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=lambda: laboResult10(self))
    self.fbutt10labo_window = self.can.create_window(self.x104,
        self.y104, window=self.butt10labo)

    self.x105, self.y105 = 868, 518
    self.butt10vm = tk.Button(self.can, text="Medical Visit10",
        font=16, width=10, fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=self.visitMed10)
    self.fbutt10vm_window = self.can.create_window(self.x105,
        self.y105, window=self.butt10vm)

    self.x106, self.y106 = 996, 518
    self.butt10aux = tk.Button(self.can, text="Aux. Equip.10", font=16,
        width=10, fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=lambda: aux10(self))
    self.fbutt10aux_window = self.can.create_window(self.x106,
        self.y106, window=self.butt10aux)

    self.x107, self.y107 = 1124, 518
    self.butt10dmst = tk.Button(self.can, text="DMST 10", font=16,
        width=10, fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=lambda: dmst10(self))
    self.fbutt10dmst_window = self.can.create_window(self.x107,
        self.y107, window=self.butt10dmst)

    # Patient 11
    try:
        with open('./newpatient/entryfile11.txt', 'r') as namefile:
            line11 = namefile.readline()
    except FileNotFoundError as callfile11:
        print("[!] File entryfile11.txt doesn't exist !", callfile11)

    try:
        self.new_data11 = line11
        self.x110, self.y110 = 144, 550
        self.new_data11 = tk.StringVar()
        self.entrpat11f = tk.Entry(self.can, textvariable=self.new_data11,
            highlightbackground='grey', bd=4)
        if line11 == '-----------':
            line11 = line11
        else:
            line11 = line11[:-1]
        self.new_data11.set(line11)
        self.fentrpat11f_window = self.can.create_window(self.x110,
            self.y110, window=self.entrpat11f)
    except UnboundLocalError as ub_error11:
        print("[!] File 11 not created !", ub_error11)

    self.x111, self.y111 = 286, 550
    self.buttpat11up = tk.Button(self.can, text="Update 11", font=16,
        width=8, fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=lambda: updateLink(self, g=11))
    self.fbuttpat11up_window = self.can.create_window(self.x111,
        self.y111, window=self.buttpat11up)

    self.x112, self.y112 = 444, 550
    self.butt11diag = tk.Button(self.can, text="Diagnostic + ATCD 11",
        font=16, width=18, fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=lambda: diagstic(self, d=11))
    self.fbutt11diag_window = self.can.create_window(self.x112,
        self.y112, window=self.butt11diag)

    self.x113, self.y113 = 612, 550
    self.butt11med = tk.Button(self.can, text="Treatments 11", font=16,
        width=10, fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=lambda: tttMed11(self))
    self.fbutt11med_window = self.can.create_window(self.x113,
        self.y113, window=self.butt11med)

    self.x114, self.y114 = 740, 550
    self.butt11labo = tk.Button(self.can, text="Laboratory 11", font=16,
        width=10, fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=lambda: laboResult11(self))
    self.fbutt11labo_window = self.can.create_window(self.x114,
        self.y114, window=self.butt11labo)

    self.x115, self.y115 = 868, 550
    self.butt11vm = tk.Button(self.can, text="Medical Visit11",
        font=16, width=10, fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=self.visitMed11)
    self.fbutt11vm_window = self.can.create_window(self.x115,
        self.y115, window=self.butt11vm)

    self.x116, self.y116 = 996, 550
    self.butt11aux = tk.Button(self.can, text="Aux. Equip.11",
        font=16, width=10, fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=lambda: aux11(self))
    self.fbutt11aux_window = self.can.create_window(self.x116,
        self.y116, window=self.butt11aux)

    self.x117, self.y117 = 1124, 550
    self.butt11dmst = tk.Button(self.can, text="DMST 11", font=16,
        width=10, fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=lambda: dmst11(self))
    self.fbutt11dmst_window = self.can.create_window(self.x117,
        self.y117, window=self.butt11dmst)

    # Patient 12
    try:
        with open('./newpatient/entryfile12.txt', 'r') as namefile:
            line12 = namefile.readline()
    except FileNotFoundError as callfile12:
        print("[!] File entryfile12.txt doesn't exist !", callfile12)

    try:
        self.new_data12 = line12
        self.x120, self.y120 = 144, 582
        self.new_data12 = tk.StringVar()
        self.entrpat12f = tk.Entry(self.can, textvariable=self.new_data12,
            highlightbackground='grey', bd=4)
        if line12 == '------------':
            line12 = line12
        else:
            line12 = line12[:-1]
        self.new_data12.set(line12)
        self.fentrpat12f_window = self.can.create_window(self.x120,
            self.y120, window=self.entrpat12f)
    except UnboundLocalError as ub_error12:
        print("[!] File 12 not created !", ub_error12)

    self.x121, self.y121 = 286, 582
    self.buttpat12up = tk.Button(self.can, text="Update 12", font=16,
        width=8, fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=lambda: updateLink(self, g=12))
    self.fbuttpat12up_window = self.can.create_window(self.x121,
        self.y121, window=self.buttpat12up)

    self.x122, self.y122 = 444, 582
    self.butt12diag = tk.Button(self.can, text="Diagnostic + ATCD 12",
        font=16, width=18, fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=lambda: diagstic(self, d=12))
    self.fbutt12diag_window = self.can.create_window(self.x122,
        self.y122, window=self.butt12diag)

    self.x123, self.y123 = 612, 582
    self.butt12med = tk.Button(self.can, text="Treatments 12",
        font=16, width=10, fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=lambda: tttMed12(self))
    self.fbutt12med_window = self.can.create_window(self.x123,
        self.y123, window=self.butt12med)

    self.x124, self.y124 = 740, 582
    self.butt12labo = tk.Button(self.can, text="Laboratory 12", font=16,
        width=10, fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=lambda: laboResult12(self))
    self.fbutt12labo_window = self.can.create_window(self.x124,
        self.y124, window=self.butt12labo)

    self.x125, self.y125 = 868, 582
    self.butt12vm = tk.Button(self.can, text="Medical Visit12",
        font=16, width=10, fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=self.visitMed12)
    self.fbutt12vm_window = self.can.create_window(self.x125,
        self.y125, window=self.butt12vm)

    self.x126, self.y126 = 996, 582
    self.butt12aux = tk.Button(self.can, text="Aux. Equip.12", font=16,
        width=10, fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=lambda: aux12(self))
    self.fbutt12aux_window = self.can.create_window(self.x126,
        self.y126, window=self.butt12aux)

    self.x127, self.y127 = 1124, 582
    self.butt12dmst = tk.Button(self.can, text="DMST 12", font=16,
        width=10, fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=lambda: dmst12(self))
    self.fbutt12dmst_window = self.can.create_window(self.x127,
        self.y127, window=self.butt12dmst)

    # Patient 13
    try:
        with open('./newpatient/entryfile13.txt', 'r') as namefile:
            line13 = namefile.readline()
    except FileNotFoundError as callfile13:
        print("[!] File entryfile13.txt doesn't exist !", callfile13)

    try:
        self.new_data13 = line13
        self.x130, self.y130 = 144, 614
        self.new_data13 = tk.StringVar()
        self.entrpat13f = tk.Entry(self.can, textvariable=self.new_data13,
            highlightbackground='grey', bd=4)
        if line13 == '-------------':
            line13 = line13
        else:
            line13 = line13[:-1]
        self.new_data13.set(line13)
        self.fentrpat13f_window = self.can.create_window(self.x130,
            self.y130, window=self.entrpat13f)
    except UnboundLocalError as ub_error13:
        print("[!] File 13 not created !", ub_error13)

    self.x131, self.y131 = 286, 614
    self.buttpat13up = tk.Button(self.can, text="Update 13", font=16,
        width=8, fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=lambda: updateLink(self, g=13))
    self.fbuttpat13up_window = self.can.create_window(self.x131,
        self.y131, window=self.buttpat13up)

    self.x132, self.y132 = 444, 614
    self.butt13diag = tk.Button(self.can, text="Diagnostic + ATCD 13",
        font=16, width=18, fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=lambda: diagstic(self, d=13))
    self.fbutt13diag_window = self.can.create_window(self.x132,
        self.y132, window=self.butt13diag)

    self.x133, self.y133 = 612, 614
    self.butt13med = tk.Button(self.can, text="Treatments 13",
        font=16, width=10, fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=lambda: tttMed13(self))
    self.fbutt13med_window = self.can.create_window(self.x133,
        self.y133, window=self.butt13med)

    self.x134, self.y134 = 740, 614
    self.butt13labo = tk.Button(self.can, text="Laboratory 13",
        font=16, width=10, fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=lambda: laboResult13(self))
    self.fbutt13labo_window = self.can.create_window(self.x134,
        self.y134, window=self.butt13labo)

    self.x135, self.y135 = 868, 614
    self.butt13vm = tk.Button(self.can, text="Medical Visit13",
        font=16, width=10, fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=self.visitMed13)
    self.fbutt13vm_window = self.can.create_window(self.x135,
        self.y135, window=self.butt13vm)

    self.x136, self.y136 = 996, 614
    self.butt13aux = tk.Button(self.can, text="Aux. Equip.13",
        font=16, width=10, fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=lambda: aux13(self))
    self.fbutt13aux_window = self.can.create_window(self.x136,
        self.y136, window=self.butt13aux)

    self.x137, self.y137 = 1124, 614
    self.butt13dmst = tk.Button(self.can, text="DMST 13", font=16,
        width=10, fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=lambda: dmst13(self))
    self.fbutt13dmst_window = self.can.create_window(self.x137,
        self.y137, window=self.butt13dmst)

    # Patient 14
    try:
        with open('./newpatient/entryfile14.txt', 'r') as namefile:
            line14 = namefile.readline()
    except FileNotFoundError as callfile14:
        print("[!] File entryfile14.txt doesn't exist !", callfile14)

    try:
        self.new_data14 = line14
        self.x140, self.y140 = 144, 646
        self.new_data14 = tk.StringVar()
        self.entrpat14f = tk.Entry(self.can, textvariable=self.new_data14,
            highlightbackground='grey', bd=4)
        if line14 == '--------------':
            line14 = line14
        else:
            line14 = line14[:-1]
        self.new_data14.set(line14)
        self.fentrpat14f_window = self.can.create_window(self.x140,
            self.y140, window=self.entrpat14f)
    except UnboundLocalError as ub_error14:
        print("[!] File 14 not created !", ub_error14)

    self.x141, self.y141 = 286, 646
    self.buttpat14up = tk.Button(self.can, text="Update 14", font=16,
        width=8, fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=lambda: updateLink(self, g=14))
    self.fbuttpat14up_window = self.can.create_window(self.x141,
        self.y141, window=self.buttpat14up)

    self.x142, self.y142 = 444, 646
    self.butt14diag = tk.Button(self.can, text="Diagnostic + ATCD 14",
        font=16, width=18, fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=lambda: diagstic(self, d=14))
    self.fbutt14diag_window = self.can.create_window(self.x142,
        self.y142, window=self.butt14diag)

    self.x143, self.y143 = 612, 646
    self.butt14med = tk.Button(self.can, text="Treatments 14", font=16,
        width=10, fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=lambda: tttMed14(self))
    self.fbutt14med_window = self.can.create_window(self.x143,
        self.y143, window=self.butt14med)

    self.x144, self.y144 = 740, 646
    self.butt14labo = tk.Button(self.can, text="Laboratory 14", font=16,
        width=10, fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=lambda: laboResult14(self))
    self.fbutt14labo_window = self.can.create_window(self.x144,
        self.y144, window=self.butt14labo)

    self.x145, self.y145 = 868, 646
    self.butt14vm = tk.Button(self.can, text="Medical Visit14",
        font=16, width=10, fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=self.visitMed14)
    self.fbutt14vm_window = self.can.create_window(self.x145,
        self.y145, window=self.butt14vm)

    self.x146, self.y146 = 996, 646
    self.butt14aux = tk.Button(self.can, text="Aux. Equip.14", font=16,
        width=10, fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=lambda: aux14(self))
    self.fbutt14aux_window = self.can.create_window(self.x146,
        self.y146, window=self.butt14aux)

    self.x147, self.y147 = 1124, 646
    self.butt14dmst = tk.Button(self.can, text="DMST 14", font=16,
        width=10, fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=lambda: dmst14(self))
    self.fbutt14dmst_window = self.can.create_window(self.x147,
        self.y147, window=self.butt14dmst)

    # Patient 15 --> to be continue (align)
    try:
        with open('./newpatient/entryfile15.txt', 'r') as namefile:
            line15 = namefile.readline()
    except FileNotFoundError as callfile15:
        print("[!] File entryfile15.txt doesn't exist !", callfile15)

    try:
        self.new_data15 = line15
        self.x150, self.y150 = 144, 678
        self.new_data15 = tk.StringVar()
        self.entrpat15f = tk.Entry(self.can, textvariable=self.new_data15,
            highlightbackground='grey', bd=4)
        if line15 == '---------------':
            line15 = line15
        else:
            line15 = line15[:-1]
        self.new_data15.set(line15)
        self.fentrpat15f_window = self.can.create_window(self.x150,
            self.y150, window=self.entrpat15f)
    except UnboundLocalError as ub_error15:
        print("[!] File 15 not created !", ub_error15)

    self.x151, self.y151 = 286, 678
    self.buttpat15up = tk.Button(self.can, width=8, font=16,
        fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise', text="Update 15",
        command=lambda: updateLink(self, g=15))
    self.fbuttpat15up_window = self.can.create_window(self.x151,
        self.y151, window=self.buttpat15up)

    self.x152, self.y152 = 444, 678
    self.butt15diag = tk.Button(self.can, width=18, font=16,
        fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise', text="Diagnostic + ATCD 15",
        command=lambda: diagstic(self, d=15))
    self.fbutt15diag_window = self.can.create_window(self.x152,
        self.y152, window=self.butt15diag)

    self.x153, self.y153 = 612, 678
    self.butt15med = tk.Button(self.can, width=10, font=16,
        fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise', text="Treatments 15",
        command=lambda: tttMed15(self))
    self.fbutt15med_window = self.can.create_window(self.x153,
        self.y153, window=self.butt15med)

    self.x154, self.y154 = 740, 678
    self.butt15labo = tk.Button(self.can, width=10, font=16,
        fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise', text="Laboratory 15",
        command=lambda: laboResult15(self))
    self.fbutt15labo_window = self.can.create_window(self.x154,
        self.y154, window=self.butt15labo)

    self.x155, self.y155 = 868, 678
    self.butt15vm = tk.Button(self.can, width=10, font=16,
        fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise', text="Medical Visit15",
        command=self.visitMed15)
    self.fbutt15vm_window = self.can.create_window(self.x155,
        self.y155, window=self.butt15vm)

    self.x156, self.y156 = 996, 678
    self.butt15aux = tk.Button(self.can, width=10, font=16,
        fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise', text="Aux. Equip.15",
        command=lambda: aux15(self))
    self.fbutt15aux_window = self.can.create_window(self.x156,
        self.y156, window=self.butt15aux)

    self.x157, self.y157 = 1124, 678
    self.butt15dmst = tk.Button(self.can, width=10, font=16,
        fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise', text="DMST 15",
        command=lambda: dmst15(self))
    self.fbutt15dmst_window = self.can.create_window(self.x157,
        self.y157, window=self.butt15dmst)

    # Patient 16
    try:
        with open('./newpatient/entryfile16.txt', 'r') as namefile:
            line16 = namefile.readline()
    except FileNotFoundError as callfile16:
        print("[!] File entryfile16.txt doesn't exist !", callfile16)

    try:
        self.new_data16 = line16
        self.x160, self.y160 = 144, 710
        self.new_data16 = tk.StringVar()
        self.entrpat16f = tk.Entry(self.can, textvariable=self.new_data16,
            highlightbackground='grey', bd=4)
        if line16 == '----------------':
            line16 = line16
        else:
            line16 = line16[:-1]
        self.new_data16.set(line16)
        self.fentrpat16f_window = self.can.create_window(self.x160,
            self.y160, window=self.entrpat16f)
    except UnboundLocalError as ub_error16:
        print("[!] File 16 not created !", ub_error16)

    self.x161, self.y161 = 286, 710
    self.buttpat16up = tk.Button(self.can, width=8, font=16,
        fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise', text="Update 16",
        command=lambda: updateLink(self, g=16))
    self.fbuttpat16up_window = self.can.create_window(self.x161,
        self.y161, window=self.buttpat16up)

    self.x162, self.y162 = 444, 710
    self.butt16diag = tk.Button(self.can, width=18, font=16,
        fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise', text="Diagnostic + ATCD 16",
        command=lambda: diagstic(self, d=16))
    self.fbutt16diag_window = self.can.create_window(self.x162,
        self.y162, window=self.butt16diag)

    self.x163, self.y163 = 612, 710
    self.butt16med = tk.Button(self.can, width=10, font=16,
        fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise', text="Treatments 16",
        command=lambda: tttMed16(self))
    self.fbutt16med_window = self.can.create_window(self.x163,
        self.y163, window=self.butt16med)

    self.x164, self.y164 = 740, 710
    self.butt16labo = tk.Button(self.can, width=10, font=16,
        fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise', text="Laboratory 16",
        command=lambda: laboResult16(self))
    self.fbutt16labo_window = self.can.create_window(self.x164,
        self.y164, window=self.butt16labo)

    self.x165, self.y165 = 868, 710
    self.butt16vm = tk.Button(self.can, width=10, font=16,
        fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise', text="Medical Visit16",
        command=self.visitMed16)
    self.fbutt16vm_window = self.can.create_window(self.x165,
        self.y165, window=self.butt16vm)

    self.x166, self.y166 = 996, 710
    self.butt16aux = tk.Button(self.can, width=10, font=16,
        fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise', text="Aux. Equip.16",
        command=lambda: aux16(self))
    self.fbutt16aux_window = self.can.create_window(self.x166,
        self.y166, window=self.butt16aux)

    self.x167, self.y167 = 1124, 710
    self.butt16dmst = tk.Button(self.can, width=10, font=16,
        fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise', text="DMST 16",
        command=lambda: dmst16(self))
    self.fbutt16dmst_window = self.can.create_window(self.x167,
        self.y167, window=self.butt16dmst)

    # Patient 17
    try:
        with open('./newpatient/entryfile17.txt', 'r') as namefile:
            line17 = namefile.readline()
    except FileNotFoundError as callfile17:
        print("[!] File entryfile17.txt doesn't exist !", callfile17)

    try:
        self.new_data17 = line17
        self.x170, self.y170 = 144, 742
        self.new_data17 = tk.StringVar()
        self.entrpat17f = tk.Entry(self.can, textvariable=self.new_data17,
            highlightbackground='grey', bd=4)
        if line17 == '-----------------':
            line17 = line17
        else:
            line17 = line17[:-1]
        self.new_data17.set(line17)
        self.fentrpat17f_window = self.can.create_window(self.x170,
            self.y170, window=self.entrpat17f)
    except UnboundLocalError as ub_error17:
        print("[!] File 17 not created !", ub_error17)

    self.x171, self.y171 = 286, 742
    self.buttpat17up = tk.Button(self.can, width=8, font=16,
        fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise', text="Update 17",
        command=lambda: updateLink(self, g=17))
    self.fbuttpat17up_window = self.can.create_window(self.x171,
        self.y171, window=self.buttpat17up)

    self.x172, self.y172 = 444, 742
    self.butt17diag = tk.Button(self.can, width=18, font=16,
        fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise', text="Diagnostic + ATCD 17",
        command=lambda: diagstic(self, d=17))
    self.fbutt17diag_window = self.can.create_window(self.x172,
        self.y172, window=self.butt17diag)

    self.x173, self.y173 = 612, 742
    self.butt17med = tk.Button(self.can, width=10, font=16,
        fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise', text="Treatments 17",
        command=lambda: tttMed17(self))
    self.fbutt17med_window = self.can.create_window(self.x173,
        self.y173, window=self.butt17med)

    self.x174, self.y174 = 740, 742
    self.butt17labo = tk.Button(self.can, width=10, font=16,
        fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise', text="Laboratory 17",
        command=lambda: laboResult17(self))
    self.fbutt17labo_window = self.can.create_window(self.x174,
        self.y174, window=self.butt17labo)

    self.x175, self.y175 = 868, 742
    self.butt17vm = tk.Button(self.can, width=10, font=16,
        fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise', text="Medical Visit17",
        command=self.visitMed17)
    self.fbutt17vm_window = self.can.create_window(self.x175,
        self.y175, window=self.butt17vm)

    self.x176, self.y176 = 996, 742
    self.butt17aux = tk.Button(self.can, width=10, font=16,
        fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise', text="Aux. Equip.17",
        command=lambda: aux17(self))
    self.fbutt17aux_window = self.can.create_window(self.x176,
        self.y176, window=self.butt17aux)

    self.x177, self.y177 = 1124, 742
    self.butt17dmst = tk.Button(self.can, width=10, font=16,
        fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise', text="DMST 17",
        command=lambda: dmst17(self))
    self.fbutt17dmst_window = self.can.create_window(self.x177,
        self.y177, window=self.butt17dmst)

    # Patient 18
    try:
        with open('./newpatient/entryfile18.txt', 'r') as namefile:
            line18 = namefile.readline()
    except FileNotFoundError as callfile18:
        print("[!] File entryfile18.txt doesn't exist !", callfile18)

    try:
        self.new_data18 = line18
        self.x180, self.y180 = 144, 774
        self.new_data18 = tk.StringVar()
        self.entrpat18f = tk.Entry(self.can, textvariable=self.new_data18,
            highlightbackground='grey', bd=4)
        if line18 == '------------------':
            line18 = line18
        else:
            line18 = line18[:-1]
        self.new_data18.set(line18)
        self.fentrpat18f_window = self.can.create_window(self.x180,
            self.y180, window=self.entrpat18f)
    except UnboundLocalError as ub_error18:
        print("[!] File 18 not created !", ub_error18)

    self.x181, self.y181 = 286, 774
    self.buttpat18up = tk.Button(self.can, width=8, font=16,
        fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise', text="Update 18",
        command=lambda: updateLink(self, g=18))
    self.fbuttpat18up_window = self.can.create_window(self.x181,
        self.y181, window=self.buttpat18up)

    self.x182, self.y182 = 444, 774
    self.butt18diag = tk.Button(self.can, width=18, font=16,
        fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise', text="Diagnostic + ATCD 18",
        command=lambda: diagstic(self, d=18))
    self.fbutt18diag_window = self.can.create_window(self.x182,
        self.y182, window=self.butt18diag)

    self.x183, self.y183 = 612, 774
    self.butt18med = tk.Button(self.can, width=10, font=16,
        fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise', text="Treatments 18",
        command=lambda: tttMed18(self))
    self.fbutt18med_window = self.can.create_window(self.x183,
        self.y183, window=self.butt18med)

    self.x184, self.y184 = 740, 774
    self.butt18labo = tk.Button(self.can, width=10, font=16,
        fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise', text="Laboratory 18",
        command=lambda: laboResult18(self))
    self.fbutt18labo_window = self.can.create_window(self.x184,
        self.y184, window=self.butt18labo)

    self.x185, self.y185 = 868, 774
    self.butt18vm = tk.Button(self.can, width=10, font=16,
        fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise', text="Medical Visit18",
        command=self.visitMed18)
    self.fbutt18vm_window = self.can.create_window(self.x185,
        self.y185, window=self.butt18vm)

    self.x186, self.y186 = 996, 774
    self.butt18aux = tk.Button(self.can, width=10, font=16,
        fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise', text="Aux. Equip.18",
        command=lambda: aux18(self))
    self.fbutt18aux_window = self.can.create_window(self.x186,
        self.y186, window=self.butt18aux)

    self.x187, self.y187 = 1124, 774
    self.butt18dmst = tk.Button(self.can, width=10, font=16,
        fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise', text="DMST 18",
        command=lambda: dmst18(self))
    self.fbutt18dmst_window = self.can.create_window(self.x187,
        self.y187, window=self.butt18dmst)

    # Patient 19
    try:
        with open('./newpatient/entryfile19.txt', 'r') as namefile:
            line19 = namefile.readline()
    except FileNotFoundError as callfile19:
        print("[!] File entryfile19.txt doesn't exist !", callfile19)

    try:
        self.new_data19 = line19
        self.x190, self.y190 = 144, 806
        self.new_data19 = tk.StringVar()
        self.entrpat19f = tk.Entry(self.can, textvariable=self.new_data19,
            highlightbackground='grey', bd=4)
        if line19 == '-------------------':
            line19 = line19
        else:
            line19 = line19[:-1]
        self.new_data19.set(line19)
        self.fentrpat19f_window = self.can.create_window(self.x190,
            self.y190, window=self.entrpat19f)
    except UnboundLocalError as ub_error19:
        print("[!] File 19 not created !", ub_error19)

    self.x191, self.y191 = 286, 806
    self.buttpat19up = tk.Button(self.can, width=8, font=16,
        fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise', text="Update 19",
        command=lambda: updateLink(self, g=19))
    self.fbuttpat19up_window = self.can.create_window(self.x191,
        self.y191, window=self.buttpat19up)

    self.x192, self.y192 = 444, 806
    self.butt19diag = tk.Button(self.can, width=18, font=16,
        fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise', text="Diagnostic + ATCD 19",
        command=lambda: diagstic(self, d=19))
    self.fbutt19diag_window = self.can.create_window(self.x192,
        self.y192, window=self.butt19diag)

    self.x193, self.y193 = 612, 806
    self.butt19med = tk.Button(self.can, width=10, font=16,
        fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise', text="Treatments 19",
        command=lambda: tttMed19(self))
    self.fbutt19med_window = self.can.create_window(self.x193,
        self.y193, window=self.butt19med)

    self.x194, self.y194 = 740, 806
    self.butt19labo = tk.Button(self.can, width=10, font=16,
        fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise', text="Laboratory 19",
        command=lambda: laboResult19(self))
    self.fbutt19labo_window = self.can.create_window(self.x194,
        self.y194, window=self.butt19labo)

    self.x195, self.y195 = 868, 806
    self.butt19vm = tk.Button(self.can, width=10, font=16,
        fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise', text="Medical Visit19",
        command=self.visitMed19)
    self.fbutt19vm_window = self.can.create_window(self.x195,
        self.y195, window=self.butt19vm)

    self.x196, self.y196 = 996, 806
    self.butt19aux = tk.Button(self.can, width=10, font=16,
        fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise', text="Aux. Equip.19",
        command=lambda: aux19(self))
    self.fbutt19aux_window = self.can.create_window(self.x196,
        self.y196, window=self.butt19aux)

    self.x197, self.y197 = 1124, 806
    self.butt19dmst = tk.Button(self.can, width=10, font=16,
        fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise', text="DMST 19",
        command=lambda: dmst19(self))
    self.fbutt19dmst_window = self.can.create_window(self.x197,
        self.y197, window=self.butt19dmst)

    # Patient 20
    try:
        with open('./newpatient/entryfile20.txt', 'r') as namefile:
            line20 = namefile.readline()
    except FileNotFoundError as callfile20:
        print("[!] File entryfile20.txt doesn't exist !", callfile20)

    try:
        self.new_data20 = line20
        self.x200, self.y200 = 144, 838
        self.new_data20 = tk.StringVar()
        self.entpat20f = tk.Entry(self.can, textvariable=self.new_data20,
            highlightbackground='grey', bd=4)
        if line20 == '--------------------':
            line20 = line20
        else:
            line20 = line20[:-1]
        self.new_data20.set(line20)
        self.fentpat20f_window = self.can.create_window(self.x200,
            self.y200, window=self.entpat20f)
    except UnboundLocalError as ub_error20:
        print("[!] File 20 not created !", ub_error20)

    self.x201, self.y201 = 286, 838
    self.butpat20up = tk.Button(self.can, width=8, font=16,
        fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise', text="Update 20",
        command=lambda: updateLink(self, g=20))
    self.fbutpat20up_window = self.can.create_window(self.x201,
        self.y201, window=self.butpat20up)

    self.x202, self.y202 = 444, 838
    self.but20diag = tk.Button(self.can, width=18, font=16,
        fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise', text="Diagnostic + ATCD 20",
        command=lambda: diagstic(self, d=20))
    self.fbut20diag_window = self.can.create_window(self.x202,
        self.y202, window=self.but20diag)

    self.x203, self.y203 = 612, 838
    self.but20med = tk.Button(self.can, width=10, font=16,
        fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise', text="Treatments 20",
        command=lambda: tttMed20(self))
    self.fbut20med_window = self.can.create_window(self.x203,
        self.y203, window=self.but20med)

    self.x204, self.y204 = 740, 838
    self.but20labo = tk.Button(self.can, width=10, font=16,
        fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise', text="Laboratory 20",
        command=lambda: laboResult20(self))
    self.fbut20labo_window = self.can.create_window(self.x204,
        self.y204, window=self.but20labo)

    self.x205, self.y205 = 868, 838
    self.but20vm = tk.Button(self.can, width=10, font=16,
        fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise', text="Medical Visit20",
        command=self.visitMed20)
    self.fbut20vm_window = self.can.create_window(self.x205,
        self.y205, window=self.but20vm)

    self.x206, self.y206 = 996, 838
    self.but20aux = tk.Button(self.can, width=10, font=16,
        fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise', text="Aux. Equip.20",
        command=lambda: aux20(self))
    self.fbut20aux_window = self.can.create_window(self.x206,
        self.y206, window=self.but20aux)

    self.x207, self.y207 = 1124, 838
    self.but20dmst = tk.Button(self.can, width=10, font=16,
        fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise', text="DMST 20",
        command=lambda: dmst20(self))
    self.fbut20dmst_window = self.can.create_window(self.x207,
        self.y207, window=self.but20dmst)

    # Patient 21
    try:
        with open('./newpatient/entryfile21.txt', 'r') as namefile:
            line21 = namefile.readline()
    except FileNotFoundError as callfile21:
        print("[!] File entryfile21.txt doesn't exist !", callfile21)

    try:
        self.new_data21 = line21
        self.x210, self.y210 = 144, 870
        self.new_data21 = tk.StringVar()
        self.entpat21f = tk.Entry(self.can, textvariable=self.new_data21,
            highlightbackground='grey', bd=4)
        if line21 == '---------------------':
            line21 = line21
        else:
            line21 = line21[:-1]
        self.new_data21.set(line21)
        self.fentpat21f_window = self.can.create_window(self.x210,
            self.y210, window=self.entpat21f)
    except UnboundLocalError as ub_error21:
        print("[!] File 21 not created !", ub_error21)

    self.x211, self.y211 = 286, 870
    self.butpat21up = tk.Button(self.can, width=8, font=16,
        fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise', text="Update 21",
        command=lambda: updateLink(self, g=21))
    self.fbutpat21up_window = self.can.create_window(self.x211,
        self.y211, window=self.butpat21up)

    self.x212, self.y212 = 444, 870
    self.butt21diag = tk.Button(self.can, width=18, font=16,
        fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise', text="Diagnostic + ATCD 21",
        command=lambda: diagstic(self, d=21))
    self.fbutt21diag_window = self.can.create_window(self.x212,
        self.y212, window=self.butt21diag)

    self.x213, self.y213 = 612, 870
    self.butt21med = tk.Button(self.can, width=10, font=16,
        fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise', text="Treatments 21",
        command=lambda: tttMed21(self))
    self.fbutt21med_window = self.can.create_window(self.x213,
        self.y213, window=self.butt21med)

    self.x214, self.y214 = 740, 870
    self.butt21labo = tk.Button(self.can, width=10, font=16,
        fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise', text="Laboratory 21",
        command=lambda: laboResult21(self))
    self.fbutt21labo_window = self.can.create_window(self.x214,
        self.y214, window=self.butt21labo)

    self.x215, self.y215 = 868, 870
    self.butt21vm = tk.Button(self.can, width=10, font=16,
        fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise', text="Medical Visit21",
        command=self.visitMed21)
    self.fbutt21vm_window = self.can.create_window(self.x215,
        self.y215, window=self.butt21vm)

    self.x216, self.y216 = 996, 870
    self.butt21aux = tk.Button(self.can, width=10, font=16,
        fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise', text="Aux. Equip.21",
        command=lambda: aux21(self))
    self.fbutt21aux_window = self.can.create_window(self.x216,
        self.y216, window=self.butt21aux)

    self.x217, self.y217 = 1124, 870
    self.butt21dmst = tk.Button(self.can, width=10, font=16,
        fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise', text="DMST 21",
        command=lambda: dmst21(self))
    self.fbutt21dmst_window = self.can.create_window(self.x217,
        self.y217, window=self.butt21dmst)

    # Patient 22
    try:
        with open('./newpatient/entryfile22.txt', 'r') as namefile:
            line22 = namefile.readline()
    except FileNotFoundError as callfile22:
        print("[!] File entryfile22.txt doesn't exist !", callfile22)

    try:
        self.new_data22 = line22
        self.x220, self.y220 = 144, 902
        self.new_data22 = tk.StringVar()
        self.entpat22f = tk.Entry(self.can, textvariable=self.new_data22,
            highlightbackground='grey', bd=4)
        if line22 == '----------------------':
            line22 = line22
        else:
            line22 = line22[:-1]
        self.new_data22.set(line22)
        self.fentpat22f_window = self.can.create_window(self.x220,
            self.y220, window=self.entpat22f)
    except UnboundLocalError as ub_error22:
        print("[!] File 22 not created !", ub_error22)

    self.x221, self.y221 = 286, 902
    self.buttpat22up = tk.Button(self.can, width=8, font=16,
        fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise', text="Update 22",
        command=lambda: updateLink(self, g=22))
    self.fbuttpat22up_window = self.can.create_window(self.x221,
        self.y221, window=self.buttpat22up)

    self.x222, self.y222 = 444, 902
    self.butt22diag = tk.Button(self.can, width=18, font=16,
        fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise', text="Diagnostic + ATCD 22",
        command=lambda: diagstic(self, d=22))
    self.fbutt22diag_window = self.can.create_window(self.x222,
        self.y222, window=self.butt22diag)

    self.x223, self.y223 = 612, 902
    self.butt22med = tk.Button(self.can, width=10, font=16,
        fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise', text="Treatments 22",
        command=lambda: tttMed22(self))
    self.fbutt22med_window = self.can.create_window(self.x223,
        self.y223, window=self.butt22med)

    self.x224, self.y224 = 740, 902
    self.butt22labo = tk.Button(self.can, width=10, font=16,
        fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise', text="Laboratory 22",
        command=lambda: laboResult22(self))
    self.fbutt22labo_window = self.can.create_window(self.x224,
        self.y224, window=self.butt22labo)

    self.x225, self.y225 = 868, 902
    self.butt22vm = tk.Button(self.can, width=10, font=16,
        fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise', text="Medical Visit22",
        command=self.visitMed22)
    self.fbutt22vm_window = self.can.create_window(self.x225,
        self.y225, window=self.butt22vm)

    self.x226, self.y226 = 996, 902
    self.butt22aux = tk.Button(self.can, width=10, font=16,
        fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise', text="Aux. Equip.22",
        command=lambda: aux22(self))
    self.fbutt22aux_window = self.can.create_window(self.x226,
        self.y226, window=self.butt22aux)

    self.x227, self.y227 = 1124, 902
    self.butt22dmst = tk.Button(self.can, width=10, font=16,
        fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise', text="DMST 22",
        command=lambda: dmst22(self))
    self.fbutt22dmst_window = self.can.create_window(self.x227,
        self.y227, window=self.butt22dmst)

    # Patient 23
    try:
        with open('./newpatient/entryfile23.txt', 'r') as namefile:
            line23 = namefile.readline()
    except FileNotFoundError as callfile23:
        print("[!] File entryfile23.txt doesn't exist !", callfile23)

    try:
        self.new_data23 = line23
        self.x230, self.y230 = 144, 934
        self.new_data23 = tk.StringVar()
        self.entrypat23f = tk.Entry(self.can, textvariable=self.new_data23,
            highlightbackground='grey', bd=4)
        if line23 == '-----------------------':
            line23 = line23
        else:
            line23 = line23[:-1]
        self.new_data23.set(line23)
        self.fentrypat23f_window = self.can.create_window(self.x230,
            self.y230, window=self.entrypat23f)
    except UnboundLocalError as ub_error23:
        print("[!] File 23 not created !", ub_error23)

    self.x231, self.y231 = 286, 934
    self.buttpat23up = tk.Button(self.can, width=8, font=16,
        fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise', text="Update 23",
        command=lambda: updateLink(self, g=23))
    self.fbuttpat23up_window = self.can.create_window(self.x231,
        self.y231, window=self.buttpat23up)

    self.x232, self.y232 = 444, 934
    self.butt23diag = tk.Button(self.can, width=18, font=16,
        fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise', text="Diagnostic + ATCD 23",
        command=lambda: diagstic(self, d=23))
    self.fbutt23diag_window = self.can.create_window(self.x232,
        self.y232, window=self.butt23diag)

    self.x233, self.y233 = 612, 934
    self.butt23med = tk.Button(self.can, width=10, font=16,
        fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise', text="Treatments 23",
        command=lambda: tttMed23(self))
    self.fbutt23med_window = self.can.create_window(self.x233,
        self.y233, window=self.butt23med)

    self.x234, self.y234 = 740, 934
    self.butt23labo = tk.Button(self.can, width=10, font=16,
        fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise', text="Laboratory 23",
        command=lambda: laboResult23(self))
    self.fbutt23labo_window = self.can.create_window(self.x234,
        self.y234, window=self.butt23labo)

    self.x235, self.y235 = 868, 934
    self.butt23vm = tk.Button(self.can, width=10, font=16,
        fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise', text="Medical Visit23",
        command=self.visitMed23)
    self.fbutt23vm_window = self.can.create_window(self.x235,
        self.y235, window=self.butt23vm)

    self.x236, self.y236 = 996, 934
    self.butt23aux = tk.Button(self.can, width=10, font=16,
        fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise', text="Aux. Equip.23",
        command=lambda: aux23(self))
    self.fbutt23aux_window = self.can.create_window(self.x236,
        self.y236, window=self.butt23aux)

    self.x237, self.y237 = 1124, 934
    self.butt23dmst = tk.Button(self.can, width=10, font=16,
        fg='navy', bg='SteelBlue2',
        activebackground='pale turquoise', text="DMST 23",
        command=lambda: dmst23(self))
    self.fbutt23dmst_window = self.can.create_window(self.x237,
        self.y237, window=self.butt23dmst)

    # Patient 24
    try:
        with open('./newpatient/entryfile24.txt', 'r') as namefile:
            line24 = namefile.readline()
    except FileNotFoundError as callfile24:
        print("[!] File entryfile24.txt doesn't exist !", callfile24)

    try:
        self.new_data24 = line24
        self.x240, self.y240 = 144, 966
        self.new_data24 = tk.StringVar()
        self.entrypat24f = tk.Entry(self.can, textvariable=self.new_data24,
          highlightbackground='grey', bd=4)
        if line24 == '------------------------':
            line24 = line24
        else:
            line24 = line24[:-1]
        self.new_data24.set(line24)
        self.fentrypat24f_window = self.can.create_window(self.x240,
            self.y240, window=self.entrypat24f)
    except UnboundLocalError as ub_error24:
        print("[!] File 24 not created !", ub_error24)

    self.x241, self.y241 = 286, 966
    self.buttpat24up = tk.Button(self.can, width=8, font=16,
        fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise', text="Update 24",
        command=lambda: updateLink(self, g=24))
    self.fbuttpat24up_window = self.can.create_window(self.x241,
        self.y241, window=self.buttpat24up)

    self.x242, self.y242 = 444, 966
    self.butt24diag = tk.Button(self.can, width=18, font=16,
        fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise', text="Diagnostic + ATCD 24",
        command=lambda: diagstic(self, d=24))
    self.fbutt24diag_window = self.can.create_window(self.x242,
        self.y242, window=self.butt24diag)

    self.x243, self.y243 = 612, 966
    self.butt24med = tk.Button(self.can, width=10, font=16,
        fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise', text="Treatments 24",
        command=lambda: tttMed24(self))
    self.fbutt24med_window = self.can.create_window(self.x243,
        self.y243, window=self.butt24med)

    self.x244, self.y244 = 740, 966
    self.butt24labo = tk.Button(self.can, width=10, font=16,
        fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise', text="Laboratory 24",
        command=lambda: laboResult24(self))
    self.fbutt24labo_window = self.can.create_window(self.x244,
        self.y244, window=self.butt24labo)

    self.x245, self.y245 = 868, 966
    self.butt24vm = tk.Button(self.can, width=10, font=16,
        fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise', text="Medical Visit24",
        command=self.visitMed24)
    self.fbutt24vm_window = self.can.create_window(self.x245,
        self.y245, window=self.butt24vm)

    self.x246, self.y246 = 996, 966
    self.butt24aux = tk.Button(self.can, width=10, font=16,
        fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise', text="Aux. Equip.24",
        command=lambda: aux24(self))
    self.fbutt24aux_window = self.can.create_window(self.x246,
        self.y246, window=self.butt24aux)

    self.x247, self.y247 = 1124, 966
    self.butt24dmst = tk.Button(self.can, width=10, font=16,
        fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise', text="DMST 24",
        command=lambda: dmst24(self))
    self.fbutt24dmst_window = self.can.create_window(self.x247,
        self.y247, window=self.butt24dmst)

    self.x248, self.y248 = 144, 1000
    self.lbl_ghost = tk.Label(self.can,
        width=20, height=1, bg='DodgerBlue2')
    self.wlbl_ghost = self.can.create_window(self.x248, self.y248,
        window = self.lbl_ghost)

    self.can.configure(scrollregion=self.can.bbox(tk.ALL))
    self.can.bind_all("<Button-4>", self.onMouseWheel)
    self.can.bind_all("<Button-5>", self.onMouseWheel)
