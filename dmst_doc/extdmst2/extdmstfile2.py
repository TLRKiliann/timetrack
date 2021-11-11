#!/usr/bin/python3
# -*- coding: utf-8 -*-


import tkinter as tk
from tkinter import messagebox
import os
import subprocess
import time
import shutil


def importationAdmin(self, fichier, encodage="Utf-8"):
    filecontact = open(fichier, 'r', encoding=encodage)
    content = filecontact.readlines()
    filecontact.close()
    for li in content:
        self.t6.insert(tk.END, li)

def importationDoc1(self, fichier, encodage="Utf-8"):
    filecontdoc = open(fichier, 'r', encoding=encodage)
    content = filecontdoc.readlines()
    filecontdoc.close()
    for li in content:
        self.t8.insert(tk.END, li)

def importationDoc2(self, fichier, encodage="Utf-8"):
    filedoc2 = open(fichier, 'r', encoding=encodage)
    content = filedoc2.readlines()
    filedoc2.close()
    for li in content:
        self.t9.insert(tk.END, li)

def importationDoc3(self, fichier, encodage="Utf-8"):
    filedoc3 = open(fichier, 'r', encoding=encodage)
    content = filedoc3.readlines()
    filedoc3.close()
    for li in content:
        self.t10.insert(tk.END, li)

def importationFam(self, fichier, encodage="Utf-8"):
    filedoc3 = open(fichier, 'r', encoding=encodage)
    content = filedoc3.readlines()
    filedoc3.close()
    for li in content:
        self.t12.insert(tk.END, li)

def importationHealOne(self, fichier, encodage="Utf-8"):
    filehcs = open(fichier, 'r', encoding=encodage)
    content = filehcs.readlines()
    filehcs.close()
    for li in content:
        self.t14.insert(tk.END, li)

def importationHealThree(self, fichier, encodage="Utf-8"):
    filehcs3 = open(fichier, 'r', encoding=encodage)
    content = filehcs3.readlines()
    filehcs3.close()
    for li in content:
        self.t16.insert(tk.END, li)

def importationFile2(self, fichier2, encodage="Utf-8"):
    file2 = open(fichier2, 'r', encoding=encodage)
    content=file2.readlines()
    file2.close()
    for li2 in content:
        self.t31.insert(tk.END, li2)

def importationParam(self, fichier, encodage="Utf-8"):
    fileparam = open(fichier, 'r', encoding=encodage)
    content = fileparam.readlines()
    fileparam.close()
    for li in content:
        self.t33.insert(tk.END, li)

def importationBmi(self, fichier, encodage="Utf-8"):
    filebmi = open(fichier, 'r', encoding=encodage)
    content = filebmi.readlines()
    filebmi.close()
    for li in content:
        self.t35.insert(tk.END, li)

def launchfunc(self):
    """
        To record data after warning !
    """
    try:
        if os.path.exists('./dmst_doc/doc_dmst2/rslt_dmst2.txt'):
            tk.messagebox.showwarning('Warning',
                '!!! Warning, saving new data will erased old file !!!')
            msgayn = tk.messagebox.askyesno('Look', 'Would you like to continue ?')
            if msgayn == 1:
                os.remove('./dmst_doc/doc_dmst2/rslt_dmst2.txt')
                print("!!! rslt_dmst2.txt removed !!!")
            else:
                tk.messagebox.showinfo("INFO", "Nothing has changed !")
    except FileNotFoundError as fnf_totry:
        print("[!] No rslt_dmst2.txt exist !", fnf_totry)
        tk.messagebox.showinfo("INFO", "Let's creat one ! ;)")

    try:
        with open('./dmst_doc/doc_dmst2/rslt_dmst2.txt', 'a+') as file:
            file.write("----------------------------------------------------------\n")
            file.write("Date : ")
            file.write(time.strftime("%d.%m.%Y") + '\n')
            file.write("Hour : ")
            file.write(time.strftime("%H:%M:%S") + '\n')
            file.write("Patient name : ")
            file.write(self.ent_name.get() + '\n')
            file.write("Birthday : ")
            file.write(self.nt_birth.get() + '\n')
            file.write("Allergy : ")
            file.write(self.allertxt.get() + '\n')
            file.write("Transmissible disease : ")
            file.write(self.transdis.get() + '\n')
            file.write("----------------------------------------------------------\n\n")
    except FileNotFoundError as nf_rsltdm:
        print("[!] File rslt_dmst2.txt not found !", nf_rsltdm)
    
    print("!!! rslt_dmst2 initialized !!!")

    try:
        with open('./diag/doc_diag2/diagrecap2.txt', 'r') as file_di:
            with open('./dmst_doc/doc_dmst2/rslt_dmst2.txt', '+a') as file_dm:
                diag_content = file_di.readlines()
                for li in diag_content:
                    file_dm.writelines(diag_content)
                    break
    except FileNotFoundError as diag_nf:
        print("[!] File diagrecap2.txt not found !", diag_nf)

    try:
        with open('./ttt/doc_ttt2/intro_ttt.txt', 'r') as file_ttt:
            with open('./dmst_doc/doc_dmst2/rslt_dmst2.txt', '+a') as file_dm:
                ttt_content = file_ttt.readlines()
                for li in ttt_content:
                    file_dm.writelines("\n--- Treatments ---\n")
                    file_dm.writelines(ttt_content)
                    break
    except FileNotFoundError as intro_nf:
        print("[!] File intro_ttt.txt not found !", intro_nf)

    try:
        with open('./ttt/doc_ttt2/intro_res.txt', 'r') as file_res:
            with open('./dmst_doc/doc_dmst2/rslt_dmst2.txt', '+a') as file_dm:
                res_content = file_res.readlines()
                for li in res_content:
                    file_dm.writelines("--- Reserves ---\n")
                    file_dm.writelines(res_content)
                    break
    except FileNotFoundError as res_nf:
        print("[!] File intro_res.txt not found !", res_nf)

    try:
        with open('./param/paramdata2.txt', 'r') as file_pa:
            with open('./dmst_doc/doc_dmst2/rslt_dmst2.txt', '+a') as file_dm:
                pa_content = file_pa.readlines()
                for li in pa_content:
                    file_dm.writelines("--- Vitals Parameters ---\n")
                    file_dm.writelines(pa_content)
                    break
    except FileNotFoundError as param_nf:
        print("[!] File paramdata2.txt not found !", param_nf)

    try:
        with open('./calBmi/bmi2.txt', 'r') as file_b:
            with open('./dmst_doc/doc_dmst2/rslt_dmst2.txt', '+a') as file_dm:
                bmi_content = file_b.readlines()
                for li in bmi_content:
                    file_dm.writelines("--- BMI ---\n")
                    file_dm.writelines(bmi_content)
                    break
    except FileNotFoundError as bmi_nf:
        print("[!] File bmi2.txt not found !", bmi_nf)

    try:
        with open('./contact/conpact2/finalfile1.txt', 'r') as file_contf1:
            with open('./dmst_doc/doc_dmst2/rslt_dmst2.txt', '+a') as file_dm:
                fcf1_content = file_contf1.readlines()
                for li in fcf1_content:
                    file_dm.writelines("\n--- Patient data ---\n")
                    file_dm.writelines(fcf1_content)
                    break
    except FileNotFoundError as ff1_nf:
        print("[!] File finalfile1.txt not found !", ff1_nf)

    try:
        with open('./contact/conpact2/finaldoc1.txt', 'r') as file_do1:
            with open('./dmst_doc/doc_dmst2/rslt_dmst2.txt', '+a') as file_dm:
                fcd1_content = file_do1.readlines()
                for li in fcd1_content:
                    file_dm.writelines("\n\n--- Docotor1 data ---\n")
                    file_dm.writelines(fcd1_content)
                    break
    except FileNotFoundError as fd1_nf:
        print("[!] File finaldoc1.txt not found !", fd1_nf)

    try:
        with open('./contact/conpact2/finaldoc2.txt', 'r') as file_do2:
            with open('./dmst_doc/doc_dmst2/rslt_dmst2.txt', '+a') as file_dm:
                fcd2_content = file_do2.readlines()
                for li in fcd2_content:
                    file_dm.writelines("\n\n--- Docotor2 data ---\n")
                    file_dm.writelines(fcd2_content)
                    break
    except FileNotFoundError as fd2_nf:
        print("[!] File finaldoc2.txt not found !", fd2_nf)

    try:
        with open('./contact/conpact2/finaldoc3.txt', 'r') as file_do3:
            with open('./dmst_doc/doc_dmst2/rslt_dmst2.txt', '+a') as file_dm:
                fcd3_content = file_do3.readlines()
                for li in fcd3_content:
                    file_dm.writelines("\n\n--- Docotor3 data ---\n")
                    file_dm.writelines(fcd3_content)
                    break
    except FileNotFoundError as fd3_nf:
        print("[!] File finaldoc3.txt not found !", fd3_nf)
    
    try:
        with open('./contact/conpact2/finalfam1.txt', 'r') as file_fam:
            with open('./dmst_doc/doc_dmst2/rslt_dmst2.txt', '+a') as file_dm:
                ff_content = file_fam.readlines()
                for li in ff_content:
                    file_dm.writelines("\n\n--- Family data ---\n")
                    file_dm.writelines(ff_content)
                    break
    except FileNotFoundError as ffam_nf:
        print("[!] File finalfam1.txt not found !", ffam_nf)

    try:
        with open('./contact/conpact2/finalhcs1.txt', 'r') as file_hcs1:
            with open('./dmst_doc/doc_dmst2/rslt_dmst2.txt', '+a') as file_dm:
                hcs1_content = file_hcs1.readlines()
                for li in hcs1_content:
                    file_dm.writelines("\n\n--- Home Care System1 ---\n")
                    file_dm.writelines(hcs1_content)
                    break
    except FileNotFoundError as hcs1_nf:
        print("[!] File finalhcs1.txt not found !", hcs1_nf)

    try:
        with open('./contact/conpact2/finalhcs2.txt', 'r') as file_hcs2:
            with open('./dmst_doc/doc_dmst2/rslt_dmst2.txt', '+a') as file_dm:
                hcs2_content = file_hcs2.readlines()
                for li in hcs2_content:
                    file_dm.writelines("\n\n--- Home Care System2 ---\n")
                    file_dm.writelines(hcs2_content)
                    break
    except FileNotFoundError as hcs2_nf:
        print("[!] File finalhcs2.txt not found !", hcs2_nf)

    try:
        with open('./contact/conpact2/finalhcs3.txt', 'r') as file_hcs3:
            with open('./dmst_doc/doc_dmst2/rslt_dmst2.txt', '+a') as file_dm:
                hcs3_content = file_hcs3.readlines()
                for li in hcs3_content:
                    file_dm.writelines("\n\n--- Home Care System3 ---\n")
                    file_dm.writelines(hcs3_content)
                    break
    except FileNotFoundError as hcs3_nf:
        print("[!] File finalhcs3.txt not found !", hcs3_nf)

    try:
        with open('./auxequip/doc_equip/auxiliary2.txt', 'r') as file_aux:
            with open('./dmst_doc/doc_dmst2/rslt_dmst2.txt', '+a') as file_dm:
                ox_equip = file_aux.readlines()
                for li in ox_equip:
                    file_dm.writelines("\n\n--- Auxiliary Equipement ---\n")
                    file_dm.writelines(ox_equip)
                    break
    except FileNotFoundError as aux_nf:
        print("[!] File auxiliary2.txt not found !", aux_nf)

    print(self.CheckVar1.get())
    if self.CheckVar1.get() == 1:
        with open('./dmst_doc/doc_dmst2/rslt_dmst2.txt', 'a+') as file1:
            file1.write("\n\n--- AGGIR grid : ---\n")
            file1.write("[+] Orientation = 1\n")
    elif self.CheckVar1.get() == 2:
        with open('./dmst_doc/doc_dmst2/rslt_dmst2.txt', 'a+') as file2:
            file2.write("\n\n--- AGGIR grid : ---\n")
            file2.write("[+] Orientation = 2\n")
    elif self.CheckVar1.get() == 3:
        with open('./dmst_doc/doc_dmst2/rslt_dmst2.txt', 'a+') as file3:
            file3.write("\n\n--- AGGIR grid : ---\n")
            file3.write("[+] Orientation = 3\n")
    elif self.CheckVar1.get() == 4:
        with open('./dmst_doc/doc_dmst2/rslt_dmst2.txt', 'a+') as file4:
            file4.write("\n\n--- AGGIR grid : ---\n")
            file4.write("[+] Orientation = 4\n")
    else:
        with open('./dmst_doc/doc_dmst2/rslt_dmst2.txt', 'a+') as file0:
            file0.write("\n\n--- AGGIR grid : ---\n")
            file0.write("[+] Orientation = 0\n")

    print(self.CheckVar2.get())
    if self.CheckVar2.get() == 1:
        with open('./dmst_doc/doc_dmst2/rslt_dmst2.txt', 'a+') as file1:
            file1.write("[+] Cohérence = 1\n")
    elif self.CheckVar2.get() == 2:
        with open('./dmst_doc/doc_dmst2/rslt_dmst2.txt', 'a+') as file2:
            file2.write("[+] Cohérence = 2\n")
    elif self.CheckVar2.get() == 3:
        with open('./dmst_doc/doc_dmst2/rslt_dmst2.txt', 'a+') as file3:
            file3.write("[+] Cohérence = 3\n")
    elif self.CheckVar2.get() == 4:
        with open('./dmst_doc/doc_dmst2/rslt_dmst2.txt', 'a+') as file4:
            file4.write("[+] Cohérence = 4\n")
    else:
        with open('./dmst_doc/doc_dmst2/rslt_dmst2.txt', 'a+') as file0:
            file0.write("[+] Cohérence = 0\n")

    print(self.CheckVar3.get())
    if self.CheckVar3.get() == 1:
        with open('./dmst_doc/doc_dmst2/rslt_dmst2.txt', 'a+') as file1:
            file1.write("[+] Toilette = 1\n")
    elif self.CheckVar3.get() == 2:
        with open('./dmst_doc/doc_dmst2/rslt_dmst2.txt', 'a+') as file2:
            file2.write("[+] Toilette = 2\n")
    elif self.CheckVar3.get() == 3:
        with open('./dmst_doc/doc_dmst2/rslt_dmst2.txt', 'a+') as file3:
            file3.write("[+] Toilette = 3\n")
    elif self.CheckVar3.get() == 4:
        with open('./dmst_doc/doc_dmst2/rslt_dmst2.txt', 'a+') as file4:
            file4.write("[+] Toilette = 4\n")
    else:
        with open('./dmst_doc/doc_dmst2/rslt_dmst2.txt', 'a+') as file0:
            file0.write("[+] Toilette = 0\n")

    print(self.CheckVar4.get())
    if self.CheckVar4.get() == 1:
        with open('./dmst_doc/doc_dmst2/rslt_dmst2.txt', 'a+') as file1:
            file1.write("[+] Habillage = 1\n")
    elif self.CheckVar4.get() == 2:
        with open('./dmst_doc/doc_dmst2/rslt_dmst2.txt', 'a+') as file2:
            file2.write("[+] Habillage = 2\n")
    elif self.CheckVar4.get() == 3:
        with open('./dmst_doc/doc_dmst2/rslt_dmst2.txt', 'a+') as file3:
            file3.write("[+] Habillage = 3\n")
    elif self.CheckVar4.get() == 4:
        with open('./dmst_doc/doc_dmst2/rslt_dmst2.txt', 'a+') as file4:
            file4.write("[+] Habillage = 4\n")
    else:
        with open('./dmst_doc/doc_dmst2/rslt_dmst2.txt', 'a+') as file0:
            file0.write("[+] Habillage = 0\n")

    print(self.CheckVar5.get())
    if self.CheckVar5.get() == 1:
        with open('./dmst_doc/doc_dmst2/rslt_dmst2.txt', 'a+') as file1:
            file1.write("[+] Alimentation = 1\n")
    elif self.CheckVar5.get() == 2:
        with open('./dmst_doc/doc_dmst2/rslt_dmst2.txt', 'a+') as file2:
            file2.write("[+] Alimentation = 2\n")
    elif self.CheckVar5.get() == 3:
        with open('./dmst_doc/doc_dmst2/rslt_dmst2.txt', 'a+') as file3:
            file3.write("[+] Alimentation = 3\n")
    elif self.CheckVar5.get() == 4:
        with open('./dmst_doc/doc_dmst2/rslt_dmst2.txt', 'a+') as file4:
            file4.write("[+] Alimentation = 4\n")
    else:
        with open('./dmst_doc/doc_dmst2/rslt_dmst2.txt', 'a+') as file0:
            file0.write("[+] Alimentation = 0\n")

    print(self.CheckVar6.get())
    if self.CheckVar6.get() == 1:
        with open('./dmst_doc/doc_dmst2/rslt_dmst2.txt', 'a+') as file1:
            file1.write("[+] Elimination = 1\n")
    elif self.CheckVar6.get() == 2:
        with open('./dmst_doc/doc_dmst2/rslt_dmst2.txt', 'a+') as file2:
            file2.write("[+] Elimination = 2\n")
    elif self.CheckVar6.get() == 3:
        with open('./dmst_doc/doc_dmst2/rslt_dmst2.txt', 'a+') as file3:
            file3.write("[+] Elimination = 3\n")
    elif self.CheckVar6.get() == 4:
        with open('./dmst_doc/doc_dmst2/rslt_dmst2.txt', 'a+') as file4:
            file4.write("[+] Elimination = 4\n")
    else:
        with open('./dmst_doc/doc_dmst2/rslt_dmst2.txt', 'a+') as file0:
            file0.write("[+] Elimination = 0\n")

    print(self.CheckVar7.get())
    if self.CheckVar7.get() == 1:
        with open('./dmst_doc/doc_dmst2/rslt_dmst2.txt', 'a+') as file1:
            file1.write("[+] Déplacement = 1\n")
    elif self.CheckVar7.get() == 2:
        with open('./dmst_doc/doc_dmst2/rslt_dmst2.txt', 'a+') as file2:
            file2.write("[+] Déplacement = 2\n")
    elif self.CheckVar7.get() == 3:
        with open('./dmst_doc/doc_dmst2/rslt_dmst2.txt', 'a+') as file3:
            file3.write("[+] Déplacement = 3\n")
    elif self.CheckVar7.get() == 4:
        with open('./dmst_doc/doc_dmst2/rslt_dmst2.txt', 'a+') as file4:
            file4.write("[+] Déplacement = 4\n")
    else:
        with open('./dmst_doc/doc_dmst2/rslt_dmst2.txt', 'a+') as file0:
            file0.write("[+] Déplacement = 0\n")

    print(self.CheckVar8.get())
    if self.CheckVar8.get() == 1:
        with open('./dmst_doc/doc_dmst2/rslt_dmst2.txt', 'a+') as file1:
            file1.write("[+] Communication = 1\n")
    elif self.CheckVar8.get() == 2:
        with open('./dmst_doc/doc_dmst2/rslt_dmst2.txt', 'a+') as file2:
            file2.write("[+] Communication = 2\n")
    elif self.CheckVar8.get() == 3:
        with open('./dmst_doc/doc_dmst2/rslt_dmst2.txt', 'a+') as file3:
            file3.write("[+] Communication = 3\n")
    elif self.CheckVar8.get() == 4:
        with open('./dmst_doc/doc_dmst2/rslt_dmst2.txt', 'a+') as file4:
            file4.write("[+] Communication = 4\n")
    else:
        with open('./dmst_doc/doc_dmst2/rslt_dmst2.txt', 'a+') as file0:
            file0.write("[+] Communication = 0\n")

    print(self.CheckVar9.get())
    if self.CheckVar9.get() == 1:
        with open('./dmst_doc/doc_dmst2/rslt_dmst2.txt', 'a+') as file1:
            file1.write("\n[+] PLAFA = Oui\n")
    else:
        print("[!] None (PLAFA)")

    print(self.CheckVar10.get())
    if self.CheckVar10.get() == 1:
        with open('./dmst_doc/doc_dmst2/rslt_dmst2.txt', 'a+') as file1:
            file1.write("\n[+] PLAFA = Non\n")
    else:
        print("[!] None (PLAFA)")

    print(self.CheckVar11.get())
    if self.CheckVar11.get() == 1:
        with open('./dmst_doc/doc_dmst2/rslt_dmst2.txt', 'a+') as file1:
            file1.write("[+] Directives anticipées = Oui\n\n")
    else:
        print("[!] None (Directives anticipées)")

    print(self.CheckVar12.get())
    if self.CheckVar12.get() == 1:
        with open('./dmst_doc/doc_dmst2/rslt_dmst2.txt', 'a+') as file1:
            file1.write("[+] Directives anticipées = Non\n\n")
    else:
        print("[!] None (Directives anticipées)")

    try:
        with open('./dmst_doc/doc_dmst2/parcours.txt', 'r') as ftor:
            with open('./dmst_doc/doc_dmst2/rslt_dmst2.txt', 'a+') as ftocp:
                lines = ftor.readlines()
                for li in lines:
                    ftocp.writelines("\nParcours :\n")
                    ftocp.writelines(lines)
                    break
    except FileNotFoundError as err_parc:
        print("! File not found !", err_parc)

    try:
        with open('./dmst_doc/doc_dmst2/pbm.txt', 'r') as fpbmtor:
            with open('./dmst_doc/doc_dmst2/rslt_dmst2.txt', 'a+') as fthreecp:
                lines = fpbmtor.readlines()
                for li in lines:
                    fthreecp.writelines("Problématique :\n")
                    fthreecp.writelines(lines)
                    break
    except FileNotFoundError as err_pbm:
        print("! File not found !", err_pbm)

    try:
        with open('./dmst_doc/doc_dmst2/project.txt', 'r') as fprojcp:
            with open('./dmst_doc/doc_dmst2/rslt_dmst2.txt', 'a+') as fortocp:
                lines = fprojcp.readlines()
                for li in lines:
                    fortocp.writelines("Projet :\n")
                    fortocp.writelines(lines)
                    break
    except FileNotFoundError as err_proj:
        print("[!] File project.txt not found !", err_proj)

def saveData(self):
    """
        Test if file parcours.txt exist and write data.
        A msg into textbox appear to informate user that
        data have been saved.
    """
    try:
        if os.path.getsize('./dmst_doc/doc_dmst2/parcours.txt'):
            print("[+] File 'parcours.txt' exist !")
            with open('./dmst_doc/doc_dmst2/parcours.txt', 'w') as parc_file:
                parc_file.write(self.t100.get("0.0", "end-1c") + '\n\n')
    except FileNotFoundError as err_parc:
        print("[!] Sorry, file 'parcours.txt' not exist !", err_parc)
        print("[+] File 'parcours.txt' created !")
        with open('./dmst_doc/doc_dmst2/parcours.txt', 'a+') as noparc_file:
            noparc_file.write(self.t100.get("0.0", "end-1c") + '\n\n')
    self.t100.insert(tk.INSERT, "\n---Data saved !---")

    try:
        if os.path.getsize('./dmst_doc/doc_dmst2/pbm.txt'):
            print("[+] File 'pbm.txt' exist !")
            with open('./dmst_doc/doc_dmst2/pbm.txt', 'w') as pbmfile:
                pbmfile.write(self.t102.get("0.0", "end-1c") + '\n\n')
    except FileNotFoundError as err_pbm:
        print("[!] Sorry, file 'pbm.txt' not exist !", err_pbm)
        print("[+] File 'pbm.txt' created !")
        with open('./dmst_doc/doc_dmst2/pbm.txt', 'a+') as no_pbmfile:
            no_pbmfile.write(self.t102.get("0.0", "end-1c") + '\n\n')
    self.t102.insert(tk.INSERT, "\n---Data saved !---")

    try:
        if os.path.getsize('./dmst_doc/doc_dmst2/project.txt'):
            print("[+] File 'project.txt' exist !")
            with open('./dmst_doc/doc_dmst2/project.txt', 'w') as projectfile:
                projectfile.write(self.t104.get("0.0", "end-1c") + '\n\n')
    except FileNotFoundError as err_proj:
        print("[!] Sorry, file 'project.txt' not exist !", err_proj)
        print("[+] File 'project.txt' created !")
        with open('./dmst_doc/doc_dmst2/project.txt', 'a+') as no_projectfile:
            no_projectfile.write(self.t104.get("0.0", "end-1c") + '\n\n')
    self.t104.insert(tk.INSERT, "\n---Data saved !---")

def copytobackup():
    """
        To copy file below to ./Backup/Files2
    """
    try:
        if os.path.exists('./dmst_doc/doc_dmst2/parcours.txt'):
            shutil.copy('./dmst_doc/doc_dmst2/parcours.txt',
                './Backup/Files2/parcours.txt')
            print("[+] File --> parcours.txt copied into ./Backup/Files2")
    except FileNotFoundError as nf_parco:
        print("Not found", nf_parco)

    try:
        if os.path.exists('./dmst_doc/doc_dmst2/pbm.txt'):
            shutil.copy('./dmst_doc/doc_dmst2/pbm.txt',
                './Backup/Files2/pbm.txt')
            print("[+] File --> pbm.txt copied into ./Backup/Files2")
    except FileNotFoundError as nf_prob:
        print("Not found", nf_prob)

    try:
        if os.path.exists('./dmst_doc/doc_dmst2/project.txt'):
            shutil.copy('./dmst_doc/doc_dmst2/project.txt',
                './Backup/Files2/project.txt')
            print("[+] File --> project.txt copied into ./Backup/Files2")
    except FileNotFoundError as nf_projex:
        print("Not found", nf_projex)

    try:
        if os.path.exists('./dmst_doc/doc_dmst2/rslt_dmst2.txt'):
            shutil.copy('./dmst_doc/doc_dmst2/rslt_dmst2.txt',
                './Backup/Files2/rslt_dmst2.txt')
            print("[+] File --> rslt_dmst2.txt copied into ./Backup/Files2")
    except FileNotFoundError as nf_rltd:
        print("Not found", nf_rltd)

def uptoserv():
    """
        To upload data on server after creating files.
    """
    proc = subprocess.run(["scp", "./dmst_doc/doc_dmst2/rslt_dmst2.txt",
        "pi@192.168.18.12:~/tt_doc/doc_txt2/dmst2/rslt_dmst2.txt"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[Upload] File rslt_dmst2.txt uploaded !")
        #tk.messagebox.showinfo("INFO", "rslt_dmst2.txt uploaded...")
    else:
        print("[!] No file to upload !")
        tk.messagebox.showerror("Error", "No rslt_dmst2.txt to upload...")

    secproc = subprocess.run(["scp", "./dmst_doc/doc_dmst2/parcours.txt",
        "pi@192.168.18.12:~/tt_doc/doc_txt2/dmst2/parcours.txt"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("[Upload] File parcours.txt uploaded !")
        #tk.messagebox.showinfo("INFO", "parcours.txt uploaded...")
    else:
        print("[!] No file to upload !")
        tk.messagebox.showerror("Error", "No parcours.txt to upload...")

    thirdproc = subprocess.run(["scp", "./dmst_doc/doc_dmst2/pbm.txt",
        "pi@192.168.18.12:~/tt_doc/doc_txt2/dmst2/pbm.txt"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(thirdproc.stderr))
    if thirdproc.stderr == b'':
        print("[Upload] File pbm.txt uploaded !")
        #tk.messagebox.showinfo("INFO", "pbm.txt uploaded...")
    else:
        print("[!] No file to upload !")
        tk.messagebox.showerror("Error", "No pbm.txt to upload...")

    forthproc = subprocess.run(["scp", "./dmst_doc/doc_dmst2/project.txt",
        "pi@192.168.18.12:~/tt_doc/doc_txt2/dmst2/project.txt"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(forthproc.stderr))
    if forthproc.stderr == b'':
        print("[Upload] File project.txt uploaded !")
        #tk.messagebox.showinfo("INFO", "project.txt uploaded...")
    else:
        print("[!] No file to upload !")
        tk.messagebox.showerror("Error", "No project.txt to upload...")

    fivth = subprocess.run(["scp", "./need/doc_suivi2/main_14b.txt",
        "pi@192.168.18.12:~/tt_doc/doc_txt2/dmst2/main_14b.txt"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(fivth.stderr))
    if fivth.stderr == b'':
        print("[Upload] File main_14b.txt uploaded !")
        #tk.messagebox.showinfo("INFO", "main_14b.txt uploaded...")
    else:
        print("[!] No file to upload !")
        tk.messagebox.showerror("Error", "No main_14b.txt to upload...")
