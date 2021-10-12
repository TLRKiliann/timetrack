#!/usr/bin/python3
# -*- coding : utf-8 -*-


"""
    Connecting the duration of progress bar
    with task = number of subprocess.
"""


from tkinter import messagebox
from diag.diagloadbar import diagdata
import subprocess


def diagloading1():
    """
        to download med files from server before
        to start with med interface.
    """
    diagdata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt1/Files1/diagrecap1.txt",
        "./diag/doc_diag/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Download] File diagrecap1.txt downloaded !")
        #messagebox.showinfo("INFO", "diagrecap.txt downloaded")
    else:
        print("[!] No file to download !")
        messagebox.showwarning("Warning", "No diagrecap1.txt to download !")

def diagloading2():
    """
        to download med files from server before
        to start with med interface.
    """
    diagdata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt2/Files2/diagrecap2.txt",
        "./diag/doc_diag2/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Download] File diagrecap2.txt downloaded !")
        #messagebox.showinfo("INFO", "diagrecap2.txt downloaded")
    else:
        print("[!] No file to download !")
        messagebox.showwarning("Warning", "No diagrecap2.txt to download !")

def diagloading3():
    """
        to download med files from server before
        to start with med interface.
    """
    diagdata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt3/Files3/diagrecap3.txt",
        "./diag/doc_diag3/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Download] File diagrecap3.txt downloaded !")
        #messagebox.showinfo("INFO", "diagrecap3.txt downloaded")
    else:
        print("[!] No file to download !")
        messagebox.showwarning("Warning", "No diagrecap3.txt to download !")

def diagloading4():
    """
        to download med files from server before
        to start with med interface.
    """
    diagdata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt4/Files4/diagrecap4.txt",
        "./diag/doc_diag4/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Download] File diagrecap4.txt downloaded !")
        #messagebox.showinfo("INFO", "diagrecap4.txt downloaded")
    else:
        print("[!] No file to download !")
        messagebox.showwarning("Warning", "No diagrecap4.txt to download !")

def diagloading5():
    """
        to download med files from server before
        to start with med interface.
    """
    diagdata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt5/Files5/diagrecap5.txt",
        "./diag/doc_diag5/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Download] File diagrecap5.txt downloaded !")
        #messagebox.showinfo("INFO", "diagrecap5.txt downloaded")
    else:
        print("[!] No file to download !")
        messagebox.showwarning("Warning", "No diagrecap5.txt to download !")

def diagloading6():
    """
        to download med files from server before
        to start with med interface.
    """
    diagdata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt6/Files6/diagrecap6.txt",
        "./diag/doc_diag6/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Download] File diagrecap6.txt downloaded !")
        #messagebox.showinfo("INFO", "diagrecap6.txt downloaded")
    else:
        print("[!] No file to download !")
        messagebox.showwarning("Warning", "No diagrecap6.txt to download !")

def diagloading7():
    """
        to download med files from server before
        to start with med interface.
    """
    diagdata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt7/Files7/diagrecap7.txt",
        "./diag/doc_diag7/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Download] File diagrecap7.txt downloaded !")
        #messagebox.showinfo("INFO", "diagrecap7.txt downloaded")
    else:
        print("[!] No file to download !")
        messagebox.showwarning("Warning", "No diagrecap7.txt to download !")

def diagloading8():
    """
        to download med files from server before
        to start with med interface.
    """
    diagdata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt8/Files8/diagrecap8.txt",
        "./diag/doc_diag8/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Download] File diagrecap8.txt downloaded !")
        #messagebox.showinfo("INFO", "diagrecap8.txt downloaded")
    else:
        print("[!] No file to download !")
        messagebox.showwarning("Warning", "No diagrecap8.txt to download !")

def diagloading9():
    """
        to download med files from server before
        to start with med interface.
    """
    diagdata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt9/Files9/diagrecap9.txt",
        "./diag/doc_diag9/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Download] File diagrecap9.txt downloaded !")
        #messagebox.showinfo("INFO", "diagrecap9.txt downloaded")
    else:
        print("[!] No file to download !")
        messagebox.showwarning("Warning", "No diagrecap9.txt to download !")

def diagloading10():
    """
        to download med files from server before
        to start with med interface.
    """
    diagdata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt10/Files10/diagrecap10.txt",
        "./diag/doc_diag10/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Download] File diagrecap10.txt downloaded !")
        #messagebox.showinfo("INFO", "diagrecap10.txt downloaded")
    else:
        print("[!] No file to download !")
        messagebox.showwarning("Warning", "No diagrecap10.txt to download !")

def diagloading11():
    """
        to download med files from server before
        to start with med interface.
    """
    diagdata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt11/Files11/diagrecap11.txt",
        "./diag/doc_diag11/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Download] File diagrecap11.txt downloaded !")
        #messagebox.showinfo("INFO", "diagrecap11.txt downloaded")
    else:
        print("[!] No file to download !")
        messagebox.showwarning("Warning", "No diagrecap11.txt to download !")

def diagloading12():
    """
        to download med files from server before
        to start with med interface.
    """
    diagdata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt12/Files12/diagrecap12.txt",
        "./diag/doc_diag12/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Download] File diagrecap12.txt downloaded !")
        #messagebox.showinfo("INFO", "diagrecap12.txt downloaded")
    else:
        print("[!] No file to download !")
        messagebox.showwarning("Warning", "No diagrecap12.txt to download !")

def diagloading13():
    """
        to download med files from server before
        to start with med interface.
    """
    diagdata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt13/Files13/diagrecap13.txt",
        "./diag/doc_diag13/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Download] File diagrecap13.txt downloaded !")
        #messagebox.showinfo("INFO", "diagrecap13.txt downloaded")
    else:
        print("[!] No file to download !")
        messagebox.showwarning("Warning", "No diagrecap13.txt to download !")

def diagloading14():
    """
        to download med files from server before
        to start with med interface.
    """
    diagdata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt14/Files14/diagrecap14.txt",
        "./diag/doc_diag14/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Download] File diagrecap14.txt downloaded !")
        #messagebox.showinfo("INFO", "diagrecap14.txt downloaded")
    else:
        print("[!] No file to download !")
        messagebox.showwarning("Warning", "No diagrecap14.txt to download !")

def diagloading15():
    """
        to download med files from server before
        to start with med interface.
    """
    diagdata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt15/Files15/diagrecap15.txt",
        "./diag/doc_diag15/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Download] File diagrecap15.txt downloaded !")
        #messagebox.showinfo("INFO", "diagrecap15.txt downloaded")
    else:
        print("[!] No file to download !")
        messagebox.showwarning("Warning", "No diagrecap15.txt to download !")

def diagloading16():
    """
        to download med files from server before
        to start with med interface.
    """
    diagdata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt16/Files16/diagrecap16.txt",
        "./diag/doc_diag16/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Download] File diagrecap16.txt downloaded !")
        #messagebox.showinfo("INFO", "diagrecap16.txt downloaded")
    else:
        print("[!] No file to download !")
        messagebox.showwarning("Warning", "No diagrecap16.txt to download !")

def diagloading17():
    """
        to download med files from server before
        to start with med interface.
    """
    diagdata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt17/Files17/diagrecap17.txt",
        "./diag/doc_diag17/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Download] File diagrecap17.txt downloaded !")
        #messagebox.showinfo("INFO", "diagrecap17.txt downloaded")
    else:
        print("[!] No file to download !")
        messagebox.showwarning("Warning", "No diagrecap17.txt to download !")

def diagloading18():
    """
        to download med files from server before
        to start with med interface.
    """
    diagdata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt18/Files18/diagrecap18.txt",
        "./diag/doc_diag18/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Download] File diagrecap18.txt downloaded !")
        #messagebox.showinfo("INFO", "diagrecap18.txt downloaded")
    else:
        print("[!] No file to download !")
        messagebox.showwarning("Warning", "No diagrecap18.txt to download !")

def diagloading19():
    """
        to download med files from server before
        to start with med interface.
    """
    diagdata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt19/Files19/diagrecap19.txt",
        "./diag/doc_diag19/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Download] File diagrecap19.txt downloaded !")
        #messagebox.showinfo("INFO", "diagrecap19.txt downloaded")
    else:
        print("[!] No file to download !")
        messagebox.showwarning("Warning", "No diagrecap19.txt to download !")

def diagloading20():
    """
        to download med files from server before
        to start with med interface.
    """
    diagdata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt20/Files20/diagrecap20.txt",
        "./diag/doc_diag20/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Download] File diagrecap20.txt downloaded !")
        #messagebox.showinfo("INFO", "diagrecap20.txt downloaded")
    else:
        print("[!] No file to download !")
        messagebox.showwarning("Warning", "No diagrecap20.txt to download !")

def diagloading21():
    """
        to download med files from server before
        to start with med interface.
    """
    diagdata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt21/Files21/diagrecap21.txt",
        "./diag/doc_diag21/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Download] File diagrecap21.txt downloaded !")
        #messagebox.showinfo("INFO", "diagrecap21.txt downloaded")
    else:
        print("[!] No file to download !")
        messagebox.showwarning("Warning", "No diagrecap21.txt to download !")

def diagloading22():
    """
        to download med files from server before
        to start with med interface.
    """
    diagdata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt22/Files22/diagrecap22.txt",
        "./diag/doc_diag22/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Download] File diagrecap22.txt downloaded !")
        #messagebox.showinfo("INFO", "diagrecap22.txt downloaded")
    else:
        print("[!] No file to download !")
        messagebox.showwarning("Warning", "No diagrecap22.txt to download !")

def diagloading23():
    """
        to download med files from server before
        to start with med interface.
    """
    diagdata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt23/Files23/diagrecap23.txt",
        "./diag/doc_diag23/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Download] File diagrecap23.txt downloaded !")
        #messagebox.showinfo("INFO", "diagrecap23.txt downloaded")
    else:
        print("[!] No file to download !")
        messagebox.showwarning("Warning", "No diagrecap23.txt to download !")

def diagloading24():
    """
        to download med files from server before
        to start with med interface.
    """
    diagdata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt24/Files24/diagrecap24.txt",
        "./diag/doc_diag24/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Download] File diagrecap24.txt downloaded !")
        #messagebox.showinfo("INFO", "diagrecap24.txt downloaded")
    else:
        print("[!] No file to download !")
        messagebox.showwarning("Warning", "No diagrecap24.txt to download !")
