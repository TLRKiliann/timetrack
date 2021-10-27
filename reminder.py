#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
    Verify if an alarm exist and display msgbox
    to advertise !
"""


import tkinter as tk
from tkinter import messagebox
import sys
import datetime
import time
import threading
from playsound import playsound


def alarmThread(self):
    """
        Function called from main app (./heal_track.py)
    """
    self.effacer()
    self.delScroll()
    # DodgerBlue2
    self.can.configure(bg='black')
    # fontalarmbg2.png 625, 350, 
    self.photo = tk.PhotoImage(file='./syno_gif/minipy3.png')
    self.item = self.can.create_image((0,0), image=self.photo, anchor=tk.NW)

    def action():
        """
            To start app with thread !
        """
        treat = threading.Thread(target=alarm, args=(1,))
        treat.setDaemon(True)
        time.sleep(2)
        treat.start()

    def alarm(n):
        """
            Alarm will sound at the scheduled time.
        """
        n = 1
        while n == 1 :
            set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
            time.sleep(1)

            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            print(current_time, set_alarm_time)

            if current_time == set_alarm_time:
                print("Alarm ring !")
                playsound("./beep_sounds/metroid_alarm.wav")
                MSGBOXA = tk.messagebox.showwarning("Alarm", "Remind : "\
                    + comment.get() + " !")
                n -= 1

    self.x10, self.y10 = 625, 100
    self.textLab = tk.Label(self.can, text="Alarm Clock",
        font=('serif', 28, 'bold'), fg='white', bg='black')
    self.textLab_window = self.can.create_window(self.x10, self.y10,
        window=self.textLab)

    self.x20, self.y20 = 625, 200
    self.textLab = tk.Label(self.can, text="Set Time",
        font=('serif', 22, 'bold'), fg='aquamarine', bg='black')
    self.textLab_window = self.can.create_window(self.x20, self.y20,
        window=self.textLab)

    self.x21, self.y21 = 625, 300
    self.textLab = tk.Label(self.can, text="Hours : Minutes : Seconds",
        font=('serif', 14, 'bold'), fg='white', bg='black')
    self.textLab_window = self.can.create_window(self.x21, self.y21,
        window=self.textLab)

    self.x30, self.y30 = 520, 350
    hour = tk.StringVar()
    self.entryhou = tk.Entry(self.can, textvariable=hour, width=6)
    hour.set(time.strftime("%H"))
    self.wentryhou_window = self.can.create_window(self.x30, self.y30,
        window=self.entryhou)

    self.x40, self.y40 = 620, 350
    minute = tk.StringVar()
    self.entrymin = tk.Entry(self.can, textvariable=minute, width=6)
    minute.set(time.strftime("%M"))
    self.wentrymin_window = self.can.create_window(self.x40, self.y40,
        window=self.entrymin)

    self.x50, self.y50 = 720, 350
    second = tk.StringVar()
    self.entrysec = tk.Entry(self.can, textvariable=second, width=6)
    second.set(time.strftime("%S"))
    self.wentrysec_window = self.can.create_window(self.x50, self.y50,
        window=self.entrysec)

    self.x51, self.y51 = 625, 420
    self.notifLab = tk.Label(self.can, text="Notifications :",
        font=('serif', 16, 'bold'), fg='white', bg='black')
    self.wnotifLab_window = self.can.create_window(self.x51, self.y51,
        window=self.notifLab)

    self.x52, self.y52 = 625, 470
    comment = tk.StringVar()
    self.entrycom = tk.Entry(self.can, textvariable=comment, width=30)
    comment.set('Write your comment here')
    self.wentrycom_window = self.can.create_window(self.x52, self.y52,
        window=self.entrycom)

    self.x60, self.y60 = 625, 550
    self.buttsave = tk.Button(self.can, text="Save", fg='white',
        bg='RoyalBlue2', bd=3, width=10, highlightbackground='black',
        activebackground='pale turquoise', command = action)
    self.wbuttsave_window = self.can.create_window(self.x60, self.y60,
        window=self.buttsave)

    self.photo2 = tk.PhotoImage(file='./syno_gif/minipy3.png')
    self.item2 = self.can.create_image((1250,0), image=self.photo2, anchor=tk.NE)

    self.can.configure(scrollregion=self.can.bbox(tk.ALL))
    self.can.unbind_all("<Button-4>")
    self.can.unbind_all("<Button-5>")
