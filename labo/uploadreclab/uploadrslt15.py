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


def uploadata15():
    """
        To upload data on server after creating files
    """
    proc = subprocess.run(["scp", "./need/doc_suivi15/patient15_14b.txt",
        "pi@192.168.18.12:~/tt_doc/doc_txt15/Files15/patient15_14b.txt"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[?] (if b'' => No more data to transfert)")
        print("[Upload] File patient15_14b.txt uploaded !")
        #tk.messagebox.showinfo("INFO", "patient15_14b.txt uploaded...")
    else:
        print("[!] No file to upload !")
        tk.messagebox.showerror("Error", "No patient15_14b.txt to upload...")

    secproc = subprocess.run(["scp", "./labo/doc_labo/result15.txt",
        "pi@192.168.18.12:~/tt_doc/doc_txt15/Files15/result15.txt"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[?] (if b'' => No more data to transfert)")
        print("[Upload] File result15.txt uploaded !")
        #tk.messagebox.showinfo("INFO", "result15.txt uploaded...")
    else:
        print("[!] No file to upload !")
        tk.messagebox.showerror("Error", "No result15.txt to upload...")
