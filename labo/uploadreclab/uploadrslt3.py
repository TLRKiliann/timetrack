#!/usr/bin/python3
# -*- coding:utf-8 -*-


"""
    Uploading after recording data int files.
"""


from tkinter import *
import tkinter as tk
from tkinter import messagebox
import os
import subprocess


def uploadata3():
    """
        To upload data on server after creating files
    """
    proc = subprocess.run(["scp", "./need/doc_suivi3/patient3_14b.txt",
        "pi@192.168.18.12:~/tt_doc/doc_txt3/Files3/patient3_14b.txt"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[?] (if b'' => No more data to transfert)")
        print("[Upload] File patient3_14b.txt uploaded !")
        #tk.messagebox.showinfo("INFO", "patient3_14b.txt uploaded...")
    else:
        print("[!] No file to upload !")
        tk.messagebox.showerror("Error", "No patient3_14b.txt to upload...")

    secproc = subprocess.run(["scp", "./labo/doc_labo/result3.txt",
        "pi@192.168.18.12:~/tt_doc/doc_txt3/Files3/result3.txt"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[?] (if b'' => No more data to transfert)")
        print("[Upload] File result3.txt uploaded !")
        #tk.messagebox.showinfo("INFO", "result3.txt uploaded...")
    else:
        print("[!] No file to upload !")
        tk.messagebox.showerror("Error", "No result3.txt to upload...")
