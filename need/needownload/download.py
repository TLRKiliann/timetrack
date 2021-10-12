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


def needload1():
    """
        to download med files from server before
        to start with med interface.
    """
    needata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt1/Files1/main_14b.txt",
        "./need/doc_suivi/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Download] File main_14b.txt downloaded !")
        #tk.messagebox.showinfo("INFO", "main_14b.txt downloaded !")
    else:
        print("[!] No file to download !")
        tk.messagebox.showerror("Error", "No main_14b.txt to download !")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt1/Files1/patient1_14b.txt",
        "./need/doc_suivi/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[Download] File patient1_14b.txt downloaded !")
        #tk.messagebox.showinfo("INFO", "patient1_14b.txt downloaded !")
    else:
        print("[!] No file to download !")
        tk.messagebox.showerror("Error", "No patient1_14b.txt to download !")

def needload2():
    """
        to download med files from server before
        to start with med interface.
    """
    needata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt2/Files2/main_14b.txt",
        "./need/doc_suivi2/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Download] File main_14b.txt downloaded !")
        #tk.messagebox.showinfo("INFO", "main_14b.txt downloaded !")
    else:
        print("[!] No file to download !")
        tk.messagebox.showerror("Error", "No main_14b.txt to download !")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt2/Files2/patient2_14b.txt",
        "./need/doc_suivi2/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[Download] File patient2_14b.txt downloaded !")
        #tk.messagebox.showinfo("INFO", "patient2_14b.txt downloaded !")
    else:
        print("[!] No file to download !")
        tk.messagebox.showerror("Error", "No patient2_14b.txt to download !")

def needload3():
    """
        to download med files from server before
        to start with med interface.
    """
    needata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt3/Files3/main_14b.txt",
        "./need/doc_suivi3/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Download] File main_14b.txt downloaded !")
        #tk.messagebox.showinfo("INFO", "main_14b.txt downloaded !")
    else:
        print("[!] No file to download !")
        tk.messagebox.showerror("Error", "No main_14b.txt to download !")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt3/Files3/patient3_14b.txt",
        "./need/doc_suivi3/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[Download] File patient3_14b.txt downloaded !")
        #tk.messagebox.showinfo("INFO", "patient3_14b.txt downloaded !")
    else:
        print("[!] No file to download !")
        tk.messagebox.showerror("Error", "No patient3_14b.txt to download !")

def needload4():
    """
        to download med files from server before
        to start with med interface.
    """
    needata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt4/Files4/main_14b.txt",
        "./need/doc_suivi4/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Download] File main_14b.txt downloaded !")
        #tk.messagebox.showinfo("INFO", "main_14b.txt downloaded !")
    else:
        print("[!] No file to download !")
        tk.messagebox.showerror("Error", "No main_14b.txt to download !")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt4/Files4/patient4_14b.txt",
        "./need/doc_suivi4/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[Download] File patient4_14b.txt downloaded !")
        #tk.messagebox.showinfo("INFO", "patient4_14b.txt downloaded !")
    else:
        print("[!] No file to download !")
        tk.messagebox.showerror("Error", "No patient4_14b.txt to download !")

def needload5():
    """
        to download med files from server before
        to start with med interface.
    """
    needata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt5/Files5/main_14b.txt",
        "./need/doc_suivi5/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Download] File main_14b.txt downloaded !")
        #tk.messagebox.showinfo("INFO", "main_14b.txt downloaded !")
    else:
        print("[!] No file to download !")
        tk.messagebox.showerror("Error", "No main_14b.txt to download !")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt5/Files5/patient5_14b.txt",
        "./need/doc_suivi5/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[Download] File patient5_14b.txt downloaded !")
        #tk.messagebox.showinfo("INFO", "patient5_14b.txt downloaded !")
    else:
        print("[!] No file to download !")
        tk.messagebox.showerror("Error", "No patient5_14b.txt to download !")

def needload6():
    """
        to download med files from server before
        to start with med interface.
    """
    needata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt6/Files6/main_14b.txt",
        "./need/doc_suivi6/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Download] File main_14b.txt downloaded !")
        #tk.messagebox.showinfo("INFO", "main_14b.txt downloaded !")
    else:
        print("[!] No file to download !")
        tk.messagebox.showerror("Error", "No main_14b.txt to download !")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt6/Files6/patient6_14b.txt",
        "./need/doc_suivi6/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[Download] File patient6_14b.txt downloaded !")
        #tk.messagebox.showinfo("INFO", "patient6_14b.txt downloaded !")
    else:
        print("[!] No file to download !")
        tk.messagebox.showerror("Error", "No patient6_14b.txt to download !")

def needload7():
    """
        to download med files from server before
        to start with med interface.
    """
    needata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt7/Files7/main_14b.txt",
        "./need/doc_suivi7/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Download] File main_14b.txt downloaded !")
        #tk.messagebox.showinfo("INFO", "main_14b.txt downloaded !")
    else:
        print("[!] No file to download !")
        tk.messagebox.showerror("Error", "No main_14b.txt to download !")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt7/Files7/patient7_14b.txt",
        "./need/doc_suivi7/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[Download] File patient7_14b.txt downloaded !")
        #tk.messagebox.showinfo("INFO", "patient7_14b.txt downloaded !")
    else:
        print("[!] No file to download !")
        tk.messagebox.showerror("Error", "No patient7_14b.txt to download !")

def needload8():
    """
        to download med files from server before
        to start with med interface.
    """
    needata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt8/Files8/main_14b.txt",
        "./need/doc_suivi8/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Download] File main_14b.txt downloaded !")
        #tk.messagebox.showinfo("INFO", "main_14b.txt downloaded !")
    else:
        print("[!] No file to download !")
        tk.messagebox.showerror("Error", "No main_14b.txt to download !")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt8/Files8/patient8_14b.txt",
        "./need/doc_suivi8/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[Download] File patient8_14b.txt downloaded !")
        #tk.messagebox.showinfo("INFO", "patient8_14b.txt downloaded !")
    else:
        print("[!] No file to download !")
        tk.messagebox.showerror("Error", "No patient8_14b.txt to download !")

def needload9():
    """
        to download med files from server before
        to start with med interface.
    """
    needata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt9/Files9/main_14b.txt",
        "./need/doc_suivi9/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Download] File main_14b.txt downloaded !")
        #tk.messagebox.showinfo("INFO", "main_14b.txt downloaded !")
    else:
        print("[!] No file to download !")
        tk.messagebox.showerror("Error", "No main_14b.txt to download !")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt3/Files9/patient9_14b.txt",
        "./need/doc_suivi9/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[Download] File patient9_14b.txt downloaded !")
        #tk.messagebox.showinfo("INFO", "patient9_14b.txt downloaded !")
    else:
        print("[!] No file to download !")
        tk.messagebox.showerror("Error", "No patient9_14b.txt to download !")

def needload10():
    """
        to download med files from server before
        to start with med interface.
    """
    needata()
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
    needata()
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
    needata()
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
    needata()
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
    needata()
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
    needata()
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
    needata()
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
    needata()
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
    needata()
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
    needata()
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
    needata()
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
    needata()
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
    needata()
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
    needata()
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
    needata()
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
