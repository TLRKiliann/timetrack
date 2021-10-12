#!/usr/bin/python3
# -*- coding: utf-8 -*-


from tkinter import messagebox
import os
import subprocess


def uploadstopres():
    """
        Upload convres.json to server.
    """
    resproc = subprocess.run(["scp", "./ttt/doc_ttt/convres.json",
        "pi@192.168.18.12:~/tt_doc/doc_txt1/Files1/convres.json"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(resproc.stderr))
    if resproc.stderr == b'':
        print("[Upload] Patient 1 convres.json uploaded !")
        messagebox.showinfo("INFO", "Patient 1 convres.json uploaded...")
    else:
        print("[!] No file convres.json for patient:1 to upload !")
        messagebox.showerror("Error", "No convres.json for patient:1 to upload...")

def upload2stopres():
    """
        Upload convres.json to server.
    """
    res2proc = subprocess.run(["scp", "./ttt/doc_ttt2/convres.json",
        "pi@192.168.18.12:~/tt_doc/doc_txt2/Files2/convres.json"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(res2proc.stderr))
    if res2proc.stderr == b'':
        print("[Upload] Patient 2 convres.json uploaded !")
        messagebox.showinfo("INFO", "Patient 2 convres.json uploaded...")
    else:
        print("[!] No file convres.json for patient:2 to upload !")
        messagebox.showerror("Error", "No convres.json for patient:2 to upload...")

def upload3stopres():
    """
        Upload convres.json to server.
    """
    res3proc = subprocess.run(["scp", "./ttt/doc_ttt3/convres.json",
        "pi@192.168.18.12:~/tt_doc/doc_txt3/Files3/convres.json"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(res3proc.stderr))
    if res3proc.stderr == b'':
        print("[Upload] Patient 3 convres.json uploaded !")
        messagebox.showinfo("INFO", "Patient 3 convres.json uploaded...")
    else:
        print("[!] No file convres.json for patient:3 to upload !")
        messagebox.showerror("Error", "No convres.json for patient:3 to upload...")

def upload4stopres():
    """
        Upload convres.json to server.
    """
    res4proc = subprocess.run(["scp", "./ttt/doc_ttt4/convres.json",
        "pi@192.168.18.12:~/tt_doc/doc_txt4/Files4/convres.json"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(res4proc.stderr))
    if res4proc.stderr == b'':
        print("[Upload] Patient 4 convres.json uploaded !")
        messagebox.showinfo("INFO", "Patient 4 convres.json uploaded...")
    else:
        print("[!] No file convres.json for patient:4 to upload !")
        messagebox.showerror("Error", "No convres.json for patient:4 to upload...")

def upload5stopres():
    """
        Upload convres.json to server.
    """
    res5proc = subprocess.run(["scp", "./ttt/doc_ttt5/convres.json",
        "pi@192.168.18.12:~/tt_doc/doc_txt5/Files5/convres.json"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(res5proc.stderr))
    if res5proc.stderr == b'':
        print("[Upload] Patient 5 convres.json uploaded !")
        messagebox.showinfo("INFO", "Patient 5 convres.json uploaded...")
    else:
        print("[!] No file convres.json for patient:5 to upload !")
        messagebox.showerror("Error", "No convres.json for patient:5 to upload...")

def upload6stopres():
    """
        Upload convres.json to server.
    """
    res6proc = subprocess.run(["scp", "./ttt/doc_ttt6/convres.json",
        "pi@192.168.18.12:~/tt_doc/doc_txt6/Files6/convres.json"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(res6proc.stderr))
    if res6proc.stderr == b'':
        print("[Upload] Patient 6 convres.json uploaded !")
        messagebox.showinfo("INFO", "Patient 6 convres.json uploaded...")
    else:
        print("[!] No file convres.json for patient:6 to upload !")
        messagebox.showerror("Error", "No convres.json for patient:6 to upload...")

def upload7stopres():
    """
        Upload convres.json to server.
    """
    res7proc = subprocess.run(["scp", "./ttt/doc_ttt7/convres.json",
        "pi@192.168.18.12:~/tt_doc/doc_txt7/Files7/convres.json"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(res7proc.stderr))
    if res7proc.stderr == b'':
        print("[Upload] Patient 7 convres.json uploaded !")
        messagebox.showinfo("INFO", "Patient 7 convres.json uploaded...")
    else:
        print("[!] No file convres.json for patient:7 to upload !")
        messagebox.showerror("Error", "No convres.json for patient:7 to upload...")

def upload8stopres():
    """
        Upload convres.json to server.
    """
    res8proc = subprocess.run(["scp", "./ttt/doc_ttt8/convres.json",
        "pi@192.168.18.12:~/tt_doc/doc_txt8/Files8/convres.json"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(res8proc.stderr))
    if res8proc.stderr == b'':
        print("[Upload] Patient 8 convres.json uploaded !")
        messagebox.showinfo("INFO", "Patient 8 convres.json uploaded...")
    else:
        print("[!] No file convres.json for patient:8 to upload !")
        messagebox.showerror("Error", "No convres.json for patient:8 to upload...")

def upload9stopres():
    """
        Upload convres.json to server.
    """
    res9proc = subprocess.run(["scp", "./ttt/doc_ttt9/convres.json",
        "pi@192.168.18.12:~/tt_doc/doc_txt9/Files9/convres.json"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(res9proc.stderr))
    if res9proc.stderr == b'':
        print("[Upload] Patient 9 convres.json uploaded !")
        messagebox.showinfo("INFO", "Patient 9 convres.json uploaded...")
    else:
        print("[!] No file convres.json for patient:9 to upload !")
        messagebox.showerror("Error", "No convres.json for patient:9 to upload...")

def upload10stopres():
    """
        Upload convres.json to server.
    """
    res10proc = subprocess.run(["scp", "./ttt/doc_ttt10/convres.json",
        "pi@192.168.18.12:~/tt_doc/doc_txt10/Files10/convres.json"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(res10proc.stderr))
    if res10proc.stderr == b'':
        print("[Upload] Patient 10 convres.json uploaded !")
        messagebox.showinfo("INFO", "Patient 10 convres.json uploaded...")
    else:
        print("[!] No file convres.json for patient:10 to upload !")
        messagebox.showerror("Error", "No convres.json for patient:10 to upload...")

def upload11stopres():
    """
        Upload convres.json to server.
    """
    res11proc = subprocess.run(["scp", "./ttt/doc_ttt11/convres.json",
        "pi@192.168.18.12:~/tt_doc/doc_txt11/Files11/convres.json"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(res11proc.stderr))
    if res11proc.stderr == b'':
        print("[Upload] Patient 11 convres.json uploaded !")
        messagebox.showinfo("INFO", "Patient 11 convres.json uploaded...")
    else:
        print("[!] No file convres.json for patient:11 to upload !")
        messagebox.showerror("Error", "No convres.json for patient:11 to upload...")

def upload12stopres():
    """
        Upload convres.json to server.
    """
    res12proc = subprocess.run(["scp", "./ttt/doc_ttt12/convres.json",
        "pi@192.168.18.12:~/tt_doc/doc_txt12/Files12/convres.json"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(res12proc.stderr))
    if res12proc.stderr == b'':
        print("[Upload] Patient 12 convres.json uploaded !")
        messagebox.showinfo("INFO", "Patient 12 convres.json uploaded...")
    else:
        print("[!] No file convres.json for patient:12 to upload !")
        messagebox.showerror("Error", "No convres.json for patient:12 to upload...")

def upload13stopres():
    """
        Upload convres.json to server.
    """
    res13proc = subprocess.run(["scp", "./ttt/doc_ttt13/convres.json",
        "pi@192.168.18.12:~/tt_doc/doc_txt13/Files13/convres.json"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(res13proc.stderr))
    if res13proc.stderr == b'':
        print("[Upload] Patient 13 convres.json uploaded !")
        messagebox.showinfo("INFO", "Patient 13 convres.json uploaded...")
    else:
        print("[!] No file convres.json for patient:13 to upload !")
        messagebox.showerror("Error", "No convres.json for patient:13 to upload...")

def upload14stopres():
    """
        Upload convres.json to server.
    """
    res14proc = subprocess.run(["scp", "./ttt/doc_ttt14/convres.json",
        "pi@192.168.18.12:~/tt_doc/doc_txt14/Files14/convres.json"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(res14proc.stderr))
    if res14proc.stderr == b'':
        print("[Upload] Patient 14 convres.json uploaded !")
        messagebox.showinfo("INFO", "Patient 14 convres.json uploaded...")
    else:
        print("[!] No file convres.json for patient:14 to upload !")
        messagebox.showerror("Error", "No convres.json for patient:14 to upload...")

def upload15stopres():
    """
        Upload convres.json to server.
    """
    res15proc = subprocess.run(["scp", "./ttt/doc_ttt15/convres.json",
        "pi@192.168.18.12:~/tt_doc/doc_txt15/Files15/convres.json"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(res15proc.stderr))
    if res15proc.stderr == b'':
        print("[Upload] Patient 15 convres.json uploaded !")
        messagebox.showinfo("INFO", "Patient 15 convres.json uploaded...")
    else:
        print("[!] No file convres.json for patient:15 to upload !")
        messagebox.showerror("Error", "No convres.json for patient:15 to upload...")

def upload16stopres():
    """
        Upload convres.json to server.
    """
    res16proc = subprocess.run(["scp", "./ttt/doc_ttt16/convres.json",
        "pi@192.168.18.12:~/tt_doc/doc_txt16/Files16/convres.json"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(res16proc.stderr))
    if res16proc.stderr == b'':
        print("[Upload] Patient 16 convres.json uploaded !")
        messagebox.showinfo("INFO", "Patient 16 convres.json uploaded...")
    else:
        print("[!] No file convres.json for patient:16 to upload !")
        messagebox.showerror("Error", "No convres.json for patient:16 to upload...")

def upload17stopres():
    """
        Upload convres.json to server.
    """
    res17proc = subprocess.run(["scp", "./ttt/doc_ttt17/convres.json",
        "pi@192.168.18.12:~/tt_doc/doc_txt17/Files17/convres.json"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(res17proc.stderr))
    if res17proc.stderr == b'':
        print("[Upload] Patient 17 convres.json uploaded !")
        messagebox.showinfo("INFO", "Patient 17 convres.json uploaded...")
    else:
        print("[!] No file convres.json for patient:17 to upload !")
        messagebox.showerror("Error", "No convres.json for patient:17 to upload...")

def upload18stopres():
    """
        Upload convres.json to server.
    """
    res18proc = subprocess.run(["scp", "./ttt/doc_ttt18/convres.json",
        "pi@192.168.18.12:~/tt_doc/doc_txt18/Files18/convres.json"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(res18proc.stderr))
    if res18proc.stderr == b'':
        print("[Upload] Patient 18 convres.json uploaded !")
        messagebox.showinfo("INFO", "Patient 18 convres.json uploaded...")
    else:
        print("[!] No file convres.json for patient:18 to upload !")
        messagebox.showerror("Error", "No convres.json for patient:18 to upload...")

def upload19stopres():
    """
        Upload convres.json to server.
    """
    res19proc = subprocess.run(["scp", "./ttt/doc_ttt19/convres.json",
        "pi@192.168.18.12:~/tt_doc/doc_txt19/Files19/convres.json"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(res19proc.stderr))
    if res19proc.stderr == b'':
        print("[Upload] Patient 19 convres.json uploaded !")
        messagebox.showinfo("INFO", "Patient 19 convres.json uploaded...")
    else:
        print("[!] No file convres.json for patient:19 to upload !")
        messagebox.showerror("Error", "No convres.json for patient:19 to upload...")

def upload20stopres():
    """
        Upload convres.json to server.
    """
    res20proc = subprocess.run(["scp", "./ttt/doc_ttt20/convres.json",
        "pi@192.168.18.12:~/tt_doc/doc_txt20/Files20/convres.json"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(res20proc.stderr))
    if res20proc.stderr == b'':
        print("[Upload] Patient 20 convres.json uploaded !")
        messagebox.showinfo("INFO", "Patient 20 convres.json uploaded...")
    else:
        print("[!] No file convres.json for patient:20 to upload !")
        messagebox.showerror("Error", "No convres.json for patient:20 to upload...")

def upload21stopres():
    """
        Upload convres.json to server.
    """
    res21proc = subprocess.run(["scp", "./ttt/doc_ttt21/convres.json",
        "pi@192.168.18.12:~/tt_doc/doc_txt21/Files21/convres.json"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(res21proc.stderr))
    if res21proc.stderr == b'':
        print("[Upload] Patient 21 convres.json uploaded !")
        messagebox.showinfo("INFO", "Patient 21 convres.json uploaded...")
    else:
        print("[!] No file convres.json for patient:21 to upload !")
        messagebox.showerror("Error", "No convres.json for patient:21 to upload...")

def upload22stopres():
    """
        Upload convres.json to server.
    """
    res22proc = subprocess.run(["scp", "./ttt/doc_ttt22/convres.json",
        "pi@192.168.18.12:~/tt_doc/doc_txt22/Files22/convres.json"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(res22proc.stderr))
    if res22proc.stderr == b'':
        print("[Upload] Patient 22 convres.json uploaded !")
        messagebox.showinfo("INFO", "Patient 22 convres.json uploaded...")
    else:
        print("[!] No file convres.json for patient:22 to upload !")
        messagebox.showerror("Error", "No convres.json for patient:22 to upload...")

def upload23stopres():
    """
        Upload convres.json to server.
    """
    res23proc = subprocess.run(["scp", "./ttt/doc_ttt23/convres.json",
        "pi@192.168.18.12:~/tt_doc/doc_txt23/Files23/convres.json"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(res23proc.stderr))
    if res23proc.stderr == b'':
        print("[Upload] Patient 23 convres.json uploaded !")
        messagebox.showinfo("INFO", "Patient 23 convres.json uploaded...")
    else:
        print("[!] No file convres.json for patient:23 to upload !")
        messagebox.showerror("Error", "No convres.json for patient:23 to upload...")

def upload24stopres():
    """
        Upload convres.json to server.
    """
    res24proc = subprocess.run(["scp", "./ttt/doc_ttt24/convres.json",
        "pi@192.168.18.12:~/tt_doc/doc_txt24/Files24/convres.json"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(res24proc.stderr))
    if res24proc.stderr == b'':
        print("[Upload] Patient 24 convres.json uploaded !")
        messagebox.showinfo("INFO", "Patient 24 convres.json uploaded...")
    else:
        print("[!] No file convres.json for patient:24 to upload !")
        messagebox.showerror("Error", "No convres.json for patient:24 to upload...")
