#!/usr/bin/python3
# -*- coding: utf-8 -*-


import tkinter as tk
from tkinter import messagebox
import time
import os
import platform
from dmst_doc.extdmst15.extdmstfile15 import importationAdmin
from dmst_doc.extdmst15.extdmstfile15 import importationDoc1
from dmst_doc.extdmst15.extdmstfile15 import importationDoc2
from dmst_doc.extdmst15.extdmstfile15 import importationDoc3
from dmst_doc.extdmst15.extdmstfile15 import importationFam
from dmst_doc.extdmst15.extdmstfile15 import importationHealOne
from dmst_doc.extdmst15.extdmstfile15 import importationHealThree
from dmst_doc.extdmst15.extdmstfile15 import importationFile2
from dmst_doc.extdmst15.extdmstfile15 import importationParam
from dmst_doc.extdmst15.extdmstfile15 import importationBmi
from dmst_doc.extdmst15.extdmstfile15 import launchfunc
from dmst_doc.extdmst15.extdmstfile15 import saveData
from dmst_doc.extdmst15.extdmstfile15 import copytobackup
from dmst_doc.extdmst15.extdmstfile15 import uptoserv


def doc_medical15(self):
    """
        Main function called since main app
        heal_track.py for displaying all data
        DMST (Document Medical Soins Transmissions).
    """
    self.effacer()
    self.delScroll()
    self.can.unbind_all("<Button-4>")
    self.can.unbind_all("<Button-5>")
    self.can.config(background='DodgerBlue2')

    def deactscroll(event):
        """
            Deactivate scrollbar and MouseWheel.
            It's activated by clicking on textbox
        """
        self.delScroll()
        self.can.unbind_all("<Button-4>")
        self.can.unbind_all("<Button-5>")
        self.t104.config(state='normal')
        print("MouseWheel deactivated for textbox !")

    self.x1, self.y1 = 500, 45
    self.labl_name = tk.Label(self.can, text="DMST",
        font=('helvetica', 18, 'bold'), width=8,
        height=2, bg='DodgerBlue2', fg='white')
    self.wlabl_name = self.can.create_window(self.x1, self.y1,
        window = self.labl_name)

    with open('./newpatient/entryfile15.txt', 'r') as filename2:
        a_linedmst = filename2.readline()
        b_linedmst = filename2.readline()
        c_linedmst = filename2.readline()
        d_linedmst = filename2.readline()

    self.x2, self.y2 = 640, 45
    self.ntry_txt = tk.StringVar()
    self.entryname = tk.Entry(self.can, textvariable=self.ntry_txt)
    self.ntry_txt.set(a_linedmst[:-1])
    self.wentryname = self.can.create_window(self.x2, self.y2,
        window = self.entryname)

    self.x3, self.y3 = 250, 100
    self.labl_title = tk.Label(self.can, text='--- Personal Data ---',
        font=('Times', 14, 'bold'), width=60,
        height=1, bg='RoyalBlue3', fg='white')
    self.wlabl_title = self.can.create_window(self.x3, self.y3,
        window = self.labl_title)

    self.x5, self.y5 = 90, 140
    self.LabDate = tk.Label(self.can, text="Date : ", width=15, font=12,
        fg='white', bg='DodgerBlue2', anchor=tk.E)
    self.wLabDate_window = self.can.create_window(self.x5, self.y5,
        window=self.LabDate)

    self.x17, self.y17 = 90, 170
    self.LabHour = tk.Label(self.can, text="Hour : ", width=15, font=12,
        fg='white', bg='DodgerBlue2', anchor=tk.E)
    self.wLabHour_window = self.can.create_window(self.x17, self.y17,
        window=self.LabHour)

    self.x18, self.y18 = 90, 200
    self.LabName = tk.Label(self.can, text="Patient name : ", width=15, font=12,
        fg='white', bg='DodgerBlue2', anchor=tk.E)
    self.wLabName_window = self.can.create_window(self.x18, self.y18,
        window=self.LabName)

    self.x19, self.y19 = 90, 230
    self.birth_lab = tk.Label(self.can, text="Birthday : ", width=15, font=12,
        fg='white', bg='DodgerBlue2', anchor=tk.E)
    self.wbirth_lab_window = self.can.create_window(self.x19, self.y19,
        window=self.birth_lab)

    self.x20, self.y20 = 90, 260
    self.allerlab = tk.Label(self.can, text="Allergy : ", width=15, font=12,
        fg='white', bg='DodgerBlue2', anchor=tk.E)
    self.wallerlab_window = self.can.create_window(self.x20, self.y20,
        window=self.allerlab)

    self.x21, self.y21 = 65, 290
    self.tran_dis = tk.Label(self.can, text="Transmi. disease : ",
        width=20, font=12,
        fg='white', bg='DodgerBlue2', anchor=tk.E)
    self.wtran_dis_window = self.can.create_window(self.x21, self.y21,
        window=self.tran_dis)

    self.x22, self.y22 = 30, 320 # +30
    self.diaglab = tk.Label(self.can, text="Diagnostics : ",
        width=15, font=12,
        fg='white', bg='DodgerBlue2', anchor=tk.E)
    self.wdiaglab_window = self.can.create_window(self.x22, self.y22,
        window=self.diaglab)

    self.x23, self.y23 = 260, 140
    self.time_string = tk.IntVar()
    self.textDate = tk.Entry(self.can, textvariable=self.time_string,
        highlightbackground='grey', bd=2)
    self.time_string.set(time.strftime("%d:%m:%Y"))
    self.wtextDate_window = self.can.create_window(self.x23, self.y23,
        window=self.textDate)

    self.x24, self.y24 = 260, 170
    self.time_Htring = tk.IntVar()
    self.textHour = tk.Entry(self.can, textvariable=self.time_Htring,
        highlightbackground='grey', bd=2)
    self.time_Htring.set(time.strftime("%H:%M:%S"))
    self.wtextHour_window = self.can.create_window(self.x24, self.y24,
        window=self.textHour)

    self.x25, self.y25 = 260, 200
    self.ent_name = tk.StringVar()
    self.txt_name = tk.Entry(self.can, textvariable=self.ent_name,
        highlightbackground='grey', bd=2)
    self.ent_name.set(a_linedmst[:-1])
    self.wtxt_name_window = self.can.create_window(self.x25, self.y25,
        window=self.txt_name)

    self.x26, self.y26 = 260, 230
    self.nt_birth = tk.StringVar()
    self.s_birth = tk.Entry(self.can, textvariable=self.nt_birth,
        highlightbackground='grey', bd=2)
    self.nt_birth.set(b_linedmst[:-1])
    self.ws_birth_window = self.can.create_window(self.x26, self.y26,
        window=self.s_birth)

    self.x27, self.y27 = 260, 260
    self.allertxt = tk.StringVar()
    self.allername = tk.Entry(self.can, textvariable=self.allertxt,
        highlightbackground='grey', bd=2)
    self.allertxt.set(c_linedmst[:-1])
    self.wallername_window = self.can.create_window(self.x27, self.y27,
        window=self.allername)

    self.x28, self.y28 = 260, 290
    self.transdis = tk.StringVar()
    self.transmission = tk.Entry(self.can, textvariable=self.transdis,
        highlightbackground='grey', bd=2)
    self.transdis.set(d_linedmst[:-1])
    self.wtransmission_window = self.can.create_window(self.x28, self.y28,
        window=self.transmission)

    #Textbox for diag 1
    self.x29, self.y29 = 250, 440
    self.t29 = tk.Text(self.can, height=10, width=50, font=18, relief=tk.SUNKEN)
    self.t29.bind("<Button-1>", deactscroll)
    self.wt29_window = self.can.create_window(self.x29, self.y29, window=self.t29)

    # Display text in textbox from diag file
    try:
        with open('./diag/doc_diag15/diagrecap15.txt', 'r') as filediag:
            linesdiag = filediag.readlines()
            for i in range(0, len(linesdiag)):
                for line in linesdiag:
                    line.replace('{', '')
                    line.replace('}', '')
                    line = linesdiag[i]
                    self.t29.config(state='normal')
                    self.t29.insert(tk.INSERT, linesdiag[i])
                    self.t29.insert(tk.INSERT, linesdiag[i+1])
                    self.t29.insert(tk.INSERT, linesdiag[i+2])
                    self.t29.insert(tk.INSERT, linesdiag[i+3])
                    self.t29.insert(tk.INSERT, linesdiag[i+4])
                    self.t29.insert(tk.INSERT, linesdiag[i+5])
                    self.t29.insert(tk.INSERT, linesdiag[i+6])
                    self.t29.config(state='disable')
                    break
                self.t29.config(state='normal')
                self.t29.insert(tk.INSERT,
                    "All diagnostics done...")
                self.t29.config(state='disable')
                break
    except FileNotFoundError as infofileout:
        print("[!] File 1 has not been found", infofileout)
    except IndexError as inforange:
        self.t29.config(state='normal')
        self.t29.insert(tk.INSERT, "All diagnostics done...")
        self.t29.config(state='disable')
        print("[!] List 1 got less than 6 lines", inforange)
    else:
        ("[!] Error unknow 1 (for diag)")

    # Labl + Textbox + func to read in ttt files
    self.x30, self.y30 = 80, 560
    self.tttlab = tk.Label(self.can, text="Treatments + Reserves : ",
        width=25, font=12,
        fg='white', bg='DodgerBlue2', anchor=tk.E)
    self.wtttlab_window = self.can.create_window(self.x30, self.y30,
        window=self.tttlab)

    def importationFile(self, fichier, encodage="Utf-8"):
        file31 = open(fichier, 'r', encoding=encodage)
        content31 = file31.readlines()
        file31.close()
        for li in content31:
            self.t31.config(state='normal')
            self.t31.insert(tk.END, li)
            self.t31.config(state='disable')

    self.x31, self.y31 = 250, 680
    self.t31 = tk.Text(self.can, height=10, width=50, font=18,
        relief=tk.SUNKEN)
    self.wt31_window = self.can.create_window(self.x31, self.y31,
        window=self.t31)
    self.t31.bind("<Button-1>", deactscroll)

    try:
        if os.path.getsize('./ttt/doc_ttt15/intro_ttt.txt'):
            importationFile(self, './ttt/doc_ttt15/intro_ttt.txt',
                encodage="Utf-8")
    except FileNotFoundError as no_file:
        print("[!] File intro_ttt not found !")
        tk.messagebox.showinfo('INFO', 'File intro_ttt not found !')

    try:
        if os.path.getsize('./ttt/doc_ttt15/intro_res.txt'):
            importationFile2(self, './ttt/doc_ttt15/intro_res.txt',
                encodage="Utf-8")
    except FileNotFoundError as no_file:
        print("[!] File intro_res not found !")
        tk.messagebox.showinfo('INFO', 'File intro_res not found !')

    # Lbl for VP
    self.x32, self.y32 = 60, 800
    self.paramlab = tk.Label(self.can, text="Vitals Parameters : ",
        width=20, font=12,
        fg='white', bg='DodgerBlue2', anchor=tk.E)
    self.wparamlab_window = self.can.create_window(self.x32, self.y32,
        window=self.paramlab)

    #Textbox for param
    self.x33, self.y33 = 250, 920
    self.t33 = tk.Text(self.can, height=10, width=50, font=18,
        relief=tk.SUNKEN)
    self.t33.bind("<Button-1>", deactscroll)
    self.wt33_window = self.can.create_window(self.x33, self.y33,
        window=self.t33)

    try:
        if os.path.getsize('./param/paramdata15.txt'):
            importationParam(self, './param/paramdata15.txt', encodage="Utf-8")
    except FileNotFoundError as no_file:
        print("[!] File paramdata15.txt not found !")
        tk.messagebox.showinfo('INFO', 'File paramdata15.txt not found !')

    # Lbl for BMI
    self.x34, self.y34 = 40, 1040
    self.paramlab = tk.Label(self.can, text="Weight and BMI : ",
        width=20, font=12, fg='white', bg='DodgerBlue2', anchor=tk.E)
    self.wparamlab_window = self.can.create_window(self.x34, self.y34,
        window=self.paramlab)

    #Textbox for bmi
    self.x35, self.y35 = 250, 1160
    self.t35 = tk.Text(self.can, height=10, width=50, font=18,
        relief=tk.SUNKEN)
    self.t35.bind("<Button-1>", deactscroll)
    self.wt35_window = self.can.create_window(self.x35, self.y35,
        window=self.t35)

    try:
        if os.path.getsize('./calBmi/bmi15.txt'):
            importationBmi(self, './calBmi/bmi15.txt', encodage="Utf-8")
    except FileNotFoundError as no_file:
        print("[!] File bmi15.txt not found !")
        tk.messagebox.showinfo('INFO', 'File bmi15.txt not found !')

    self.x36, self.y36 = 250, 1290 
    self.lbl_need = tk.Label(self.can,
        text='--- AGGIR (grid) and depedencies ---',
        font=('Times', 14, 'bold'), width=60,
        height=1, bg='RoyalBlue3', fg='white')
    self.wlbl_need = self.can.create_window(self.x36, self.y36,
        window = self.lbl_need)

    self.x4, self.y4 = 870, 100
    self.labl_title2 = tk.Label(self.can, text='--- Admin Data ---',
        font=('Times', 14, 'bold'), width=60,
        height=1, bg='RoyalBlue3', fg='white')
    self.wlabl_title2 = self.can.create_window(self.x4, self.y4,
        window = self.labl_title2)

    # Admin from contact col 2
    self.x6, self.y6 = 870, 240
    self.t6 = tk.Text(self.can, height=11, width=50, font=18, relief=tk.SUNKEN)
    self.t6.bind("<Button-1>", deactscroll)
    self.wt6_window = self.can.create_window(self.x6, self.y6, window=self.t6)

    try:
        if os.path.exists('./contact/conpact15/finalfile15.txt'):
            importationAdmin(self, './contact/conpact15/finalfile15.txt', encodage="Utf-8")
    except FileNotFoundError as no_file:
        print("[!] File finalfile15.txt not found !")
        tk.messagebox.showinfo('INFO', 'File Admin not found !')

    self.x7, self.y7 = 870, 380
    self.lbl_doc = tk.Label(self.can, text='--- Doctor Data ---',
        font=('Times', 14, 'bold'), width=60,
        height=1, bg='RoyalBlue3', fg='white')
    self.wlbl_doc = self.can.create_window(self.x7, self.y7,
        window = self.lbl_doc)

    # Doctor from contact col 2
    self.x8, self.y8 = 870, 490
    self.t8 = tk.Text(self.can, height=8, width=50, font=18, relief=tk.SUNKEN)
    self.t8.bind("<Button-1>", deactscroll)
    self.wt8_window = self.can.create_window(self.x8, self.y8, window=self.t8)

    try:
        if os.path.getsize('./contact/conpact15/finaldoc1.txt'):
            importationDoc1(self, './contact/conpact15/finaldoc1.txt', encodage="Utf-8")
    except FileNotFoundError as no_file:
        print("[!] File finaldoc1 not found !")
        tk.messagebox.showinfo('INFO', 'File Doctor not found !')

    # Doctor2 from contact col 2
    self.x9, self.y9 = 870, 670
    self.t9 = tk.Text(self.can, height=8, width=50, font=18, relief=tk.SUNKEN)
    self.t9.bind("<Button-1>", deactscroll)
    self.wt9_window = self.can.create_window(self.x9, self.y9, window=self.t9)

    try:
        if os.path.getsize('./contact/conpact15/finaldoc2.txt'):
            importationDoc2(self, './contact/conpact15/finaldoc2.txt', encodage="Utf-8")
    except FileNotFoundError as no_file:
        print("[!] File finaldoc2 not found !")
        tk.messagebox.showinfo('INFO', 'File Doctor2 not found !')

    # Doctor3 from contact col 2
    self.x10, self.y10 = 870, 850
    self.t10 = tk.Text(self.can, height=8, width=50, font=18, relief=tk.SUNKEN)
    self.t10.bind("<Button-1>", deactscroll)
    self.wt10_window = self.can.create_window(self.x10, self.y10, window=self.t10)

    try:
        if os.path.getsize('./contact/conpact15/finaldoc3.txt'):
            importationDoc3(self, './contact/conpact15/finaldoc3.txt', encodage="Utf-8")
    except FileNotFoundError as no_file:
        print("[!] File finaldoc3.txt not found !")
        tk.messagebox.showinfo('INFO', 'File Doctor3 not found !')

    self.x11, self.y11 = 870, 960
    self.lbl_fam = tk.Label(self.can, text='--- Family Data ---',
        font=('Times', 14, 'bold'), width=60,
        height=1, bg='RoyalBlue3', fg='white')
    self.wlbl_fam = self.can.create_window(self.x11, self.y11,
        window = self.lbl_fam)

    self.x12, self.y12 = 870, 1050
    self.t12 = tk.Text(self.can, height=6, width=50, font=18, relief=tk.SUNKEN)
    self.t12.bind("<Button-1>", deactscroll)
    self.wt12_window = self.can.create_window(self.x12, self.y12, window=self.t12)

    try:
        if os.path.getsize('./contact/conpact15/finalfam15.txt'):
            importationFam(self, './contact/conpact15/finalfam15.txt', encodage="Utf-8")
    except FileNotFoundError as no_file:
        print("[!] File finalfam15.txt not found !")
        tk.messagebox.showinfo('INFO', 'File finalfam15.txt not found !')

    self.x13, self.y13 = 870, 1140
    self.lbl_heal = tk.Label(self.can, text='--- Home Care System Data ---',
        font=('Times', 14, 'bold'), width=60,
        height=1, bg='RoyalBlue3', fg='white')
    self.wlbl_heal = self.can.create_window(self.x13, self.y13,
        window = self.lbl_heal)

    self.x14, self.y14 = 870, 1230
    self.t14 = tk.Text(self.can, height=6, width=50, font=18, relief=tk.SUNKEN)
    self.t14.bind("<Button-1>", deactscroll)
    self.wt14_window = self.can.create_window(self.x14, self.y14, window=self.t14)

    try:
        if os.path.getsize('./contact/conpact15/finalhcs1.txt'):
            importationHealOne(self, './contact/conpact15/finalhcs1.txt', encodage="Utf-8")
    except FileNotFoundError as no_file:
        print("[!] File finalhcs1.txt not found !")
        tk.messagebox.showinfo('INFO', 'File finalhcs1.txt not found !')

    def importationHealTwo(fichier, encodage="Utf-8"):
        filehcs2 = open(fichier, 'r', encoding=encodage)
        content = filehcs2.readlines()
        filehcs2.close()
        for li in content:
            self.t15.config(state='normal')
            self.t15.insert(tk.END, li)
            self.t15.config(state='disable')

    self.x15, self.y15 = 870, 1370
    self.t15 = tk.Text(self.can, height=6, width=50, font=18, relief=tk.SUNKEN)
    self.t15.bind("<Button-1>", deactscroll)
    self.wt15_window = self.can.create_window(self.x15, self.y15, window=self.t15)

    try:
        if os.path.getsize('./contact/conpact15/finalhcs2.txt'):
            importationHealTwo('./contact/conpact15/finalhcs2.txt', encodage="Utf-8")
    except FileNotFoundError as no_file:
        print("[!] File finalhcs2.txt not found !")
        tk.messagebox.showinfo('INFO', 'File finalhcs2.txt not found !')

    self.x16, self.y16 = 870, 1510
    self.t16 = tk.Text(self.can, height=6, width=50, font=18, relief=tk.SUNKEN)
    self.t16.bind("<Button-1>", deactscroll)
    self.wt16_window = self.can.create_window(self.x16, self.y16, window=self.t16)

    try:
        if os.path.getsize('./contact/conpact15/finalhcs3.txt'):
            importationHealThree(self, './contact/conpact15/finalhcs3.txt',
                encodage="Utf-8")
    except FileNotFoundError as no_file:
        print("[!] File finalhcs3.txt not found !")
        tk.messagebox.showinfo('INFO', 'File finalhcs3.txt not found !')

    self.x37, self.y37 = 250, 1320
    self.lbl_exneeds = tk.Label(self.can,
        text="0 = None / 1 = supervision only /"\
        " 2 = passive help / 3 = active help / 4 = show and tell",
        font="Times 11", width=80,
        height=1, bg='DodgerBlue2', fg='white')
    self.wlbl_exneeds = self.can.create_window(self.x37, self.y37,
        window = self.lbl_exneeds)

    self.x38, self.y38 = 80, 1360
    self.lbl_eat = tk.Label(self.can, text='- Orientation :',
        font=('Times', 14, 'bold'), width=20, height=1,
        bg='DodgerBlue2', fg='white', anchor=tk.W)
    self.wlbl_eat = self.can.create_window(self.x38, self.y38,
        window = self.lbl_eat)

    self.CheckVar1 = tk.IntVar()
    self.x39, self.y39 = 240, 1360
    self.C0 = tk.Radiobutton(self.can, text="0",
        highlightbackground='cyan', fg='black',
        bg='DodgerBlue2', variable=self.CheckVar1,
        value=0, height=1, width=3, anchor=tk.W)
    self.wC0 = self.can.create_window(self.x39, self.y39,
        window = self.C0)

    self.x40, self.y40 = 295, 1360
    self.C1 = tk.Radiobutton(self.can, text="1",
        highlightbackground='cyan', fg='black',
        bg='DodgerBlue2', variable=self.CheckVar1,
        value=1, height=1, width=3, anchor=tk.W)
    self.wC1 = self.can.create_window(self.x40, self.y40,
        window = self.C1)

    self.x41, self.y41 = 350, 1360
    self.C2 = tk.Radiobutton(self.can, text="2",
        highlightbackground='cyan', fg='black',
        bg='DodgerBlue2', variable=self.CheckVar1,
        value=2, height=1, width=3, anchor=tk.W)
    self.wC2 = self.can.create_window(self.x41, self.y41,
        window = self.C2)

    self.x42, self.y42 = 405, 1360
    self.C3 = tk.Radiobutton(self.can, text="3",
        highlightbackground='cyan', fg='black',
        bg='DodgerBlue2', variable=self.CheckVar1, 
        value=3, height=1, width=3, anchor=tk.W)
    self.wC3 = self.can.create_window(self.x42, self.y42,
        window = self.C3)

    self.x43, self.y43 = 460, 1360
    self.C4 = tk.Radiobutton(self.can, text="4",
        highlightbackground='cyan', fg='black',
        bg='DodgerBlue2', variable=self.CheckVar1, 
        value=4, height=1, width=3, anchor=tk.W)
    self.wC4 = self.can.create_window(self.x43, self.y43,
        window = self.C4)

    # second need
    self.x44, self.y44 = 80, 1385
    self.lbl_sec = tk.Label(self.can, text='- Coherence :',
        font=('Times', 14, 'bold'), width=20, height=1,
        bg='DodgerBlue2', fg='white', anchor=tk.W)
    self.wlbl_sec = self.can.create_window(self.x44, self.y44,
        window = self.lbl_sec)

    self.CheckVar2 = tk.IntVar()
    self.x45, self.y45 = 240, 1385
    self.C10 = tk.Radiobutton(self.can, text="0",
        highlightbackground='cyan', fg='black',
        bg='DodgerBlue2', variable=self.CheckVar2,
        value=0, height=1, width=3, anchor=tk.W)
    self.wC10 = self.can.create_window(self.x45, self.y45,
        window = self.C10)

    self.x46, self.y46 = 295, 1385
    self.C11 = tk.Radiobutton(self.can, text="1",
        highlightbackground='cyan', fg='black',
        bg='DodgerBlue2', variable=self.CheckVar2,
        value=1, height=1, width=3, anchor=tk.W)
    self.wC11 = self.can.create_window(self.x46, self.y46,
        window = self.C11)

    self.x47, self.y47 = 350, 1385
    self.C12 = tk.Radiobutton(self.can, text="2",
        highlightbackground='cyan', fg='black',
        bg='DodgerBlue2', variable=self.CheckVar2,
        value=2, height=1, width=3, anchor=tk.W)
    self.wC12 = self.can.create_window(self.x47, self.y47,
        window = self.C12)

    self.x48, self.y48 = 405, 1385
    self.C13 = tk.Radiobutton(self.can, text="3",
        highlightbackground='cyan', fg='black', 
        bg='DodgerBlue2', variable=self.CheckVar2, 
        value=3, height=1, width=3, anchor=tk.W)
    self.wC13 = self.can.create_window(self.x48, self.y48,
        window = self.C13)

    self.x49, self.y49 = 460, 1385
    self.C14 = tk.Radiobutton(self.can, text="4",
        highlightbackground='cyan', fg='black', 
        bg='DodgerBlue2', variable=self.CheckVar2, 
        value=4, height=1, width=3, anchor=tk.W)
    self.wC14 = self.can.create_window(self.x49, self.y49,
        window = self.C14)

    # third need
    self.x50, self.y50 = 80, 1410
    self.lbl_third = tk.Label(self.can, text='- Toilet :',
        font=('Times', 14, 'bold'), width=20, height=1,
        bg='DodgerBlue2', fg='white', anchor=tk.W)
    self.wlbl_third = self.can.create_window(self.x50, self.y50,
        window = self.lbl_third)

    self.CheckVar3 = tk.IntVar()
    self.x51, self.y51 = 240, 1410
    self.C20 = tk.Radiobutton(self.can, text="0",
        highlightbackground='cyan', fg='black',
        bg='DodgerBlue2', variable=self.CheckVar3,
        value=0, height=1, width=3, anchor=tk.W)
    self.wC20 = self.can.create_window(self.x51, self.y51,
        window = self.C20)

    self.x52, self.y52 = 295, 1410
    self.C21 = tk.Radiobutton(self.can, text="1",
        highlightbackground='cyan', fg='black',
        bg='DodgerBlue2', variable=self.CheckVar3,
        value=1, height=1, width=3, anchor=tk.W)
    self.wC21 = self.can.create_window(self.x52, self.y52,
        window = self.C21)

    self.x53, self.y53 = 350, 1410
    self.C22 = tk.Radiobutton(self.can, text="2",
        highlightbackground='cyan', fg='black',
        bg='DodgerBlue2', variable=self.CheckVar3,
        value=2, height=1, width=3, anchor=tk.W)
    self.wC22 = self.can.create_window(self.x53, self.y53,
        window = self.C22)

    self.x54, self.y54 = 405, 1410
    self.C23 = tk.Radiobutton(self.can, text="3",
        highlightbackground='cyan', fg='black',
        bg='DodgerBlue2', variable=self.CheckVar3, 
        value=3, height=1, width=3, anchor=tk.W)
    self.wC23 = self.can.create_window(self.x54, self.y54,
        window = self.C23)

    self.x55, self.y55 = 460, 1410
    self.C24 = tk.Radiobutton(self.can, text="4",
        highlightbackground='cyan', fg='black',
        bg='DodgerBlue2', variable=self.CheckVar3, 
        value=4, height=1, width=3, anchor=tk.W)
    self.wC24 = self.can.create_window(self.x55, self.y55,
        window = self.C24)

    # Forth need
    self.x56, self.y56 = 80, 1435
    self.lbl_forth = tk.Label(self.can, text='- Dressing :',
        font=('Times', 14, 'bold'), width=20, height=1,
        bg='DodgerBlue2', fg='white', anchor=tk.W)
    self.wlbl_forth = self.can.create_window(self.x56, self.y56,
        window = self.lbl_forth)

    self.CheckVar4 = tk.IntVar()
    self.x57, self.y57 = 240, 1435
    self.C30 = tk.Radiobutton(self.can, text="0",
        highlightbackground='cyan', fg='black',
        bg='DodgerBlue2', variable=self.CheckVar4,
        value=0, height=1, width=3, anchor=tk.W)
    self.wC30 = self.can.create_window(self.x57, self.y57,
        window = self.C30)

    self.x58, self.y58 = 295, 1435
    self.C31 = tk.Radiobutton(self.can, text="1",
        highlightbackground='cyan', fg='black',
        bg='DodgerBlue2', variable=self.CheckVar4,
        value=1, height=1, width=3, anchor=tk.W)
    self.wC31 = self.can.create_window(self.x58, self.y58,
        window = self.C31)

    self.x59, self.y59 = 350, 1435
    self.C32 = tk.Radiobutton(self.can, text="2",
        highlightbackground='cyan', fg='black',
        bg='DodgerBlue2', variable=self.CheckVar4,
        value=2, height=1, width=3, anchor=tk.W)
    self.wC32 = self.can.create_window(self.x59, self.y59,
        window = self.C32)

    self.x60, self.y60 = 405, 1435
    self.C33 = tk.Radiobutton(self.can, text="3",
        highlightbackground='cyan', fg='black',
        bg='DodgerBlue2', variable=self.CheckVar4, 
        value=3, height=1, width=3, anchor=tk.W)
    self.wC33 = self.can.create_window(self.x60, self.y60,
        window = self.C33)

    self.x61, self.y61 = 460, 1435
    self.C34 = tk.Radiobutton(self.can, text="4",
        highlightbackground='cyan', fg='black',
        bg='DodgerBlue2', variable=self.CheckVar4, 
        value=4, height=1, width=3, anchor=tk.W)
    self.wC34 = self.can.create_window(self.x61, self.y61,
        window = self.C34)

    # fivth need
    self.x62, self.y62 = 80, 1460
    self.lbl_fivth = tk.Label(self.can, text='- Food :',
        font=('Times', 14, 'bold'), width=20, height=1,
        bg='DodgerBlue2', fg='white', anchor=tk.W)
    self.wlbl_fivth = self.can.create_window(self.x62, self.y62,
        window = self.lbl_fivth)

    self.CheckVar5 = tk.IntVar()
    self.x63, self.y63 = 240, 1460
    self.C40 = tk.Radiobutton(self.can, text="0",
        highlightbackground='cyan', fg='black',
        bg='DodgerBlue2', variable=self.CheckVar5,
        value=0, height=1, width=3, anchor=tk.W)
    self.wC40 = self.can.create_window(self.x63, self.y63,
        window = self.C40)

    self.x64, self.y64 = 295, 1460
    self.C41 = tk.Radiobutton(self.can, text="1",
        highlightbackground='cyan', fg='black',
        bg='DodgerBlue2', variable=self.CheckVar5,
        value=1, height=1, width=3, anchor=tk.W)
    self.wC41 = self.can.create_window(self.x64, self.y64,
        window = self.C41)

    self.x65, self.y65 = 350, 1460
    self.C42 = tk.Radiobutton(self.can, text="2",
        highlightbackground='cyan', fg='black',
        bg='DodgerBlue2', variable=self.CheckVar5,
        value=2, height=1, width=3, anchor=tk.W)
    self.wC42 = self.can.create_window(self.x65, self.y65,
        window = self.C42)

    self.x66, self.y66 = 405, 1460
    self.C43 = tk.Radiobutton(self.can, text="3",
        highlightbackground='cyan', fg='black',
        bg='DodgerBlue2', variable=self.CheckVar5, 
        value=3, height=1, width=3, anchor=tk.W)
    self.wC43 = self.can.create_window(self.x66, self.y66,
        window = self.C43)

    self.x67, self.y67 = 460, 1460
    self.C44 = tk.Radiobutton(self.can, text="4",
        highlightbackground='cyan', fg='black',
        bg='DodgerBlue2', variable=self.CheckVar5, 
        value=4, height=1, width=3, anchor=tk.W)
    self.wC44 = self.can.create_window(self.x67, self.y67,
        window = self.C44)

    # Sixth need
    self.x68, self.y68 = 80, 1485
    self.lbl_sixth = tk.Label(self.can, text='- Elimination :',
        font=('Times', 14, 'bold'), width=20, height=1,
        bg='DodgerBlue2', fg='white', anchor=tk.W)
    self.wlbl_sixth = self.can.create_window(self.x68, self.y68,
        window = self.lbl_sixth)

    self.CheckVar6 = tk.IntVar()
    self.x69, self.y69 = 240, 1485
    self.C50 = tk.Radiobutton(self.can, text="0",
        highlightbackground='cyan', fg='black',
        bg='DodgerBlue2', variable=self.CheckVar6,
        value=0, height=1, width=3, anchor=tk.W)
    self.wC50 = self.can.create_window(self.x69, self.y69,
        window = self.C50)

    self.x70, self.y70 = 295, 1485
    self.C51 = tk.Radiobutton(self.can, text="1",
        highlightbackground='cyan', fg='black',
        bg='DodgerBlue2', variable=self.CheckVar6,
        value=1, height=1, width=3, anchor=tk.W)
    self.wC51 = self.can.create_window(self.x70, self.y70,
        window = self.C51)

    self.x71, self.y71 = 350, 1485
    self.C52 = tk.Radiobutton(self.can, text="2",
        highlightbackground='cyan', fg='black',
        bg='DodgerBlue2', variable=self.CheckVar6,
        value=2, height=1, width=3, anchor=tk.W)
    self.wC52 = self.can.create_window(self.x71, self.y71,
        window = self.C52)

    self.x72, self.y72 = 405, 1485
    self.C53 = tk.Radiobutton(self.can, text="3",
        highlightbackground='cyan', fg='black',
        bg='DodgerBlue2', variable=self.CheckVar6, 
        value=3, height=1, width=3, anchor=tk.W)
    self.wC53 = self.can.create_window(self.x72, self.y72,
        window = self.C53)

    self.x73, self.y73 = 460, 1485
    self.C54 = tk.Radiobutton(self.can, text="4",
        highlightbackground='cyan', fg='black',
        bg='DodgerBlue2', variable=self.CheckVar6, 
        value=4, height=1, width=3, anchor=tk.W)
    self.wC54 = self.can.create_window(self.x73, self.y73,
        window = self.C54)

    # Seventh need
    self.x74, self.y74 = 80, 1510
    self.lbl_seven = tk.Label(self.can, text='- Move around :',
        font=('Times', 14, 'bold'), width=20, height=1,
        bg='DodgerBlue2', fg='white', anchor=tk.W)
    self.wlbl_seven = self.can.create_window(self.x74, self.y74,
        window = self.lbl_seven)

    self.CheckVar7 = tk.IntVar()
    self.x75, self.y75 = 240, 1510
    self.C60 = tk.Radiobutton(self.can, text="0",
        highlightbackground='cyan', fg='black',
        bg='DodgerBlue2', variable=self.CheckVar7,
        value=0, height=1, width=3, anchor=tk.W)
    self.wC60 = self.can.create_window(self.x75, self.y75,
        window = self.C60)

    self.x76, self.y76 = 295, 1510
    self.C61 = tk.Radiobutton(self.can, text="1",
        highlightbackground='cyan', fg='black',
        bg='DodgerBlue2', variable=self.CheckVar7,
        value=1, height=1, width=3, anchor=tk.W)
    self.wC61 = self.can.create_window(self.x76, self.y76,
        window = self.C61)

    self.x77, self.y77 = 350, 1510
    self.C62 = tk.Radiobutton(self.can, text="2",
        highlightbackground='cyan', fg='black',
        bg='DodgerBlue2', variable=self.CheckVar7,
        value=2, height=1, width=3, anchor=tk.W)
    self.wC62 = self.can.create_window(self.x77, self.y77,
        window = self.C62)

    self.x78, self.y78 = 405, 1510
    self.C63 = tk.Radiobutton(self.can, text="3",
        highlightbackground='cyan', fg='black', 
        bg='DodgerBlue2', variable=self.CheckVar7, 
        value=3, height=1, width=3, anchor=tk.W)
    self.wC63 = self.can.create_window(self.x78, self.y78,
        window = self.C63)

    self.x79, self.y79 = 460, 1510
    self.C64 = tk.Radiobutton(self.can, text="4",
        highlightbackground='cyan', fg='black', 
        bg='DodgerBlue2', variable=self.CheckVar7, 
        value=4, height=1, width=3, anchor=tk.W)
    self.wC64 = self.can.create_window(self.x79, self.y79,
        window = self.C64)

    # Heighth need
    self.x80, self.y80 = 80, 1535
    self.lbl_height = tk.Label(self.can, text='- Communication :',
        font=('Times', 14, 'bold'), width=20, height=1,
        bg='DodgerBlue2', fg='white', anchor=tk.W)
    self.wlbl_height = self.can.create_window(self.x80, self.y80,
        window = self.lbl_height)

    self.CheckVar8 = tk.IntVar()
    self.x81, self.y81 = 240, 1535
    self.C70 = tk.Radiobutton(self.can, text="0",
        highlightbackground='cyan', fg='black',
        bg='DodgerBlue2', variable=self.CheckVar8,
        value=0, height=1, width=3, anchor=tk.W)
    self.wC70 = self.can.create_window(self.x81, self.y81,
        window = self.C70)

    self.x82, self.y82 = 295, 1535
    self.C71 = tk.Radiobutton(self.can, text="1",
        highlightbackground='cyan', fg='black',
        bg='DodgerBlue2', variable=self.CheckVar8,
        value=1, height=1, width=3, anchor=tk.W)
    self.wC71 = self.can.create_window(self.x82, self.y82,
        window = self.C71)

    self.x83, self.y83 = 350, 1535
    self.C72 = tk.Radiobutton(self.can, text="2",
        highlightbackground='cyan', fg='black',
        bg='DodgerBlue2', variable=self.CheckVar8,
        value=2, height=1, width=3, anchor=tk.W)
    self.wC72 = self.can.create_window(self.x83, self.y83,
        window = self.C72)

    self.x84, self.y84 = 405, 1535
    self.C73 = tk.Radiobutton(self.can, text="3",
        highlightbackground='cyan', fg='black', 
        bg='DodgerBlue2', variable=self.CheckVar8, 
        value=3, height=1, width=3, anchor=tk.W)
    self.wC73 = self.can.create_window(self.x84, self.y84,
        window = self.C73)

    self.x85, self.y85 = 460, 1535
    self.C74 = tk.Radiobutton(self.can, text="4",
        highlightbackground='cyan', fg='black', 
        bg='DodgerBlue2', variable=self.CheckVar8, 
        value=4, height=1, width=3, anchor=tk.W)
    self.wC74 = self.can.create_window(self.x85, self.y85,
        window = self.C74)

    # Auxiliary
    self.x86, self.y86 = 250, 1580
    self.lbl_aux = tk.Label(self.can,
        text='--- Auxiliary Equipement ---',
        font=('Times', 14, 'bold'), width=60,
        height=1, bg='RoyalBlue3', fg='white')
    self.wlbl_aux = self.can.create_window(self.x86, self.y86,
        window = self.lbl_aux)

    def importationHealTwo(fichier, encodage="Utf-8"):
        filehcs2 = open(fichier, 'r', encoding=encodage)
        content = filehcs2.readlines()
        filehcs2.close()
        for li in content:
            self.t87.config(state='normal')
            self.t87.insert(tk.END, li)
            self.t87.config(state='disable')

    self.x87, self.y87 = 250, 1670
    self.t87 = tk.Text(self.can, height=6, width=50, font=18, relief=tk.SUNKEN)
    self.t87.bind("<Button-1>", deactscroll)
    self.wt87_window = self.can.create_window(self.x87, self.y87, window=self.t87)

    try:
        if os.path.getsize('./auxequip/doc_equip/auxiliary15.txt'):
            importationHealTwo('./auxequip/doc_equip/auxiliary15.txt', encodage="Utf-8")
    except FileNotFoundError as no_file:
        print("[!] File auxiliary15.txt not found !")
        tk.messagebox.showinfo('INFO', 'File auxiliary15.txt not found !')

    # PLAFA
    self.x88, self.y88 = 750, 1655
    self.lbl_plafa = tk.Label(self.can, text='PLAFA :',
        font=('Times', 14, 'bold'), width=20, height=1,
        bg='DodgerBlue2', fg='white', anchor=tk.W)
    self.wlbl_plafa = self.can.create_window(self.x88, self.y88,
        window = self.lbl_plafa)

    # Directives Anticip.
    self.x91, self.y91 = 750, 1700
    self.lbl_diranticip = tk.Label(self.can, text='Directives anticipées :',
        font=('Times', 14, 'bold'), width=20, height=1,
        bg='DodgerBlue2', fg='white', anchor=tk.W)
    self.wlbl_diranticip = self.can.create_window(self.x91, self.y91,
        window = self.lbl_diranticip)

    self.CheckVar9 = tk.IntVar()
    self.x89, self.y89 = 920, 1655
    self.C75 = tk.Checkbutton(self.can, text=" Oui", fg='black', 
        bg='cyan', variable=self.CheckVar9,
        onvalue=1, offvalue=0, height=1, 
        width=6, anchor=tk.W)
    self.wC75 = self.can.create_window(self.x89, self.y89,
        window = self.C75)

    self.CheckVar10 = tk.IntVar()
    self.x90, self.y90 = 994, 1655
    self.C76 = tk.Checkbutton(self.can, text=" Non", fg='black', 
        bg='cyan', variable=self.CheckVar10, 
        onvalue=1, offvalue=0, height=1, 
        width=6, anchor=tk.W)
    self.wC76 = self.can.create_window(self.x90, self.y90,
        window = self.C76)

    self.CheckVar11 = tk.IntVar()
    self.x92, self.y92 = 920, 1700
    self.C77 = tk.Checkbutton(self.can, text=" Oui", fg='black',
        bg='cyan', variable=self.CheckVar11, 
        onvalue=1, offvalue=0, height=1, 
        width=6, anchor=tk.W)
    self.wC77 = self.can.create_window(self.x92, self.y92,
        window = self.C77)

    self.CheckVar12 = tk.IntVar()
    self.x93, self.y93 = 994, 1700
    self.C78 = tk.Checkbutton(self.can, text=" Non", fg='black',
        bg='cyan', variable=self.CheckVar12, 
        onvalue=1, offvalue=0, height=1, 
        width=6, anchor=tk.W)
    self.wC78 = self.can.create_window(self.x93, self.y93,
        window = self.C78)

    # 14 needs
    self.x94, self.y94 = 550, 1765
    self.lbl_need = tk.Label(self.can, text='--- 14 Needs ---',
        font=('Times', 14, 'bold'), width=128,
        height=1, bg='RoyalBlue3', fg='white')
    self.wlbl_need = self.can.create_window(self.x94, self.y94,
        window = self.lbl_need)

    def needimport(fichier):
        secfile = open(fichier, 'r')
        seccontent = secfile.readlines()
        secfile.close()
        for li in seccontent:
            self.t95.config(state='normal')
            self.t95.insert(tk.END, li)
            self.t95.config(state='disable')

    self.x95, self.y95 = 550, 1995
    self.t95 = tk.Text(self.can, height=20, width=100, font=18,
        relief=tk.SUNKEN)
    self.t95.bind("<Button-1>", deactscroll)
    self.wt95_window = self.can.create_window(self.x95, self.y95,
        window=self.t95)

    try:
        if os.path.getsize('./need/doc_suivi15/main_14b.txt'):
            print("[+] File 'main_14b.txt' exist !")
            needimport('./need/doc_suivi15/main_14b.txt')
    except FileNotFoundError as need_f:
        print("[!] File 'main_14b.txt' does not exist !")
        print(need_f)

    # Line
    self.x96, self.y96 = 550, 2225
    self.lbl_need = tk.Label(self.can, font=('Times', 14, 'bold'),
        width=128, height=1, bg='RoyalBlue3', fg='white')
    self.wlbl_need = self.can.create_window(self.x96, self.y96,
        window = self.lbl_need)

    self.x97, self.y97 = 80, 2270
    self.lbl_evadate = tk.Label(self.can, text="Date of evaluation : ",
        font=('Times', 14, 'bold'), width=20, height=1,
        bg='DodgerBlue2', fg='white', anchor=tk.W)
    self.wlbl_evadate = self.can.create_window(self.x97, self.y97,
        window = self.lbl_evadate)

    self.x98, self.y98 = 240, 2270
    self.ntry_eva = tk.StringVar()
    self.entryname = tk.Entry(self.can, textvariable=self.ntry_eva, width=10)
    self.ntry_eva.set(time.strftime("%d/%m/%Y"))
    self.wentryname = self.can.create_window(self.x98, self.y98,
        window = self.entryname)    

    self.x99, self.y99 = 80, 2315
    self.lbl_parcvita = tk.Label(self.can, text="Path life : ",
        font=('Times', 14, 'bold'), width=20, height=1,
        bg='DodgerBlue2', fg='white', anchor=tk.W)
    self.wlbl_parcvita = self.can.create_window(self.x99, self.y99,
        window = self.lbl_parcvita)

    def importationFile(fichier):
        file = open(fichier, 'r')
        content = file.readlines()
        file.close()
        for li in content:
            self.t100.config(state='normal')
            self.t100.insert(tk.END, li)
            self.t100.config(state='normal')

    self.x100, self.y100 = 600, 2405
    self.t100 = tk.Text(self.can, height=10, width=80, font=18,
        relief=tk.SUNKEN)
    self.t100.bind("<Button-1>", deactscroll)
    self.wt100_window = self.can.create_window(self.x100, self.y100,
        window=self.t100)

    try:
        if os.path.getsize('./dmst_doc/doc_dmst15/parcours.txt'):
            print("[+] File 'parcours.txt' exist !")
            importationFile('./dmst_doc/doc_dmst15/parcours.txt')
    except FileNotFoundError as nf_file:
        print("[!] File 'parcours.txt' does not exist !")
        print(nf_file)

    self.x101, self.y101 = 80, 2540 # 80, 2020
    self.lbl_pbm = tk.Label(self.can, text="Problematic : ",
        font=('Times', 14, 'bold'), width=20, height=1,
        bg='DodgerBlue2', fg='white', anchor=tk.W)
    self.wlbl_pbm = self.can.create_window(self.x101, self.y101,
        window = self.lbl_pbm)

    def pbmimport(fichier):
        secfile = open(fichier, 'r')
        seccontent = secfile.readlines()
        secfile.close()
        for li in seccontent:
            self.t102.config(state='normal')
            self.t102.insert(tk.END, li)
            self.t102.config(state='normal')

    self.x102, self.y102 = 600, 2625
    self.t102 = tk.Text(self.can, height=10, width=80, font=18,
        relief=tk.SUNKEN)
    self.t102.bind("<Button-1>", deactscroll)
    self.wt102_window = self.can.create_window(self.x102, self.y102,
        window=self.t102)

    try:
        if os.path.getsize('./dmst_doc/doc_dmst15/pbm.txt'):
            print("[+] File 'pbm.txt' exist !")
            pbmimport('./dmst_doc/doc_dmst15/pbm.txt')
    except FileNotFoundError as pbm_f:
        print("[!] File 'pbm.txt' does not exist !")
        print(pbm_f)

    self.x103, self.y103 = 80, 2760
    self.lbl_project = tk.Label(self.can, text="Personal targets : ",
        font=('Times', 14, 'bold'), width=20, height=1,
        bg='DodgerBlue2', fg='white', anchor=tk.W)
    self.wlbl_project = self.can.create_window(self.x103, self.y103,
        window = self.lbl_project)

    def projectimport(fichier):
        thirdfile = open(fichier, 'r')
        thirdcontent = thirdfile.readlines()
        thirdfile.close()
        for li in thirdcontent:
            self.t104.config(state='normal')
            self.t104.insert(tk.END, li)
            self.t104.config(state='normal')

    self.x104, self.y104 = 600, 2845
    self.t104 = tk.Text(self.can, height=10, width=80, font=18,
        relief=tk.SUNKEN)
    self.t104.bind("<Button-1>", deactscroll)
    self.wt104_window = self.can.create_window(self.x104, self.y104,
        window=self.t104)

    try:
        if os.path.getsize('./dmst_doc/doc_dmst15/project.txt'):
            print("[+] File 'project.txt' exist !")
            projectimport('./dmst_doc/doc_dmst15/project.txt')
    except FileNotFoundError as project_f:
        print("[!] File 'project.txt' does not exist !")
        print(project_f)

    def msgvalidate():
        """
            To display a msg to confirm that all data have been saved.
        """
        tk.messagebox.showinfo("Confirmation", "Record confirmed and finished !")

    def way_back():
        """
            To return back to main page.
        """
        try:
            self.showPatients()
        except (OSError, ValueError) as p_out:
            print("Error from dmst to way out", p_out)

    def record_alldata(self):
        """
            That the main function to save all data by calling other functions.
        """
        MsgBox = tk.messagebox.askyesno('Record', 'Data will be saved, ok ?')
        if MsgBox == 1:
            saveData(self)
            launchfunc(self)
            copytobackup()
            uptoserv()
            msgvalidate()
            way_back()
        else:
            tk.messagebox.showinfo('Return', 'Ok, nothing has changed...')

    def prireadfunc():

        callplatform = platform.system()
        print(platform.system())
        
        if callplatform == 'Linux':
            os.system('gio open "./dmst_doc/doc_dmst15/rslt_dmst15.txt"')
        elif callplatform =='Darwin':
            subprocess.call('./dmst_doc/doc_dmst15/rslt_dmst15.txt')
        else:
            os.startfile('./dmst_doc/doc_dmst15/rslt_dmst15.txt')

    # Button to read and print
    self.x109, self.y109 = 600, 3020
    self.buttreadprint = tk.Button(self.can, text="Read / Print",
        width=10, bd=3, fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise',
        highlightbackground='DodgerBlue2', command = prireadfunc)
    self.buttreadprint = self.can.create_window(self.x109, self.y109,
        window = self.buttreadprint)

    # Button save
    self.x110, self.y110 = 800, 3020
    self.buttonsave = tk.Button(self.can, text="Save", width=10, bd=3,
        fg='yellow', bg='RoyalBlue3', activebackground='pale turquoise',
        highlightbackground='DodgerBlue2', command=lambda: record_alldata(self))
    self.buttonsave = self.can.create_window(self.x110, self.y110,
        window = self.buttonsave)

    # Button quit
    self.x111, self.y111 = 1020, 3020
    self.buttonquit = tk.Button(self.can, text='Return to main menu',
        width=20, bd=3, fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise',
        highlightbackground='DodgerBlue2', command = way_back)
    self.buttonquit = self.can.create_window(self.x111, self.y111,
        window = self.buttonquit)

    # Label ghost
    self.x112, self.y112 = 80, 3070
    self.lbl_ghost = tk.Label(self.can, text="",
        font=('Times', 14, 'bold'), width=20, height=1,
        bg='DodgerBlue2', fg='white')
    self.wlbl_ghost = self.can.create_window(self.x112, self.y112,
        window = self.lbl_ghost)

    self.can.configure(scrollregion=self.can.bbox(tk.ALL))
    self.can.bind("<Button-1>", self.reinitscroll)
