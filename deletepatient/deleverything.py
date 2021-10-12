#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
    To delete patient by his name
"""


from tkinter import *
import tkinter as tk
from tkinter import messagebox
import os
from del_patient1 import *
from del_patient2 import *
from del_patient3 import *
from del_patient4 import *
from del_patient5 import *
from del_patient6 import *
from del_patient7 import *
from del_patient8 import *
from del_patient9 import *
from del_patient10 import *
from del_patient11 import *
from del_patient12 import *
from del_patient13 import *
from del_patient14 import *
from del_patient15 import *
from del_patient16 import *
from del_patient17 import *
from del_patient18 import *
from del_patient19 import *
from del_patient20 import *
from del_patient21 import *
from del_patient22 import *
from del_patient23 import *
from del_patient24 import *
try:
    import pymysql
    pymysql.install_as_MySQLdb()
except ImportError as err_report3:
    print("[!] An error occured about pymysql - deleverything.py [!]", err_report3)
    pass


def get(Nompatient, entree, PatientID, Num_pat):
    """
        To delete patient name and all files by functions
        with a msgbox to verify the choice.
    """
    MsgBox = messagebox.askyesno('Save data', 'Do you want to delete ?')
    if MsgBox == 1:
        Nompatient = entree.get()
        Num_pat = PatientID.get()

        sqlCon = pymysql.connect(host='192.168.18.12', user='koala33', password='Ko@l@tr3379',
            database='timetrackconn')
        cur = sqlCon.cursor()
        cur.execute("DELETE from timetrackconn where stdid=%s", PatientID.get())
        sqlCon.commit()
        sqlCon.close()
        messagebox.showinfo("Data Entry Form", "Record Successfully Deleted !")

        if os.path.getsize('./newpatient/entryfile.txt'):
            with open('./newpatient/entryfile.txt', 'r') as file:
                lines = file.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if Nompatient in line:
                        delFuncFile1()
                    else:
                        print("End of test delete files 1.")

        if os.path.getsize('./newpatient/entryfile2.txt'):
            with open('./newpatient/entryfile2.txt', 'r') as file2:
                lines = file2.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if Nompatient in line:
                        delFuncFile2()
                    else:
                        print("End of test delete files 2.")

        if os.path.getsize('./newpatient/entryfile3.txt'):
            with open('./newpatient/entryfile3.txt', 'r') as file3:
                lines = file3.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if Nompatient in line:
                        delFuncFile3()
                    else:
                        print("End of test delete files 3.")

        if os.path.getsize('./newpatient/entryfile4.txt'):
            with open('./newpatient/entryfile4.txt', 'r') as file4:
                lines = file4.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if Nompatient in line:
                        delFuncFile4()
                    else:
                        print("End of test delete files 4.")

        if os.path.getsize('./newpatient/entryfile5.txt'):
            with open('./newpatient/entryfile5.txt', 'r') as file5:
                lines = file5.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if Nompatient in line:
                        delFuncFile5()
                    else:
                        print("End of test delete files 5.")

        if os.path.getsize('./newpatient/entryfile6.txt'):
            with open('./newpatient/entryfile6.txt', 'r') as file6:
                lines = file6.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if Nompatient in line:
                        delFuncFile6()
                    else:
                        print("End of test delete files 6.")

        if os.path.getsize('./newpatient/entryfile7.txt'):
            with open('./newpatient/entryfile7.txt', 'r') as file7:
                lines = file7.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if Nompatient in line:
                        delFuncFile7()
                    else:
                        print("End of test delete files 7.")

        if os.path.getsize('./newpatient/entryfile8.txt'):
            with open('./newpatient/entryfile8.txt', 'r') as file8:
                lines = file8.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if Nompatient in line:
                        delFuncFile8()
                    else:
                        print("End of test delete files 8.")

        if os.path.getsize('./newpatient/entryfile9.txt'):
            with open('./newpatient/entryfile9.txt', 'r') as file9:
                lines = file9.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if Nompatient in line:
                        delFuncFile9()
                    else:
                        print("End of test delete files 9.")

        if os.path.getsize('./newpatient/entryfile10.txt'):
            with open('./newpatient/entryfile10.txt', 'r') as file10:
                lines = file10.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if Nompatient in line:
                        delFuncFile10()
                    else:
                        print("End of test delete files 10.")

        if os.path.getsize('./newpatient/entryfile11.txt'):
            with open('./newpatient/entryfile11.txt', 'r') as file11:
                lines = file11.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if Nompatient in line:
                        delFuncFile11()
                    else:
                        print("End of test delete files 11.")

        if os.path.getsize('./newpatient/entryfile12.txt'):
            with open('./newpatient/entryfile12.txt', 'r') as file12:
                lines = file12.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if Nompatient in line:
                        delFuncFile12()          
                    else:
                        print("End of test delete files 12.")

        if os.path.getsize('./newpatient/entryfile13.txt'):
            with open('./newpatient/entryfile13.txt', 'r') as file13:
                lines = file13.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if Nompatient in line:
                        delFuncFile13()
                    else:
                        print("End of test delete files 13.")

        if os.path.getsize('./newpatient/entryfile14.txt'):
            with open('./newpatient/entryfile14.txt', 'r') as file14:
                lines = file14.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if Nompatient in line:
                        delFuncFile14()
                    else:
                        print("End of test delete files 14.")

        if os.path.getsize('./newpatient/entryfile15.txt'):
            with open('./newpatient/entryfile15.txt', 'r') as file15:
                lines = file15.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if Nompatient in line:
                        delFuncFile15()
                    else:
                        print("End of test delete files 15.")

        if os.path.getsize('./newpatient/entryfile16.txt'):
            with open('./newpatient/entryfile16.txt', 'r') as file16:
                lines = file16.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if Nompatient in line:
                        delFuncFile16()
                    else:
                        print("End of test delete files 16.")

        if os.path.getsize('./newpatient/entryfile17.txt'):
            with open('./newpatient/entryfile17.txt', 'r') as file17:
                lines = file17.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if Nompatient in line:
                        delFuncFile17()
                    else:
                        print("End of test delete files 17.")

        if os.path.getsize('./newpatient/entryfile18.txt'):
            with open('./newpatient/entryfile18.txt', 'r') as file18:
                lines = file18.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if Nompatient in line:
                        delFuncFile18()
                    else:
                        print("End of test delete files 18.")

        if os.path.getsize('./newpatient/entryfile19.txt'):
            with open('./newpatient/entryfile19.txt', 'r') as file19:
                lines = file19.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if Nompatient in line:
                        delFuncFile19()
                    else:
                        print("End of test delete files 19.")

        if os.path.getsize('./newpatient/entryfile20.txt'):
            with open('./newpatient/entryfile20.txt', 'r') as file20:
                lines = file20.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if Nompatient in line:
                        delFuncFile20()
                    else:
                        print("End of test delete files 20.")

        if os.path.getsize('./newpatient/entryfile21.txt'):
            with open('./newpatient/entryfile21.txt', 'r') as file20:
                lines = file20.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if Nompatient in line:
                        delFuncFile21()
                    else:
                        print("End of test delete files 21.")

        if os.path.getsize('./newpatient/entryfile22.txt'):
            with open('./newpatient/entryfile22.txt', 'r') as file20:
                lines = file20.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if Nompatient in line:
                        delFuncFile22()
                    else:
                        print("End of test delete files 22.")

        if os.path.getsize('./newpatient/entryfile23.txt'):
            with open('./newpatient/entryfile23.txt', 'r') as file20:
                lines = file20.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if Nompatient in line:
                        delFuncFile23()
                    else:
                        print("End of test delete files 23.")

        if os.path.getsize('./newpatient/entryfile24.txt'):
            with open('./newpatient/entryfile24.txt', 'r') as file20:
                lines = file20.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if Nompatient in line:
                        delFuncFile24()
                    else:
                        print("End of test delete files 24.")
    else:           
        messagebox.showinfo('Return', 'None file was found !')

    gui.destroy()

gui = tk.Tk()
gui.title("Time-Track")
gui.configure(bg='DodgerBlue2')
#gui.geometry('300x200')

labelID = tk.Label(gui, text='ID Number : ',
    font="Times 14 bold", fg='white', bg='DodgerBlue2')
labelID.pack(pady=10)

Num_pat = tk.StringVar()
PatientID = tk.Entry(gui, textvariable=Num_pat,
    highlightbackground='SteelBlue', bd=4)
Num_pat.set('ID Number')
PatientID.pack()

labelName = tk.Label(gui, text='Enter Name To Delete : ',
    font="Times 14 bold", fg='white', bg='DodgerBlue2')
labelName.pack(pady=10)

Nompatient = tk.StringVar()
entree = tk.Entry(gui, textvariable=Nompatient,
    highlightbackground='SteelBlue', bd=4)
Nompatient.set('Firstname + Lastname')
entree.pack()

bouton1 = tk.Button(gui, text="Delete", fg='yellow', bg='RoyalBlue3',
    width=8, bd=4, highlightbackground='SteelBlue',
    activebackground="pale turquoise",
    command = lambda: get(Nompatient, entree, PatientID, Num_pat))
bouton1.pack(side=tk.LEFT, padx=10, pady=20)

buttQuit = tk.Button(gui, text="Quit", fg='cyan', bg='RoyalBlue3',
    width=8, bd=4, highlightbackground='SteelBlue',
    activebackground="pale turquoise",
    command = quit)
buttQuit.pack(side=tk.LEFT, padx=10, pady=20)

gui.mainloop()
