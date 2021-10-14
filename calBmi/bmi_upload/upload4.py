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
    proc = subprocess.run(["scp", "./calBmi/bmi4.txt",
        "pi@192.168.18.12:~/tt_doc/doc_txt4/Files4/bmi4.txt"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Upload] File bmi4.txt uploaded !")
        #tk.messagebox.showinfo("INFO", "bmi4.txt uploaded...")
    else:
        print("[!] No file to upload !")
        tk.messagebox.showerror("Error", "No bmi4.txt to upload...")

    secproc = subprocess.run(["scp", "./calBmi/doc_BMI2/file_kg.json",
        "pi@192.168.18.12:~/tt_doc/doc_txt4/Files4/file_kg.json"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[Upload] File file_kg.json uploaded !")
        #tk.messagebox.showinfo("INFO", "file_kg.json uploaded...")
    else:
        print("[!] No file to upload !")
        tk.messagebox.showerror("Error", "No file_kg.json to upload...")

    thirdproc = subprocess.run(["scp", "./calBmi/doc_BMI2/file_bmi.json",
        "pi@192.168.18.12:~/tt_doc/doc_txt4/Files4/file_bmi.json"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(thirdproc.stderr))
    if thirdproc.stderr == b'':
        print("[Upload] File file_bmi.json uploaded !")
        #tk.messagebox.showinfo("INFO", "file_bmi.json uploaded...")
    else:
        print("[!] No file to upload !")
        tk.messagebox.showerror("Error", "No file_bmi.json to upload...")

    print('Upload done !')
    root.quit()

def uploadata():
    root = tk.Tk()
    treat = threading.Thread(target=process_unknown_duration, args=(root,))
    treat.start()
    managetask(root)  # This will block while the mainloop runs
    treat.join()
    root.destroy()
