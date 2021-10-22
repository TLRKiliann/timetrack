#!/usr/bin/python3
# -*- coding: utf-8 -*-


import tkinter as tk
from tkinter import messagebox
import subprocess
import time


def auxi_equip1(self):
    """
        Main function called since main app
        heal_track.py for displaying auxiliary
        equipement.
    """
    self.effacer()
    self.delScroll()
    self.can.configure(background='DodgerBlue2')

    self.x1, self.y1 = 530, 45
    self.labl_name = tk.Label(self.can, text="Auxiliary Equipement",
        font=('helvetica', 18, 'bold'), width=20,
        height=2, bg='DodgerBlue2', fg='white')
    self.labl_name = self.can.create_window(self.x1, self.y1,
        window = self.labl_name)

    with open('./newpatient/entryfile.txt', 'r') as filename:
        line1 = filename.readline()

    self.x2, self.y2 = 760, 45
    ntry_txt = tk.StringVar()
    self.entryname = tk.Entry(self.can, textvariable=ntry_txt, width=20)
    ntry_txt.set(line1[:-1])
    self.entryname = self.can.create_window(self.x2, self.y2,
        window = self.entryname)

    def recordaux():
        print("Date : " + time.strftime("%d/%m/%Y"))
        print("Nom du patient : ", ntry_txt.get())
        with open('./auxequip/doc_equip/auxiliary1.txt', 'a+') as fintro:
            fintro.write("----------------------------------------------------------\n")
            fintro.write("Date : ")
            fintro.write(time.strftime("%d/%m/%Y")+ '\n')
            fintro.write("Patient name : ")
            fintro.write(ntry_txt.get() + '\n')

        with open('./auxequip/doc_equip/auxiliary1.txt', 'a+') as endfile:
            endfile.write("---------------------------------------------------------\n")

        print(CheckVar1.get())
        if CheckVar1.get() == 1:
            print("[+] Stick was checked !")
            with open('./auxequip/doc_equip/auxiliary1.txt', 'a+') as sfile:
                sfile.write("# Stick : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("[-] Stick ok, nothing to do")
            
        print(CheckVar2.get())
        if CheckVar2.get() == 1:
            print("[+] Walking Frame (FR) was checked !")
            with open('./auxequip/doc_equip/auxiliary1.txt', 'a+') as wffile:
                wffile.write("# Walking Frame : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("[-] Walking Frame ok, nothing to do")

        print(CheckVar3.get())
        if CheckVar3.get() == 1:
            print("[+] Rollator was checked !")
            with open('./auxequip/doc_equip/auxiliary1.txt', 'a+') as rollfile:
                rollfile.write("# Rollator : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("[-] Rollator ok, nothing to do")
            
        print(CheckVar4.get())
        if CheckVar4.get() == 1:
            print("[+] Wheelchair was checked !")
            with open('./auxequip/doc_equip/auxiliary1.txt', 'a+') as wheelfile:
                wheelfile.write("# Wheelchair : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("[-] Wheelchair ok, nothing to do")

        print(CheckVar5.get())
        if CheckVar5.get() == 1:
            print("[+] Crutches was checked !")
            with open('./auxequip/doc_equip/auxiliary1.txt', 'a+') as crutchfile:
                crutchfile.write("# Crutches was checked : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("[-] Crutches ok, nothing to do")

        print(CheckVar50.get())
        if CheckVar50.get() == 1:
            print("[+] Vein-flon was checked !")
            with open('./auxequip/doc_equip/auxiliary1.txt', 'a+') as veinfile:
                veinfile.write("# Vein-flon : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("[-] Vein-flon ok, nothing to do")

        print(CheckVar60.get())
        if CheckVar60.get() == 1:
            print("[+] Pace-maker was checked !")
            with open('./auxequip/doc_equip/auxiliary1.txt', 'a+') as pacefile:
                pacefile.write("# Pace-maker : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("[-] Pace-maker ok, nothing to do")

        print(CheckVar61.get())
        if CheckVar61.get() == 1:
            print("[+] Holter was checked !")
            with open('./auxequip/doc_equip/auxiliary1.txt', 'a+') as holtfile:
                holtfile.write("# Holter : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("[-] Holter ok, nothing to do")

        print(CheckVar70.get())
        if CheckVar70.get() == 1:
            print("[+] Insulin Pump was checked !")
            with open('./auxequip/doc_equip/auxiliary1.txt', 'a+') as insulinfile:
                insulinfile.write("# Insulin Pump : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("[-] Insulin Pump ok, nothing to do")

        print(CheckVar80.get())
        if CheckVar80.get() == 1:
            print("[+] Morphine Pump was checked !")
            with open('./auxequip/doc_equip/auxiliary1.txt', 'a+') as mofile:
                mofile.write("# Morphine Pump : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("[-] Morphine Pump ok, nothing to do")

        print(CheckVar90.get())
        if CheckVar90.get() == 1:
            print("[+] VAC (escarre) was checked !")
            with open('./auxequip/doc_equip/auxiliary1.txt', 'a+') as vacfile:
                vacfile.write("# VAC (escarre) : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("[-] VAC (escarre) ok, nothing to do")

        print(CheckVar100.get())
        if CheckVar100.get() == 1:
            print("[+] Nasal Cannula was checked !")
            with open('./auxequip/doc_equip/auxiliary1.txt', 'a+') as nasalfile:
                nasalfile.write("# Nasal Cannula : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("[-] Nasal Cannula ok, nothing to do")

        print(CheckVar110.get())
        if CheckVar110.get() == 1:
            print("[+] Eyeglasses was checked !")
            with open('./auxequip/doc_equip/auxiliary1.txt', 'a+') as glassfile:
                glassfile.write("# Eyeglasses : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("[-] Eyeglasses ok, nothing to do")

        print(CheckVar120.get())
        if CheckVar120.get() == 1:
            print("[+] Hearing Aids L was checked !")
            with open('./auxequip/doc_equip/auxiliary1.txt', 'a+') as hearfile:
                hearfile.write("# Hearing Aids L : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("[-] Hearing Aids L ok, nothing to do")

        print(CheckVar121.get())
        if CheckVar121.get() == 1:
            print("[+] Hearing Aids R was checked !")
            with open('./auxequip/doc_equip/auxiliary1.txt', 'a+') as hearightfile:
                hearightfile.write("# Hearing Aids R : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("[-] Hearing Aids R ok, nothing to do")

        print(CheckVar130.get())
        if CheckVar130.get() == 1:
            print("[+] Wound Wick was checked !")
            with open('./auxequip/doc_equip/auxiliary1.txt', 'a+') as wondyfile:
                wondyfile.write("# Wound Wick : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("[-] Wound Wick ok, nothing to do")

        print(CheckVar140.get())
        if CheckVar140.get() == 1:
            print("[+] Pleural Drain was checked !")
            with open('./auxequip/doc_equip/auxiliary1.txt', 'a+') as pleuralfile:
                pleuralfile.write("# Pleural Drain : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("[-] Pleural Drain ok, nothing to do")

        print(CheckVar150.get())
        if CheckVar150.get() == 1:
            print("[+] Redon Drain was checked !")
            with open('./auxequip/doc_equip/auxiliary1.txt', 'a+') as redonfile:
                redonfile.write("# Redon Drain : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("[-] Redon Drain ok, nothing to do")

        print(CheckVar160.get())
        if CheckVar160.get() == 1:
            print("[+] Kher Drain was checked !")
            with open('./auxequip/doc_equip/auxiliary1.txt', 'a+') as kherfile:
                kherfile.write("# Kher Drain : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("[-] Kher Drain ok, nothing to do")

        print(CheckVar170.get())
        if CheckVar170.get() == 1:
            print("[+] Blake Drain was checked !")
            with open('./auxequip/doc_equip/auxiliary1.txt', 'a+') as blakefile:
                blakefile.write("# Blake Drain : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("[-] Blake Drain ok, nothing to do")

        print(CheckVar180.get())
        if CheckVar180.get() == 1:
            print("[+] Penrose Drain was checked !")
            with open('./auxequip/doc_equip/auxiliary1.txt', 'a+') as penrosefile:
                penrosefile.write("# Penrose Drain : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("[-] Penrose Drain ok, nothing to do")

        print(CheckVar190.get())
        if CheckVar190.get() == 1:
            print("[+] Mikulicz Drain was checked !")
            with open('./auxequip/doc_equip/auxiliary1.txt', 'a+') as mikufile:
                mikufile.write("# Mikulicz Drain : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("[-] Mikulicz Drain ok, nothing to do")

        print(CheckVar200.get())
        if CheckVar200.get() == 1:
            print("[+] VP Shunt was checked !")
            with open('./auxequip/doc_equip/auxiliary1.txt', 'a+') as vpfile:
                vpfile.write("# VP Shunt : " + \
                    time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("[-] VP Shunt ok, nothing to do")

        print(CheckVar210.get())
        if CheckVar210.get() == 1:
            print("[+] VA Shunt was checked !")
            with open('./auxequip/doc_equip/auxiliary1.txt', 'a+') as vafile:
                vafile.write("# VA Shunt : " + \
                    time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("[-] VA Shunt ok, nothing to do")

        print(CheckVar220.get())
        if CheckVar220.get() == 1:
            print("[+] Total Hip L was checked !")
            with open('./auxequip/doc_equip/auxiliary1.txt', 'a+') as lhipfile:
                lhipfile.write("# Total Hip L : " + \
                    time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("[-] Total Hip L ok, nothing to do")

        print(CheckVar230.get())
        if CheckVar230.get() == 1:
            print("[+] Total Hip R was checked !")
            with open('./auxequip/doc_equip/auxiliary1.txt', 'a+') as rhipfile:
                rhipfile.write("# Total Hip R : " + \
                    time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("[-] Total Hip R ok, nothing to do")

        print(CheckVar240.get())
        if CheckVar240.get() == 1:
            print("[+] Total Knee L was checked !")
            with open('./auxequip/doc_equip/auxiliary1.txt', 'a+') as lkneefile:
                lkneefile.write("# Total Knee L : " + \
                    time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("[-] Total Knee L ok, nothing to do")

        print(CheckVar250.get())
        if CheckVar250.get() == 1:
            print("[+] Total Knee R was checked !")
            with open('./auxequip/doc_equip/auxiliary1.txt', 'a+') as rkneefile:
                rkneefile.write("# Total Knee R : " + \
                    time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("[-] Total Knee R ok, nothing to do")

        print(CheckVar260.get())
        if CheckVar260.get() == 1:
            print("[+] Shoulder Prosthesis L was checked !")
            with open('./auxequip/doc_equip/auxiliary1.txt', 'a+') as shouldfile:
                shouldfile.write("# Shoulder Prosthesis L : " + \
                    time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("[-] Shoulder Prosthesis L ok, nothing to do")

        print(CheckVar270.get())
        if CheckVar270.get() == 1:
            print("[+] Shoulder Prosthesis R was checked !")
            with open('./auxequip/doc_equip/auxiliary1.txt', 'a+') as rshouldfile:
                rshouldfile.write("# Shoulder Prosthesis R : " + \
                    time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("[-] Shoulder Prosthesis R ok, nothing to do")

        print(CheckVar280.get())
        if CheckVar280.get() == 1:
            print("[+] Total Elbow L was checked !")
            with open('./auxequip/doc_equip/auxiliary1.txt', 'a+') as lelbfile:
                lelbfile.write("# Total Elbow L : " + \
                    time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("[-] Total Elbow L ok, nothing to do")

        print(CheckVar290.get())
        if CheckVar290.get() == 1:
            print("[+] Total Elbow R was checked !")
            with open('./auxequip/doc_equip/auxiliary1.txt', 'a+') as relbfile:
                relbfile.write("# Total Elbow R : " + \
                    time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("[-] Total Elbow R ok, nothing to do")

        print(CheckVar300.get())
        if CheckVar300.get() == 1:
            print("[+] Foot Prosthesis L was checked !")
            with open('./auxequip/doc_equip/auxiliary1.txt', 'a+') as lfootfile:
                lfootfile.write("# Foot Prosthesis L : " + \
                    time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("[-] Foot Prosthesis L ok, nothing to do")

        print(CheckVar310.get())
        if CheckVar310.get() == 1:
            print("[+] Foot Prosthesis R was checked !")
            with open('./auxequip/doc_equip/auxiliary1.txt', 'a+') as rfootfile:
                rfootfile.write("# Foot Prosthesis R : " + \
                    time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("[-] Foot Prosthesis R ok, nothing to do")

        print(CheckVar320.get())
        if CheckVar320.get() == 1:
            print("[+] Leg prosthesis L was checked !")
            with open('./auxequip/doc_equip/auxiliary1.txt', 'a+') as llegfile:
                llegfile.write("# Leg prosthesis L : " + \
                    time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("[-] Leg prosthesis L ok, nothing to do")

        print(CheckVar330.get())
        if CheckVar330.get() == 1:
            print("[+] Leg prosthesis R was checked !")
            with open('./auxequip/doc_equip/auxiliary1.txt', 'a+') as rlegfile:
                rlegfile.write("# Leg prosthesis R : " + \
                    time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("[-] Leg prosthesis R ok, nothing to do")

        print(CheckVar340.get())
        if CheckVar340.get() == 1:
            print("[+] Hand Prosthesis L was checked !")
            with open('./auxequip/doc_equip/auxiliary1.txt', 'a+') as lhandfile:
                lhandfile.write("# Hand Prosthesis L : " + \
                    time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("[-] Hand Prosthesis L ok, nothing to do")

        print(CheckVar350.get())
        if CheckVar350.get() == 1:
            print("[+] Hand Prosthesis R was checked !")
            with open('./auxequip/doc_equip/auxiliary1.txt', 'a+') as rhandfile:
                rhandfile.write("# Hand Prosthesis R : " + \
                    time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("[-] Hand Prosthesis R ok, nothing to do")

        print(CheckVar360.get())
        if CheckVar360.get() == 1:
            print("[+] Upper Arm Prosth. L was checked !")
            with open('./auxequip/doc_equip/auxiliary1.txt', 'a+') as larmfile:
                larmfile.write("# Upper Arm Prosth. L : " + \
                    time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("[-] Upper Arm Prosth. L ok, nothing to do")

        print(CheckVar370.get())
        if CheckVar370.get() == 1:
            print("[+] Upper Arm Prosth. R was checked !")
            with open('./auxequip/doc_equip/auxiliary1.txt', 'a+') as rarmfile:
                rarmfile.write("# Upper Arm Prosth. R : " + \
                    time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("[-] Upper Arm Prosth. R ok, nothing to do")

        print(CheckVar380.get())
        if CheckVar380.get() == 1:
            print("[+] Ocular Prosthesis L was checked !")
            with open('./auxequip/doc_equip/auxiliary1.txt', 'a+') as locularfile:
                locularfile.write("# Ocular Prosthesis L : " + \
                    time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("[-] Ocular Prosthesis L ok, nothing to do")

        print(CheckVar390.get())
        if CheckVar390.get() == 1:
            print("[+] Ocular Prosthesis R was checked !")
            with open('./auxequip/doc_equip/auxiliary1.txt', 'a+') as rocularfile:
                rocularfile.write("# Ocular Prosthesis R : " + \
                    time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("[-] Ocular Prosthesis R ok, nothing to do")

        print(CheckVar400.get())
        if CheckVar400.get() == 1:
            print("[+] Shoe Sole L was checked !")
            with open('./auxequip/doc_equip/auxiliary1.txt', 'a+') as lsemfile:
                lsemfile.write("# Shoe Sole L : " + \
                    time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("[-] Shoe Sole L ok, nothing to do")

        print(CheckVar410.get())
        if CheckVar410.get() == 1:
            print("[+] Shoe Sole R was checked !")
            with open('./auxequip/doc_equip/auxiliary1.txt', 'a+') as rsemfile:
                rsemfile.write("# Shoe Sole R : " + \
                    time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("[-] Shoe Sole R ok, nothing to do")

        print(CheckVar420.get())
        if CheckVar420.get() == 1:
            print("[+] Lower Dental Prosth. was checked !")
            with open('./auxequip/doc_equip/auxiliary1.txt', 'a+') as ldentalfile:
                ldentalfile.write("# Lower Dental Prosth. : " + \
                    time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("[-] Lower Dental Prosth. ok, nothing to do")

        print(CheckVar430.get())
        if CheckVar430.get() == 1:
            print("[+] Upper Dental Prosth. was checked !")
            with open('./auxequip/doc_equip/auxiliary1.txt', 'a+') as udentalfile:
                udentalfile.write("# Upper Dental Prosth. : " + \
                    time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("[-] Upper Dental Prosth. ok, nothing to do")

        print(CheckVar440.get())
        if CheckVar440.get() == 1:
            print("[+] Maxilofacial Prosthetics was checked !")
            with open('./auxequip/doc_equip/auxiliary1.txt', 'a+') as maxilofile:
                maxilofile.write("# Maxilofacial Prosthetics : " + \
                    time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("[-] Maxilofacial Prosthetics ok, nothing to do")

        print(CheckVar450.get())
        if CheckVar450.get() == 1:
            print("[+] Nose Prosthesis was checked !")
            with open('./auxequip/doc_equip/auxiliary1.txt', 'a+') as nasaprotfile:
                nasaprotfile.write("# Nose Prosthesis : " + \
                    time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("[-] Nose Prosthesis ok, nothing to do")

    def uploadaux():
        """
            To upload data on server after creating files
        """
        proc = subprocess.run(["scp", "./auxequip/doc_equip/auxiliary1.txt",
            "pi@192.168.18.12:~/tt_doc/doc_txt1/Files1/auxiliary1.txt"],
            stderr=subprocess.PIPE)
        print("Result SCP transfert : %s" % repr(proc.stderr))
        if proc.stderr == b'':
            print("[+] File auxiliary1.txt uploaded !")
            tk.messagebox.showinfo("INFO", "auxiliary1.txt uploaded...")
        else:
            print("[!] No file to upload !")
            tk.messagebox.showerror("Error", "No auxiliary1.txt to upload...")

    def msgrec():
        tk.messagebox.showinfo("Confirmation", "Record confirmed and finished !")

    def transwritedata():
        MsgBox = tk.messagebox.askyesno('Record', 'Results will be saved, ok ?')
        if MsgBox == 1:
            recordaux()
            uploadaux()
            msgrec()
            self.showPatients()
        else:
            tk.messagebox.showinfo('Return', 'Ok, nothing has changed...')

    def wayout():
        try:
            self.effacer()
            self.showPatients()
        except (OSError, ValueError) as p_out:
            print("Error from labo to way out", p_out)

    self.x30, self.y30 = 200, 120
    self.labl_mob = tk.Label(self.can, text='--- Mobilisation ---',
        font="Times 14 bold", width=21,
        height=1, bg='RoyalBlue3', fg='white')
    self.labl_mob = self.can.create_window(self.x30, self.y30,
        window = self.labl_mob)

    self.x40, self.y40 = 200, 145
    CheckVar1 = tk.IntVar()
    self.C1 = tk.Checkbutton(self.can, text="Stick", fg='navy',
        bg='cyan', variable=CheckVar1,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C1 = self.can.create_window(self.x40, self.y40,
        window = self.C1)

    self.x50, self.y50 = 200, 167
    CheckVar2 = tk.IntVar()
    self.C2 = tk.Checkbutton(self.can, text="Walking Frame", fg='navy',
        bg='cyan', variable=CheckVar2,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C2 = self.can.create_window(self.x50, self.y50,
        window = self.C2)

    self.x60, self.y60 = 200, 189
    CheckVar3 = tk.IntVar()
    self.C3 = tk.Checkbutton(self.can, text="Rollator", fg='navy',
        bg='cyan', variable=CheckVar3,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C3 = self.can.create_window(self.x60, self.y60,
        window = self.C3)

    self.x70, self.y70 = 200, 211
    CheckVar4 = tk.IntVar()
    self.C4 = tk.Checkbutton(self.can, text="Wheelchair", fg='navy',
        bg='cyan', variable=CheckVar4,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C4 = self.can.create_window(self.x70, self.y70,
        window = self.C4)

    self.x71, self.y71 = 200, 233
    CheckVar5 = tk.IntVar()
    self.C5 = tk.Checkbutton(self.can, text="Crutches", fg='navy',
        bg='cyan', variable=CheckVar5,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C5 = self.can.create_window(self.x71, self.y71,
        window = self.C5)

    self.x80, self.y80 = 200, 350
    self.labl_appa = tk.Label(self.can, text='--- Appareillage ---',
        font="Times 14 bold", width=21,
        height=1, bg='RoyalBlue3', fg='white')
    self.labl_appa = self.can.create_window(self.x80, self.y80,
        window = self.labl_appa)

    self.x90, self.y90 = 200, 375
    CheckVar50 = tk.IntVar()
    self.C50 = tk.Checkbutton(self.can, text="Vein-flon", fg='navy',
        bg='cyan', variable=CheckVar50,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C50 = self.can.create_window(self.x90, self.y90,
        window = self.C50)

    self.x100, self.y100 = 200, 397
    CheckVar60 = tk.IntVar()
    self.C60 = tk.Checkbutton(self.can, text="Pace-maker", fg='navy',
        bg='cyan', variable=CheckVar60,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C60 = self.can.create_window(self.x100, self.y100,
        window = self.C60)

    self.x101, self.y101 = 200, 419
    CheckVar61 = tk.IntVar()
    self.C61 = tk.Checkbutton(self.can, text="Holter", fg='navy',
        bg='cyan', variable=CheckVar61,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C61 = self.can.create_window(self.x101, self.y101,
        window = self.C61)

    self.x110, self.y110 = 200, 441
    CheckVar70 = tk.IntVar()
    self.C70 = tk.Checkbutton(self.can, text="Insulin Pump", fg='navy',
        bg='cyan', variable=CheckVar70,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C70 = self.can.create_window(self.x110, self.y110,
        window = self.C70)

    self.x120, self.y120 = 200, 463
    CheckVar80 = tk.IntVar()
    self.C80 = tk.Checkbutton(self.can, text="Morphine Pump", fg='navy',
        bg='cyan', variable=CheckVar80,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C80 = self.can.create_window(self.x120, self.y120,
        window = self.C80)

    self.x130, self.y130 = 200, 485
    CheckVar90 = tk.IntVar()
    self.C90 = tk.Checkbutton(self.can, text="VAC (escarre)", fg='navy',
        bg='cyan', variable=CheckVar90,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C90 = self.can.create_window(self.x130, self.y130,
        window = self.C90)

    self.x140, self.y140 = 200, 507
    CheckVar100 = tk.IntVar()
    self.C100 = tk.Checkbutton(self.can, text="Nasal Cannula", fg='navy',
        bg='cyan', variable=CheckVar100,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C100 = self.can.create_window(self.x140, self.y140,
        window = self.C100)

    self.x150, self.y150 = 200, 529
    CheckVar110 = tk.IntVar()
    self.C110 = tk.Checkbutton(self.can, text="Eyeglasses", fg='navy',
        bg='cyan', variable=CheckVar110,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C110 = self.can.create_window(self.x150, self.y150,
        window = self.C110)

    self.x160, self.y160 = 200, 551
    CheckVar120 = tk.IntVar()
    self.C120 = tk.Checkbutton(self.can, text="Hearing Aids L", fg='navy',
        bg='cyan', variable=CheckVar120,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C120 = self.can.create_window(self.x160, self.y160,
        window = self.C120)

    self.x161, self.y161 = 200, 573
    CheckVar121 = tk.IntVar()
    self.C121 = tk.Checkbutton(self.can, text="Hearing Aids R", fg='navy',
        bg='cyan', variable=CheckVar121,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C121 = self.can.create_window(self.x161, self.y161,
        window = self.C121)

    self.x170, self.y170 = 800, 120
    self.labl_appa = tk.Label(self.can, text='--- Catheters and Drains ---',
        font="Times 14 bold", width=65,
        height=1, bg='RoyalBlue3', fg='white')
    self.labl_appa = self.can.create_window(self.x170, self.y170,
        window = self.labl_appa)

    self.x180, self.y180 = 600, 145
    CheckVar130 = tk.IntVar()
    self.C130 = tk.Checkbutton(self.can, text="Wound Wick", fg='navy',
        bg='cyan', variable=CheckVar130,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C130 = self.can.create_window(self.x180, self.y180,
        window = self.C130)

    self.x190, self.y190 = 600, 167
    CheckVar140 = tk.IntVar()
    self.C140 = tk.Checkbutton(self.can, text="Pleural Drain", fg='navy',
        bg='cyan', variable=CheckVar140,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C140 = self.can.create_window(self.x190, self.y190,
        window = self.C140)

    self.x200, self.y200 = 600, 189
    CheckVar150 = tk.IntVar()
    self.C150 = tk.Checkbutton(self.can, text="Redon Drain", fg='navy',
        bg='cyan', variable=CheckVar150,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C150 = self.can.create_window(self.x200, self.y200,
        window = self.C150)

    self.x210, self.y210 = 600, 211 # sonde nasogastrique
    CheckVar160 = tk.IntVar()
    self.C160 = tk.Checkbutton(self.can, text="Kher Drain", fg='navy',
        bg='cyan', variable=CheckVar160,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C160 = self.can.create_window(self.x210, self.y210,
        window = self.C160)

    self.x220, self.y220 = 600, 233
    CheckVar170 = tk.IntVar()
    self.C170 = tk.Checkbutton(self.can, text="Blake Drain", fg='navy',
        bg='cyan', variable=CheckVar170,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C170 = self.can.create_window(self.x220, self.y220,
        window = self.C170)

    self.x230, self.y230 = 600, 255
    CheckVar180 = tk.IntVar()
    self.C180 = tk.Checkbutton(self.can, text="Penrose Drain", fg='navy',
        bg='cyan', variable=CheckVar180,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C180 = self.can.create_window(self.x230, self.y230,
        window = self.C180)

    self.x240, self.y240 = 600, 277
    CheckVar190 = tk.IntVar()
    self.C190 = tk.Checkbutton(self.can, text="Mikulicz Drain", fg='navy',
        bg='cyan', variable=CheckVar190,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C190 = self.can.create_window(self.x240, self.y240,
        window = self.C190)

    self.x250, self.y250 = 1000, 145
    CheckVar200 = tk.IntVar()
    self.C200 = tk.Checkbutton(self.can, text="VP Shunt", fg='navy',
        bg='cyan', variable=CheckVar200,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C200 = self.can.create_window(self.x250, self.y250,
        window = self.C200)

    self.x260, self.y260 = 1000, 167
    CheckVar210 = tk.IntVar()
    self.C210 = tk.Checkbutton(self.can, text="VA Shunt", fg='navy',
        bg='cyan', variable=CheckVar210,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C210 = self.can.create_window(self.x260, self.y260,
        window = self.C210)

    self.x270, self.y270 = 800, 350
    self.labl_proth = tk.Label(self.can, text='--- Prothesis ---',
        font="Times 14 bold", width=65,
        height=1, bg='RoyalBlue3', fg='white')
    self.labl_proth = self.can.create_window(self.x270, self.y270,
        window = self.labl_proth)

    self.x280, self.y280 = 600, 375
    CheckVar220 = tk.IntVar()
    self.C220 = tk.Checkbutton(self.can, text="Total Hip L", fg='navy',
        bg='cyan', variable=CheckVar220,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C220 = self.can.create_window(self.x280, self.y280,
        window = self.C220)

    self.x290, self.y290 = 600, 397
    CheckVar230 = tk.IntVar()
    self.C230 = tk.Checkbutton(self.can, text="Total Hip R", fg='navy',
        bg='cyan', variable=CheckVar230,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C230 = self.can.create_window(self.x290, self.y290,
        window = self.C230)

    self.x300, self.y300 = 600, 419
    CheckVar240 = tk.IntVar()
    self.C240 = tk.Checkbutton(self.can, text="Total Knee L", fg='navy',
        bg='cyan', variable=CheckVar240,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C240 = self.can.create_window(self.x300, self.y300,
        window = self.C240)

    self.x310, self.y310 = 600, 441
    CheckVar250 = tk.IntVar()
    self.C250 = tk.Checkbutton(self.can, text="Total Knee R", fg='navy',
        bg='cyan', variable=CheckVar250,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C250 = self.can.create_window(self.x310, self.y310,
        window = self.C250)

    self.x320, self.y320 = 600, 485
    CheckVar260 = tk.IntVar()
    self.C260 = tk.Checkbutton(self.can, text="Shoulder Prosthesis L", fg='navy',
        bg='cyan', variable=CheckVar260,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C260 = self.can.create_window(self.x320, self.y320,
        window = self.C260)

    self.x330, self.y330 = 600, 507
    CheckVar270 = tk.IntVar()
    self.C270 = tk.Checkbutton(self.can, text="Shoulder Prosthesis R", fg='navy',
        bg='cyan', variable=CheckVar270,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C270 = self.can.create_window(self.x330, self.y330,
        window = self.C270)

    self.x340, self.y340 = 600, 529
    CheckVar280 = tk.IntVar()
    self.C280 = tk.Checkbutton(self.can, text="Total Elbow L", fg='navy',
        bg='cyan', variable=CheckVar280,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C280 = self.can.create_window(self.x340, self.y340,
        window = self.C280)

    self.x350, self.y350 = 600, 551
    CheckVar290 = tk.IntVar()
    self.C290 = tk.Checkbutton(self.can, text="Total Elbow R", fg='navy',
        bg='cyan', variable=CheckVar290,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C290 = self.can.create_window(self.x350, self.y350,
        window = self.C290)

    self.x360, self.y360 = 1000, 375
    CheckVar300 = tk.IntVar()
    self.C300 = tk.Checkbutton(self.can, text="Foot Prosthesis L", fg='navy',
        bg='cyan', variable=CheckVar300,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C300 = self.can.create_window(self.x360, self.y360,
        window = self.C300)

    self.x370, self.y370 = 1000, 397
    CheckVar310 = tk.IntVar()
    self.C310 = tk.Checkbutton(self.can, text="Foot Prosthesis R", fg='navy',
        bg='cyan', variable=CheckVar310,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C310 = self.can.create_window(self.x370, self.y370,
        window = self.C310)

    self.x380, self.y380 = 1000, 419
    CheckVar320 = tk.IntVar()
    self.C320 = tk.Checkbutton(self.can, text="Leg prosthesis L", fg='navy',
        bg='cyan', variable=CheckVar320,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C320 = self.can.create_window(self.x380, self.y380,
        window = self.C320)

    self.x390, self.y390 = 1000, 441
    CheckVar330 = tk.IntVar()
    self.C330 = tk.Checkbutton(self.can, text="Leg prosthesis R", fg='navy',
        bg='cyan', variable=CheckVar330,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C330 = self.can.create_window(self.x390, self.y390,
        window = self.C330)

    self.x400, self.y400 = 1000, 463
    CheckVar340 = tk.IntVar()
    self.C340 = tk.Checkbutton(self.can, text="Hand Prosthesis L", fg='navy',
        bg='cyan', variable=CheckVar340,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C340 = self.can.create_window(self.x400, self.y400,
        window = self.C340)

    self.x410, self.y410 = 1000, 485
    CheckVar350 = tk.IntVar()
    self.C350 = tk.Checkbutton(self.can, text="Hand Prosthesis R", fg='navy',
        bg='cyan', variable=CheckVar350,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C350 = self.can.create_window(self.x410, self.y410,
        window = self.C350)

    self.x420, self.y420 = 1000, 507
    CheckVar360 = tk.IntVar()
    self.C360 = tk.Checkbutton(self.can, text="Upper Arm Prosth. L", fg='navy',
        bg='cyan', variable=CheckVar360,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C360 = self.can.create_window(self.x420, self.y420,
        window = self.C360)

    self.x430, self.y430 = 1000, 529
    CheckVar370 = tk.IntVar()
    self.C370 = tk.Checkbutton(self.can, text="Upper Arm Prosth. R", fg='navy',
        bg='cyan', variable=CheckVar370,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C370 = self.can.create_window(self.x430, self.y430,
        window = self.C370)

    self.x440, self.y440 = 800, 375
    CheckVar380 = tk.IntVar()
    self.C380 = tk.Checkbutton(self.can, text="Ocular Prosthesis L", fg='navy',
        bg='cyan', variable=CheckVar380,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C380 = self.can.create_window(self.x440, self.y440,
        window = self.C380)

    self.x450, self.y450 = 800, 397
    CheckVar390 = tk.IntVar()
    self.C390 = tk.Checkbutton(self.can, text="Ocular Prosthesis R", fg='navy',
        bg='cyan', variable=CheckVar390,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C390 = self.can.create_window(self.x450, self.y450,
        window = self.C390)

    self.x460, self.y460 = 800, 419
    CheckVar400 = tk.IntVar()
    self.C400 = tk.Checkbutton(self.can, text="Shoe Sole L", fg='navy',
        bg='cyan', variable=CheckVar400,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C400 = self.can.create_window(self.x460, self.y460,
        window = self.C400)

    self.x470, self.y470 = 800, 441
    CheckVar410 = tk.IntVar()
    self.C410 = tk.Checkbutton(self.can, text="Shoe Sole R", fg='navy',
        bg='cyan', variable=CheckVar410,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C410 = self.can.create_window(self.x470, self.y470,
        window = self.C410)

    self.x480, self.y480 = 800, 463
    CheckVar420 = tk.IntVar()
    self.C420 = tk.Checkbutton(self.can, text="Lower Dental Prosth. ", fg='navy',
        bg='cyan', variable=CheckVar420,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C420 = self.can.create_window(self.x480, self.y480,
        window = self.C420)

    self.x490, self.y490 = 800, 485
    CheckVar430 = tk.IntVar()
    self.C430 = tk.Checkbutton(self.can, text="Upper Dental Prosth.", fg='navy',
        bg='cyan', variable=CheckVar430,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C430 = self.can.create_window(self.x490, self.y490,
        window = self.C430)

    self.x500, self.y500 = 800, 507
    CheckVar440 = tk.IntVar()
    self.C440 = tk.Checkbutton(self.can, text="Maxilofacial Prosthetics", fg='navy',
        bg='cyan', variable=CheckVar440,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C440 = self.can.create_window(self.x500, self.y500,
        window = self.C440)

    self.x510, self.y510 = 800, 529
    CheckVar450 = tk.IntVar()
    self.C450 = tk.Checkbutton(self.can, text="Nose Prosthesis", fg='navy',
        bg='cyan', variable=CheckVar450,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor=tk.W)
    self.C450 = self.can.create_window(self.x510, self.y510,
        window = self.C450)

    # Button save and quit
    self.x520, self.y520 = 800, 650
    self.buttonsave = tk.Button(self.can, text="Save", width=10, bd=3,
        fg='yellow', bg='RoyalBlue3', activebackground='pale turquoise',
        highlightbackground='cyan', command=transwritedata)
    self.buttonsave = self.can.create_window(self.x520, self.y520,
        window = self.buttonsave)

    self.x530, self.y530 = 1050, 650
    self.buttonquit = tk.Button(self.can, text='Return to main menu', width=20, bd=3,
        fg='white', bg='RoyalBlue3', activebackground='pale turquoise',
        highlightbackground='cyan', command=wayout)
    self.buttonquit = self.can.create_window(self.x530, self.y530,
        window = self.buttonquit)

    self.can.configure(scrollregion=self.can.bbox(tk.ALL))
    self.can.unbind_all("<Button-4>")
    self.can.unbind_all("<Button-5>")
