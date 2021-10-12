#!/usr/bin/python3
# -*- coding : utf-8 -*-


from tkinter import *
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

    pb_hD = ttk.Progressbar(root,
        style = 'blue.Horizontal.TProgressbar',
        orient = 'horizontal',
        length = 200,
        mode = 'determinate')
    pb_hD.pack()
    pb_hD.start(10)
    root.mainloop()

def process_launched(root):
    """
        Define the process of unknown duration
        with root as one of the input And once
        done, add root.quit() at the end.
    """
    time.sleep(1)
    print('My pid is', os.getpid())
    root.quit() # To destroy threading

def medata():
    root = tk.Tk()
    t1 = threading.Thread(target=process_launched, args=(root,))
    #print(t1)
    t1.start()
    print("Download...")
    task(root) # This will block while the mainloop runs
    t1.join()
    root.destroy() # To destroy completely window
