#!/usr/bin/python3
# -*- coding: utf-8 -*-


from tkinter import messagebox
import datetime
import time
import os
import subprocess
import shutil


def dispAgBox():
    """
        Display messagebox for agenda if an appointment
        has been fixed for tomorrow. Display nothing when reminder stopped.
        Change value (days=1) by (days=0) if you prefer to show the same day.
    """
    # Patient 1
    try:
        with open('./newpatient/entryfile.txt', 'r') as namefile:
            line1 = namefile.readline()
            new_text1 = line1
    except FileNotFoundError as fileout1:
        print("No file entryfile.txt exist", fileout1)

    try:
        magicword = (datetime.datetime.now() + datetime.timedelta(\
            days=1)).strftime('%d/%m/%Y')
        for path, dirs, files in os.walk('./patient_agenda/events/'
            'doc_events/fix_agenda/agenda_saved/'):
            for file in files:
                with open(os.path.join(path, file), 'r') as read_f:
                    lines = read_f.readlines()
                    for i in range(0, len(lines)):
                        line = lines[i]
                        if magicword in line:
                            print("[info] Here is lines of file.")
                            print(lines[i])
                            print(lines[i+1])
                            print(lines[i+2])
                            messagebox.showwarning('Info', 'Look at AGENDA, '
                                'there is an appointment tomorrow for : '\
                                + new_text1 + lines[i] + lines[i+1] + \
                                lines[i+2])

                            MSGREM1 = messagebox.askyesno("Ask", "Do you want to stop reminder ?")
                            if MSGREM1 == 1:
                                mwrename = magicword.replace("/", ".")
                                write_f = open(os.path.join(path, file), 'w')
                                write_f.write("* Rdv past--> " + mwrename + "\n" +
                                    lines[i+1] + lines[i+2] + "\n")
                                print("[+] Modification finish")
                                break
                            else:
                                pass
    except (FileNotFoundError, IndexError) as infofile1:
        print("File 1 has not been found (agendapp.py)", infofile1)
    else:
        print("Error unknow for patient 1 (agendapp.py).")

    # Patient 2
    try:
        with open('./newpatient/entryfile2.txt', 'r') as namefile:
            line2 = namefile.readline()
            new_text2 = line2
    except FileNotFoundError as fileout2:
        print("No file entryfile2.txt exist", fileout2)

    try:
        magicword2 = (datetime.datetime.now() + datetime.timedelta(\
            days=1)).strftime('%d/%m/%Y')
        for path, dirs, files in os.walk('./patient_agenda/events2/'
            'doc_events/fix_agenda/agenda_saved/'):
            for file in files:
                with open(os.path.join(path, file), 'r') as read_f:
                    lines = read_f.readlines()
                    for i in range(0, len(lines)):
                        line = lines[i]
                        if magicword2 in line:
                            print("[info] Here is lines of file.")
                            print(lines[i])
                            print(lines[i+1])
                            print(lines[i+2])
                            messagebox.showwarning('Info', 'Look at AGENDA, '
                                'there is an appointment tomorrow for : '\
                                + new_text2 + lines[i] + lines[i+1] + \
                                lines[i+2])

                            MSGREM2 = messagebox.askyesno("Ask", "Do you want to stop reminder ?")
                            if MSGREM2 == 1:
                                mwrename2 = magicword2.replace("/", ".")
                                write_f = open(os.path.join(path, file), 'w')
                                write_f.write("* Rdv past--> " + mwrename2 + "\n" +
                                    lines[i+1] + lines[i+2] + "\n")
                                print("[+] Modification finish")
                                break
                            else:
                                pass
    except (FileNotFoundError, IndexError) as infofile2:
        print("File 2 has not been found (agendapp.py)", infofile2)
    else:
        print("Error unknow for patient 2 (agendapp.py).")

    # Patient 3
    try:
        with open('./newpatient/entryfile3.txt', 'r') as namefile:
            line3 = namefile.readline()
            new_text3 = line3
    except FileNotFoundError as fileout3:
        print("No file entryfile3.txt exist", fileout3)

    try:
        magicword3 = (datetime.datetime.now() + datetime.timedelta(\
            days=1)).strftime('%d/%m/%Y')
        for path, dirs, files in os.walk('./patient_agenda/events3/'
            'doc_events/fix_agenda/agenda_saved/'):
            for file in files:
                with open(os.path.join(path, file), 'r') as read_f:
                    lines = read_f.readlines()
                    for i in range(0, len(lines)):
                        line = lines[i]
                        if magicword3 in line:
                            print("[info] Here is lines of file.")
                            print(lines[i])
                            print(lines[i+1])
                            print(lines[i+2])
                            messagebox.showwarning('Info', 'Look at AGENDA, '
                                'there is an appointment tomorrow for : '\
                                + new_text3 + lines[i] + lines[i+1] + \
                                lines[i+2])

                            MSGREM3 = messagebox.askyesno("Ask", "Do you want to stop reminder ?")
                            if MSGREM3 == 1:
                                mwrename3 = magicword3.replace("/", ".")
                                write_f = open(os.path.join(path, file), 'w')
                                write_f.write("* Rdv past--> " + mwrename3 + "\n" +
                                    lines[i+1] + lines[i+2] + "\n")
                                print("[+] Modification finish")
                                break
                            else:
                                pass
    except (FileNotFoundError, IndexError) as infofile3:
        print("File 3 has not been found (agendapp.py)", infofile3)
    else:
        print("Error unknow for patient 3 (agendapp.py).")

    # Patient 4
    try:
        with open('./newpatient/entryfile4.txt', 'r') as namefile:
            line4 = namefile.readline()
            new_text4 = line4
    except FileNotFoundError as fileout4:
        print("No file entryfile4.txt exist", fileout4)

    try:
        magicword4 = (datetime.datetime.now() + datetime.timedelta(\
            days=1)).strftime('%d/%m/%Y')
        for path, dirs, files in os.walk('./patient_agenda/events4/'
            'doc_events/fix_agenda/agenda_saved/'):
            for file in files:
                with open(os.path.join(path, file), 'r') as read_f:
                    lines = read_f.readlines()
                    for i in range(0, len(lines)):
                        line = lines[i]
                        if magicword4 in line:
                            print("[info] Here is lines of file.")
                            print(lines[i])
                            print(lines[i+1])
                            print(lines[i+2])
                            messagebox.showwarning('Info', 'Look at AGENDA, '
                                'there is an appointment tomorrow for : '\
                                + new_text4 + lines[i] + lines[i+1] + \
                                lines[i+2])

                            MSGREM4 = messagebox.askyesno("Ask", "Do you want to stop reminder ?")
                            if MSGREM4 == 1:
                                mwrename4 = magicword4.replace("/", ".")
                                write_f = open(os.path.join(path, file), 'w')
                                write_f.write("* Rdv past--> " + mwrename4 + "\n" +
                                    lines[i+1] + lines[i+2] + "\n")
                                print("[+] Modification finish")
                                break
                            else:
                                pass
    except (FileNotFoundError, IndexError) as infofile4:
        print("File 4 has not been found (agendapp.py)", infofile4)
    else:
        print("Error unknow for patient 4 (agendapp.py).")

    # Patient 5
    try:
        with open('./newpatient/entryfile5.txt', 'r') as namefile:
            line5 = namefile.readline()
            new_text5 = line5
    except FileNotFoundError as fileout5:
        print("No file entryfile5.txt exist", fileout5)

    try:
        magicword5 = (datetime.datetime.now() + datetime.timedelta(\
            days=1)).strftime('%d/%m/%Y')
        for path, dirs, files in os.walk('./patient_agenda/events5/'
            'doc_events/fix_agenda/agenda_saved/'):
            for file in files:
                with open(os.path.join(path, file), 'r') as read_f:
                    lines = read_f.readlines()
                    for i in range(0, len(lines)):
                        line = lines[i]
                        if magicword5 in line:
                            print("[info] Here is lines of file.")
                            print(lines[i])
                            print(lines[i+1])
                            print(lines[i+2])
                            messagebox.showwarning('Info', 'Look at AGENDA, '
                                'there is an appointment tomorrow for : '\
                                + new_text5 + lines[i] + lines[i+1] + \
                                lines[i+2])

                            MSGREM5 = messagebox.askyesno("Ask", "Do you want to stop reminder ?")
                            if MSGREM5 == 1:
                                mwrename5 = magicword5.replace("/", ".")
                                write_f = open(os.path.join(path, file), 'w')
                                write_f.write("* Rdv past--> " + mwrename5 + "\n" +
                                    lines[i+1] + lines[i+2] + "\n")
                                print("[+] Modification finish")
                                break
                            else:
                                pass
    except (FileNotFoundError, IndexError) as infofile5:
        print("File 5 has not been found (agendapp.py)", infofile5)
    else:
        print("Error unknow for patient 5 (agendapp.py).")

    # Patient 6
    try:
        with open('./newpatient/entryfile6.txt', 'r') as namefile:
            line6 = namefile.readline()
            new_text6 = line6
    except FileNotFoundError as fileout6:
        print("No file entryfile6.txt exist", fileout6)

    try:
        magicword6 = (datetime.datetime.now() + datetime.timedelta(\
            days=1)).strftime('%d/%m/%Y')
        for path, dirs, files in os.walk('./patient_agenda/events6/'
            'doc_events/fix_agenda/agenda_saved/'):
            for file in files:
                with open(os.path.join(path, file), 'r') as read_f:
                    lines = read_f.readlines()
                    for i in range(0, len(lines)):
                        line = lines[i]
                        if magicword6 in line:
                            print("[info] Here is lines of file.")
                            print(lines[i])
                            print(lines[i+1])
                            print(lines[i+2])
                            messagebox.showwarning('Info', 'Look at AGENDA, '
                                'there is an appointment tomorrow for : '\
                                + new_text6 + lines[i] + lines[i+1] + \
                                lines[i+2])

                            MSGREM6 = messagebox.askyesno("Ask", "Do you want to stop reminder ?")
                            if MSGREM6 == 1:
                                mwrename6 = magicword6.replace("/", ".")
                                write_f = open(os.path.join(path, file), 'w')
                                write_f.write("* Rdv past--> " + mwrename6 + "\n" +
                                    lines[i+1] + lines[i+2] + "\n")
                                print("[+] Modification finish")
                                break
                            else:
                                pass
    except (FileNotFoundError, IndexError) as infofile6:
        print("File 6 has not been found (agendapp.py)", infofile6)
    else:
        print("Error unknow for patient 6 (agendapp.py).")

    # Patient 7
    try:
        with open('./newpatient/entryfile7.txt', 'r') as namefile:
            line7 = namefile.readline()
            new_text7 = line7
    except FileNotFoundError as fileout7:
        print("No file entryfile7.txt exist", fileout7)

    try:
        magicword7 = (datetime.datetime.now() + datetime.timedelta(\
            days=1)).strftime('%d/%m/%Y')
        for path, dirs, files in os.walk('./patient_agenda/events7/'
            'doc_events/fix_agenda/agenda_saved/'):
            for file in files:
                with open(os.path.join(path, file), 'r') as read_f:
                    lines = read_f.readlines()
                    for i in range(0, len(lines)):
                        line = lines[i]
                        if magicword7 in line:
                            print("[info] Here is lines of file.")
                            print(lines[i])
                            print(lines[i+1])
                            print(lines[i+2])
                            messagebox.showwarning('Info', 'Look at AGENDA, '
                                'there is an appointment tomorrow for : '\
                                + new_text7 + lines[i] + lines[i+1] + \
                                lines[i+2])

                            MSGREM7 = messagebox.askyesno("Ask", "Do you want to stop reminder ?")
                            if MSGREM7 == 1:
                                mwrename7 = magicword7.replace("/", ".")
                                write_f = open(os.path.join(path, file), 'w')
                                write_f.write("* Rdv past--> " + mwrename7 + "\n" +
                                    lines[i+1] + lines[i+2] + "\n")
                                print("[+] Modification finish")
                                break
                            else:
                                pass
    except (FileNotFoundError, IndexError) as infofile7:
        print("File 7 has not been found (agendapp.py)", infofile7)
    else:
        print("Error unknow for patient 7 (agendapp.py).")

    # Patient 8
    try:
        with open('./newpatient/entryfile8.txt', 'r') as namefile:
            line8 = namefile.readline()
            new_text8 = line8
    except FileNotFoundError as fileout8:
        print("No file entryfile8.txt exist", fileout8)

    try:
        magicword8 = (datetime.datetime.now() + datetime.timedelta(\
            days=1)).strftime('%d/%m/%Y')
        for path, dirs, files in os.walk('./patient_agenda/events8/'
            'doc_events/fix_agenda/agenda_saved/'):
            for file in files:
                with open(os.path.join(path, file), 'r') as read_f:
                    lines = read_f.readlines()
                    for i in range(0, len(lines)):
                        line = lines[i]
                        if magicword8 in line:
                            print("[info] Here is lines of file.")
                            print(lines[i])
                            print(lines[i+1])
                            print(lines[i+2])
                            messagebox.showwarning('Info', 'Look at AGENDA, '
                                'there is an appointment tomorrow for : '\
                                + new_text8 + lines[i] + lines[i+1] + \
                                lines[i+2])

                            MSGREM8 = messagebox.askyesno("Ask", "Do you want to stop reminder ?")
                            if MSGREM8 == 1:
                                mwrename8 = magicword8.replace("/", ".")
                                write_f = open(os.path.join(path, file), 'w')
                                write_f.write("* Rdv past--> " + mwrename8 + "\n" +
                                    lines[i+1] + lines[i+2] + "\n")
                                print("[+] Modification finish")
                                break
                            else:
                                pass
    except (FileNotFoundError, IndexError) as infofile8:
        print("File 8 has not been found (agendapp.py)", infofile8)
    else:
        print("Error unknow for patient 8 (agendapp.py).")

    # Patient 9
    try:
        with open('./newpatient/entryfile9.txt', 'r') as namefile:
            line9 = namefile.readline()
            new_text9 = line9
    except FileNotFoundError as fileout9:
        print("No file entryfile9.txt exist", fileout9)

    try:
        magicword9 = (datetime.datetime.now() + datetime.timedelta(\
            days=1)).strftime('%d/%m/%Y')
        for path, dirs, files in os.walk('./patient_agenda/events9/'
            'doc_events/fix_agenda/agenda_saved/'):
            for file in files:
                with open(os.path.join(path, file), 'r') as read_f:
                    lines = read_f.readlines()
                    for i in range(0, len(lines)):
                        line = lines[i]
                        if magicword9 in line:
                            print("[info] Here is lines of file.")
                            print(lines[i])
                            print(lines[i+1])
                            print(lines[i+2])
                            messagebox.showwarning('Info', 'Look at AGENDA, '
                                'there is an appointment tomorrow for : '\
                                + new_text9 + lines[i] + lines[i+1] + \
                                lines[i+2])

                            MSGREM9 = messagebox.askyesno("Ask", "Do you want to stop reminder ?")
                            if MSGREM9 == 1:
                                mwrename9 = magicword9.replace("/", ".")
                                write_f = open(os.path.join(path, file), 'w')
                                write_f.write("* Rdv past--> " + mwrename9 + "\n" +
                                    lines[i+1] + lines[i+2] + "\n")
                                print("[+] Modification finish")
                                break
                            else:
                                pass
    except (FileNotFoundError, IndexError) as infofile9:
        print("File 9 has not been found (agendapp.py)", infofile9)
    else:
        print("Error unknow for patient 9 (agendapp.py).")

    # Patient 10
    try:
        with open('./newpatient/entryfile10.txt', 'r') as namefile:
            line10 = namefile.readline()
            new_text10 = line10
    except FileNotFoundError as fileout10:
        print("No file entryfile10.txt exist", fileout10)

    try:
        magicword10 = (datetime.datetime.now() + datetime.timedelta(\
            days=1)).strftime('%d/%m/%Y')
        for path, dirs, files in os.walk('./patient_agenda/events10/'
            'doc_events/fix_agenda/agenda_saved/'):
            for file in files:
                with open(os.path.join(path, file), 'r') as read_f:
                    lines = read_f.readlines()
                    for i in range(0, len(lines)):
                        line = lines[i]
                        if magicword10 in line:
                            print("[info] Here is lines of file.")
                            print(lines[i])
                            print(lines[i+1])
                            print(lines[i+2])
                            messagebox.showwarning('Info', 'Look at AGENDA, '
                                'there is an appointment tomorrow for : '\
                                + new_text10 + lines[i] + lines[i+1] + \
                                lines[i+2])

                            MSGREM10 = messagebox.askyesno("Ask", "Do you want to stop reminder ?")
                            if MSGREM10 == 1:
                                mwrename10 = magicword10.replace("/", ".")
                                write_f = open(os.path.join(path, file), 'w')
                                write_f.write("* Rdv past--> " + mwrename10 + "\n" +
                                    lines[i+1] + lines[i+2] + "\n")
                                print("[+] Modification finish")
                                break
                            else:
                                pass
    except (FileNotFoundError, IndexError) as infofile10:
        print("File 10 has not been found (agendapp.py)", infofile10)
    else:
        print("Error unknow for patient 10 (agendapp.py).")

    # Patient 11
    try:
        with open('./newpatient/entryfile11.txt', 'r') as namefile:
            line11 = namefile.readline()
            new_text11 = line11
    except FileNotFoundError as fileout11:
        print("No file entryfile11.txt exist", fileout11)

    try:
        magicword11 = (datetime.datetime.now() + datetime.timedelta(\
            days=1)).strftime('%d/%m/%Y')
        for path, dirs, files in os.walk('./patient_agenda/events11/'
            'doc_events/fix_agenda/agenda_saved/'):
            for file in files:
                with open(os.path.join(path, file), 'r') as read_f:
                    lines = read_f.readlines()
                    for i in range(0, len(lines)):
                        line = lines[i]
                        if magicword11 in line:
                            print("[info] Here is lines of file.")
                            print(lines[i])
                            print(lines[i+1])
                            print(lines[i+2])
                            messagebox.showwarning('Info', 'Look at AGENDA, '
                                'there is an appointment tomorrow for : '\
                                + new_text11 + lines[i] + lines[i+1] + \
                                lines[i+2])

                            MSGREM11 = messagebox.askyesno("Ask", "Do you want to stop reminder ?")
                            if MSGREM11 == 1:
                                mwrename11 = magicword11.replace("/", ".")
                                write_f = open(os.path.join(path, file), 'w')
                                write_f.write("* Rdv past--> " + mwrename11 + "\n" +
                                    lines[i+1] + lines[i+2] + "\n")
                                print("[+] Modification finish")
                                break
                            else:
                                pass
    except (FileNotFoundError, IndexError) as infofile11:
        print("File 11 has not been found (agendapp.py)", infofile11)
    else:
        print("Error unknow for patient 11 (agendapp.py).")

    # Patient 12
    try:
        with open('./newpatient/entryfile12.txt', 'r') as namefile:
            line12 = namefile.readline()
            new_text12 = line12
    except FileNotFoundError as fileout12:
        print("No file entryfile12.txt exist", fileout12)

    try:
        magicword12 = (datetime.datetime.now() + datetime.timedelta(\
            days=1)).strftime('%d/%m/%Y')
        for path, dirs, files in os.walk('./patient_agenda/events12/'
            'doc_events/fix_agenda/agenda_saved/'):
            for file in files:
                with open(os.path.join(path, file), 'r') as read_f:
                    lines = read_f.readlines()
                    for i in range(0, len(lines)):
                        line = lines[i]
                        if magicword12 in line:
                            print("[info] Here is lines of file.")
                            print(lines[i])
                            print(lines[i+1])
                            print(lines[i+2])
                            messagebox.showwarning('Info', 'Look at AGENDA, '
                                'there is an appointment tomorrow for : '\
                                + new_text12 + lines[i] + lines[i+1] + \
                                lines[i+2])

                            MSGREM12 = messagebox.askyesno("Ask", "Do you want to stop reminder ?")
                            if MSGREM12 == 1:
                                mwrename12 = magicword12.replace("/", ".")
                                write_f = open(os.path.join(path, file), 'w')
                                write_f.write("* Rdv past--> " + mwrename12 + "\n" +
                                    lines[i+1] + lines[i+2] + "\n")
                                print("[+] Modification finish")
                                break
                            else:
                                pass
    except (FileNotFoundError, IndexError) as infofile12:
        print("File 12 has not been found (agendapp.py)", infofile12)
    else:
        print("Error unknow for patient 12 (agendapp.py).")

    # Patient 13
    try:
        with open('./newpatient/entryfile13.txt', 'r') as namefile:
            line13 = namefile.readline()
            new_text13 = line13
    except FileNotFoundError as fileout13:
        print("No file entryfile13.txt exist", fileout13)

    try:
        magicword13 = (datetime.datetime.now() + datetime.timedelta(\
            days=1)).strftime('%d/%m/%Y')
        for path, dirs, files in os.walk('./patient_agenda/events13/'
            'doc_events/fix_agenda/agenda_saved/'):
            for file in files:
                with open(os.path.join(path, file), 'r') as read_f:
                    lines = read_f.readlines()
                    for i in range(0, len(lines)):
                        line = lines[i]
                        if magicword13 in line:
                            print("[info] Here is lines of file.")
                            print(lines[i])
                            print(lines[i+1])
                            print(lines[i+2])
                            messagebox.showwarning('Info', 'Look at AGENDA, '
                                'there is an appointment tomorrow for : '\
                                + new_text13 + lines[i] + lines[i+1] + \
                                lines[i+2])

                            MSGREM13 = messagebox.askyesno("Ask", "Do you want to stop reminder ?")
                            if MSGREM13 == 1:
                                mwrename13 = magicword13.replace("/", ".")
                                write_f = open(os.path.join(path, file), 'w')
                                write_f.write("* Rdv past--> " + mwrename13 + "\n" +
                                    lines[i+1] + lines[i+2] + "\n")
                                print("[+] Modification finish")
                                break
                            else:
                                pass
    except (FileNotFoundError, IndexError) as infofile13:
        print("File 13 has not been found (agendapp.py)", infofile13)
    else:
        print("Error unknow for patient 13 (agendapp.py).")

    # Patient 14
    try:
        with open('./newpatient/entryfile14.txt', 'r') as namefile:
            line14 = namefile.readline()
            new_text14 = line14
    except FileNotFoundError as fileout14:
        print("No file entryfile14.txt exist", fileout14)

    try:
        magicword14 = (datetime.datetime.now() + datetime.timedelta(\
            days=1)).strftime('%d/%m/%Y')
        for path, dirs, files in os.walk('./patient_agenda/events14/'
            'doc_events/fix_agenda/agenda_saved/'):
            for file in files:
                with open(os.path.join(path, file), 'r') as read_f:
                    lines = read_f.readlines()
                    for i in range(0, len(lines)):
                        line = lines[i]
                        if magicword14 in line:
                            print("[info] Here is lines of file.")
                            print(lines[i])
                            print(lines[i+1])
                            print(lines[i+2])
                            messagebox.showwarning('Info', 'Look at AGENDA, '
                                'there is an appointment tomorrow for : '\
                                + new_text14 + lines[i] + lines[i+1] + \
                                lines[i+2])

                            MSGREM14 = messagebox.askyesno("Ask", "Do you want to stop reminder ?")
                            if MSGREM14 == 1:
                                mwrename14 = magicword14.replace("/", ".")
                                write_f = open(os.path.join(path, file), 'w')
                                write_f.write("* Rdv past--> " + mwrename14 + "\n" +
                                    lines[i+1] + lines[i+2] + "\n")
                                print("[+] Modification finish")
                                break
                            else:
                                pass
    except (FileNotFoundError, IndexError) as infofile14:
        print("File 14 has not been found (agendapp.py)", infofile14)
    else:
        print("Error unknow for patient 14 (agendapp.py).")

    # Patient 15
    try:
        with open('./newpatient/entryfile15.txt', 'r') as namefile:
            line15 = namefile.readline()
            new_text15 = line15
    except FileNotFoundError as fileout15:
        print("No file entryfile15.txt exist", fileout15)

    try:
        magicword15 = (datetime.datetime.now() + datetime.timedelta(\
            days=1)).strftime('%d/%m/%Y')
        for path, dirs, files in os.walk('./patient_agenda/events15/'
            'doc_events/fix_agenda/agenda_saved/'):
            for file in files:
                with open(os.path.join(path, file), 'r') as read_f:
                    lines = read_f.readlines()
                    for i in range(0, len(lines)):
                        line = lines[i]
                        if magicword15 in line:
                            print("[info] Here is lines of file.")
                            print(lines[i])
                            print(lines[i+1])
                            print(lines[i+2])
                            messagebox.showwarning('Info', 'Look at AGENDA, '
                                'there is an appointment tomorrow for : '\
                                + new_text15 + lines[i] + lines[i+1] + \
                                lines[i+2])

                            MSGREM15 = messagebox.askyesno("Ask", "Do you want to stop reminder ?")
                            if MSGREM15 == 1:
                                mwrename15 = magicword15.replace("/", ".")
                                write_f = open(os.path.join(path, file), 'w')
                                write_f.write("* Rdv past--> " + mwrename15 + "\n" +
                                    lines[i+1] + lines[i+2] + "\n")
                                print("[+] Modification finish")
                                break
                            else:
                                pass
    except (FileNotFoundError, IndexError) as infofile15:
        print("File 15 has not been found (agendapp.py)", infofile15)
    else:
        print("Error unknow for patient 15 (agendapp.py).")

    # Patient 16
    try:
        with open('./newpatient/entryfile16.txt', 'r') as namefile:
            line16 = namefile.readline()
            new_text16 = line16
    except FileNotFoundError as fileout16:
        print("No file entryfile16.txt exist", fileout16)

    try:
        magicword16 = (datetime.datetime.now() + datetime.timedelta(\
            days=1)).strftime('%d/%m/%Y')
        for path, dirs, files in os.walk('./patient_agenda/events16/'
            'doc_events/fix_agenda/agenda_saved/'):
            for file in files:
                with open(os.path.join(path, file), 'r') as read_f:
                    lines = read_f.readlines()
                    for i in range(0, len(lines)):
                        line = lines[i]
                        if magicword16 in line:
                            print("[info] Here is lines of file.")
                            print(lines[i])
                            print(lines[i+1])
                            print(lines[i+2])
                            messagebox.showwarning('Info', 'Look at AGENDA, '
                                'there is an appointment tomorrow for : '\
                                + new_text16 + lines[i] + lines[i+1] + \
                                lines[i+2])

                            MSGREM16 = messagebox.askyesno("Ask", "Do you want to stop reminder ?")
                            if MSGREM16 == 1:
                                mwrename16 = magicword16.replace("/", ".")
                                write_f = open(os.path.join(path, file), 'w')
                                write_f.write("* Rdv past--> " + mwrename16 + "\n" +
                                    lines[i+1] + lines[i+2] + "\n")
                                print("[+] Modification finish")
                                break
                            else:
                                pass
    except (FileNotFoundError, IndexError) as infofile16:
        print("File 16 has not been found (agendapp.py)", infofile16)
    else:
        print("Error unknow for patient 16 (agendapp.py).")

    # Patient 17
    try:
        with open('./newpatient/entryfile17.txt', 'r') as namefile:
            line17 = namefile.readline()
            new_text17 = line17
    except FileNotFoundError as fileout17:
        print("No file entryfile17.txt exist", fileout17)

    try:
        magicword17 = (datetime.datetime.now() + datetime.timedelta(\
            days=1)).strftime('%d/%m/%Y')
        for path, dirs, files in os.walk('./patient_agenda/events17/'
            'doc_events/fix_agenda/agenda_saved/'):
            for file in files:
                with open(os.path.join(path, file), 'r') as read_f:
                    lines = read_f.readlines()
                    for i in range(0, len(lines)):
                        line = lines[i]
                        if magicword17 in line:
                            print("[info] Here is lines of file.")
                            print(lines[i])
                            print(lines[i+1])
                            print(lines[i+2])
                            messagebox.showwarning('Info', 'Look at AGENDA, '
                                'there is an appointment tomorrow for : '\
                                + new_text17 + lines[i] + lines[i+1] + \
                                lines[i+2])

                            MSGREM17 = messagebox.askyesno("Ask", "Do you want to stop reminder ?")
                            if MSGREM17 == 1:
                                mwrename17 = magicword17.replace("/", ".")
                                write_f = open(os.path.join(path, file), 'w')
                                write_f.write("* Rdv past--> " + mwrename17 + "\n" +
                                    lines[i+1] + lines[i+2] + "\n")
                                print("[+] Modification finish")
                                break
                            else:
                                pass
    except (FileNotFoundError, IndexError) as infofile17:
        print("File 17 has not been found (agendapp.py)", infofile17)
    else:
        print("Error unknow for patient 17 (agendapp.py).")

    # Patient 18
    try:
        with open('./newpatient/entryfile18.txt', 'r') as namefile:
            line18 = namefile.readline()
            new_text18 = line18
    except FileNotFoundError as fileout18:
        print("No file entryfile18.txt exist", fileout18)

    try:
        magicword18 = (datetime.datetime.now() + datetime.timedelta(\
            days=1)).strftime('%d/%m/%Y')
        for path, dirs, files in os.walk('./patient_agenda/events18/'
            'doc_events/fix_agenda/agenda_saved/'):
            for file in files:
                with open(os.path.join(path, file), 'r') as read_f:
                    lines = read_f.readlines()
                    for i in range(0, len(lines)):
                        line = lines[i]
                        if magicword18 in line:
                            print("[info] Here is lines of file.")
                            print(lines[i])
                            print(lines[i+1])
                            print(lines[i+2])
                            messagebox.showwarning('Info', 'Look at AGENDA, '
                                'there is an appointment tomorrow for : '\
                                + new_text18 + lines[i] + lines[i+1] + \
                                lines[i+2])

                            MSGREM18 = messagebox.askyesno("Ask", "Do you want to stop reminder ?")
                            if MSGREM18 == 1:
                                mwrename18 = magicword18.replace("/", ".")
                                write_f = open(os.path.join(path, file), 'w')
                                write_f.write("* Rdv past--> " + mwrename18 + "\n" +
                                    lines[i+1] + lines[i+2] + "\n")
                                print("[+] Modification finish")
                                break
                            else:
                                pass
    except (FileNotFoundError, IndexError) as infofile18:
        print("File 18 has not been found (agendapp.py)", infofile18)
    else:
        print("Error unknow for patient 18 (agendapp.py).")

    # Patient 19
    try:
        with open('./newpatient/entryfile19.txt', 'r') as namefile:
            line19 = namefile.readline()
            new_text19 = line19
    except FileNotFoundError as fileout19:
        print("No file entryfile19.txt exist", fileout19)

    try:
        magicword19 = (datetime.datetime.now() + datetime.timedelta(\
            days=1)).strftime('%d/%m/%Y')
        for path, dirs, files in os.walk('./patient_agenda/events19/'
            'doc_events/fix_agenda/agenda_saved/'):
            for file in files:
                with open(os.path.join(path, file), 'r') as read_f:
                    lines = read_f.readlines()
                    for i in range(0, len(lines)):
                        line = lines[i]
                        if magicword19 in line:
                            print("[info] Here is lines of file.")
                            print(lines[i])
                            print(lines[i+1])
                            print(lines[i+2])
                            messagebox.showwarning('Info', 'Look at AGENDA, '
                                'there is an appointment tomorrow for : '\
                                + new_text19 + lines[i] + lines[i+1] + \
                                lines[i+2])

                            MSGREM19 = messagebox.askyesno("Ask", "Do you want to stop reminder ?")
                            if MSGREM19 == 1:
                                mwrename19 = magicword19.replace("/", ".")
                                write_f = open(os.path.join(path, file), 'w')
                                write_f.write("* Rdv past--> " + mwrename19 + "\n" +
                                    lines[i+1] + lines[i+2] + "\n")
                                print("[+] Modification finish")
                                break
                            else:
                                pass
    except (FileNotFoundError, IndexError) as infofile19:
        print("File 19 has not been found (agendapp.py)", infofile19)
    else:
        print("Error unknow for patient 19 (agendapp.py).")

    # Patient 20
    try:
        with open('./newpatient/entryfile20.txt', 'r') as namefile:
            line20 = namefile.readline()
            new_text20 = line20
    except FileNotFoundError as fileout20:
        print("No file entryfile20.txt exist", fileout20)

    try:
        magicword20 = (datetime.datetime.now() + datetime.timedelta(\
            days=1)).strftime('%d/%m/%Y')
        for path, dirs, files in os.walk('./patient_agenda/events20/'
            'doc_events/fix_agenda/agenda_saved/'):
            for file in files:
                with open(os.path.join(path, file), 'r') as read_f:
                    lines = read_f.readlines()
                    for i in range(0, len(lines)):
                        line = lines[i]
                        if magicword20 in line:
                            print("[info] Here is lines of file.")
                            print(lines[i])
                            print(lines[i+1])
                            print(lines[i+2])
                            messagebox.showwarning('Info', 'Look at AGENDA, '
                                'there is an appointment tomorrow for : '\
                                + new_text20 + lines[i] + lines[i+1] + \
                                lines[i+2])

                            MSGREM20 = messagebox.askyesno("Ask", "Do you want to stop reminder ?")
                            if MSGREM20 == 1:
                                mwrename20 = magicword20.replace("/", ".")
                                write_f = open(os.path.join(path, file), 'w')
                                write_f.write("* Rdv past--> " + mwrename20 + "\n" +
                                    lines[i+1] + lines[i+2] + "\n")
                                print("[+] Modification finish")
                                break
                            else:
                                pass
    except (FileNotFoundError, IndexError) as infofile20:
        print("File 20 has not been found (agendapp.py)", infofile20)
    else:
        print("Error unknow for patient 20 (agendapp.py).")

    # Patient 21
    try:
        with open('./newpatient/entryfile21.txt', 'r') as namefile:
            line21 = namefile.readline()
            new_text21 = line21
    except FileNotFoundError as fileout21:
        print("No file entryfile21.txt exist", fileout21)

    try:
        magicword21 = (datetime.datetime.now() + datetime.timedelta(\
            days=1)).strftime('%d/%m/%Y')
        for path, dirs, files in os.walk('./patient_agenda/events21/'
            'doc_events/fix_agenda/agenda_saved/'):
            for file in files:
                with open(os.path.join(path, file), 'r') as read_f:
                    lines = read_f.readlines()
                    for i in range(0, len(lines)):
                        line = lines[i]
                        if magicword21 in line:
                            print("[info] Here is lines of file.")
                            print(lines[i])
                            print(lines[i+1])
                            print(lines[i+2])
                            messagebox.showwarning('Info', 'Look at AGENDA, '
                                'there is an appointment tomorrow for : '\
                                + new_text21 + lines[i] + lines[i+1] + \
                                lines[i+2])

                            MSGREM21 = messagebox.askyesno("Ask", "Do you want to stop reminder ?")
                            if MSGREM21 == 1:
                                mwrename21 = magicword21.replace("/", ".")
                                write_f = open(os.path.join(path, file), 'w')
                                write_f.write("* Rdv past--> " + mwrename21 + "\n" +
                                    lines[i+1] + lines[i+2] + "\n")
                                print("[+] Modification finish")
                                break
                            else:
                                pass
    except (FileNotFoundError, IndexError) as infofile21:
        print("File 21 has not been found (agendapp.py)", infofile21)
    else:
        print("Error unknow for patient 21 (agendapp.py).")

    # Patient 22
    try:
        with open('./newpatient/entryfile22.txt', 'r') as namefile:
            line22 = namefile.readline()
            new_text22 = line22
    except FileNotFoundError as fileout22:
        print("No file entryfile22.txt exist", fileout22)

    try:
        magicword22 = (datetime.datetime.now() + datetime.timedelta(\
            days=1)).strftime('%d/%m/%Y')
        for path, dirs, files in os.walk('./patient_agenda/events22/'
            'doc_events/fix_agenda/agenda_saved/'):
            for file in files:
                with open(os.path.join(path, file), 'r') as read_f:
                    lines = read_f.readlines()
                    for i in range(0, len(lines)):
                        line = lines[i]
                        if magicword22 in line:
                            print("[info] Here is lines of file.")
                            print(lines[i])
                            print(lines[i+1])
                            print(lines[i+2])
                            messagebox.showwarning('Info', 'Look at AGENDA, '
                                'there is an appointment tomorrow for : '\
                                + new_text22 + lines[i] + lines[i+1] + \
                                lines[i+2])

                            MSGREM22 = messagebox.askyesno("Ask", "Do you want to stop reminder ?")
                            if MSGREM22 == 1:
                                mwrename22 = magicword22.replace("/", ".")
                                write_f = open(os.path.join(path, file), 'w')
                                write_f.write("* Rdv past--> " + mwrename22 + "\n" +
                                    lines[i+1] + lines[i+2] + "\n")
                                print("[+] Modification finish")
                                break
                            else:
                                pass
    except (FileNotFoundError, IndexError) as infofile22:
        print("File 22 has not been found (agendapp.py)", infofile22)
    else:
        print("Error unknow for patient 22 (agendapp.py).")

    # Patient 23
    try:
        with open('./newpatient/entryfile23.txt', 'r') as namefile:
            line23 = namefile.readline()
            new_text23 = line23
    except FileNotFoundError as fileout23:
        print("No file entryfile23.txt exist", fileout23)

    try:
        magicword23 = (datetime.datetime.now() + datetime.timedelta(\
            days=1)).strftime('%d/%m/%Y')
        for path, dirs, files in os.walk('./patient_agenda/events23/'
            'doc_events/fix_agenda/agenda_saved/'):
            for file in files:
                with open(os.path.join(path, file), 'r') as read_f:
                    lines = read_f.readlines()
                    for i in range(0, len(lines)):
                        line = lines[i]
                        if magicword23 in line:
                            print("[info] Here is lines of file.")
                            print(lines[i])
                            print(lines[i+1])
                            print(lines[i+2])
                            messagebox.showwarning('Info', 'Look at AGENDA, '
                                'there is an appointment tomorrow for : '\
                                + new_text23 + lines[i] + lines[i+1] + \
                                lines[i+2])

                            MSGREM23 = messagebox.askyesno("Ask", "Do you want to stop reminder ?")
                            if MSGREM23 == 1:
                                mwrename23 = magicword23.replace("/", ".")
                                write_f = open(os.path.join(path, file), 'w')
                                write_f.write("* Rdv past--> " + mwrename23 + "\n" +
                                    lines[i+1] + lines[i+2] + "\n")
                                print("[+] Modification finish")
                                break
                            else:
                                pass
    except (FileNotFoundError, IndexError) as infofile23:
        print("File 23 has not been found (agendapp.py)", infofile23)
    else:
        print("Error unknow for patient 23 (agendapp.py).")

    # Patient 24
    try:
        with open('./newpatient/entryfile24.txt', 'r') as namefile:
            line24 = namefile.readline()
            new_text24 = line24
    except FileNotFoundError as fileout24:
        print("No file entryfile24.txt exist", fileout24)

    try:
        magicword24 = (datetime.datetime.now() + datetime.timedelta(\
            days=1)).strftime('%d/%m/%Y')
        for path, dirs, files in os.walk('./patient_agenda/events24/'
            'doc_events/fix_agenda/agenda_saved/'):
            for file in files:
                with open(os.path.join(path, file), 'r') as read_f:
                    lines = read_f.readlines()
                    for i in range(0, len(lines)):
                        line = lines[i]
                        if magicword24 in line:
                            print("[info] Here is lines of file.")
                            print(lines[i])
                            print(lines[i+1])
                            print(lines[i+2])
                            messagebox.showwarning('Info', 'Look at AGENDA, '
                                'there is an appointment tomorrow for : '\
                                + new_text24 + lines[i] + lines[i+1] + \
                                lines[i+2])

                            MSGREM24 = messagebox.askyesno("Ask", "Do you want to stop reminder ?")
                            if MSGREM24 == 1:
                                mwrename24 = magicword24.replace("/", ".")
                                write_f = open(os.path.join(path, file), 'w')
                                write_f.write("* Rdv past--> " + mwrename24 + "\n" +
                                    lines[i+1] + lines[i+2] + "\n")
                                print("[+] Modification finish")
                                break
                            else:
                                pass
    except (FileNotFoundError, IndexError) as infofile24:
        print("File 24 has not been found (agendapp.py)", infofile24)
    else:
        print("Error unknow for patient 24 (agendapp.py).")
