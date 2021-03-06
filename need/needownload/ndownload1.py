#!/usr/bin/python3
# -*- coding : utf-8 -*-


"""
    Connecting the duration of progress bar
    with task = number of subprocess.
"""


import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import threading
import os
import subprocess


def task(root):
    """
        Define Progress Bar function
    """
    root.title("Downloading")
    s = ttk.Style()
    s.theme_use('alt')
    s.configure('blue.Horizontal.TProgressbar',
        troughcolor = '#4d4d4d',
        troughrelief = 'flat',
        background = '#2f92ff')

    pb_need = ttk.Progressbar(root,
        style = 'blue.Horizontal.TProgressbar',
        orient = 'horizontal',
        length = 200,
        mode = 'indeterminate')
    pb_need.pack()
    pb_need.start(10)
    root.resizable(False, False)
    root.mainloop()

def process_launched(root):
    """
        to download med files from server before
        to start with suivi_patient_1 interface.
    """
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

    print('My pid is :', os.getpid())
    print("[ Downloading complete ! ]")
    root.quit()

def need_dl1():
    root = tk.Tk()
    t1 = threading.Thread(target=process_launched, args=(root,))
    t1.start()
    print("[ Downloading 14 needs... ]")
    task(root)
    t1.join()
    root.destroy()
