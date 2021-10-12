#!/usr/bin/python3
# -*- coding: utf-8 -*-


import tkinter as tk
from tkinter import messagebox
import os
try:
    import pymysql
    pymysql.install_as_MySQLdb()
except ImportError as err_report:
    print("[!] An error occured about pymysql - updatpatient13.py [!]", err_report)
    pass


gui = tk.Tk()
gui.title("Update Allergy File")
gui.configure(bg='DodgerBlue2')
gui.resizable(False, False)

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
        #allergia.set(row[4]) 
        transdisval.set(row[5])
        diagnosis.set(row[6])
        sqlCon.commit()
    except:
        print("[!] Error with search function in DB")
        tk.messagebox.showinfo("Data Entry Form", "No Such Record Found !")
    sqlCon.close()

def searchLineName13(firstpat, surname, birthvalue, allergia, transdisval, diagnosis):
    """
        To save changing data for 
        entryfile.txt and display
        tk.messagebox.
    """
    MsgBox2 = tk.messagebox.askyesno('Save data', 'Do you want to save ?')
    if MsgBox2 == 1:
        with open('./newpatient/entryfile13.txt', 'w') as file2:
            file2.write(firstpat + " " + surname + '\n')
            file2.write(birthvalue + '\n')
            file2.write(allergia + '\n')
            file2.write(transdisval + '\n')
            file2.write(diagnosis + '\n')
        with open('./allergy/allergyfile13.txt', 'w') as al_file:
            al_file.write(allergia + '\n')
    tk.messagebox.showinfo("Info", "Data was updated for entryfile13.txt and "\
        "allergyfile13.txt !")

def uptopat(idpatient, patient_num, firstpat, firstname_pat,
    surname, sur_pat, birthvalue, birth_entree, allergia, allergy_pat,
    transdisval, diseasetrans, diagnosis, diagnos_pat):
    """
        Update data for patients
        in function of their id
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
        cur.execute("UPDATE timetrackconn set firstname=%s, surname=%s, birth=%s,\
            allergy=%s, disease=%s, maindiagnostic=%s where stdid=%s",(
        firstname_pat.get(),
        sur_pat.get(),
        birth_entree.get(),
        allergy_pat.get(),
        diseasetrans.get(),
        diagnos_pat.get(),
        patient_num.get(),
        ))
        sqlCon.commit()
        sqlCon.close()
        tk.messagebox.showinfo("Data Entry Form", "Record Updated Successfully !")

    if idpatient == '13':
        if os.path.getsize('./newpatient/entryfile13.txt'):
            print("[+] File 'entryfile13.txt' exist !")
            os.remove('./newpatient/entryfile13.txt')
            os.remove('./allergy/aller_drop13.txt')
            #os.remove('./allergy/allergyfile13.txt')
            searchLineName13(firstpat, surname, birthvalue,
                allergia, transdisval, diagnosis)
    else:
        pass
    gui.destroy()

with open('./allergy/aller_drop13.txt', 'r') as patfile:
    linea = patfile.readline()

with open('./newpatient/entryfile13.txt', 'r') as filename:
    a_line = filename.readline()
    b_line = filename.readline()
    c_line = filename.readline()

labelID = tk.Label(gui, text='ID : ',
    font="Times 14 bold",
    fg='RoyalBlue4', bg='DodgerBlue2')
labelID.pack(pady=10)

idpatient = tk.StringVar()
patient_num = tk.Entry(gui, textvariable=idpatient,
    highlightbackground='light sky blue', bd=4)
idpatient.set('13')
patient_num.pack()

labelname = tk.Label(gui, text='Name : ',
    font="Times 14 bold",
    fg='RoyalBlue4', bg='DodgerBlue2')
labelname.pack(pady=10)

firstpat = tk.StringVar()
#firstpat.set('Firstname')
firstname_pat = tk.Entry(gui, textvariable=firstpat,
    highlightbackground='light sky blue',
    bd=4)
firstname_pat.pack()

surname = tk.StringVar()
#surname.set("Lastname")
sur_pat = tk.Entry(gui, textvariable=surname,
    highlightbackground='light sky blue',
    bd=4)
sur_pat.pack()

labelbirth = tk.Label(gui, text='Birth Date : ', font="Times 14 bold",
    fg='RoyalBlue4', bg='DodgerBlue2')
labelbirth.pack(pady=10)

birthvalue = tk.StringVar()
#birthvalue.set('Format: 00/00/0000')
birth_entree = tk.Entry(gui, textvariable=birthvalue,
    highlightbackground='light sky blue', bd=4)
birth_entree.pack()

labelaller = tk.Label(gui, text='Allergy : ',
    font="Times 14 bold",
    fg='RoyalBlue4', bg='DodgerBlue2')
labelaller.pack(pady=10)

allergia = tk.StringVar()
allergy_pat = tk.Entry(gui, textvariable=allergia,
    highlightbackground='light sky blue', bd=4, width=40)
allergia.set(linea + c_line[:-1])
allergy_pat.pack()

labeltrans = tk.Label(gui, text='Transmissible Disease : ',
    font="Times 14 bold",
    fg='RoyalBlue4', bg='DodgerBlue2')
labeltrans.pack(pady=10)

transdisval = tk.StringVar()
#transdisval.set('None')
diseasetrans = tk.Entry(gui, textvariable=transdisval,
    highlightbackground='light sky blue',
    bd=4)
diseasetrans.pack()

labeldiag = tk.Label(gui, text='Diagnosis : ',
    font="Times 14 bold",
    fg='RoyalBlue4', bg='DodgerBlue2')
labeldiag.pack(pady=10)

diagnosis = tk.StringVar()
#diagnosis.set('Diagnostic (main)')
diagnos_pat = tk.Entry(gui, textvariable=diagnosis,
    highlightbackground='light sky blue',
    bd=4)
diagnos_pat.pack()

buttonsearch = tk.Button(gui, text="Search ID", width=8, bd=3,
    fg='yellow', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='pale turquoise',
    command = searchDB)
buttonsearch.pack(side=tk.LEFT, padx=10, pady=20)

buttonupdate = tk.Button(gui, text="Enter", width=8, bd=3,
    fg='orange', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='pale turquoise',
    command = lambda: uptopat(idpatient, patient_num, firstpat, firstname_pat,
        surname, sur_pat, birthvalue, birth_entree, allergia, allergy_pat,
        transdisval, diseasetrans, diagnosis, diagnos_pat))
buttonupdate.pack(side=tk.LEFT, padx=10, pady=20)

buttQuit = tk.Button(gui, text="Quit", width=8, bd=3,
    fg='white', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='pale turquoise', command=quit)
buttQuit.pack(side=tk.LEFT, padx=10, pady=20)

gui.mainloop()

