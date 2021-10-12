#!/usr/bin/python3
# -*- coding:utf-8 -*-


"""
    Main frame of Labo Check.
    Record psychomedication checked
    into files and upload them
    directly after.
"""


from tkinter import *
import tkinter as tk
from tkinter import messagebox
import os
import subprocess
import platform
import time

from labo.recorderesult.recrslt16 import checkerecord16
from labo.uploadreclab.uploadrslt16 import uploadata16

from labo.funcplatform.resultfunc16 import funcOsLab16
from labo.funcplatform.resultfunc16 import funcOsMicrobio16
from labo.funcplatform.resultfunc16 import callingOsRslt16


def callLabo16(self):
    """
        To display labo into Canvas
    """
    self.can.delete(ALL)
    self.can.configure(bg='DodgerBlue2')

    self.x1, self.y1 = 540, 45
    self.labelname = tk.Label(self.can, text="Labo check",
        font=('helvetica', 18, 'bold'), width=10,
        height=2, bg='DodgerBlue2', fg='white')
    self.labelname = self.can.create_window(self.x1, self.y1,
        window = self.labelname)

    def recordOption(self):
        """
            Record options checked !
        """
        checkerecord16(self)

    def recordToServer():
        """
            To upload data on server after creating files
        """
        uploadata16()

    def confRec():
        """
            Msg to verify if everything is ok.
        """
        tk.messagebox.showinfo("Confirmation", "Record on server confirmed and finished !")

    def recordTofile(self):
        """
            To record data and upload to server with msg of confirmation !
        """
        MsgBox = tk.messagebox.askyesno("Record", "Results will be saved into Care"\
            "and Monitoring, ok ?")
        if MsgBox == 1:
            recordOption(self)
            print("\n[Saved] Ok, data saved !\n")
            recordToServer()
            print("\n[Uploaded] Ok, data uploaded !\n")
            confRec()
            #self.can.delete(ALL)
            self.showPatients()
        else:
            tk.messagebox.showinfo('Return', 'Ok, nothing has changed.')

    with open('./newpatient/entryfile16.txt', 'r') as filename:
        line1 = filename.readline()

    self.x2, self.y2 = 720, 45
    self.entrytext = tk.StringVar()
    self.entryname = tk.Entry(self.can, textvariable=self.entrytext, width=20)
    self.entrytext.set(line1[:-1])
    self.entryname = self.can.create_window(self.x2, self.y2,
        window = self.entryname)

    self.x3, self.y3 = 625, 100
    self.labelresult = tk.Label(self.can, text='--- Neuroleptiques ---',
        font="Times 14 bold", width=135,
        height=1, bg='RoyalBlue3', fg='white')
    self.labelresult = self.can.create_window(self.x3, self.y3,
        window = self.labelresult)

    self.x4, self.y4 = 134, 125
    self.CheckVar1 = tk.IntVar()
    self.C1 = tk.Checkbutton(self.can, text="Abilify (aripiprazol)", fg='navy',
        bg='cyan', variable=self.CheckVar1,
        onvalue=1, offvalue=0, height=1,
        width=26, anchor="w")
    self.C1 = self.can.create_window(self.x4, self.y4,
        window = self.C1)

    self.x5, self.y5 = 134, 148
    self.CheckVar2 = tk.IntVar()
    self.C2 = tk.Checkbutton(self.can, text="Clopixol (zuclopenthixol)", fg='navy',
        bg='cyan', variable=self.CheckVar2,
        onvalue=1, offvalue=0, height=1,
        width=26, anchor="w")
    self.C2 = self.can.create_window(self.x5, self.y5,
        window = self.C2)

    self.x6, self.y6 = 134, 171
    self.CheckVar3 = tk.IntVar()
    self.C3 = tk.Checkbutton(self.can, text="Clozapine (clopin, leponex)", fg='navy',
        bg='cyan', variable=self.CheckVar3,
        onvalue=1, offvalue=0, height=1,
        width=26, anchor="w")
    self.C3 = self.can.create_window(self.x6, self.y6,
        window = self.C3)

    self.x7, self.y7 = 134, 194
    self.CheckVar4 = tk.IntVar()
    self.C4 = tk.Checkbutton(self.can, text="Dogmatil (sulprid)", fg='navy',
        bg='cyan', variable=self.CheckVar4,
        onvalue=1, offvalue=0, height=1,
        width=26, anchor="w")
    self.C4 = self.can.create_window(self.x7, self.y7,
        window = self.C4)

    self.x8, self.y8 = 134, 217
    self.CheckVar5 = tk.IntVar()
    self.C5 = tk.Checkbutton(self.can, text="Entumine (clotiapin)", fg='navy',
        bg='cyan', variable=self.CheckVar5,
        onvalue=1, offvalue=0, height=1,
        width=26, anchor="w")
    self.C5 = self.can.create_window(self.x8, self.y8,
        window = self.C5)

    self.x9, self.y9 = 461, 125
    self.CheckVar6 = tk.IntVar()
    self.C6 = tk.Checkbutton(self.can, text="Fluanxol (flupentixol)", fg='navy',
        bg='cyan', variable=self.CheckVar6,
        onvalue=1, offvalue=0, height=1,
        width=26, anchor="w")
    self.C6 = self.can.create_window(self.x9, self.y9,
        window = self.C6)

    self.x10, self.y10 = 461, 148
    self.CheckVar7 = tk.IntVar()
    self.C7 = tk.Checkbutton(self.can, text="Haldol (haloperidol)", fg='navy',
        bg='cyan', variable=self.CheckVar7,
        onvalue=1, offvalue=0, height=1,
        width=26, anchor="w")
    self.C7 = self.can.create_window(self.x10, self.y10,
        window = self.C7)

    self.x11, self.y11 = 461, 171
    self.CheckVar8 = tk.IntVar()
    self.C8 = tk.Checkbutton(self.can, text="Invega (paliperidon)", fg='navy',
        bg='cyan', variable=self.CheckVar8,
        onvalue=1, offvalue=0, height=1,
        width=26, anchor="w")
    self.C8 = self.can.create_window(self.x11, self.y11,
        window = self.C8)

    self.x12, self.y12 = 461, 194
    self.CheckVar9 = tk.IntVar()
    self.C9 = tk.Checkbutton(self.can, text="Nozinan (levomepromazin)", fg='navy',
        bg='cyan', variable=self.CheckVar9,
        onvalue=1, offvalue=0, height=1,
        width=26, anchor="w")
    self.C9 = self.can.create_window(self.x12, self.y12,
        window = self.C9)

    self.x13, self.y13 = 461, 217
    self.CheckVar10 = tk.IntVar()
    self.C10 = tk.Checkbutton(self.can, text="Prazine (promazin)", fg='navy',
        bg='cyan', variable=self.CheckVar10,
        onvalue=1, offvalue=0, height=1,
        width=26, anchor="w")
    self.C10 = self.can.create_window(self.x13, self.y13,
        window = self.C10)

    self.x14, self.y14 = 790, 125
    self.CheckVar12 = tk.IntVar()
    self.C12 = tk.Checkbutton(self.can, text="Quetiapine (seroquel, sequase)", fg='navy',
        bg='cyan', variable=self.CheckVar12,
        onvalue=1, offvalue=0, height=1,
        width=26, anchor="w")
    self.C12 = self.can.create_window(self.x14, self.y14,
        window = self.C12)

    self.x15, self.y15 = 790, 148
    self.CheckVar13 = tk.IntVar()
    self.C13 = tk.Checkbutton(self.can, text="Risperdal (risperidon)", fg='navy',
        bg='cyan', variable=self.CheckVar13,
        onvalue=1, offvalue=0, height=1,
        width=26, anchor="w")
    self.C13 = self.can.create_window(self.x15, self.y15,
        window = self.C13)

    self.x16, self.y16 = 790, 171
    self.CheckVar14 = tk.IntVar()
    self.C14 = tk.Checkbutton(self.can, text="Serdolect (sertindol)", fg='navy',
        bg='cyan', variable=self.CheckVar14,
        onvalue=1, offvalue=0, height=1,
        width=26, anchor="w")
    self.C14 = self.can.create_window(self.x16, self.y16,
        window = self.C14)

    self.x17, self.y17 = 790, 194
    self.CheckVar15 = tk.IntVar()
    self.C15 = tk.Checkbutton(self.can, text="Solian (amisulprid)", fg='navy',
        bg='cyan', variable=self.CheckVar15,
        onvalue=1, offvalue=0, height=1,
        width=26, anchor="w")
    self.C15 = self.can.create_window(self.x17, self.y17,
        window = self.C15)

    self.x18, self.y18 = 790, 217
    self.CheckVar16 = tk.IntVar()
    self.C16 = tk.Checkbutton(self.can, text="Tiapridal (tiaprid)", fg='navy',
        bg='cyan', variable=self.CheckVar16,
        onvalue=1, offvalue=0, height=1,
        width=26, anchor="w")
    self.C16 = self.can.create_window(self.x18, self.y18,
        window = self.C16)

    self.x19, self.y19 = 1117, 125
    self.CheckVar17 = tk.IntVar()
    self.C17 = tk.Checkbutton(self.can, text="Truxal (chlorprothixen)", fg='navy',
        bg='cyan', variable=self.CheckVar17,
        onvalue=1, offvalue=0, height=1,
        width=26, anchor="w")
    self.C17 = self.can.create_window(self.x19, self.y19,
        window = self.C17)

    self.x20, self.y20 = 1117, 148
    self.CheckVar18 = tk.IntVar()
    self.C18 = tk.Checkbutton(self.can, text="Zyprexa (olanzapin)", fg='navy',
        bg='cyan', variable=self.CheckVar18,
        onvalue=1, offvalue=0, height=1,
        width=26, anchor="w")
    self.C18 = self.can.create_window(self.x20, self.y20,
        window = self.C18)

    # MAE
    self.x21, self.y21 = 625, 243
    self.labelresult2 = tk.Label(self.can, text='--- Médicaments anti-épileptiques ---',
        font="Times 14 bold", width=135,
        height=1, bg='RoyalBlue3', fg='white')
    self.labelresult2 = self.can.create_window(self.x21, self.y21,
        window = self.labelresult2)

    #separator = tk.Label(self.can, height=5, bd=2, relief=SUNKEN)
    #separator.grid(sticky='ns', row=2, column=1)

    self.x22, self.y22 = 134, 268
    self.CheckVar19 = tk.IntVar()
    self.C19 = tk.Checkbutton(self.can, text="Briviact (brivaracetam)", fg='navy',
        bg='cyan', variable=self.CheckVar19,
        onvalue=1, offvalue=0, height=1,
        width=26, anchor="w")
    self.C19 = self.can.create_window(self.x22, self.y22,
        window = self.C19)

    self.x23, self.y23 = 134, 291
    self.CheckVar20 = tk.IntVar()
    self.C20 = tk.Checkbutton(self.can, text="Carbamazepine (tegretol)", fg='navy',
        bg='cyan', variable=self.CheckVar20,
        onvalue=1, offvalue=0, height=1,
        width=26, anchor="w")
    self.C20 = self.can.create_window(self.x23, self.y23,
        window = self.C20)

    self.x24, self.y24 = 134, 314
    self.CheckVar21 = tk.IntVar()
    self.C21 = tk.Checkbutton(self.can, text="Depakine (valproate)", fg='navy',
        bg='cyan', variable=self.CheckVar21,
        onvalue=1, offvalue=0, height=1,
        width=26, anchor="w")
    self.C21 = self.can.create_window(self.x24, self.y24,
        window = self.C21)

    self.x25, self.y25 = 134, 337
    self.CheckVar22 = tk.IntVar()
    self.C22 = tk.Checkbutton(self.can, text="Ethosuximide (petinimid)", fg='navy',
        bg='cyan', variable=self.CheckVar22,
        onvalue=1, offvalue=0, height=1,
        width=26, anchor="w")
    self.C22 = self.can.create_window(self.x25, self.y25,
        window = self.C22)

    self.x26, self.y26 = 134, 360
    self.CheckVar23 = tk.IntVar()
    self.C23 = tk.Checkbutton(self.can, text="Fycompa (perampanel)", fg='navy',
        bg='cyan', variable=self.CheckVar23,
        onvalue=1, offvalue=0, height=1,
        width=26, anchor="w")
    self.C23 = self.can.create_window(self.x26, self.y26,
        window = self.C23)

    self.x27, self.y27 = 134, 383
    self.CheckVar24 = tk.IntVar()
    self.C24 = tk.Checkbutton(self.can, text="Gabitril (tiagabine)", fg='navy',
        bg='cyan', variable=self.CheckVar24,
        onvalue=1, offvalue=0, height=1,
        width=26, anchor="w")
    self.C24 = self.can.create_window(self.x27, self.y27,
        window = self.C24)

    self.x28, self.y28 = 461, 268
    self.CheckVar25 = tk.IntVar()
    self.C25 = tk.Checkbutton(self.can, text="Inovelon (rufinamid)", fg='navy',
        bg='cyan', variable=self.CheckVar25,
        onvalue=1, offvalue=0, height=1,
        width=26, anchor="w")
    self.C25 = self.can.create_window(self.x28, self.y28,
        window = self.C25)

    self.x29, self.y29 = 461, 291
    self.CheckVar26 = tk.IntVar()
    self.C26 = tk.Checkbutton(self.can, text="Keppra (levetiracetam)", fg='navy',
        bg='cyan', variable=self.CheckVar26,
        onvalue=1, offvalue=0, height=1,
        width=26, anchor="w")
    self.C26 = self.can.create_window(self.x29, self.y29,
        window = self.C26)

    self.x30, self.y30 = 461, 314
    self.CheckVar27 = tk.IntVar()
    self.C27 = tk.Checkbutton(self.can, text="Lamictal (lamotrigine)", fg='navy',
        bg='cyan', variable=self.CheckVar27,
        onvalue=1, offvalue=0, height=1,
        width=26, anchor="w")
    self.C27 = self.can.create_window(self.x30, self.y30,
        window = self.C27)

    self.x31, self.y31 = 461, 337
    self.CheckVar28 = tk.IntVar()
    self.C28 = tk.Checkbutton(self.can, text="Lyrica (pregabalin)", fg='navy',
        bg='cyan', variable=self.CheckVar28,
        onvalue=1, offvalue=0, height=1,
        width=26, anchor="w")
    self.C28 = self.can.create_window(self.x31, self.y31,
        window = self.C28)

    self.x32, self.y32 = 461, 360
    self.CheckVar29 = tk.IntVar()
    self.C29 = tk.Checkbutton(self.can, text="Myzoline (primidon)", fg='navy',
        bg='cyan', variable=self.CheckVar29,
        onvalue=1, offvalue=0, height=1,
        width=26, anchor="w")
    self.C29 = self.can.create_window(self.x32, self.y32,
        window = self.C29)

    self.x33, self.y33 = 461, 383
    self.CheckVar30 = tk.IntVar()
    self.C30 = tk.Checkbutton(self.can, text="Neurontin (gabapentin)", fg='navy',
        bg='cyan', variable=self.CheckVar30,
        onvalue=1, offvalue=0, height=1,
        width=26, anchor="w")
    self.C30 = self.can.create_window(self.x33, self.y33,
        window = self.C30)

    self.x34, self.y34 = 790, 268
    self.CheckVar31 = tk.IntVar()
    self.C31 = tk.Checkbutton(self.can, text="Phenobarbital (aphenylbarbit)", fg='navy',
        bg='cyan', variable=self.CheckVar31,
        onvalue=1, offvalue=0, height=1,
        width=26, anchor="w")
    self.C31 = self.can.create_window(self.x34, self.y34,
        window = self.C31)

    self.x35, self.y35 = 790, 291
    self.CheckVar32 = tk.IntVar()
    self.C32 = tk.Checkbutton(self.can, text="Phenytoïne", fg='navy',
        bg='cyan', variable=self.CheckVar32,
        onvalue=1, offvalue=0, height=1,
        width=26, anchor="w")
    self.C32 = self.can.create_window(self.x35, self.y35,
        window = self.C32)

    self.x36, self.y36 = 790, 314
    self.CheckVar33 = tk.IntVar()
    self.C33 = tk.Checkbutton(self.can, text="Sabril (vigabatrin)", fg='navy',
        bg='cyan', variable=self.CheckVar33,
        onvalue=1, offvalue=0, height=1,
        width=26, anchor="w")
    self.C33 = self.can.create_window(self.x36, self.y36,
        window = self.C33)

    self.x37, self.y37 = 790, 337
    self.CheckVar34 = tk.IntVar()
    self.C34 = tk.Checkbutton(self.can, text="Taloxa (felbamate)", fg='navy',
        bg='cyan', variable=self.CheckVar34,
        onvalue=1, offvalue=0, height=1,
        width=26, anchor="w")
    self.C34 = self.can.create_window(self.x37, self.y37,
        window = self.C34)

    self.x38, self.y38 = 790, 360
    self.CheckVar35 = tk.IntVar()
    self.C35 = tk.Checkbutton(self.can, text="Topamax (topiramate)", fg='navy',
        bg='cyan', variable=self.CheckVar35,
        onvalue=1, offvalue=0, height=1,
        width=26, anchor="w")
    self.C35 = self.can.create_window(self.x38, self.y38,
        window = self.C35)

    self.x39, self.y39 = 790, 383
    self.CheckVar36 = tk.IntVar()
    self.C36 = tk.Checkbutton(self.can, text="Trileptal (oxcarbazepin)", fg='navy',
        bg='cyan', variable=self.CheckVar36,
        onvalue=1, offvalue=0, height=1,
        width=26, anchor="w")
    self.C36 = self.can.create_window(self.x39, self.y39,
        window = self.C36)

    self.x40, self.y40 = 1117, 268
    self.CheckVar37 = tk.IntVar()
    self.C37 = tk.Checkbutton(self.can, text="Trobalt (retigabin)", fg='navy',
        bg='cyan', variable=self.CheckVar37,
        onvalue=1, offvalue=0, height=1,
        width=26, anchor="w")
    self.C37 = self.can.create_window(self.x40, self.y40,
        window = self.C37)

    self.x41, self.y41 = 1117, 291
    self.CheckVar38 = tk.IntVar()
    self.C38 = tk.Checkbutton(self.can, text="Vimpat (lacosamid)", fg='navy',
        bg='cyan', variable=self.CheckVar38,
        onvalue=1, offvalue=0, height=1,
        width=26, anchor="w")
    self.C38 = self.can.create_window(self.x41, self.y41,
        window = self.C38)

    self.x42, self.y42 = 1117, 314
    self.CheckVar39 = tk.IntVar()
    self.C39 = tk.Checkbutton(self.can, text="Zonegran (zonisamid)", fg='navy',
        bg='cyan', variable=self.CheckVar39,
        onvalue=1, offvalue=0, height=1,
        width=26, anchor="w")
    self.C39 = self.can.create_window(self.x42, self.y42,
        window = self.C39)

    # ATD
    self.x43, self.y43 = 625, 409
    self.labelresult3 = tk.Label(self.can, text='--- Antidépresseurs ---',
        font="Times 14 bold", width=135,
        height=1, bg='RoyalBlue3', fg='white')
    self.labelresult3 = self.can.create_window(self.x43, self.y43,
        window = self.labelresult3)

    self.x44, self.y44 = 134, 434
    self.CheckVar40 = tk.IntVar()
    self.C40 = tk.Checkbutton(self.can, text="Anafrani (clomipramin)", fg='navy',
        bg='cyan', variable=self.CheckVar40,
        onvalue=1, offvalue=0, height=1,
        width=26, anchor="w")
    self.C40 = self.can.create_window(self.x44, self.y44,
        window = self.C40)

    self.x45, self.y45 = 134, 457
    self.CheckVar41 = tk.IntVar()
    self.C41 = tk.Checkbutton(self.can, text="Citalopram", fg='navy',
        bg='cyan', variable=self.CheckVar41,
        onvalue=1, offvalue=0, height=1,
        width=26, anchor="w")
    self.C41 = self.can.create_window(self.x45, self.y45,
        window = self.C41)

    self.x46, self.y46 = 134, 480
    self.CheckVar42 = tk.IntVar()
    self.C42 = tk.Checkbutton(self.can, text="Cipralex (escitalopram)", fg='navy',
        bg='cyan', variable=self.CheckVar42,
        onvalue=1, offvalue=0, height=1,
        width=26, anchor="w")
    self.C42 = self.can.create_window(self.x46, self.y46,
        window = self.C42)

    self.x47, self.y47 = 134, 503
    self.CheckVar43 = tk.IntVar()
    self.C43 = tk.Checkbutton(self.can, text="Cymbalta (duloxetin)", fg='navy',
        bg='cyan', variable=self.CheckVar43,
        onvalue=1, offvalue=0, height=1,
        width=26, anchor="w")
    self.C43 = self.can.create_window(self.x47, self.y47,
        window = self.C43)

    self.x48, self.y48 = 461, 434
    self.CheckVar44 = tk.IntVar()
    self.C44 = tk.Checkbutton(self.can, text="Deroxat (paroxetin)", fg='navy',
        bg='cyan', variable=self.CheckVar44,
        onvalue=1, offvalue=0, height=1,
        width=26, anchor="w")
    self.C44 = self.can.create_window(self.x48, self.y48,
        window = self.C44)

    self.x49, self.y49 = 461, 457
    self.CheckVar45 = tk.IntVar()
    self.C45 = tk.Checkbutton(self.can, text="Effexor (venlafaxin)", fg='navy',
        bg='cyan', variable=self.CheckVar45,
        onvalue=1, offvalue=0, height=1,
        width=26, anchor="w")
    self.C45 = self.can.create_window(self.x49, self.y49,
        window = self.C45)

    self.x50, self.y50 = 461, 480
    self.CheckVar46 = tk.IntVar()
    self.C46 = tk.Checkbutton(self.can, text="Floxifral (fluvoxamin)", fg='navy',
        bg='cyan', variable=self.CheckVar46,
        onvalue=1, offvalue=0, height=1,
        width=26, anchor="w")
    self.C46 = self.can.create_window(self.x50, self.y50,
        window = self.C46)

    self.x51, self.y51 = 461, 503
    self.CheckVar47 = tk.IntVar()
    self.C47 = tk.Checkbutton(self.can, text="Fluctine (fluoxetin)", fg='navy',
        bg='cyan', variable=self.CheckVar47,
        onvalue=1, offvalue=0, height=1,
        width=26, anchor="w")
    self.C47 = self.can.create_window(self.x51, self.y51,
        window = self.C47)

    self.x52, self.y52 = 790, 434
    self.CheckVar48 = tk.IntVar()
    self.C48 = tk.Checkbutton(self.can, text="Ludiomil (maprotilin)", fg='navy',
        bg='cyan', variable=self.CheckVar48,
        onvalue=1, offvalue=0, height=1,
        width=26, anchor="w")
    self.C48 = self.can.create_window(self.x52, self.y52,
        window = self.C48)

    self.x53, self.y53 = 790, 457
    self.CheckVar49 = tk.IntVar()
    self.C49 = tk.Checkbutton(self.can, text="Remeron (mirtazapin)", fg='navy',
        bg='cyan', variable=self.CheckVar49,
        onvalue=1, offvalue=0, height=1,
        width=26, anchor="w")
    self.C49 = self.can.create_window(self.x53, self.y53,
        window = self.C49)

    self.x54, self.y54 = 790, 480
    self.CheckVar50 = tk.IntVar()
    self.C50 = tk.Checkbutton(self.can, text="Saroten (amitriptylin)", fg='navy',
        bg='cyan', variable=self.CheckVar50,
        onvalue=1, offvalue=0, height=1,
        width=26, anchor="w")
    self.C50 = self.can.create_window(self.x54, self.y54,
        window = self.C50)

    self.x55, self.y55 = 790, 503
    self.CheckVar51 = tk.IntVar()
    self.C51 = tk.Checkbutton(self.can, text="Sertraline (zoloft)", fg='navy',
        bg='cyan', variable=self.CheckVar51,
        onvalue=1, offvalue=0, height=1,
        width=26, anchor="w")
    self.C51 = self.can.create_window(self.x55, self.y55,
        window = self.C51)

    self.x56, self.y56 = 1117, 434
    self.CheckVar52 = tk.IntVar()
    self.C52 = tk.Checkbutton(self.can, text="Surmontil (trimipramin)", fg='navy',
        bg='cyan', variable=self.CheckVar52,
        onvalue=1, offvalue=0, height=1,
        width=26, anchor="w")
    self.C52 = self.can.create_window(self.x56, self.y56,
        window = self.C52)

    self.x57, self.y57 = 1117, 457
    self.CheckVar53 = tk.IntVar()
    self.C53 = tk.Checkbutton(self.can, text="Wellbutrin (bupropion)", fg='navy',
        bg='cyan', variable=self.CheckVar53,
        onvalue=1, offvalue=0, height=1,
        width=26, anchor="w")
    self.C53 = self.can.create_window(self.x57, self.y57,
        window = self.C53)

    # Lithium
    self.x60, self.y60 = 790, 528
    self.labelinfuri = tk.Label(self.can, text='--- Lithium ---',
        font="Times 14 bold", width=26,
        height=1, bg='RoyalBlue3', fg='white')
    self.labelinfuri = self.can.create_window(self.x60, self.y60,
        window = self.labelinfuri)

    self.x70, self.y70 = 790, 553
    self.CheckVar54 = tk.IntVar()
    self.C54 = tk.Checkbutton(self.can, text="Lithiofor (lithium)", fg='navy',
        bg='cyan', variable=self.CheckVar54,
        onvalue=1, offvalue=0, height=1,
        width=26, anchor="w")
    self.C54 = self.can.create_window(self.x70, self.y70,
        window = self.C54)

    def comburTips():
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        subprocess.run('./labo/combtest16.py', check=True)
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()

    self.x80, self.y80 = 1117, 530
    self.buttonstix = tk.Button(self.can, text='Stix', width=10, bd=3,
        fg='cyan', bg='RoyalBlue3', activebackground='pale turquoise',
        highlightbackground='cyan', command=comburTips)
    self.buttonstix = self.can.create_window(self.x80, self.y80,
        window = self.buttonstix)

    # Printable
    self.x90, self.y90 = 298, 528
    self.labelresult4 = tk.Label(self.can, text='--- Printable ---',
        font="Times 14 bold", width=62,
        height=1, bg='RoyalBlue3', fg='white')
    self.labelresult4 = self.can.create_window(self.x90, self.y90,
        window = self.labelresult4)

    def sheetLabo():
        """
            For openning file at pdf
            format with a bit prog-sys code.
            For Linux, Windows and MAC.
        """
        funcOsLab16()

    # Buttons printable sheet
    self.x100, self.y100 = 140, 620
    self.buttonSheet = tk.Button(self.can,
        text="Complete lab sheet", width=15, fg='cyan', bg='navy',
        activebackground='pale turquoise', command=sheetLabo)
    self.buttonSheet = self.can.create_window(self.x100,
        self.y100, window = self.buttonSheet)

    def sheetMicrobio():
        """
            For openning file at pdf
            format with a bit prog-sys code.
            For Linux, Windows and MAC.
        """
        funcOsMicrobio16()

    self.x110, self.y110 = 460, 620
    self.buttonMicro = tk.Button(self.can,
        text="Microbiology sheet", width=15, fg='cyan', bg='navy',
        activebackground='pale turquoise', command=sheetMicrobio)
    self.buttonMicro = self.can.create_window(self.x110,
        self.y110, window = self.buttonMicro)

    def printLabo():
        """
            Need to be modified in
            function of platform's
            user !!! Here, it's
            for linux ! ;)
        """
        #lpr = subprocess.Popen("/usr/bin/lpr", stdin=subprocess.PIPE)
        #lpr.stdin.write('4.15.0-96-generic')
        pass

    # Button save, read and quit
    self.x120, self.y120 = 710, 620
    self.buttonsave = tk.Button(self.can, text="Save", width=10, bd=3,
        fg='yellow', bg='RoyalBlue3', activebackground='pale turquoise',
        highlightbackground='cyan', command= lambda: recordTofile(self))
    self.fbuttonsave_window = self.can.create_window(self.x120, self.y120,
        window = self.buttonsave)

    def read_file():
        """
            To read laborslt.txt
        """
        callingOsRslt16()

    self.x130, self.y130 = 870, 620
    self.buttread = tk.Button(self.can, text="Read", width=10, bd=3,
        fg='cyan', bg='RoyalBlue3', activebackground='pale turquoise',
        highlightbackground='cyan', command=read_file)
    self.fbuttread_window = self.can.create_window(self.x130, self.y130,
        window = self.buttread)

    def awayOut():
        try:
            self.can.delete(ALL)
            self.showPatients()
        except (OSError, ValueError) as p_out:
            print("[!] Error from labo to way out", p_out)

    self.x140, self.y140 = 1110, 620
    self.buttonquit = tk.Button(self.can, text='Return to main menu',
        width=20, bd=3, fg='white', bg='RoyalBlue3',
        activebackground='pale turquoise', highlightbackground='cyan',
        command=awayOut)
    self.fbuttonquit_window = self.can.create_window(self.x140, self.y140,
        window = self.buttonquit)

    self.can.configure(scrollregion=self.can.bbox(ALL))
