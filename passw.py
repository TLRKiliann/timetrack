#!/usr/bin/python3
# -*- coding: utf-8 -*-


import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import subprocess
from playsound import playsound
#from tt_download import launchdownload


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
    playsound('./beep_sounds/ok_butt.wav')

def playError():
    playsound('./beep_sounds/metroid_alarm.wav')

def playButt():
    playsound('./beep_sounds/menu_ok.wav')

def closeWindow():
    """    
        Class call from
        heal_track.py !
    """
    window.destroy()
    #launchdownload()

def validentry():
    """
        To validate entree
        from user.
    """
    playButt()
    namenter = entryname.get()
    passentry = getpass.get()
    MSGBox = tk.messagebox.askyesno("Ask", "Validate password ?")
    if MSGBox == 1:
        if entryname.get() == "root" and getpass.get() == "root":
            playOne()
            tk.messagebox.showinfo("ACCESS", "Welcome ! You get access !!!")
            playTwo()
            closeWindow()
        elif entryname.get() == "koala" and getpass.get() == "tree":
            playOne()
            tk.messagebox.showinfo("ACCESS", "Welcome ! You get access !!!")
            playTwo()
            closeWindow()
        elif entryname.get() == "me" and getpass.get() == "me":
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

buttonvalidate = ttk.Button(window, text='Validate', command=validentry)
buttonvalidate.pack(pady=10)

window.mainloop()