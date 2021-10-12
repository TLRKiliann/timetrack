#!/usr/bin/python3
# -*- coding: utf-8 -*-


from tkinter import *
import tkinter as tk
from tkinter import messagebox
import subprocess


def tttupload():
    """
        Launch upload txt ttt files to server.
    """
    introtttproc = subprocess.run(["scp", "./ttt/doc_ttt20/intro_ttt.txt",
        "pi@192.168.18.12:~/tt_doc/doc_txt20/Files20/intro_ttt.txt"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(introtttproc.stderr))
    if introtttproc.stderr == b'':
        print("[Upload] File intro_ttt.txt uploaded.")
        messagebox.showinfo("INFO", "intro_ttt.txt uploaded...")
    else:
        print("[!] No file intro_ttt.txt to upload !")
        messagebox.showerror("Error", "No intro_ttt.txt to upload !")

    stoptttproc = subprocess.run(["scp", "./ttt/doc_ttt20/stopped_ttt.txt",
        "pi@192.168.18.12:~/tt_doc/doc_txt20/Files20/stopped_ttt.txt"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(stoptttproc.stderr))
    if stoptttproc.stderr == b'':
        print("[Upload] File stopped_ttt.txt uploaded.")
        messagebox.showinfo("INFO", "stopped_ttt.txt uploaded...")
    else:
        print("[!] No file stopped_ttt.txt to upload !")
        messagebox.showerror("Error", "No stopped_ttt.txt to upload !")

    introstp_ts = subprocess.run(["scp", "./ttt/doc_ttt20/intro_ts.txt",
        "pi@192.168.18.12:~/tt_doc/doc_txt20/Files20/intro_ts.txt"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(introstp_ts.stderr))
    if introstp_ts.stderr == b'':
        print("[Upload] File intro_ts.txt uploaded.")
        messagebox.showinfo("INFO", "intro_ts.txt uploaded...")
    else:
        print("[!] No file intro_ts.txt to upload !")
        messagebox.showerror("Error", "No intro_ts.txt to upload !")

    tttproc = subprocess.run(["scp", "./ttt/doc_ttt20/convdose.json",
        "pi@192.168.18.12:~/tt_doc/doc_txt20/Files20/convdose.json"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(tttproc.stderr))
    if tttproc.stderr == b'':
        print("[Upload] File convdose.json uploaded.")
        messagebox.showinfo("INFO", "convdose.json uploaded.")
    else:
        print("[!] No file convdose.json to upload !")
        messagebox.showerror("Error", "No convdose.json to upload !")
