#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
    GUI script for auxiliary equipment.
"""


import tkinter as tk
from tkinter import messagebox
import os
from auxequip.folderaux.auxrec7 import transwritedata


def auxi_equip7(self):
    """
        Main function called since main app
        (heal_track.py) for displaying auxiliary
        equipment.
    """
    self.effacer()
    self.delScroll()
    self.can.configure(background='DodgerBlue2')

    self.x1, self.y1 = 530, 45
    self.labl_name = tk.Label(self.can, text="EQUIPMENT FOR : ",
        font=('Times New Roman', 18, 'bold'), width=20,
        height=2, bg='DodgerBlue2', fg='white')
    self.labl_name = self.can.create_window(self.x1, self.y1,
        window = self.labl_name)

    with open('./newpatient/entryfile7.txt', 'r') as filename:
        line1 = filename.readline()

    self.x2, self.y2 = 740, 45
    self.ntry_txt = tk.StringVar()
    self.entryname = tk.Entry(self.can, textvariable=self.ntry_txt, width=20)
    self.ntry_txt.set(line1[:-1])
    self.entryname = self.can.create_window(self.x2, self.y2,
        window = self.entryname)
    
    def showData():
        """
            This function is called when you
            enter this page or after a save.
        """
        self.x3, self.y3 = 205, 370
        self.textbox = tk.Text(self.can, height=30, width=35, font=18, relief=tk.SUNKEN)
        self.textbox.delete('1.0', tk.END)
        self.textbox.update()
        self.ftextbox_window = self.can.create_window(self.x3, self.y3, window=self.textbox)

        def importationFile(fichier, encodage="Utf-8"):
            file = open(fichier, 'r', encoding=encodage)
            content = file.readlines()
            file.close()
            for li in content:
                self.textbox.insert(tk.END, li)

        try:
            if os.path.getsize('./auxequip/doc_equip/auxiliary7.txt'):
                importationFile('./auxequip/doc_equip/auxiliary7.txt', encodage="Utf-8")
        except FileNotFoundError as err_fnfaux:
            print("[!] File auxiliary7.txt for patient 7 not found !", err_fnfaux)
            tk.messagebox.showwarning('Warning', 'File auxiliary7.txt not found !')

    showData()

    self.x30, self.y30 = 500, 120
    self.labl_mob = tk.Label(self.can, text='--- Mobilisation ---',
        font="Times 14 bold", width=21,
        height=1, bg='RoyalBlue3', fg='white')
    self.labl_mob = self.can.create_window(self.x30, self.y30,
        window = self.labl_mob)

    self.x40, self.y40 = 500, 145
    self.CheckVar1 = tk.IntVar()
    self.C1 = tk.Checkbutton(self.can, text="Stick", fg='navy',
        bg='cyan', variable=self.CheckVar1,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C1 = self.can.create_window(self.x40, self.y40,
        window = self.C1)

    self.x50, self.y50 = 500, 167
    self.CheckVar2 = tk.IntVar()
    self.C2 = tk.Checkbutton(self.can, text="Walking Frame", fg='navy',
        bg='cyan', variable=self.CheckVar2,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C2 = self.can.create_window(self.x50, self.y50,
        window = self.C2)

    self.x60, self.y60 = 500, 189
    self.CheckVar3 = tk.IntVar()
    self.C3 = tk.Checkbutton(self.can, text="Rollator", fg='navy',
        bg='cyan', variable=self.CheckVar3,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C3 = self.can.create_window(self.x60, self.y60,
        window = self.C3)

    self.x70, self.y70 = 500, 211
    self.CheckVar4 = tk.IntVar()
    self.C4 = tk.Checkbutton(self.can, text="Wheelchair", fg='navy',
        bg='cyan', variable=self.CheckVar4,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C4 = self.can.create_window(self.x70, self.y70,
        window = self.C4)

    self.x71, self.y71 = 500, 233
    self.CheckVar5 = tk.IntVar()
    self.C5 = tk.Checkbutton(self.can, text="Crutches", fg='navy',
        bg='cyan', variable=self.CheckVar5,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C5 = self.can.create_window(self.x71, self.y71,
        window = self.C5)

    self.x80, self.y80 = 500, 310
    self.labl_appa = tk.Label(self.can, text='--- Equipment ---',
        font="Times 14 bold", width=21,
        height=1, bg='RoyalBlue3', fg='white')
    self.labl_appa = self.can.create_window(self.x80, self.y80,
        window = self.labl_appa)

    self.x90, self.y90 = 500, 335
    self.CheckVar50 = tk.IntVar()
    self.C50 = tk.Checkbutton(self.can, text="Patch", fg='navy',
        bg='cyan', variable=self.CheckVar50,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C50 = self.can.create_window(self.x90, self.y90,
        window = self.C50)

    self.x100, self.y100 = 500, 357
    self.CheckVar60 = tk.IntVar()
    self.C60 = tk.Checkbutton(self.can, text="Pace-maker", fg='navy',
        bg='cyan', variable=self.CheckVar60,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C60 = self.can.create_window(self.x100, self.y100,
        window = self.C60)

    self.x101, self.y101 = 500, 379
    self.CheckVar61 = tk.IntVar()
    self.C61 = tk.Checkbutton(self.can, text="Holter", fg='navy',
        bg='cyan', variable=self.CheckVar61,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C61 = self.can.create_window(self.x101, self.y101,
        window = self.C61)

    self.x110, self.y110 = 500, 401
    self.CheckVar70 = tk.IntVar()
    self.C70 = tk.Checkbutton(self.can, text="Insulin Pump", fg='navy',
        bg='cyan', variable=self.CheckVar70,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C70 = self.can.create_window(self.x110, self.y110,
        window = self.C70)

    self.x120, self.y120 = 500, 423
    self.CheckVar80 = tk.IntVar()
    self.C80 = tk.Checkbutton(self.can, text="Morphine Pump", fg='navy',
        bg='cyan', variable=self.CheckVar80,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C80 = self.can.create_window(self.x120, self.y120,
        window = self.C80)

    self.x130, self.y130 = 500, 445
    self.CheckVar90 = tk.IntVar()
    self.C90 = tk.Checkbutton(self.can, text="VAC (escarre)", fg='navy',
        bg='cyan', variable=self.CheckVar90,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C90 = self.can.create_window(self.x130, self.y130,
        window = self.C90)

    self.x140, self.y140 = 500, 467
    self.CheckVar100 = tk.IntVar()
    self.C100 = tk.Checkbutton(self.can, text="Nasal Cannula", fg='navy',
        bg='cyan', variable=self.CheckVar100,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C100 = self.can.create_window(self.x140, self.y140,
        window = self.C100)

    self.x150, self.y150 = 500, 489
    self.CheckVar110 = tk.IntVar()
    self.C110 = tk.Checkbutton(self.can, text="Eyeglasses", fg='navy',
        bg='cyan', variable=self.CheckVar110,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C110 = self.can.create_window(self.x150, self.y150,
        window = self.C110)

    self.x160, self.y160 = 500, 511
    self.CheckVar120 = tk.IntVar()
    self.C120 = tk.Checkbutton(self.can, text="Hearing Aids L", fg='navy',
        bg='cyan', variable=self.CheckVar120,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C120 = self.can.create_window(self.x160, self.y160,
        window = self.C120)

    self.x161, self.y161 = 500, 533
    self.CheckVar121 = tk.IntVar()
    self.C121 = tk.Checkbutton(self.can, text="Hearing Aids R", fg='navy',
        bg='cyan', variable=self.CheckVar121,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C121 = self.can.create_window(self.x161, self.y161,
        window = self.C121)

    self.x162, self.y162 = 500, 555
    self.CheckVar122 = tk.IntVar()
    self.C122 = tk.Checkbutton(self.can, text="Arterioven. Fistula", fg='navy',
        bg='cyan', variable=self.CheckVar122,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C122 = self.can.create_window(self.x162, self.y162,
        window = self.C122)

    self.x163, self.y163 = 500, 577
    self.CheckVar123 = tk.IntVar()
    self.C123 = tk.Checkbutton(self.can, text="Ostomy Bag", fg='navy',
        bg='cyan', variable=self.CheckVar123,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C123 = self.can.create_window(self.x163, self.y163,
        window = self.C123)

    self.x164, self.y164 = 500, 599
    self.CheckVar124 = tk.IntVar()
    self.C124 = tk.Checkbutton(self.can, text="Perfusion", fg='navy',
        bg='cyan', variable=self.CheckVar124,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C124 = self.can.create_window(self.x164, self.y164,
        window = self.C124)

    self.x165, self.y165 = 500, 621
    self.CheckVar125 = tk.IntVar()
    self.C125 = tk.Checkbutton(self.can, text="Periodical Injection", fg='navy',
        bg='cyan', variable=self.CheckVar125,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C125 = self.can.create_window(self.x165, self.y165,
        window = self.C125)

    self.x170, self.y170 = 900, 120
    self.labl_appa = tk.Label(self.can, text='--- Catheters and Drains ---',
        font="Times 14 bold", width=65,
        height=1, bg='RoyalBlue3', fg='white')
    self.labl_appa = self.can.create_window(self.x170, self.y170,
        window = self.labl_appa)

    self.x180, self.y180 = 700, 145
    self.CheckVar130 = tk.IntVar()
    self.C130 = tk.Checkbutton(self.can, text="Wound Wick", fg='navy',
        bg='cyan', variable=self.CheckVar130,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C130 = self.can.create_window(self.x180, self.y180,
        window = self.C130)

    self.x200, self.y200 = 700, 167
    self.CheckVar150 = tk.IntVar()
    self.C150 = tk.Checkbutton(self.can, text="Redon Drain", fg='navy',
        bg='cyan', variable=self.CheckVar150,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C150 = self.can.create_window(self.x200, self.y200,
        window = self.C150)

    self.x210, self.y210 = 700, 189
    self.CheckVar160 = tk.IntVar()
    self.C160 = tk.Checkbutton(self.can, text="Kher Drain", fg='navy',
        bg='cyan', variable=self.CheckVar160,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C160 = self.can.create_window(self.x210, self.y210,
        window = self.C160)

    self.x220, self.y220 = 700, 211
    self.CheckVar170 = tk.IntVar()
    self.C170 = tk.Checkbutton(self.can, text="Blake Drain", fg='navy',
        bg='cyan', variable=self.CheckVar170,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C170 = self.can.create_window(self.x220, self.y220,
        window = self.C170)

    self.x230, self.y230 = 700, 233
    self.CheckVar180 = tk.IntVar()
    self.C180 = tk.Checkbutton(self.can, text="Penrose Drain", fg='navy',
        bg='cyan', variable=self.CheckVar180,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C180 = self.can.create_window(self.x230, self.y230,
        window = self.C180)

    self.x240, self.y240 = 700, 255
    self.CheckVar190 = tk.IntVar()
    self.C190 = tk.Checkbutton(self.can, text="Mikulicz Drain", fg='navy',
        bg='cyan', variable=self.CheckVar190,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C190 = self.can.create_window(self.x240, self.y240,
        window = self.C190)

    self.x241, self.y241 = 900, 145
    self.CheckVar191 = tk.IntVar()
    self.C191 = tk.Checkbutton(self.can, text="Dialysis", fg='navy',
        bg='cyan', variable=self.CheckVar191,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C191 = self.can.create_window(self.x241, self.y241,
        window = self.C191)

    self.x242, self.y242 = 900, 167
    self.CheckVar192 = tk.IntVar()
    self.C192 = tk.Checkbutton(self.can, text="Biliary Drain", fg='navy',
        bg='cyan', variable=self.CheckVar192,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C192 = self.can.create_window(self.x242, self.y242,
        window = self.C192)

    self.x243, self.y243 = 900, 189
    self.CheckVar193 = tk.IntVar()
    self.C193 = tk.Checkbutton(self.can, text="Urinary Catheter", fg='navy',
        bg='cyan', variable=self.CheckVar193,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C193 = self.can.create_window(self.x243, self.y243,
        window = self.C193)

    self.x244, self.y244 = 900, 211
    self.CheckVar194 = tk.IntVar()
    self.C194 = tk.Checkbutton(self.can, text="Suprapubic Catheter", fg='navy',
        bg='cyan', variable=self.CheckVar194,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C194 = self.can.create_window(self.x244, self.y244,
        window = self.C194)

    self.x190, self.y190 = 900, 233
    self.CheckVar195 = tk.IntVar()
    self.C195 = tk.Checkbutton(self.can, text="Pleural Drain", fg='navy',
        bg='cyan', variable=self.CheckVar195,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C195 = self.can.create_window(self.x190, self.y190,
        window = self.C195)

    self.x190, self.y190 = 900, 255
    self.CheckVar196 = tk.IntVar()
    self.C196 = tk.Checkbutton(self.can, text="Nasogastric Tube", fg='navy',
        bg='cyan', variable=self.CheckVar196,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C196 = self.can.create_window(self.x190, self.y190,
        window = self.C196)

    self.x250, self.y250 = 1100, 145
    self.CheckVar200 = tk.IntVar()
    self.C200 = tk.Checkbutton(self.can, text="VP Shunt", fg='navy',
        bg='cyan', variable=self.CheckVar200,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C200 = self.can.create_window(self.x250, self.y250,
        window = self.C200)

    self.x260, self.y260 = 1100, 167
    self.CheckVar210 = tk.IntVar()
    self.C210 = tk.Checkbutton(self.can, text="VA Shunt", fg='navy',
        bg='cyan', variable=self.CheckVar210,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C210 = self.can.create_window(self.x260, self.y260,
        window = self.C210)

    self.x261, self.y261 = 1100, 189
    self.CheckVar211 = tk.IntVar()
    self.C211 = tk.Checkbutton(self.can, text="3-Ways Catheter", fg='navy',
        bg='cyan', variable=self.CheckVar211,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C211 = self.can.create_window(self.x261, self.y261,
        window = self.C211)

    self.x262, self.y262 = 1100, 211
    self.CheckVar212 = tk.IntVar()
    self.C212 = tk.Checkbutton(self.can, text="PIC-Line", fg='navy',
        bg='cyan', variable=self.CheckVar212,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C212 = self.can.create_window(self.x262, self.y262,
        window = self.C212)

    self.x263, self.y263 = 1100, 233
    self.CheckVar213 = tk.IntVar()
    self.C213 = tk.Checkbutton(self.can, text="Central Catheter", fg='navy',
        bg='cyan', variable=self.CheckVar213,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C213 = self.can.create_window(self.x263, self.y263,
        window = self.C213)

    self.x264, self.y264 = 1100, 255
    self.CheckVar214 = tk.IntVar()
    self.C214 = tk.Checkbutton(self.can, text="Vein-Flon", fg='navy',
        bg='cyan', variable=self.CheckVar214,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C214 = self.can.create_window(self.x264, self.y264,
        window = self.C214)

    self.x270, self.y270 = 900, 310
    self.labl_proth = tk.Label(self.can, text='--- Prosthesis ---',
        font="Times 14 bold", width=65,
        height=1, bg='RoyalBlue3', fg='white')
    self.labl_proth = self.can.create_window(self.x270, self.y270,
        window = self.labl_proth)

    self.x280, self.y280 = 700, 335
    self.CheckVar220 = tk.IntVar()
    self.C220 = tk.Checkbutton(self.can, text="Total Hip L", fg='navy',
        bg='cyan', variable=self.CheckVar220,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C220 = self.can.create_window(self.x280, self.y280,
        window = self.C220)

    self.x290, self.y290 = 700, 357
    self.CheckVar230 = tk.IntVar()
    self.C230 = tk.Checkbutton(self.can, text="Total Hip R", fg='navy',
        bg='cyan', variable=self.CheckVar230,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C230 = self.can.create_window(self.x290, self.y290,
        window = self.C230)

    self.x300, self.y300 = 700, 379
    self.CheckVar240 = tk.IntVar()
    self.C240 = tk.Checkbutton(self.can, text="Total Knee L", fg='navy',
        bg='cyan', variable=self.CheckVar240,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C240 = self.can.create_window(self.x300, self.y300,
        window = self.C240)

    self.x310, self.y310 = 700, 401
    self.CheckVar250 = tk.IntVar()
    self.C250 = tk.Checkbutton(self.can, text="Total Knee R", fg='navy',
        bg='cyan', variable=self.CheckVar250,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C250 = self.can.create_window(self.x310, self.y310,
        window = self.C250)

    self.x320, self.y320 = 700, 423
    self.CheckVar260 = tk.IntVar()
    self.C260 = tk.Checkbutton(self.can, text="Shoulder Prosthesis L", fg='navy',
        bg='cyan', variable=self.CheckVar260,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C260 = self.can.create_window(self.x320, self.y320,
        window = self.C260)

    self.x330, self.y330 = 700, 445
    self.CheckVar270 = tk.IntVar()
    self.C270 = tk.Checkbutton(self.can, text="Shoulder Prosthesis R", fg='navy',
        bg='cyan', variable=self.CheckVar270,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C270 = self.can.create_window(self.x330, self.y330,
        window = self.C270)

    self.x340, self.y340 = 700, 467
    self.CheckVar280 = tk.IntVar()
    self.C280 = tk.Checkbutton(self.can, text="Total Elbow L", fg='navy',
        bg='cyan', variable=self.CheckVar280,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C280 = self.can.create_window(self.x340, self.y340,
        window = self.C280)

    self.x350, self.y350 = 700, 489
    self.CheckVar290 = tk.IntVar()
    self.C290 = tk.Checkbutton(self.can, text="Total Elbow R", fg='navy',
        bg='cyan', variable=self.CheckVar290,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C290 = self.can.create_window(self.x350, self.y350,
        window = self.C290)

    self.x440, self.y440 = 900, 335
    self.CheckVar380 = tk.IntVar()
    self.C380 = tk.Checkbutton(self.can, text="Ocular Prosthesis L", fg='navy',
        bg='cyan', variable=self.CheckVar380,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C380 = self.can.create_window(self.x440, self.y440,
        window = self.C380)

    self.x450, self.y450 = 900, 357
    self.CheckVar390 = tk.IntVar()
    self.C390 = tk.Checkbutton(self.can, text="Ocular Prosthesis R", fg='navy',
        bg='cyan', variable=self.CheckVar390,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C390 = self.can.create_window(self.x450, self.y450,
        window = self.C390)

    self.x460, self.y460 = 900, 379
    self.CheckVar400 = tk.IntVar()
    self.C400 = tk.Checkbutton(self.can, text="Shoe Sole L", fg='navy',
        bg='cyan', variable=self.CheckVar400,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C400 = self.can.create_window(self.x460, self.y460,
        window = self.C400)

    self.x470, self.y470 = 900, 401
    self.CheckVar410 = tk.IntVar()
    self.C410 = tk.Checkbutton(self.can, text="Shoe Sole R", fg='navy',
        bg='cyan', variable=self.CheckVar410,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C410 = self.can.create_window(self.x470, self.y470,
        window = self.C410)

    self.x480, self.y480 = 900, 423
    self.CheckVar420 = tk.IntVar()
    self.C420 = tk.Checkbutton(self.can, text="Lower Dental Prosth. ", fg='navy',
        bg='cyan', variable=self.CheckVar420,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C420 = self.can.create_window(self.x480, self.y480,
        window = self.C420)

    self.x490, self.y490 = 900, 445
    self.CheckVar430 = tk.IntVar()
    self.C430 = tk.Checkbutton(self.can, text="Upper Dental Prosth.", fg='navy',
        bg='cyan', variable=self.CheckVar430,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C430 = self.can.create_window(self.x490, self.y490,
        window = self.C430)

    self.x500, self.y500 = 900, 467
    self.CheckVar440 = tk.IntVar()
    self.C440 = tk.Checkbutton(self.can, text="Maxilofacial Prosthetics", fg='navy',
        bg='cyan', variable=self.CheckVar440,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C440 = self.can.create_window(self.x500, self.y500,
        window = self.C440)

    self.x510, self.y510 = 900, 489
    self.CheckVar450 = tk.IntVar()
    self.C450 = tk.Checkbutton(self.can, text="Nose Prosthesis", fg='navy',
        bg='cyan', variable=self.CheckVar450,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C450 = self.can.create_window(self.x510, self.y510,
        window = self.C450)

    self.x520, self.y520 = 1100, 335
    self.CheckVar300 = tk.IntVar()
    self.C300 = tk.Checkbutton(self.can, text="Foot Prosthesis L", fg='navy',
        bg='cyan', variable=self.CheckVar300,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C300 = self.can.create_window(self.x520, self.y520,
        window = self.C300)

    self.x530, self.y530 = 1100, 357
    self.CheckVar310 = tk.IntVar()
    self.C310 = tk.Checkbutton(self.can, text="Foot Prosthesis R", fg='navy',
        bg='cyan', variable=self.CheckVar310,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C310 = self.can.create_window(self.x530, self.y530,
        window = self.C310)

    self.x540, self.y540 = 1100, 379
    self.CheckVar320 = tk.IntVar()
    self.C320 = tk.Checkbutton(self.can, text="Leg prosthesis L", fg='navy',
        bg='cyan', variable=self.CheckVar320,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C320 = self.can.create_window(self.x540, self.y540,
        window = self.C320)

    self.x550, self.y550 = 1100, 401
    self.CheckVar330 = tk.IntVar()
    self.C330 = tk.Checkbutton(self.can, text="Leg prosthesis R", fg='navy',
        bg='cyan', variable=self.CheckVar330,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C330 = self.can.create_window(self.x550, self.y550,
        window = self.C330)

    self.x560, self.y560 = 1100, 423
    self.CheckVar340 = tk.IntVar()
    self.C340 = tk.Checkbutton(self.can, text="Hand Prosthesis L", fg='navy',
        bg='cyan', variable=self.CheckVar340,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C340 = self.can.create_window(self.x560, self.y560,
        window = self.C340)

    self.x570, self.y570 = 1100, 445
    self.CheckVar350 = tk.IntVar()
    self.C350 = tk.Checkbutton(self.can, text="Hand Prosthesis R", fg='navy',
        bg='cyan', variable=self.CheckVar350,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C350 = self.can.create_window(self.x570, self.y570,
        window = self.C350)

    self.x580, self.y580 = 1100, 467
    self.CheckVar360 = tk.IntVar()
    self.C360 = tk.Checkbutton(self.can, text="Upper Arm Prosth. L", fg='navy',
        bg='cyan', variable=self.CheckVar360,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C360 = self.can.create_window(self.x580, self.y580,
        window = self.C360)

    self.x590, self.y590 = 1100, 489
    self.CheckVar370 = tk.IntVar()
    self.C370 = tk.Checkbutton(self.can, text="Upper Arm Prosth. R", fg='navy',
        bg='cyan', variable=self.CheckVar370,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C370 = self.can.create_window(self.x590, self.y590,
        window = self.C370)

    def wayout():
        """
            The way out to return to main menu (patcaps.py).
        """
        try:
            self.effacer()
            self.showPatients()
        except (OSError, ValueError) as p_out:
            print("Error from labo to way out", p_out)

    self.x600, self.y600 = 780, 580
    self.buttonsave = tk.Button(self.can, text="Save", width=10, bd=3,
        fg='cyan', bg='RoyalBlue3', activebackground='pale turquoise',
        highlightbackground='cyan', command=lambda: ([transwritedata(self), showData()]))
    self.buttonsave = self.can.create_window(self.x600, self.y600,
        window = self.buttonsave)

    self.x610, self.y610 = 1040, 580
    self.buttonquit = tk.Button(self.can, text='Return to main menu', width=20, bd=3,
        fg='white', bg='RoyalBlue3', activebackground='pale turquoise',
        highlightbackground='cyan', command=wayout)
    self.buttonquit = self.can.create_window(self.x610, self.y610,
        window = self.buttonquit)

    self.can.configure(scrollregion=self.can.bbox(tk.ALL))
    self.can.unbind_all("<Button-4>")
    self.can.unbind_all("<Button-5>")
