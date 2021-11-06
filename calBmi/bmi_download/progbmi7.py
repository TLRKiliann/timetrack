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
import time
import subprocess
import os


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

    pb_hD = ttk.Progressbar(root,
        style = 'blue.Horizontal.TProgressbar',
        orient = 'horizontal',
        length = 200,
        mode = 'indeterminate')
    pb_hD.pack()
    pb_hD.start(10)
    root.resizable(False, False)
    root.mainloop()

def procesSubBmi(root):
    """
        Define the process of unknown duration
        with root as one of the input And once
        done, add root.quit() at the end.
    """
    time.sleep(1)
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt7/Files7/bmi7.txt",
        "./calBmi/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Download] File bmi7.txt downloaded !")
        #tk.messagebox.showinfo("INFO", "bmi7.txt downloaded")
    else:
        print("[!] No file to download !")
        tk.messagebox.showerror("Error", "No bmi7.txt to download")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt7/Files7/file_kg.json",
        "./calBmi/doc_BMI7/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[Download] File file_kg.json downloaded !")
        #tk.messagebox.showinfo("INFO", "file_kg.json downloaded")
    else:
        print("[!] No file to download !")
        tk.messagebox.showerror("Error", "No file_kg.json to download")

    thirdproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt7/Files7/file_bmi.json",
        "./calBmi/doc_BMI7/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(thirdproc.stderr))
    if thirdproc.stderr == b'':
        print("[Download] File file_bmi.json downloaded !")
        #tk.messagebox.showinfo("INFO", "file_bmi.json downloaded")
    else:
        print("[!] No file to download !")
        tk.messagebox.showerror("Error", "No file_bmi.json to download...")
    # linux, mac
    print('My pid is', os.getpid())
    print("[ Download complete ]")
    root.quit()

def downloadBmi7():
    """
        To start app with thread !
    """
    root = tk.Tk()
    t1 = threading.Thread(target=procesSubBmi, args=(root,))
    t1.start()
    print("[ Downloading BMI_7 start ]")
    task(root)
    t1.join()
    root.destroy()
