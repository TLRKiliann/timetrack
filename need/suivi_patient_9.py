#!/usr/bin/python3
# -*- coding: utf-8 -*-


import tkinter as tk
from tkinter import messagebox
import subprocess
import os


class ScrollCanvas(tk.Frame):
    def __init__(self, boss=None):
        tk.Frame.__init__(self, borderwidth=borderwidth, relief=relief)
        self.can = tk.Canvas(self, width=width, height=height, bd=bd, bg=bg,
            relief=relief)
        self.frame = tk.Frame(self.can)
        self.vsb = tk.Scrollbar(self, orient=tk.VERTICAL, command=self.can.yview)
        self.can.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(side=tk.RIGHT, fill=tk.Y)
        self.can.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.can.create_window((4, 4), window=self.frame, anchor=tk.NW,
            tags="self.frame")
        self.frame.bind("<Configure>", self.onFrameConfigure)

class MenuBar(tk.Frame):
    def __init__(self, boss=None):
        tk.Frame.__init__(self, borderwidth=5, bg='RoyalBlue3', padx=0)
        But2 = tk.Button(self, text ="Close", fg='white', bg='RoyalBlue3',
            relief=tk.GROOVE, activebackground='pale turquoise',
            command=boss.quit).pack(side=tk.LEFT, padx=3)

class Application(tk.Frame):
    def __init__(self, boss=None):
        tk.Frame.__init__(self)
        self.master.title('TIME-TRACK : Care')

        mBar = MenuBar(self)
        mBar.pack(side=tk.TOP, fill=tk.X, expand=True)

        # ScrollCanvas limite de la zone à parcourir avec la barre
        self.can = tk.Canvas(self, width=600, height=400, bg='DodgerBlue2')
        self.frame = tk.Frame(self.can)
        self.vsb = tk.Scrollbar(self, orient=tk.VERTICAL, command=self.can.yview)
        self.can.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(side=tk.RIGHT, fill=tk.Y)
        self.can.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.can.create_window((4,4), window=self.frame, anchor=tk.NW,
            tags="self.frame")
        # Insertion du texte
        self.can.create_text(300, 150, anchor=tk.CENTER, text="Care and Monitoring",
            font=('Times New Roman', 28), fill='white')
        self.can.create_text(590, 380, anchor=tk.NE, text="14 needs",
            font=('Times', 12), fill='white') 
        self.can.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        # Configuration de la Scrollbar sur le Frame
        self.frame.bind("<Configure>", self.onFrameConfigure)

        self.x2, self.y2 = 200, 250
        self.b2 = tk.Button(self.can, width=10, bd=3, font=16,
            bg='RoyalBlue3', fg='gold',
            activebackground='pale turquoise',
            highlightbackground='light sky blue',
            text="Add", command=self.lienDirect)
        self.fb2 = self.can.create_window(self.x2, self.y2, window=self.b2)

        self.x3, self.y3 = 400, 250
        self.b3 = tk.Button(self.can, width=10, bd=3, font=16,
            bg='RoyalBlue3', fg='gold',
            activebackground='pale turquoise',
            highlightbackground='light sky blue',
            text="Read", command=self.lectureFic)
        self.fb3 = self.can.create_window(self.x3, self.y3, window=self.b3)
        #self.can.pack(side=LEFT, fill=BOTH, expand=True)
        self.pack()

    # Méthode pour reconfigurer la scrollbar à chaque fois
    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.can.configure(scrollregion=self.can.bbox(tk.ALL))

    def lienDirect(self):
        """
        Add button check
        if files exist.
        """
        try:
            if os.path.getsize('./need/doc_suivi9/patient9_14b.txt'):
                print("[+] File '14 needs' exist (add)!")
                subprocess.run('./need/doc_suivi9/patient9_write.py', check=True)
        except FileNotFoundError as outmsg:
            print("[!] Sorry, file '14 needs' not exist !")
            print(outmsg)
            self.commentFileRecNeeds()

    def lectureFic(self):
        """
        Read button check
        if files exist.
        """
        try:
            if os.path.getsize('./need/doc_suivi9/patient9_14b.txt'):
                print("[+] File '14 needs' exist (read)!")
                subprocess.run('./need/doc_suivi9/patient9_read.py', check=True)
        except FileNotFoundError as outnote:
            print("[!] Sorry, file '14 needs' not exist !")
            print(outnote)
            self.commentFileRecNeeds()

    def commentFileRecNeeds(self):
        self.MsgBox1msg = tk.messagebox.showwarning("Warning", "File '14 needs' "
            "doesn't exist. Check options to '14 needs' before !")

if __name__=='__main__':
    root = tk.Tk()
    root.resizable(False, False)
    app = Application()
    app.mainloop()
