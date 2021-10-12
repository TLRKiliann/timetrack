#!/usr/bin/python3
# -*- coding: utf-8 -*-


from tkinter import *
from tkinter import messagebox
import os
import subprocess


# La ScrollBar en class! Préparation pour l'application.
class ScrollCanvas(Frame):
    def __init__(self, boss=None):
        Frame.__init__(self, borderwidth=borderwidth, relief=relief)
        self.can = Canvas(self, width=width, height=height, bd=bd, bg=bg,
            relief=relief)
        self.frame = Frame(self.can)

        self.vsb = Scrollbar(self, orient=VERTICAL, command=self.can.yview)
        self.can.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side=RIGHT, fill=Y)
        self.can.pack(side=LEFT, fill=BOTH, expand=YES)
        self.can.create_window((4,4), window=self.frame, anchor=NW, 
                                  tags="self.frame")
        self.frame.bind("<Configure>", self.onFrameConfigure)

# Class de la barre des menus
class MenuBar(Frame):
    """Barre menu déroulant"""
    def __init__(self, boss=None):
        Frame.__init__(self, borderwidth=5, bg='RoyalBlue3', padx=0)
        # Menu fichier
        But = Button(self, text ="Close", fg='cyan', bg='RoyalBlue3',
            activebackground='pale turquoise', command=boss.quit).pack(side=LEFT,
            padx=3)

# Application principale
class Application(Frame):
    def __init__(self, boss=None):
        Frame.__init__(self)
        self.master.title('Diagnosis')
        mBar = MenuBar(self)
        mBar.pack(side=TOP, fill=X, expand=1)
        # ScrollCanvas limite de la zone à parcourir avec la barre
        self.can = Canvas(self, width=600, height=400, bg='DodgerBlue2')
        self.frame = Frame(self.can)
        self.vsb = Scrollbar(self, orient=VERTICAL, command=self.can.yview)
        self.can.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(side=RIGHT, fill=Y)
        self.can.pack(side=LEFT, fill=BOTH, expand=YES)
        self.can.create_window((4,4), window=self.frame, anchor=NW, 
                                  tags="self.frame")
        # Insertion du texte
        self.can.create_text(300, 140, anchor=CENTER, text="Diagnostics and ATCD",
                    font=('Times New Roman', 28), fill='navy')
        self.can.create_text(590, 380, anchor=NE, text="Diagnosis + Update",
                    font=('Times', 12), fill='white') 
        self.can.pack(side=LEFT, fill=BOTH, expand=1)
        # Configuration de la Scrollbar sur le Frame
        self.frame.bind("<Configure>", self.onFrameConfigure)
        # Création des boutons
        self.x2, self.y2 = 200, 250
        self.b2 = Button(self.can, width=10, font=16, bg='RoyalBlue3', fg='gold',
            activebackground='pale turquoise', bd=3, 
            highlightbackground='light sky blue', 
            text="Add", command=self.Frame_Ap1)
        self.fb2 = self.can.create_window(self.x2, self.y2, window=self.b2)

        self.x3, self.y3 = 400, 250
        self.b3 = Button(self.can, width=10, font=16, bg='RoyalBlue3', fg='gold',
            activebackground='pale turquoise', bd=3, 
            highlightbackground='light sky blue', 
            text="Read", command=self.Frame_Ap2)
        self.fb3 = self.can.create_window(self.x3, self.y3, window=self.b3)
        self.pack()

    def onFrameConfigure(self, event):
        """
            Method for reconfiguring scrollbar at every time.
            Reset the scroll region to encompass the inner frame.
        """
        self.can.configure(scrollregion=self.can.bbox(ALL))

    def toDisplayError(self):
        """
            Explain trouble about files miss.
        """
        self.MsgBox2msg = messagebox.showwarning("Warning",
            "entryfile14.txt or diagrecap14.txt doesn't exist !")

    def addLine(self):
        """
            Indicate that one more line has been added.
        """
        self.MSGBOX = messagebox.showinfo("Info",
            "Main Diagnosis from entryfile14.txt (DB) has been added, "\
            "click a second time on add !")

    def lastLap(self):
        """
            If diagrecap.txt created, main diagnosis from
            entryfile14.txt is added.
        """
        try:
            if os.path.getsize('./newpatient/entryfile14.txt'):
                print("[+] File 'entryfile14.txt' exist (add_2)!")
                with open('./newpatient/entryfile14.txt', 'r') as file_diag:
                    line_a=file_diag.readline()
                    line_b=file_diag.readline()
                    line_c=file_diag.readline()
                    line_d=file_diag.readline()
                    line_e=file_diag.readline()
                with open("./diag/doc_diag14/diagrecap14.txt", "a+") as report_diag:
                    report_diag.write(line_e)
                print("[+] File diagrecap14.txt completed !")
                self.addLine()
        except FileNotFoundError as outdiag:
            print("[!] Sorry, file 'entryfile14.txt' doesn't exist !", outdiag)
            self.toDisplayError()

    def Frame_Ap1(self):
        """
            When you click on button "add":
            Verify if diagrecap.txt exist. If yes, a child process run.
            Else, diagrecap is created and title is written.
        """
        try:
            if os.path.getsize('./diag/doc_diag14/diagrecap14.txt'):
                print("[+] File diagrecap14.txt exist (add)!")
                subprocess.run('./diag/doc_diag14/diag_write.py', check=True)
        except FileNotFoundError as outmsg:
            print("[!] Sorry, file diagrecap14.txt doesn't exist (add)!", outmsg)
            print("[+] File diag.txt created (add)!")
            with open('./diag/doc_diag14/diagrecap14.txt', 'w') as file:
                file.write("--- DIAGNOSTICS ---\n")
            print("[+] File diagrecap14.txt created !")
            self.lastLap()

    def Frame_Ap2(self):
        """
            Verify if diagrecap.txt exist when you click on button "read".
        """
        try:
            if os.path.getsize('./diag/doc_diag14/diagrecap14.txt'):
                print("[+] File diagrecap14.txt exist (read)!")
                subprocess.run('./diag/doc_diag14/diag_read.py', check=True)
        except FileNotFoundError as outcom:
            print("[!] Sorry, file diagrecap14.txt doesn't exist (read)!", outcom)
            self.toDisplayError()
        
if __name__=='__main__':
    app = Application()
    app.mainloop()
