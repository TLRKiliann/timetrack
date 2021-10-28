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
        mode = 'determinate')
    pb_need.pack()
    pb_need.start(5)
    root.resizable(False, False)
    root.mainloop()

def process_launched(root):
    """
        to download med files from server before
        to start with med interface.
    """
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

    print('My pid is :', os.getpid())
    root.quit()

def need_dl7():
    root = tk.Tk()
    t1 = threading.Thread(target=process_launched, args=(root,))
    t1.start()
    print("[ Downloading 14 needs... ]")
    task(root)
    t1.join()
    root.destroy()