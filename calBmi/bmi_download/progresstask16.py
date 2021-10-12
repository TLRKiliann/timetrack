#!/usr/bin/python3
# -*- coding : utf-8 -*-


"""
    Connecting the duration of progress bar
    with task = number of subprocess.
"""


from tkinter import *
import tkinter as tk
from tkinter import ttk
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
    root.mainloop()

def process_of_unknown_duration(root):
    """
        Define the process of unknown duration
        with root as one of the input And once
        done, add root.quit() at the end.
    """
    time.sleep(1)
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt16/Files16/bmi16.txt",
        "./calBmi/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File bmi16.txt downloaded !")
        #messagebox.showinfo("INFO", "bmi16.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No bmi16.txt to download")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt16/Files16/file_kg.json",
        "./calBmi/doc_BMI16/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("+ File file_kg.json downloaded !")
        #messagebox.showinfo("INFO", "file_kg.json downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No file_kg.json to download")

    thirdproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt16/Files16/file_bmi.json",
        "./calBmi/doc_BMI16/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(thirdproc.stderr))
    if thirdproc.stderr == b'':
        print("+ File file_bmi.json downloaded !")
        #messagebox.showinfo("INFO", "file_bmi.json downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No file_bmi.json to download...")

    print('Done')
    # linux, mac
    print('My pid is', os.getpid())
    root.quit() # To destroy threading

def downloadata():
    """
        To start app with thread !
    """
    root = tk.Tk()
    t1 = threading.Thread(target=process_of_unknown_duration, args=(root,))
    #print(t1)
    t1.start()
    print("Download...")
    task(root) # This will block while the mainloop runs
    t1.join()
    root.destroy() # To destroy completely window
