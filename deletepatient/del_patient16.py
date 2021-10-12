#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
    To delete all files for patient 16
    when usr delete patient by pressing
    the delete button.
"""


from tkinter import *
from tkinter import messagebox
import os
import subprocess
import shutil


def delFuncFile16():
    """
        This function delete all files with
        a test before removing files.
    """
    backproc = subprocess.run(["scp", "-r", "-C", "./Backup/Files16",
        "pi@192.168.18.12:~/tt_doc/doc_txt16/Backup16"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(backproc.stderr))
    if backproc.stderr == b'':
        print("[Backup] Backup16 done on server !")
        messagebox.showinfo("INFO", "Backup16 done on server !")
    else:
        print("[!] No Backup16 done on server [!]")
        messagebox.showerror("Error", "!!! No Backup16 done on server !!!")

    delproc = subprocess.run(["ssh",
        "pi@192.168.18.12", "rm -r ~/tt_doc/doc_txt16/Files16/*"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(delproc.stderr))
    if delproc.stderr == b'':
        print("[del] Files16 has been deleted on server !")
        messagebox.showinfo("INFO", "Files16 has been deleted on server !")
    else:
        print("[!] Error", "Not deleted Files16 on server [!]")
        messagebox.showerror("Error", "!!! Not deleted Files16 on server !!!")

    try:
        if os.path.getsize('./need/doc_suivi16/main_14b.txt'):
            os.remove('./need/doc_suivi16/main_14b.txt')
            print("[del] File main_14b.txt deleted")
    except FileNotFoundError as filefunc1:
        print("[!] File main_14b.txt does not exist", filefunc1)

    try:
        if os.path.getsize('./need/doc_suivi16/patient16_14b.txt'):
            os.remove('./need/doc_suivi16/patient16_14b.txt')
            print("[del] File patient16_14b.txt deleted")
    except FileNotFoundError as filefunc2:
        print("[!] File patient16_14b.txt does not exist", filefunc2)

    try:
        if os.path.getsize('./ttt/doc_ttt16/convdose.json'):
            os.remove('./ttt/doc_ttt16/convdose.json')
            print("[del] File convdose.json deleted")
    except FileNotFoundError as filefunc3:
        print("[!] File convdose.json does not exist", filefunc3)

    try:
        if os.path.getsize('./ttt/doc_ttt16/intro_ttt.txt'):
            os.remove('./ttt/doc_ttt16/intro_ttt.txt')
            print("[del] File intro_ttt.txt deleted")
    except FileNotFoundError as filefunc4:
        print("[!] File intro_ttt.txt does not exist", filefunc4)

    try:
        if os.path.getsize('./ttt/doc_ttt16/stopped_ttt.txt'):
            os.remove('./ttt/doc_ttt16/stopped_ttt.txt')
            print("[del] File stopped_ttt.txt deleted")
    except FileNotFoundError as fnf_stopttt:
        print("[!] File stopped_ttt.txt does not exist", fnf_stopttt)

    try:
        if os.path.getsize('./ttt/doc_ttt16/intro_ts.txt'):
            os.remove('./ttt/doc_ttt16/intro_ts.txt')
            print("[del] File intro_ts.txt deleted (16)")
    except FileNotFoundError as err_ts:
        print("[!] File intro_ts.txt does not exist", err_ts)

    try:
        if os.path.getsize('./ttt/doc_ttt16/report_ttt.txt'):
            os.remove('./ttt/doc_ttt16/report_ttt.txt')
            print("[del] File report_ttt.txt deleted (16)")
    except FileNotFoundError as err_trep:
        print("[!] File report_ttt.txt does not exist", err_trep)

    try:
        if os.path.getsize('./ttt/doc_ttt16/report_res.txt'):
            os.remove('./ttt/doc_ttt16/report_res.txt')
            print("[del] File report_res.txt deleted (16)")
    except FileNotFoundError as err_resrep:
        print("[!] File report_res.txt does not exist", err_resrep)

    try:
        if os.path.getsize('./ttt/doc_ttt16/ires_rs.txt'):
            os.remove('./ttt/doc_ttt16/ires_rs.txt')
            print("[del] File ires_rs.txt deleted (16)")
    except FileNotFoundError as err_res:
        print("[!] File ires_rs.txt does not exist", err_res)

    try:
        if os.path.getsize('./ttt/doc_ttt16/convres.json'):
            os.remove('./ttt/doc_ttt16/convres.json')
            print("[del] File convres.json deleted")
    except FileNotFoundError as filefunc5:
        print("[!] File convres.json does not exist", filefunc5)

    try:
        if os.path.getsize('./ttt/doc_ttt16/intro_res.txt'):
            os.remove('./ttt/doc_ttt16/intro_res.txt')
            print("[del] File intro_res.txt deleted")
    except FileNotFoundError as filefunc6:
        print("[!] File intro_res.txt does not exist", filefunc6)

    try:
        if os.path.getsize('./ttt/doc_ttt16/stopped_res.txt'):
            os.remove('./ttt/doc_ttt16/stopped_res.txt')
            print("[del] File stopped_res.txt deleted")
    except FileNotFoundError as fnf_stopres:
        print("[!] File stopped_res.txt does not exist", fnf_stopres)

    try:
        if os.path.getsize('./param/paramdata16.txt'):
            os.remove('./param/paramdata16.txt')
            print("[del] File paramdata16.txt deleted")
    except FileNotFoundError as filefunc61:
        print("[!] File paramdata16.txt does not exist", filefunc61)

    try:
        if os.path.getsize('./param/aspifile16/diastol.json'):
            os.remove('./param/aspifile16/diastol.json')
            print("[del] File diastol.json deleted")
    except FileNotFoundError as filefunc62:
        print("[!] File diastol.json does not exist", filefunc62)

    try:
        if os.path.getsize('./param/aspifile16/dlr.json'):
            os.remove('./param/aspifile16/dlr.json')
            print("[del] File dlr.json deleted")
    except FileNotFoundError as filefunc63:
        print("[!] File dlr.json does not exist", filefunc63)

    try:
        if os.path.getsize('./param/aspifile16/freq.json'):
            os.remove('./param/aspifile16/freq.json')
            print("[del] File freq.json deleted")
    except FileNotFoundError as filefunc64:
        print("[!] File freq.json does not exist", filefunc64)

    try:
        if os.path.getsize('./param/aspifile16/gly.json'):
            os.remove('./param/aspifile16/gly.json')
            print("[del] File gly.json deleted")
    except FileNotFoundError as filefunc65:
        print("[!] File gly.json does not exist", filefunc65)

    try:
        if os.path.getsize('./param/aspifile16/puls.json'):
            os.remove('./param/aspifile16/puls.json')
            print("[del] File puls.json deleted")
    except FileNotFoundError as filefunc66:
        print("[!] File puls.json does not exist", filefunc66)

    try:
        if os.path.getsize('./param/aspifile16/sat.json'):
            os.remove('./param/aspifile16/sat.json')
            print("[del] File sat.json deleted")
    except FileNotFoundError as filefunc67:
        print("[!] File sat.json does not exist", filefunc67)

    try:
        if os.path.getsize('./param/aspifile16/systol.json'):
            os.remove('./param/aspifile16/systol.json')
            print("[del] File systol.json deleted")
    except FileNotFoundError as filefunc68:
        print("[!] File systol.json does not exist", filefunc68)

    try:
        if os.path.getsize('./param/aspifile16/temp.json'):
            os.remove('./param/aspifile16/temp.json')
            print("[del] File temp.json deleted")
    except FileNotFoundError as filefunc69:
        print("[!] File temp.json does not exist", filefunc69)

    try:
        if os.path.getsize('./calBmi/doc_BMI16/file_bmi.json'):
            os.remove('./calBmi/doc_BMI16/file_bmi.json')
            print("[del] File file_bmi.json deleted")
    except FileNotFoundError as filefunc7:
        print("[!] File file_bmi.json does not exist", filefunc7)

    try:
        if os.path.getsize('./calBmi/doc_BMI16/file_kg.json'):
            os.remove('./calBmi/doc_BMI16/file_kg.json')
            print("[del] File file_kg.json deleted")
    except FileNotFoundError as filefunc8:
        print("[!] File file_kg.json does not exist", filefunc8)

    try:
        if os.path.getsize('./calBmi/doc_BMI16/custom_kg.txt'):
            os.remove('./calBmi/doc_BMI16/custom_kg.txt')
            print("[del] File custom_kg.txt deleted")
    except FileNotFoundError as filefunc81:
        print("[!] File custom_kg.txt does not exist", filefunc81)

    try:
        if os.path.getsize('./calBmi/bmi16.txt'):
            os.remove('./calBmi/bmi16.txt')
            print("[del] File bmi16.txt deleted")
    except FileNotFoundError as filefunc9:
        print("[!] File bmi16.txt does not exist", filefunc9)

    try:
        if os.path.getsize('./diag/doc_diag16/diagrecap16.txt'):
            os.remove('./diag/doc_diag16/diagrecap16.txt')
            print("[del] File diagrecap16.txt deleted")
    except FileNotFoundError as filefunc10:
        print("[!] File diagrecap16.txt does not exist", filefunc10)

    try:
        if os.path.getsize('./labo/doc_labo/result16.txt'):
            os.remove('./labo/doc_labo/result16.txt')
            print("[del] File result16.txt deleted")
    except FileNotFoundError as filefunc11:
        print("[!] File result16.txt does not exist", filefunc11)

    try:
        if os.path.getsize('./patient_agenda/events16/doc_events/fix_agenda/fixed_rdv.txt'):
            os.remove('./patient_agenda/events16/doc_events/fix_agenda/fixed_rdv.txt')
            print("[del] File fixed_rdv.txt deleted")
    except FileNotFoundError as filefunc12:
        print("[!] File fixed_rdv.txt does not exist", filefunc12)

    try:
        if os.path.getsize('./patient_agenda/events16/doc_events/fix_agenda/modifrdv.txt'):
            os.remove('./patient_agenda/events16/doc_events/fix_agenda/modifrdv.txt')
            print("[del] File modifrdv.txt deleted")
    except FileNotFoundError as filefunc13:
        print("[!] File modifrdv.txt does not exist", filefunc13)

    try:
        if os.path.getsize('./patient_agenda/events16/doc_events/fix_agenda/patient_value.json'):
            os.remove('./patient_agenda/events16/doc_events/fix_agenda/patient_value.json')
            print("[del] File patient_value.json deleted")
    except FileNotFoundError as filefunc14:
        print("[!] File patient_value.json does not exist", filefunc14)

    try:
        if os.path.getsize('./patient_agenda/events16/doc_events/patient_rdv.json'):
            os.remove('./patient_agenda/events16/doc_events/patient_rdv.json')
            print("[del] File patient_rdv.json deleted")
    except FileNotFoundError as filefunc15:
        print("[!] File patient_rdv.json does not exist", filefunc15)

    try:
        if os.path.getsize('./patient_agenda/events16/patient_calendar.txt'):
            os.remove('./patient_agenda/events16/patient_calendar.txt')
            print("[del] File patient_calendar.txt deleted")
    except FileNotFoundError as filefunc16:
        print("[!] File patient_calendar.txt does not exist", filefunc16)

    try:
        if os.path.getsize('./vmed/doc_vmed16/resultvmed16.txt'):
            os.remove('./vmed/doc_vmed16/resultvmed16.txt')
            print("[del] File resultvmed16.txt deleted")
    except FileNotFoundError as filefunc17:
        print("[!] File resultvmed16.txt does not exist", filefunc17)

    try:
        if os.path.getsize('./allergy/allergyfile16.txt'):
            os.remove('./allergy/allergyfile16.txt')
            print("[del] File allergyfile16.txt deleted")
    except FileNotFoundError as filefunc18:
        print("[!] File allergyfile16.txt does not exist", filefunc18)

    try:
        if os.path.getsize('./newpatient/entryfile16.txt'):
            with open('./newpatient/entryfile16.txt', 'w') as file:
                file.write("----------------")
            print("[del] File entryfile16.txt deleted")
    except FileNotFoundError as filefunc19:
        print("[!] File entryfile16.txt does not exist", filefunc19)

    proc = subprocess.run(["scp", "./newpatient/entryfile16.txt",
        "pi@192.168.18.12:~/tt_doc/doc_txt16/Files16/entryfile16.txt"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[!] File entryfile16.txt uploaded !")
        #messagebox.showinfo("INFO", "entryfile16.txt uploaded...")
    else:
        print("[!] No file to upload !")
        messagebox.showerror("Error", "No entryfile16.txt to upload...")

    try:
        if os.path.getsize('./auxequip/doc_equip16/auxiliary1.txt'):
            os.remove('./auxequip/doc_equip16/auxiliary1.txt')
            print("[del] File auxiliary1.txt deleted")
    except FileNotFoundError as filefunc20:
        print("[!] File auxiliary1.txt does not exist", filefunc20)

    try:
        if os.path.getsize('./contact/conpact16/contact1.txt'):
            os.remove('./contact/conpact16/contact1.txt')
            print("[del] File contact1.txt deleted")
    except FileNotFoundError as filefunc21:
        print("[!] File contact1.txt does not exist", filefunc21)

    try:
        if os.path.getsize('./contact/conpact16/contactdoc1.txt'):
            os.remove('./contact/conpact16/contactdoc1.txt')
            print("[del] File contactdoc1.txt deleted")
    except FileNotFoundError as filefunc22:
        print("[!] File contactdoc1.txt does not exist", filefunc22)

    try:
        if os.path.getsize('./contact/conpact16/contactdoc2.txt'):
            os.remove('./contact/conpact16/contactdoc2.txt')
            print("[del] File contactdoc2.txt deleted")
    except FileNotFoundError as filefunc23:
        print("[!] File contactdoc2.txt does not exist", filefunc23)

    try:
        if os.path.getsize('./contact/conpact16/contactdoc3.txt'):
            os.remove('./contact/conpact16/contactdoc3.txt')
            print("[del] File contactdoc3.txt deleted")
    except FileNotFoundError as filefunc24:
        print("[!] File contactdoc3.txt does not exist", filefunc24)

    try:
        if os.path.getsize('./contact/conpact16/famycontact1.txt'):
            os.remove('./contact/conpact16/famycontact1.txt')
            print("[del] File famycontact1.txt deleted")
    except FileNotFoundError as filefunc25:
        print("[!] File famycontact1.txt does not exist", filefunc25)

    try:
        if os.path.getsize('./contact/conpact16/hcscontact1.txt'):
            os.remove('./contact/conpact16/hcscontact1.txt')
            print("[del] File hcscontact1.txt deleted")
    except FileNotFoundError as filefunc26:
        print("[!] File hcscontact1.txt does not exist", filefunc26)

    try:
        if os.path.getsize('./contact/conpact16/hcscontact2.txt'):
            os.remove('./contact/conpact16/hcscontact2.txt')
            print("[del] File hcscontact2.txt deleted")
    except FileNotFoundError as filefunc27:
        print("[!] File hcscontact2.txt does not exist", filefunc27)

    try:
        if os.path.getsize('./contact/conpact16/hcscontact3.txt'):
            os.remove('./contact/conpact16/hcscontact3.txt')
            print("[del] File hcscontact3.txt deleted")
    except FileNotFoundError as filefunc28:
        print("[!] File hcscontact3.txt does not exist", filefunc28)

    try:
        if os.path.getsize('./medidoc/doc_dmst16/parcours.txt'):
            os.remove('./medidoc/doc_dmst16/parcours.txt')
            print("[del] File parcours.txt deleted")
    except FileNotFoundError as filefunc29:
        print("[!] File parcours.txt does not exist", filefunc29)

    try:
        if os.path.getsize('./medidoc/doc_dmst16/pbm.txt'):
            os.remove('./medidoc/doc_dmst16/pbm.txt')
            print("[del] File pbm.txt deleted")
    except FileNotFoundError as filefunc30:
        print("[!] File pbm.txt does not exist", filefunc30)

    try:
        if os.path.getsize('./medidoc/doc_dmst16/project.txt'):
            os.remove('./medidoc/doc_dmst16/project.txt')
            print("[del] File project.txt deleted")
    except FileNotFoundError as filefunc31:
        print("[!] File project.txt does not exist", filefunc31)

    try:
        if os.path.getsize('./medidoc/doc_dmst16/rslt_dmst1.txt'):
            os.remove('./medidoc/doc_dmst16/rslt_dmst1.txt')
            print("[del] File rslt_dmst1.txt deleted")
    except FileNotFoundError as filefunc32:
        print("[!] File rslt_dmst1.txt does not exist", filefunc32)

    try:
        if os.path.exists('./Backup/Files16/Backup_param16.txt'):
            print("[+] Backup_param16.txt exist")
            shutil.copy('./Backup/Files16/Backup_param16.txt',
                './Backup/old/oldfiles16/Backup_param16.txt')
            os.remove('./Backup/Files16/Backup_param16.txt')
    except FileNotFoundError as nf_param:
        print("[!] Not found", nf_param)

    try:
        if os.path.exists('./Backup/Files16/Backup_patient16.txt'):
            print("[+] Backup_patient16.txt exist")
            shutil.copy('./Backup/Files16/Backup_patient16.txt',
                './Backup/old/oldfiles16/Backup_patient16.txt')
            os.remove('./Backup/Files16/Backup_patient16.txt')
    except FileNotFoundError as nf_oldfile:
        print("[!] Not found", nf_oldfile)

    try:
        if os.path.exists('./Backup/Files16/Backup_careneeds16.txt'):
            print("[+] Backup_careneeds16.txt exist")
            shutil.copy('./Backup/Files16/Backup_careneeds16.txt',
                './Backup/old/oldfiles16/Backup_careneeds16.txt')
            os.remove('./Backup/Files16/Backup_careneeds16.txt')
    except FileNotFoundError as nf_oldfile2:
        print("[!] Not found", nf_oldfile2)

    try:
        if os.path.exists('./Backup/Files16/Backup_diag16.txt'):
            print("[+] Backup_diag16.txt exist")
            shutil.copy('./Backup/Files16/Backup_diag16.txt',
                './Backup/old/oldfiles16/Backup_diag16.txt')
            os.remove('./Backup/Files16/Backup_diag16.txt')
    except FileNotFoundError as nf_oldfile3:
        print("[!] Not found", nf_oldfile3)

    try:
        if os.path.exists('./Backup/Files16/Backup_Bmi16.txt'):
            print("[+] Backup_Bmi16.txt exist")
            shutil.copy('./Backup/Files16/Backup_Bmi16.txt',
                './Backup/old/oldfiles16/Backup_Bmi16.txt')
            os.remove('./Backup/Files16/Backup_Bmi16.txt')
    except FileNotFoundError as nf_oldfile4:
        print("[!] Not found", nf_oldfile4)

    try:
        if os.path.exists('./Backup/Files16/Backup_resultvmed16.txt'):
            print("[+] Backup_resultvmed16.txt exist")
            shutil.copy('./Backup/Files16/Backup_resultvmed16.txt',
                './Backup/old/oldfiles16/Backup_resultvmed16.txt')
            os.remove('./Backup/Files16/Backup_resultvmed16.txt')
    except FileNotFoundError as nf_oldfile5:
        print("[!] Not found", nf_oldfile5)

    try:
        if os.path.exists('./Backup/Files16/Backup_ttt16.txt'):
            print("[+] Backup_ttt16.txt exist")
            shutil.copy('./Backup/Files16/Backup_ttt16.txt',
                './Backup/old/oldfiles16/Backup_ttt16.txt')
            os.remove('./Backup/Files16/Backup_ttt16.txt')
    except FileNotFoundError as nf_oldfile6:
        print("[!] Not found", nf_oldfile6)

    try:
        if os.path.exists('./Backup/Files16'):
            print("[+] Files16 doc exist !")
            shutil.rmtree('./Backup/Files16')
            print("[del] Files16 doc deleted !")
    except OSError as doc_nf:
        print("[!] Not found", doc_nf)

    print("!!! All files have been deleted !!!")
    print("[Backup] Copy and transfer files in directory <old> was made !")
