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

def process_of_unknown_duration(root):
    """
        Define the process of unknown duration
        with root as one of the input And once
        done, add root.quit() at the end.
    """
    time.sleep(1)
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt8/Files8/paramdata8.txt",
        "./param/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[+] File paramdata8.txt downloaded !")
        #tk.messagebox.showinfo("INFO", "paramdata8.txt downloaded")
    else:
        print("[!] No file to download !")
        tk.messagebox.showerror("Error", "No paramdata8.txt to download !")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt8/Files8/diastol.json",
        "./param/aspifile8/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[+] File diastol.json downloaded !")
        #tk.messagebox.showinfo("INFO", "diastol.json downloaded")
    else:
        print("[!] No file to download !")
        tk.messagebox.showerror("Error", "No diastol.json to download !")

    thirdproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt8/Files8/dlr.json",
        "./param/aspifile8/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(thirdproc.stderr))
    if thirdproc.stderr == b'':
        print("[+] File dlr.json downloaded !")
        #tk.messagebox.showinfo("INFO", "dlr.json downloaded")
    else:
        print("[!] No file to download !")
        tk.messagebox.showerror("Error", "No dlr.json to download !")

    forthproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt8/Files8/freq.json",
        "./param/aspifile8/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(forthproc.stderr))
    if forthproc.stderr == b'':
        print("[+] File freq.json downloaded !")
        #tk.messagebox.showinfo("INFO", "freq.json downloaded")
    else:
        print("[!] No file to download !")
        tk.messagebox.showerror("Error", "No freq.json to download !")

    fivthproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt8/Files8/gly.json",
        "./param/aspifile8/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(fivthproc.stderr))
    if fivthproc.stderr == b'':
        print("[+] File gly.json downloaded !")
        #tk.messagebox.showinfo("INFO", "gly.json downloaded")
    else:
        print("[!] No file to download !")
        tk.messagebox.showerror("Error", "No gly.json to download !")

    sixthproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt8/Files8/puls.json",
        "./param/aspifile8/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(sixthproc.stderr))
    if sixthproc.stderr == b'':
        print("[+] File puls.json downloaded !")
        #tk.messagebox.showinfo("INFO", "puls.json downloaded")
    else:
        print("[!] No file to download !")
        tk.messagebox.showerror("Error", "No puls.json to download !")

    sevenproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt8/Files8/sat.json",
        "./param/aspifile8/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(sevenproc.stderr))
    if sevenproc.stderr == b'':
        print("[+] File sat.json downloaded !")
        #tk.messagebox.showinfo("INFO", "sat.json downloaded")
    else:
        print("[!] No file to download !")
        tk.messagebox.showerror("Error", "No sat.json to download !")

    eightproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt8/Files8/systol.json",
        "./param/aspifile8/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(eightproc.stderr))
    if eightproc.stderr == b'':
        print("[+] File systol.json downloaded !")
        #tk.messagebox.showinfo("INFO", "systol.json downloaded")
    else:
        print("[!] No file to download !")
        tk.messagebox.showerror("Error", "No systol.json to download !")

    ninethproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt8/Files8/temp.json",
        "./param/aspifile8/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(ninethproc.stderr))
    if ninethproc.stderr == b'':
        print("[+] File temp.json downloaded !")
        #tk.messagebox.showinfo("INFO", "temp.json downloaded")
    else:
        print("[!] No file to download !")
        tk.messagebox.showerror("Error", "No temp.json to download !")
    print('Done')
    # linux, mac
    print('[PID] My pid is', os.getpid())
    print("\n[ - Download complete - ]")
    root.quit() # To destroy threading

def downloadata():
    """
        To start app with thread !
    """
    root = tk.Tk()
    t1 = threading.Thread(target=process_of_unknown_duration, args=(root,))
    t1.start()
    print("\n[ Downloading vital parameters... ]\n")
    task(root)
    t1.join()
    root.destroy()
