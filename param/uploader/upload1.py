#!/usr/bin/python3
# -*- coding : utf-8 -*-


import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os
import subprocess
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
    """
        To upload vital parameters files
    """
    #time.sleep(1)
    proc = subprocess.run(["scp", "./param/paramdata1.txt",
        "pi@192.168.18.12:~/tt_doc/doc_txt1/Files1/paramdata1.txt"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[+] File paramdata1.txt uploaded !")
        #tk.messagebox.showinfo("INFO", "paramdata1.txt uploaded...")
    else:
        print("[!] No file to upload !")
        tk.messagebox.showerror("Error", "No paramdata1.txt to upload...")

    secproc = subprocess.run(["scp", "./param/aspifile1/diastol.json",
        "pi@192.168.18.12:~/tt_doc/doc_txt1/Files1/diastol.json"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[+] File diastol.json uploaded !")
        #tk.messagebox.showinfo("INFO", "diastol.json uploaded...")
    else:
        print("[!] No file to upload !")
        tk.messagebox.showerror("Error", "No diastol.json to upload...")

    thirdproc = subprocess.run(["scp", "./param/aspifile1/systol.json",
        "pi@192.168.18.12:~/tt_doc/doc_txt1/Files1/systol.json"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(thirdproc.stderr))
    if thirdproc.stderr == b'':
        print("[+] File systol.json uploaded !")
        #tk.messagebox.showinfo("INFO", "systol.json uploaded...")
    else:
        print("[!] No file to upload !")
        tk.messagebox.showerror("Error", "No systol.json to upload...")

    fourproc = subprocess.run(["scp", "./param/aspifile1/dlr.json",
        "pi@192.168.18.12:~/tt_doc/doc_txt1/Files1/dlr.json"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(fourproc.stderr))
    if fourproc.stderr == b'':
        print("[+] File dlr.json uploaded !")
        #tk.messagebox.showinfo("INFO", "dlr.json uploaded...")
    else:
        print("[!] No file to upload !")
        tk.messagebox.showerror("Error", "No dlr.json to upload...")

    fiveproc = subprocess.run(["scp", "./param/aspifile1/freq.json",
        "pi@192.168.18.12:~/tt_doc/doc_txt1/Files1/freq.json"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(fiveproc.stderr))
    if fiveproc.stderr == b'':
        print("[+] File freq.json uploaded !")
        #tk.messagebox.showinfo("INFO", "freq.json uploaded...")
    else:
        print("[!] No file to upload !")
        tk.messagebox.showerror("Error", "No freq.json to upload...")

    sixproc = subprocess.run(["scp", "./param/aspifile1/gly.json",
        "pi@192.168.18.12:~/tt_doc/doc_txt1/Files1/gly.json"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(sixproc.stderr))
    if sixproc.stderr == b'':
        print("[+] File gly.json uploaded !")
        #tk.messagebox.showinfo("INFO", "gly.json uploaded...")
    else:
        print("[!] No file to upload !")
        tk.messagebox.showerror("Error", "No gly.json to upload...")

    sevenproc = subprocess.run(["scp", "./param/aspifile1/puls.json",
        "pi@192.168.18.12:~/tt_doc/doc_txt1/Files1/puls.json"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(sevenproc.stderr))
    if sevenproc.stderr == b'':
        print("[+] File puls.json uploaded !")
        #tk.messagebox.showinfo("INFO", "puls.json uploaded...")
    else:
        print("[!] No file to upload !")
        tk.messagebox.showerror("Error", "No puls.json to upload...")

    eightproc = subprocess.run(["scp", "./param/aspifile1/sat.json",
        "pi@192.168.18.12:~/tt_doc/doc_txt1/Files1/sat.json"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(eightproc.stderr))
    if eightproc.stderr == b'':
        print("[+] File sat.json uploaded !")
        #tk.messagebox.showinfo("INFO", "sat.json uploaded...")
    else:
        print("[!] No file to upload !")
        tk.messagebox.showerror("Error", "No sat.json to upload...")

    nineproc = subprocess.run(["scp", "./param/aspifile1/temp.json",
        "pi@192.168.18.12:~/tt_doc/doc_txt1/Files1/temp.json"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(nineproc.stderr))
    if nineproc.stderr == b'':
        print("[+] File temp.json uploaded !")
        #tk.messagebox.showinfo("INFO", "temp.json uploaded...")
    else:
        print("[!] No file to upload !")
        tk.messagebox.showerror("Error", "No temp.json to upload...")
    print('[PID] My pid is', os.getpid())
    print("\n[ - Upload complete - ]")
    root.quit()

def uploadata():
    root = tk.Tk()
    treat = threading.Thread(target=process_unknown_duration, args=(root,))
    treat.start()
    print("\n[ Uploading vital parameters... ]\n")
    managetask(root)
    treat.join()
    root.destroy()
