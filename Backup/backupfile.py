#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
    This script make a backup of files of app on your own machine
    in <Backup> directory and in the <old> directory per date for
    which one correspond of xdate_file.json file. A backup is made,
    when you delete patient.
"""


from tkinter import *
from tkinter import messagebox
import time
import json
from Backup.entryback import entryCall
from Backup.allergyback import allergyCall
from Backup.diagback import diagCall
from Backup.paramback import paramCall
from Backup.bmiback import bmiCall
from Backup.kiloback import kiloCall
from Backup.needback import needCall
from Backup.stoptback import stoptCall
from Backup.stoprback import stoprCall
from Backup.introtback import introtCall
from Backup.introrback import introrCall
from Backup.vtttback import viewCallTreat
from Backup.vresback import viewCallRes
from Backup.vmedback import vmedCall


def dataBackToSave(self):
    """
        Make a backup if date corresponding to date
        of today and delete the value of date after backup.
    """
    listeDate = []
    with open("./Backup/xdate_file.json") as file_r:
        listeDate = json.load(file_r)
        for index, value in listeDate.items():
            for x in value:
                print(x)
                if time.strftime("%d/%m/%Y") == x:
                    print("------------------------------")
                    print("> Backup Today : ", x)
                    print("------------------------------")

                    entryCall()
                    allergyCall()
                    diagCall()
                    paramCall()
                    bmiCall()
                    kiloCall()
                    needCall()
                    stoptCall()
                    stoprCall()
                    introtCall()
                    introrCall()
                    viewCallTreat()
                    viewCallRes()
                    vmedCall()

                    x=str(x)
                    value.remove(x)
                    file_w = open("./Backup/xdate_file.json", "w")
                    listeDate = json.dump(listeDate, file_w, indent=4)
                    print("------------------------------")
                    print("--- Backup done ---")
                    print("------------------------------")
                    messagebox.showinfo('INFO', 'BACKUP done !')
                    messagebox.showinfo('INFO', 'Go to Global to read one of them !')
