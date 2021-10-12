#!/usr/bin/python3
# -*- coding : utf-8 -*-


"""
    Connecting the duration of progress bar
    with task = number of subprocess.
"""


from tkinter import messagebox
from ttt.bardownload import downloadatattt
import subprocess


def downloadttt1():
    """
        Download medication files from server before
        to start with medication interface.
    """
    downloadatattt()
    stoptttproc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt1/Files1/stopped_ttt.txt",
        "./ttt/doc_ttt/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(stoptttproc.stderr))
    if stoptttproc.stderr == b'':
        print("[download] File stopped_ttt.txt downloaded !")
        #messagebox.showinfo("INFO", "stopped_ttt.txt downloaded !")
    else:
        print("[!] No file stopped_ttt.txt to download from server !")
        messagebox.showwarning("Warning",
            "No stopped_ttt.txt to download from server !")

    introtttproc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt1/Files1/intro_ttt.txt",
        "./ttt/doc_ttt/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(introtttproc.stderr))
    if introtttproc.stderr == b'':
        print("[download] File intro_ttt.txt downloaded !")
        #messagebox.showinfo("INFO", "intro_ttt.txt downloaded !")
    else:
        print("[!] No file intro_ttt.txt to download from server !")
        messagebox.showwarning("Warning",
            "No intro_ttt.txt to download from server !")

    stoprproc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt1/Files1/stopped_res.txt",
        "./ttt/doc_ttt/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(stoprproc.stderr))
    if stoprproc.stderr == b'':
        print("[download] File stopped_res.txt downloaded !")
        #messagebox.showinfo("INFO", "stopped_res.txt downloaded !")
    else:
        print("[!] No file stopped_res.txt to download from server !")
        messagebox.showwarning("Warning",
            "No stopped_res.txt to download from server !")

    introrproc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt1/Files1/intro_res.txt",
        "./ttt/doc_ttt/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(introrproc.stderr))
    if introrproc.stderr == b'':
        print("[download] File intro_res.txt downloaded !")
        #messagebox.showinfo("INFO", "intro_res.txt downloaded !")
    else:
        print("[!] No file intro_res.txt to download from server !")
        messagebox.showwarning("Warning",
            "No intro_res.txt to download from server !")

    convdoseproc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt1/Files1/convdose.json",
        "./ttt/doc_ttt/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(convdoseproc.stderr))
    if convdoseproc.stderr == b'':
        print("[download] File convdose.json downloaded !")
        #messagebox.showinfo("INFO", "convdose.json downloaded !")
    else:
        print("[!] No convdose.json to download from server !")
        messagebox.showwarning("Warning",
            "No convdose.json to download from server !")

    convresproc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt1/Files1/convres.json",
        "./ttt/doc_ttt/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(convresproc.stderr))
    if convresproc.stderr == b'':
        print("[download] File convres.json downloaded !")
        #messagebox.showinfo("INFO", "convres.json downloaded !")
    else:
        print("[!] No file convres.json to download from server !")
        messagebox.showwarning("Warning",
            "No convres.json to download from server !")

def downloadttt2():
    """
        Download medication files from server before
        to start with medication interface.
    """
    downloadatattt()
    proc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt2/Files2/stopped_ttt.txt",
        "./ttt/doc_ttt2/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[download] File stopped_ttt.txt downloaded !")
        #messagebox.showinfo("INFO", "stopped_ttt.txt downloaded")
    else:
        print("[!] No file to download from server !")
        messagebox.showwarning("Warning",
            "No stopped_ttt.txt to download from server !")

    secproc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt2/Files2/convdose.json",
        "./ttt/doc_ttt2/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[download] File convdose.json downloaded !")
        #messagebox.showinfo("INFO", "convdose.json downloaded !")
    else:
        print("[!] No convdose.json to download from server !")
        messagebox.showwarning("Warning",
            "No convdose.json to download from server !")

    thirdproc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt2/Files2/stopped_res.txt",
        "./ttt/doc_ttt2/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(thirdproc.stderr))
    if thirdproc.stderr == b'':
        print("[download] File stopped_res.txt downloaded !")
        #messagebox.showinfo("INFO", "stopped_res.txt downloaded !")
    else:
        print("[!] No file to download from server !")
        messagebox.showwarning("Warning",
            "No stopped_res.txt to download from server !")

    forthproc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt2/Files2/convres.json",
        "./ttt/doc_ttt2/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(forthproc.stderr))
    if forthproc.stderr == b'':
        print("[download] File convres.json downloaded !")
        #messagebox.showinfo("INFO", "convres.json downloaded !")
    else:
        print("[!] No file to download from server !")
        messagebox.showwarning("Warning",
            "No convres.json to download from server !")

def downloadttt3():
    """
        Download medication files from server before
        to start with medication interface.
    """
    downloadatattt()
    proc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt3/Files3/stopped_ttt.txt",
        "./ttt/doc_ttt3/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[download] File stopped_ttt.txt downloaded !")
        #messagebox.showinfo("INFO", "stopped_ttt.txt downloaded")
    else:
        print("[!] No file to download from server !")
        messagebox.showwarning("Warning",
            "No stopped_ttt.txt to download from server !")

    secproc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt3/Files3/convdose.json",
        "./ttt/doc_ttt3/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[download] File convdose.json downloaded !")
        #messagebox.showinfo("INFO", "convdose.json downloaded !")
    else:
        print("[!] No convdose.json to download from server !")
        messagebox.showwarning("Warning",
            "No convdose.json to download from server !")

    thirdproc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt3/Files3/stopped_res.txt",
        "./ttt/doc_ttt3/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(thirdproc.stderr))
    if thirdproc.stderr == b'':
        print("[download] File stopped_res.txt downloaded !")
        #messagebox.showinfo("INFO", "stopped_res.txt downloaded !")
    else:
        print("[!] No file to download from server !")
        messagebox.showwarning("Warning",
            "No stopped_res.txt to download from server !")

    forthproc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt3/Files3/convres.json",
        "./ttt/doc_ttt3/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(forthproc.stderr))
    if forthproc.stderr == b'':
        print("[download] File convres.json downloaded !")
        #messagebox.showinfo("INFO", "convres.json downloaded !")
    else:
        print("[!] No file to download from server !")
        messagebox.showwarning("Warning",
            "No convres.json to download from server !")

def downloadttt4():
    """
        Download medication files from server before
        to start with medication interface.
    """
    downloadatattt()
    proc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt4/Files4/stopped_ttt.txt",
        "./ttt/doc_ttt4/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[download] File stopped_ttt.txt downloaded !")
        #messagebox.showinfo("INFO", "stopped_ttt.txt downloaded")
    else:
        print("[!] No file to download from server !")
        messagebox.showwarning("Warning",
            "No stopped_ttt.txt to download from server !")

    secproc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt4/Files4/convdose.json",
        "./ttt/doc_ttt4/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[download] File convdose.json downloaded !")
        #messagebox.showinfo("INFO", "convdose.json downloaded !")
    else:
        print("[!] No convdose.json to download from server !")
        messagebox.showwarning("Warning",
            "No convdose.json to download from server !")

    thirdproc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt4/Files4/stopped_res.txt",
        "./ttt/doc_ttt4/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(thirdproc.stderr))
    if thirdproc.stderr == b'':
        print("[download] File stopped_res.txt downloaded !")
        #messagebox.showinfo("INFO", "stopped_res.txt downloaded !")
    else:
        print("[!] No file to download from server !")
        messagebox.showwarning("Warning",
            "No stopped_res.txt to download from server !")

    forthproc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt4/Files4/convres.json",
        "./ttt/doc_ttt4/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(forthproc.stderr))
    if forthproc.stderr == b'':
        print("[download] File convres.json downloaded !")
        #messagebox.showinfo("INFO", "convres.json downloaded !")
    else:
        print("[!] No file to download from server !")
        messagebox.showwarning("Warning",
            "No convres.json to download from server !")

def downloadttt5():
    """
        Download medication files from server before
        to start with medication interface.
    """
    downloadatattt()
    proc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt5/Files5/stopped_ttt.txt",
        "./ttt/doc_ttt5/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[download] File stopped_ttt.txt downloaded !")
        #messagebox.showinfo("INFO", "stopped_ttt.txt downloaded")
    else:
        print("[!] No file to download from server !")
        messagebox.showwarning("Warning",
            "No stopped_ttt.txt to download from server !")

    secproc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt5/Files5/convdose.json",
        "./ttt/doc_ttt5/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[download] File convdose.json downloaded !")
        #messagebox.showinfo("INFO", "convdose.json downloaded !")
    else:
        print("[!] No convdose.json to download from server !")
        messagebox.showwarning("Warning",
            "No convdose.json to download from server !")

    thirdproc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt5/Files5/stopped_res.txt",
        "./ttt/doc_ttt5/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(thirdproc.stderr))
    if thirdproc.stderr == b'':
        print("[download] File stopped_res.txt downloaded !")
        #messagebox.showinfo("INFO", "stopped_res.txt downloaded !")
    else:
        print("[!] No file to download from server !")
        messagebox.showwarning("Warning",
            "No stopped_res.txt to download from server !")

    forthproc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt5/Files5/convres.json",
        "./ttt/doc_ttt5/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(forthproc.stderr))
    if forthproc.stderr == b'':
        print("[download] File convres.json downloaded !")
        #messagebox.showinfo("INFO", "convres.json downloaded !")
    else:
        print("[!] No file to download from server !")
        messagebox.showwarning("Warning",
            "No convres.json to download from server !")

def downloadttt6():
    """
        Download medication files from server before
        to start with medication interface.
    """
    downloadatattt()
    proc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt6/Files6/stopped_ttt.txt",
        "./ttt/doc_ttt6/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[download] File stopped_ttt.txt downloaded !")
        #messagebox.showinfo("INFO", "stopped_ttt.txt downloaded")
    else:
        print("[!] No file to download from server !")
        messagebox.showwarning("Warning",
            "No stopped_ttt.txt to download from server !")

    secproc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt6/Files6/convdose.json",
        "./ttt/doc_ttt6/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[download] File convdose.json downloaded !")
        #messagebox.showinfo("INFO", "convdose.json downloaded !")
    else:
        print("[!] No convdose.json to download from server !")
        messagebox.showwarning("Warning",
            "No convdose.json to download from server !")

    thirdproc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt6/Files6/stopped_res.txt",
        "./ttt/doc_ttt6/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(thirdproc.stderr))
    if thirdproc.stderr == b'':
        print("[download] File stopped_res.txt downloaded !")
        #messagebox.showinfo("INFO", "stopped_res.txt downloaded !")
    else:
        print("[!] No file to download from server !")
        messagebox.showwarning("Warning",
            "No stopped_res.txt to download from server !")

    forthproc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt6/Files6/convres.json",
        "./ttt/doc_ttt6/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(forthproc.stderr))
    if forthproc.stderr == b'':
        print("[download] File convres.json downloaded !")
        #messagebox.showinfo("INFO", "convres.json downloaded !")
    else:
        print("[!] No file to download from server !")
        messagebox.showwarning("Warning",
            "No convres.json to download from server !")

def downloadttt7():
    """
        Download medication files from server before
        to start with medication interface.
    """
    downloadatattt()
    proc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt7/Files7/stopped_ttt.txt",
        "./ttt/doc_ttt7/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[download] File stopped_ttt.txt downloaded !")
        #messagebox.showinfo("INFO", "stopped_ttt.txt downloaded")
    else:
        print("[!] No file to download from server !")
        messagebox.showwarning("Warning",
            "No stopped_ttt.txt to download from server !")

    secproc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt7/Files7/convdose.json",
        "./ttt/doc_ttt7/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[download] File convdose.json downloaded !")
        #messagebox.showinfo("INFO", "convdose.json downloaded !")
    else:
        print("[!] No convdose.json to download from server !")
        messagebox.showwarning("Warning",
            "No convdose.json to download from server !")

    thirdproc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt7/Files7/stopped_res.txt",
        "./ttt/doc_ttt7/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(thirdproc.stderr))
    if thirdproc.stderr == b'':
        print("[download] File stopped_res.txt downloaded !")
        #messagebox.showinfo("INFO", "stopped_res.txt downloaded !")
    else:
        print("[!] No file to download from server !")
        messagebox.showwarning("Warning",
            "No stopped_res.txt to download from server !")

    forthproc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt7/Files7/convres.json",
        "./ttt/doc_ttt7/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(forthproc.stderr))
    if forthproc.stderr == b'':
        print("[download] File convres.json downloaded !")
        #messagebox.showinfo("INFO", "convres.json downloaded !")
    else:
        print("[!] No file to download from server !")
        messagebox.showwarning("Warning",
            "No convres.json to download from server !")

def downloadttt8():
    """
        Download medication files from server before
        to start with medication interface.
    """
    downloadatattt()
    proc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt8/Files8/stopped_ttt.txt",
        "./ttt/doc_ttt8/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[download] File stopped_ttt.txt downloaded !")
        #messagebox.showinfo("INFO", "stopped_ttt.txt downloaded")
    else:
        print("[!] No file to download from server !")
        messagebox.showwarning("Warning",
            "No stopped_ttt.txt to download from server !")

    secproc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt8/Files8/convdose.json",
        "./ttt/doc_ttt8/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[download] File convdose.json downloaded !")
        #messagebox.showinfo("INFO", "convdose.json downloaded !")
    else:
        print("[!] No convdose.json to download from server !")
        messagebox.showwarning("Warning",
            "No convdose.json to download from server !")

    thirdproc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt8/Files8/stopped_res.txt",
        "./ttt/doc_ttt8/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(thirdproc.stderr))
    if thirdproc.stderr == b'':
        print("[download] File stopped_res.txt downloaded !")
        #messagebox.showinfo("INFO", "stopped_res.txt downloaded !")
    else:
        print("[!] No file to download from server !")
        messagebox.showwarning("Warning",
            "No stopped_res.txt to download from server !")

    forthproc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt8/Files8/convres.json",
        "./ttt/doc_ttt8/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(forthproc.stderr))
    if forthproc.stderr == b'':
        print("[download] File convres.json downloaded !")
        #messagebox.showinfo("INFO", "convres.json downloaded !")
    else:
        print("[!] No file to download from server !")
        messagebox.showwarning("Warning",
            "No convres.json to download from server !")

def downloadttt9():
    """
        Download medication files from server before
        to start with medication interface.
    """
    downloadatattt()
    proc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt9/Files9/stopped_ttt.txt",
        "./ttt/doc_ttt9/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[download] File stopped_ttt.txt downloaded !")
        #messagebox.showinfo("INFO", "stopped_ttt.txt downloaded")
    else:
        print("[!] No file to download from server !")
        messagebox.showwarning("Warning",
            "No stopped_ttt.txt to download from server !")

    secproc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt9/Files9/convdose.json",
        "./ttt/doc_ttt9/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[download] File convdose.json downloaded !")
        #messagebox.showinfo("INFO", "convdose.json downloaded !")
    else:
        print("[!] No convdose.json to download from server !")
        messagebox.showwarning("Warning",
            "No convdose.json to download from server !")

    thirdproc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt9/Files9/stopped_res.txt",
        "./ttt/doc_ttt9/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(thirdproc.stderr))
    if thirdproc.stderr == b'':
        print("[download] File stopped_res.txt downloaded !")
        #messagebox.showinfo("INFO", "stopped_res.txt downloaded !")
    else:
        print("[!] No file to download from server !")
        messagebox.showwarning("Warning",
            "No stopped_res.txt to download from server !")

    forthproc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt9/Files9/convres.json",
        "./ttt/doc_ttt9/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(forthproc.stderr))
    if forthproc.stderr == b'':
        print("[download] File convres.json downloaded !")
        #messagebox.showinfo("INFO", "convres.json downloaded !")
    else:
        print("[!] No file to download from server !")
        messagebox.showwarning("Warning",
            "No convres.json to download from server !")

def downloadttt10():
    """
        Download medication files from server before
        to start with medication interface.
    """
    downloadatattt()
    proc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt10/Files10/stopped_ttt.txt",
        "./ttt/doc_ttt10/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[download] File stopped_ttt.txt downloaded !")
        #messagebox.showinfo("INFO", "stopped_ttt.txt downloaded")
    else:
        print("[!] No file to download from server !")
        messagebox.showwarning("Warning",
            "No stopped_ttt.txt to download from server !")

    secproc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt10/Files10/convdose.json",
        "./ttt/doc_ttt10/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[download] File convdose.json downloaded !")
        #messagebox.showinfo("INFO", "convdose.json downloaded !")
    else:
        print("[!] No convdose.json to download from server !")
        messagebox.showwarning("Warning",
            "No convdose.json to download from server !")

    thirdproc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt10/Files10/stopped_res.txt",
        "./ttt/doc_ttt10/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(thirdproc.stderr))
    if thirdproc.stderr == b'':
        print("[download] File stopped_res.txt downloaded !")
        #messagebox.showinfo("INFO", "stopped_res.txt downloaded !")
    else:
        print("[!] No file to download from server !")
        messagebox.showwarning("Warning",
            "No stopped_res.txt to download from server !")

    forthproc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt10/Files10/convres.json",
        "./ttt/doc_ttt10/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(forthproc.stderr))
    if forthproc.stderr == b'':
        print("[download] File convres.json downloaded !")
        #messagebox.showinfo("INFO", "convres.json downloaded !")
    else:
        print("[!] No file to download from server !")
        messagebox.showwarning("Warning",
            "No convres.json to download from server !")

def downloadttt11():
    """
        Download medication files from server before
        to start with medication interface.
    """
    downloadatattt()
    proc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt11/Files11/stopped_ttt.txt",
        "./ttt/doc_ttt11/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[download] File stopped_ttt.txt downloaded !")
        #messagebox.showinfo("INFO", "stopped_ttt.txt downloaded")
    else:
        print("[!] No file to download from server !")
        messagebox.showwarning("Warning",
            "No stopped_ttt.txt to download from server !")

    secproc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt11/Files11/convdose.json",
        "./ttt/doc_ttt11/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[download] File convdose.json downloaded !")
        #messagebox.showinfo("INFO", "convdose.json downloaded !")
    else:
        print("[!] No convdose.json to download from server !")
        messagebox.showwarning("Warning",
            "No convdose.json to download from server !")

    thirdproc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt11/Files11/stopped_res.txt",
        "./ttt/doc_ttt11/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(thirdproc.stderr))
    if thirdproc.stderr == b'':
        print("[download] File stopped_res.txt downloaded !")
        #messagebox.showinfo("INFO", "stopped_res.txt downloaded !")
    else:
        print("[!] No file to download from server !")
        messagebox.showwarning("Warning",
            "No stopped_res.txt to download from server !")

    forthproc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt11/Files11/convres.json",
        "./ttt/doc_ttt11/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(forthproc.stderr))
    if forthproc.stderr == b'':
        print("[download] File convres.json downloaded !")
        #messagebox.showinfo("INFO", "convres.json downloaded !")
    else:
        print("[!] No file to download from server !")
        messagebox.showwarning("Warning",
            "No convres.json to download from server !")

def downloadttt12():
    """
        Download medication files from server before
        to start with medication interface.
    """
    downloadatattt()
    proc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt12/Files12/stopped_ttt.txt",
        "./ttt/doc_ttt12/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[download] File stopped_ttt.txt downloaded !")
        #messagebox.showinfo("INFO", "stopped_ttt.txt downloaded")
    else:
        print("[!] No file to download from server !")
        messagebox.showwarning("Warning",
            "No stopped_ttt.txt to download from server !")

    secproc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt12/Files12/convdose.json",
        "./ttt/doc_ttt12/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[download] File convdose.json downloaded !")
        #messagebox.showinfo("INFO", "convdose.json downloaded !")
    else:
        print("[!] No convdose.json to download from server !")
        messagebox.showwarning("Warning",
            "No convdose.json to download from server !")

    thirdproc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt12/Files12/stopped_res.txt",
        "./ttt/doc_ttt12/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(thirdproc.stderr))
    if thirdproc.stderr == b'':
        print("[download] File stopped_res.txt downloaded !")
        #messagebox.showinfo("INFO", "stopped_res.txt downloaded !")
    else:
        print("[!] No file to download from server !")
        messagebox.showwarning("Warning",
            "No stopped_res.txt to download from server !")

    forthproc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt12/Files12/convres.json",
        "./ttt/doc_ttt12/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(forthproc.stderr))
    if forthproc.stderr == b'':
        print("[download] File convres.json downloaded !")
        #messagebox.showinfo("INFO", "convres.json downloaded !")
    else:
        print("[!] No file to download from server !")
        messagebox.showwarning("Warning",
            "No convres.json to download from server !")

def downloadttt13():
    """
        Download medication files from server before
        to start with medication interface.
    """
    downloadatattt()
    proc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt13/Files13/stopped_ttt.txt",
        "./ttt/doc_ttt13/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[download] File stopped_ttt.txt downloaded !")
        #messagebox.showinfo("INFO", "stopped_ttt.txt downloaded")
    else:
        print("[!] No file to download from server !")
        messagebox.showwarning("Warning",
            "No stopped_ttt.txt to download from server !")

    secproc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt13/Files13/convdose.json",
        "./ttt/doc_ttt13/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[download] File convdose.json downloaded !")
        #messagebox.showinfo("INFO", "convdose.json downloaded !")
    else:
        print("[!] No convdose.json to download from server !")
        messagebox.showwarning("Warning",
            "No convdose.json to download from server !")

    thirdproc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt13/Files13/stopped_res.txt",
        "./ttt/doc_ttt13/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(thirdproc.stderr))
    if thirdproc.stderr == b'':
        print("[download] File stopped_res.txt downloaded !")
        #messagebox.showinfo("INFO", "stopped_res.txt downloaded !")
    else:
        print("[!] No file to download from server !")
        messagebox.showwarning("Warning",
            "No stopped_res.txt to download from server !")

    forthproc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt13/Files13/convres.json",
        "./ttt/doc_ttt13/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(forthproc.stderr))
    if forthproc.stderr == b'':
        print("[download] File convres.json downloaded !")
        #messagebox.showinfo("INFO", "convres.json downloaded !")
    else:
        print("[!] No file to download from server !")
        messagebox.showwarning("Warning",
            "No convres.json to download from server !")

def downloadttt14():
    """
        Download medication files from server before
        to start with medication interface.
    """
    downloadatattt()
    proc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt14/Files14/stopped_ttt.txt",
        "./ttt/doc_ttt14/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[download] File stopped_ttt.txt downloaded !")
        #messagebox.showinfo("INFO", "stopped_ttt.txt downloaded")
    else:
        print("[!] No file to download from server !")
        messagebox.showwarning("Warning",
            "No stopped_ttt.txt to download from server !")

    secproc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt14/Files14/convdose.json",
        "./ttt/doc_ttt14/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[download] File convdose.json downloaded !")
        #messagebox.showinfo("INFO", "convdose.json downloaded !")
    else:
        print("[!] No convdose.json to download from server !")
        messagebox.showwarning("Warning",
            "No convdose.json to download from server !")

    thirdproc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt14/Files14/stopped_res.txt",
        "./ttt/doc_ttt14/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(thirdproc.stderr))
    if thirdproc.stderr == b'':
        print("[download] File stopped_res.txt downloaded !")
        #messagebox.showinfo("INFO", "stopped_res.txt downloaded !")
    else:
        print("[!] No file to download from server !")
        messagebox.showwarning("Warning",
            "No stopped_res.txt to download from server !")

    forthproc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt14/Files14/convres.json",
        "./ttt/doc_ttt14/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(forthproc.stderr))
    if forthproc.stderr == b'':
        print("[download] File convres.json downloaded !")
        #messagebox.showinfo("INFO", "convres.json downloaded !")
    else:
        print("[!] No file to download from server !")
        messagebox.showwarning("Warning",
            "No convres.json to download from server !")

def downloadttt15():
    """
        Download medication files from server before
        to start with medication interface.
    """
    downloadatattt()
    proc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt15/Files15/stopped_ttt.txt",
        "./ttt/doc_ttt15/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[download] File stopped_ttt.txt downloaded !")
        #messagebox.showinfo("INFO", "stopped_ttt.txt downloaded")
    else:
        print("[!] No file to download from server !")
        messagebox.showwarning("Warning",
            "No stopped_ttt.txt to download from server !")

    secproc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt15/Files15/convdose.json",
        "./ttt/doc_ttt15/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[download] File convdose.json downloaded !")
        #messagebox.showinfo("INFO", "convdose.json downloaded !")
    else:
        print("[!] No convdose.json to download from server !")
        messagebox.showwarning("Warning",
            "No convdose.json to download from server !")

    thirdproc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt15/Files15/stopped_res.txt",
        "./ttt/doc_ttt15/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(thirdproc.stderr))
    if thirdproc.stderr == b'':
        print("[download] File stopped_res.txt downloaded !")
        #messagebox.showinfo("INFO", "stopped_res.txt downloaded !")
    else:
        print("[!] No file to download from server !")
        messagebox.showwarning("Warning",
            "No stopped_res.txt to download from server !")

    forthproc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt15/Files15/convres.json",
        "./ttt/doc_ttt15/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(forthproc.stderr))
    if forthproc.stderr == b'':
        print("[download] File convres.json downloaded !")
        #messagebox.showinfo("INFO", "convres.json downloaded !")
    else:
        print("[!] No file to download from server !")
        messagebox.showwarning("Warning",
            "No convres.json to download from server !")

def downloadttt16():
    """
        Download medication files from server before
        to start with medication interface.
    """
    downloadatattt()
    proc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt16/Files16/stopped_ttt.txt",
        "./ttt/doc_ttt16/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[download] File stopped_ttt.txt downloaded !")
        #messagebox.showinfo("INFO", "stopped_ttt.txt downloaded")
    else:
        print("[!] No file to download from server !")
        messagebox.showwarning("Warning",
            "No stopped_ttt.txt to download from server !")

    secproc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt16/Files16/convdose.json",
        "./ttt/doc_ttt16/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[download] File convdose.json downloaded !")
        #messagebox.showinfo("INFO", "convdose.json downloaded !")
    else:
        print("[!] No convdose.json to download from server !")
        messagebox.showwarning("Warning",
            "No convdose.json to download from server !")

    thirdproc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt16/Files16/stopped_res.txt",
        "./ttt/doc_ttt16/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(thirdproc.stderr))
    if thirdproc.stderr == b'':
        print("[download] File stopped_res.txt downloaded !")
        #messagebox.showinfo("INFO", "stopped_res.txt downloaded !")
    else:
        print("[!] No file to download from server !")
        messagebox.showwarning("Warning",
            "No stopped_res.txt to download from server !")

    forthproc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt16/Files16/convres.json",
        "./ttt/doc_ttt16/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(forthproc.stderr))
    if forthproc.stderr == b'':
        print("[download] File convres.json downloaded !")
        #messagebox.showinfo("INFO", "convres.json downloaded !")
    else:
        print("[!] No file to download from server !")
        messagebox.showwarning("Warning",
            "No convres.json to download from server !")

def downloadttt17():
    """
        Download medication files from server before
        to start with medication interface.
    """
    downloadatattt()
    proc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt17/Files17/stopped_ttt.txt",
        "./ttt/doc_ttt17/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[download] File stopped_ttt.txt downloaded !")
        #messagebox.showinfo("INFO", "stopped_ttt.txt downloaded")
    else:
        print("[!] No file to download from server !")
        messagebox.showwarning("Warning",
            "No stopped_ttt.txt to download from server !")

    secproc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt17/Files17/convdose.json",
        "./ttt/doc_ttt17/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[download] File convdose.json downloaded !")
        #messagebox.showinfo("INFO", "convdose.json downloaded !")
    else:
        print("[!] No convdose.json to download from server !")
        messagebox.showwarning("Warning",
            "No convdose.json to download from server !")

    thirdproc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt17/Files17/stopped_res.txt",
        "./ttt/doc_ttt17/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(thirdproc.stderr))
    if thirdproc.stderr == b'':
        print("[download] File stopped_res.txt downloaded !")
        #messagebox.showinfo("INFO", "stopped_res.txt downloaded !")
    else:
        print("[!] No file to download from server !")
        messagebox.showwarning("Warning",
            "No stopped_res.txt to download from server !")

    forthproc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt17/Files17/convres.json",
        "./ttt/doc_ttt17/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(forthproc.stderr))
    if forthproc.stderr == b'':
        print("[download] File convres.json downloaded !")
        #messagebox.showinfo("INFO", "convres.json downloaded !")
    else:
        print("[!] No file to download from server !")
        messagebox.showwarning("Warning",
            "No convres.json to download from server !")

def downloadttt18():
    """
        Download medication files from server before
        to start with medication interface.
    """
    downloadatattt()
    proc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt18/Files18/stopped_ttt.txt",
        "./ttt/doc_ttt18/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[download] File stopped_ttt.txt downloaded !")
        #messagebox.showinfo("INFO", "stopped_ttt.txt downloaded")
    else:
        print("[!] No file to download from server !")
        messagebox.showwarning("Warning",
            "No stopped_ttt.txt to download from server !")

    secproc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt18/Files18/convdose.json",
        "./ttt/doc_ttt18/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[download] File convdose.json downloaded !")
        #messagebox.showinfo("INFO", "convdose.json downloaded !")
    else:
        print("[!] No convdose.json to download from server !")
        messagebox.showwarning("Warning",
            "No convdose.json to download from server !")

    thirdproc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt18/Files18/stopped_res.txt",
        "./ttt/doc_ttt18/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(thirdproc.stderr))
    if thirdproc.stderr == b'':
        print("[download] File stopped_res.txt downloaded !")
        #messagebox.showinfo("INFO", "stopped_res.txt downloaded !")
    else:
        print("[!] No file to download from server !")
        messagebox.showwarning("Warning",
            "No stopped_res.txt to download from server !")

    forthproc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt18/Files18/convres.json",
        "./ttt/doc_ttt18/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(forthproc.stderr))
    if forthproc.stderr == b'':
        print("[download] File convres.json downloaded !")
        #messagebox.showinfo("INFO", "convres.json downloaded !")
    else:
        print("[!] No file to download from server !")
        messagebox.showwarning("Warning",
            "No convres.json to download from server !")

def downloadttt19():
    """
        Download medication files from server before
        to start with medication interface.
    """
    downloadatattt()
    proc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt19/Files19/stopped_ttt.txt",
        "./ttt/doc_ttt19/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[download] File stopped_ttt.txt downloaded !")
        #messagebox.showinfo("INFO", "stopped_ttt.txt downloaded")
    else:
        print("[!] No file to download from server !")
        messagebox.showwarning("Warning",
            "No stopped_ttt.txt to download from server !")

    secproc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt19/Files19/convdose.json",
        "./ttt/doc_ttt19/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[download] File convdose.json downloaded !")
        #messagebox.showinfo("INFO", "convdose.json downloaded !")
    else:
        print("[!] No convdose.json to download from server !")
        messagebox.showwarning("Warning",
            "No convdose.json to download from server !")

    thirdproc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt19/Files19/stopped_res.txt",
        "./ttt/doc_ttt19/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(thirdproc.stderr))
    if thirdproc.stderr == b'':
        print("[download] File stopped_res.txt downloaded !")
        #messagebox.showinfo("INFO", "stopped_res.txt downloaded !")
    else:
        print("[!] No file to download from server !")
        messagebox.showwarning("Warning",
            "No stopped_res.txt to download from server !")

    forthproc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt19/Files19/convres.json",
        "./ttt/doc_ttt19/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(forthproc.stderr))
    if forthproc.stderr == b'':
        print("[download] File convres.json downloaded !")
        #messagebox.showinfo("INFO", "convres.json downloaded !")
    else:
        print("[!] No file to download from server !")
        messagebox.showwarning("Warning",
            "No convres.json to download from server !")

def downloadttt20():
    """
        Download medication files from server before
        to start with medication interface.
    """
    downloadatattt()
    proc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt20/Files20/stopped_ttt.txt",
        "./ttt/doc_ttt20/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[download] File stopped_ttt.txt downloaded !")
        #messagebox.showinfo("INFO", "stopped_ttt.txt downloaded")
    else:
        print("[!] No file to download from server !")
        messagebox.showwarning("Warning",
            "No stopped_ttt.txt to download from server !")

    secproc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt20/Files20/convdose.json",
        "./ttt/doc_ttt20/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[download] File convdose.json downloaded !")
        #messagebox.showinfo("INFO", "convdose.json downloaded !")
    else:
        print("[!] No convdose.json to download from server !")
        messagebox.showwarning("Warning",
            "No convdose.json to download from server !")

    thirdproc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt20/Files20/stopped_res.txt",
        "./ttt/doc_ttt20/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(thirdproc.stderr))
    if thirdproc.stderr == b'':
        print("[download] File stopped_res.txt downloaded !")
        #messagebox.showinfo("INFO", "stopped_res.txt downloaded !")
    else:
        print("[!] No file to download from server !")
        messagebox.showwarning("Warning",
            "No stopped_res.txt to download from server !")

    forthproc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt20/Files20/convres.json",
        "./ttt/doc_ttt20/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(forthproc.stderr))
    if forthproc.stderr == b'':
        print("[download] File convres.json downloaded !")
        #messagebox.showinfo("INFO", "convres.json downloaded !")
    else:
        print("[!] No file to download from server !")
        messagebox.showwarning("Warning",
            "No convres.json to download from server !")

def downloadttt21():
    """
        Download medication files from server before
        to start with medication interface.
    """
    downloadatattt()
    proc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt21/Files21/stopped_ttt.txt",
        "./ttt/doc_ttt21/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[download] File stopped_ttt.txt downloaded !")
        #messagebox.showinfo("INFO", "stopped_ttt.txt downloaded")
    else:
        print("[!] No file to download from server !")
        messagebox.showwarning("Warning",
            "No stopped_ttt.txt to download from server !")

    secproc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt21/Files21/convdose.json",
        "./ttt/doc_ttt21/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[download] File convdose.json downloaded !")
        #messagebox.showinfo("INFO", "convdose.json downloaded !")
    else:
        print("[!] No convdose.json to download from server !")
        messagebox.showwarning("Warning",
            "No convdose.json to download from server !")

    thirdproc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt21/Files21/stopped_res.txt",
        "./ttt/doc_ttt21/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(thirdproc.stderr))
    if thirdproc.stderr == b'':
        print("[download] File stopped_res.txt downloaded !")
        #messagebox.showinfo("INFO", "stopped_res.txt downloaded !")
    else:
        print("[!] No file to download from server !")
        messagebox.showwarning("Warning",
            "No stopped_res.txt to download from server !")

    forthproc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt21/Files21/convres.json",
        "./ttt/doc_ttt21/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(forthproc.stderr))
    if forthproc.stderr == b'':
        print("[download] File convres.json downloaded !")
        #messagebox.showinfo("INFO", "convres.json downloaded !")
    else:
        print("[!] No file to download from server !")
        messagebox.showwarning("Warning",
            "No convres.json to download from server !")

def downloadttt22():
    """
        Download medication files from server before
        to start with medication interface.
    """
    downloadatattt()
    proc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt22/Files22/stopped_ttt.txt",
        "./ttt/doc_ttt22/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[download] File stopped_ttt.txt downloaded !")
        #messagebox.showinfo("INFO", "stopped_ttt.txt downloaded")
    else:
        print("[!] No file to download from server !")
        messagebox.showwarning("Warning",
            "No stopped_ttt.txt to download from server !")

    secproc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt22/Files22/convdose.json",
        "./ttt/doc_ttt22/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[download] File convdose.json downloaded !")
        #messagebox.showinfo("INFO", "convdose.json downloaded !")
    else:
        print("[!] No convdose.json to download from server !")
        messagebox.showwarning("Warning",
            "No convdose.json to download from server !")

    thirdproc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt22/Files22/stopped_res.txt",
        "./ttt/doc_ttt22/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(thirdproc.stderr))
    if thirdproc.stderr == b'':
        print("[download] File stopped_res.txt downloaded !")
        #messagebox.showinfo("INFO", "stopped_res.txt downloaded !")
    else:
        print("[!] No file to download from server !")
        messagebox.showwarning("Warning",
            "No stopped_res.txt to download from server !")

    forthproc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt22/Files22/convres.json",
        "./ttt/doc_ttt22/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(forthproc.stderr))
    if forthproc.stderr == b'':
        print("[download] File convres.json downloaded !")
        #messagebox.showinfo("INFO", "convres.json downloaded !")
    else:
        print("[!] No file to download from server !")
        messagebox.showwarning("Warning",
            "No convres.json to download from server !")

def downloadttt23():
    """
        Download medication files from server before
        to start with medication interface.
    """
    downloadatattt()
    proc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt23/Files23/stopped_ttt.txt",
        "./ttt/doc_ttt23/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[download] File stopped_ttt.txt downloaded !")
        #messagebox.showinfo("INFO", "stopped_ttt.txt downloaded")
    else:
        print("[!] No file to download from server !")
        messagebox.showwarning("Warning",
            "No stopped_ttt.txt to download from server !")

    secproc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt23/Files23/convdose.json",
        "./ttt/doc_ttt23/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[download] File convdose.json downloaded !")
        #messagebox.showinfo("INFO", "convdose.json downloaded !")
    else:
        print("[!] No convdose.json to download from server !")
        messagebox.showwarning("Warning",
            "No convdose.json to download from server !")

    thirdproc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt23/Files23/stopped_res.txt",
        "./ttt/doc_ttt23/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(thirdproc.stderr))
    if thirdproc.stderr == b'':
        print("[download] File stopped_res.txt downloaded !")
        #messagebox.showinfo("INFO", "stopped_res.txt downloaded !")
    else:
        print("[!] No file to download from server !")
        messagebox.showwarning("Warning",
            "No stopped_res.txt to download from server !")

    forthproc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt23/Files23/convres.json",
        "./ttt/doc_ttt23/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(forthproc.stderr))
    if forthproc.stderr == b'':
        print("[download] File convres.json downloaded !")
        #messagebox.showinfo("INFO", "convres.json downloaded !")
    else:
        print("[!] No file to download from server !")
        messagebox.showwarning("Warning",
            "No convres.json to download from server !")

def downloadttt24():
    """
        Download medication files from server before
        to start with medication interface.
    """
    downloadatattt()
    proc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt24/Files24/stopped_ttt.txt",
        "./ttt/doc_ttt24/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[download] File stopped_ttt.txt downloaded !")
        #messagebox.showinfo("INFO", "stopped_ttt.txt downloaded")
    else:
        print("[!] No file to download from server !")
        messagebox.showwarning("Warning",
            "No stopped_ttt.txt to download from server !")

    secproc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt24/Files24/convdose.json",
        "./ttt/doc_ttt24/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[download] File convdose.json downloaded !")
        #messagebox.showinfo("INFO", "convdose.json downloaded !")
    else:
        print("[!] No convdose.json to download from server !")
        messagebox.showwarning("Warning",
            "No convdose.json to download from server !")

    thirdproc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt24/Files24/stopped_res.txt",
        "./ttt/doc_ttt24/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(thirdproc.stderr))
    if thirdproc.stderr == b'':
        print("[download] File stopped_res.txt downloaded !")
        #messagebox.showinfo("INFO", "stopped_res.txt downloaded !")
    else:
        print("[!] No file to download from server !")
        messagebox.showwarning("Warning",
            "No stopped_res.txt to download from server !")

    forthproc = subprocess.run(["scp",
        "pi@192.168.18.12:~/tt_doc/doc_txt24/Files24/convres.json",
        "./ttt/doc_ttt24/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(forthproc.stderr))
    if forthproc.stderr == b'':
        print("[download] File convres.json downloaded !")
        #messagebox.showinfo("INFO", "convres.json downloaded !")
    else:
        print("[!] No file to download from server !")
        messagebox.showwarning("Warning",
            "No convres.json to download from server !")
