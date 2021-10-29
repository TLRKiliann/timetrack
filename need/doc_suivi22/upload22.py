#!/usr/bin/python3
# -*- coding : utf-8 -*-


import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import subprocess
import time
import threading


def managetask(root):
    root.title("Uploading")
    style = ttk.Style()
    style.theme_use('alt')
    style.configure('blue.Horizontal.TProgressbar',
        troughcolor = '#4d4d4d',
        troughrelief = 'flat',
        background = '#2f92ff')

    pb = ttk.Progressbar(root,
        style = 'blue.Horizontal.TProgressbar',
        orient = 'horizontal',
        length = 200,
        mode = 'indeterminate')
    pb.pack()
    pb.start(10)
    root.resizable(False, False)
    root.mainloop()

def process_unknown_duration(root):
    time.sleep(1)
    proc = subprocess.run(["scp", "./need/doc_suivi22/main_14b.txt",
        "pi@192.168.18.12:~/tt_doc/doc_txt22/Files22/main_14b.txt"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Upload] File main_14b.txt uploaded !")
        #tk.messagebox.showinfo("INFO", "main_14b.txt uploaded...")
    else:
        print("[!] No file to upload !")
        tk.messagebox.showerror("Error", "No main_14b.txt to upload...")

    secproc = subprocess.run(["scp", "./need/doc_suivi22/patient22_14b.txt",
        "pi@192.168.18.12:~/tt_doc/doc_txt22/Files22/patient22_14b.txt"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[Upload] File patient22_14b.txt uploaded !")
        #tk.messagebox.showinfo("INFO", "patient22_14b.txt uploaded...")
    else:
        print("[!] No file to upload !")
        tk.messagebox.showerror("Error", "No patient22_14b.txt to upload...")
    print("\n[ - Upload complete - ]")
    root.quit()

def needuploadata():
    root = tk.Tk()
    treat = threading.Thread(target=process_unknown_duration, args=(root,))
    treat.start()
    print("\n[ Uploading data from 14 needs... ]\n")
    managetask(root)
    treat.join()
    root.destroy()
