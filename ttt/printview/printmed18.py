#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
    Verify if files exist or not, when usr press
    button from ./ttt/patientttX.py script.
    In case, if file doesn't exist a msgbox
    appear to explain that. Otherwise, usr can
    open file to display data and print them.
"""


from tkinter import *
import tkinter as tk
from tkinter import messagebox
import os
import sys
import subprocess
import platform
import json


def systemTreat():
    """
        Choose platform for calling report_ttt.txt.
    """
    ttt_pview = platform.system()
    print(ttt_pview)

    if ttt_pview == 'Linux':
        os.system('gio open "./ttt/doc_ttt18/report_ttt.txt"') # Linux
    elif ttt_pview == 'Darwin':
        subprocess.call('open', './ttt/doc_ttt18/report_ttt.txt') # Mac
    else:
        os.startfile('./ttt/doc_ttt18/report_ttt.txt') # Windows

def tttPrint():
    """
        Usr can print and view file report_ttt.txt.
    """
    if os.path.exists('./ttt/doc_ttt18/report_ttt.txt'):
        print("[+] File 'report_ttt.txt' exist (18)!")
        systemTreat()
    else:
        #raise Exception("[!!!] Reach report_ttt.txt failed [!!!]")
        messagebox.showerror('Error', 'File report_ttt.txt does not exist (18)!')

def tttviewnprint():
    """
        Read convdose.json and write report_ttt.txt
        with Treatments as title.
        Call tttPrint() to verify if file exist.
    """
    try:
        if os.path.getsize('./ttt/doc_ttt18/convdose.json'):
            print("[+] File 'convdose' exist (18)!")
            with open('./ttt/doc_ttt18/convdose.json', 'r') as datatttf:
                datastore = json.load(datatttf)
            with open('./ttt/doc_ttt18/report_ttt.txt', 'w') as datatttf2:
                datatttf2.write(str("Treatments :"))
                json.dump(datastore['data'][0:15], datatttf2, indent=4, ensure_ascii=False)
            tttPrint()
    except FileNotFoundError as fnf_convdose:
        print('[!] Sorry, file convdose.json does not exist (18)!', fnf_convdose)
        messagebox.showerror('Error', 'File convdose.json does not exist (18)!')

def systemRes():
    """
        Choose platform for calling report_res.txt.
    """
    res_pview = platform.system()
    print(res_pview)

    if res_pview == 'Linux':
        os.system('gio open "./ttt/doc_ttt18/report_res.txt"') # Linux
    elif res_pview == 'Darwin':
        subprocess.call('open', './ttt/doc_ttt18/report_res.txt') # Mac
    else:
        os.startfile('./ttt/doc_ttt18/report_res.txt') # Windows

def resPrint():
    """
        Usr can print and view file report_res.txt.
    """
    if os.path.exists('./ttt/doc_ttt18/report_res.txt'):
        print("[+] File 'report_res.txt' exist (18)!")
        systemRes()
    else:
        #raise Exception("[!!!] Reach report_res.txt failed [!!!]")
        messagebox.showerror('Error', 'File report_res.txt does not exist (18)!')

def resviewnprint():
    """
        Read convres.json and write report_res.txt
        with Treatments as title.
        Call resPrint() to verify if file exist.
    """
    try:
        if os.path.getsize('./ttt/doc_ttt18/convres.json'):
            print("[+] File 'convres' exist (18)!")
            with open('./ttt/doc_ttt18/convres.json', 'r') as datafile:
                dataresort = json.load(datafile)
            with open('./ttt/doc_ttt18/report_res.txt', 'w') as datafile2:
                datafile2.write(str("Reserves :"))
                json.dump(dataresort['data'][0:9], datafile2, indent=4, ensure_ascii=False)
            resPrint()
    except FileNotFoundError as fnf_convres:
        print('[!] Sorry, file convres.json does not exist (18)!', fnf_convres)
        messagebox.showerror('Error', 'File convres.json does not exist (18)!')

def systemStopttt():
    """
        Choose platform for calling intro_ts.txt.
    """
    stp_tpview = platform.system()
    print(stp_tpview)

    if stp_tpview == 'Linux':
        os.system('gio open "./ttt/doc_ttt18/intro_ts.txt"') # Linux
    elif stp_tpview == 'Darwin':
        subprocess.call('open', './ttt/doc_ttt18/intro_ts.txt') # Mac
    else:
        os.startfile('./ttt/doc_ttt18/intro_ts.txt') # Windows

def ttt_stpview():
    """
        Usr can print and view file intro_ts.txt.
    """
    if os.path.exists('./ttt/doc_ttt18/intro_ts.txt'):
        print("[+] File 'intro_ts.txt' exist (18)!")
        systemStopttt()
    else:
        #raise Exception("[!!!] Reach intro_ts.txt failed [!!!]")
        messagebox.showerror("Error", "File 'intro_ts.txt' does not exist (18)!")

def systemStopRes():
    """
        Choose platform for calling ires_rs.txt.
    """
    stp_respview = platform.system()
    print(stp_respview)

    if stp_respview == 'Linux':
        os.system('gio open "./ttt/doc_ttt18/ires_rs.txt"') # Linux
    elif stp_respview == 'Darwin':
        subprocess.call('open', './ttt/doc_ttt18/ires_rs.txt') # Mac
    else:
        os.startfile('./ttt/doc_ttt18/ires_rs.txt') # Windows

def res_stpview():
    """
        Usr can print and view file ires_rs.txt.
    """
    if os.path.exists('./ttt/doc_ttt18/ires_rs.txt'):
        print("[+] File 'ires_rs.txt' exist (18)!")
        systemStopRes()
    else:
        #raise Exception("[!!!] Reach ires_rs.txt failed [!!!]")
        messagebox.showerror("Error", "File 'ires_rs.txt' does not exist (18)!")
