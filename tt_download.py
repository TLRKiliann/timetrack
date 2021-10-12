#!/usr/bin/python3
# -*- coding : utf-8 -*-


"""
    Connecting the duration of progress bar
    with task = number of subprocess.
"""


#from tkinter import *
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
    style = ttk.Style()
    style.theme_use('alt')
    style.configure('blue.Horizontal.TProgressbar',
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
    proc = subprocess.run(["scp", "-r", "-C",
        "pi@192.168.18.12:~/tt_doc/doc_txt1/Files1",
        "./Backup/"], stderr=subprocess.PIPE)
    print("[Download] Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Download] Folder Files1 downloaded...")
    else:
        print("[!] No folder Files1 to download from server !")
        messagebox.showerror("Error", "No folder Files1 to download from server !")

    secproc = subprocess.run(["scp", "-r", "-C",
        "pi@192.168.18.12:~/tt_doc/doc_txt2/Files2",
        "./Backup/"], stderr=subprocess.PIPE)
    print("[Download] Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[Download] Folder Files2 downloaded...")
    else:
        print("[!] No folder Files2 to download from server !")
        messagebox.showerror("Error", "No folder Files2 to download from server !")

    thirdproc = subprocess.run(["scp", "-r", "-C",
        "pi@192.168.18.12:~/tt_doc/doc_txt3/Files3",
        "./Backup/"], stderr=subprocess.PIPE)
    print("[Download] Result SCP transfert : %s" % repr(thirdproc.stderr))
    if thirdproc.stderr == b'':
        print("[Download] Folder Files3 downloaded...")
    else:
        print("[!] No folder Files3 to download from server !")
        messagebox.showerror("Error", "No folder Files3 to download from server !")

    forthproc = subprocess.run(["scp", "-r", "-C",
        "pi@192.168.18.12:~/tt_doc/doc_txt4/Files4",
        "./Backup/"], stderr=subprocess.PIPE)
    print("[Download] Result SCP transfert : %s" % repr(forthproc.stderr))
    if forthproc.stderr == b'':
        print("[Download] Folder Files4 downloaded...")
    else:
        print("[!] No folder Files4 to download from server !")
        messagebox.showerror("Error", "No folder Files4 to download from server !")

    fivthproc = subprocess.run(["scp", "-r", "-C",
        "pi@192.168.18.12:~/tt_doc/doc_txt5/Files5",
        "./Backup/"], stderr=subprocess.PIPE)
    print("[Download] Result SCP transfert : %s" % repr(fivthproc.stderr))
    if fivthproc.stderr == b'':
        print("[Download] Folder Files5 downloaded...")
    else:
        print("[!] No folder Files5 to download from server !")
        messagebox.showerror("Error", "No folder Files5 to download from server !")

    sixthproc = subprocess.run(["scp", "-r", "-C",
        "pi@192.168.18.12:~/tt_doc/doc_txt6/Files6",
        "./Backup/"], stderr=subprocess.PIPE)
    print("[Download] Result SCP transfert : %s" % repr(sixthproc.stderr))
    if sixthproc.stderr == b'':
        print("[Download] Folder Files6 downloaded...")
    else:
        print("[!] No folder Files6 to download from server !")
        messagebox.showerror("Error", "No folder Files6 to download from server !")

    sevenproc = subprocess.run(["scp", "-r", "-C",
        "pi@192.168.18.12:~/tt_doc/doc_txt7/Files7",
        "./Backup/"], stderr=subprocess.PIPE)
    print("[Download] Result SCP transfert : %s" % repr(sevenproc.stderr))
    if sevenproc.stderr == b'':
        print("[Download] Folder Files7 downloaded...")
    else:
        print("[!] No folder Files7 to download from server !")
        messagebox.showerror("Error", "No folder Files7 to download from server !")

    eightproc = subprocess.run(["scp", "-r", "-C",
        "pi@192.168.18.12:~/tt_doc/doc_txt8/Files8",
        "./Backup/"], stderr=subprocess.PIPE)
    print("[Download] Result SCP transfert : %s" % repr(eightproc.stderr))
    if eightproc.stderr == b'':
        print("[Download] Folder Files8 downloaded...")
    else:
        print("[!] No folder Files8 to download from server !")
        messagebox.showerror("Error", "No folder Files8 to download from server !")

    ninethproc = subprocess.run(["scp", "-r", "-C",
        "pi@192.168.18.12:~/tt_doc/doc_txt9/Files9",
        "./Backup/"], stderr=subprocess.PIPE)
    print("[Download] Result SCP transfert : %s" % repr(ninethproc.stderr))
    if ninethproc.stderr == b'':
        print("[Download] Folder Files9 downloaded...")
    else:
        print("[!] No folder Files9 to download from server !")
        messagebox.showerror("Error", "No folder Files9 to download from server !")

    tenproc = subprocess.run(["scp", "-r", "-C",
        "pi@192.168.18.12:~/tt_doc/doc_txt10/Files10",
        "./Backup/"], stderr=subprocess.PIPE)
    print("[Download] Result SCP transfert : %s" % repr(tenproc.stderr))
    if tenproc.stderr == b'':
        print("[Download] Folder Files10 downloaded...")
    else:
        print("[!] No folder Files10 to download from server !")
        messagebox.showerror("Error", "No folder Files10 to download from server !")

    eleventhproc = subprocess.run(["scp", "-r", "-C",
        "pi@192.168.18.12:~/tt_doc/doc_txt11/Files11",
        "./Backup/"], stderr=subprocess.PIPE)
    print("[Download] Result SCP transfert : %s" % repr(eleventhproc.stderr))
    if eleventhproc.stderr == b'':
        print("[Download] Folder Files11 downloaded...")
    else:
        print("[!] No folder Files11 to download from server !")
        messagebox.showerror("Error", "No folder Files11 to download from server !")

    twelvthproc = subprocess.run(["scp", "-r", "-C",
        "pi@192.168.18.12:~/tt_doc/doc_txt12/Files12",
        "./Backup/"], stderr=subprocess.PIPE)
    print("[Download] Result SCP transfert : %s" % repr(twelvthproc.stderr))
    if twelvthproc.stderr == b'':
        print("[Download] Folder Files12 downloaded...")
    else:
        print("[!] No folder Files12 to download from server !")
        messagebox.showerror("Error", "No folder Files12 to download from server !")

    thirthproc = subprocess.run(["scp", "-r", "-C",
        "pi@192.168.18.12:~/tt_doc/doc_txt13/Files13",
        "./Backup/"], stderr=subprocess.PIPE)
    print("[Download] Result SCP transfert : %s" % repr(thirthproc.stderr))
    if thirthproc.stderr == b'':
        print("[Download] Folder Files13 downloaded...")
    else:
        print("[!] No folder Files13 to download from server !")
        messagebox.showerror("Error", "No folder Files13 to download from server !")

    fourteenproc = subprocess.run(["scp", "-r", "-C",
        "pi@192.168.18.12:~/tt_doc/doc_txt14/Files14",
        "./Backup/"], stderr=subprocess.PIPE)
    print("[Download] Result SCP transfert : %s" % repr(fourteenproc.stderr))
    if fourteenproc.stderr == b'':
        print("[Download] Folder Files14 downloaded...")
    else:
        print("[!] No folder Files14 to download from server !")
        messagebox.showerror("Error", "No folder Files14 to download from server !")

    fivteenthproc = subprocess.run(["scp", "-r", "-C",
        "pi@192.168.18.12:~/tt_doc/doc_txt15/Files15",
        "./Backup/"], stderr=subprocess.PIPE)
    print("[Download] Result SCP transfert : %s" % repr(fivteenthproc.stderr))
    if fivteenthproc.stderr == b'':
        print("[Download] Folder Files15 downloaded...")
    else:
        print("[!] No folder Files15 to download from server !")
        messagebox.showerror("Error", "No folder Files15 to download from server !")

    sixteenthproc = subprocess.run(["scp", "-r", "-C",
        "pi@192.168.18.12:~/tt_doc/doc_txt16/Files16",
        "./Backup/"], stderr=subprocess.PIPE)
    print("[Download] Result SCP transfert : %s" % repr(sixteenthproc.stderr))
    if sixteenthproc.stderr == b'':
        print("[Download] Folder Files16 downloaded...")
    else:
        print("[!] No folder Files16 to download from server !")
        messagebox.showerror("Error", "No folder Files16 to download from server !")

    seventeenthproc = subprocess.run(["scp", "-r", "-C",
        "pi@192.168.18.12:~/tt_doc/doc_txt17/Files17",
        "./Backup/"], stderr=subprocess.PIPE)
    print("[Download] Result SCP transfert : %s" % repr(seventeenthproc.stderr))
    if seventeenthproc.stderr == b'':
        print("[Download] Folder Files17 downloaded...")
    else:
        print("[!] No folder Files17 to download from server !")
        messagebox.showerror("Error", "No folder Files17 to download from server !")

    eighteenthproc = subprocess.run(["scp", "-r", "-C",
        "pi@192.168.18.12:~/tt_doc/doc_txt18/Files18",
        "./Backup/"], stderr=subprocess.PIPE)
    print("[Download] Result SCP transfert : %s" % repr(eighteenthproc.stderr))
    if eighteenthproc.stderr == b'':
        print("[Download] Folder Files18 downloaded...")
    else:
        print("[!] No folder Files18 to download from server !")
        messagebox.showerror("Error", "No folder Files18 to download from server !")

    ninteenthproc = subprocess.run(["scp", "-r", "-C",
        "pi@192.168.18.12:~/tt_doc/doc_txt19/Files19",
        "./Backup/"], stderr=subprocess.PIPE)
    print("[Download] Result SCP transfert : %s" % repr(ninteenthproc.stderr))
    if ninteenthproc.stderr == b'':
        print("[Download] Folder Files19 downloaded...")
    else:
        print("[!] No folder Files19 to download from server !")
        messagebox.showerror("Error", "No folder Files19 to download from server !")

    twentythproc = subprocess.run(["scp", "-r", "-C",
        "pi@192.168.18.12:~/tt_doc/doc_txt20/Files20",
        "./Backup/"], stderr=subprocess.PIPE)
    print("[Download] Result SCP transfert : %s" % repr(twentythproc.stderr))
    if twentythproc.stderr == b'':
        print("[Download] Folder Files20 downloaded...")
    else:
        print("[!] No folder Files20 to download from server !")
        messagebox.showerror("Error", "No folder Files20 to download from server !")

    twentyoneproc = subprocess.run(["scp", "-r", "-C",
        "pi@192.168.18.12:~/tt_doc/doc_txt21/Files21",
        "./Backup/"], stderr=subprocess.PIPE)
    print("[Download] Result SCP transfert : %s" % repr(twentyoneproc.stderr))
    if twentyoneproc.stderr == b'':
        print("[Download] Folder Files21 downloaded...")
    else:
        print("[!] No folder Files21 to download from server !")
        messagebox.showerror("Error", "No folder Files21 to download from server !")

    twentytwoproc = subprocess.run(["scp", "-r", "-C",
        "pi@192.168.18.12:~/tt_doc/doc_txt22/Files22",
        "./Backup/"], stderr=subprocess.PIPE)
    print("[Download] Result SCP transfert : %s" % repr(twentytwoproc.stderr))
    if twentytwoproc.stderr == b'':
        print("[Download] Folder Files22 downloaded...")
    else:
        print("[!] No folder Files22 to download from server !")
        messagebox.showerror("Error", "No folder Files22 to download from server !")

    twentythreeproc = subprocess.run(["scp", "-r", "-C",
        "pi@192.168.18.12:~/tt_doc/doc_txt23/Files23",
        "./Backup/"], stderr=subprocess.PIPE)
    print("[Download] Result SCP transfert : %s" % repr(twentythreeproc.stderr))
    if twentythreeproc.stderr == b'':
        print("[Download] Folder Files23 downloaded...")
    else:
        print("[!] No folder Files23 to download from server !")
        messagebox.showerror("Error", "No folder Files23 to download from server !")

    twentyfourproc = subprocess.run(["scp", "-r", "-C",
        "pi@192.168.18.12:~/tt_doc/doc_txt24/Files24",
        "./Backup/"], stderr=subprocess.PIPE)
    print("[Download] Result SCP transfert : %s" % repr(twentyfourproc.stderr))
    if twentyfourproc.stderr == b'':
        print("[Download] Folder Files24 downloaded...")
    else:
        print("[!] No folder Files24 to download from server !")
        messagebox.showerror("Error", "No folder Files24 to download from server !")

    print('Downloading done !\n')
    print('[PID] My pid is :', os.getpid())
    root.quit()

def launchdownload():
    """
        To start app with thread !
    """
    root = tk.Tk()
    treat = threading.Thread(target=process_of_unknown_duration, args=(root,))
    treat.start()
    print("\n[Downloading...]\n")
    # This will block while the mainloop runs
    task(root)
    treat.join()
    root.destroy()
