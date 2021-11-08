#!/usr/bin/python3
# -*- coding : utf-8 -*-


import tkinter as tk
from tkinter import ttk
import time
import threading


def task(root):
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
        mode = 'determinate')
    pb.pack()
    pb.start(10)
    root.mainloop()

def processUpload(root):
    time.sleep(1)
    print('[ Uploading complete ! ]')
    root.quit()

def uploadmain():
    root = tk.Tk()
    thrd=threading.Thread(target=processUpload, args=(root,))
    thrd.start()
    print("[ Uploading 14 need started... ]")
    task(root)
    thrd.join()
    root.destroy()
