#!/usr/bin/python3
# -*- coding : utf-8 -*-


import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import subprocess
import time
import threading


def managetask(root):
    root.title("Upload")
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
    proc = subprocess.run(["scp", "./need/doc_suivi11/main_14b.txt",
        "pi@192.168.18.12:~/tt_doc/doc_txt11/Files11/main_14b.txt"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Upload] File main_14b.txt uploaded !")
        #tk.messagebox.showinfo("INFO", "main_14b.txt uploaded...")
    else:
        print("[!] No file to upload !")
        tk.messagebox.showerror("Error", "No main_14b.txt to upload...")

    secproc = subprocess.run(["scp", "./need/doc_suivi11/patient11_14b.txt",
        "pi@192.168.18.12:~/tt_doc/doc_txt11/Files11/patient11_14b.txt"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[Upload] File patient11_14b.txt uploaded !")
        #tk.messagebox.showinfo("INFO", "patient11_14b.txt uploaded...")
    else:
        print("[!] No file to upload !")
        tk.messagebox.showerror("Error", "No patient11_14b.txt to upload...")
    print('Upload done !')
    root.quit()

def needuploadata():
    root = tk.Tk()
    treat = threading.Thread(target=process_unknown_duration, args=(root,))
    treat.start()
    managetask(root)
    treat.join()
    root.destroy()