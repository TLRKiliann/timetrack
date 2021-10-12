#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
    To delete all files for patient 3
    when usr delete patient by pressing
    the delete button.
"""


from tkinter import *
from tkinter import messagebox
import os
import subprocess
import shutil


def delFuncFile3():
    """
        This function delete all files with
        a test before removing files.
    """
    backproc = subprocess.run(["scp", "-r", "-C", "./Backup/Files3",
        "pi@192.168.18.12:~/tt_doc/doc_txt3/Backup3"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(backproc.stderr))
    if backproc.stderr == b'':
        print("[Backup] Backup3 done on server !")
        messagebox.showinfo("INFO", "Backup3 done on server !")
    else:
        print("[!] No Backup3 done on server [!]")
        messagebox.showerror("Error", "!!! No Backup3 done on server !!!")

    delproc = subprocess.run(["ssh",
        "pi@192.168.18.12", "rm -r ~/tt_doc/doc_txt3/Files3/*"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(delproc.stderr))
    if delproc.stderr == b'':
        print("[del] Files3 has been deleted on server !")
        messagebox.showinfo("INFO", "Files3 has been deleted on server !")
    else:
        print("[!] Error", "Not deleted Files3 on server [!]")
        messagebox.showerror("Error", "!!! Not deleted Files3 on server !!!")

    try:
        if os.path.getsize('./need/doc_suivi3/main_14b.txt'):
            os.remove('./need/doc_suivi3/main_14b.txt')
            print("[del] File main_14b.txt deleted (3)")
    except FileNotFoundError as filefunc1:
        print("[!] File main_14b.txt does not exist", filefunc1)

    try:
        if os.path.getsize('./need/doc_suivi3/patient3_14b.txt'):
            os.remove('./need/doc_suivi3/patient3_14b.txt')
            print("[del] File patient3_14b.txt deleted (3)")
    except FileNotFoundError as filefunc2:
        print("[!] File patient3_14b.txt does not exist", filefunc2)

    try:
        if os.path.getsize('./ttt/doc_ttt3/convdose.json'):
            os.remove('./ttt/doc_ttt3/convdose.json')
            print("[del] File convdose.json deleted (3)")
    except FileNotFoundError as filefunc3:
        print("[!] File convdose.json does not exist", filefunc3)

    try:
        if os.path.getsize('./ttt/doc_ttt3/intro_ttt.txt'):
            os.remove('./ttt/doc_ttt3/intro_ttt.txt')
            print("[del] File intro_ttt.txt deleted (3)")
    except FileNotFoundError as filefunc4:
        print("[!] File intro_ttt.txt does not exist", filefunc4)

    try:
        if os.path.getsize('./ttt/doc_ttt3/stopped_ttt.txt'):
            os.remove('./ttt/doc_ttt3/stopped_ttt.txt')
            print("[del] File stopped_ttt.txt deleted (3)")
    except FileNotFoundError as fnf_stopttt:
        print("[!] File stopped_ttt.txt does not exist", fnf_stopttt)

    try:
        if os.path.getsize('./ttt/doc_ttt3/intro_ts.txt'):
            os.remove('./ttt/doc_ttt3/intro_ts.txt')
            print("[del] File intro_ts.txt deleted (3)")
    except FileNotFoundError as err_ts:
        print("[!] File intro_ts.txt does not exist", err_ts)

    try:
        if os.path.getsize('./ttt/doc_ttt3/report_ttt.txt'):
            os.remove('./ttt/doc_ttt3/report_ttt.txt')
            print("[del] File report_ttt.txt deleted (3)")
    except FileNotFoundError as err_trep:
        print("[!] File report_ttt.txt does not exist", err_trep)

    try:
        if os.path.getsize('./ttt/doc_ttt3/report_res.txt'):
            os.remove('./ttt/doc_ttt3/report_res.txt')
            print("[del] File report_res.txt deleted (3)")
    except FileNotFoundError as err_resrep:
        print("[!] File report_res.txt does not exist", err_resrep)

    try:
        if os.path.getsize('./ttt/doc_ttt3/ires_rs.txt'):
            os.remove('./ttt/doc_ttt3/ires_rs.txt')
            print("[del] File ires_rs.txt deleted (3)")
    except FileNotFoundError as err_res:
        print("[!] File ires_rs.txt does not exist", err_res)

    try:
        if os.path.getsize('./ttt/doc_ttt3/convres.json'):
            os.remove('./ttt/doc_ttt3/convres.json')
            print("[del] File convres.json deleted (3)")
    except FileNotFoundError as filefunc5:
        print("[!] File convres.json does not exist", filefunc5)

    try:
        if os.path.getsize('./ttt/doc_ttt3/intro_res.txt'):
            os.remove('./ttt/doc_ttt3/intro_res.txt')
            print("[del] File intro_res.txt deleted (3)")
    except FileNotFoundError as filefunc6:
        print("[!] File intro_res.txt does not exist", filefunc6)

    try:
        if os.path.getsize('./ttt/doc_ttt3/stopped_res.txt'):
            os.remove('./ttt/doc_ttt3/stopped_res.txt')
            print("[del] File stopped_res.txt deleted (3)")
    except FileNotFoundError as fnf_stopres:
        print("[!] File stopped_res.txt does not exist", fnf_stopres)

    try:
        if os.path.getsize('./param/paramdata3.txt'):
            os.remove('./param/paramdata3.txt')
            print("[del] File paramdata3.txt deleted (3)")
    except FileNotFoundError as fnf_param:
        print("[!] File paramdata3.txt does not exist", fnf_param)

    try:
        if os.path.getsize('./param/aspifile3/diastol.json'):
            os.remove('./param/aspifile3/diastol.json')
            print("[del] File diastol.json deleted (3)")
    except FileNotFoundError as filefunc62:
        print("[!] File diastol.json does not exist", filefunc62)

    try:
        if os.path.getsize('./param/aspifile3/dlr.json'):
            os.remove('./param/aspifile3/dlr.json')
            print("[del] File dlr.json deleted (3)")
    except FileNotFoundError as filefunc63:
        print("[!] File dlr.json does not exist", filefunc63)

    try:
        if os.path.getsize('./param/aspifile3/freq.json'):
            os.remove('./param/aspifile3/freq.json')
            print("[del] File freq.json deleted (3)")
    except FileNotFoundError as filefunc64:
        print("[!] File freq.json does not exist", filefunc64)

    try:
        if os.path.getsize('./param/aspifile3/gly.json'):
            os.remove('./param/aspifile3/gly.json')
            print("[del] File gly.json deleted (3)")
    except FileNotFoundError as filefunc65:
        print("[!] File gly.json does not exist", filefunc65)

    try:
        if os.path.getsize('./param/aspifile3/puls.json'):
            os.remove('./param/aspifile3/puls.json')
            print("[del] File puls.json deleted (3)")
    except FileNotFoundError as filefunc66:
        print("[!] File puls.json does not exist", filefunc66)

    try:
        if os.path.getsize('./param/aspifile3/sat.json'):
            os.remove('./param/aspifile3/sat.json')
            print("[del] File sat.json deleted (3)")
    except FileNotFoundError as filefunc67:
        print("[!] File sat.json does not exist", filefunc67)

    try:
        if os.path.getsize('./param/aspifile3/systol.json'):
            os.remove('./param/aspifile3/systol.json')
            print("[del] File systol.json deleted (3)")
    except FileNotFoundError as filefunc68:
        print("[!] File systol.json does not exist", filefunc68)

    try:
        if os.path.getsize('./param/aspifile3/temp.json'):
            os.remove('./param/aspifile3/temp.json')
            print("[del] File temp.json deleted (3)")
    except FileNotFoundError as filefunc69:
        print("[!] File temp.json does not exist", filefunc69)

    try:
        if os.path.getsize('./calBmi/doc_BMI3/file_bmi.json'):
            os.remove('./calBmi/doc_BMI3/file_bmi.json')
            print("[del] File file_bmi.json deleted (3)")
    except FileNotFoundError as filefunc7:
        print("[!] File file_bmi.json does not exist", filefunc7)

    try:
        if os.path.getsize('./calBmi/doc_BMI3/file_kg.json'):
            os.remove('./calBmi/doc_BMI3/file_kg.json')
            print("[del] File file_kg.json deleted (3)")
    except FileNotFoundError as filefunc8:
        print("[!] File file_kg.json does not exist", filefunc8)

    try:
        if os.path.getsize('./calBmi/doc_BMI3/custom_kg.txt'):
            os.remove('./calBmi/doc_BMI3/custom_kg.txt')
            print("[del] File custom_kg.txt deleted (3)")
    except FileNotFoundError as filefunc81:
        print("[!] File custom_kg.txt does not exist", filefunc81)

    try:
        if os.path.getsize('./calBmi/bmi3.txt'):
            os.remove('./calBmi/bmi3.txt')
            print("[del] File bmi3.txt deleted (3)")
    except FileNotFoundError as filefunc9:
        print("[!] File bmi3.txt does not exist", filefunc9)

    try:
        if os.path.getsize('./diag/doc_diag3/diagrecap3.txt'):
            os.remove('./diag/doc_diag3/diagrecap3.txt')
            print("[del] File diagrecap3.txt deleted (3)")
    except FileNotFoundError as filefunc10:
        print("[!] File diagrecap3.txt does not exist", filefunc10)

    try:
        if os.path.getsize('./labo/doc_labo/result3.txt'):
            os.remove('./labo/doc_labo/result3.txt')
            print("[del] File result3.txt deleted (3)")
    except FileNotFoundError as filefunc11:
        print("[!] File result3.txt does not exist", filefunc11)

    try:
        if os.path.getsize('./patient_agenda/events3/doc_events/fix_agenda/fixed_rdv.txt'):
            os.remove('./patient_agenda/events3/doc_events/fix_agenda/fixed_rdv.txt')
            print("[del] File fixed_rdv.txt deleted (3)")
    except FileNotFoundError as filefunc12:
        print("[!] File fixed_rdv.txt does not exist", filefunc12)

    try:
        if os.path.getsize('./patient_agenda/events3/doc_events/fix_agenda/modifrdv.txt'):
            os.remove('./patient_agenda/events3/doc_events/fix_agenda/modifrdv.txt')
            print("[del] File modifrdv.txt deleted (3)")
    except FileNotFoundError as filefunc13:
        print("[!] File modifrdv.txt does not exist", filefunc13)

    try:
        if os.path.getsize('./patient_agenda/events3/doc_events/fix_agenda/patient_value.json'):
            os.remove('./patient_agenda/events3/doc_events/fix_agenda/patient_value.json')
            print("[del] File patient_value.json deleted (3)")
    except FileNotFoundError as filefunc14:
        print("[!] File patient_value.json does not exist", filefunc14)

    try:
        if os.path.getsize('./patient_agenda/events3/doc_events/patient_rdv.json'):
            os.remove('./patient_agenda/events3/doc_events/patient_rdv.json')
            print("[del] File patient_rdv.json deleted (3)")
    except FileNotFoundError as filefunc15:
        print("[!] File patient_rdv.json does not exist", filefunc15)

    try:
        if os.path.getsize('./patient_agenda/events3/patient_calendar.txt'):
            os.remove('./patient_agenda/events3/patient_calendar.txt')
            print("[del] File patient_calendar.txt deleted (3)")
    except FileNotFoundError as err_patcalend:
        print("[!] File patient_calendar.txt does not exist", err_patcalend)

    try:
        if os.path.getsize('./vmed/doc_vmed3/resultvmed3.txt'):
            os.remove('./vmed/doc_vmed3/resultvmed3.txt')
            print("[del] File resultvmed3.txt.txt deleted (3)")
    except FileNotFoundError as err_vmed:
        print("[!] File resultvmed3.txt.txt does not exist", err_vmed)

    try:
        if os.path.getsize('./allergy/allergyfile3.txt'):
            os.remove('./allergy/allergyfile3.txt')
            print("[del] File allergyfile3.txt deleted (3)")
    except FileNotFoundError as filefunc18:
        print("[!] File allergyfile3.txt does not exist", filefunc18)

    try:
        if os.path.getsize('./newpatient/entryfile3.txt'):
            with open('./newpatient/entryfile3.txt', 'w') as file:
                file.write("---")
            print("[del] File entryfile3.txt reborn")
    except FileNotFoundError as filefunc19:
        print("[!] File entryfile3.txt does not exist", filefunc19)

    proc = subprocess.run(["scp", "./newpatient/entryfile3.txt",
        "pi@192.168.18.12:~/tt_doc/doc_txt3/Files3/entryfile3.txt"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("[!] File entryfile3.txt uploaded !")
        #messagebox.showinfo("INFO", "entryfile3.txt uploaded...")
    else:
        print("[!] No file to upload !")
        messagebox.showerror("Error", "No entryfile3.txt to upload...")

    try:
        if os.path.getsize('./auxequip/doc_equip3/auxiliary1.txt'):
            os.remove('./auxequip/doc_equip3/auxiliary1.txt')
            print("[del] File auxiliary1.txt deleted (3)")
    except FileNotFoundError as filefunc20:
        print("[!] File auxiliary1.txt does not exist", filefunc20)

    try:
        if os.path.getsize('./contact/conpact3/contact1.txt'):
            os.remove('./contact/conpact3/contact1.txt')
            print("[del] File contact1.txt deleted (3)")
    except FileNotFoundError as filefunc21:
        print("[!] File contact1.txt does not exist", filefunc21)

    try:
        if os.path.getsize('./contact/conpact3/contactdoc1.txt'):
            os.remove('./contact/conpact3/contactdoc1.txt')
            print("[del] File contactdoc1.txt deleted (3)")
    except FileNotFoundError as filefunc22:
        print("[!] File contactdoc1.txt does not exist", filefunc22)

    try:
        if os.path.getsize('./contact/conpact3/contactdoc2.txt'):
            os.remove('./contact/conpact3/contactdoc2.txt')
            print("[del] File contactdoc2.txt deleted (3)")
    except FileNotFoundError as filefunc23:
        print("[!] File contactdoc2.txt does not exist", filefunc23)

    try:
        if os.path.getsize('./contact/conpact3/contactdoc3.txt'):
            os.remove('./contact/conpact3/contactdoc3.txt')
            print("[del] File contactdoc3.txt deleted (3)")
    except FileNotFoundError as filefunc24:
        print("[!] File contactdoc3.txt does not exist", filefunc24)

    try:
        if os.path.getsize('./contact/conpact3/famycontact1.txt'):
            os.remove('./contact/conpact3/famycontact1.txt')
            print("[del] File famycontact1.txt deleted (3)")
    except FileNotFoundError as err_famy:
        print("[!] File famycontact1.txt does not exist", err_famy)

    try:
        if os.path.getsize('./contact/conpact3/hcscontact1.txt'):
            os.remove('./contact/conpact3/hcscontact1.txt')
            print("[del] File hcscontact1.txt deleted (3)")
    except FileNotFoundError as err_hcs1:
        print("[!] File hcscontact1.txt does not exist", err_hcs1)

    try:
        if os.path.getsize('./contact/conpact3/hcscontact2.txt'):
            os.remove('./contact/conpact3/hcscontact2.txt')
            print("[del] File hcscontact2.txt deleted (3)")
    except FileNotFoundError as err_hcs2:
        print("[!] File hcscontact2.txt does not exist", err_hcs2)

    try:
        if os.path.getsize('./contact/conpact3/hcscontact3.txt'):
            os.remove('./contact/conpact3/hcscontact3.txt')
            print("[del] File hcscontact3.txt deleted (3)")
    except FileNotFoundError as err_hcs3:
        print("[!] File hcscontact3.txt does not exist", err_hcs3)

    try:
        if os.path.getsize('./medidoc/doc_dmst3/parcours.txt'):
            os.remove('./medidoc/doc_dmst3/parcours.txt')
            print("[del] File parcours.txt deleted (3)")
    except FileNotFoundError as filefunc29:
        print("[!] File parcours.txt does not exist", filefunc29)

    try:
        if os.path.getsize('./medidoc/doc_dmst3/pbm.txt'):
            os.remove('./medidoc/doc_dmst3/pbm.txt')
            print("[del] File pbm.txt deleted (3)")
    except FileNotFoundError as filefunc30:
        print("[!] File pbm.txt does not exist", filefunc30)

    try:
        if os.path.getsize('./medidoc/doc_dmst3/project.txt'):
            os.remove('./medidoc/doc_dmst3/project.txt')
            print("[del] File project.txt deleted (3)")
    except FileNotFoundError as filefunc31:
        print("[!] File project.txt does not exist", filefunc31)

    try:
        if os.path.getsize('./medidoc/doc_dmst3/rslt_dmst1.txt'):
            os.remove('./medidoc/doc_dmst3/rslt_dmst1.txt')
            print("[del] File rslt_dmst1.txt deleted (3)")
    except FileNotFoundError as fnf_dmst:
        print("[!] File rslt_dmst1.txt does not exist", fnf_dmst)

    try:
        if os.path.exists('./Backup/Files3/Backup_param3.txt'):
            print("[+] Backup_param3.txt exist")
            shutil.copy('./Backup/Files3/Backup_param3.txt',
                './Backup/old/oldfiles3/Backup_param3.txt')
            os.remove('./Backup/Files3/Backup_param3.txt')
    except FileNotFoundError as nf_param:
        print("[!] Not found", nf_param)

    try:
        if os.path.exists('./Backup/Files3/Backup_patient3.txt'):
            print("[+] Backup_patient3.txt exist")
            shutil.copy('./Backup/Files3/Backup_patient3.txt',
                './Backup/old/oldfiles3/Backup_patient3.txt')
            os.remove('./Backup/Files3/Backup_patient3.txt')
    except FileNotFoundError as nf_oldfpat:
        print("[!] Not found", nf_oldfpat)

    try:
        if os.path.exists('./Backup/Files3/Backup_careneeds3.txt'):
            print("[+] Backup_careneeds3.txt exist")
            shutil.copy('./Backup/Files3/Backup_careneeds3.txt',
                './Backup/old/oldfiles3/Backup_careneeds3.txt')
            os.remove('./Backup/Files3/Backup_careneeds3.txt')
    except FileNotFoundError as nf_oldfneed:
        print("[!] Not found", nf_oldfneed)

    try:
        if os.path.exists('./Backup/Files3/Backup_diag3.txt'):
            print("[+] Backup_diag3.txt exist")
            shutil.copy('./Backup/Files3/Backup_diag3.txt',
                './Backup/old/oldfiles3/Backup_diag3.txt')
            os.remove('./Backup/Files3/Backup_diag3.txt')
    except FileNotFoundError as nf_oldfilediag:
        print("[!] Not found", nf_oldfilediag)

    try:
        if os.path.exists('./Backup/Files3/Backup_Bmi3.txt'):
            print("[+] Backup_Bmi3.txt exist")
            shutil.copy('./Backup/Files3/Backup_Bmi3.txt',
                './Backup/old/oldfiles3/Backup_Bmi3.txt')
            os.remove('./Backup/Files3/Backup_Bmi3.txt')
    except FileNotFoundError as nf_oldfilebmi:
        print("[!] Not found", nf_oldfilebmi)

    try:
        if os.path.exists('./Backup/Files3/Backup_resultvmed3.txt'):
            print("[+] Backup_resultvmed3.txt exist")
            shutil.copy('./Backup/Files3/Backup_resultvmed3.txt',
                './Backup/old/oldfiles3/Backup_resultvmed3.txt')
            os.remove('./Backup/Files3/Backup_resultvmed3.txt')
    except FileNotFoundError as nf_oldfilevmed:
        print("[!] Not found", nf_oldfilevmed)

    try:
        if os.path.exists('./Backup/Files3/Backup_ttt3.txt'):
            print("[+] Backup_ttt3.txt exist")
            shutil.copy('./Backup/Files3/Backup_ttt3.txt',
                './Backup/old/oldfiles3/Backup_ttt3.txt')
            os.remove('./Backup/Files3/Backup_ttt3.txt')
    except FileNotFoundError as nf_oldfilettt:
        print("[!] Not found", nf_oldfilettt)

    try:
        if os.path.exists('./Backup/Files3'):
            print("[+] Files3 doc exist !")
            shutil.rmtree('./Backup/Files3')
            print("[del] Files3 doc deleted !")
    except OSError as doc_nf:
        print("[!] Not found", doc_nf)

    print("!!! All files have been deleted !!!")
    print("[Backup] Copy and transfer files in directory <old> was made !")
    