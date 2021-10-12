#!/usr/bin/python3
# -*- coding: utf-8 -*-


import calendar
import datetime
import sys
import subprocess
import os
from pickle import dump
from tkinter import *
import tkinter as tk


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
        self.wid = []
        self.day_selected = 1
        self.month_selected = self.month
        self.year_selected = self.year
        self.day_name = ''

        self.setup(self.year, self.month)

    def clear(self):
        for w in self.wid[:]:
            w.grid_forget()
            #w.destroy()
            self.wid.remove(w)

    def go_prev(self):
        if self.month > 1:
            self.month -= 1
        else:
            self.month = 12
            self.year -= 1
        #self.selected = (self.month, self.year)
        self.clear()
        self.setup(self.year, self.month)

    def go_next(self):
        if self.month < 12:
            self.month += 1
        else:
            self.month = 1
            self.year += 1

        #self.selected = (self.month, self.year)
        self.clear()
        self.setup(self.year, self.month)

    def selection(self, day, name):
        self.day_selected = day
        self.month_selected = self.month
        self.year_selected = self.year
        self.day_name = name

        #data
        self.values['day_selected'] = day
        self.values['month_selected'] = self.month
        self.values['year_selected'] = self.year
        self.values['day_name'] = name
        self.values['month_name'] = calendar.month_name[self.month_selected]

        self.clear()
        self.setup(self.year, self.month)

    def setup(self, y, m):
        left = tk.Button(self.parent, text='<', bg='navy', fg='cyan', command=self.go_prev)
        self.wid.append(left)
        left.grid(row=0, column=1)

        header = tk.Label(self.parent, fg='white', bg='DodgerBlue2',
            height=2, text='{}   {}'.format(calendar.month_abbr[m], str(y)))
        self.wid.append(header)
        header.grid(row=0, column=2, columnspan=3)

        right = tk.Button(self.parent, text='>', bg='navy', fg='cyan', command=self.go_next)
        self.wid.append(right)
        right.grid(row=0, column=5)

        days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        for num, name in enumerate(days):
            t = tk.Label(self.parent, text=name[:3], fg='yellow', bg='navy')
            self.wid.append(t)
            t.grid(row=1, column=num)

        for w, week in enumerate(self.cal.monthdayscalendar(y, m), 2):
            for d, day in enumerate(week):
                if day:
                    #print(calendar.day_name[day])
                    b = tk.Button(self.parent, width=1, text=day,
                        fg='white', bg='navy',
                        command=lambda day=day:self.selection(day, calendar.day_name[(day-1) % 7]))
                    self.wid.append(b)
                    b.grid(row=w, column=d, rowspan=1, columnspan=1, padx=2, pady=2)

        sel = tk.Label(self.parent, height=2, text='{} {} {} {}'.format(
            self.day_name, calendar.month_name[self.month_selected],
            self.day_selected, self.year_selected), fg='white', bg='DodgerBlue2')
        self.wid.append(sel)
        sel.grid(row=8, column=0, columnspan=7)

        ok = tk.Button(self.parent, width=5, text='OK', fg='cyan', bg='navy',
            command=self.kill_and_save)
        self.wid.append(ok)
        ok.grid(row=9, column=2, columnspan=3, pady=10)

    def kill_and_save(self):
        self.parent.destroy()

if __name__=='__main__':

    class Control:
        def __init__(self, parent):
            self.parent = parent.title("Time-Track")
            self.parent = parent.configure(background='cyan')
            self.labelo = tk.Label(self.parent, text='Agenda',
                font='Times 18 bold', width=17, height=2, fg='cyan', bg='RoyalBlue4')

            with open('./newpatient/entryfile24.txt', 'r') as file_r:
                line_a = file_r.readline()

            self.data_time = StringVar()
            self.entryname = tk.Entry(self.parent, textvariable=self.data_time,
                font='Times 14', width=22, fg='RoyalBlue4', bg='pale turquoise', bd=2,
                justify=CENTER)
            self.data_time.set(line_a[:-1])

            self.choose_btn = tk.Button(self.parent, text="1 - Choice a date",
                font="Times 14", width=20, height=1, fg='white', bg='RoyalBlue3',
                activebackground='pale turquoise', command=self.popup)
            self.show_btn = tk.Button(self.parent, text='2 - Fix appointment',
                font="Times 14", width=20, height=1,fg='white', bg='RoyalBlue3',
                activebackground='pale turquoise', command=self.print_selected_date)
            self.buttAgenda = tk.Button(self.parent, text='Agenda', font="Times 14",
                width=20, height=1, fg='cyan', bg='RoyalBlue3', activebackground='pale turquoise',
                command=self.accessDate)
            self.buttLook = tk.Button(self.parent, text='To change rdv', font="Times 14",
                width=20, height=1, fg='cyan', bg='RoyalBlue3', activebackground='pale turquoise',
                command=self.accessLook)
            self.butQuit = tk.Button(self.parent, text='Quit', font="Times 14", width=20,
                height=1, fg='white', bg='RoyalBlue3', activebackground='pale turquoise',
                activeforeground='red', command=quit)
            self.labelo.grid()
            self.entryname.grid()
            self.choose_btn.grid()
            self.show_btn.grid()
            self.buttAgenda.grid()
            self.buttLook.grid()
            self.butQuit.grid()
            self.data = {}

        def popup(self):
            child = tk.Toplevel(bg='DodgerBlue2')
            cal = Calendar(child, self.data)

        def print_selected_date(self):
            """
                To write in binary into file
                patient_calendar.txt if it
                does not exist.
            """
            print(self.data)
            try:
                if os.path.getsize('./patient_agenda/events24/patient_calendar.txt'):
                    print("+ File 'patient_calendar.txt' exist !")
                    file = open('./patient_agenda/events24/patient_calendar.txt','wb')
                    dump(self.data, file)
                    file.close()
                    subprocess.run('./patient_agenda/events24/entrer_event1.py', check=True)
            except FileNotFoundError as file_creat:
                print("+ File not existing!")
                print(file_creat)
                print("+ File 'patient_calendar.txt' created !")
                file = open('./patient_agenda/events24/patient_calendar.txt','wb')
                dump(self.data, file)
                file.close()
                subprocess.run('./patient_agenda/events24/entrer_event1.py', check=True)

        def accessDate(self):
            try:
                subprocess.run('./patient_agenda/events24/doc_events/fix_agenda/read_file.py', check=True)
            except FileNotFoundError as note_agenda:
                print("+ Agenda not created !")
                print(note_agenda)

        def accessLook(self):
            try:
                subprocess.run('./patient_agenda/events24/doc_events/fix_agenda/main.py', check=True)
            except FileNotFoundError as note_change:
                print("+ Agenda not created !")
                print(note_change)

    root = tk.Tk()
    app = Control(root)
    root.mainloop()
