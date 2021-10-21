#!/usr/bin/python3
# -*- coding: utf-8 -*-


import tkinter as tk


def instalpy(self):
    """
        Explanation about skills
        and how to use app
    """
    self.can.delete(tk.ALL)
    self.can.configure(background='black')

    self.photo = tk.PhotoImage(file='./syno_gif/minipy3.png')
    self.item = self.can.create_image((0,0), image=self.photo, anchor=tk.NW)

    self.can.create_text((400,20), anchor=tk.NW,
    text=" - MAPAPP -\n\n"

        " Usefull functionalities :\n"
        " ----------------------------\n"
        " ---> Backup is scheduled every 5 days and each month for Vital Parameters and BMI\n"
        " ---> Display if a treatment or reserve ends the next day and print a stop into tabs\n"
        " You need to write name of 'Treatment' to realy stop it !\n"
        " ---> Agenda is verified every day and a reminder appear to show you" \
        " if an appointment is fixed for tomorrow\n\n"

        " How to use heal-track :\n\n"
        " To launch app :\n"
        " > python3 heal_track.py\n\n"

        " To make a patient entry : \n"

        " Entry or Add patient (read below) ---> Allergy + Intolerance --->" \
        " 14 Needs ---> Care and Monitoring :\n"
        " -----------------------------------------------------------------"
        " ---------------------------------------------------------\n"
        " Use 'Entry' button to enter for first time new patient. Use 'Add " \
        " patient' once time all patients were enter \n"
        " (button to replace a patient who's left with delete button).\n"
        " Once time, patient had added use 'Update' button to enter an allergy " \
        " if none, write 'none' and press enter !\n"
        " You can also use 'Intolerance' in the Menu Bar to complete 'allergy'.\n"
        " After it, Care and Monitoring is available only if you have entered one " \
        " or more needs of patient.\n\n"
        " 1 ---> Press <add patient> button.\n"
        " 2 ---> Write the number by which it will be classified in the database.\n"
        " 2 ---> Write data of patient and press <Enter>.\n"
        " 3 ---> Use <Refresh> button and look at if name has changed.\n\n"
        " Update for Allergia - Intolerance - Diagnosis :\n"
        " 4 ---> Use <Update> button to write allergia into DB\n"
        " 5 ---> Click on <Intolerance All> (in menubar) and save data.\n\n"
        "\nA revoir le fonctionnement !!!\n\n"
        " To verify :\n"
        " * ---> Click on <DataBase>.\n"
        " * ---> Click on <14 Needs>.\n"
        " * ---> Click on <Care and monitoring>.\n\n"

        " Care and monitoring retrieve all data from :\n"
        " ----------------------------------------------------\n"
        " + 14 Needs (V. Henderson)\n"
        " + Treatments (show Treatment(s) and Reserve(s) stopped).\n"
        " + Labo (Neuroleptic dosages on which the results can be added in care and monitoring).\n"
        " + Stix (which the results can be added in care and monitoring too).\n\n"

        " Good point of view over all files :\n"
        " ----------------------------------------\n"
        " + Click on 'Global' button and search file you're interested by.\n"
        " You can put all files you want in this folder, but it will not be uploaded to server.\n"
        " For that it's better to upload it with scp command, such as : \n"
        " (with python3 command :)\n"
        " subprocess.run(['scp', './Backup/FilesX/yourfile.xyz', 'pi@192.168.18.12:~/tt_doc/doc_txtX/FilesX/yourfile.xyz]',\n"
        " stderr=subprocess.PIPE)\n"
        " (or with shell command :)\n"
        " $ scp ./Backup/FilesX/yourfile.xyz pi@192.168.18.12:~/tt_doc/doc_txtX/FilesX/yourfile.xyz\n"

        " + Click on 'EventBox' for seeing previously about yesterday news and backup will"\
        " be launched every 5 days.\n"

        "\n !!! WARNING !!! : Don't press 'delete patient' before informing administrator, \n"\
        " otherwise all files and data will be losted...\n"

        "\n Developped on Linux Xubuntu (xfce4) Voyager 18.04 by ko@l@tr33\n",
        font=('Times New Roman', 14), fill='aquamarine')

    self.can.configure(scrollregion=self.can.bbox(tk.ALL))
    self.can.bind_all("<Button-4>", self.onMouseWheel)
    self.can.bind_all("<Button-5>", self.onMouseWheel)
