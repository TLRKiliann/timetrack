#!/usr/bin/python3
# -*- coding : utf-8 -*-


import tkinter as tk
from tkinter import ttk
import threading
import time
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

    pbdown = ttk.Progressbar(root,
        style = 'blue.Horizontal.TProgressbar',
        orient = 'horizontal',
        length = 200,
        mode = 'determinate')
    pbdown.pack()
    pbdown.start(10)
    root.resizable(False, False)
    root.mainloop()

def processDownload(root):
    """
        Define the process of unknown duration
        with root as one of the input And once
        done, add root.quit() at the end.
    """
    time.sleep(1)
    print("[PID] My pid is :", os.getpid())
    print("[ Downloading complete ! ]")
    root.quit()

def downloadatattt():
    root = tk.Tk()
    t1 = threading.Thread(target=processDownload, args=(root,))
    t1.start()
    print("\n[ Downloading for medication... ]\n")
    task(root)
    t1.join()
    root.destroy()
