#!/usr/bin/python3
# -*- coding: utf-8 -*-


from tkinter import *
import tkinter as tk
from tkinter import messagebox
import subprocess


def resupload():
    """
        Launch upload for copying files to server.
    """
    introres_proc = subprocess.run(["scp", "./ttt/doc_ttt16/intro_res.txt",
        "pi@192.168.18.12:~/tt_doc/doc_txt16/Files16/intro_res.txt"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(introres_proc.stderr))
    if introres_proc.stderr == b'':
        print("[Upload] File intro_res.txt uploaded.")
        messagebox.showinfo("INFO", "intro_res.txt uploaded...")
    else:
        print("[!] No file intro_res.txt to upload !")
        messagebox.showerror("Error", "No intro_res.txt to upload !")

    stopres_proc = subprocess.run(["scp", "./ttt/doc_ttt16/stopped_res.txt",
        "pi@192.168.18.12:~/tt_doc/doc_txt16/Files16/stopped_res.txt"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(stopres_proc.stderr))
    if stopres_proc.stderr == b'':
        print("[Upload] File stopped_res.txt uploaded !")
        messagebox.showinfo("INFO", "stopped_res.txt uploaded...")
    else:
        print("[!] No file stopped_res.txt to upload !")
        messagebox.showerror("Error", "No stopped_res.txt to upload...")

    irestp_proc = subprocess.run(["scp", "./ttt/doc_ttt16/ires_rs.txt",
        "pi@192.168.18.12:~/tt_doc/doc_txt16/Files16/ires_rs.txt"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(irestp_proc.stderr))
    if irestp_proc.stderr == b'':
        print("[Upload] File ires_rs.txt uploaded !")
        messagebox.showinfo("INFO", "ires_rs.txt uploaded...")
    else:
        print("[!] No file ires_rs.txt to upload !")
        messagebox.showerror("Error", "No ires_rs.txt to upload...")

    convdose_proc = subprocess.run(["scp", "./ttt/doc_ttt16/convres.json",
        "pi@192.168.18.12:~/tt_doc/doc_txt16/Files16/convres.json"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(convdose_proc.stderr))
    if convdose_proc.stderr == b'':
        print("[Upload] File convres.json uploaded !")
        messagebox.showinfo("INFO", "convres.json uploaded...")
    else:
        print("[!] No file convres.json to upload !")
        messagebox.showerror("Error", "No convres.json to upload...")
