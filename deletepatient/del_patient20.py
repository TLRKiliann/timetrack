#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
    To delete all files for patient 20
    when usr delete patient by pressing
    the delete button.
"""


from tkinter import *
from tkinter import messagebox
import os
import subprocess
import shutil


def delFuncFile20():
    """
        This function delete all files with
        a test before removing files.
    """
    backproc = subprocess.run(["scp", "-r", "-C", "./Backup/Files20",
        "pi@192.168.18.12:~/tt_doc/doc_txt20/Backup20"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(backproc.stderr))
    if backproc.stderr == b'':
        print("[Backup] Backup20 done on server !")
        messagebox.showinfo("INFO", "Backup20 done on server !")
    else:
        print("[!] No Backup20 done on server [!]")
        messagebox.showerror("Error", "!!! No Backup20 done on server !!!")

    delproc = subprocess.run(["ssh",
        "pi@192.168.18.12", "rm -r ~/tt_doc/doc_txt20/Files20/*"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(delproc.stderr))
    if delproc.stderr == b'':
        print("[del] Files20 has been deleted on server !")
        messagebox.showinfo("INFO", "Files20 has been deleted on server !")
    else:
        print("[!] Error", "Not deleted Files20 on server [!]")
        messagebox.showerror("Error", "!!! Not deleted Files20 on server !!!")

    try:
        if os.path.getsize('./need/doc_suivi20/main_14b.txt'):
            os.remove('./need/doc_suivi20/main_14b.txt')
            print("[del] File main_14b.txt deleted")
    except FileNotFoundError as filefunc1:
        print("[!] File main_14b.txt does not exist", filefunc1)

    try:
        if os.path.getsize('./need/doc_suivi20/patient20_14b.txt'):
            os.remove('./need/doc_suivi20/patient20_14b.txt')
            print("[del] File patient20_14b.txt deleted")
    except FileNotFoundError as filefunc2:
        print("[!] File patient20_14b.txt does not exist", filefunc2)

    try:
        if os.path.getsize('./ttt/doc_ttt20/convdose.json'):
            os.remove('./ttt/doc_ttt20/convdose.json')
            print("[del] File convdose.json deleted")
    except FileNotFoundError as filefunc3:
        print("[!] File convdose.json does not exist", filefunc3)

    try:
        if os.path.getsize('./ttt/doc_ttt20/intro_ttt.txt'):
            os.remove('./ttt/doc_ttt20/intro_ttt.txt')
            print("[del] File intro_ttt.txt deleted")
    except FileNotFoundError as filefunc4:
        print("[!] File intro_ttt.txt does not exist", filefunc4)

    try:
        if os.path.getsize('./ttt/doc_ttt20/stopped_ttt.txt'):
            os.remove('./ttt/doc_ttt20/stopped_ttt.txt')
            print("[del] File stopped_ttt.txt deleted")
    except FileNotFoundError as fnf_stopttt:
        print("[!] File stopped_ttt.txt does not exist", fnf_stopttt)

    try:
        if os.path.getsize('./ttt/doc_ttt20/intro_ts.txt'):
            os.remove('./ttt/doc_ttt20/intro_ts.txt')
            print("[del] File intro_ts.txt deleted (20)")
    except FileNotFoundError as err_ts:
        print("[!] File intro_ts.txt does not exist", err_ts)

    try:
        if os.path.getsize('./ttt/doc_ttt20/report_ttt.txt'):
            os.remove('./ttt/doc_ttt20/report_ttt.txt')
            print("[del] File report_ttt.txt deleted (20)")
    except FileNotFoundError as err_trep:
        print("[!] File report_ttt.txt does not exist", err_trep)

    try:
        if os.path.getsize('./ttt/doc_ttt20/report_res.txt'):
            os.remove('./ttt/doc_ttt20/report_res.txt')
            print("[del] File report_res.txt deleted (20)")
    except FileNotFoundError as err_resrep:
        print("[!] File report_res.txt does not exist", err_resrep)

    try:
        if os.path.getsize('./ttt/doc_ttt20/ires_rs.txt'):
            os.remove('./ttt/doc_ttt20/ires_rs.txt')
            print("[del] File ires_rs.txt deleted (20)")
    except FileNotFoundError as err_res:
        print("[!] File ires_rs.txt does not exist", err_res)

    try:
        if os.path.getsize('./ttt/doc_ttt20/convres.json'):
            os.remove('./ttt/doc_ttt20/convres.json')
            print("[del] File convres.json deleted")
    except FileNotFoundError as filefunc5:
        print("[!] File convres.json does not exist", filefunc5)

    try:
        if os.path.getsize('./ttt/doc_ttt20/intro_res.txt'):
            os.remove('./ttt/doc_ttt20/intro_res.txt')
            print("[del] File intro_res.txt deleted")
    except FileNotFoundError as filefunc6:
        print("[!] File intro_res.txt does not exist", filefunc6)

    try:
        if os.path.getsize('./ttt/doc_ttt20/stopped_res.txt'):
            os.remove('./ttt/doc_ttt20/stopped_res.txt')
            print("[del] File stopped_res.txt deleted")
    except FileNotFoundError as fnf_stopres:
        print("[!] File stopped_res.txt does not exist", fnf_stopres)

    try:
        if os.path.getsize('./param/paramdata20.txt'):
            os.remove('./param/paramdata20.txt')
            print("[del] File paramdata20.txt deleted")
    except FileNotFoundError as filefunc61:
        print("[!] File paramdata20.txt does not exist", filefunc61)

    try:
        if os.path.getsize('./param/aspifile20/diastol.json'):
            os.remove('./param/aspifile20/diastol.json')
            print("[del] File diastol.json deleted")
    except FileNotFoundError as filefunc62:
        print("[!] File diastol.json does not exist", filefunc62)

    try:
        if os.path.getsize('./param/aspifile20/dlr.json'):
            os.remove('./param/aspifile20/dlr.json')
            print("[del] File dlr.json deleted")
    except FileNotFoundError as filefunc63:
        print("[!] File dlr.json does not exist", filefunc63)

    try:
        if os.path.getsize('./param/aspifile20/freq.json'):
            os.remove('./param/aspifile20/freq.json')
            print("[del] File freq.json deleted")
    except FileNotFoundError as filefunc64:
        print("[!] File freq.json does not exist", filefunc64)

    try:
        if os.path.getsize('./param/aspifile20/gly.json'):
            os.remove('./param/aspifile20/gly.json')
            print("[del] File gly.json deleted")
    except FileNotFoundError as filefunc65:
        print("[!] File gly.json does not exist", filefunc65)

    try:
        if os.path.getsize('./param/aspifile20/puls.json'):
            os.remove('./param/aspifile20/puls.json')
            print("[del] File puls.json deleted")
    except FileNotFoundError as filefunc66:
        print("[!] File puls.json does not exist", filefunc66)

    try:
        if os.path.getsize('./param/aspifile20/sat.json'):
            os.remove('./param/aspifile20/sat.json')
            print("[del] File sat.json deleted")
    except FileNotFoundError as filefunc67:
        print("[!] File sat.json does not exist", filefunc67)

    try:
        if os.path.getsize('./param/aspifile20/systol.json'):
            os.remove('./param/aspifile20/systol.json')
            print("[del] File systol.json deleted")
    except FileNotFoundError as filefunc68:
        print("[!] File systol.json does not exist", filefunc68)

    try:
        if os.path.getsize('./param/aspifile20/temp.json'):
            os.remove('./param/aspifile20/temp.json')
            print("[del] File temp.json deleted")
    except FileNotFoundError as filefunc69:
        print("[!] File temp.json does not exist", filefunc69)

    try:
        if os.path.getsize('./calBmi/doc_BMI20/file_bmi.json'):
            os.remove('./calBmi/doc_BMI20/file_bmi.json')
            print("[del] File file_bmi.json deleted")
    except FileNotFoundError as filefunc7:
        print("[!] File file_bmi.json does not exist", filefunc7)

    try:
        if os.path.getsize('./calBmi/doc_BMI20/file_kg.json'):
            os.remove('./calBmi/doc_BMI20/file_kg.json')
            print("[del] File file_kg.json deleted")
    except FileNotFoundError as filefunc8:
        print("[!] File file_kg.json does not exist", filefunc8)

    try:
        if os.path.getsize('./calBmi/doc_BMI20/custom_kg.txt'):
            os.remove('./calBmi/doc_BMI20/custom_kg.txt')
            print("[del] File custom_kg.txt deleted")
    except FileNotFoundError as filefunc81:
        print("[!] File custom_kg.txt does not exist", filefunc81)

    try:
        if os.path.getsize('./calBmi/bmi20.txt'):
            os.remove('./calBmi/bmi20.txt')
            print("[del] File bmi20.txt deleted")
    except FileNotFoundError as filefunc9:
        print("[!] File bmi20.txt does not exist", filefunc9)

    try:
        if os.path.getsize('./diag/doc_diag20/diagrecap20.txt'):
            os.remove('./diag/doc_diag20/diagrecap20.txt')
            print("[del] File diagrecap20.txt deleted")
    except FileNotFoundError as filefunc10:
        print("[!] File diagrecap20.txt does not exist", filefunc10)

    try:
        if os.path.getsize('./labo/doc_labo/result20.txt'):
            os.remove('./labo/doc_labo/result20.txt')
            print("[del] File result20.txt deleted")
    except FileNotFoundError as filefunc11:
        print("[!] File result20.txt does not exist", filefunc11)

    try:
        if os.path.getsize('./patient_agenda/events20/doc_events/fix_agenda/fixed_rdv.txt'):
            os.remove('./patient_agenda/events20/doc_events/fix_agenda/fixed_rdv.txt')
            print("[del] File fixed_rdv.txt deleted")
    except FileNotFoundError as filefunc12:
        print("[!] File fixed_rdv.txt does not exist", filefunc12)

    try:
        if os.path.getsize('./patient_agenda/events20/doc_events/fix_agenda/modifrdv.txt'):
            os.remove('./patient_agenda/events20/doc_events/fix_agenda/modifrdv.txt')
            print("[del] File modifrdv.txt deleted")
    except FileNotFoundError as filefunc13:
        print("[!] File modifrdv.txt does not exist", filefunc13)

    try:
        if os.path.getsize('./patient_agenda/events20/doc_events/fix_agenda/patient_value.json'):
            os.remove('./patient_agenda/events20/doc_events/fix_agenda/patient_value.json')
            print("[del] File patient_value.json deleted")
    except FileNotFoundError as filefunc14:
        print("[!] File patient_value.json does not exist", filefunc14)

    try:
        if os.path.getsize('./patient_agenda/events20/doc_events/patient_rdv.json'):
            os.remove('./patient_agenda/events20/doc_events/patient_rdv.json')
            print("[del] File patient_rdv.json deleted")
    except FileNotFoundError as filefunc15:
        print("[!] File patient_rdv.json does not exist", filefunc15)

    try:
        if os.path.getsize('./patient_agenda/events20/patient_calendar.txt'):
            os.remove('./patient_agenda/events20/patient_calendar.txt')
            print("[del] File patient_calendar.txt deleted")
    except FileNotFoundError as filefunc16:
        print("[!] File patient_calendar.txt does not exist", filefunc16)

    try:
        if os.path.getsize('./vmed/doc_vmed20/resultvmed20.txt'):
            os.remove('./vmed/doc_vmed20/resultvmed20.txt')
            print("[del] File resultvmed20.txt deleted")
    except FileNotFoundError as filefunc17:
        print("[!] File resultvmed20.txt does not exist", filefunc17)

    try:
        if os.path.getsize('./allergy/allergyfile20.txt'):
            os.remove('./allergy/allergyfile20.txt')
            print("[del] File allergyfile20.txt deleted")
    except FileNotFoundError as filefunc18:
        print("[!] File allergyfile20.txt does not exist", filefunc18)

    try:
        if os.path.getsize('./newpatient/entryfile20.txt'):
            with open('./newpatient/entryfile20.txt', 'w') as file:
                file.write("--------------------")
            print("[del] File entryfile20.txt deleted")
    except FileNotFoundError as filefunc19:
        print("[!] File entryfile20.txt does not exist", filefunc19)

    proc = subprocess.run(["scp", "./newpatient/entryfile20.txt",
        "pi@192.168.18.12:~/tt_doc/doc_txt20/Files20/entryfile20.txt"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[!] File entryfile20.txt uploaded !")
        #messagebox.showinfo("INFO", "entryfile20.txt uploaded...")
    else:
        print("[!] No file to upload !")
        messagebox.showerror("Error", "No entryfile20.txt to upload...")

    try:
        if os.path.getsize('./auxequip/doc_equip20/auxiliary1.txt'):
            os.remove('./auxequip/doc_equip20/auxiliary1.txt')
            print("[del] File auxiliary1.txt deleted")
    except FileNotFoundError as filefunc20:
        print("[!] File auxiliary1.txt does not exist", filefunc20)

    try:
        if os.path.getsize('./contact/conpact20/contact1.txt'):
            os.remove('./contact/conpact20/contact1.txt')
            print("[del] File contact1.txt deleted")
    except FileNotFoundError as filefunc21:
        print("[!] File contact1.txt does not exist", filefunc21)

    try:
        if os.path.getsize('./contact/conpact20/contactdoc1.txt'):
            os.remove('./contact/conpact20/contactdoc1.txt')
            print("[del] File contactdoc1.txt deleted")
    except FileNotFoundError as filefunc22:
        print("[!] File contactdoc1.txt does not exist", filefunc22)

    try:
        if os.path.getsize('./contact/conpact20/contactdoc2.txt'):
            os.remove('./contact/conpact20/contactdoc2.txt')
            print("[del] File contactdoc2.txt deleted")
    except FileNotFoundError as filefunc23:
        print("[!] File contactdoc2.txt does not exist", filefunc23)

    try:
        if os.path.getsize('./contact/conpact20/contactdoc3.txt'):
            os.remove('./contact/conpact20/contactdoc3.txt')
            print("[del] File contactdoc3.txt deleted")
    except FileNotFoundError as filefunc24:
        print("[!] File contactdoc3.txt does not exist", filefunc24)

    try:
        if os.path.getsize('./contact/conpact20/famycontact1.txt'):
            os.remove('./contact/conpact20/famycontact1.txt')
            print("[del] File famycontact1.txt deleted")
    except FileNotFoundError as filefunc25:
        print("[!] File famycontact1.txt does not exist", filefunc25)

    try:
        if os.path.getsize('./contact/conpact20/hcscontact1.txt'):
            os.remove('./contact/conpact20/hcscontact1.txt')
            print("[del] File hcscontact1.txt deleted")
    except FileNotFoundError as filefunc26:
        print("[!] File hcscontact1.txt does not exist", filefunc26)

    try:
        if os.path.getsize('./contact/conpact20/hcscontact2.txt'):
            os.remove('./contact/conpact20/hcscontact2.txt')
            print("[del] File hcscontact2.txt deleted")
    except FileNotFoundError as filefunc27:
        print("[!] File hcscontact2.txt does not exist", filefunc27)

    try:
        if os.path.getsize('./contact/conpact20/hcscontact3.txt'):
            os.remove('./contact/conpact20/hcscontact3.txt')
            print("[del] File hcscontact3.txt deleted")
    except FileNotFoundError as filefunc28:
        print("[!] File hcscontact3.txt does not exist", filefunc28)

    try:
        if os.path.getsize('./medidoc/doc_dmst20/parcours.txt'):
            os.remove('./medidoc/doc_dmst20/parcours.txt')
            print("[del] File parcours.txt deleted")
    except FileNotFoundError as filefunc29:
        print("[!] File parcours.txt does not exist", filefunc29)

    try:
        if os.path.getsize('./medidoc/doc_dmst20/pbm.txt'):
            os.remove('./medidoc/doc_dmst20/pbm.txt')
            print("[del] File pbm.txt deleted")
    except FileNotFoundError as filefunc30:
        print("[!] File pbm.txt does not exist", filefunc30)

    try:
        if os.path.getsize('./medidoc/doc_dmst20/project.txt'):
            os.remove('./medidoc/doc_dmst20/project.txt')
            print("[del] File project.txt deleted")
    except FileNotFoundError as filefunc31:
        print("[!] File project.txt does not exist", filefunc31)

    try:
        if os.path.getsize('./medidoc/doc_dmst20/rslt_dmst1.txt'):
            os.remove('./medidoc/doc_dmst20/rslt_dmst1.txt')
            print("[del] File rslt_dmst1.txt deleted")
    except FileNotFoundError as filefunc32:
        print("[!] File rslt_dmst1.txt does not exist", filefunc32)

    try:
        if os.path.exists('./Backup/Files20/Backup_param20.txt'):
            print("[+] Backup_param20.txt exist")
            shutil.copy('./Backup/Files20/Backup_param20.txt',
                './Backup/old/oldfiles20/Backup_param20.txt')
            os.remove('./Backup/Files20/Backup_param20.txt')
    except FileNotFoundError as nf_param:
        print("[!] Not found", nf_param)

    try:
        if os.path.exists('./Backup/Files20/Backup_patient20.txt'):
            print("[+] Backup_patient20.txt exist")
            shutil.copy('./Backup/Files20/Backup_patient20.txt',
                './Backup/old/oldfiles20/Backup_patient20.txt')
            os.remove('./Backup/Files20/Backup_patient20.txt')
    except FileNotFoundError as nf_oldfile:
        print("[!] Not found", nf_oldfile)

    try:
        if os.path.exists('./Backup/Files20/Backup_careneeds20.txt'):
            print("[+] Backup_careneeds20.txt exist")
            shutil.copy('./Backup/Files20/Backup_careneeds20.txt',
                './Backup/old/oldfiles20/Backup_careneeds20.txt')
            os.remove('./Backup/Files20/Backup_careneeds20.txt')
    except FileNotFoundError as nf_oldfile2:
        print("[!] Not found", nf_oldfile2)

    try:
        if os.path.exists('./Backup/Files20/Backup_diag20.txt'):
            print("[+] Backup_diag20.txt exist")
            shutil.copy('./Backup/Files20/Backup_diag20.txt',
                './Backup/old/oldfiles20/Backup_diag20.txt')
            os.remove('./Backup/Files20/Backup_diag20.txt')
    except FileNotFoundError as nf_oldfile3:
        print("[!] Not found", nf_oldfile3)

    try:
        if os.path.exists('./Backup/Files20/Backup_Bmi20.txt'):
            print("[+] Backup_Bmi20.txt exist")
            shutil.copy('./Backup/Files20/Backup_Bmi20.txt',
                './Backup/old/oldfiles20/Backup_Bmi20.txt')
            os.remove('./Backup/Files20/Backup_Bmi20.txt')
    except FileNotFoundError as nf_oldfile4:
        print("[!] Not found", nf_oldfile4)

    try:
        if os.path.exists('./Backup/Files20/Backup_resultvmed20.txt'):
            print("[+] Backup_resultvmed20.txt exist")
            shutil.copy('./Backup/Files20/Backup_resultvmed20.txt',
                './Backup/old/oldfiles20/Backup_resultvmed20.txt')
            os.remove('./Backup/Files20/Backup_resultvmed20.txt')
    except FileNotFoundError as nf_oldfile5:
        print("[!] Not found", nf_oldfile5)

    try:
        if os.path.exists('./Backup/Files20/Backup_ttt20.txt'):
            print("[+] Backup_ttt20.txt exist")
            shutil.copy('./Backup/Files20/Backup_ttt20.txt',
                './Backup/old/oldfiles20/Backup_ttt20.txt')
            os.remove('./Backup/Files20/Backup_ttt20.txt')
    except FileNotFoundError as nf_oldfile6:
        print("[!] Not found", nf_oldfile6)

    try:
        if os.path.exists('./Backup/Files20'):
            print("[+] Files20 doc exist !")
            shutil.rmtree('./Backup/Files20')
            print("[del] Files20 doc deleted !")
    except OSError as doc_nf:
        print("[!] Not found", doc_nf)

    print("!!! All files have been deleted !!!")
    print("[Backup] Copy and transfer files in directory <old> was made !")
