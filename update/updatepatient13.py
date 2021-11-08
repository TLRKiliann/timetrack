#!/usr/bin/python3
# -*- coding: utf-8 -*-


import tkinter as tk
from tkinter import messagebox
import os
import subprocess
try:
    import pymysql
    pymysql.install_as_MySQLdb()
except ImportError as err_report:
    print("[!] An error occured about pymysql - updatepatient13.py [!]", err_report)
    pass


gui = tk.Tk()
gui.title("Update")
gui.configure(bg='DodgerBlue2')

# Interact with database to search data
def searchDB():
    """
        To search patient by ID
        and display data into
        each GUI entree.
    """
    try:
        sqlCon = pymysql.connect(host='192.168.18.12', port=3306, user='koala33',
            password='Ko@l@tr3379', database='timetrackconn')
        cur = sqlCon.cursor()
        cur.execute("SELECT * from timetrackconn where stdid=%s", patient_num.get())
        row = cur.fetchone()
        idpatient.set(row[0])
        firstpat.set(row[1])
        surname.set(row[2])
        birthvalue.set(row[3])
        allergia.set(row[4])
        transdisval.set(row[5])
        diagnosis.set(row[6])
        sqlCon.commit()
        sqlCon.close()
    except:
        print("Error with function search in DB")
        tk.messagebox.showwarning('Warning', 'Database no connected !')
        print("Database no connected !")

def diagRecapt(diagnosis):
    try:
        if os.path.getsize('./diag/doc_diag13/diagrecap13.txt'):
            with open('./diag/doc_diag13/diagrecap13.txt', 'a+') as filediag:
                filediag.write(diagnosis + '\n')

            tk.messagebox.showinfo("Info", "Data was updated for entryfile13.txt, "\
                "allergyfile13.txt !")
    except FileNotFoundError as not_ffile:
        print("- diagrecap13.txt not found, plz create file clicking on diagnostic -")
        print(str(not_ffile))
        tk.messagebox.showwarning("WARNING", "File diagrecap13.txt not found ! "\
            "Please, create one by clicking on diagnostic 'add'.")

def searchLineName10(firstpat, surname, birthvalue,
    allergia, transdisval, diagnosis):
    """
        To save changing data for
        entryfile13.txt and display
        tk.messagebox.
    """
    MsgBox = tk.messagebox.askyesno('Save data', 'Do you want to save ?')
    if MsgBox == 1:
        with open('./newpatient/entryfile13.txt', 'w') as fullfile:
            fullfile.write(firstpat + " " + surname + '\n')
            fullfile.write(birthvalue + '\n')
            fullfile.write(allergia + '\n')
            fullfile.write(transdisval + '\n')
            fullfile.write(diagnosis + '\n')

        with open('./allergy/allergyfile13.txt', 'w') as filealler:
            filealler.write(allergia + " ")
    else:
        tk.messagebox.showinfo("INFO", "! Nothing has been saved !")
    diagRecapt(diagnosis)

def funcrecord():
    """
        To upload data record to server !
    """
    proc = subprocess.run(["scp", './newpatient/entryfile13.txt',
        "pi@192.168.18.12:~/tt_doc/doc_txt13/Files13/entryfile13.txt"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File entryfile13.txt uploaded !")
        #tk.messagebox.showinfo("INFO", "entryfile13.txt uploaded...")
    else:
        print("+ No file to upload !")
        tk.messagebox.showerror("Error", "No entryfile13.txt to upload...")

def uptopat(idpatient, patient_num, firstpat, firstname_pat,
    surname, sur_pat, birthvalue, birth_entree, allergia, allergy_pat,
    transdisval, diseasetrans, diagnosis, diagnos_pat):
    """
        Update data for patients
        by id of database.
        Verify if all variables are called
        (because there are a lot, that could
        be losted).
    """
    idpatient = patient_num.get()
    firstpat = firstname_pat.get()
    surname = sur_pat.get()
    birthvalue = birth_entree.get()
    allergia = allergy_pat.get()
    transdisval = diseasetrans.get()
    diagnosis = diagnos_pat.get()

    # Interact with database to update
    if patient_num.get() == "" or firstname_pat.get() == "" or sur_pat.get() == "":
        tk.messagebox.showerror("MySQL Connection", "Enter Correct Details.")
    else:
        sqlCon = pymysql.connect(host='192.168.18.12', port=3306, user='koala33',
            password='Ko@l@tr3379', database='timetrackconn')
        cur = sqlCon.cursor()
        cur.execute("UPDATE timetrackconn set firstname=%s, surname=%s, birth=%s, "\
            "allergy=%s, disease=%s, maindiagnostic=%s where stdid=%s",(
        firstname_pat.get(),
        sur_pat.get(),
        birth_entree.get(),
        allergy_pat.get(),
        diseasetrans.get(),
        diagnos_pat.get(),
        patient_num.get()
        ))
        sqlCon.commit()
        sqlCon.close()
        tk.messagebox.showinfo("Data Entry Form",
            "Record Updated Successfully !")

    if idpatient == '13':
        if os.path.getsize('./newpatient/entryfile13.txt'):
            print("+ File 'entryfile13.txt' exist !")
            os.remove('./newpatient/entryfile13.txt')
            searchLineName10(firstpat, surname, birthvalue,
                allergia, transdisval, diagnosis)
    else:
        pass
    funcrecord()
    gui.destroy()

labelID = tk.Label(gui, text='ID : ',
    font="Times 14 bold",
    fg='white', bg='DodgerBlue2')
labelID.pack(pady=10)

idpatient = tk.StringVar()
patient_num = tk.Entry(gui, textvariable=idpatient,
    highlightbackground='light sky blue', bd=4)
idpatient.set('13')
patient_num.pack()

labelname = tk.Label(gui, text='Name : ',
    font="Times 14 bold",
    fg='white', bg='DodgerBlue2')
labelname.pack(pady=10)

firstpat = tk.StringVar()
firstname_pat = tk.Entry(gui, textvariable=firstpat,
    highlightbackground='light sky blue', bd=4)
firstname_pat.pack()

surname = tk.StringVar()
sur_pat = tk.Entry(gui, textvariable=surname,
    highlightbackground='light sky blue', bd=4)
sur_pat.pack()

labelbirth = tk.Label(gui, text='Birth Date : ', font="Times 14 bold",
    fg='white', bg='DodgerBlue2')
labelbirth.pack(pady=10)

birthvalue = tk.StringVar()
birth_entree = tk.Entry(gui, textvariable=birthvalue,
    highlightbackground='light sky blue', bd=4)
birth_entree.pack()

labelaller = tk.Label(gui, text='Allergy : ',
    font="Times 14 bold",
    fg='white', bg='DodgerBlue2')
labelaller.pack(pady=10)

allergia = tk.StringVar()
allergy_pat = tk.Entry(gui, textvariable=allergia,
    highlightbackground='light sky blue',
    bd=4, width=40)
allergy_pat.pack(padx=10)

labeltrans = tk.Label(gui, text='Transmissible Disease : ',
    font="Times 14 bold",
    fg='white', bg='DodgerBlue2')
labeltrans.pack(pady=10)

transdisval = tk.StringVar()
diseasetrans = tk.Entry(gui, textvariable=transdisval,
    highlightbackground='light sky blue', bd=4)
diseasetrans.pack()

labeldiag = tk.Label(gui, text='Diagnosis : ',
    font="Times 14 bold",
    fg='white', bg='DodgerBlue2')
labeldiag.pack(pady=10)

diagnosis = tk.StringVar()
diagnos_pat = tk.Entry(gui, textvariable=diagnosis,
    highlightbackground='light sky blue', bd=4)
diagnos_pat.pack()

buttonsearch = tk.Button(gui, text="Search ID", width=8, bd=3,
    fg='yellow', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='pale turquoise', command = searchDB)
buttonsearch.pack(side=tk.LEFT, padx=10, pady=20)

buttonupdate = tk.Button(gui, text="Enter", width=8, bd=3,
    fg='orange', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='pale turquoise',
    command = lambda: uptopat(idpatient, patient_num, firstpat, firstname_pat,
        surname, sur_pat, birthvalue, birth_entree, allergia, allergy_pat,
        transdisval, diseasetrans, diagnosis, diagnos_pat))
buttonupdate.pack(side=tk.LEFT, padx=10, pady=20)

buttQuit = tk.Button(gui, text="Quit", width=8, bd=3,
    fg='cyan', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='pale turquoise', command=quit)
buttQuit.pack(side=tk.LEFT, padx=10, pady=20)

searchDB()
gui.mainloop()
