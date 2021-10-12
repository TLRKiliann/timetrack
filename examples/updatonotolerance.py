#!/usr/bin/python3
# -*- coding: utf-8 -*-


from tkinter import *
from tkinter import messagebox
import os
try:
    import pymysql
    pymysql.install_as_MySQLdb()
except ImportError as err_report:
    print("+ An error occured about pymysql !", err_report)
    pass


gui=Tk()
gui.title("Enter new patient")
gui.configure(bg='DodgerBlue2')

# Interact with database to search data
def searchDB():
    """
        To search patient by ID
        and display data into 
        each GUI entree.
    """
    try:
        sqlCon = pymysql.connect(host='127.0.0.1', user='root', password='Ko@l@tr3379', database='timetrackconn')
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
        print("Error with search function in DB")
        messagebox.showinfo("Data Entry Form", "No Such Record Found !")
    sqlCon.close()

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
        messagebox.showerror("MySQL Connection", "Enter Correct Details.")
    else:
        sqlCon = pymysql.connect(host='127.0.0.1', user='root', password='Ko@l@tr3379', database='timetrackconn')
        cur = sqlCon.cursor()
        cur.execute("UPDATE timetrackconn set firstname=%s, surname=%s, birth=%s, allergia=%s, disease=%s, maindiagnostic=%s where stdid=%s",(
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
        messagebox.showinfo("Data Entry Form", "Record Updated Successfully !")

    if idpatient == '1':
        if os.path.getsize('./newpatient/entryfile.txt'):
            print("+ File 'entryfile.txt' exist !")
            os.remove('./newpatient/entryfile.txt')
            searchLineName(firstpat, surname, birthvalue, allergia, transdisval, diagnosis)
    else:
        pass

    if idpatient == '2':
        if os.path.getsize('./newpatient/entryfile2.txt'):
            print("+ File 'entryfile2.txt' exist !")
            os.remove('./newpatient/entryfile2.txt')
            searchLineName2(firstpat, surname, birthvalue, allergia, transdisval, diagnosis)
    else:
        pass

    if idpatient == '3':
        if os.path.getsize('./newpatient/entryfile3.txt'):
            print("+ File 'entryfile3.txt' exist !")
            os.remove('./newpatient/entryfile3.txt')
            searchLineName3(firstpat, surname, birthvalue, allergia, transdisval, diagnosis)
    else:
        pass

    if idpatient == '4':
        if os.path.getsize('./newpatient/entryfile4.txt'):
            print("+ File 'entryfile4.txt' exist !")
            os.remove('./newpatient/entryfile4.txt')
            searchLineName4(firstpat, surname, birthvalue, allergia, transdisval, diagnosis)
    else:
        pass

    if idpatient == '5':
        if os.path.getsize('./newpatient/entryfile5.txt'):
            print("+ File 'entryfile5.txt' exist !")
            os.remove('./newpatient/entryfile5.txt')
            searchLineName5(firstpat, surname, birthvalue, allergia, transdisval, diagnosis)
    else:
        pass

    if idpatient == '6':
        if os.path.getsize('./newpatient/entryfile6.txt'):
            print("+ File 'entryfile6.txt' exist !")
            os.remove('./newpatient/entryfile6.txt')
            searchLineName6(firstpat, surname, birthvalue, allergia, transdisval, diagnosis)
    else:
        pass

    if idpatient == '7':
        if os.path.getsize('./newpatient/entryfile7.txt'):
            print("+ File 'entryfile7.txt' exist !")
            os.remove('./newpatient/entryfile7.txt')
            searchLineName7(firstpat, surname, birthvalue, allergia, transdisval, diagnosis)
    else:
        pass

    if idpatient == '8':
        if os.path.getsize('./newpatient/entryfile8.txt'):
            print("+ File 'entryfile8.txt' exist !")
            os.remove('./newpatient/entryfile8.txt')
            searchLineName8(firstpat, surname, birthvalue, allergia, transdisval, diagnosis)
    else:
        pass

    if idpatient == '9':
        if os.path.getsize('./newpatient/entryfile9.txt'):
            print("+ File 'entryfile9.txt' exist !")
            os.remove('./newpatient/entryfile9.txt')
            searchLineName9(firstpat, surname, birthvalue, allergia, transdisval, diagnosis)
    else:
        pass

    if idpatient == '10':
        if os.path.getsize('./newpatient/entryfile10.txt'):
            print("+ File 'entryfile10.txt' exist !")
            os.remove('./newpatient/entryfile10.txt')
            searchLineName10(firstpat, surname, birthvalue, allergia, transdisval, diagnosis)
    else:
        pass

    if idpatient == '11':
        if os.path.getsize('./newpatient/entryfile11.txt'):
            print("+ File 'entryfile11.txt' exist !")
            os.remove('./newpatient/entryfile11.txt')
            searchLineName11(firstpat, surname, birthvalue, allergia, transdisval, diagnosis)
    else:
        pass

    if idpatient == '12':
        if os.path.getsize('./newpatient/entryfile12.txt'):
            print("+ File 'entryfile12.txt' exist !")
            os.remove('./newpatient/entryfile12.txt')
            searchLineName12(firstpat, surname, birthvalue, allergia, transdisval, diagnosis)
    else:
        pass

    if idpatient == '13':
        if os.path.getsize('./newpatient/entryfile13.txt'):
            print("+ File 'entryfile13.txt' exist !")
            os.remove('./newpatient/entryfile13.txt')
            searchLineName13(firstpat, surname, birthvalue, allergia, transdisval, diagnosis)
    else:
        pass

    if idpatient == '14':
        if os.path.getsize('./newpatient/entryfile14.txt'):
            print("+ File 'entryfile14.txt' exist !")
            os.remove('./newpatient/entryfile14.txt')
            searchLineName14(firstpat, surname, birthvalue, allergia, transdisval, diagnosis)
    else:
        pass

    if idpatient == '15':
        if os.path.getsize('./newpatient/entryfile15.txt'):
            print("+ File 'entryfile15.txt' exist !")
            os.remove('./newpatient/entryfile15.txt')
            searchLineName15(firstpat, surname, birthvalue, allergia, transdisval, diagnosis)
    else:
        pass

    if idpatient == '16':
        if os.path.getsize('./newpatient/entryfile16.txt'):
            print("+ File 'entryfile16.txt' exist !")
            os.remove('./newpatient/entryfile16.txt')
            searchLineName16(firstpat, surname, birthvalue, allergia, transdisval, diagnosis)
    else:
        pass

    if idpatient == '17':
        if os.path.getsize('./newpatient/entryfile17.txt'):
            print("+ File 'entryfile17.txt' exist !")
            os.remove('./newpatient/entryfile17.txt')
            searchLineName17(firstpat, surname, birthvalue, allergia, transdisval, diagnosis)
    else:
        pass

    if idpatient == '18':
        if os.path.getsize('./newpatient/entryfile18.txt'):
            print("+ File 'entryfile18.txt' exist !")
            os.remove('./newpatient/entryfile18.txt')
            searchLineName18(firstpat, surname, birthvalue, allergia, transdisval, diagnosis)
    else:
        pass

    if idpatient == '19':
        if os.path.getsize('./newpatient/entryfile19.txt'):
            print("+ File 'entryfile19.txt' exist !")
            os.remove('./newpatient/entryfile19.txt')
            searchLineName19(firstpat, surname, birthvalue, allergia, transdisval, diagnosis)
    else:
        pass

    if idpatient == '20':
        if os.path.getsize('./newpatient/entryfile20.txt'):
            print("+ File 'entryfile20.txt' exist !")
            os.remove('./newpatient/entryfile20.txt')
            searchLineName20(firstpat, surname, birthvalue, allergia, transdisval, diagnosis)
    else:
        pass

    if idpatient == '21':
        if os.path.getsize('./newpatient/entryfile21.txt'):
            print("+ File 'entryfile21.txt' exist !")
            os.remove('./newpatient/entryfile21.txt')
            searchLineName21(firstpat, surname, birthvalue, allergia, transdisval, diagnosis)
    else:
        pass

    if idpatient == '22':
        if os.path.getsize('./newpatient/entryfile22.txt'):
            print("+ File 'entryfile22.txt' exist !")
            os.remove('./newpatient/entryfile22.txt')
            searchLineName22(firstpat, surname, birthvalue, allergia, transdisval, diagnosis)
    else:
        pass

    if idpatient == '23':
        if os.path.getsize('./newpatient/entryfile23.txt'):
            print("+ File 'entryfile23.txt' exist !")
            os.remove('./newpatient/entryfile23.txt')
            searchLineName23(firstpat, surname, birthvalue, allergia, transdisval, diagnosis)
    else:
        pass

    if idpatient == '24':
        if os.path.getsize('./newpatient/entryfile24.txt'):
            print("+ File 'entryfile24.txt' exist !")
            os.remove('./newpatient/entryfile24.txt')
            searchLineName24(firstpat, surname, birthvalue, allergia, transdisval, diagnosis)
    else:
        pass
    gui.destroy()

def searchLineName(firstpat, surname, birthvalue, allergia, transdisval, diagnosis):
    """
        To save changing data for 
        entryfile.txt and display
        messagebox.
    """
    MsgBox = messagebox.askyesno('Save data', 'Do you want to save ?')
    if MsgBox == 1:
        with open('./newpatient/entryfile.txt', 'w') as file:
            file.write(firstpat + " " + surname + '\n')
            file.write(birthvalue + '\n')
            file.write(allergia + '\n')
            file.write(transdisval + '\n')
            file.write(diagnosis + '\n')
    messagebox.showinfo("Info", "Data was updated for entryfile.txt !")

def searchLineName2(firstpat, surname, birthvalue, allergia, transdisval, diagnosis):
    MsgBox2 = messagebox.askyesno('Save data', 'Do you want to save ?')
    if MsgBox2 == 1:
        with open('./newpatient/entryfile2.txt', 'w') as file2:
            file2.write(firstpat + " " + surname + '\n')
            file2.write(birthvalue + '\n')
            file2.write(allergia + '\n')
            file2.write(transdisval + '\n')
            file2.write(diagnosis + '\n')
    messagebox.showinfo("Info", "Data was updated for entryfile2.txt !")

def searchLineName3(firstpat, surname, birthvalue, allergia, transdisval, diagnosis):
    MsgBox2 = messagebox.askyesno('Save data', 'Do you want to save ?')
    if MsgBox2 == 1:
        with open('./newpatient/entryfile3.txt', 'w') as file3:
            file3.write(firstpat + " " + surname + '\n')
            file3.write(birthvalue + '\n')
            file3.write(allergia + '\n')
            file3.write(transdisval + '\n')
            file3.write(diagnosis + '\n')
    messagebox.showinfo("Info", "Data was updated for entryfile3.txt !")

def searchLineName4(firstpat, surname, birthvalue, allergia, transdisval, diagnosis):
    MsgBox2 = messagebox.askyesno('Save data', 'Do you want to save ?')
    if MsgBox2 == 1:
        with open('./newpatient/entryfile4.txt', 'w') as file4:
            file4.write(firstpat + " " + surname + '\n')
            file4.write(birthvalue + '\n')
            file4.write(allergia + '\n')
            file4.write(transdisval + '\n')
            file4.write(diagnosis + '\n')
    messagebox.showinfo("Info", "Data was updated for entryfile4.txt !")

def searchLineName5(firstpat, surname, birthvalue, allergia, transdisval, diagnosis):
    MsgBox2 = messagebox.askyesno('Save data', 'Do you want to save ?')
    if MsgBox2 == 1:
        with open('./newpatient/entryfile5.txt', 'w') as file5:
            file5.write(firstpat + " " + surname + '\n')
            file5.write(birthvalue + '\n')
            file5.write(allergia + '\n')
            file5.write(transdisval + '\n')
            file5.write(diagnosis + '\n')
    messagebox.showinfo("Info", "Data was updated for entryfile5.txt !")

def searchLineName6(firstpat, surname, birthvalue, allergia, transdisval, diagnosis):
    MsgBox2 = messagebox.askyesno('Save data', 'Do you want to save ?')
    if MsgBox2 == 1:
        with open('./newpatient/entryfile6.txt', 'w') as file6:
            file6.write(firstpat + " " + surname + '\n')
            file6.write(birthvalue + '\n')
            file6.write(allergia + '\n')
            file6.write(transdisval + '\n')
            file6.write(diagnosis + '\n')
    messagebox.showinfo("Info", "Data was updated for entryfile6.txt !")

def searchLineName7(firstpat, surname, birthvalue, allergia, transdisval, diagnosis):
    MsgBox2 = messagebox.askyesno('Save data', 'Do you want to save ?')
    if MsgBox2 == 1:
        with open('./newpatient/entryfile7.txt', 'w') as file7:
            file7.write(firstpat + " " + surname + '\n')
            file7.write(birthvalue + '\n')
            file7.write(allergia + '\n')
            file7.write(transdisval + '\n')
            file7.write(diagnosis + '\n')
    messagebox.showinfo("Info", "Data was updated for entryfile7.txt !")

def searchLineName8(firstpat, surname, birthvalue, allergia, transdisval, diagnosis):
    MsgBox2 = messagebox.askyesno('Save data', 'Do you want to save ?')
    if MsgBox2 == 1:
        with open('./newpatient/entryfile8.txt', 'w') as file8:
            file8.write(firstpat + " " + surname + '\n')
            file8.write(birthvalue + '\n')
            file8.write(allergia + '\n')
            file8.write(transdisval + '\n')
            file8.write(diagnosis + '\n')
    messagebox.showinfo("Info", "Data was updated for entryfile8.txt !")

def searchLineName9(firstpat, surname, birthvalue, allergia, transdisval, diagnosis):
    MsgBox2 = messagebox.askyesno('Save data', 'Do you want to save ?')
    if MsgBox2 == 1:
        with open('./newpatient/entryfile9.txt', 'w') as file9:
            file9.write(firstpat + " " + surname + '\n')
            file9.write(birthvalue + '\n')
            file9.write(allergia + '\n')
            file9.write(transdisval + '\n')
            file9.write(diagnosis + '\n')
    messagebox.showinfo("Info", "Data was updated for entryfile9.txt !")

def searchLineName10(firstpat, surname, birthvalue, allergia, transdisval, diagnosis):
    MsgBox2 = messagebox.askyesno('Save data', 'Do you want to save ?')
    if MsgBox2 == 1:
        with open('./newpatient/entryfile10.txt', 'w') as file10:
            file10.write(firstpat + " " + surname + '\n')
            file10.write(birthvalue + '\n')
            file10.write(allergia + '\n')
            file10.write(transdisval + '\n')
            file10.write(diagnosis + '\n')
    messagebox.showinfo("Info", "Data was updated for entryfile10.txt !")

def searchLineName11(firstpat, surname, birthvalue, allergia, transdisval, diagnosis):
    MsgBox2 = messagebox.askyesno('Save data', 'Do you want to save ?')
    if MsgBox2 == 1:
        with open('./newpatient/entryfile11.txt', 'w') as file11:
            file11.write(firstpat + " " + surname + '\n')
            file11.write(birthvalue + '\n')
            file11.write(allergia + '\n')
            file11.write(transdisval + '\n')
            file11.write(diagnosis + '\n')
    messagebox.showinfo("Info", "Data was updated for entryfile11.txt !")

def searchLineName12(firstpat, surname, birthvalue, allergia, transdisval, diagnosis):
    MsgBox2 = messagebox.askyesno('Save data', 'Do you want to save ?')
    if MsgBox2 == 1:
        with open('./newpatient/entryfile12.txt', 'w') as file12:
            file12.write(firstpat + " " + surname + '\n')
            file12.write(birthvalue + '\n')
            file12.write(allergia + '\n')
            file12.write(transdisval + '\n')
            file12.write(diagnosis + '\n')
    messagebox.showinfo("Info", "Data was updated for entryfile12.txt !")

def searchLineName13(firstpat, surname, birthvalue, allergia, transdisval, diagnosis):
    MsgBox2 = messagebox.askyesno('Save data', 'Do you want to save ?')
    if MsgBox2 == 1:
        with open('./newpatient/entryfile13.txt', 'w') as file13:
            file13.write(firstpat + " " + surname + '\n')
            file13.write(birthvalue + '\n')
            file13.write(allergia + '\n')
            file13.write(transdisval + '\n')
            file13.write(diagnosis + '\n')
    messagebox.showinfo("Info", "Data was updated for entryfile13.txt !")

def searchLineName14(firstpat, surname, birthvalue, allergia, transdisval, diagnosis):
    MsgBox2 = messagebox.askyesno('Save data', 'Do you want to save ?')
    if MsgBox2 == 1:
        with open('./newpatient/entryfile14.txt', 'w') as file14:
            file14.write(firstpat + " " + surname + '\n')
            file14.write(birthvalue + '\n')
            file14.write(allergia + '\n')
            file14.write(transdisval + '\n')
            file14.write(diagnosis + '\n')
    messagebox.showinfo("Info", "Data was updated for entryfile14.txt !")

def searchLineName15(firstpat, surname, birthvalue, allergia, transdisval, diagnosis):
    MsgBox2 = messagebox.askyesno('Save data', 'Do you want to save ?')
    if MsgBox2 == 1:
        with open('./newpatient/entryfile15.txt', 'w') as file15:
            file15.write(firstpat + " " + surname + '\n')
            file15.write(birthvalue + '\n')
            file15.write(allergia + '\n')
            file15.write(transdisval + '\n')
            file15.write(diagnosis + '\n')
    messagebox.showinfo("Info", "Data was updated for entryfile15.txt !")

def searchLineName16(firstpat, surname, birthvalue, allergia, transdisval, diagnosis):
    MsgBox2 = messagebox.askyesno('Save data', 'Do you want to save ?')
    if MsgBox2 == 1:
        with open('./newpatient/entryfile16.txt', 'w') as file16:
            file16.write(firstpat + " " + surname + '\n')
            file16.write(birthvalue + '\n')
            file16.write(allergia + '\n')
            file16.write(transdisval + '\n')
            file16.write(diagnosis + '\n')
    messagebox.showinfo("Info", "Data was updated for entryfile16.txt !")

def searchLineName17(firstpat, surname, birthvalue, allergia, transdisval, diagnosis):
    MsgBox2 = messagebox.askyesno('Save data', 'Do you want to save ?')
    if MsgBox2 == 1:
        with open('./newpatient/entryfile17.txt', 'w') as file17:
            file17.write(firstpat + " " + surname + '\n')
            file17.write(birthvalue + '\n')
            file17.write(allergia + '\n')
            file17.write(transdisval + '\n')
            file17.write(diagnosis + '\n')
    messagebox.showinfo("Info", "Data was updated for entryfile17.txt !")

def searchLineName18(firstpat, surname, birthvalue, allergia, transdisval, diagnosis):
    MsgBox2 = messagebox.askyesno('Save data', 'Do you want to save ?')
    if MsgBox2 == 1:
        with open('./newpatient/entryfile18.txt', 'w') as file18:
            file18.write(firstpat + " " + surname + '\n')
            file18.write(birthvalue + '\n')
            file18.write(allergia + '\n')
            file18.write(transdisval + '\n')
            file18.write(diagnosis + '\n')
    messagebox.showinfo("Info", "Data was updated for entryfile18.txt !")

def searchLineName19(firstpat, surname, birthvalue, allergia, transdisval, diagnosis):
    MsgBox2 = messagebox.askyesno('Save data', 'Do you want to save ?')
    if MsgBox2 == 1:
        with open('./newpatient/entryfile19.txt', 'w') as file19:
            file19.write(firstpat + " " + surname + '\n')
            file19.write(birthvalue + '\n')
            file19.write(allergia + '\n')
            file19.write(transdisval + '\n')
            file19.write(diagnosis + '\n')
    messagebox.showinfo("Info", "Data was updated for entryfile19.txt !")

def searchLineName20(firstpat, surname, birthvalue, allergia, transdisval, diagnosis):
    MsgBox2 = messagebox.askyesno('Save data', 'Do you want to save ?')
    if MsgBox2 == 1:
        with open('./newpatient/entryfile20.txt', 'w') as file20:
            file20.write(firstpat + " " + surname + '\n')
            file20.write(birthvalue + '\n')
            file20.write(allergia + '\n')
            file20.write(transdisval + '\n')
            file20.write(diagnosis + '\n')
    messagebox.showinfo("Info", "Data was updated for entryfile20.txt !")

def searchLineName21(firstpat, surname, birthvalue, allergia, transdisval, diagnosis):
    MsgBox2 = messagebox.askyesno('Save data', 'Do you want to save ?')
    if MsgBox2 == 1:
        with open('./newpatient/entryfile21.txt', 'w') as file21:
            file21.write(firstpat + " " + surname + '\n')
            file21.write(birthvalue + '\n')
            file21.write(allergia + '\n')
            file21.write(transdisval + '\n')
            file21.write(diagnosis + '\n')
    messagebox.showinfo("Info", "Data was updated for entryfile21.txt !")

def searchLineName22(firstpat, surname, birthvalue, allergia, transdisval, diagnosis):
    MsgBox2 = messagebox.askyesno('Save data', 'Do you want to save ?')
    if MsgBox2 == 1:
        with open('./newpatient/entryfile22.txt', 'w') as file22:
            file22.write(firstpat + " " + surname + '\n')
            file22.write(birthvalue + '\n')
            file22.write(allergia + '\n')
            file22.write(transdisval + '\n')
            file22.write(diagnosis + '\n')
    messagebox.showinfo("Info", "Data was updated for entryfile22.txt !")

def searchLineName23(firstpat, surname, birthvalue, allergia, transdisval, diagnosis):
    MsgBox2 = messagebox.askyesno('Save data', 'Do you want to save ?')
    if MsgBox2 == 1:
        with open('./newpatient/entryfile23.txt', 'w') as file23:
            file23.write(firstpat + " " + surname + '\n')
            file23.write(birthvalue + '\n')
            file23.write(allergia + '\n')
            file23.write(transdisval + '\n')
            file23.write(diagnosis + '\n')
    messagebox.showinfo("Info", "Data was updated for entryfile23.txt !")

def searchLineName24(firstpat, surname, birthvalue, allergia, transdisval, diagnosis):
    MsgBox2 = messagebox.askyesno('Save data', 'Do you want to save ?')
    if MsgBox2 == 1:
        with open('./newpatient/entryfile24.txt', 'w') as file24:
            file24.write(firstpat + " " + surname + '\n')
            file24.write(birthvalue + '\n')
            file24.write(allergia + '\n')
            file24.write(transdisval + '\n')
            file24.write(diagnosis + '\n')
    messagebox.showinfo("Info", "Data was updated for entryfile24.txt !")

with open('./allergy/allergyfile.txt', 'r') as patfile:
    linea = patfile.readline()

with open('./newpatient/entryfile.txt', 'r') as filename:
    a_line=filename.readline()
    b_line=filename.readline()
    c_line=filename.readline()

labelID = Label(gui)
labelID = Label(text='ID : ',
    font="Times 14 bold",
    fg='RoyalBlue4', bg='DodgerBlue2')
labelID.pack(pady=10)

idpatient = StringVar()
idpatient.set('1')
patient_num = Entry(gui, textvariable=idpatient,
    highlightbackground='light sky blue',
    bd=4)
patient_num.pack()

labelname = Label(gui)
labelname = Label(text='Name : ',
    font="Times 14 bold",
    fg='RoyalBlue4', bg='DodgerBlue2')
labelname.pack(pady=10)

firstpat = StringVar()
firstname_pat = Entry(gui, textvariable=firstpat,
    highlightbackground='light sky blue',
    bd=4)
firstname_pat.pack()

surname = StringVar()
sur_pat = Entry(gui, textvariable=surname,
    highlightbackground='light sky blue',
    bd=4)
sur_pat.pack()

labelbirth = Label(gui)
labelbirth = Label(text='Birth Date : ', font="Times 14 bold",
    fg='RoyalBlue4', bg='DodgerBlue2')
labelbirth.pack(pady=10)

birthvalue=StringVar()
birth_entree = Entry(gui, textvariable=birthvalue,
    highlightbackground='light sky blue', bd=4)
birth_entree.pack()

# Allergia
labelaller = Label(gui)
labelaller = Label(text='Allergy : ',
    font="Times 14 bold",
    fg='RoyalBlue4', bg='DodgerBlue2')
labelaller.pack(pady=10)

allergia = StringVar()
allergy_pat = Entry(gui, textvariable=allergia,
    highlightbackground='light sky blue',
    bd=4, width=40)
allergia.set(linea + c_line[:-1])
allergy_pat.pack()

labeltrans = Label(gui)
labeltrans = Label(text='Transmissible Disease : ',
    font="Times 14 bold",
    fg='RoyalBlue4', bg='DodgerBlue2')
labeltrans.pack(pady=10)

transdisval = StringVar()
diseasetrans = Entry(gui, textvariable=transdisval,
    highlightbackground='light sky blue',
    bd=4)
diseasetrans.pack()

labeldiag = Label(gui)
labeldiag = Label(text='Diagnosis : ',
    font="Times 14 bold",
    fg='RoyalBlue4', bg='DodgerBlue2')
labeldiag.pack(pady=10)

diagnosis = StringVar()
diagnos_pat = Entry(gui, textvariable=diagnosis,
    highlightbackground='light sky blue',
    bd=4)
diagnos_pat.pack()

buttonsearch = Button(gui, text="Search ID", width=8, bd=3,
    fg='yellow', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='pale turquoise',
    command = searchDB)
buttonsearch.pack(side=LEFT, padx=10, pady=20)

buttonupdate = Button(gui, text="Enter", width=8, bd=3,
    fg='orange', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='pale turquoise',
    command = lambda: uptopat(idpatient, patient_num, firstpat, firstname_pat,
        surname, sur_pat, birthvalue, birth_entree, allergia, allergy_pat,
        transdisval, diseasetrans, diagnosis, diagnos_pat))
buttonupdate.pack(side=LEFT, padx=10, pady=20)

buttQuit=Button(gui, text="Quit", width=8, bd=3,
    fg='DodgerBlue2', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='pale turquoise', command=quit)
buttQuit.pack(side=LEFT, padx=10, pady=20)

gui.mainloop()
