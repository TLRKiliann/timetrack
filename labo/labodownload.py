#!/usr/bin/python3
# -*- coding : utf-8 -*-


"""
    Connecting the duration of progress bar
    with task = number of subprocess.
"""


from tkinter import messagebox
import subprocess
from labo.labobar import labodata # labo


def labodownload1():
    """
        to download labo files from server before
        to start with labo interface.
    """
    labodata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt1/Files1/patient1_14b.txt",
        "./need/doc_suivi/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Download] File patient1_14b.txt downloaded !")
        #messagebox.showinfo("INFO", "patient1_14b.txt downloaded !")
    else:
        print("[!] No file to download [!]")
        messagebox.showwarning("Warning", "No patient1_14b.txt to download !")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt1/Files1/result.txt",
        "./labo/doc_labo/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[Download] File result.txt downloaded !")
        #messagebox.showinfo("INFO", "result.txt downloaded !")
    else:
        print("[!] No file to download [!]")
        messagebox.showwarning("Warning", "No result.txt to download !")

def labodownload2():
    """
        to download labo files from server before
        to start with labo interface.
    """
    labodata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt2/Files2/patient2_14b.txt",
        "./need/doc_suivi2/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Download] File patient2_14b.txt downloaded !")
        #messagebox.showinfo("INFO", "patient2_14b.txt downloaded !")
    else:
        print("[!] No file to download [!]")
        messagebox.showwarning("Warning", "No patient2_14b.txt to download !")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt2/Files2/result2.txt",
        "./labo/doc_labo/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[Download] File result2.txt downloaded !")
        #messagebox.showinfo("INFO", "result2.txt downloaded !")
    else:
        print("[!] No file to download [!]")
        messagebox.showwarning("Warning", "No result2.txt to download !")

def labodownload3():
    """
        to download labo files from server before
        to start with labo interface.
    """
    labodata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt3/Files3/patient3_14b.txt",
        "./need/doc_suivi3/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Download] File patient3_14b.txt downloaded !")
        #messagebox.showinfo("INFO", "patient3_14b.txt downloaded !")
    else:
        print("[!] No file to download [!]")
        messagebox.showwarning("Warning", "No patient3_14b.txt to download !")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt3/Files3/result3.txt",
        "./labo/doc_labo/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[Download] File result3.txt downloaded !")
        #messagebox.showinfo("INFO", "result3.txt downloaded !")
    else:
        print("[!] No file to download [!]")
        messagebox.showwarning("Warning", "No result3.txt to download !")

def labodownload4():
    """
        to download labo files from server before
        to start with labo interface.
    """
    labodata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt4/Files4/patient4_14b.txt",
        "./need/doc_suivi4/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Download] File patient4_14b.txt downloaded !")
        #messagebox.showinfo("INFO", "patient4_14b.txt downloaded !")
    else:
        print("[!] No file to download [!]")
        messagebox.showwarning("Warning", "No patient4_14b.txt to download !")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt4/Files4/result4.txt",
        "./labo/doc_labo/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[Download] File result4.txt downloaded !")
        #messagebox.showinfo("INFO", "result4.txt downloaded !")
    else:
        print("[!] No file to download [!]")
        messagebox.showwarning("Warning", "No result4.txt to download !")

def labodownload5():
    """
        to download labo files from server before
        to start with labo interface.
    """
    labodata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt5/Files5/patient5_14b.txt",
        "./need/doc_suivi5/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Download] File patient5_14b.txt downloaded !")
        #messagebox.showinfo("INFO", "patient5_14b.txt downloaded !")
    else:
        print("[!] No file to download [!]")
        messagebox.showwarning("Warning", "No patient5_14b.txt to download !")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt5/Files5/result5.txt",
        "./labo/doc_labo/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[Download] File result5.txt downloaded !")
        #messagebox.showinfo("INFO", "result5.txt downloaded !")
    else:
        print("[!] No file to download [!]")
        messagebox.showwarning("Warning", "No result5.txt to download !")

def labodownload6():
    """
        to download labo files from server before
        to start with labo interface.
    """
    labodata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt6/Files6/patient6_14b.txt",
        "./need/doc_suivi6/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Download] File patient6_14b.txt downloaded !")
        #messagebox.showinfo("INFO", "patient6_14b.txt downloaded !")
    else:
        print("[!] No file to download [!]")
        messagebox.showwarning("Warning", "No patient6_14b.txt to download !")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt6/Files6/result6.txt",
        "./labo/doc_labo/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[Download] File result6.txt downloaded !")
        #messagebox.showinfo("INFO", "result6.txt downloaded !")
    else:
        print("[!] No file to download [!]")
        messagebox.showwarning("Warning", "No result6.txt to download !")

def labodownload7():
    """
        to download labo files from server before
        to start with labo interface.
    """
    labodata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt7/Files7/patient7_14b.txt",
        "./need/doc_suivi7/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Download] File patient7_14b.txt downloaded !")
        #messagebox.showinfo("INFO", "patient7_14b.txt downloaded !")
    else:
        print("[!] No file to download [!]")
        messagebox.showwarning("Warning", "No patient7_14b.txt to download !")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt7/Files7/result7.txt",
        "./labo/doc_labo/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[Download] File result7.txt downloaded !")
        #messagebox.showinfo("INFO", "result7.txt downloaded !")
    else:
        print("[!] No file to download [!]")
        messagebox.showwarning("Warning", "No result7.txt to download !")

def labodownload8():
    """
        to download labo files from server before
        to start with labo interface.
    """
    labodata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt8/Files8/patient8_14b.txt",
        "./need/doc_suivi8/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Download] File patient8_14b.txt downloaded !")
        #messagebox.showinfo("INFO", "patient8_14b.txt downloaded !")
    else:
        print("[!] No file to download [!]")
        messagebox.showwarning("Warning", "No patient8_14b.txt to download !")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt8/Files8/result8.txt",
        "./labo/doc_labo/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[Download] File result8.txt downloaded !")
        #messagebox.showinfo("INFO", "result8.txt downloaded !")
    else:
        print("[!] No file to download [!]")
        messagebox.showwarning("Warning", "No result8.txt to download !")

def labodownload9():
    """
        to download labo files from server before
        to start with labo interface.
    """
    labodata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt9/Files9/patient9_14b.txt",
        "./need/doc_suivi9/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Download] File patient9_14b.txt downloaded !")
        #messagebox.showinfo("INFO", "patient9_14b.txt downloaded !")
    else:
        print("[!] No file to download [!]")
        messagebox.showwarning("Warning", "No patient9_14b.txt to download !")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt9/Files9/result9.txt",
        "./labo/doc_labo/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[Download] File result9.txt downloaded !")
        #messagebox.showinfo("INFO", "result9.txt downloaded !")
    else:
        print("[!] No file to download [!]")
        messagebox.showwarning("Warning", "No result9.txt to download !")

def labodownload10():
    """
        to download labo files from server before
        to start with labo interface.
    """
    labodata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt10/Files10/patient10_14b.txt",
        "./need/doc_suivi10/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Download] File patient10_14b.txt downloaded !")
        #messagebox.showinfo("INFO", "patient10_14b.txt downloaded !")
    else:
        print("[!] No file to download [!]")
        messagebox.showwarning("Warning", "No patient10_14b.txt to download !")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt10/Files10/result10.txt",
        "./labo/doc_labo/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[Download] File result10.txt downloaded !")
        #messagebox.showinfo("INFO", "result10.txt downloaded !")
    else:
        print("[!] No file to download [!]")
        messagebox.showwarning("Warning", "No result10.txt to download !")

def labodownload11():
    """
        to download labo files from server before
        to start with labo interface.
    """
    labodata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt11/Files11/patient11_14b.txt",
        "./need/doc_suivi11/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Download] File patient11_14b.txt downloaded !")
        #messagebox.showinfo("INFO", "patient11_14b.txt downloaded !")
    else:
        print("[!] No file to download [!]")
        messagebox.showwarning("Warning", "No patient11_14b.txt to download !")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt11/Files11/result11.txt",
        "./labo/doc_labo/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[Download] File result11.txt downloaded !")
        #messagebox.showinfo("INFO", "result11.txt downloaded !")
    else:
        print("[!] No file to download [!]")
        messagebox.showwarning("Warning", "No result11.txt to download !")

def labodownload12():
    """
        to download labo files from server before
        to start with labo interface.
    """
    labodata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt12/Files12/patient12_14b.txt",
        "./need/doc_suivi12/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Download] File patient12_14b.txt downloaded !")
        #messagebox.showinfo("INFO", "patient12_14b.txt downloaded !")
    else:
        print("[!] No file to download [!]")
        messagebox.showwarning("Warning", "No patient12_14b.txt to download !")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt12/Files12/result12.txt",
        "./labo/doc_labo/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[Download] File result12.txt downloaded !")
        #messagebox.showinfo("INFO", "result12.txt downloaded !")
    else:
        print("[!] No file to download [!]")
        messagebox.showwarning("Warning", "No result12.txt to download !")

def labodownload13():
    """
        to download labo files from server before
        to start with labo interface.
    """
    labodata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt13/Files13/patient13_14b.txt",
        "./need/doc_suivi13/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Download] File patient13_14b.txt downloaded !")
        #messagebox.showinfo("INFO", "patient13_14b.txt downloaded !")
    else:
        print("[!] No file to download [!]")
        messagebox.showwarning("Warning", "No patient13_14b.txt to download !")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt13/Files13/result13.txt",
        "./labo/doc_labo/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[Download] File result13.txt downloaded !")
        #messagebox.showinfo("INFO", "result13.txt downloaded !")
    else:
        print("[!] No file to download [!]")
        messagebox.showwarning("Warning", "No result13.txt to download !")

def labodownload14():
    """
        to download labo files from server before
        to start with labo interface.
    """
    labodata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt14/Files14/patient14_14b.txt",
        "./need/doc_suivi14/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Download] File patient14_14b.txt downloaded !")
        #messagebox.showinfo("INFO", "patient14_14b.txt downloaded !")
    else:
        print("[!] No file to download [!]")
        messagebox.showwarning("Warning", "No patient14_14b.txt to download !")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt14/Files14/result14.txt",
        "./labo/doc_labo/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[Download] File result14.txt downloaded !")
        #messagebox.showinfo("INFO", "result14.txt downloaded !")
    else:
        print("[!] No file to download [!]")
        messagebox.showwarning("Warning", "No result14.txt to download !")

def labodownload15():
    """
        to download labo files from server before
        to start with labo interface.
    """
    labodata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt15/Files15/patient15_14b.txt",
        "./need/doc_suivi15/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Download] File patient15_14b.txt downloaded !")
        #messagebox.showinfo("INFO", "patient15_14b.txt downloaded !")
    else:
        print("[!] No file to download [!]")
        messagebox.showwarning("Warning", "No patient15_14b.txt to download !")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt15/Files15/result15.txt",
        "./labo/doc_labo/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[Download] File result15.txt downloaded !")
        #messagebox.showinfo("INFO", "result15.txt downloaded !")
    else:
        print("[!] No file to download [!]")
        messagebox.showwarning("Warning", "No result15.txt to download !")

def labodownload16():
    """
        to download labo files from server before
        to start with labo interface.
    """
    labodata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt16/Files16/patient16_14b.txt",
        "./need/doc_suivi16/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Download] File patient16_14b.txt downloaded !")
        #messagebox.showinfo("INFO", "patient16_14b.txt downloaded !")
    else:
        print("[!] No file to download [!]")
        messagebox.showwarning("Warning", "No patient16_14b.txt to download !")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt16/Files16/result16.txt",
        "./labo/doc_labo/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[Download] File result16.txt downloaded !")
        #messagebox.showinfo("INFO", "result16.txt downloaded !")
    else:
        print("[!] No file to download [!]")
        messagebox.showwarning("Warning", "No result16.txt to download !")

def labodownload17():
    """
        to download labo files from server before
        to start with labo interface.
    """
    labodata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt17/Files17/patient17_14b.txt",
        "./need/doc_suivi17/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Download] File patient17_14b.txt downloaded !")
        #messagebox.showinfo("INFO", "patient17_14b.txt downloaded !")
    else:
        print("[!] No file to download [!]")
        messagebox.showwarning("Warning", "No patient17_14b.txt to download !")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt17/Files17/result17.txt",
        "./labo/doc_labo/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[Download] File result17.txt downloaded !")
        #messagebox.showinfo("INFO", "result17.txt downloaded !")
    else:
        print("[!] No file to download [!]")
        messagebox.showwarning("Warning", "No result17.txt to download !")

def labodownload18():
    """
        to download labo files from server before
        to start with labo interface.
    """
    labodata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt18/Files18/patient18_14b.txt",
        "./need/doc_suivi18/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Download] File patient18_14b.txt downloaded !")
        #messagebox.showinfo("INFO", "patient18_14b.txt downloaded !")
    else:
        print("[!] No file to download [!]")
        messagebox.showwarning("Warning", "No patient18_14b.txt to download !")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt18/Files18/result18.txt",
        "./labo/doc_labo/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[Download] File result18.txt downloaded !")
        #messagebox.showinfo("INFO", "result18.txt downloaded !")
    else:
        print("[!] No file to download [!]")
        messagebox.showwarning("Warning", "No result18.txt to download !")

def labodownload19():
    """
        to download labo files from server before
        to start with labo interface.
    """
    labodata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt19/Files19/patient19_14b.txt",
        "./need/doc_suivi19/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Download] File patient19_14b.txt downloaded !")
        #messagebox.showinfo("INFO", "patient19_14b.txt downloaded !")
    else:
        print("[!] No file to download [!]")
        messagebox.showwarning("Warning", "No patient19_14b.txt to download !")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt19/Files19/result19.txt",
        "./labo/doc_labo/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[Download] File result19.txt downloaded !")
        #messagebox.showinfo("INFO", "result19.txt downloaded !")
    else:
        print("[!] No file to download [!]")
        messagebox.showwarning("Warning", "No result19.txt to download !")

def labodownload20():
    """
        to download labo files from server before
        to start with labo interface.
    """
    labodata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt20/Files20/patient20_14b.txt",
        "./need/doc_suivi20/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Download] File patient20_14b.txt downloaded !")
        #messagebox.showinfo("INFO", "patient20_14b.txt downloaded !")
    else:
        print("[!] No file to download [!]")
        messagebox.showwarning("Warning", "No patient20_14b.txt to download !")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt20/Files20/result20.txt",
        "./labo/doc_labo/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[Download] File result20.txt downloaded !")
        #messagebox.showinfo("INFO", "result20.txt downloaded !")
    else:
        print("[!] No file to download [!]")
        messagebox.showwarning("Warning", "No result20.txt to download !")

def labodownload21():
    """
        to download labo files from server before
        to start with labo interface.
    """
    labodata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt21/Files21/patient21_14b.txt",
        "./need/doc_suivi21/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Download] File patient21_14b.txt downloaded !")
        #messagebox.showinfo("INFO", "patient21_14b.txt downloaded !")
    else:
        print("[!] No file to download [!]")
        messagebox.showwarning("Warning", "No patient21_14b.txt to download !")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt21/Files21/result21.txt",
        "./labo/doc_labo/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[Download] File result21.txt downloaded !")
        #messagebox.showinfo("INFO", "result21.txt downloaded !")
    else:
        print("[!] No file to download [!]")
        messagebox.showwarning("Warning", "No result21.txt to download !")

def labodownload22():
    """
        to download labo files from server before
        to start with labo interface.
    """
    labodata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt22/Files22/patient22_14b.txt",
        "./need/doc_suivi22/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Download] File patient22_14b.txt downloaded !")
        #messagebox.showinfo("INFO", "patient22_14b.txt downloaded !")
    else:
        print("[!] No file to download [!]")
        messagebox.showwarning("Warning", "No patient22_14b.txt to download !")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt22/Files22/result22.txt",
        "./labo/doc_labo/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[Download] File result22.txt downloaded !")
        #messagebox.showinfo("INFO", "result22.txt downloaded !")
    else:
        print("[!] No file to download [!]")
        messagebox.showwarning("Warning", "No result22.txt to download !")

def labodownload23():
    """
        to download labo files from server before
        to start with labo interface.
    """
    labodata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt23/Files23/patient23_14b.txt",
        "./need/doc_suivi23/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Download] File patient23_14b.txt downloaded !")
        #messagebox.showinfo("INFO", "patient23_14b.txt downloaded !")
    else:
        print("[!] No file to download [!]")
        messagebox.showwarning("Warning", "No patient23_14b.txt to download !")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt23/Files23/result23.txt",
        "./labo/doc_labo/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[Download] File result23.txt downloaded !")
        #messagebox.showinfo("INFO", "result23.txt downloaded !")
    else:
        print("[!] No file to download [!]")
        messagebox.showwarning("Warning", "No result23.txt to download !")

def labodownload24():
    """
        to download labo files from server before
        to start with labo interface.
    """
    labodata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt24/Files24/patient24_14b.txt",
        "./need/doc_suivi24/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Download] File patient24_14b.txt downloaded !")
        #messagebox.showinfo("INFO", "patient24_14b.txt downloaded !")
    else:
        print("[!] No file to download [!]")
        messagebox.showwarning("Warning", "No patient24_14b.txt to download !")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt24/Files24/result24.txt",
        "./labo/doc_labo/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[Download] File result24.txt downloaded !")
        #messagebox.showinfo("INFO", "result24.txt downloaded !")
    else:
        print("[!] No file to download [!]")
        messagebox.showwarning("Warning", "No result24.txt to download !")
