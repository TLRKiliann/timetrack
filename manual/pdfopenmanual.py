#!/usr/bin/python3
# -*-encoding:Utf-8-*-


#from tkinter import *
import tkinter as tk
from tkinter import messagebox
import os
import subprocess
import platform


class ScrollCanvas(tk.Frame):
    '''ScrollBar Canvas preconfiguration '''
    def __init__(self, boss=None):
        tk.Frame.__init__(self, borderwidth=borderwidth, relief=relief)
        self.can = tk.Canvas(self, width=width, height=height, bd=bd, bg=bg,
            relief=relief)
        self.frame = tk.Frame(self.can)

        self.vsb = tk.Scrollbar(self, orient=tk.VERTICAL, command=can.yview)
        self.can.configure(yscrollcommand=vsb.set)

        self.vsb.pack(side=tk.RIGHT, fill=tk.Y)
        self.can.pack(side=tk.LEFT, fill='both', expand=True)
        self.can.create_window((4, 4), window=self.frame, anchor=tk.NW,
            tags="self.frame")
        self.frame.bind("<Configure>", self.onFrameConfigure)

class MenuBar(tk.Frame):
    '''Barre menu déroulant'''
    def __init__(self, boss=None):
        tk.Frame.__init__(self, borderwidth=5, bg='RoyalBlue3', padx=0)
        But2 = tk.Button(self, text ="Close", fg='cyan', bg='navy', relief=tk.GROOVE,
            activebackground='cyan', command=boss.quit).pack(side=tk.LEFT, padx=3)

class Manualmain(tk.Frame):
    '''Main app'''
    def __init__(self, boss=None):
        tk.Frame.__init__(self)
        self.master.title('PDF MANUALS')
        mBar = MenuBar(self)
        mBar.pack(side=tk.TOP, fill=tk.X, expand=1)
        # ScrollCanvas limite de la zone à parcourir avec la barre
        self.can = tk.Canvas(self, width=900, height=750, bg='DodgerBlue2')
        self.frame = tk.Frame(self.can)
        self.vsb = tk.Scrollbar(self, orient=tk.VERTICAL, command=self.can.yview)
        self.can.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(side=tk.RIGHT, fill=tk.Y)
        self.can.pack(side=tk.LEFT, fill='both', expand=True)
        self.can.create_window((4,4), window=self.frame, anchor=tk.NW,
            tags="self.frame")
        # Insertion du texte
        self.can.create_text(200, 65, anchor=tk.CENTER, text="PDF Manuals",
            font=('Times New Roman', 28), fill='yellow')

        self.can.create_text(200, 150, anchor='w', text="Monovettes",
            font=('Times New Roman', 18), fill='white')
        self.can.create_text(200, 200, anchor='w', text="Urines 1er jet",
            font=('Times New Roman', 18), fill='white')
        self.can.create_text(200, 250, anchor='w', text="Urines 2ème jet",
            font=('Times New Roman', 18), fill='white')
        self.can.create_text(200, 300, anchor='w', text="Urines/24h",
            font=('Times New Roman', 18), fill='white')
        self.can.create_text(200, 350, anchor='w', text="Baby urines",
            font=('Times New Roman', 18), fill='white')
        self.can.create_text(200, 400, anchor='w', text="Urine pic ovulaire",
            font=('Times New Roman', 18), fill='white')
        self.can.create_text(200, 450, anchor='w', text="Hemocultures",
            font=('Times New Roman', 18), fill='white')
        self.can.create_text(200, 500, anchor='w', text="Frottis",
            font=('Times New Roman', 18), fill='white')
        self.can.create_text(200, 550, anchor='w', text="Helicobacter pylori",
            font=('Times New Roman', 18), fill='white')
        self.can.create_text(200, 600, anchor='w', text="Expectoration",
            font=('Times New Roman', 18), fill='white')
        self.can.create_text(200, 650, anchor='w', text="Coprocultures",
            font=('Times New Roman', 18), fill='white')
        self.can.create_text(200, 700, anchor='w', text="Research oxyures",
            font=('Times New Roman', 18), fill='white')

        self.can.create_text(600, 65, anchor=tk.CENTER, text="Monitoring",
            font=('Times New Roman', 28), fill='yellow')

        self.can.create_text(600, 150, anchor='w', text="Etat Mental Général",
            font=('Times New Roman', 18), fill='white')
        self.can.create_text(600, 200, anchor='w', text="Echelle Anxiété",
            font=('Times New Roman', 18), fill='white')
        self.can.create_text(600, 250, anchor='w', text="Evaluation de l'Humeur",
            font=('Times New Roman', 18), fill='white')
        self.can.create_text(600, 300, anchor='w', text="Démence - Délirium",
            font=('Times New Roman', 18), fill='white')
        self.can.create_text(600, 350, anchor='w', text="Orientation (3 modes)",
            font=('Times New Roman', 18), fill='white')
        self.can.create_text(600, 400, anchor='w', text="Hallucinations Visuelles",
            font=('Times New Roman', 18), fill='white')
        self.can.create_text(600, 450, anchor='w', text="Hallucinations Auditives",
            font=('Times New Roman', 18), fill='white')
        self.can.create_text(600, 500, anchor='w', text="Id Suicidaires",
            font=('Times New Roman', 18), fill='white')
        self.can.create_text(600, 550, anchor='w', text="Auto-agressivité",
            font=('Times New Roman', 18), fill='white')
        self.can.create_text(600, 600, anchor='w', text="Hétéro-agressivité",
            font=('Times New Roman', 18), fill='white')
        self.can.create_text(600, 650, anchor='w', text="SNM, SSero, ",
            font=('Times New Roman', 18), fill='white')
        self.can.create_text(600, 700, anchor='w', text="Crise d'Epilepsie (obs.)",
            font=('Times New Roman', 18), fill='white')
        self.can.pack(side=tk.LEFT, fill='both', expand=1)

        # Configuration de la Scrollbar sur le Frame
        self.frame.bind("<Configure>", self.onFrameConfigure)

        # Button to read Diabetologia
        self.x2, self.y2 = 100, 150
        self.monobutt = tk.Button(self.can, width=10, bd=3, font=16, bg='RoyalBlue4', fg='gold',
            activebackground='pale turquoise', text="open",
            highlightbackground='DodgerBlue2', command=self.openMonov)
        self.fmonobutt_window=self.can.create_window(self.x2, self.y2, window=self.monobutt)
        self.pack()

        # Button2 to open2 Oncology
        self.x4, self.y4 = 100, 200
        self.urinaone = tk.Button(self.can, width=10, bd=3, font=16, bg='RoyalBlue4', fg='gold',
            activebackground='pale turquoise', text="open",
            highlightbackground='DodgerBlue2', command=self.openUrinalOne)
        self.furinaone_window=self.can.create_window(self.x4, self.y4, window=self.urinaone)
        self.pack()

        # Button3 to open3 Ophtalmology
        self.x6, self.y6 = 100, 250
        self.urinasec = tk.Button(self.can, width=10, bd=3, font=16, bg='RoyalBlue4', fg='gold',
            activebackground='pale turquoise', text="open",
            highlightbackground='DodgerBlue2', command=self.openUrinalSecond)
        self.furinasec_window=self.can.create_window(self.x6, self.y6, window=self.urinasec)
        self.pack()

        # Button4 to open4 Dentist
        self.x8, self.y8 = 100, 300
        self.openubutt = tk.Button(self.can, width=10, bd=3, font=16, bg='RoyalBlue4', fg='gold',
            activebackground='pale turquoise', text="open",
            highlightbackground='DodgerBlue2', command=self.openUrin24h)
        self.fopenubutt_window=self.can.create_window(self.x8, self.y8, window=self.openubutt)
        self.pack()

        # Button5 to open5 Stomatherapy
        self.x10, self.y10 = 100, 350
        self.babybutt = tk.Button(self.can, width=10, bd=3, font=16, bg='RoyalBlue4', fg='gold',
            activebackground='pale turquoise', text="open",
            highlightbackground='DodgerBlue2', command=self.openUrineBb)
        self.fbabybutt_window=self.can.create_window(self.x10, self.y10, window=self.babybutt)
        self.pack()

        # Button6 to open6 Aromatherapy
        self.x12, self.y12 = 100, 400
        self.buttpic = tk.Button(self.can, width=10, bd=3, font=16, bg='RoyalBlue4', fg='gold',
            activebackground='pale turquoise', text="open",
            highlightbackground='DodgerBlue2', command=self.openUrinPicOv)
        self.fbuttpic_window=self.can.create_window(self.x12, self.y12, window=self.buttpic)
        self.pack()

        # Button7 to open7 Physiotherapy
        self.x12, self.y12 = 100, 450
        self.butthemoc = tk.Button(self.can, width=10, bd=3, font=16, bg='RoyalBlue4', fg='gold',
            activebackground='pale turquoise', text="open",
            highlightbackground='DodgerBlue2', command=self.openHemoc)
        self.fbutthemoc_window=self.can.create_window(self.x12, self.y12, window=self.butthemoc)
        self.pack()

        # Button8 to open8 Ergotherapy
        self.x14, self.y14 = 100, 500
        self.buttfrott = tk.Button(self.can, width=10, bd=3, font=16, bg='RoyalBlue4', fg='gold',
            activebackground='pale turquoise', text="open",
            highlightbackground='DodgerBlue2', command=self.openFrottis)
        self.fbuttfrott_window=self.can.create_window(self.x14, self.y14, window=self.buttfrott)
        self.pack()

        # Button9 to open9 Podology
        self.x16, self.y16 = 100, 550
        self.butteli = tk.Button(self.can, width=10, bd=3, font=16, bg='RoyalBlue4', fg='gold',
            activebackground='pale turquoise', text="open",
            highlightbackground='DodgerBlue2', command=self.openHelico)
        self.fbutteli_window=self.can.create_window(self.x16, self.y16, window=self.butteli)
        self.pack()

        # Button9 to open9 Podology
        self.x17, self.y17 = 100, 600
        self.buttexpect = tk.Button(self.can, width=10, bd=3, font=16, bg='RoyalBlue4', fg='gold',
            activebackground='pale turquoise', text="open",
            highlightbackground='DodgerBlue2', command=self.openExpecto)
        self.fbuttexpect_window=self.can.create_window(self.x17, self.y17, window=self.buttexpect)
        self.pack()

        # Button9 to open9 Podology
        self.x18, self.y18 = 100, 650
        self.buttcup = tk.Button(self.can, width=10, bd=3, font=16, bg='RoyalBlue4', fg='gold',
            activebackground='pale turquoise', text="open",
            highlightbackground='DodgerBlue2', command=self.openCopro)
        self.fbuttcup_window=self.can.create_window(self.x18, self.y18, window=self.buttcup)
        self.pack()

        # Button9 to open9 Podology
        self.x19, self.y19 = 100, 700
        self.buttscotch = tk.Button(self.can, width=10, bd=3, font=16, bg='RoyalBlue4', fg='gold',
            activebackground='pale turquoise', text="open",
            highlightbackground='DodgerBlue2', command=self.openScotchTest)
        self.fbuttscotch_window=self.can.create_window(self.x19, self.y19, window=self.buttscotch)

        # Eva mental
        self.x20, self.y20 = 500, 150
        self.buttexam = tk.Button(self.can, width=10, bd=3, font=16, bg='RoyalBlue4', fg='gold',
            activebackground='pale turquoise', text="open",
            highlightbackground='DodgerBlue2', command=self.examental)
        self.fbuttexam_window=self.can.create_window(self.x20, self.y20, window=self.buttexam)
        self.pack()

        # Anxious scale
        self.x21, self.y21 = 500, 200
        self.buttanx = tk.Button(self.can, width=10, bd=3, font=16, bg='RoyalBlue4', fg='gold',
            activebackground='pale turquoise', text="open",
            highlightbackground='DodgerBlue2', command=self.anxious)
        self.fbuttanx_window=self.can.create_window(self.x21, self.y21, window=self.buttanx)
        self.pack()

        # Humeur
        self.x22, self.y22 = 500, 250
        self.butty = tk.Button(self.can, width=10, bd=3, font=16, bg='RoyalBlue4', fg='gold',
            activebackground='pale turquoise', text="open",
            highlightbackground='DodgerBlue2', command=self.thymia)
        self.fbutty_window=self.can.create_window(self.x22, self.y22, window=self.butty)
        self.pack()

        # Demence
        self.x23, self.y23 = 500, 300
        self.buttdem = tk.Button(self.can, width=10, bd=3, font=16, bg='RoyalBlue4', fg='gold',
            activebackground='pale turquoise', text="open",
            highlightbackground='DodgerBlue2', command=self.demence)
        self.fbuttdem_window=self.can.create_window(self.x23, self.y23, window=self.buttdem)
        self.pack()

        # Desorientation
        self.x24, self.y24 = 500, 350
        self.buttconf = tk.Button(self.can, width=10, bd=3, font=16, bg='RoyalBlue4', fg='gold',
            activebackground='pale turquoise', text="open",
            highlightbackground='DodgerBlue2', command=self.confusion)
        self.fbuttconf_window=self.can.create_window(self.x24, self.y24, window=self.buttconf)
        self.pack()

        # Visual hallucinations
        self.x25, self.y25 = 500, 400
        self.buttview = tk.Button(self.can, width=10, bd=3, font=16, bg='RoyalBlue4', fg='gold',
            activebackground='pale turquoise', text="open",
            highlightbackground='DodgerBlue2', command=self.visual)
        self.fbuttview_window=self.can.create_window(self.x25, self.y25, window=self.buttview)
        self.pack()

        # Hallu auditives
        self.x26, self.y26 = 500, 450
        self.buttaudit = tk.Button(self.can, width=10, bd=3, font=16, bg='RoyalBlue4', fg='gold',
            activebackground='pale turquoise', text="open",
            highlightbackground='DodgerBlue2', command=self.auditive)
        self.fbuttaudit_window=self.can.create_window(self.x26, self.y26, window=self.buttaudit)
        self.pack()

        # Suicide Idea
        self.x27, self.y27 = 500, 500
        self.buttsi = tk.Button(self.can, width=10, bd=3, font=16, bg='RoyalBlue4', fg='gold',
            activebackground='pale turquoise', text="open",
            highlightbackground='DodgerBlue2', command=self.suicid)
        self.fbuttsi_window=self.can.create_window(self.x27, self.y27, window=self.buttsi)
        self.pack()

        # Auto-agressif
        self.x28, self.y28 = 500, 550
        self.buttautoa = tk.Button(self.can, width=10, bd=3, font=16, bg='RoyalBlue4', fg='gold',
            activebackground='pale turquoise', text="open",
            highlightbackground='DodgerBlue2', command=self.autoagress)
        self.fbuttautoa=self.can.create_window(self.x28, self.y28, window=self.buttautoa)
        self.pack()

        # Hetero-agressif
        self.x29, self.y29 = 500, 600
        self.butthetero = tk.Button(self.can, width=10, bd=3, font=16, bg='RoyalBlue4', fg='gold',
            activebackground='pale turquoise', text="open",
            highlightbackground='DodgerBlue2', command=self.heteroagress)
        self.fbutthetero_window=self.can.create_window(self.x29, self.y29, window=self.butthetero)
        self.pack()

        # SNM
        self.x30, self.y30 = 500, 650
        self.buttsyn = tk.Button(self.can, width=10, bd=3, font=16, bg='RoyalBlue4', fg='gold',
            activebackground='pale turquoise', text="open",
            highlightbackground='DodgerBlue2', command=self.syndrome)
        self.fbuttsyn_window=self.can.create_window(self.x30, self.y30, window=self.buttsyn)
        self.pack()

        # Epilepsia seizure
        self.x31, self.y31 = 500, 700
        self.buttepi = tk.Button(self.can, width=10, bd=3, font=16, bg='RoyalBlue4', fg='gold',
            activebackground='pale turquoise', text="open",
            highlightbackground='DodgerBlue2', command=self.epilepsia)
        self.fbuttepi_window=self.can.create_window(self.x31, self.y31, window=self.buttepi)
        self.pack()

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.can.configure(scrollregion=self.can.bbox(ALL))

    def msgQuitapp(self, arg):
        """
            If usr want to quit, a question
            into a msgbox appear.
        """
        try:
            MsgBox = tk.messagebox.askyesno('Quit system', 'Do you want to quit ?')
            if MsgBox == 1:
                self.master.destroy()
        except OSError as err_exit:
            print("[!] Error 2 : time to quit !!!", err_exit)

    def openMonov(self):
        ''' Open monovet.pdf '''
        proc_mono = platform.system()
        print(proc_mono)        
        if proc_mono == 'Linux':
            if os.path.getsize('./manual/monovet.pdf'):
                print("[+] File 'monovet.pdf' exist (read)!")
                os.system('gio open "./manual/monovet.pdf"') # Linux
            else:
                raise Exception("[!] Sorry, file 'monovet.pdf' not found !")
        elif proc_mono =='Darwin':
            subprocess.call('open', './manual/monovet.pdf' ) # Mac
        else:
            os.startfile('./manual/monovet.pdf') # Windows

    def openUrinalOne(self):
        ''' Open premierjet.pdf '''
        proc_urione = platform.system()
        print(proc_urione)
        if proc_urione == 'Linux':
            if os.path.getsize('./manual/premierjet.pdf'):
                print("[+] File 'premierjet.pdf' exist (read)!")
                os.system('gio open "./manual/premierjet.pdf"') # Linux
            else:
                raise Exception("[!] Sorry, file 'premierjet.pdf' not found !")
        elif proc_urione =='Darwin':
            subprocess.call('open', './manual/premierjet.pdf' ) # Mac
        else:
            os.startfile('./manual/premierjet.pdf') # Windows

    def openUrinalSecond(self):
        ''' Open secondjet.pdf '''
        proc_urisec = platform.system()
        print(proc_urisec)
        if proc_urisec == 'Linux':
            if os.path.getsize('./manual/secondjet.pdf'):
                print("[+] File 'secondjet.pdf' exist (read)!")
                os.system('gio open "./manual/secondjet.pdf"') # Linux
            else:
                raise Exception("[!] Sorry, file 'secondjet.pdf' not found !")
        elif proc_urisec =='Darwin':
            subprocess.call('open', './manual/secondjet.pdf' ) # Mac
        else:
            os.startfile('./manual/secondjet.pdf') # Windows

    def openUrin24h(self):
        ''' Open urine24h.pdf '''
        proc_urinh = platform.system()
        print(proc_urinh)
        if proc_urinh == 'Linux':
            if os.path.getsize('./manual/urine24h.pdf'):
                print("[+] File 'urine24h.pdf' exist (read)!")
                os.system('gio open "./manual/urine24h.pdf"') # Linux
            else:
                raise Exception("[!] Sorry, file 'urine24h.pdf' not found !")
        elif proc_urinh =='Darwin':
            subprocess.call('open', './manual/urine24h.pdf' ) # Mac
        else:
            os.startfile('./manual/urine24h.pdf') # Windows

    def openUrineBb(self):
        ''' Open urinebaby.pdf '''
        proc_ubb = platform.system()
        print(platform.system())
        if proc_ubb == 'Linux':
            if os.path.getsize('./manual/urinebaby.pdf'):
                print("[+] File 'urinebaby.pdf' exist (read)!")
                os.system('gio open "./manual/urinebaby.pdf"') # Linux
            else:
                raise Exception("[!] Sorry, file 'urinebaby.pdf' not found !")
        elif proc_ubb =='Darwin':
            subprocess.call('open', './manual/urinebaby.pdf' ) # Mac
        else:
            os.startfile('./manual/urinebaby.pdf') # Windows

    def openUrinPicOv(self):
        ''' Open urinepicovulr.pdf '''
        proc_ou = platform.system()
        print(proc_ou)
        if proc_ou == 'Linux':
            if os.path.getsize('./manual/urinepicovulr.pdf'):
                print("[+] File 'urinepicovulr.pdf' exist (read)!")
                os.system('gio open "./manual/urinepicovulr.pdf"') # Linux
            else:
                raise Exception("[!] Sorry, file 'urinepicovulr.pdf' not found !")
        elif proc_ou =='Darwin':
            subprocess.call('open', './manual/urinepicovulr.pdf' ) # Mac
        else:
            os.startfile('./manual/urinepicovulr.pdf') # Windows

    def openHemoc(self):
        ''' Open hemoc.pdf '''
        proc_hemoc = platform.system()
        print(proc_hemoc)
        if proc_hemoc == 'Linux':
            if os.path.getsize('./manual/hemoc.pdf'):
                print("[+] File 'hemoc.pdf' exist (read)!")
                os.system('gio open "./manual/hemoc.pdf"') # Linux
            else:
                raise Exception("[!] Sorry, file 'hemoc.pdf' not found !")
        elif proc_hemoc =='Darwin':
            subprocess.call('open', './manual/hemoc.pdf' ) # Mac
        else:
            os.startfile('./manual/hemoc.pdf') # Windows

    def openFrottis(self):
        ''' Open frottis.pdf '''
        proc_frott = platform.system()
        print(proc_frott)
        if proc_frott == 'Linux':
            if os.path.getsize('./manual/frottis.pdf'):
                print("[+] File 'frottis.pdf' exist (read)!")
                os.system('gio open "./manual/frottis.pdf"') # Linux
            else:
                raise Exception("[!] Sorry, file 'frottis.pdf' not found !")
        elif proc_frott =='Darwin':
            subprocess.call('open', './manual/frottis.pdf' ) # Mac
        else:
            os.startfile('./manual/frottis.pdf') # Windows

    def openHelico(self):
        ''' Open helicobacter.pdf '''
        proc_helico = platform.system()
        print(proc_helico)
        if proc_helico == 'Linux':
            if os.path.getsize('./manual/helicobacter.pdf'):
                print("[+] File 'helicobacter.pdf' exist (read)!")
                os.system('gio open "./manual/helicobacter.pdf"') # Linux
            else:
                raise Exception("[!] Sorry, file 'helicobacter.pdf' not found !")
        elif proc_helico =='Darwin':
            subprocess.call('open', './manual/helicobacter.pdf' ) # Mac
        else:
            os.startfile('./manual/helicobacter.pdf') # Windows

    def openExpecto(self):
        ''' Open expecto.pdf '''
        proc_expect = platform.system()
        print(proc_expect)
        if proc_expect == 'Linux':
            if os.path.getsize('./manual/expecto.pdf'):
                print("[+] File 'expecto.pdf' exist (read)!")
                os.system('gio open "./manual/expecto.pdf"') # Linux
            else:
                raise Exception("[!] Sorry, file 'expecto.pdf' not found !")
        elif proc_expect =='Darwin':
            subprocess.call('open', './manual/expecto.pdf' ) # Mac
        else:
            os.startfile('./manual/expecto.pdf') # Windows

    def openCopro(self):
        ''' Open copro.pdf '''
        proc_cop = platform.system()
        print(proc_cop)
        if proc_cop == 'Linux':
            if os.path.getsize('./manual/copro.pdf'):
                print("[+] File 'copro.pdf' exist (read)!")
                os.system('gio open "./manual/copro.pdf"') # Linux
            else:
                raise Exception("[!] Sorry, file 'copro.pdf' not found !")
        elif proc_cop =='Darwin':
            subprocess.call('open', './manual/copro.pdf' ) # Mac
        else:
            os.startfile('./manual/copro.pdf') # Windows

    def openScotchTest(self):
        ''' Open scotchtest.pdf '''
        proc_scotch = platform.system()
        print(proc_scotch)
        if proc_scotch == 'Linux':
            if os.path.getsize('./manual/scotchtest.pdf'):
                print("[+] File 'scotchtest.pdf' exist (read)!")
                os.system('gio open "./manual/scotchtest.pdf"') # Linux
            else:
                raise Exception("[!] Sorry, file 'scotchtest.pdf' not found !")
        elif proc_scotch =='Darwin':
            subprocess.call('open', './manual/scotchtest.pdf' ) # Mac
        else:
            os.startfile('./manual/scotchtest.pdf') # Windows

    def examental(self):
        ''' Open examental.txt '''
        proc_extal = platform.system()
        print(proc_extal)
        if proc_extal == 'Linux':
            if os.path.exists('./manual/examental.txt'):
                print("[+] File 'examental.txt' exist (read)!")
                os.system('gio open "./manual/examental.txt"') # Linux
            else:
                raise Exception("[!] Sorry, file 'examental.txt' not found !")
        elif proc_extal =='Darwin':
            subprocess.call('open', './manual/examental.txt' ) # Mac
        else:
            os.startfile('./manual/examental.txt') # Windows

    def anxious(self):
        ''' Open anxious.txt '''
        proc_anx = platform.system()
        print(proc_anx)
        if proc_anx == 'Linux':
            if os.path.exists('./manual/anxious.txt'):
                print("[+] File 'anxious.txt' exist (read)!")
                os.system('gio open "./manual/anxious.txt"') # Linux
            else:
                raise Exception("[!] Sorry, file 'anxious.txt' not found !")
        elif proc_anx =='Darwin':
            subprocess.call('open', './manual/anxious.txt' ) # Mac
        else:
            os.startfile('./manual/anxious.txt') # Windows

    def thymia(self):
        ''' Open humeur.png '''
        proc_thym = platform.system()
        print(proc_thym)
        if proc_thym == 'Linux':
            if os.path.exists('./manual/humeur.png'):
                print("[+] File 'humeur.png' exist (read)!")
                os.system('gio open "./manual/humeur.png"') # Linux
            else:
                raise Exception("[!] Sorry, file 'humeur.png' not found !")
        elif proc_thym =='Darwin':
            subprocess.call('open', './manual/humeur.png' ) # Mac
        else:
            os.startfile('./manual/humeur.png') # Windows

    def demence(self):
        pass

    def confusion(self):
        ''' Open orientation.txt '''
        proc_conf = platform.system()
        print(proc_conf)
        if proc_conf == 'Linux':
            if os.path.exists('./manual/orientation.txt'):
                print("[+] File 'orientation.txt' exist (read)!")
                os.system('gio open "./manual/orientation.txt"') # Linux
            else:
                raise Exception("[!] Sorry, file 'orientation.txt' not found !")
        elif proc_conf =='Darwin':
            subprocess.call('open', './manual/orientation.txt' ) # Mac
        else:
            os.startfile('./manual/orientation.txt') # Windows

    def visual(self):
        ''' Open hallu_visual.txt '''
        proc_view = platform.system()
        print(proc_view)
        if proc_view == 'Linux':
            if os.path.exists('./manual/hallu_visual.txt'):
                print("[+] File 'hallu_visual.txt' exist (read)!")
                os.system('gio open "./manual/hallu_visual.txt"') # Linux
            else:
                raise Exception("[!] Sorry, file 'hallu_visual.txt' not found !")
        elif proc_view =='Darwin':
            subprocess.call('open', './manual/hallu_visual.txt' ) # Mac
        else:
            os.startfile('./manual/hallu_visual.txt') # Windows

    def auditive(self):
        '''Open hallu_audit.txt'''
        proc_audit = platform.system()
        print(proc_audit)
        if proc_audit == 'Linux':
            if os.path.exists('./manual/hallu_audit.txt'):
                print("[+] File 'hallu_audit.txt' exist (read)!")
                os.system('gio open "./manual/hallu_audit.txt"') # Linux
            else:
                raise Exception("[!] Sorry, file 'hallu_audit.txt' not found !")
        elif proc_audit =='Darwin':
            subprocess.call('open', './manual/hallu_audit.txt' ) # Mac
        else:
            os.startfile('./manual/hallu_audit.txt') # Windows

    def suicid(self):
        '''Open suicid.txt'''
        proc_is = platform.system()
        print(proc_is)
        if proc_is == 'Linux':
            if os.path.exists('./manual/suicid.txt'):
                print("[+] File 'suicid.txt' exist (read)!")
                os.system('gio open "./manual/suicid.txt"') # Linux
            else:
                raise Exception("[!] Sorry, file 'suicid.txt' not found !")
        elif proc_is =='Darwin':
            subprocess.call('open', './manual/suicid.txt' ) # Mac
        else:
            os.startfile('./manual/suicid.txt') # Windows

    def heteroagress(self):
        '''Open hetero_agress.txt'''
        proc_heteroa = platform.system()
        print(proc_heteroa)
        if proc_heteroa == 'Linux':
            if os.path.exists('./manual/hetero_agress.txt'):
                print("[+] File 'hetero_agress.txt' exist (read)!")
                os.system('gio open "./manual/hetero_agress.txt"') # Linux
            else:
                raise Exception("[!] Sorry, file 'hetero_agress.txt' not found !")
        elif proc_heteroa =='Darwin':
            subprocess.call('open', './manual/hetero_agress.txt' ) # Mac
        else:
            os.startfile('./manual/hetero_agress.txt') # Windows

    def autoagress(self):
        '''Open auto_agress.txt'''
        proc_autoa = platform.system()
        print(proc_autoa)
        if proc_autoa == 'Linux':
            if os.path.exists('./manual/auto_agress.txt'):
                print("[+] File 'auto_agress.txt' exist (read)!")
                os.system('gio open "./manual/auto_agress.txt"') # Linux
            else:
                raise Exception("[!] Sorry, file 'auto_agress.txt' not found !")
        elif proc_autoa =='Darwin':
            subprocess.call('open', './manual/auto_agress.txt' ) # Mac
        else:
            os.startfile('./manual/auto_agress.txt') # Windows

    def syndrome(self):
        pass

    def epilepsia(self):
        '''Open epilepsia.pdf'''
        proc_epi = platform.system()
        print(proc_epi)
        if proc_epi == 'Linux':
            if os.path.exists('./manual/epilepsia.pdf'):
                print("[+] File 'epilepsia.pdf' exist (read)!")
                os.system('gio open "./manual/epilepsia.pdf"') # Linux
            else:
                raise Exception("[!] Sorry, file 'epilepsia.pdf' not found !")
        elif proc_epi =='Darwin':
            subprocess.call('open', './manual/epilepsia.pdf' ) # Mac
        else:
            os.startfile('./manual/epilepsia.pdf') # Windows

if __name__=='__main__':
    root = tk.Tk()
    root.resizable(False, False)
    Manualmain(root).pack()
    root.mainloop()
