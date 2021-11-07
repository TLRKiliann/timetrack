#!/usr/bin/python3
# -*- coding: utf-8 -*-


import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import subprocess
import threading
import time
from playsound import playsound
from tt_download import launchDownload
from cpfoldtrans import loaderfile


window = tk.Tk()
window.style = ttk.Style()
window.style.configure('TButton', font=('Helvetica', 11),
    foreground='yellow', background='navy')
window.title('ACCESS')
window.configure(bg='RoyalBlue3')
window.resizable(False, False)

def hangonwin():
    """
        For security
        this function
        prevent to close
        window by x button
    """
    window.update()

window.protocol('WM_DELETE_WINDOW', hangonwin)

def playOne():
    playsound('./beep_sounds/c4_plant2.wav')

def playTwo():
    playsound('./beep_sounds/loop79.mp3')
    #playsound('./beep_sounds/sound101.wav')

def playError():
    playsound('./beep_sounds/metroid_alarm.wav')

def playButt():
    playsound('./beep_sounds/menu_ok.wav')

def playNieR():
    playsound('./beep_sounds/NieR_sound.wav')

def closeWindow():
    """
        Class call from
        heal_track.py !
    """
    window.destroy()

    def muse():
        """
            Video intro of NieR:Automata
        """
        playsound("./syno_gif/9s_prog.mp4")
    t1 = threading.Thread(target=muse)
    t1.start()

    def down():
        """
            Download all files.
        """
        launchDownload()
    down()

    def tocopyfiles():
        """
            Load 24 folders when app start.
        """
        #time.sleep(2)
        loaderfile()
    tocopyfiles()

    def pod():
        playsound("./syno_gif/pod_font.mp3")
    t2 = threading.Thread(target=pod)
    t2.start()

def validentry(event):
    """
        To validate entree
        from user.
    """
    playButt()
    namenter = entryname.get()
    passentry = getpass.get()
    MSGBOX = tk.messagebox.askyesno("Ask", "Validate password ?")
    if MSGBOX == 1:
        with open('./filenter.txt', 'r') as read_file:
            line1 = read_file.readline()
            line2 = read_file.readline()
            line3 = read_file.readline()
            line4 = read_file.readline()
            line5 = read_file.readline()
            line6 = read_file.readline()
            line7 = read_file.readline()
            line8 = read_file.readline()
            if entryname.get() == line1[:-1] and getpass.get() == line2[:-1]:
                playOne()
                tk.messagebox.showinfo("ACCESS", "Welcome ! You get access !!!")
                playTwo()
                closeWindow()
            elif entryname.get() == line3[:-1] and getpass.get() == line4[:-1]:
                playOne()
                tk.messagebox.showinfo("ACCESS", "Welcome ! You get access !!!")
                playTwo()
                closeWindow()
            elif entryname.get() == line5[:-1] and getpass.get() == line6[:-1]:
                playOne()
                tk.messagebox.showinfo("ACCESS", "Welcome ! You get access !!!")
                playTwo()
                closeWindow()
            elif entryname.get() == line7[:-1] and getpass.get() == line8[:-1]:
                playOne()
                tk.messagebox.showinfo("ACCESS", "Welcome ! You get access !!!")
                playTwo()
                closeWindow()
            else:
                playError()
                tk.messagebox.showwarning("Warning", "Password or Username failed !")
                playTwo()
    else:
        playsound('./beep_sounds/flute_error.wav')

labelname = ttk.Label(window, text='Enter username :',
    font=('Times New Roman', 14, 'bold'),
    foreground="white", background="RoyalBlue3")
labelname.pack(pady=10)

entryname = tk.StringVar()
namenter = ttk.Entry(window, textvariable=entryname)
namenter.focus()
namenter.pack(padx=10)

labelpass = ttk.Label(window, text='Enter password :',
    font=('Times New Roman', 14, 'bold'),
    foreground="white", background="RoyalBlue3")
labelpass.pack(pady=10)

getpass = tk.StringVar()
passentry = ttk.Entry(window, textvariable=getpass, show='*')
passentry.pack(padx=10)

window.bind('<Return>', validentry)
buttonvalidate = ttk.Button(window, text='Enter')
buttonvalidate.pack(pady=10)

window.mainloop()
