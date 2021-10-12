#!/usr/bin/python3
# -*- coding: utf-8 -*-


from tkinter import messagebox
import os
import subprocess


def uploadstopttt():
    """
        Upload convdose.json to server.
    """
    tttproc = subprocess.run(["scp", "./ttt/doc_ttt/convdose.json",
        "pi@192.168.18.12:~/tt_doc/doc_txt1/Files1/convdose.json"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(tttproc.stderr))
    if tttproc.stderr == b'':
        print("[Upload] Patient 1 convdose.json uploaded.")
        messagebox.showinfo("INFO", "Patient 1 convdose.json uploaded.")
    else:
        print("[!] No file convdose.json for patient:1 to upload !")
        messagebox.showerror("Error", "No convdose.json for patient:1 to upload !")

def upload2stopttt():
    """
        Upload convdose.json to server.
    """
    tttproc2 = subprocess.run(["scp", "./ttt/doc_ttt2/convdose.json",
        "pi@192.168.18.12:~/tt_doc/doc_txt2/Files2/convdose.json"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(tttproc2.stderr))
    if tttproc2.stderr == b'':
        print("[Upload] Patient 2 convdose.json uploaded.")
        messagebox.showinfo("INFO", "Patient 2 convdose.json uploaded.")
    else:
        print("[!] No file convdose.json for patient:2 to upload !")
        messagebox.showerror("Error", "No convdose.json for patient:2 to upload !")

def upload3stopttt():
    """
        Upload convdose.json to server.
    """
    tttproc3 = subprocess.run(["scp", "./ttt/doc_ttt3/convdose.json",
        "pi@192.168.18.12:~/tt_doc/doc_txt3/Files3/convdose.json"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(tttproc3.stderr))
    if tttproc3.stderr == b'':
        print("[Upload] Patient 3 convdose.json uploaded.")
        messagebox.showinfo("INFO", "Patient 3 convdose.json uploaded.")
    else:
        print("[!] No file convdose.json for patient:3 to upload !")
        messagebox.showerror("Error", "No convdose.json for patient:3 to upload !")

def upload4stopttt():
    """
        Upload convdose.json to server.
    """
    tttproc4 = subprocess.run(["scp", "./ttt/doc_ttt4/convdose.json",
        "pi@192.168.18.12:~/tt_doc/doc_txt4/Files4/convdose.json"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(tttproc4.stderr))
    if tttproc4.stderr == b'':
        print("[Upload] Patient 4 convdose.json uploaded.")
        messagebox.showinfo("INFO", "Patient 4 convdose.json uploaded.")
    else:
        print("[!] No file convdose.json for patient:4 to upload !")
        messagebox.showerror("Error", "No convdose.json for patient:4 to upload !")

def upload5stopttt():
    """
        Upload convdose.json to server.
    """
    tttproc5 = subprocess.run(["scp", "./ttt/doc_ttt5/convdose.json",
        "pi@192.168.18.12:~/tt_doc/doc_txt5/Files5/convdose.json"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(tttproc5.stderr))
    if tttproc5.stderr == b'':
        print("[Upload] Patient 5 convdose.json uploaded.")
        messagebox.showinfo("INFO", "Patient 5 convdose.json uploaded.")
    else:
        print("[!] No file convdose.json for patient:5 to upload !")
        messagebox.showerror("Error", "No convdose.json for patient:5 to upload !")

def upload6stopttt():
    """
        Upload convdose.json to server.
    """
    tttproc6 = subprocess.run(["scp", "./ttt/doc_ttt6/convdose.json",
        "pi@192.168.18.12:~/tt_doc/doc_txt6/Files6/convdose.json"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(tttproc6.stderr))
    if tttproc6.stderr == b'':
        print("[Upload] Patient 6 convdose.json uploaded.")
        messagebox.showinfo("INFO", "Patient 6 convdose.json uploaded.")
    else:
        print("[!] No file convdose.json for patient:6 to upload !")
        messagebox.showerror("Error", "No convdose.json for patient:6 to upload !")

def upload7stopttt():
    """
        Upload convdose.json to server.
    """
    tttproc7 = subprocess.run(["scp", "./ttt/doc_ttt7/convdose.json",
        "pi@192.168.18.12:~/tt_doc/doc_txt7/Files7/convdose.json"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(tttproc7.stderr))
    if tttproc7.stderr == b'':
        print("[Upload] Patient 7 convdose.json uploaded.")
        messagebox.showinfo("INFO", "Patient 7 convdose.json uploaded.")
    else:
        print("[!] No file convdose.json for patient:7 to upload !")
        messagebox.showerror("Error", "No convdose.json for patient:7 to upload !")

def upload8stopttt():
    """
        Upload convdose.json to server.
    """
    tttproc8 = subprocess.run(["scp", "./ttt/doc_ttt8/convdose.json",
        "pi@192.168.18.12:~/tt_doc/doc_txt8/Files8/convdose.json"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(tttproc8.stderr))
    if tttproc8.stderr == b'':
        print("[Upload] Patient 8 convdose.json uploaded.")
        messagebox.showinfo("INFO", "Patient 8 convdose.json uploaded.")
    else:
        print("[!] No file convdose.json for patient:8 to upload !")
        messagebox.showerror("Error", "No convdose.json for patient:8 to upload !")

def upload9stopttt():
    """
        Upload convdose.json to server.
    """
    tttproc9 = subprocess.run(["scp", "./ttt/doc_ttt9/convdose.json",
        "pi@192.168.18.12:~/tt_doc/doc_txt9/Files9/convdose.json"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(tttproc9.stderr))
    if tttproc9.stderr == b'':
        print("[Upload] Patient 9 convdose.json uploaded.")
        messagebox.showinfo("INFO", "Patient 9 convdose.json uploaded.")
    else:
        print("[!] No file convdose.json for patient:9 to upload !")
        messagebox.showerror("Error", "No convdose.json for patient:9 to upload !")

def upload10stopttt():
    """
        Upload convdose.json to server.
    """
    tttproc10 = subprocess.run(["scp", "./ttt/doc_ttt10/convdose.json",
        "pi@192.168.18.12:~/tt_doc/doc_txt10/Files10/convdose.json"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(tttproc10.stderr))
    if tttproc10.stderr == b'':
        print("[Upload] Patient 10 convdose.json uploaded.")
        messagebox.showinfo("INFO", "Patient 10 convdose.json uploaded.")
    else:
        print("[!] No file convdose.json for patient:10 to upload !")
        messagebox.showerror("Error", "No convdose.json for patient:10 to upload !")

def upload11stopttt():
    """
        Upload convdose.json to server.
    """
    tttproc11 = subprocess.run(["scp", "./ttt/doc_ttt11/convdose.json",
        "pi@192.168.18.12:~/tt_doc/doc_txt11/Files11/convdose.json"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(tttproc11.stderr))
    if tttproc11.stderr == b'':
        print("[Upload] Patient 11 convdose.json uploaded.")
        messagebox.showinfo("INFO", "Patient 11 convdose.json uploaded.")
    else:
        print("[!] No file convdose.json for patient:11 to upload !")
        messagebox.showerror("Error", "No convdose.json for patient:11 to upload !")

def upload12stopttt():
    """
        Upload convdose.json to server.
    """
    tttproc12 = subprocess.run(["scp", "./ttt/doc_ttt12/convdose.json",
        "pi@192.168.18.12:~/tt_doc/doc_txt12/Files12/convdose.json"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(tttproc12.stderr))
    if tttproc12.stderr == b'':
        print("[Upload] Patient 12 convdose.json uploaded.")
        messagebox.showinfo("INFO", "Patient 12 convdose.json uploaded.")
    else:
        print("[!] No file convdose.json for patient:12 to upload !")
        messagebox.showerror("Error", "No convdose.json for patient:12 to upload !")

def upload13stopttt():
    """
        Upload convdose.json to server.
    """
    tttproc13 = subprocess.run(["scp", "./ttt/doc_ttt13/convdose.json",
        "pi@192.168.18.12:~/tt_doc/doc_txt13/Files13/convdose.json"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(tttproc13.stderr))
    if tttproc13.stderr == b'':
        print("[Upload] Patient 13 convdose.json uploaded.")
        messagebox.showinfo("INFO", "Patient 13 convdose.json uploaded.")
    else:
        print("[!] No file convdose.json for patient:13 to upload !")
        messagebox.showerror("Error", "No convdose.json for patient:13 to upload !")

def upload14stopttt():
    """
        Upload convdose.json to server.
    """
    tttproc14 = subprocess.run(["scp", "./ttt/doc_ttt14/convdose.json",
        "pi@192.168.18.12:~/tt_doc/doc_txt14/Files14/convdose.json"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(tttproc14.stderr))
    if tttproc14.stderr == b'':
        print("[Upload] Patient 14 convdose.json uploaded.")
        messagebox.showinfo("INFO", "Patient 14 convdose.json uploaded.")
    else:
        print("[!] No file convdose.json for patient:14 to upload !")
        messagebox.showerror("Error", "No convdose.json for patient:14 to upload !")

def upload15stopttt():
    """
        Upload convdose.json to server.
    """
    tttproc15 = subprocess.run(["scp", "./ttt/doc_ttt15/convdose.json",
        "pi@192.168.18.12:~/tt_doc/doc_txt15/Files15/convdose.json"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(tttproc15.stderr))
    if tttproc15.stderr == b'':
        print("[Upload] Patient 15 convdose.json uploaded.")
        messagebox.showinfo("INFO", "Patient 15 convdose.json uploaded.")
    else:
        print("[!] No file convdose.json for patient:15 to upload !")
        messagebox.showerror("Error", "No convdose.json for patient:15 to upload !")

def upload16stopttt():
    """
        Upload convdose.json to server.
    """
    tttproc16 = subprocess.run(["scp", "./ttt/doc_ttt16/convdose.json",
        "pi@192.168.18.12:~/tt_doc/doc_txt16/Files16/convdose.json"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(tttproc16.stderr))
    if tttproc16.stderr == b'':
        print("[Upload] Patient 16 convdose.json uploaded.")
        messagebox.showinfo("INFO", "Patient 16 convdose.json uploaded.")
    else:
        print("[!] No file convdose.json for patient:16 to upload !")
        messagebox.showerror("Error", "No convdose.json for patient:16 to upload !")

def upload17stopttt():
    """
        Upload convdose.json to server.
    """
    tttproc17 = subprocess.run(["scp", "./ttt/doc_ttt17/convdose.json",
        "pi@192.168.18.12:~/tt_doc/doc_txt17/Files17/convdose.json"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(tttproc17.stderr))
    if tttproc17.stderr == b'':
        print("[Upload] Patient 17 convdose.json uploaded.")
        messagebox.showinfo("INFO", "Patient 17 convdose.json uploaded.")
    else:
        print("[!] No file convdose.json for patient:17 to upload !")
        messagebox.showerror("Error", "No convdose.json for patient:17 to upload !")

def upload18stopttt():
    """
        Upload convdose.json to server.
    """
    tttproc18 = subprocess.run(["scp", "./ttt/doc_ttt18/convdose.json",
        "pi@192.168.18.12:~/tt_doc/doc_txt18/Files18/convdose.json"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(tttproc18.stderr))
    if tttproc18.stderr == b'':
        print("[Upload] Patient 18 convdose.json uploaded.")
        messagebox.showinfo("INFO", "Patient 18 convdose.json uploaded.")
    else:
        print("[!] No file convdose.json for patient:18 to upload !")
        messagebox.showerror("Error", "No convdose.json for patient:18 to upload !")

def upload19stopttt():
    """
        Upload convdose.json to server.
    """
    tttproc19 = subprocess.run(["scp", "./ttt/doc_ttt19/convdose.json",
        "pi@192.168.18.12:~/tt_doc/doc_txt19/Files19/convdose.json"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(tttproc19.stderr))
    if tttproc19.stderr == b'':
        print("[Upload] Patient 19 convdose.json uploaded.")
        messagebox.showinfo("INFO", "Patient 19 convdose.json uploaded.")
    else:
        print("[!] No file convdose.json for patient:19 to upload !")
        messagebox.showerror("Error", "No convdose.json for patient:19 to upload !")

def upload20stopttt():
    """
        Upload convdose.json to server.
    """
    tttproc20 = subprocess.run(["scp", "./ttt/doc_ttt20/convdose.json",
        "pi@192.168.18.12:~/tt_doc/doc_txt20/Files20/convdose.json"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(tttproc20.stderr))
    if tttproc20.stderr == b'':
        print("[Upload] Patient 20 convdose.json uploaded.")
        messagebox.showinfo("INFO", "Patient 20 convdose.json uploaded.")
    else:
        print("[!] No file convdose.json for patient:20 to upload !")
        messagebox.showerror("Error", "No convdose.json for patient:20 to upload !")

def upload21stopttt():
    """
        Upload convdose.json to server.
    """
    tttproc21 = subprocess.run(["scp", "./ttt/doc_ttt21/convdose.json",
        "pi@192.168.18.12:~/tt_doc/doc_txt21/Files21/convdose.json"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(tttproc21.stderr))
    if tttproc21.stderr == b'':
        print("[Upload] Patient 21 convdose.json uploaded.")
        messagebox.showinfo("INFO", "Patient 21 convdose.json uploaded.")
    else:
        print("[!] No file convdose.json for patient:21 to upload !")
        messagebox.showerror("Error", "No convdose.json for patient:21 to upload !")

def upload22stopttt():
    """
        Upload convdose.json to server.
    """
    tttproc22 = subprocess.run(["scp", "./ttt/doc_ttt22/convdose.json",
        "pi@192.168.18.12:~/tt_doc/doc_txt22/Files22/convdose.json"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(tttproc22.stderr))
    if tttproc22.stderr == b'':
        print("[Upload] Patient 22 convdose.json uploaded.")
        messagebox.showinfo("INFO", "Patient 22 convdose.json uploaded.")
    else:
        print("[!] No file convdose.json for patient:22 to upload !")
        messagebox.showerror("Error", "No convdose.json for patient:22 to upload !")

def upload23stopttt():
    """
        Upload convdose.json to server.
    """
    tttproc23 = subprocess.run(["scp", "./ttt/doc_ttt23/convdose.json",
        "pi@192.168.18.12:~/tt_doc/doc_txt23/Files23/convdose.json"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(tttproc23.stderr))
    if tttproc23.stderr == b'':
        print("[Upload] Patient 23 convdose.json uploaded.")
        messagebox.showinfo("INFO", "Patient 23 convdose.json uploaded.")
    else:
        print("[!] No file convdose.json for patient:23 to upload !")
        messagebox.showerror("Error", "No convdose.json for patient:23 to upload !")

def upload24stopttt():
    """
        Upload convdose.json to server.
    """
    tttproc24 = subprocess.run(["scp", "./ttt/doc_ttt24/convdose.json",
        "pi@192.168.18.12:~/tt_doc/doc_txt24/Files24/convdose.json"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(tttproc24.stderr))
    if tttproc24.stderr == b'':
        print("[Upload] Patient 24 convdose.json uploaded.")
        messagebox.showinfo("INFO", "Patient 24 convdose.json uploaded.")
    else:
        print("[!] No file convdose.json for patient:24 to upload !")
        messagebox.showerror("Error", "No convdose.json for patient:24 to upload !")
