#!/usr/bin/python3
# -*- coding : utf-8 -*-


from tkinter import *
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
    root.mainloop()

def process_unknown_duration(root):
    time.sleep(1)
    proc = subprocess.run(["scp", "./calBmi/bmi19.txt",
        "pi@192.168.18.12:~/tt_doc/doc_txt19/Files19/bmi19.txt"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[+] File bmi19.txt uploaded !")
        #messagebox.showinfo("INFO", "bmi19.txt uploaded...")
    else:
        print("[!] No file to upload !")
        messagebox.showerror("Error", "No bmi19.txt to upload...")

    secproc = subprocess.run(["scp", "./calBmi/doc_BMI19/file_kg.json",
        "pi@192.168.18.12:~/tt_doc/doc_txt19/Files19/file_kg.json"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[+] File file_kg.json uploaded !")
        #messagebox.showinfo("INFO", "file_kg.json uploaded...")
    else:
        print("[!] No file to upload !")
        messagebox.showerror("Error", "No file_kg.json to upload...")

    thirdproc = subprocess.run(["scp", "./calBmi/doc_BMI19/file_bmi.json",
        "pi@192.168.18.12:~/tt_doc/doc_txt19/Files19/file_bmi.json"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(thirdproc.stderr))
    if thirdproc.stderr == b'':
        print("[+] File file_bmi.json uploaded !")
        #messagebox.showinfo("INFO", "file_bmi.json uploaded...")
    else:
        print("[!] No file to upload !")
        messagebox.showerror("Error", "No file_bmi.json to upload...")

    print('Upload done !')
    root.quit()

def uploadata():
    root = tk.Tk()
    treat = threading.Thread(target=process_unknown_duration, args=(root,))
    treat.start()
    managetask(root)  # This will block while the mainloop runs
    treat.join()
    root.destroy()
