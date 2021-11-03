#!/usr/bin/python3
# -*- coding: utf-8 -*-


import tkinter as tk
from tkinter import scrolledtext


def instalpy(self):
    """
        Explanation about skills
        and how to use app
    """
    self.effacer()
    self.delScroll()

    self.photo = tk.PhotoImage(file='./syno_gif/a2f.png')

    self.item = tk.Label(self.can, image=self.photo, bg='black')
    self.item.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    self.text_area = tk.scrolledtext.ScrolledText(self.can, fg='turquoise',
        highlightbackground='black', width=92, height=30, font=("Times New Roman", 14), bd=0)
    self.text_area.vbar.config(troughcolor='black', bg='turquoise')

    self.text_area.pack(side=tk.RIGHT, fill=tk.BOTH, expand=1)
    self.text_area.insert(tk.END,"\n\n"
        "                                             --- TUTORIAL ---\n"
        "\n [+] Usefull functionalities :\n"
        " ----------------------------------\n"
        " [*] Backup is scheduled every 5 days and each month for Vital Parameters and BMI\n"
        " [*] Display if a treatment or reserve ends the next day and print a stop into tabs\n"
        " [!] You need to write name of 'MEDICATION' to realy stop it [!]\n"
        " [*] Agenda is verified every day and a reminder appear to show you"\
        " if an appointment is fixed for tomorrow\n"
        " [*] A programmable alarm is available as long as the application remains open.\n\n"

        " How to use Time-Track :\n\n"
        " To launch app :\n"
        " > python3 heal_track.py\n\n"

        " [+] Enter a patient in the application : \n"
        " ----------------------------------------------\n"

        " [-->] Entry or Add patient (read below) --> Allergy --> Intolerance -->" \
        " 14 Needs --> Care and Monitoring :\n\n"

        " Use <New Entry> button to enter for first time new patient. Use <Add " \
        " patient> once time all patients were\n"
        " <Enter> ......... \n"
        " (button to replace a patient who's left with <Delete> button).\n"
        " Once time, patient had added use <Update> button to enter an allergy " \
        " if none, write 'none' and press enter !\n"
        " You can also use <Intolerance> in the Menu Bar to complete <Allergy>>.\n"
        " After it, <Care and Monitoring> is available only if you have entered one " \
        " or more needs of patient.\n\n"
        " [1] ---> Press <add patient> button.\n"
        " [2] ---> Write the number by which it will be classified in the database.\n"
        " [3] ---> Write data of patient and press <Enter>.\n"
        " [4] ---> Use <Refresh> button and look at if name has changed.\n\n"
        " Update for Allergia - Intolerance - Diagnosis :\n"
        " [5] ---> Use <Update> button to write allergia into DB\n"
        " [6] ---> Click on <Intolerance> (in menubar) and save data.\n\n"

        " To be verified :\n"
        " [-->] Click on <DataBase> for new entry and when it's empty.\n"
        " [-->] Click on <14 Needs>.\n"
        " [-->] Click on <Care and monitoring>.\n\n"

        " [+] Alarm :\n"
        "----------------\n"
        " [*] Set the alarm by entering a comment. It will work as long as the application\n"
        " remains open.\n\n"

        " [+] Agenda :\n"
        "----------------\n"
        " [1] Press <choose a date> date button and press <fix appointment> to follow step.\n"
        " [2] You have the possibility to fix an appointment after.\n"
        " [*] A reminder will show you one day before appointment.\n"
        " [*] You can change in everytime the clock or the data of appointment.\n"
        " [*] You can see all RDV with a reader.\n\n"

        " [+] 14 Needs :\n"
        "------------------\n"
        " [*] After having record all data about a patient you can click on the need.\n"
        " [*] The record is report to care and monitoring. You have to save it.\n\n"

        " [+] Care and monitoring retrieve all data from :\n"
        " --------------------------------------------------------\n"
        " [*] 14 Needs (V. Henderson)\n"
        " [*] Treatments (show Treatment(s) and Reserve(s) stopped).\n"
        " [*] Labo (Neuroleptic dosages on which the results can be added in care and monitoring).\n"
        " [*] Stix (which the results can be added in care and monitoring too).\n\n"

        " [+] Vital Parameters :\n"
        " -------------------------\n"
        " [*] The vp allows you to enter parameters such as blood pressure, pulse, respiratory rate, \n"
        " oxygen saturation, temperature, blood sugar, pain and to display them in the form of graphs.\n"
        " [*] The read button allows you to read the data in a file.\n"
        " [*] A text box is included in the frame for data insertion. It's nicer and especially the data\n"
        " may appear more easily.\n\n"

        " [+] Good point of view over all files :\n"
        " --------------------------------------------\n"
        " [*] Click on <Global> button and search file you're interested by.\n"
        " You can put all files you want in this folder, but it will not be uploaded to server.\n"
        " For that, it's better to upload it with scp command, such as : \n"
        " (with python3 command :)\n\n"
        " subprocess.run(['scp', './Backup/FilesX/yourfile.pdf',\n"
        "'pi@192.168.18.12:~/tt_doc/doc_txtX/FilesX/yourfile.pdf]', stderr=subprocess.PIPE)\n"
        " (or with shell command :)\n\n"
        " $ scp ./Backup/FilesX/yourfile.pdf pi@192.168.18.12:~/tt_doc/doc_txtX/FilesX/yourfile.pdf\n\n"

        " [*] Click on <EventBox> for seeing previously about yesterday news and backup will"\
        " be launched every 5 days. This interface is usefull to prevent if a rdv has been fixed for tomorrow.\n\n"

        " !!! WARNING !!! : Don't press <delete patient> button before informing your administrator, \n"
        " otherwise all files and data will be losted forever...\n"

        "\n Developped on Linux Xubuntu (xfce4) Voyager 18.04 by ko@l@tr33\n")

    self.text_area.configure(state ='disable', background="black")

    self.can.configure(scrollregion=self.can.bbox(tk.ALL))
