#!/usr/bin/python3
# -*- coding: utf-8 -*-


from tkinter import *
import tkinter as tk
from tkinter import messagebox
import os
import subprocess


# La ScrollBar en class! Préparation pour l'application.
class ScrollCanvas(tk.Frame):
    def __init__(self, boss=None):
        tk.Frame.__init__(self, borderwidth=borderwidth, relief=relief)
        self.can = tk.Canvas(self, width=width, height=height, bd=bd, bg=bg,
            relief=relief)
        self.frame = tk.Frame(self.can)

        self.vsb = tk.Scrollbar(self, orient=VERTICAL, command=self.can.yview)
        self.can.configure(yscrollcommand=self.vsb.set)
        
        self.vsb.pack(side=tk.RIGHT, fill=Y)
        self.can.pack(side=tk.LEFT, fill=BOTH, expand=YES)
        self.can.create_window((4, 4), window=self.frame, anchor=tk.NW,
            tags="self.frame")
        self.frame.bind("<Configure>", self.onFrameConfigure)

# Class de la barre des menus
class MenuBar(tk.Frame):
    """Barre menu déroulant"""
    def __init__(self, boss=None):
        tk.Frame.__init__(self, borderwidth=5, bg='RoyalBlue3', padx=0)
        But2 = tk.Button(self, text ="Close", fg='cyan', bg='RoyalBlue3',
            relief=GROOVE, activebackground='pale turquoise',
            command=boss.quit).pack(side=tk.LEFT, padx=3)

# Application principale
class Application(tk.Frame):
    def __init__(self, boss=None):
        tk.Frame.__init__(self)
        self.master.title('Medical Visit')
        mBar = MenuBar(self)
        mBar.pack(side=TOP, fill=X, expand=1)
        # ScrollCanvas limite de la zone à parcourir avec la barre
        self.can = tk.Canvas(self, width=600, height=400, bg='DodgerBlue2')
        self.frame = tk.Frame(self.can)
        self.vsb = tk.Scrollbar(self, orient=VERTICAL, command=self.can.yview)
        self.can.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(side=tk.RIGHT, fill=Y)
        self.can.pack(side=tk.LEFT, fill=BOTH, expand=YES)
        self.can.create_window((4,4), window=self.frame, anchor=tk.NW,
            tags="self.frame")
        # Insertion du texte
        self.can.create_text(300, 150, anchor=tk.CENTER,
            text="Medical Visit", font=('Times New Roman', 28),
            fill='aquamarine')
        self.can.create_text(590, 375, anchor=tk.NE, text="ko@l@tr33",
            font=('Times', 12), fill='white') 
        self.can.pack(side=tk.LEFT, fill=BOTH, expand=1)
        # Configuration de la Scrollbar sur le Frame
        self.frame.bind("<Configure>", self.onFrameConfigure)
        # Button to add
        self.x2, self.y2 = 200, 250
        self.b2 = tk.Button(self.can, width=10, font=16, bd=3,
            bg='RoyalBlue2', fg='white',
            activebackground='pale turquoise',
            highlightbackground='cyan',
            text="Add", command=self.lienDirect)
        self.fb2 = self.can.create_window(self.x2,
            self.y2, window=self.b2)
        # Button to read
        self.x3, self.y3 = 400, 250
        self.b3 = tk.Button(self.can, width=10, font=16, bd=3,
            bg='RoyalBlue2', fg='white',
            activebackground='pale turquoise',
            highlightbackground='cyan',
            text="Read", command=self.lectureFic)
        self.fb3 = self.can.create_window(self.x3,
            self.y3, window=self.b3)
        self.pack()

    # Method to reconfigure scrollbar everytime
    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.can.configure(scrollregion=self.can.bbox(ALL))

    def lienDirect(self):
        """
            To verify and write in VM file
        """
        try:
            if os.path.getsize('./vmed/doc_vmed12/resultvmed12.txt'):
                print("+ File 'VMED' exist (add)!")
                subprocess.run('./vmed/doc_vmed12/vmed_write.py', check=True)
        except FileNotFoundError as outmsg:
            print("+ Sorry, file 'VMED' not exist !", outmsg)
            print("+ File VMED created !!!")
            with open('./vmed/doc_vmed12/resultvmed12.txt', 'w') as file:
                file.write("--- MEDICAL VISIT ---\n")
            self.confRec()

    def lectureFic(self):
        """
            To verify and read diag file
        """
        try:
            if os.path.getsize('./vmed/doc_vmed12/resultvmed12.txt'):
                print("+ File 'VMED' exist (read)!")
                subprocess.run('./vmed/doc_vmed12/vmed_read.py', check=True)
        except FileNotFoundError as outcom:
            print("+ Sorry, file 'VMED' not exist !", outcom)
            self.confRec()

    def confRec(self):
        self.MsgBox2msg = messagebox.showinfo("Warning", "File 'VMED' "
            "was created, but no Medical Visit has been checked !")
        subprocess.run('./vmed/doc_vmed12/vmed_write.py', check=True)

if __name__=='__main__':
    app = Application()
    app.mainloop()
