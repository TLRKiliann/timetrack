#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
    The purpose of this script is to copy
    the data from the aux_X.py script into
    the ../doc_equip/. document.
"""


import tkinter as tk
from tkinter import messagebox
import subprocess
import time


def recordaux(self):
    """
        Data to record from aux_X.py
    """
    print("Date : " + time.strftime("%d/%m/%Y"))
    print("Nom du patient : ", self.ntry_txt.get())
    with open('./auxequip/doc_equip/auxiliary20.txt', 'a+') as fintro:
        fintro.write("----------------------------------------------------------\n")
        fintro.write("Date : ")
        fintro.write(time.strftime("%d/%m/%Y")+ '\n')
        fintro.write("Patient name : ")
        fintro.write(self.ntry_txt.get() + '\n')

    with open('./auxequip/doc_equip/auxiliary20.txt', 'a+') as endfile:
        endfile.write("---------------------------------------------------------\n")

    print(self.CheckVar1.get())
    if self.CheckVar1.get() == 1:
        print("[+] Stick was checked !")
        with open('./auxequip/doc_equip/auxiliary20.txt', 'a+') as sfile:
            sfile.write("# Stick : " + time.strftime("%d/%m/%Y") + " yes\n")
    else:
        print("[-] Stick ok, nothing to do")

    print(self.CheckVar2.get())
    if self.CheckVar2.get() == 1:
        print("[+] Walking Frame (FR) was checked !")
        with open('./auxequip/doc_equip/auxiliary20.txt', 'a+') as wffile:
            wffile.write("# Walking Frame : " + time.strftime("%d/%m/%Y") + " yes\n")
    else:
        print("[-] Walking Frame ok, nothing to do")

    print(self.CheckVar3.get())
    if self.CheckVar3.get() == 1:
        print("[+] Rollator was checked !")
        with open('./auxequip/doc_equip/auxiliary20.txt', 'a+') as rollfile:
            rollfile.write("# Rollator : " + time.strftime("%d/%m/%Y") + " yes\n")
    else:
        print("[-] Rollator ok, nothing to do")

    print(self.CheckVar4.get())
    if self.CheckVar4.get() == 1:
        print("[+] Wheelchair was checked !")
        with open('./auxequip/doc_equip/auxiliary20.txt', 'a+') as wheelfile:
            wheelfile.write("# Wheelchair : " + time.strftime("%d/%m/%Y") + " yes\n")
    else:
        print("[-] Wheelchair ok, nothing to do")

    print(self.CheckVar5.get())
    if self.CheckVar5.get() == 1:
        print("[+] Crutches was checked !")
        with open('./auxequip/doc_equip/auxiliary20.txt', 'a+') as crutchfile:
            crutchfile.write("# Crutches : " + time.strftime("%d/%m/%Y") + " yes\n")
    else:
        print("[-] Crutches ok, nothing to do")

    print(self.CheckVar50.get())
    if self.CheckVar50.get() == 1:
        print("[+] Patch was checked !")
        with open('./auxequip/doc_equip/auxiliary20.txt', 'a+') as patchfile:
            patchfile.write("# Patch : " + time.strftime("%d/%m/%Y") + " yes\n")
    else:
        print("[-] Patch ok, nothing to do")

    print(self.CheckVar60.get())
    if self.CheckVar60.get() == 1:
        print("[+] Pace-maker was checked !")
        with open('./auxequip/doc_equip/auxiliary20.txt', 'a+') as pacefile:
            pacefile.write("# Pace-maker : " + time.strftime("%d/%m/%Y") + " yes\n")
    else:
        print("[-] Pace-maker ok, nothing to do")

    print(self.CheckVar61.get())
    if self.CheckVar61.get() == 1:
        print("[+] Holter was checked !")
        with open('./auxequip/doc_equip/auxiliary20.txt', 'a+') as holtfile:
            holtfile.write("# Holter : " + time.strftime("%d/%m/%Y") + " yes\n")
    else:
        print("[-] Holter ok, nothing to do")

    print(self.CheckVar70.get())
    if self.CheckVar70.get() == 1:
        print("[+] Insulin Pump was checked !")
        with open('./auxequip/doc_equip/auxiliary20.txt', 'a+') as insulinfile:
            insulinfile.write("# Insulin Pump : " + time.strftime("%d/%m/%Y") + " yes\n")
    else:
        print("[-] Insulin Pump ok, nothing to do")

    print(self.CheckVar80.get())
    if self.CheckVar80.get() == 1:
        print("[+] Morphine Pump was checked !")
        with open('./auxequip/doc_equip/auxiliary20.txt', 'a+') as mofile:
            mofile.write("# Morphine Pump : " + time.strftime("%d/%m/%Y") + " yes\n")
    else:
        print("[-] Morphine Pump ok, nothing to do")

    print(self.CheckVar90.get())
    if self.CheckVar90.get() == 1:
        print("[+] VAC (escarre) was checked !")
        with open('./auxequip/doc_equip/auxiliary20.txt', 'a+') as vacfile:
            vacfile.write("# VAC (escarre) : " + time.strftime("%d/%m/%Y") + " yes\n")
    else:
        print("[-] VAC (escarre) ok, nothing to do")

    print(self.CheckVar100.get())
    if self.CheckVar100.get() == 1:
        print("[+] Nasal Cannula was checked !")
        with open('./auxequip/doc_equip/auxiliary20.txt', 'a+') as nasalfile:
            nasalfile.write("# Nasal Cannula : " + time.strftime("%d/%m/%Y") + " yes\n")
    else:
        print("[-] Nasal Cannula ok, nothing to do")

    print(self.CheckVar110.get())
    if self.CheckVar110.get() == 1:
        print("[+] Eyeglasses was checked !")
        with open('./auxequip/doc_equip/auxiliary20.txt', 'a+') as glassfile:
            glassfile.write("# Eyeglasses : " + time.strftime("%d/%m/%Y") + " yes\n")
    else:
        print("[-] Eyeglasses ok, nothing to do")

    print(self.CheckVar120.get())
    if self.CheckVar120.get() == 1:
        print("[+] Hearing Aids L was checked !")
        with open('./auxequip/doc_equip/auxiliary20.txt', 'a+') as hearfile:
            hearfile.write("# Hearing Aids L : " + time.strftime("%d/%m/%Y") + " yes\n")
    else:
        print("[-] Hearing Aids L ok, nothing to do")

    print(self.CheckVar121.get())
    if self.CheckVar121.get() == 1:
        print("[+] Hearing Aids R was checked !")
        with open('./auxequip/doc_equip/auxiliary20.txt', 'a+') as hearightfile:
            hearightfile.write("# Hearing Aids R : " + time.strftime("%d/%m/%Y") + " yes\n")
    else:
        print("[-] Hearing Aids R ok, nothing to do")

    print(self.CheckVar122.get())
    if self.CheckVar122.get() == 1:
        print("[+] Arteriovenous Fistula was checked !")
        with open('./auxequip/doc_equip/auxiliary20.txt', 'a+') as artfistfile:
            artfistfile.write("# Arteriovenous Fistula : " + time.strftime("%d/%m/%Y") + " yes\n")
    else:
        print("[-] Arteriovenous Fistula ok, nothing to do")

    print(self.CheckVar123.get())
    if self.CheckVar123.get() == 1:
        print("[+] Ostomy Bag was checked !")
        with open('./auxequip/doc_equip/auxiliary20.txt', 'a+') as ostofile:
            ostofile.write("# Ostomy Bag : " + time.strftime("%d/%m/%Y") + " yes\n")
    else:
        print("[-] Ostomy Bag ok, nothing to do")

    print(self.CheckVar124.get())
    if self.CheckVar124.get() == 1:
        print("[+] Perfusion was checked !")
        with open('./auxequip/doc_equip/auxiliary20.txt', 'a+') as perfile:
            perfile.write("# Perfusion : " + time.strftime("%d/%m/%Y") + " yes\n")
    else:
        print("[-] Perfusion ok, nothing to do")

    print(self.CheckVar125.get())
    if self.CheckVar125.get() == 1:
        print("[+] Periodical Injection was checked !")
        with open('./auxequip/doc_equip/auxiliary20.txt', 'a+') as injectfile:
            injectfile.write("# Periodical Injection : " + time.strftime("%d/%m/%Y") + " yes\n")
    else:
        print("[-] Periodical Injection ok, nothing to do")

    print(self.CheckVar130.get())
    if self.CheckVar130.get() == 1:
        print("[+] Wound Wick was checked !")
        with open('./auxequip/doc_equip/auxiliary20.txt', 'a+') as wondyfile:
            wondyfile.write("# Wound Wick : " + time.strftime("%d/%m/%Y") + " yes\n")
    else:
        print("[-] Wound Wick ok, nothing to do")

    print(self.CheckVar150.get())
    if self.CheckVar150.get() == 1:
        print("[+] Redon Drain was checked !")
        with open('./auxequip/doc_equip/auxiliary20.txt', 'a+') as redonfile:
            redonfile.write("# Redon Drain : " + time.strftime("%d/%m/%Y") + " yes\n")
    else:
        print("[-] Redon Drain ok, nothing to do")

    print(self.CheckVar160.get())
    if self.CheckVar160.get() == 1:
        print("[+] Kher Drain was checked !")
        with open('./auxequip/doc_equip/auxiliary20.txt', 'a+') as kherfile:
            kherfile.write("# Kher Drain : " + time.strftime("%d/%m/%Y") + " yes\n")
    else:
        print("[-] Kher Drain ok, nothing to do")

    print(self.CheckVar170.get())
    if self.CheckVar170.get() == 1:
        print("[+] Blake Drain was checked !")
        with open('./auxequip/doc_equip/auxiliary20.txt', 'a+') as blakefile:
            blakefile.write("# Blake Drain : " + time.strftime("%d/%m/%Y") + " yes\n")
    else:
        print("[-] Blake Drain ok, nothing to do")

    print(self.CheckVar180.get())
    if self.CheckVar180.get() == 1:
        print("[+] Penrose Drain was checked !")
        with open('./auxequip/doc_equip/auxiliary20.txt', 'a+') as penrosefile:
            penrosefile.write("# Penrose Drain : " + time.strftime("%d/%m/%Y") + " yes\n")
    else:
        print("[-] Penrose Drain ok, nothing to do")

    print(self.CheckVar190.get())
    if self.CheckVar190.get() == 1:
        print("[+] Mikulicz Drain was checked !")
        with open('./auxequip/doc_equip/auxiliary20.txt', 'a+') as mikufile:
            mikufile.write("# Mikulicz Drain : " + time.strftime("%d/%m/%Y") + " yes\n")
    else:
        print("[-] Mikulicz Drain ok, nothing to do")

    print(self.CheckVar191.get())
    if self.CheckVar191.get() == 1:
        print("[+] Dialysis was checked !")
        with open('./auxequip/doc_equip/auxiliary20.txt', 'a+') as diafile:
            diafile.write("# Dialysis : " + \
                time.strftime("%d/%m/%Y") + " yes\n")
    else:
        print("[-] Dialysis ok, nothing to do")

    print(self.CheckVar192.get())
    if self.CheckVar192.get() == 1:
        print("[+] Biliary Drain was checked !")
        with open('./auxequip/doc_equip/auxiliary20.txt', 'a+') as bilifile:
            bilifile.write("# Biliary Drain : " + \
                time.strftime("%d/%m/%Y") + " yes\n")
    else:
        print("[-] Biliary Drain ok, nothing to do")

    print(self.CheckVar193.get())
    if self.CheckVar193.get() == 1:
        print("[+] Urinary Catheter was checked !")
        with open('./auxequip/doc_equip/auxiliary20.txt', 'a+') as urifile:
            urifile.write("# Urinary Catheter : " + \
                time.strftime("%d/%m/%Y") + " yes\n")
    else:
        print("[-] Urinary Catheter ok, nothing to do")

    print(self.CheckVar194.get())
    if self.CheckVar194.get() == 1:
        print("[+] Suprapubic Catheter was checked !")
        with open('./auxequip/doc_equip/auxiliary20.txt', 'a+') as suprafile:
            suprafile.write("# Suprapubic Catheter : " + \
                time.strftime("%d/%m/%Y") + " yes\n")
    else:
        print("[-] Suprapubic Catheter ok, nothing to do")

    print(self.CheckVar195.get())
    if self.CheckVar195.get() == 1:
        print("[+] Pleural Drain was checked !")
        with open('./auxequip/doc_equip/auxiliary20.txt', 'a+') as pleuralfile:
            pleuralfile.write("# Pleural Drain : " + time.strftime("%d/%m/%Y") + " yes\n")
    else:
        print("[-] Pleural Drain ok, nothing to do")

    print(self.CheckVar196.get())
    if self.CheckVar196.get() == 1:
        print("[+] Nasogastric Tube was checked !")
        with open('./auxequip/doc_equip/auxiliary20.txt', 'a+') as nasogafile:
            nasogafile.write("# Nasogastric Tube : " + time.strftime("%d/%m/%Y") + " yes\n")
    else:
        print("[-] Nasogastric Tube ok, nothing to do")

    print(self.CheckVar200.get())
    if self.CheckVar200.get() == 1:
        print("[+] VP Shunt was checked !")
        with open('./auxequip/doc_equip/auxiliary20.txt', 'a+') as vpfile:
            vpfile.write("# VP Shunt : " + \
                time.strftime("%d/%m/%Y") + " yes\n")
    else:
        print("[-] VP Shunt ok, nothing to do")

    print(self.CheckVar210.get())
    if self.CheckVar210.get() == 1:
        print("[+] VA Shunt was checked !")
        with open('./auxequip/doc_equip/auxiliary20.txt', 'a+') as vafile:
            vafile.write("# VA Shunt : " + \
                time.strftime("%d/%m/%Y") + " yes\n")
    else:
        print("[-] VA Shunt ok, nothing to do")

    print(self.CheckVar211.get())
    if self.CheckVar211.get() == 1:
        print("[+] 3-Ways Catheter was checked !")
        with open('./auxequip/doc_equip/auxiliary20.txt', 'a+') as treewayfile:
            treewayfile.write("# 3-Ways Catheter : " + \
                time.strftime("%d/%m/%Y") + " yes\n")
    else:
        print("[-] 3-Ways Catheter ok, nothing to do")

    print(self.CheckVar212.get())
    if self.CheckVar212.get() == 1:
        print("[+] PIC-Line was checked !")
        with open('./auxequip/doc_equip/auxiliary20.txt', 'a+') as picfile:
            picfile.write("# PIC-Line : " + \
                time.strftime("%d/%m/%Y") + " yes\n")
    else:
        print("[-] PIC-Line ok, nothing to do")

    print(self.CheckVar213.get())
    if self.CheckVar213.get() == 1:
        print("[+] Central Catheter was checked !")
        with open('./auxequip/doc_equip/auxiliary20.txt', 'a+') as centralcatf:
            centralcatf.write("# Central Catheter : " + \
                time.strftime("%d/%m/%Y") + " yes\n")
    else:
        print("[-] Central Catheter ok, nothing to do")

    print(self.CheckVar214.get())
    if self.CheckVar214.get() == 1:
        print("[+] Vein-flon was checked !")
        with open('./auxequip/doc_equip/auxiliary20.txt', 'a+') as veinfile:
            veinfile.write("# Vein-flon : " + time.strftime("%d/%m/%Y") + " yes\n")
    else:
        print("[-] Vein-flon ok, nothing to do")

    print(self.CheckVar220.get())
    if self.CheckVar220.get() == 1:
        print("[+] Total Hip L was checked !")
        with open('./auxequip/doc_equip/auxiliary20.txt', 'a+') as lhipfile:
            lhipfile.write("# Total Hip L : " + \
                time.strftime("%d/%m/%Y") + " yes\n")
    else:
        print("[-] Total Hip L ok, nothing to do")

    print(self.CheckVar230.get())
    if self.CheckVar230.get() == 1:
        print("[+] Total Hip R was checked !")
        with open('./auxequip/doc_equip/auxiliary20.txt', 'a+') as rhipfile:
            rhipfile.write("# Total Hip R : " + \
                time.strftime("%d/%m/%Y") + " yes\n")
    else:
        print("[-] Total Hip R ok, nothing to do")

    print(self.CheckVar240.get())
    if self.CheckVar240.get() == 1:
        print("[+] Total Knee L was checked !")
        with open('./auxequip/doc_equip/auxiliary20.txt', 'a+') as lkneefile:
            lkneefile.write("# Total Knee L : " + \
                time.strftime("%d/%m/%Y") + " yes\n")
    else:
        print("[-] Total Knee L ok, nothing to do")

    print(self.CheckVar250.get())
    if self.CheckVar250.get() == 1:
        print("[+] Total Knee R was checked !")
        with open('./auxequip/doc_equip/auxiliary20.txt', 'a+') as rkneefile:
            rkneefile.write("# Total Knee R : " + \
                time.strftime("%d/%m/%Y") + " yes\n")
    else:
        print("[-] Total Knee R ok, nothing to do")

    print(self.CheckVar260.get())
    if self.CheckVar260.get() == 1:
        print("[+] Shoulder Prosthesis L was checked !")
        with open('./auxequip/doc_equip/auxiliary20.txt', 'a+') as shouldfile:
            shouldfile.write("# Shoulder Prosthesis L : " + \
                time.strftime("%d/%m/%Y") + " yes\n")
    else:
        print("[-] Shoulder Prosthesis L ok, nothing to do")

    print(self.CheckVar270.get())
    if self.CheckVar270.get() == 1:
        print("[+] Shoulder Prosthesis R was checked !")
        with open('./auxequip/doc_equip/auxiliary20.txt', 'a+') as rshouldfile:
            rshouldfile.write("# Shoulder Prosthesis R : " + \
                time.strftime("%d/%m/%Y") + " yes\n")
    else:
        print("[-] Shoulder Prosthesis R ok, nothing to do")

    print(self.CheckVar280.get())
    if self.CheckVar280.get() == 1:
        print("[+] Total Elbow L was checked !")
        with open('./auxequip/doc_equip/auxiliary20.txt', 'a+') as lelbfile:
            lelbfile.write("# Total Elbow L : " + \
                time.strftime("%d/%m/%Y") + " yes\n")
    else:
        print("[-] Total Elbow L ok, nothing to do")

    print(self.CheckVar290.get())
    if self.CheckVar290.get() == 1:
        print("[+] Total Elbow R was checked !")
        with open('./auxequip/doc_equip/auxiliary20.txt', 'a+') as relbfile:
            relbfile.write("# Total Elbow R : " + \
                time.strftime("%d/%m/%Y") + " yes\n")
    else:
        print("[-] Total Elbow R ok, nothing to do")

    print(self.CheckVar300.get())
    if self.CheckVar300.get() == 1:
        print("[+] Foot Prosthesis L was checked !")
        with open('./auxequip/doc_equip/auxiliary20.txt', 'a+') as lfootfile:
            lfootfile.write("# Foot Prosthesis L : " + \
                time.strftime("%d/%m/%Y") + " yes\n")
    else:
        print("[-] Foot Prosthesis L ok, nothing to do")

    print(self.CheckVar310.get())
    if self.CheckVar310.get() == 1:
        print("[+] Foot Prosthesis R was checked !")
        with open('./auxequip/doc_equip/auxiliary20.txt', 'a+') as rfootfile:
            rfootfile.write("# Foot Prosthesis R : " + \
                time.strftime("%d/%m/%Y") + " yes\n")
    else:
        print("[-] Foot Prosthesis R ok, nothing to do")

    print(self.CheckVar320.get())
    if self.CheckVar320.get() == 1:
        print("[+] Leg prosthesis L was checked !")
        with open('./auxequip/doc_equip/auxiliary20.txt', 'a+') as llegfile:
            llegfile.write("# Leg prosthesis L : " + \
                time.strftime("%d/%m/%Y") + " yes\n")
    else:
        print("[-] Leg prosthesis L ok, nothing to do")

    print(self.CheckVar330.get())
    if self.CheckVar330.get() == 1:
        print("[+] Leg prosthesis R was checked !")
        with open('./auxequip/doc_equip/auxiliary20.txt', 'a+') as rlegfile:
            rlegfile.write("# Leg prosthesis R : " + \
                time.strftime("%d/%m/%Y") + " yes\n")
    else:
        print("[-] Leg prosthesis R ok, nothing to do")

    print(self.CheckVar340.get())
    if self.CheckVar340.get() == 1:
        print("[+] Hand Prosthesis L was checked !")
        with open('./auxequip/doc_equip/auxiliary20.txt', 'a+') as lhandfile:
            lhandfile.write("# Hand Prosthesis L : " + \
                time.strftime("%d/%m/%Y") + " yes\n")
    else:
        print("[-] Hand Prosthesis L ok, nothing to do")

    print(self.CheckVar350.get())
    if self.CheckVar350.get() == 1:
        print("[+] Hand Prosthesis R was checked !")
        with open('./auxequip/doc_equip/auxiliary20.txt', 'a+') as rhandfile:
            rhandfile.write("# Hand Prosthesis R : " + \
                time.strftime("%d/%m/%Y") + " yes\n")
    else:
        print("[-] Hand Prosthesis R ok, nothing to do")

    print(self.CheckVar360.get())
    if self.CheckVar360.get() == 1:
        print("[+] Upper Arm Prosth. L was checked !")
        with open('./auxequip/doc_equip/auxiliary20.txt', 'a+') as larmfile:
            larmfile.write("# Upper Arm Prosth. L : " + \
                time.strftime("%d/%m/%Y") + " yes\n")
    else:
        print("[-] Upper Arm Prosth. L ok, nothing to do")

    print(self.CheckVar370.get())
    if self.CheckVar370.get() == 1:
        print("[+] Upper Arm Prosth. R was checked !")
        with open('./auxequip/doc_equip/auxiliary20.txt', 'a+') as rarmfile:
            rarmfile.write("# Upper Arm Prosth. R : " + \
                time.strftime("%d/%m/%Y") + " yes\n")
    else:
        print("[-] Upper Arm Prosth. R ok, nothing to do")

    print(self.CheckVar380.get())
    if self.CheckVar380.get() == 1:
        print("[+] Ocular Prosthesis L was checked !")
        with open('./auxequip/doc_equip/auxiliary20.txt', 'a+') as locularfile:
            locularfile.write("# Ocular Prosthesis L : " + \
                time.strftime("%d/%m/%Y") + " yes\n")
    else:
        print("[-] Ocular Prosthesis L ok, nothing to do")

    print(self.CheckVar390.get())
    if self.CheckVar390.get() == 1:
        print("[+] Ocular Prosthesis R was checked !")
        with open('./auxequip/doc_equip/auxiliary20.txt', 'a+') as rocularfile:
            rocularfile.write("# Ocular Prosthesis R : " + \
                time.strftime("%d/%m/%Y") + " yes\n")
    else:
        print("[-] Ocular Prosthesis R ok, nothing to do")

    print(self.CheckVar400.get())
    if self.CheckVar400.get() == 1:
        print("[+] Shoe Sole L was checked !")
        with open('./auxequip/doc_equip/auxiliary20.txt', 'a+') as lsemfile:
            lsemfile.write("# Shoe Sole L : " + \
                time.strftime("%d/%m/%Y") + " yes\n")
    else:
        print("[-] Shoe Sole L ok, nothing to do")

    print(self.CheckVar410.get())
    if self.CheckVar410.get() == 1:
        print("[+] Shoe Sole R was checked !")
        with open('./auxequip/doc_equip/auxiliary20.txt', 'a+') as rsemfile:
            rsemfile.write("# Shoe Sole R : " + \
                time.strftime("%d/%m/%Y") + " yes\n")
    else:
        print("[-] Shoe Sole R ok, nothing to do")

    print(self.CheckVar420.get())
    if self.CheckVar420.get() == 1:
        print("[+] Lower Dental Prosth. was checked !")
        with open('./auxequip/doc_equip/auxiliary20.txt', 'a+') as ldentalfile:
            ldentalfile.write("# Lower Dental Prosth. : " + \
                time.strftime("%d/%m/%Y") + " yes\n")
    else:
        print("[-] Lower Dental Prosth. ok, nothing to do")

    print(self.CheckVar430.get())
    if self.CheckVar430.get() == 1:
        print("[+] Upper Dental Prosth. was checked !")
        with open('./auxequip/doc_equip/auxiliary20.txt', 'a+') as udentalfile:
            udentalfile.write("# Upper Dental Prosth. : " + \
                time.strftime("%d/%m/%Y") + " yes\n")
    else:
        print("[-] Upper Dental Prosth. ok, nothing to do")

    print(self.CheckVar440.get())
    if self.CheckVar440.get() == 1:
        print("[+] Maxilofacial Prosthetics was checked !")
        with open('./auxequip/doc_equip/auxiliary20.txt', 'a+') as maxilofile:
            maxilofile.write("# Maxilofacial Prosthetics : " + \
                time.strftime("%d/%m/%Y") + " yes\n")
    else:
        print("[-] Maxilofacial Prosthetics ok, nothing to do")

    print(self.CheckVar450.get())
    if self.CheckVar450.get() == 1:
        print("[+] Nose Prosthesis was checked !")
        with open('./auxequip/doc_equip/auxiliary20.txt', 'a+') as nasaprotfile:
            nasaprotfile.write("# Nose Prosthesis : " + \
                time.strftime("%d/%m/%Y") + " yes\n")
    else:
        print("[-] Nose Prosthesis ok, nothing to do")

def uploadaux():
    """
        Upload the data once they have been saved in the auxiliary_X.txt file
    """
    procaux = subprocess.run(["scp", "./auxequip/doc_equip/auxiliary20.txt",
        "pi@192.168.18.12:~/tt_doc/doc_txt20/Files20/auxiliary20.txt"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(procaux.stderr))
    if procaux.stderr == b'':
        print("[+] File auxiliary20.txt uploaded !")
        tk.messagebox.showinfo("INFO", "auxiliary20.txt uploaded...")
    else:
        print("[!] No file auxiliary20.txt to upload !")
        tk.messagebox.showerror("Error", "No auxiliary20.txt to upload...")

def msgrec():
    """
        Message confirming that data has been saved.
    """
    tk.messagebox.showinfo("Confirmation", "Record confirmed and finished !")

def transwritedata(self):
    """
        This function allows different saving modes.
        You can use : self.showPatients() at the end
        to return to main menu (patcaps.py)
    """
    MsgBox = tk.messagebox.askyesno('Record', 'Results will be saved, ok ?')
    if MsgBox == 1:
        recordaux(self)
        uploadaux()
        msgrec()
    else:
        tk.messagebox.showinfo('Return', 'Ok, nothing has changed...')
