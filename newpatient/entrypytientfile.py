#!/usr/bin/python3
# -*- coding: utf-8 -*-


from tkinter import *
import tkinter as tk
from tkinter import messagebox
import os
import subprocess
try:
    import pymysql
    pymysql.install_as_MySQLdb()
except ImportError as err_report2:
    print("[!] An error occured about pymysql !", err_report2)
    pass


gui = tk.Tk()
gui.title("New Patient")
gui.configure(bg='DodgerBlue2')
#gui.geometry('300x200')

def get(IDpatient, Patient_num, Patientname, Firstname_pat, Surname, Sur_pat,
    Birthvalue, Birth_entree, Allergia, Patient_allergy, TransDisVal, TransDisease,
    Diagnostic, Diagnos_pat):
    """
        Entry at first time a patient
        (when program is open for the
        first time) and when entry button
        is pressed.
    """
    MsgBox = messagebox.askyesno('Save data', 'Do you want to save ?')
    if MsgBox == 1:
        IDpatient = Patient_num.get()
        Patientname = Firstname_pat.get()
        Surname = Sur_pat.get()
        Birthvalue = Birth_entree.get()
        Allergia = Patient_allergy.get()
        TransDisVal = TransDisease.get()
        Diagnostic = Diagnos_pat.get()

        if Patient_num.get() == "" or Firstname_pat.get() == "" or Sur_pat.get() == "":
            messagebox.showerror("MySQL Connection", "Enter Correct Details.")
        else:
            sqlCon = pymysql.connect(host='192.168.18.12', port=3306, user='koala33',
                password='Ko@l@tr3379', database='timetrackconn')
            cur = sqlCon.cursor()
            cur.execute("INSERT into timetrackconn values (%s, %s, %s, %s, %s, %s, %s)",(
            Patient_num.get(),
            Firstname_pat.get(),
            Sur_pat.get(),
            Birth_entree.get(),
            Patient_allergy.get(),
            TransDisease.get(),
            Diagnos_pat.get(),
            ))
            sqlCon.commit()
            sqlCon.close()
            messagebox.showinfo("MySQL connection", "Record Entered Successfully !")

        try:
            if os.path.getsize('./newpatient/entryfile.txt'):
                print("[+] File 'entryfile.txt' exist !")
        except FileNotFoundError as outcom1:
            print("[!] Sorry, file 'entryfile.txt' does not exist !", outcom1)
            with open('./newpatient/entryfile.txt', 'w') as namefile:
                namefile.write(Patientname + " " + Surname + '\n')
                namefile.write(Birthvalue + '\n')
                namefile.write(Allergia + '\n')
                namefile.write(TransDisVal + '\n')
                namefile.write(Diagnostic + '\n')
            print("[+] File 'entryfile.txt' created !")

            proc = subprocess.run(["scp", './newpatient/entryfile.txt',
                "pi@192.168.18.12:~/tt_doc/doc_txt1/Files1/entryfile.txt"],
                stderr=subprocess.PIPE)
            print("Result SCP transfert : %s" % repr(proc.stderr))
            if proc.stderr == b'':
                print("[upload] File entryfile.txt uploaded !")
                #messagebox.showinfo("INFO", "entryfile.txt uploaded...")
            else:
                print("[!] No file entryfile.txt to upload !")
                messagebox.showerror("Error", "No entryfile.txt to upload...")

            if os.path.getsize('./newpatient/entryfile.txt'):
                return

        try:
            if os.path.getsize('./newpatient/entryfile2.txt'):
                print("[+] File 'entryfile2.txt' exist !")
        except FileNotFoundError as outcom2:
            print("[!] Sorry, file 'entryfile2.txt' does not exist !", outcom2)
            with open('./newpatient/entryfile2.txt', 'w') as namefile:
                namefile.write(Patientname + " " + Surname + '\n')
                namefile.write(Birthvalue + '\n')
                namefile.write(Allergia + '\n')
                namefile.write(TransDisVal + '\n')
                namefile.write(Diagnostic + '\n')
            print("[+] File 'entryfile2.txt' created !")

            proc = subprocess.run(["scp", './newpatient/entryfile2.txt',
                "pi@192.168.18.12:~/tt_doc/doc_txt2/Files2/entryfile2.txt"],
                stderr=subprocess.PIPE)
            print("Result SCP transfert : %s" % repr(proc.stderr))
            if proc.stderr == b'':
                print("[upload] File entryfile2.txt uploaded !")
                #messagebox.showinfo("INFO", "entryfile2.txt uploaded...")
            else:
                print("[!] No file to upload !")
                messagebox.showerror("Error", "No entryfile2.txt to upload...")

            if os.path.getsize('./newpatient/entryfile2.txt'):
                return

        try:
            if os.path.getsize('./newpatient/entryfile3.txt'):
                print("[+] File 'entryfile3.txt' exist !")
        except FileNotFoundError as outcom3:
            print("[!] Sorry, file 'entryfile3.txt' does not exist !", outcom3)
            with open('./newpatient/entryfile3.txt', 'w') as namefile:
                namefile.write(Patientname + " " + Surname + '\n')
                namefile.write(Birthvalue + '\n')
                namefile.write(Allergia + '\n')
                namefile.write(TransDisVal + '\n')
                namefile.write(Diagnostic + '\n')
            print("[+] File 'entryfile3.txt' created !")

            proc = subprocess.run(["scp", './newpatient/entryfile3.txt',
                "pi@192.168.18.12:~/tt_doc/doc_txt3/Files3/entryfile3.txt"],
                stderr=subprocess.PIPE)
            print("Result SCP transfert : %s" % repr(proc.stderr))
            if proc.stderr == b'':
                print("[upload] File entryfile3.txt uploaded !")
                #messagebox.showinfo("INFO", "entryfile3.txt uploaded...")
            else:
                print("[!] No file to upload !")
                messagebox.showerror("Error", "No entryfile3.txt to upload...")

            if os.path.getsize('./newpatient/entryfile3.txt'):
                return

        try:
            if os.path.getsize('./newpatient/entryfile4.txt'):
                print("[+] File 'entryfile4.txt' exist !")
        except FileNotFoundError as outcom4:
            print("[!] Sorry, file 'entryfile4.txt' does not exist !", outcom4)
            with open('./newpatient/entryfile4.txt', 'w') as namefile:
                namefile.write(Patientname + " " + Surname + '\n')
                namefile.write(Birthvalue + '\n')
                namefile.write(Allergia + '\n')
                namefile.write(TransDisVal + '\n')
                namefile.write(Diagnostic + '\n')
            print("[+] File 'entryfile4.txt' created !")

            proc = subprocess.run(["scp", './newpatient/entryfile4.txt',
                "pi@192.168.18.12:~/tt_doc/doc_txt4/Files4/entryfile4.txt"],
                stderr=subprocess.PIPE)
            print("Result SCP transfert : %s" % repr(proc.stderr))
            if proc.stderr == b'':
                print("[upload] File entryfile4.txt uploaded !")
                #messagebox.showinfo("INFO", "entryfile4.txt uploaded...")
            else:
                print("[!] No file to upload !")
                messagebox.showerror("Error", "No entryfile4.txt to upload...")

            if os.path.getsize('./newpatient/entryfile4.txt'):
                return

        try:
            if os.path.getsize('./newpatient/entryfile5.txt'):
                print("[+] File 'entryfile5.txt' exist !")
        except FileNotFoundError as outcom5:
            print("[!] Sorry, file 'entryfile5.txt' does not exist !", outcom5)
            with open('./newpatient/entryfile5.txt', 'w') as namefile:
                namefile.write(Patientname + " " + Surname + '\n')
                namefile.write(Birthvalue + '\n')
                namefile.write(Allergia + '\n')
                namefile.write(TransDisVal + '\n')
                namefile.write(Diagnostic + '\n')
            print("[+] File 'entryfile5.txt' created !")

            proc = subprocess.run(["scp", './newpatient/entryfile5.txt',
                "pi@192.168.18.12:~/tt_doc/doc_txt5/Files5/entryfile5.txt"],
                stderr=subprocess.PIPE)
            print("Result SCP transfert : %s" % repr(proc.stderr))
            if proc.stderr == b'':
                print("[upload] File entryfile5.txt uploaded !")
                #messagebox.showinfo("INFO", "entryfile5.txt uploaded...")
            else:
                print("[!] No file to upload !")
                messagebox.showerror("Error", "No entryfile5.txt to upload...")

            if os.path.getsize('./newpatient/entryfile5.txt'):
                return

        try:
            if os.path.getsize('./newpatient/entryfile6.txt'):
                print("[+] File 'entryfile6.txt' exist !")
        except FileNotFoundError as outcom6:
            print("[!] Sorry, file 'entryfile6.txt' does not exist !", outcom6)
            with open('./newpatient/entryfile6.txt', 'w') as namefile:
                namefile.write(Patientname + " " + Surname + '\n')
                namefile.write(Birthvalue + '\n')
                namefile.write(Allergia + '\n')
                namefile.write(TransDisVal + '\n')
                namefile.write(Diagnostic + '\n')
            print("[+] File 'entryfile6.txt' created !")

            proc = subprocess.run(["scp", './newpatient/entryfile6.txt',
                "pi@192.168.18.12:~/tt_doc/doc_txt6/Files6/entryfile6.txt"],
                stderr=subprocess.PIPE)
            print("Result SCP transfert : %s" % repr(proc.stderr))
            if proc.stderr == b'':
                print("[upload] File entryfile6.txt uploaded !")
                #messagebox.showinfo("INFO", "entryfile6.txt uploaded...")
            else:
                print("[!] No file to upload !")
                messagebox.showerror("Error", "No entryfile6.txt to upload...")

            if os.path.getsize('./newpatient/entryfile6.txt'):
                return

        try:
            if os.path.getsize('./newpatient/entryfile7.txt'):
                print("[+] File 'entryfile7.txt' exist !")
        except FileNotFoundError as outcom7:
            print("[!] Sorry, file 'entryfile7.txt' does not exist !", outcom7)
            with open('./newpatient/entryfile7.txt', 'w') as namefile:
                namefile.write(Patientname + " " + Surname + '\n')
                namefile.write(Birthvalue + '\n')
                namefile.write(Allergia + '\n')
                namefile.write(TransDisVal + '\n')
                namefile.write(Diagnostic + '\n')
            print("[+] File 'entryfile7.txt' created !")

            proc = subprocess.run(["scp", './newpatient/entryfile7.txt',
                "pi@192.168.18.12:~/tt_doc/doc_txt7/Files7/entryfile7.txt"],
                stderr=subprocess.PIPE)
            print("Result SCP transfert : %s" % repr(proc.stderr))
            if proc.stderr == b'':
                print("[upload] File entryfile7.txt uploaded !")
                #messagebox.showinfo("INFO", "entryfile7.txt uploaded...")
            else:
                print("[!] No file to upload !")
                messagebox.showerror("Error", "No entryfile7.txt to upload...")

            if os.path.getsize('./newpatient/entryfile7.txt'):
                return

        try:
            if os.path.getsize('./newpatient/entryfile8.txt'):
                print("[+] File 'entryfile8.txt' exist !")
        except FileNotFoundError as outcom8:
            print("[!] Sorry, file 'entryfile8.txt' does not exist !", outcom8)
            with open('./newpatient/entryfile8.txt', 'w') as namefile:
                namefile.write(Patientname + " " + Surname + '\n')
                namefile.write(Birthvalue + '\n')
                namefile.write(Allergia + '\n')
                namefile.write(TransDisVal + '\n')
                namefile.write(Diagnostic + '\n')
            print("[+] File 'entryfile8.txt' created !")

            proc = subprocess.run(["scp", './newpatient/entryfile8.txt',
                "pi@192.168.18.12:~/tt_doc/doc_txt8/Files8/entryfile8.txt"],
                stderr=subprocess.PIPE)
            print("Result SCP transfert : %s" % repr(proc.stderr))
            if proc.stderr == b'':
                print("[upload] File entryfile8.txt uploaded !")
                #messagebox.showinfo("INFO", "entryfile8.txt uploaded...")
            else:
                print("[!] No file to upload !")
                messagebox.showerror("Error", "No entryfile8.txt to upload...")

            if os.path.getsize('./newpatient/entryfile8.txt'):
                return

        try:
            if os.path.getsize('./newpatient/entryfile9.txt'):
                print("[+] File 'entryfile9.txt' exist !")
        except FileNotFoundError as outcom9:
            print("[!] Sorry, file 'entryfile9.txt' does not exist !", outcom9)
            with open('./newpatient/entryfile9.txt', 'w') as namefile:
                namefile.write(Patientname + " " + Surname + '\n')
                namefile.write(Birthvalue + '\n')
                namefile.write(Allergia + '\n')
                namefile.write(TransDisVal + '\n')
                namefile.write(Diagnostic + '\n')
            print("[+] File 'entryfile9.txt' created !")

            proc = subprocess.run(["scp", './newpatient/entryfile9.txt',
                "pi@192.168.18.12:~/tt_doc/doc_txt9/Files9/entryfile9.txt"],
                stderr=subprocess.PIPE)
            print("Result SCP transfert : %s" % repr(proc.stderr))
            if proc.stderr == b'':
                print("[upload] File entryfile9.txt uploaded !")
                #messagebox.showinfo("INFO", "entryfile9.txt uploaded...")
            else:
                print("[!] No file to upload !")
                messagebox.showerror("Error", "No entryfile9.txt to upload...")

            if os.path.getsize('./newpatient/entryfile9.txt'):
                return

        try:
            if os.path.getsize('./newpatient/entryfile10.txt'):
                print("[+] File 'entryfile10.txt' exist !")
        except FileNotFoundError as outcom10:
            print("[!] Sorry, file 'entryfile10.txt' does not exist !", outcom10)
            with open('./newpatient/entryfile10.txt', 'w') as namefile:
                namefile.write(Patientname + " " + Surname + '\n')
                namefile.write(Birthvalue + '\n')
                namefile.write(Allergia + '\n')
                namefile.write(TransDisVal + '\n')
                namefile.write(Diagnostic + '\n')
            print("[+] File 'entryfile10.txt' created !")

            proc = subprocess.run(["scp", './newpatient/entryfile10.txt',
                "pi@192.168.18.12:~/tt_doc/doc_txt10/Files10/entryfile10.txt"],
                stderr=subprocess.PIPE)
            print("Result SCP transfert : %s" % repr(proc.stderr))
            if proc.stderr == b'':
                print("[upload] File entryfile10.txt uploaded !")
                #messagebox.showinfo("INFO", "entryfile10.txt uploaded...")
            else:
                print("[!] No file to upload !")
                messagebox.showerror("Error", "No entryfile10.txt to upload...")

            if os.path.getsize('./newpatient/entryfile10.txt'):
                return

        try:
            if os.path.getsize('./newpatient/entryfile11.txt'):
                print("[+] File 'entryfile11.txt' exist !")
        except FileNotFoundError as outcom11:
            print("[!] Sorry, file 'entryfile11.txt' does not exist !", outcom11)
            with open('./newpatient/entryfile11.txt', 'w') as namefile:
                namefile.write(Patientname + " " + Surname + '\n')
                namefile.write(Birthvalue + '\n')
                namefile.write(Allergia + '\n')
                namefile.write(TransDisVal + '\n')
                namefile.write(Diagnostic + '\n')
            print("[+] File 'entryfile11.txt' created !")

            proc = subprocess.run(["scp", './newpatient/entryfile11.txt',
                "pi@192.168.18.12:~/tt_doc/doc_txt11/Files11/entryfile11.txt"],
                stderr=subprocess.PIPE)
            print("Result SCP transfert : %s" % repr(proc.stderr))
            if proc.stderr == b'':
                print("[upload] File entryfile11.txt uploaded !")
                #messagebox.showinfo("INFO", "entryfile11.txt uploaded...")
            else:
                print("[!] No file to upload !")
                messagebox.showerror("Error", "No entryfile11.txt to upload...")

            if os.path.getsize('./newpatient/entryfile11.txt'):
                return

        try:
            if os.path.getsize('./newpatient/entryfile12.txt'):
                print("[+] File 'entryfile12.txt' exist !")
        except FileNotFoundError as outcom12:
            print("[!] Sorry, file 'entryfile12.txt' does not exist !", outcom12)
            with open('./newpatient/entryfile12.txt', 'w') as namefile:
                namefile.write(Patientname + " " + Surname + '\n')
                namefile.write(Birthvalue + '\n')
                namefile.write(Allergia + '\n')
                namefile.write(TransDisVal + '\n')
                namefile.write(Diagnostic + '\n')
            print("[+] File 'entryfile12.txt' created !")

            proc = subprocess.run(["scp", './newpatient/entryfile12.txt',
                "pi@192.168.18.12:~/tt_doc/doc_txt12/Files12/entryfile12.txt"],
                stderr=subprocess.PIPE)
            print("Result SCP transfert : %s" % repr(proc.stderr))
            if proc.stderr == b'':
                print("[upload] File entryfile12.txt uploaded !")
                #messagebox.showinfo("INFO", "entryfile12.txt uploaded...")
            else:
                print("[!] No file to upload !")
                messagebox.showerror("Error", "No entryfile12.txt to upload...")

            if os.path.getsize('./newpatient/entryfile12.txt'):
                return

        try:
            if os.path.getsize('./newpatient/entryfile13.txt'):
                print("[+] File 'entryfile13.txt' exist !")
        except FileNotFoundError as outcom13:
            print("[!] Sorry, file 'entryfile13.txt' does not exist !", outcom13)
            with open('./newpatient/entryfile13.txt', 'w') as namefile:
                namefile.write(Patientname + " " + Surname + '\n')
                namefile.write(Birthvalue + '\n')
                namefile.write(Allergia + '\n')
                namefile.write(TransDisVal + '\n')
                namefile.write(Diagnostic + '\n')
            print("[+] File 'entryfile13.txt' created !")

            proc = subprocess.run(["scp", './newpatient/entryfile13.txt',
                "pi@192.168.18.12:~/tt_doc/doc_txt13/Files13/entryfile13.txt"],
                stderr=subprocess.PIPE)
            print("Result SCP transfert : %s" % repr(proc.stderr))
            if proc.stderr == b'':
                print("[upload] File entryfile13.txt uploaded !")
                #messagebox.showinfo("INFO", "entryfile13.txt uploaded...")
            else:
                print("[!] No file to upload !")
                messagebox.showerror("Error", "No entryfile13.txt to upload...")

            if os.path.getsize('./newpatient/entryfile13.txt'):
                return

        try:
            if os.path.getsize('./newpatient/entryfile14.txt'):
                print("[+] File 'entryfile14.txt' exist !")
        except FileNotFoundError as outcom14:
            print("[!] Sorry, file 'entryfile14.txt' does not exist !", outcom14)
            with open('./newpatient/entryfile14.txt', 'w') as namefile:
                namefile.write(Patientname + " " + Surname + '\n')
                namefile.write(Birthvalue + '\n')
                namefile.write(Allergia + '\n')
                namefile.write(TransDisVal + '\n')
                namefile.write(Diagnostic + '\n')
            print("[+] File 'entryfile14.txt' created !")

            proc = subprocess.run(["scp", './newpatient/entryfile14.txt',
                "pi@192.168.18.12:~/tt_doc/doc_txt14/Files14/entryfile14.txt"],
                stderr=subprocess.PIPE)
            print("Result SCP transfert : %s" % repr(proc.stderr))
            if proc.stderr == b'':
                print("[upload] File entryfile14.txt uploaded !")
                #messagebox.showinfo("INFO", "entryfile14.txt uploaded...")
            else:
                print("[!] No file to upload !")
                messagebox.showerror("Error", "No entryfile14.txt to upload...")

            if os.path.getsize('./newpatient/entryfile14.txt'):
                return

        try:
            if os.path.getsize('./newpatient/entryfile15.txt'):
                print("[+] File 'entryfile15.txt' exist !")
        except FileNotFoundError as outcom15:
            print("[!] Sorry, file 'entryfile15.txt' does not exist !", outcom15)
            with open('./newpatient/entryfile15.txt', 'w') as namefile:
                namefile.write(Patientname + " " + Surname + '\n')
                namefile.write(Birthvalue + '\n')
                namefile.write(Allergia + '\n')
                namefile.write(TransDisVal + '\n')
                namefile.write(Diagnostic + '\n')
            print("[+] File 'entryfile15.txt' created !")

            proc = subprocess.run(["scp", './newpatient/entryfile15.txt',
                "pi@192.168.18.12:~/tt_doc/doc_txt15/Files15/entryfile15.txt"],
                stderr=subprocess.PIPE)
            print("Result SCP transfert : %s" % repr(proc.stderr))
            if proc.stderr == b'':
                print("[upload] File entryfile15.txt uploaded !")
                #messagebox.showinfo("INFO", "entryfile15.txt uploaded...")
            else:
                print("[!] No file to upload !")
                messagebox.showerror("Error", "No entryfile15.txt to upload...")

            if os.path.getsize('./newpatient/entryfile15.txt'):
                return

        try:
            if os.path.getsize('./newpatient/entryfile16.txt'):
                print("[+] File 'entryfile16.txt' exist !")
        except FileNotFoundError as outcom16:
            print("[!] Sorry, file 'entryfile16.txt' does not exist !", outcom16)
            with open('./newpatient/entryfile16.txt', 'w') as namefile:
                namefile.write(Patientname + " " + Surname + '\n')
                namefile.write(Birthvalue + '\n')
                namefile.write(Allergia + '\n')
                namefile.write(TransDisVal + '\n')
                namefile.write(Diagnostic + '\n')
            print("[+] File 'entryfile16.txt' created !")

            proc = subprocess.run(["scp", './newpatient/entryfile16.txt',
                "pi@192.168.18.12:~/tt_doc/doc_txt16/Files16/entryfile16.txt"],
                stderr=subprocess.PIPE)
            print("Result SCP transfert : %s" % repr(proc.stderr))
            if proc.stderr == b'':
                print("[upload] File entryfile16.txt uploaded !")
                #messagebox.showinfo("INFO", "entryfile16.txt uploaded...")
            else:
                print("[!] No file to upload !")
                messagebox.showerror("Error", "No entryfile16.txt to upload...")

            if os.path.getsize('./newpatient/entryfile16.txt'):
                return

        try:
            if os.path.getsize('./newpatient/entryfile17.txt'):
                print("[+] File 'entryfile17.txt' exist !")
        except FileNotFoundError as outcom17:
            print("[!] Sorry, file 'entryfile17.txt' does not exist !", outcom17)
            with open('./newpatient/entryfile17.txt', 'w') as namefile:
                namefile.write(Patientname + " " + Surname + '\n')
                namefile.write(Birthvalue + '\n')
                namefile.write(Allergia + '\n')
                namefile.write(TransDisVal + '\n')
                namefile.write(Diagnostic + '\n')
            print("[+] File 'entryfile17.txt' created !")

            proc = subprocess.run(["scp", './newpatient/entryfile17.txt',
                "pi@192.168.18.12:~/tt_doc/doc_txt17/Files17/entryfile17.txt"],
                stderr=subprocess.PIPE)
            print("Result SCP transfert : %s" % repr(proc.stderr))
            if proc.stderr == b'':
                print("[upload] File entryfile17.txt uploaded !")
                #messagebox.showinfo("INFO", "entryfile17.txt uploaded...")
            else:
                print("[!] No file to upload !")
                messagebox.showerror("Error", "No entryfile17.txt to upload...")

            if os.path.getsize('./newpatient/entryfile17.txt'):
                return

        try:
            if os.path.getsize('./newpatient/entryfile18.txt'):
                print("[+] File 'entryfile18.txt' exist !")
        except FileNotFoundError as outcom18:
            print("[!] Sorry, file 'entryfile18.txt' does not exist !", outcom18)
            with open('./newpatient/entryfile18.txt', 'w') as namefile:
                namefile.write(Patientname + " " + Surname + '\n')
                namefile.write(Birthvalue + '\n')
                namefile.write(Allergia + '\n')
                namefile.write(TransDisVal + '\n')
                namefile.write(Diagnostic + '\n')
            print("[+] File 'entryfile18.txt' created !")

            proc = subprocess.run(["scp", './newpatient/entryfile18.txt',
                "pi@192.168.18.12:~/tt_doc/doc_txt18/Files18/entryfile18.txt"],
                stderr=subprocess.PIPE)
            print("Result SCP transfert : %s" % repr(proc.stderr))
            if proc.stderr == b'':
                print("[upload] File entryfile18.txt uploaded !")
                #messagebox.showinfo("INFO", "entryfile18.txt uploaded...")
            else:
                print("[!] No file to upload !")
                messagebox.showerror("Error", "No entryfile18.txt to upload...")

            if os.path.getsize('./newpatient/entryfile18.txt'):
                return

        try:
            if os.path.getsize('./newpatient/entryfile19.txt'):
                print("[+] File 'entryfile19.txt' exist !")
        except FileNotFoundError as outcom19:
            print("[!] Sorry, file 'entryfile19.txt' does not exist !", outcom19)
            with open('./newpatient/entryfile19.txt', 'w') as namefile:
                namefile.write(Patientname + " " + Surname + '\n')
                namefile.write(Birthvalue + '\n')
                namefile.write(Allergia + '\n')
                namefile.write(TransDisVal + '\n')
                namefile.write(Diagnostic + '\n')
            print("[+] File 'entryfile19.txt' created !")

            proc = subprocess.run(["scp", './newpatient/entryfile19.txt',
                "pi@192.168.18.12:~/tt_doc/doc_txt19/Files19/entryfile19.txt"],
                stderr=subprocess.PIPE)
            print("Result SCP transfert : %s" % repr(proc.stderr))
            if proc.stderr == b'':
                print("[upload] File entryfile19.txt uploaded !")
                #messagebox.showinfo("INFO", "entryfile19.txt uploaded...")
            else:
                print("[!] No file to upload !")
                messagebox.showerror("Error", "No entryfile19.txt to upload...")

            if os.path.getsize('./newpatient/entryfile19.txt'):
                return

        try:
            if os.path.getsize('./newpatient/entryfile20.txt'):
                print("[+] File 'entryfile20.txt' exist !")
        except FileNotFoundError as outcom20:
            print("[!] Sorry, file 'entryfile20.txt' does not exist !", outcom20)
            with open('./newpatient/entryfile20.txt', 'w') as namefile:
                namefile.write(Patientname + " " + Surname + '\n')
                namefile.write(Birthvalue + '\n')
                namefile.write(Allergia + '\n')
                namefile.write(TransDisVal + '\n')
                namefile.write(Diagnostic + '\n')
            print("[+] File 'entryfile20.txt' created !")

            proc = subprocess.run(["scp", './newpatient/entryfile20.txt',
                "pi@192.168.18.12:~/tt_doc/doc_txt20/Files20/entryfile20.txt"],
                stderr=subprocess.PIPE)
            print("Result SCP transfert : %s" % repr(proc.stderr))
            if proc.stderr == b'':
                print("[upload] File entryfile20.txt uploaded !")
                #messagebox.showinfo("INFO", "entryfile20.txt uploaded...")
            else:
                print("[!] No file to upload !")
                messagebox.showerror("Error", "No entryfile20.txt to upload...")

            if os.path.getsize('./newpatient/entryfile20.txt'):
                return

        try:
            if os.path.getsize('./newpatient/entryfile21.txt'):
                print("[+] File 'entryfile21.txt' exist !")
        except FileNotFoundError as outcom21:
            print("[!] Sorry, file 'entryfile21.txt' does not exist !", outcom21)
            with open('./newpatient/entryfile21.txt', 'w') as namefile:
                namefile.write(Patientname + " " + Surname + '\n')
                namefile.write(Birthvalue + '\n')
                namefile.write(Allergia + '\n')
                namefile.write(TransDisVal + '\n')
                namefile.write(Diagnostic + '\n')
            print("[+] File 'entryfile21.txt' created !")

            proc = subprocess.run(["scp", './newpatient/entryfile21.txt',
                "pi@192.168.18.12:~/tt_doc/doc_txt21/Files21/entryfile21.txt"],
                stderr=subprocess.PIPE)
            print("Result SCP transfert : %s" % repr(proc.stderr))
            if proc.stderr == b'':
                print("[upload] File entryfile21.txt uploaded !")
                #messagebox.showinfo("INFO", "entryfile21.txt uploaded...")
            else:
                print("[!] No file to upload !")
                messagebox.showerror("Error", "No entryfile21.txt to upload...")

            if os.path.getsize('./newpatient/entryfile21.txt'):
                return

        try:
            if os.path.getsize('./newpatient/entryfile22.txt'):
                print("[+] File 'entryfile22.txt' exist !")
        except FileNotFoundError as outcom22:
            print("[!] Sorry, file 'entryfile22.txt' does not exist !", outcom22)
            with open('./newpatient/entryfile22.txt', 'w') as namefile:
                namefile.write(Patientname + " " + Surname + '\n')
                namefile.write(Birthvalue + '\n')
                namefile.write(Allergia + '\n')
                namefile.write(TransDisVal + '\n')
                namefile.write(Diagnostic + '\n')
            print("[+] File 'entryfile22.txt' created !")

            proc = subprocess.run(["scp", './newpatient/entryfile22.txt',
                "pi@192.168.18.12:~/tt_doc/doc_txt22/Files22/entryfile22.txt"],
                stderr=subprocess.PIPE)
            print("Result SCP transfert : %s" % repr(proc.stderr))
            if proc.stderr == b'':
                print("[upload] File entryfile22.txt uploaded !")
                #messagebox.showinfo("INFO", "entryfile22.txt uploaded...")
            else:
                print("[!] No file to upload !")
                messagebox.showerror("Error", "No entryfile22.txt to upload...")

            if os.path.getsize('./newpatient/entryfile22.txt'):
                return

        try:
            if os.path.getsize('./newpatient/entryfile23.txt'):
                print("[+] File 'entryfile23.txt' exist !")
        except FileNotFoundError as outcom23:
            print("[!] Sorry, file 'entryfile23.txt' does not exist !", outcom23)
            with open('./newpatient/entryfile23.txt', 'w') as namefile:
                namefile.write(Patientname + " " + Surname + '\n')
                namefile.write(Birthvalue + '\n')
                namefile.write(Allergia + '\n')
                namefile.write(TransDisVal + '\n')
                namefile.write(Diagnostic + '\n')
            print("[+] File 'entryfile23.txt' created !")

            proc = subprocess.run(["scp", './newpatient/entryfile23.txt',
                "pi@192.168.18.12:~/tt_doc/doc_txt23/Files23/entryfile23.txt"],
                stderr=subprocess.PIPE)
            print("Result SCP transfert : %s" % repr(proc.stderr))
            if proc.stderr == b'':
                print("[upload] File entryfile23.txt uploaded !")
                #messagebox.showinfo("INFO", "entryfile23.txt uploaded...")
            else:
                print("[!] No file to upload !")
                messagebox.showerror("Error", "No entryfile23.txt to upload...")

            if os.path.getsize('./newpatient/entryfile23.txt'):
                return

        try:
            if os.path.getsize('./newpatient/entryfile24.txt'):
                print("[+] File 'entryfile24.txt' exist !")
        except FileNotFoundError as outcom24:
            print("[!] Sorry, file 'entryfile24.txt' does not exist !", outcom24)
            with open('./newpatient/entryfile24.txt', 'w') as namefile:
                namefile.write(Patientname + " " + Surname + '\n')
                namefile.write(Birthvalue + '\n')
                namefile.write(Allergia + '\n')
                namefile.write(TransDisVal + '\n')
                namefile.write(Diagnostic + '\n')
            print("[+] File 'entryfile24.txt' created !")

            proc = subprocess.run(["scp", './newpatient/entryfile24.txt',
                "pi@192.168.18.12:~/tt_doc/doc_txt24/Files24/entryfile24.txt"],
                stderr=subprocess.PIPE)
            print("Result SCP transfert : %s" % repr(proc.stderr))
            if proc.stderr == b'':
                print("[upload] File entryfile24.txt uploaded !")
                #messagebox.showinfo("INFO", "entryfile24.txt uploaded...")
            else:
                print("[!] No file to upload !")
                messagebox.showerror("Error", "No entryfile24.txt to upload...")

            if os.path.getsize('./newpatient/entryfile24.txt'):
                return

    #gui.destroy()

labelID = tk.Label(gui, text='ID Number : ',
    font="Times 14 bold",
    fg='white', bg='DodgerBlue2')
labelID.pack(pady=10)

IDpatient = tk.StringVar()
Patient_num = tk.Entry(gui, textvariable=IDpatient,
    highlightbackground='SteelBlue', bd=4)
IDpatient.set('Patient ID')
Patient_num.pack()

labelName = tk.Label(gui, text='Name : ',
    font="Times 14 bold",
    fg='white', bg='DodgerBlue2')
labelName.pack(pady=10)

Patientname = tk.StringVar()
Firstname_pat = tk.Entry(gui, textvariable=Patientname,
    highlightbackground='SteelBlue', bd=4)
Patientname.set('Firstname')
Firstname_pat.pack()

Surname = tk.StringVar()
Sur_pat = tk.Entry(gui, textvariable=Surname,
    highlightbackground='SteelBlue', bd=4)
Surname.set("Lastname")
Sur_pat.pack()

labelBirth = tk.Label(gui, text='Birth Date : ', font="Times 14 bold",
    fg='white', bg='DodgerBlue2')
labelBirth.pack(pady=10)

Birthvalue = tk.StringVar()
Birth_entree = tk.Entry(gui, textvariable=Birthvalue,
    highlightbackground='SteelBlue', bd=4)
Birthvalue.set('Format: 00/00/0000')
Birth_entree.pack()

labelAller = tk.Label(gui, text='Allergy : ',
    font="Times 14 bold",
    fg='white', bg='DodgerBlue2')
labelAller.pack(pady=10)

Allergia = tk.StringVar()
Patient_allergy = tk.Entry(gui, textvariable=Allergia,
    highlightbackground='SteelBlue', bd=4)
Allergia.set('None')
Patient_allergy.pack()

labelTrans = tk.Label(gui, text='Transmissible Disease : ',
    font="Times 14 bold",
    fg='white', bg='DodgerBlue2')
labelTrans.pack(pady=10)

TransDisVal = tk.StringVar()
TransDisease = tk.Entry(gui, textvariable=TransDisVal,
    highlightbackground='SteelBlue', bd=4)
TransDisVal.set('None')
TransDisease.pack()

labelDiag = tk.Label(gui, text='Diagnosis : ',
    font="Times 14 bold",
    fg='white', bg='DodgerBlue2')
labelDiag.pack(pady=10)

Diagnosis = tk.StringVar()
Diagnos_pat = tk.Entry(gui, textvariable=Diagnosis,
    highlightbackground='SteelBlue', bd=4)
Diagnosis.set('Diagnostic (main)')
Diagnos_pat.pack()

bouton1 = tk.Button(gui, text="Enter", width=8, bd=3,
    fg='yellow', bg='RoyalBlue3', highlightbackground='SteelBlue',
    activebackground='pale turquoise',
    command = lambda: get(IDpatient, Patient_num, Patientname, Firstname_pat,
        Surname, Sur_pat, Birthvalue, Birth_entree, Allergia, Patient_allergy, 
        TransDisVal, TransDisease, Diagnosis, Diagnos_pat))
bouton1.pack(side=LEFT, padx=10, pady=20)

buttQuit = tk.Button(gui, text="Quit", width=8, bd=3,
    fg='cyan', bg='RoyalBlue3', highlightbackground='SteelBlue',
    activebackground='pale turquoise', command=quit)
buttQuit.pack(side=tk.LEFT, padx=10, pady=20)

gui.mainloop()
