#!/usr/bin/python3
# -*- coding: utf-8 -*-


import tkinter as tk
import os
import subprocess
import datetime
import calendar
from pickle import dump


class Calendar:
    """
        Class agenda with all attributes from module
        (don't give name : "calendar to this file,
        otherwise, you will get surprise...")
    """
    def __init__(self, parent, values):
        self.values = values
        self.parent = parent
        self.cal = calendar.TextCalendar(calendar.SUNDAY)
        self.year = datetime.date.today().year
        self.month = datetime.date.today().month
        actualday = datetime.date.today().day
        self.wid = []
        self.day_selected = actualday
        self.month_selected = self.month
        self.year_selected = self.year
        self.day_name = ''

        self.setup(self.year, self.month)

    def clear(self):
        for w in self.wid[:]:
            w.grid_forget()
            self.wid.remove(w)

    def go_prev(self):
        if self.month > 1:
            self.month -= 1
        else:
            self.month = 12
            self.year -= 1

        self.clear()
        self.setup(self.year, self.month)

    def go_next(self):
        if self.month < 12:
            self.month += 1
        else:
            self.month = 1
            self.year += 1

        self.clear()
        self.setup(self.year, self.month)

    def selection(self, actualday, name):
        self.day_selected = actualday
        self.month_selected = self.month
        self.year_selected = self.year
        self.day_name = name

        self.values['day_selected'] = actualday
        self.values['month_selected'] = self.month
        self.values['year_selected'] = self.year
        self.values['day_name'] = name
        self.values['month_name'] = calendar.month_name[self.month_selected]

        self.clear()
        self.setup(self.year, self.month)

    def setup(self, y, m):
        left = tk.Button(self.parent, text='<', width=15, height=1,
            fg='cyan', bg='RoyalBlue3', highlightbackground='RoyalBlue4',
            activebackground='pale turquoise', command=self.go_prev)
        self.wid.append(left)
        left.grid(row=0, column=0, columnspan=2, pady=20)

        #calendar.month_abbr[m]
        header = tk.Label(self.parent, fg='white', bg='DodgerBlue2',
            height=2, font=('Times New Roman', 16, 'bold'),
            text='{} {}'.format(calendar.month_name[m], str(y)))
        self.wid.append(header)
        header.grid(row=0, column=2, columnspan=3)

        right = tk.Button(self.parent, text='>', width=15, height=1,
            fg='cyan', bg='RoyalBlue3', highlightbackground='RoyalBlue4',
            activebackground='pale turquoise', command=self.go_next)
        self.wid.append(right)
        right.grid(row=0, column=5, columnspan=2, pady=20)

        days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

        for num, name in enumerate(days):
            t = tk.Label(self.parent, text=name[:3], font=('Times', 16, 'bold'),
                fg='yellow', bg='DodgerBlue2')
            self.wid.append(t)
            t.grid(row=1, column=num)

        for w, week in enumerate(self.cal.monthdayscalendar(y, m), 2):
            for d, actualday in enumerate(week):
                if actualday:
                    b = tk.Button(self.parent, width=6, height=3, text=actualday,
                        fg='white', bg='RoyalBlue3', highlightbackground='RoyalBlue4',
                        activebackground='pale turquoise',
                        command=lambda actualday=actualday:self.selection(actualday,
                            calendar.day_name[(actualday-1) % 7]))
                    self.wid.append(b)
                    b.grid(row=w, column=d, padx=1, pady=1)

        sel = tk.Label(self.parent, height=2,
            text='{} {} {}'.format(calendar.month_name[self.month_selected],
            self.day_selected, self.year_selected), font=('Times New Roman', 16, 'bold'),
        fg='white', bg='DodgerBlue2')
        self.wid.append(sel)
        sel.grid(row=8, column=0, columnspan=7)

        ok = tk.Button(self.parent, width=20, height=1, text='SAVE',
            font=('Times New Roman', 14, 'bold'), fg='cyan', bg='RoyalBlue3',
            highlightbackground='RoyalBlue4', activebackground='pale turquoise',
            command=self.kill_and_save)
        self.wid.append(ok)
        ok.grid(row=9, column=2, columnspan=3, pady=10)

    def kill_and_save(self):
        self.parent.destroy()

if __name__=='__main__':
    class Control:
        def __init__(self, parent):
            self.parent = parent.title("Time-Track")
            self.parent = parent.configure(background='RoyalBlue3')

            self.labelo = tk.Label(self.parent, text='Agenda',
                font='Times 18 bold', width=17, height=2,
                fg='white', bg='RoyalBlue3')

            with open('./newpatient/entryfile18.txt', 'r') as file_r:
                line_a = file_r.readline()

            self.data_time = tk.StringVar()
            self.entryname = tk.Entry(self.parent, textvariable=self.data_time,
                font='Times 14', width=20, fg='white', bg='DodgerBlue2', bd=2,
                highlightbackground='pale turquoise', justify=tk.CENTER)
            self.data_time.set(line_a[:-1])

            self.choose_btn = tk.Button(self.parent, text="1 - Choice a date",
                bd=2, font="Times 14", width=20, height=1, fg='cyan',
                bg='RoyalBlue4', highlightbackground='DodgerBlue2',
                activebackground='pale turquoise', command=self.popup)

            self.show_btn = tk.Button(self.parent, text='2 - Fix appointment',
                bd=2, font="Times 14", width=20, height=1,fg='cyan',
                bg='RoyalBlue4', highlightbackground='DodgerBlue2',
                activebackground='pale turquoise', command=self.print_selected_date)

            self.buttAgenda = tk.Button(self.parent, text='Agenda',
                font="Times 14", bd=2, width=20, height=1, fg='cyan',
                bg='RoyalBlue4', highlightbackground='DodgerBlue2',
                activebackground='pale turquoise', command=self.accessDate)

            self.buttLook = tk.Button(self.parent, text='Modifications',
                font="Times 14", bd=2, width=20, height=1,
                fg='cyan', bg='RoyalBlue4', highlightbackground='DodgerBlue2',
                activebackground='pale turquoise', command=self.accessLook)

            self.butQuit = tk.Button(self.parent, text='Quit', font="Times 14",
                width=20, bd=2, height=1, fg='white', bg='RoyalBlue4',
                activebackground='pale turquoise', command=quit)

            self.labelo.grid()
            self.entryname.grid(pady=10)
            self.choose_btn.grid()
            self.show_btn.grid()
            self.buttAgenda.grid()
            self.buttLook.grid()
            self.butQuit.grid()
            self.data = {}

        def popup(self):
            child = tk.Toplevel(bg='DodgerBlue2')
            child.resizable(False, False)
            cal = Calendar(child, self.data)

        def print_selected_date(self):
            """
                To write in binary into file
                patient_calendar.txt if it
                does not exist.
            """
            print(self.data)
            try:
                if os.path.getsize('./patient_agenda/events18/patient_calendar.txt'):
                    print("[+] File 'patient_calendar.txt' exist !")
                    file = open('./patient_agenda/events18/patient_calendar.txt','wb')
                    dump(self.data, file)
                    file.close()
                    subprocess.run('./patient_agenda/events18/entrer_event1.py', check=True)
            except FileNotFoundError as file_creat:
                print("[!] File not existing!")
                print(file_creat)
                print("[+] File 'patient_calendar.txt' created !")
                file = open('./patient_agenda/events18/patient_calendar.txt','wb')
                dump(self.data, file)
                file.close()
                subprocess.run('./patient_agenda/events18/entrer_event1.py', check=True)

        def accessDate(self):
            try:
                subprocess.run('./patient_agenda/events18/doc_events/fix_agenda/read_file.py',
                    check=True)
            except FileNotFoundError as note_agenda:
                print("[!] Agenda not created !")
                print(note_agenda)

        def accessLook(self):
            try:
                subprocess.run('./patient_agenda/events18/doc_events/fix_agenda/main.py',
                    check=True)
            except FileNotFoundError as note_change:
                print("[!] Agenda not created !")
                print(note_change)

    root = tk.Tk()
    root.resizable(False, False)
    app = Control(root)
    root.mainloop()
