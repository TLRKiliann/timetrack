#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
    Verify if files exist or not, when usr press
    button from ./ttt/patientttX.py script.
    In case, if file doesn't exist a msgbox
    appear to explain that.
"""


from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os
import subprocess


def tttTabs():
    """
        Display msgbox if there isn't convdose.json file.
    """
    messagebox.showerror("Error", "No TREATMENT recorded for "\
        "this patient, convdose.json file missing (5)!")

def showTreat():
    """
        Verify if convdose.json file exist and call
        tabs.py in this case. Otherwise, msgbox
        will be call by tttTabs() function.
    """
    try:
        if os.path.getsize('./ttt/doc_ttt5/convdose.json'):
            subprocess.run('./ttt/doc_ttt5/tabs.py')
    except FileNotFoundError as no_tabtreat:
        print("[!] Sorry, it's not possible to show tab of ttt, "\
            "convdose.json file missing !", no_tabtreat)
        tttTabs()

def noReservStory():
    """
        Display msgbox if there isn't convres.json file.
    """
    messagebox.showerror("Error", "No RESERVE recorded for "\
        "this patient, convres.json file missing (5)!")

def showReserve():
    """
        Verify if convres.json file exist and call
        tabres.py in this case. Otherwise, msgbox
        will be call by noReservStory() function.
    """
    try:
        if os.path.getsize('./ttt/doc_ttt5/convres.json'):
            subprocess.run('./ttt/doc_ttt5/tabres.py')
    except FileNotFoundError as no_tabres:
        print("[!] Sorry, it's not possible to show tab of "\
            "reserve, convres.json file missing !", no_tabres)
        noReservStory()

def introStoryTreat():
    """
        Display msgbox if there isn't intro_ttt.txt file.
    """
    messagebox.showerror("Error", "None stopped TREATMENT is "\
        "available, maybe no TREATMENT has been introduced (5)!")

def readTttStory():
    """
        Verify if intro_ttt.txt file exist and call
        readstory_ttt.py in this case. Otherwise, msgbox
        will be call by introStoryTreat() function.
    """
    try:
        if os.path.getsize("./ttt/doc_ttt5/intro_ttt.txt"):
            subprocess.run("./ttt/doc_ttt5/readstory_ttt.py")
    except FileNotFoundError as err_storyttt:
        print("[!] Sorry, it's not possible to show tab of ttt, "\
            "no TREATMENT have been stopped !", err_storyttt)
        introStoryTreat()

def introResStory():
    """
        Display msgbox if intro_res.txt file not found.
    """
    messagebox.showerror("Error", "None stopped RESERVE is "\
        "available, maybe no RESERVE has been introduced (5)!")

def readResStory():
    """
        Verify if intro_res.txt file exist and call
        readstory_res.py in this case. Otherwise, msgbox
        will be call by introResStory() function.
    """
    try:
        if os.path.getsize("./ttt/doc_ttt5/intro_res.txt"):
            subprocess.run("./ttt/doc_ttt5/readstory_res.py")
    except FileNotFoundError as err_restory:
        print("[!] Sorry, it's not possible to show tab of RESERVE, "\
            "maybe no RESERVE have been stopped !", err_restory)
        introResStory()

def readFileStory():
    """
        Verify if stopped_ttt.txt file exist and call
        readstory.py in this case. Otherwise, msgbox
        will be call by noHistory() function.
    """
    try:
        if os.path.getsize("./ttt/doc_ttt5/stopped_ttt.txt"):
            subprocess.run("./ttt/doc_ttt5/readstory.py")
    except FileNotFoundError as no_storyfile:
        print("[!] Sorry, none stopped ttt is available, "\
        "maybe no ttt has been introduced (5)!", no_storyfile)
        introStoryTreat()

def noRecStop():
    """
        Display msgbox if ires_rs.txt file not found.
    """
    try:
        if os.path.getsize("./ttt/doc_ttt5/ires_rs.txt"):
            subprocess.run("./ttt/doc_ttt5/stp_readstorymed.py")
    except FileNotFoundError as no_storyrestp:
        print("[!] Sorry, none RESERVE has been stopped (5)!", no_storyrestp)
        messagebox.showerror("Error", "None RESERVE has been stopped (5)!")

def showStopMed():
    """
        Verify if intro_ts.txt file exist and call
        readstory.py in this case. Otherwise, msgbox
        will be call by noRecStop() function.
    """
    try:
        if os.path.getsize("./ttt/doc_ttt5/intro_ts.txt"):
            subprocess.run("./ttt/doc_ttt5/stp_readstorymed.py")
    except FileNotFoundError as no_storyttstp:
        print("[!] Sorry, none TREATMENT has been stopped (5)!", no_storyttstp)
        messagebox.showerror("Error", "None TREATMENT has been stopped (5)!")
        noRecStop()
