#!/usr/bin/python3
# -*- coding : utf-8 -*-


"""
    Connecting the duration of progress bar
    with task = number of subprocess.
"""

import tkinter as tk
from tkinter import messagebox
from need.needownload.loadbar import needata
import subprocess



def needload10():
    """
        to download med files from server before
        to start with med interface.
    """
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt10/Files10/main_14b.txt",
        "./need/doc_suivi10/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Download] File main_14b.txt downloaded !")
        #tk.messagebox.showinfo("INFO", "main_14b.txt downloaded !")
    else:
        print("[!] No file to download !")
        tk.messagebox.showerror("Error", "No main_14b.txt to download !")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt3/Files10/patient10_14b.txt",
        "./need/doc_suivi10/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[Download] File patient10_14b.txt downloaded !")
        #tk.messagebox.showinfo("INFO", "patient10_14b.txt downloaded !")
    else:
        print("[!] No file to download !")
        tk.messagebox.showerror("Error", "No patient10_14b.txt to download !")

def needload11():
    """
        to download med files from server before
        to start with med interface.
    """
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt11/Files11/main_14b.txt",
        "./need/doc_suivi11/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Download] File main_14b.txt downloaded !")
        #tk.messagebox.showinfo("INFO", "main_14b.txt downloaded !")
    else:
        print("[!] No file to download !")
        tk.messagebox.showerror("Error", "No main_14b.txt to download !")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt11/Files11/patient11_14b.txt",
        "./need/doc_suivi11/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[Download] File patient11_14b.txt downloaded !")
        #tk.messagebox.showinfo("INFO", "patient11_14b.txt downloaded !")
    else:
        print("[!] No file to download !")
        tk.messagebox.showerror("Error", "No patient11_14b.txt to download !")

def needload12():
    """
        to download med files from server before
        to start with med interface.
    """
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt12/Files12/main_14b.txt",
        "./need/doc_suivi12/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Download] File main_14b.txt downloaded !")
        #tk.messagebox.showinfo("INFO", "main_14b.txt downloaded !")
    else:
        print("[!] No file to download !")
        tk.messagebox.showerror("Error", "No main_14b.txt to download !")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt12/Files12/patient12_14b.txt",
        "./need/doc_suivi12/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[Download] File patient12_14b.txt downloaded !")
        #tk.messagebox.showinfo("INFO", "patient12_14b.txt downloaded !")
    else:
        print("[!] No file to download !")
        tk.messagebox.showerror("Error", "No patient12_14b.txt to download !")

def needload13():
    """
        to download med files from server before
        to start with med interface.
    """
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt13/Files13/main_14b.txt",
        "./need/doc_suivi13/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Download] File main_14b.txt downloaded !")
        #tk.messagebox.showinfo("INFO", "main_14b.txt downloaded !")
    else:
        print("[!] No file to download !")
        tk.messagebox.showerror("Error", "No main_14b.txt to download !")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt13/Files13/patient13_14b.txt",
        "./need/doc_suivi13/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[Download] File patient13_14b.txt downloaded !")
        #tk.messagebox.showinfo("INFO", "patient13_14b.txt downloaded !")
    else:
        print("[!] No file to download !")
        tk.messagebox.showerror("Error", "No patient13_14b.txt to download !")

def needload14():
    """
        to download med files from server before
        to start with med interface.
    """
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt14/Files14/main_14b.txt",
        "./need/doc_suivi14/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Download] File main_14b.txt downloaded !")
        #tk.messagebox.showinfo("INFO", "main_14b.txt downloaded !")
    else:
        print("[!] No file to download !")
        tk.messagebox.showerror("Error", "No main_14b.txt to download !")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt14/Files14/patient14_14b.txt",
        "./need/doc_suivi14/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[Download] File patient14_14b.txt downloaded !")
        #tk.messagebox.showinfo("INFO", "patient14_14b.txt downloaded !")
    else:
        print("[!] No file to download !")
        tk.messagebox.showerror("Error", "No patient14_14b.txt to download !")

def needload15():
    """
        to download med files from server before
        to start with med interface.
    """
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt15/Files15/main_14b.txt",
        "./need/doc_suivi15/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Download] File main_14b.txt downloaded !")
        #tk.messagebox.showinfo("INFO", "main_14b.txt downloaded !")
    else:
        print("[!] No file to download !")
        tk.messagebox.showerror("Error", "No main_14b.txt to download !")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt15/Files15/patient15_14b.txt",
        "./need/doc_suivi15/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[Download] File patient15_14b.txt downloaded !")
        #tk.messagebox.showinfo("INFO", "patient15_14b.txt downloaded !")
    else:
        print("[!] No file to download !")
        tk.messagebox.showerror("Error", "No patient15_14b.txt to download !")

def needload16():
    """
        to download med files from server before
        to start with med interface.
    """
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt16/Files16/main_14b.txt",
        "./need/doc_suivi16/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Download] File main_14b.txt downloaded !")
        #tk.messagebox.showinfo("INFO", "main_14b.txt downloaded !")
    else:
        print("[!] No file to download !")
        tk.messagebox.showerror("Error", "No main_14b.txt to download !")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt16/Files16/patient16_14b.txt",
        "./need/doc_suivi16/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[Download] File patient16_14b.txt downloaded !")
        #tk.messagebox.showinfo("INFO", "patient16_14b.txt downloaded !")
    else:
        print("[!] No file to download !")
        tk.messagebox.showerror("Error", "No patient16_14b.txt to download !")

def needload17():
    """
        to download med files from server before
        to start with med interface.
    """
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt17/Files17/main_14b.txt",
        "./need/doc_suivi17/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Download] File main_14b.txt downloaded !")
        #tk.messagebox.showinfo("INFO", "main_14b.txt downloaded !")
    else:
        print("[!] No file to download !")
        tk.messagebox.showerror("Error", "No main_14b.txt to download !")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt17/Files17/patient17_14b.txt",
        "./need/doc_suivi17/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[Download] File patient17_14b.txt downloaded !")
        #tk.messagebox.showinfo("INFO", "patient17_14b.txt downloaded !")
    else:
        print("[!] No file to download !")
        tk.messagebox.showerror("Error", "No patient17_14b.txt to download !")

def needload18():
    """
        to download med files from server before
        to start with med interface.
    """
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt18/Files18/main_14b.txt",
        "./need/doc_suivi18/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Download] File main_14b.txt downloaded !")
        #tk.messagebox.showinfo("INFO", "main_14b.txt downloaded !")
    else:
        print("[!] No file to download !")
        tk.messagebox.showerror("Error", "No main_14b.txt to download !")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt18/Files18/patient18_14b.txt",
        "./need/doc_suivi18/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[Download] File patient18_14b.txt downloaded !")
        #tk.messagebox.showinfo("INFO", "patient18_14b.txt downloaded !")
    else:
        print("[!] No file to download !")
        tk.messagebox.showerror("Error", "No patient18_14b.txt to download !")

def needload19():
    """
        to download med files from server before
        to start with med interface.
    """
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt19/Files19/main_14b.txt",
        "./need/doc_suivi19/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Download] File main_14b.txt downloaded !")
        #tk.messagebox.showinfo("INFO", "main_14b.txt downloaded !")
    else:
        print("[!] No file to download !")
        tk.messagebox.showerror("Error", "No main_14b.txt to download !")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt19/Files19/patient19_14b.txt",
        "./need/doc_suivi19/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[Download] File patient19_14b.txt downloaded !")
        #tk.messagebox.showinfo("INFO", "patient19_14b.txt downloaded !")
    else:
        print("[!] No file to download !")
        tk.messagebox.showerror("Error", "No patient19_14b.txt to download !")

def needload20():
    """
        to download med files from server before
        to start with med interface.
    """
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt20/Files20/main_14b.txt",
        "./need/doc_suivi20/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Download] File main_14b.txt downloaded !")
        #tk.messagebox.showinfo("INFO", "main_14b.txt downloaded !")
    else:
        print("[!] No file to download !")
        tk.messagebox.showerror("Error", "No main_14b.txt to download !")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt20/Files20/patient20_14b.txt",
        "./need/doc_suivi20/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[Download] File patient20_14b.txt downloaded !")
        #tk.messagebox.showinfo("INFO", "patient20_14b.txt downloaded !")
    else:
        print("[!] No file to download !")
        tk.messagebox.showerror("Error", "No patient20_14b.txt to download !")

def needload21():
    """
        to download med files from server before
        to start with med interface.
    """
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt21/Files21/main_14b.txt",
        "./need/doc_suivi21/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Download] File main_14b.txt downloaded !")
        #tk.messagebox.showinfo("INFO", "main_14b.txt downloaded !")
    else:
        print("[!] No file to download !")
        tk.messagebox.showerror("Error", "No main_14b.txt to download !")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt21/Files21/patient21_14b.txt",
        "./need/doc_suivi21/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[Download] File patient21_14b.txt downloaded !")
        #tk.messagebox.showinfo("INFO", "patient21_14b.txt downloaded !")
    else:
        print("[!] No file to download !")
        tk.messagebox.showerror("Error", "No patient21_14b.txt to download !")

def needload22():
    """
        to download med files from server before
        to start with med interface.
    """
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt22/Files22/main_14b.txt",
        "./need/doc_suivi22/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Download] File main_14b.txt downloaded !")
        #tk.messagebox.showinfo("INFO", "main_14b.txt downloaded !")
    else:
        print("[!] No file to download !")
        tk.messagebox.showerror("Error", "No main_14b.txt to download !")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt22/Files22/patient22_14b.txt",
        "./need/doc_suivi22/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[Download] File patient22_14b.txt downloaded !")
        #tk.messagebox.showinfo("INFO", "patient22_14b.txt downloaded !")
    else:
        print("[!] No file to download !")
        tk.messagebox.showerror("Error", "No patient22_14b.txt to download !")

def needload23():
    """
        to download med files from server before
        to start with med interface.
    """
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt23/Files23/main_14b.txt",
        "./need/doc_suivi23/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Download] File main_14b.txt downloaded !")
        #tk.messagebox.showinfo("INFO", "main_14b.txt downloaded !")
    else:
        print("[!] No file to download !")
        tk.messagebox.showerror("Error", "No main_14b.txt to download !")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt23/Files23/patient23_14b.txt",
        "./need/doc_suivi23/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[Download] File patient23_14b.txt downloaded !")
        #tk.messagebox.showinfo("INFO", "patient23_14b.txt downloaded !")
    else:
        print("[!] No file to download !")
        tk.messagebox.showerror("Error", "No patient23_14b.txt to download !")

def needload24():
    """
        to download med files from server before
        to start with med interface.
    """
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt24/Files24/main_14b.txt",
        "./need/doc_suivi24/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Download] File main_14b.txt downloaded !")
        #tk.messagebox.showinfo("INFO", "main_14b.txt downloaded !")
    else:
        print("[!] No file to download !")
        tk.messagebox.showerror("Error", "No main_14b.txt to download !")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt24/Files24/patient24_14b.txt",
        "./need/doc_suivi24/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[Download] File patient24_14b.txt downloaded !")
        #tk.messagebox.showinfo("INFO", "patient24_14b.txt downloaded !")
    else:
        print("[!] No file to download !")
        tk.messagebox.showerror("Error", "No patient24_14b.txt to download !")
