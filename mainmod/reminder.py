#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
    Verify if an alarm exist and display msgbox
    to advertise !
"""


import tkinter as tk
from tkinter import messagebox
import sys
import time
from playsound import playsound


def alarmThread(self):
    """
        Function called from main app (heal_track.py)
    """
    self.effacer()
    self.forgetVsb()

    self.can.configure(bg='black')
    self.photo = tk.PhotoImage(file='./syno_gif/2bf.png')
    self.item = self.can.create_image((0,0), image=self.photo, anchor=tk.NW)

    self.x10, self.y10 = 625, 120
    self.textLab = tk.Label(self.can, text="Alarm Clock",
        font=('serif', 28, 'bold'), fg='white', bg='black')
    self.textLab_window = self.can.create_window(self.x10, self.y10,
        window=self.textLab)

    self.x20, self.y20 = 625, 240
    self.textLab = tk.Label(self.can, text="Set Time",
        font=('serif', 22, 'bold'), fg='turquoise', bg='black')
    self.textLab_window = self.can.create_window(self.x20, self.y20,
        window=self.textLab)

    self.x21, self.y21 = 625, 300
    self.textLab = tk.Label(self.can, text="Hours : Minutes : Seconds",
        font=('serif', 14, 'bold'), fg='white', bg='black')
    self.textLab_window = self.can.create_window(self.x21, self.y21,
        window=self.textLab)

    self.x30, self.y30 = 520, 350
    self.hour = tk.StringVar()
    self.entryhou = tk.Entry(self.can, textvariable=self.hour, width=6)
    self.hour.set(time.strftime("%H"))
    self.wentryhou_window = self.can.create_window(self.x30, self.y30,
        window=self.entryhou)

    self.x40, self.y40 = 620, 350
    self.minute = tk.StringVar()
    self.entrymin = tk.Entry(self.can, textvariable=self.minute, width=6)
    self.minute.set(time.strftime("%M"))
    self.wentrymin_window = self.can.create_window(self.x40, self.y40,
        window=self.entrymin)

    self.x50, self.y50 = 720, 350
    self.second = tk.StringVar()
    self.entrysec = tk.Entry(self.can, textvariable=self.second, width=6)
    self.second.set(time.strftime("%S"))
    self.wentrysec_window = self.can.create_window(self.x50, self.y50,
        window=self.entrysec)

    self.x51, self.y51 = 625, 420
    self.notifLab = tk.Label(self.can, text="Notifications :",
        font=('serif', 16, 'bold'), fg='turquoise', bg='black')
    self.wnotifLab_window = self.can.create_window(self.x51, self.y51,
        window=self.notifLab)

    self.x52, self.y52 = 625, 470
    self.comment = tk.StringVar()
    self.entrycom = tk.Entry(self.can, textvariable=self.comment, width=30)
    self.comment.set('Write your comment here')
    self.wentrycom_window = self.can.create_window(self.x52, self.y52,
        window=self.entrycom)

    self.x60, self.y60 = 625, 550
    self.buttsave = tk.Button(self.can, text="Save", fg='white',
        bg='RoyalBlue3', bd=3, width=10, highlightbackground='black',
        activebackground='pale turquoise', command =lambda: self.alarm())
    self.wbuttsave_window = self.can.create_window(self.x60, self.y60,
        window=self.buttsave)

    self.photo2 = tk.PhotoImage(file='./syno_gif/9sf.png')
    self.item2 = self.can.create_image((1250,0), image=self.photo2, anchor=tk.NE)

    self.can.configure(scrollregion=self.can.bbox(tk.ALL))
    self.can.bind("<Button-1>", self.delScroll)
