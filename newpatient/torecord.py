#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
    To record a new patient
    in text zone (entree cap)
"""


from tkinter import *
import tkinter as tk
from tkinter import messagebox
import os
import subprocess
try:
    import pymysql
    pymysql.install_as_MySQLdb()
except ImportError as err_report4:
    print("[!] An error occured about pymysql - torecord.py [!]", err_report4)
    pass


gui = tk.Tk()
gui.title("Add Patient")
gui.configure(bg='DodgerBlue2')
#gui.geometry('300x200')

def get(PatientID, patientnum, Firstname, labelfirst, Surname, lblsurname, 
    Birthvalue, Birth_entree, Allergia, Patient_allergy, TransDisVal, TransDisease,
    Diagnosis, Diagnos_pat):
    """
        Add a patient with
        the add button
    """
    mot = "-"
    mot2 = "--"
    mot3 = "---"
    mot4 = "----"
    mot5 = "-----"
    mot6 = "------"
    mot7 = "-------"
    mot8 = "--------"
    mot9 = "---------"
    mot10 = "----------"
    mot11 = "-----------"
    mot12 = "------------"
    mot13 = "-------------"
    mot14 = "--------------"
    mot15 = "---------------"
    mot16 = "----------------"
    mot17 = "-----------------"
    mot18 = "------------------"
    mot19 = "-------------------"
    mot20 = "--------------------"
    mot21 = "---------------------"
    mot22 = "----------------------"
    mot23 = "-----------------------"
    mot24 = "------------------------"

    PatientID = patientnum.get()
    Firstname = labelfirst.get()
    Surname = lblsurname.get()
    Birthvalue = Birth_entree.get()
    Allergia = Patient_allergy.get()
    TransDisVal = TransDisease.get()
    Diagnosis = Diagnos_pat.get()

    if patientnum.get() == "" or labelfirst.get() == "" or lblsurname.get() == "":
        messagebox.showerror("MySQL Connection", "No data to record !")
    else:
        sqlCon = pymysql.connect(host='192.168.18.12', port=3306, user='koala33',
            password='Ko@l@tr3379', database='timetrackconn')
        cur = sqlCon.cursor()
        cur.execute("INSERT into timetrackconn values (%s, %s, %s, %s, %s, %s, %s)",(
        patientnum.get(),
        labelfirst.get(),
        lblsurname.get(),
        Birth_entree.get(),
        Patient_allergy.get(),
        TransDisease.get(),
        Diagnos_pat.get(),
        ))
        sqlCon.commit()
        sqlCon.close()
        messagebox.showinfo("MySQL connection", "Record Entered Successfully !")

    if mot == '-':
        if os.path.getsize('./newpatient/entryfile.txt'):
            with open('./newpatient/entryfile.txt', 'r') as file1:
                lines = file1.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot in line:
                        searchLine1(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis)
    else:
        pass

    if mot2 == '--':
        if os.path.getsize('./newpatient/entryfile2.txt'):
            with open('./newpatient/entryfile2.txt', 'r') as file2:
                lines = file2.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot2 in line:
                        searchLine2(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis)
    else:
        pass

    if mot3 == '---':
        if os.path.getsize('./newpatient/entryfile3.txt'):
            with open('./newpatient/entryfile3.txt', 'r') as file3:
                lines = file3.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot3 in line:
                        searchLine3(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis)
    else:
        pass

    if mot4 == '----':
        if os.path.getsize('./newpatient/entryfile4.txt'):
            with open('./newpatient/entryfile4.txt', 'r') as file4:
                lines = file4.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot4 in line:
                        searchLine4(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis)
    else:
        pass

    if mot5 == '-----':
        if os.path.getsize('./newpatient/entryfile5.txt'):
            with open('./newpatient/entryfile5.txt', 'r') as file5:
                lines = file5.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot5 in line:
                        searchLine5(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis)
    else:
        pass

    if mot6 == '------':
        if os.path.getsize('./newpatient/entryfile6.txt'):
            with open('./newpatient/entryfile6.txt', 'r') as file6:
                lines = file6.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot6 in line:
                        searchLine6(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis)
    else:
        pass

    if mot7 == '-------':
        if os.path.getsize('./newpatient/entryfile7.txt'):
            with open('./newpatient/entryfile7.txt', 'r') as file7:
                lines = file7.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot7 in line:
                        searchLine7(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis)
    else:
        pass

    if mot8 == '--------':
        if os.path.getsize('./newpatient/entryfile8.txt'):
            with open('./newpatient/entryfile8.txt', 'r') as file8:
                lines = file8.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot8 in line:
                        searchLine8(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis)
    else:
        pass

    if mot9 == '---------':
        if os.path.getsize('./newpatient/entryfile9.txt'):
            with open('./newpatient/entryfile9.txt', 'r') as file9:
                lines = file9.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot9 in line:
                        searchLine9(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis)
    else:
        pass

    if mot10 == '----------':
        if os.path.getsize('./newpatient/entryfile10.txt'):
            with open('./newpatient/entryfile10.txt', 'r') as file10:
                lines = file10.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot10 in line:
                        searchLine10(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis)
    else:
        pass

    if mot11 == '-----------':
        if os.path.getsize('./newpatient/entryfile11.txt'):
            with open('./newpatient/entryfile11.txt', 'r') as file11:
                lines = file11.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot11 in line:
                        searchLine11(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis)
    else:
        pass

    if mot12 == '------------':
        if os.path.getsize('./newpatient/entryfile12.txt'):
            with open('./newpatient/entryfile12.txt', 'r') as file12:
                lines = file12.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot12 in line:
                        searchLine12(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis)
    else:
        pass

    if mot13 == '-------------':
        if os.path.getsize('./newpatient/entryfile13.txt'):
            with open('./newpatient/entryfile13.txt', 'r') as file13:
                lines = file13.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot13 in line:
                        searchLine13(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis)
    else:
        pass

    if mot14 == '--------------':
        if os.path.getsize('./newpatient/entryfile14.txt'):
            with open('./newpatient/entryfile14.txt', 'r') as file14:
                lines = file14.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot14 in line:
                        searchLine14(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis)
    else:
        pass

    if mot15 == '---------------':
        if os.path.getsize('./newpatient/entryfile15.txt'):
            with open('./newpatient/entryfile15.txt', 'r') as file15:
                lines = file15.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot15 in line:
                        searchLine15(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis)
    else:
        pass

    if mot16 == '----------------':
        if os.path.getsize('./newpatient/entryfile16.txt'):
            with open('./newpatient/entryfile16.txt', 'r') as file16:
                lines = file16.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot16 in line:
                        searchLine16(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis)
    else:
        pass

    if mot17 == '-----------------':
        if os.path.getsize('./newpatient/entryfile17.txt'):
            with open('./newpatient/entryfile17.txt', 'r') as file17:
                lines = file17.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot17 in line:
                        searchLine17(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis)
    else:
        pass

    if mot18 == '------------------':
        if os.path.getsize('./newpatient/entryfile18.txt'):
            with open('./newpatient/entryfile18.txt', 'r') as file18:
                lines = file18.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot18 in line:
                        searchLine18(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis)
    else:
        pass

    if mot19 == '-------------------':
        if os.path.getsize('./newpatient/entryfile19.txt'):
            with open('./newpatient/entryfile19.txt', 'r') as file19:
                lines = file19.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot19 in line:
                        searchLine19(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis)
    else:
        pass

    if mot20 == '--------------------':
        if os.path.getsize('./newpatient/entryfile20.txt'):
            with open('./newpatient/entryfile20.txt', 'r') as file20:
                lines = file20.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot20 in line:
                        searchLine20(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis)
    else:
        pass

    if mot21 == '---------------------':
        if os.path.getsize('./newpatient/entryfile21.txt'):
            with open('./newpatient/entryfile21.txt', 'r') as file21:
                lines = file21.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot21 in line:
                        searchLine21(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis)
    else:
        pass

    if mot22 == '----------------------':
        if os.path.getsize('./newpatient/entryfile22.txt'):
            with open('./newpatient/entryfile22.txt', 'r') as file22:
                lines = file22.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot22 in line:
                        searchLine22(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis)
    else:
        pass

    if mot23 == '-----------------------':
        if os.path.getsize('./newpatient/entryfile23.txt'):
            with open('./newpatient/entryfile23.txt', 'r') as file23:
                lines = file23.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot23 in line:
                        searchLine23(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis)
    else:
        pass

    if mot24 == '------------------------':
        if os.path.getsize('./newpatient/entryfile24.txt'):
            with open('./newpatient/entryfile24.txt', 'r') as file24:
                lines = file24.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot24 in line:
                        searchLine24(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis)
    else:
        print("There is no file to edit as entryfile")

    gui.destroy()

def searchLine1(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis):
    """
        To save new patient name
        by a msgbox and write the
        new name in an entryfile.txt
        To upload data record to server !
    """
    MsgBox = messagebox.askyesno('Save data', 'Do you want to save ?')
    if MsgBox == 1:
        with open('./newpatient/entryfile.txt', 'w') as file:
            file.write(Firstname + " " + Surname + '\n')
            file.write(Birthvalue + '\n')
            file.write(Allergia + '\n')
            file.write(TransDisVal + '\n')
            file.write(Diagnosis + '\n')

        proc = subprocess.run(["scp", './newpatient/entryfile.txt',
            "pi@192.168.18.12:~/tt_doc/doc_txt1/Files1/entryfile.txt"],
            stderr=subprocess.PIPE)
        print("Result SCP transfert : %s" % repr(proc.stderr))
        if proc.stderr == b'':
            print("[+] File entryfile.txt uploaded !")
            #messagebox.showinfo("INFO", "entryfile.txt uploaded...")
        else:
            print("[!] No file to upload !")
            messagebox.showerror("Error", "No entryfile.txt to upload...")

def searchLine2(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis):
    MsgBox2 = messagebox.askyesno('Save data', 'Do you want to save for patient 2 ?')
    if MsgBox2 == 1:
        with open('./newpatient/entryfile2.txt', 'w') as file2:
            file2.write(Firstname + " " + Surname + '\n')
            file2.write(Birthvalue + '\n')
            file2.write(Allergia + '\n')
            file2.write(TransDisVal + '\n')
            file2.write(Diagnosis + '\n')

        proc = subprocess.run(["scp", './newpatient/entryfile2.txt',
            "pi@192.168.18.12:~/tt_doc/doc_txt2/Files2/entryfile2.txt"],
            stderr=subprocess.PIPE)
        print("Result SCP transfert : %s" % repr(proc.stderr))
        if proc.stderr == b'':
            print("[+] File entryfile2.txt uploaded !")
            #messagebox.showinfo("INFO", "entryfile2.txt uploaded...")
        else:
            print("[!] No file to upload !")
            messagebox.showerror("Error", "No entryfile2.txt to upload...")

def searchLine3(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis):
    MsgBox3 = messagebox.askyesno('Save data', 'Do you want to save for patient 3 ?')
    if MsgBox3 == 1:
        with open('./newpatient/entryfile3.txt', 'w') as file3:
            file3.write(Firstname + " " + Surname + '\n')
            file3.write(Birthvalue + '\n')
            file3.write(Allergia + '\n')
            file3.write(TransDisVal + '\n')
            file3.write(Diagnosis + '\n')

        proc = subprocess.run(["scp", './newpatient/entryfile3.txt',
            "pi@192.168.18.12:~/tt_doc/doc_txt3/Files3/entryfile3.txt"],
            stderr=subprocess.PIPE)
        print("Result SCP transfert : %s" % repr(proc.stderr))
        if proc.stderr == b'':
            print("[+] File entryfile3.txt uploaded !")
            #messagebox.showinfo("INFO", "entryfile3.txt uploaded...")
        else:
            print("[!] No file to upload !")
            messagebox.showerror("Error", "No entryfile3.txt to upload...")

def searchLine4(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis):
    MsgBox4 = messagebox.askyesno('Save data', 'Do you want to save for patient 4 ?')
    if MsgBox4 == 1:
        with open('./newpatient/entryfile4.txt', 'w') as file4:
            file4.write(Firstname + " " + Surname + '\n')
            file4.write(Birthvalue + '\n')
            file4.write(Allergia + '\n')
            file4.write(TransDisVal + '\n')
            file4.write(Diagnosis + '\n')

        proc = subprocess.run(["scp", './newpatient/entryfile4.txt',
            "pi@192.168.18.12:~/tt_doc/doc_txt4/Files4/entryfile4.txt"],
            stderr=subprocess.PIPE)
        print("Result SCP transfert : %s" % repr(proc.stderr))
        if proc.stderr == b'':
            print("[+] File entryfile4.txt uploaded !")
            #messagebox.showinfo("INFO", "entryfile4.txt uploaded...")
        else:
            print("[!] No file to upload !")
            messagebox.showerror("Error", "No entryfile4.txt to upload...")

def searchLine5(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis):
    MsgBox5 = messagebox.askyesno('Save data', 'Do you want to save for patient 5 ?')
    if MsgBox5 == 1:
        with open('./newpatient/entryfile5.txt', 'w') as file5:
            file5.write(Firstname + " " + Surname + '\n')
            file5.write(Birthvalue + '\n')
            file5.write(Allergia + '\n')
            file5.write(TransDisVal + '\n')
            file5.write(Diagnosis + '\n')

        proc = subprocess.run(["scp", './newpatient/entryfile5.txt',
            "pi@192.168.18.12:~/tt_doc/doc_txt5/Files5/entryfile5.txt"],
            stderr=subprocess.PIPE)
        print("Result SCP transfert : %s" % repr(proc.stderr))
        if proc.stderr == b'':
            print("[+] File entryfile5.txt uploaded !")
            #messagebox.showinfo("INFO", "entryfile5.txt uploaded...")
        else:
            print("[!] No file to upload !")
            messagebox.showerror("Error", "No entryfile5.txt to upload...")

def searchLine6(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis):
    MsgBox6 = messagebox.askyesno('Save data', 'Do you want to save for patient 6 ?')
    if MsgBox6 == 1:
        with open('./newpatient/entryfile6.txt', 'w') as file6:
            file6.write(Firstname + " " + Surname + '\n')
            file6.write(Birthvalue + '\n')
            file6.write(Allergia + '\n')
            file6.write(TransDisVal + '\n')
            file6.write(Diagnosis + '\n')

        proc = subprocess.run(["scp", './newpatient/entryfile6.txt',
            "pi@192.168.18.12:~/tt_doc/doc_txt6/Files6/entryfile6.txt"],
            stderr=subprocess.PIPE)
        print("Result SCP transfert : %s" % repr(proc.stderr))
        if proc.stderr == b'':
            print("[+] File entryfile6.txt uploaded !")
            #messagebox.showinfo("INFO", "entryfile6.txt uploaded...")
        else:
            print("[!] No file to upload !")
            messagebox.showerror("Error", "No entryfile6.txt to upload...")

def searchLine7(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis):
    MsgBox7 = messagebox.askyesno('Save data', 'Do you want to save for patient 7 ?')
    if MsgBox7 == 1:
        with open('./newpatient/entryfile7.txt', 'w') as file7:
            file7.write(Firstname + " " + Surname + '\n')
            file7.write(Birthvalue + '\n')
            file7.write(Allergia + '\n')
            file7.write(TransDisVal + '\n')
            file7.write(Diagnosis + '\n')

        proc = subprocess.run(["scp", './newpatient/entryfile7.txt',
            "pi@192.168.18.12:~/tt_doc/doc_txt7/Files7/entryfile7.txt"],
            stderr=subprocess.PIPE)
        print("Result SCP transfert : %s" % repr(proc.stderr))
        if proc.stderr == b'':
            print("[+] File entryfile7.txt uploaded !")
            #messagebox.showinfo("INFO", "entryfile7.txt uploaded...")
        else:
            print("[!] No file to upload !")
            messagebox.showerror("Error", "No entryfile7.txt to upload...")

def searchLine8(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis):
    MsgBox8 = messagebox.askyesno('Save data', 'Do you want to save for patient 8 ?')
    if MsgBox8 == 1:
        with open('./newpatient/entryfile8.txt', 'w') as file8:
            file8.write(Firstname + " " + Surname + '\n')
            file8.write(Birthvalue + '\n')
            file8.write(Allergia + '\n')
            file8.write(TransDisVal + '\n')
            file8.write(Diagnosis + '\n')

        proc = subprocess.run(["scp", './newpatient/entryfile8.txt',
            "pi@192.168.18.12:~/tt_doc/doc_txt8/Files8/entryfile8.txt"],
            stderr=subprocess.PIPE)
        print("Result SCP transfert : %s" % repr(proc.stderr))
        if proc.stderr == b'':
            print("[+] File entryfile8.txt uploaded !")
            #messagebox.showinfo("INFO", "entryfile8.txt uploaded...")
        else:
            print("[!] No file to upload !")
            messagebox.showerror("Error", "No entryfile8.txt to upload...")

def searchLine9(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis):
    MsgBox9 = messagebox.askyesno('Save data', 'Do you want to save for patient 9 ?')
    if MsgBox9 == 1:
        with open('./newpatient/entryfile9.txt', 'w') as file9:
            file9.write(Firstname + " " + Surname + '\n')
            file9.write(Birthvalue + '\n')
            file9.write(Allergia + '\n')
            file9.write(TransDisVal + '\n')
            file9.write(Diagnosis + '\n')

        proc = subprocess.run(["scp", './newpatient/entryfile9.txt',
            "pi@192.168.18.12:~/tt_doc/doc_txt9/Files9/entryfile9.txt"],
            stderr=subprocess.PIPE)
        print("Result SCP transfert : %s" % repr(proc.stderr))
        if proc.stderr == b'':
            print("[+] File entryfile9.txt uploaded !")
            #messagebox.showinfo("INFO", "entryfile9.txt uploaded...")
        else:
            print("[!] No file to upload !")
            messagebox.showerror("Error", "No entryfile9.txt to upload...")

def searchLine10(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis):
    MsgBox10 = messagebox.askyesno('Save data', 'Do you want to save for patient 10 ?')
    if MsgBox10 == 1:
        with open('./newpatient/entryfile10.txt', 'w') as file10:
            file10.write(Firstname + " " + Surname + '\n')
            file10.write(Birthvalue + '\n')
            file10.write(Allergia + '\n')
            file10.write(TransDisVal + '\n')
            file10.write(Diagnosis + '\n')

        proc = subprocess.run(["scp", './newpatient/entryfile10.txt',
            "pi@192.168.18.12:~/tt_doc/doc_txt10/Files10/entryfile10.txt"],
            stderr=subprocess.PIPE)
        print("Result SCP transfert : %s" % repr(proc.stderr))
        if proc.stderr == b'':
            print("[+] File entryfile10.txt uploaded !")
            #messagebox.showinfo("INFO", "entryfile10.txt uploaded...")
        else:
            print("[!] No file to upload !")
            messagebox.showerror("Error", "No entryfile10.txt to upload...")

def searchLine11(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis):
    MsgBox11 = messagebox.askyesno('Save data', 'Do you want to save for patient 11 ?')
    if MsgBox11 == 1:
        with open('./newpatient/entryfile11.txt', 'w') as file11:
            file11.write(Firstname + " " + Surname + '\n')
            file11.write(Birthvalue + '\n')
            file11.write(Allergia + '\n')
            file11.write(TransDisVal + '\n')
            file11.write(Diagnosis + '\n')

        proc = subprocess.run(["scp", './newpatient/entryfile11.txt',
            "pi@192.168.18.12:~/tt_doc/doc_txt11/Files11/entryfile11.txt"],
            stderr=subprocess.PIPE)
        print("Result SCP transfert : %s" % repr(proc.stderr))
        if proc.stderr == b'':
            print("[+] File entryfile11.txt uploaded !")
            #messagebox.showinfo("INFO", "entryfile11.txt uploaded...")
        else:
            print("[!] No file to upload !")
            messagebox.showerror("Error", "No entryfile11.txt to upload...")

def searchLine12(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis):
    MsgBox12 = messagebox.askyesno('Save data', 'Do you want to save for patient 12 ?')
    if MsgBox12 == 1:
        with open('./newpatient/entryfile12.txt', 'w') as file12:
            file12.write(Firstname + " " + Surname + '\n')
            file12.write(Birthvalue + '\n')
            file12.write(Allergia + '\n')
            file12.write(TransDisVal + '\n')
            file12.write(Diagnosis + '\n')

        proc = subprocess.run(["scp", './newpatient/entryfile12.txt',
            "pi@192.168.18.12:~/tt_doc/doc_txt12/Files12/entryfile12.txt"],
            stderr=subprocess.PIPE)
        print("Result SCP transfert : %s" % repr(proc.stderr))
        if proc.stderr == b'':
            print("[+] File entryfile12.txt uploaded !")
            #messagebox.showinfo("INFO", "entryfile12.txt uploaded...")
        else:
            print("[!] No file to upload !")
            messagebox.showerror("Error", "No entryfile12.txt to upload...")

def searchLine13(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis):
    MsgBox13 = messagebox.askyesno('Save data', 'Do you want to save for patient 13 ?')
    if MsgBox13 == 1:
        with open('./newpatient/entryfile13.txt', 'w') as file13:
            file13.write(Firstname + " " + Surname + '\n')
            file13.write(Birthvalue + '\n')
            file13.write(Allergia + '\n')
            file13.write(TransDisVal + '\n')
            file13.write(Diagnosis + '\n')

        proc = subprocess.run(["scp", './newpatient/entryfile13.txt',
            "pi@192.168.18.12:~/tt_doc/doc_txt13/Files13/entryfile13.txt"],
            stderr=subprocess.PIPE)
        print("Result SCP transfert : %s" % repr(proc.stderr))
        if proc.stderr == b'':
            print("[+] File entryfile13.txt uploaded !")
            #messagebox.showinfo("INFO", "entryfile13.txt uploaded...")
        else:
            print("[!] No file to upload !")
            messagebox.showerror("Error", "No entryfile13.txt to upload...")

def searchLine14(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis):
    MsgBox14 = messagebox.askyesno('Save data', 'Do you want to save for patient 14 ?')
    if MsgBox14 == 1:
        with open('./newpatient/entryfile14.txt', 'w') as file14:
            file14.write(Firstname + " " + Surname + '\n')
            file14.write(Birthvalue + '\n')
            file14.write(Allergia + '\n')
            file14.write(TransDisVal + '\n')
            file14.write(Diagnosis + '\n')

        proc = subprocess.run(["scp", './newpatient/entryfile14.txt',
            "pi@192.168.18.12:~/tt_doc/doc_txt14/Files14/entryfile14.txt"],
            stderr=subprocess.PIPE)
        print("Result SCP transfert : %s" % repr(proc.stderr))
        if proc.stderr == b'':
            print("[+] File entryfile14.txt uploaded !")
            #messagebox.showinfo("INFO", "entryfile14.txt uploaded...")
        else:
            print("[!] No file to upload !")
            messagebox.showerror("Error", "No entryfile14.txt to upload...")

def searchLine15(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis):
    MsgBox15 = messagebox.askyesno('Save data', 'Do you want to save for patient 15 ?')
    if MsgBox15 == 1:
        with open('./newpatient/entryfile15.txt', 'w') as file15:
            file15.write(Firstname + " " + Surname + '\n')
            file15.write(Birthvalue + '\n')
            file15.write(Allergia + '\n')
            file15.write(TransDisVal + '\n')
            file15.write(Diagnosis + '\n')

        proc = subprocess.run(["scp", './newpatient/entryfile15.txt',
            "pi@192.168.18.12:~/tt_doc/doc_txt15/Files15/entryfile15.txt"],
            stderr=subprocess.PIPE)
        print("Result SCP transfert : %s" % repr(proc.stderr))
        if proc.stderr == b'':
            print("[+] File entryfile15.txt uploaded !")
            #messagebox.showinfo("INFO", "entryfile15.txt uploaded...")
        else:
            print("[!] No file to upload !")
            messagebox.showerror("Error", "No entryfile15.txt to upload...")

def searchLine16(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis):
    MsgBox16 = messagebox.askyesno('Save data', 'Do you want to save for patient 16 ?')
    if MsgBox16 == 1:
        with open('./newpatient/entryfile16.txt', 'w') as file16:
            file16.write(Firstname + " " + Surname + '\n')
            file16.write(Birthvalue + '\n')
            file16.write(Allergia + '\n')
            file16.write(TransDisVal + '\n')
            file16.write(Diagnosis + '\n')

        proc = subprocess.run(["scp", './newpatient/entryfile16.txt',
            "pi@192.168.18.12:~/tt_doc/doc_txt16/Files16/entryfile16.txt"],
            stderr=subprocess.PIPE)
        print("Result SCP transfert : %s" % repr(proc.stderr))
        if proc.stderr == b'':
            print("[+] File entryfile16.txt uploaded !")
            #messagebox.showinfo("INFO", "entryfile16.txt uploaded...")
        else:
            print("[!] No file to upload !")
            messagebox.showerror("Error", "No entryfile16.txt to upload...")

def searchLine17(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis):
    MsgBox17 = messagebox.askyesno('Save data', 'Do you want to save for patient 17 ?')
    if MsgBox17 == 1:
        with open('./newpatient/entryfile17.txt', 'w') as file17:
            file17.write(Firstname + " " + Surname + '\n')
            file17.write(Birthvalue + '\n')
            file17.write(Allergia + '\n')
            file17.write(TransDisVal + '\n')
            file17.write(Diagnosis + '\n')

        proc = subprocess.run(["scp", './newpatient/entryfile17.txt',
            "pi@192.168.18.12:~/tt_doc/doc_txt17/Files17/entryfile17.txt"],
            stderr=subprocess.PIPE)
        print("Result SCP transfert : %s" % repr(proc.stderr))
        if proc.stderr == b'':
            print("[+] File entryfile17.txt uploaded !")
            #messagebox.showinfo("INFO", "entryfile17.txt uploaded...")
        else:
            print("[!] No file to upload !")
            messagebox.showerror("Error", "No entryfile17.txt to upload...")

def searchLine18(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis):
    MsgBox18 = messagebox.askyesno('Save data', 'Do you want to save for patient 18 ?')
    if MsgBox18 == 1:
        with open('./newpatient/entryfile18.txt', 'w') as file18:
            file18.write(Firstname + " " + Surname + '\n')
            file18.write(Birthvalue + '\n')
            file18.write(Allergia + '\n')
            file18.write(TransDisVal + '\n')
            file18.write(Diagnosis + '\n')

        proc = subprocess.run(["scp", './newpatient/entryfile18.txt',
            "pi@192.168.18.12:~/tt_doc/doc_txt18/Files18/entryfile18.txt"],
            stderr=subprocess.PIPE)
        print("Result SCP transfert : %s" % repr(proc.stderr))
        if proc.stderr == b'':
            print("[+] File entryfile18.txt uploaded !")
            #messagebox.showinfo("INFO", "entryfile18.txt uploaded...")
        else:
            print("[!] No file to upload !")
            messagebox.showerror("Error", "No entryfile18.txt to upload...")

def searchLine19(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis):
    MsgBox19 = messagebox.askyesno('Save data', 'Do you want to save for patient 19 ?')
    if MsgBox19 == 1:
        with open('./newpatient/entryfile19.txt', 'w') as file19:
            file19.write(Firstname + " " + Surname + '\n')
            file19.write(Birthvalue + '\n')
            file19.write(Allergia + '\n')
            file19.write(TransDisVal + '\n')
            file19.write(Diagnosis + '\n')

        proc = subprocess.run(["scp", './newpatient/entryfile19.txt',
            "pi@192.168.18.12:~/tt_doc/doc_txt19/Files19/entryfile19.txt"],
            stderr=subprocess.PIPE)
        print("Result SCP transfert : %s" % repr(proc.stderr))
        if proc.stderr == b'':
            print("[+] File entryfile19.txt uploaded !")
            #messagebox.showinfo("INFO", "entryfile19.txt uploaded...")
        else:
            print("[!] No file to upload !")
            messagebox.showerror("Error", "No entryfile19.txt to upload...")

def searchLine20(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis):
    MsgBox20 = messagebox.askyesno('Save data', 'Do you want to save for patient 20 ?')
    if MsgBox20 == 1:
        with open('./newpatient/entryfile20.txt', 'w') as file20:
            file20.write(Firstname + " " + Surname + '\n')
            file20.write(Birthvalue + '\n')
            file20.write(Allergia + '\n')
            file20.write(TransDisVal + '\n')
            file20.write(Diagnosis + '\n')

        proc = subprocess.run(["scp", './newpatient/entryfile20.txt',
            "pi@192.168.18.12:~/tt_doc/doc_txt20/Files20/entryfile20.txt"],
            stderr=subprocess.PIPE)
        print("Result SCP transfert : %s" % repr(proc.stderr))
        if proc.stderr == b'':
            print("[+] File entryfile20.txt uploaded !")
            #messagebox.showinfo("INFO", "entryfile20.txt uploaded...")
        else:
            print("[!] No file to upload !")
            messagebox.showerror("Error", "No entryfile20.txt to upload...")

def searchLine21(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis):
    MsgBox21 = messagebox.askyesno('Save data', 'Do you want to save for patient 21 ?')
    if MsgBox21 == 1:
        with open('./newpatient/entryfile21.txt', 'w') as file21:
            file21.write(Firstname + " " + Surname + '\n')
            file21.write(Birthvalue + '\n')
            file21.write(Allergia + '\n')
            file21.write(TransDisVal + '\n')
            file21.write(Diagnosis + '\n')

        proc = subprocess.run(["scp", './newpatient/entryfile21.txt',
            "pi@192.168.18.12:~/tt_doc/doc_txt21/Files21/entryfile21.txt"],
            stderr=subprocess.PIPE)
        print("Result SCP transfert : %s" % repr(proc.stderr))
        if proc.stderr == b'':
            print("[+] File entryfile21.txt uploaded !")
            #messagebox.showinfo("INFO", "entryfile21.txt uploaded...")
        else:
            print("[!] No file to upload !")
            messagebox.showerror("Error", "No entryfile21.txt to upload...")

def searchLine22(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis):
    MsgBox22 = messagebox.askyesno('Save data', 'Do you want to save for patient 22 ?')
    if MsgBox22 == 1:
        with open('./newpatient/entryfile22.txt', 'w') as file22:
            file22.write(Firstname + " " + Surname + '\n')
            file22.write(Birthvalue + '\n')
            file22.write(Allergia + '\n')
            file22.write(TransDisVal + '\n')
            file22.write(Diagnosis + '\n')

        proc = subprocess.run(["scp", './newpatient/entryfile22.txt',
            "pi@192.168.18.12:~/tt_doc/doc_txt22/Files22/entryfile22.txt"],
            stderr=subprocess.PIPE)
        print("Result SCP transfert : %s" % repr(proc.stderr))
        if proc.stderr == b'':
            print("[+] File entryfile22.txt uploaded !")
            #messagebox.showinfo("INFO", "entryfile22.txt uploaded...")
        else:
            print("[!] No file to upload !")
            messagebox.showerror("Error", "No entryfile22.txt to upload...")

def searchLine23(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis):
    MsgBox23 = messagebox.askyesno('Save data', 'Do you want to save for patient 23 ?')
    if MsgBox23 == 1:
        with open('./newpatient/entryfile23.txt', 'w') as file23:
            file23.write(Firstname + " " + Surname + '\n')
            file23.write(Birthvalue + '\n')
            file23.write(Allergia + '\n')
            file23.write(TransDisVal + '\n')
            file23.write(Diagnosis + '\n')

        proc = subprocess.run(["scp", './newpatient/entryfile23.txt',
            "pi@192.168.18.12:~/tt_doc/doc_txt23/Files23/entryfile23.txt"],
            stderr=subprocess.PIPE)
        print("Result SCP transfert : %s" % repr(proc.stderr))
        if proc.stderr == b'':
            print("[+] File entryfile23.txt uploaded !")
            #messagebox.showinfo("INFO", "entryfile23.txt uploaded...")
        else:
            print("[!] No file to upload !")
            messagebox.showerror("Error", "No entryfile23.txt to upload...")

def searchLine24(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis):
    MsgBox24 = messagebox.askyesno('Save data', 'Do you want to save for patient 24 ?')
    if MsgBox24 == 1:
        with open('./newpatient/entryfile24.txt', 'w') as file24:
            file24.write(Firstname + " " + Surname + '\n')
            file24.write(Birthvalue + '\n')
            file24.write(Allergia + '\n')
            file24.write(TransDisVal + '\n')
            file24.write(Diagnosis + '\n')

        proc = subprocess.run(["scp", './newpatient/entryfile24.txt',
            "pi@192.168.18.12:~/tt_doc/doc_txt24/Files24/entryfile24.txt"],
            stderr=subprocess.PIPE)
        print("Result SCP transfert : %s" % repr(proc.stderr))
        if proc.stderr == b'':
            print("[+] File entryfile24.txt uploaded !")
            #messagebox.showinfo("INFO", "entryfile24.txt uploaded...")
        else:
            print("[!] No file to upload !")
            messagebox.showerror("Error", "No entryfile24.txt to upload...")

labelID = tk.Label(gui, text='ID Number: ',
    font="Times 14 bold",
    fg='white', bg='DodgerBlue2')
labelID.pack(pady=10)

PatientID = tk.StringVar()
patientnum = tk.Entry(gui, textvariable=PatientID,
    highlightbackground='SteelBlue', bd=4)
PatientID.set('Patient ID')
patientnum.pack()

labelName = tk.Label(gui, text='Name : ',
    font="Times 14 bold",
    fg='white', bg='DodgerBlue2')
labelName.pack(pady=10)

Firstname = tk.StringVar()
labelfirst = tk.Entry(gui, textvariable=Firstname,
    highlightbackground='DodgerBlue2', bd=4)
Firstname.set('Firstname')
labelfirst.pack()

Surname = tk.StringVar()
lblsurname = tk.Entry(gui, textvariable=Surname,
    highlightbackground='SteelBlue', bd=4)
Surname.set('Lastname')
lblsurname.pack()

labelBirth = tk.Label(gui, text='Birth Date : ', font="Times 14 bold",
    fg='white', bg='DodgerBlue2')
labelBirth.pack(pady=10)

Birthvalue = tk.StringVar()
Birth_entree = tk.Entry(gui, textvariable=Birthvalue,
    highlightbackground='SteelBlue', bd=4)
Birthvalue.set('Format: 00/00/0000')
Birth_entree.pack()

labelAller = tk.Label(gui)
labelAller = Label(text='Allergy : ',
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

bouton1 = tk.Button(gui, text="Enter", width=8, bd=4,
    fg='yellow', bg='RoyalBlue3', highlightbackground='SteelBlue',
    activebackground='pale turquoise',
    command = lambda: get(PatientID, patientnum, Firstname, labelfirst,
        Surname, lblsurname, Birthvalue, Birth_entree, Allergia,
        Patient_allergy, TransDisVal, TransDisease, Diagnosis, Diagnos_pat))
bouton1.pack(side=LEFT, padx=10, pady=20)

buttQuit = tk.Button(gui, text="Quit", width=8, bd=4,
    fg='cyan', bg='RoyalBlue3', highlightbackground='SteelBlue',
    activebackground='pale turquoise', command=quit)
buttQuit.pack(side=tk.LEFT, padx=10, pady=20)

gui.mainloop()
