#!/usr/bin/python3
# -*- coding: utf-8 -*-


from tkinter import *
from tkinter import messagebox
import datetime
import time
import os
import subprocess
import shutil

# To copy to ./Backup/Files1
try:
    src = r'./patient_agenda/events/doc_events/fix_agenda/agenda_saved'
    dst = r'./Backup/Files1'
    shutil.copy(os.path.join(src, file), dst)
except (OSError, FileNotFoundError) as e:
    print("+ No files from agenda_1 copied !!!", e)

# To upload to server
proc = subprocess.run(["scp", "-r", "./Backup/Files1",
    "pi@192.168.18.12:~/tt_doc/doc_txt1"], stderr=subprocess.PIPE)
print("Result SCP transfert : %s" % repr(proc.stderr))
if proc.stderr == b'':
    print("+ './Backup/Files1' uploaded !")
else:
    print("+ No file to upload !")
    messagebox.showerror("Error", "./Backup/Files1 not uploaded !")

# To copy to ./Backup/Files2
try:
    src2 = r'./patient_agenda/events2/doc_events/fix_agenda/agenda_saved'
    dst2 = r'./Backup/Files2'
    shutil.copy(os.path.join(src2, file), dst2)
except (OSError, FileNotFoundError) as e2:
    print("+ No files from agenda_2 copied !!!", e2)

secproc = subprocess.run(["scp", "-r", "./Backup/Files2",
    "pi@192.168.18.12:~/tt_doc/doc_txt2"], stderr=subprocess.PIPE)
print("Result SCP transfert : %s" % repr(proc.stderr))
if secproc.stderr == b'':
    print("+ './Backup/Files2' uploaded !")
else:
    print("+ No file to upload !")
    messagebox.showerror("Error", "./Backup/Files2 not uploaded !")


# To copy to ./Backup/Files3
try:
    src3 = r'./patient_agenda/events3/doc_events/fix_agenda/agenda_saved'
    dst3 = r'./Backup/Files3'
    shutil.copy(os.path.join(src3, file), dst3)
except (OSError, FileNotFoundError) as err_3shut:
    print("+ No files from agenda_3 copied !!!", err_3shut)

secproc = subprocess.run(["scp", "-r", "./Backup/Files3",
    "pi@192.168.18.12:~/tt_doc/doc_txt3"], stderr=subprocess.PIPE)
print("Result SCP transfert : %s" % repr(proc.stderr))
if secproc.stderr == b'':
    print("+ './Backup/Files3' uploaded !")
else:
    print("+ No file to upload !")
    messagebox.showerror("Error", "./Backup/Files3 not uploaded !")

# To copy to ./Backup/Files4
try:
    src4 = r'./patient_agenda/events4/doc_events/fix_agenda/agenda_saved'
    dst4 = r'./Backup/Files4'
    shutil.copy(os.path.join(src4, file), dst4)
except (OSError, FileNotFoundError) as err_4shut:
    print("+ No files from agenda_4 copied !!!", err_4shut)

secproc = subprocess.run(["scp", "-r", "./Backup/Files4",
    "pi@192.168.18.12:~/tt_doc/doc_txt4"], stderr=subprocess.PIPE)
print("Result SCP transfert : %s" % repr(proc.stderr))
if secproc.stderr == b'':
    print("+ './Backup/Files4' uploaded !")
else:
    print("+ No file to upload !")
    messagebox.showerror("Error", "./Backup/Files4 not uploaded !")

# To copy to ./Backup/Files5
try:
    src5 = r'./patient_agenda/events5/doc_events/fix_agenda/agenda_saved'
    dst5 = r'./Backup/Files5'
    shutil.copy(os.path.join(src5, file), dst5)
except (OSError, FileNotFoundError) as err_5shut:
    print("+ No files from agenda_5 copied !!!", err_5shut)

secproc = subprocess.run(["scp", "-r", "./Backup/Files5",
    "pi@192.168.18.12:~/tt_doc/doc_txt5"], stderr=subprocess.PIPE)
print("Result SCP transfert : %s" % repr(proc.stderr))
if secproc.stderr == b'':
    print("+ './Backup/Files5' uploaded !")
else:
    print("+ No file to upload !")
    messagebox.showerror("Error", "./Backup/Files5 not uploaded !")

# To copy to ./Backup/Files6
try:
    src6 = r'./patient_agenda/events6/doc_events/fix_agenda/agenda_saved'
    dst6 = r'./Backup/Files6'
    shutil.copy(os.path.join(src6, file), dst6)
except (OSError, FileNotFoundError) as err_6shut:
    print("+ No files from agenda_6 copied !!!", err_6shut)

secproc = subprocess.run(["scp", "-r", "./Backup/Files6",
    "pi@192.168.18.12:~/tt_doc/doc_txt6"], stderr=subprocess.PIPE)
print("Result SCP transfert : %s" % repr(proc.stderr))
if secproc.stderr == b'':
    print("+ './Backup/Files6' uploaded !")
else:
    print("+ No file to upload !")
    messagebox.showerror("Error", "./Backup/Files6 not uploaded !")

# To copy to ./Backup/Files7
try:
    src7 = r'./patient_agenda/events7/doc_events/fix_agenda/agenda_saved'
    dst7 = r'./Backup/Files7'
    shutil.copy(os.path.join(src7, file), dst7)
except (OSError, FileNotFoundError) as err_7shut:
    print("+ No files from agenda_7 copied !!!", err_7shut)

secproc = subprocess.run(["scp", "-r", "./Backup/Files7",
    "pi@192.168.18.12:~/tt_doc/doc_txt7"], stderr=subprocess.PIPE)
print("Result SCP transfert : %s" % repr(proc.stderr))
if secproc.stderr == b'':
    print("+ './Backup/Files7' uploaded !")
else:
    print("+ No file to upload !")
    messagebox.showerror("Error", "./Backup/Files7 not uploaded !")

# To copy to ./Backup/Files8
try:
    src8 = r'./patient_agenda/events8/doc_events/fix_agenda/agenda_saved'
    dst8 = r'./Backup/Files8'
    shutil.copy(os.path.join(src8, file), dst8)
except (OSError, FileNotFoundError) as err_8shut:
    print("+ No files from agenda_8 copied !!!", err_8shut)

secproc = subprocess.run(["scp", "-r", "./Backup/Files8",
    "pi@192.168.18.12:~/tt_doc/doc_txt8"], stderr=subprocess.PIPE)
print("Result SCP transfert : %s" % repr(proc.stderr))
if secproc.stderr == b'':
    print("+ './Backup/Files8' uploaded !")
else:
    print("+ No file to upload !")
    messagebox.showerror("Error", "./Backup/Files8 not uploaded !")

# To copy to ./Backup/Files9
try:
    src9 = r'./patient_agenda/events9/doc_events/fix_agenda/agenda_saved'
    dst9 = r'./Backup/Files9'
    shutil.copy(os.path.join(src9, file), dst9)
except (OSError, FileNotFoundError) as err_9shut:
    print("+ No files from agenda_9 copied !!!", err_9shut)

secproc = subprocess.run(["scp", "-r", "./Backup/Files9",
    "pi@192.168.18.12:~/tt_doc/doc_txt9"], stderr=subprocess.PIPE)
print("Result SCP transfert : %s" % repr(proc.stderr))
if secproc.stderr == b'':
    print("+ './Backup/Files9' uploaded !")
else:
    print("+ No file to upload !")
    messagebox.showerror("Error", "./Backup/Files9 not uploaded !")

# To copy to ./Backup/Files10
try:
    src10 = r'./patient_agenda/events10/doc_events/fix_agenda/agenda_saved'
    dst10 = r'./Backup/Files10'
    shutil.copy(os.path.join(src10, file), dst10)
except (OSError, FileNotFoundError) as err_10shut:
    print("+ No files from agenda_10 copied !!!", err_10shut)

secproc = subprocess.run(["scp", "-r", "./Backup/Files10",
    "pi@192.168.18.12:~/tt_doc/doc_txt10"], stderr=subprocess.PIPE)
print("Result SCP transfert : %s" % repr(proc.stderr))
if secproc.stderr == b'':
    print("+ './Backup/Files10' uploaded !")
else:
    print("+ No file to upload !")
    messagebox.showerror("Error", "./Backup/Files10 not uploaded !")

# To copy to ./Backup/Files11
try:
    src11 = r'./patient_agenda/events11/doc_events/fix_agenda/agenda_saved'
    dst11 = r'./Backup/Files11'
    shutil.copy(os.path.join(src11, file), dst11)
except (OSError, FileNotFoundError) as err_11shut:
    print("+ No files from agenda_11 copied !!!", err_11shut)

secproc = subprocess.run(["scp", "-r", "./Backup/Files11",
    "pi@192.168.18.12:~/tt_doc/doc_txt11"], stderr=subprocess.PIPE)
print("Result SCP transfert : %s" % repr(proc.stderr))
if secproc.stderr == b'':
    print("+ './Backup/Files11' uploaded !")
else:
    print("+ No file to upload !")
    messagebox.showerror("Error", "./Backup/Files11 not uploaded !")

# To copy to ./Backup/Files12
try:
    src12 = r'./patient_agenda/events12/doc_events/fix_agenda/agenda_saved'
    dst12 = r'./Backup/Files12'
    shutil.copy(os.path.join(src12, file), dst12)
except (OSError, FileNotFoundError) as err_12shut:
    print("+ No files from agenda_12 copied !!!", err_12shut)

secproc = subprocess.run(["scp", "-r", "./Backup/Files12",
    "pi@192.168.18.12:~/tt_doc/doc_txt12"], stderr=subprocess.PIPE)
print("Result SCP transfert : %s" % repr(proc.stderr))
if secproc.stderr == b'':
    print("+ './Backup/Files12' uploaded !")
else:
    print("+ No file to upload !")
    messagebox.showerror("Error", "./Backup/Files12 not uploaded !")

# To copy to ./Backup/Files13
try:
    src13 = r'./patient_agenda/events13/doc_events/fix_agenda/agenda_saved'
    dst13 = r'./Backup/Files13'
    shutil.copy(os.path.join(src13, file), dst13)
except (OSError, FileNotFoundError) as err_13shut:
    print("+ No files from agenda_13 copied !!!", err_13shut)

secproc = subprocess.run(["scp", "-r", "./Backup/Files13",
    "pi@192.168.18.12:~/tt_doc/doc_txt13"], stderr=subprocess.PIPE)
print("Result SCP transfert : %s" % repr(proc.stderr))
if secproc.stderr == b'':
    print("+ './Backup/Files13' uploaded !")
else:
    print("+ No file to upload !")
    messagebox.showerror("Error", "./Backup/Files13 not uploaded !")

# To copy to ./Backup/Files14
try:
    src14 = r'./patient_agenda/events14/doc_events/fix_agenda/agenda_saved'
    dst14 = r'./Backup/Files14'
    shutil.copy(os.path.join(src14, file), dst14)
except (OSError, FileNotFoundError) as err_14shut:
    print("+ No files from agenda_14 copied !!!", err_14shut)

secproc = subprocess.run(["scp", "-r", "./Backup/Files14",
    "pi@192.168.18.12:~/tt_doc/doc_txt14"], stderr=subprocess.PIPE)
print("Result SCP transfert : %s" % repr(proc.stderr))
if secproc.stderr == b'':
    print("+ './Backup/Files14' uploaded !")
else:
    print("+ No file to upload !")
    messagebox.showerror("Error", "./Backup/Files14 not uploaded !")

# To copy to ./Backup/Files15
try:
    src15 = r'./patient_agenda/events15/doc_events/fix_agenda/agenda_saved'
    dst15 = r'./Backup/Files15'
    shutil.copy(os.path.join(src15, file), dst15)
except (OSError, FileNotFoundError) as err_15shut:
    print("+ No files from agenda_15 copied !!!", err_15shut)

secproc = subprocess.run(["scp", "-r", "./Backup/Files15",
    "pi@192.168.18.12:~/tt_doc/doc_txt15"], stderr=subprocess.PIPE)
print("Result SCP transfert : %s" % repr(proc.stderr))
if secproc.stderr == b'':
    print("+ './Backup/Files15' uploaded !")
else:
    print("+ No file to upload !")
    messagebox.showerror("Error", "./Backup/Files15 not uploaded !")

# To copy to ./Backup/Files16
try:
    src16 = r'./patient_agenda/events16/doc_events/fix_agenda/agenda_saved'
    dst16 = r'./Backup/Files16'
    shutil.copy(os.path.join(src16, file), dst16)
except (OSError, FileNotFoundError) as err_16shut:
    print("+ No files from agenda_16 copied !!!", err_16shut)

secproc = subprocess.run(["scp", "-r", "./Backup/Files16",
    "pi@192.168.18.12:~/tt_doc/doc_txt16"], stderr=subprocess.PIPE)
print("Result SCP transfert : %s" % repr(proc.stderr))
if secproc.stderr == b'':
    print("+ './Backup/Files16' uploaded !")
else:
    print("+ No file to upload !")
    messagebox.showerror("Error", "./Backup/Files16 not uploaded !")

# To copy to ./Backup/Files17
try:
    src17 = r'./patient_agenda/events17/doc_events/fix_agenda/agenda_saved'
    dst17 = r'./Backup/Files17'
    shutil.copy(os.path.join(src17, file), dst17)
except (OSError, FileNotFoundError) as err_17shut:
    print("+ No files from agenda_17 copied !!!", err_17shut)

secproc = subprocess.run(["scp", "-r", "./Backup/Files17",
    "pi@192.168.18.12:~/tt_doc/doc_txt17"], stderr=subprocess.PIPE)
print("Result SCP transfert : %s" % repr(proc.stderr))
if secproc.stderr == b'':
    print("+ './Backup/Files17' uploaded !")
else:
    print("+ No file to upload !")
    messagebox.showerror("Error", "./Backup/Files17 not uploaded !")

# To copy to ./Backup/Files18
try:
    src18 = r'./patient_agenda/events18/doc_events/fix_agenda/agenda_saved'
    dst18 = r'./Backup/Files18'
    shutil.copy(os.path.join(src18, file), dst18)
except (OSError, FileNotFoundError) as err_18shut:
    print("+ No files from agenda_18 copied !!!", err_18shut)

secproc = subprocess.run(["scp", "-r", "./Backup/Files18",
    "pi@192.168.18.12:~/tt_doc/doc_txt18"], stderr=subprocess.PIPE)
print("Result SCP transfert : %s" % repr(proc.stderr))
if secproc.stderr == b'':
    print("+ './Backup/Files18' uploaded !")
else:
    print("+ No file to upload !")
    messagebox.showerror("Error", "./Backup/Files18 not uploaded !")

# To copy to ./Backup/Files19
try:
    src19 = r'./patient_agenda/events19/doc_events/fix_agenda/agenda_saved'
    dst19 = r'./Backup/Files19'
    shutil.copy(os.path.join(src19, file), dst19)
except (OSError, FileNotFoundError) as err_19shut:
    print("+ No files from agenda_19 copied !!!", err_19shut)

secproc = subprocess.run(["scp", "-r", "./Backup/Files19",
    "pi@192.168.18.12:~/tt_doc/doc_txt19"], stderr=subprocess.PIPE)
print("Result SCP transfert : %s" % repr(proc.stderr))
if secproc.stderr == b'':
    print("+ './Backup/Files19' uploaded !")
else:
    print("+ No file to upload !")
    messagebox.showerror("Error", "./Backup/Files19 not uploaded !")

# To copy to ./Backup/Files20
try:
    src20 = r'./patient_agenda/events20/doc_events/fix_agenda/agenda_saved'
    dst20 = r'./Backup/Files20'
    shutil.copy(os.path.join(src20, file), dst20)
except (OSError, FileNotFoundError) as err_20shut:
    print("+ No files from agenda_20 copied !!!", err_20shut)

secproc = subprocess.run(["scp", "-r", "./Backup/Files20",
    "pi@192.168.18.12:~/tt_doc/doc_txt20"], stderr=subprocess.PIPE)
print("Result SCP transfert : %s" % repr(proc.stderr))
if secproc.stderr == b'':
    print("+ './Backup/Files20' uploaded !")
else:
    print("+ No file to upload !")
    messagebox.showerror("Error", "./Backup/Files20 not uploaded !")

# To copy to ./Backup/Files21
try:
    src21 = r'./patient_agenda/events21/doc_events/fix_agenda/agenda_saved'
    dst21 = r'./Backup/Files21'
    shutil.copy(os.path.join(src21, file), dst21)
except (OSError, FileNotFoundError) as err_21shut:
    print("+ No files from agenda_21 copied !!!", err_21shut)

secproc = subprocess.run(["scp", "-r", "./Backup/Files21",
    "pi@192.168.18.12:~/tt_doc/doc_txt21"], stderr=subprocess.PIPE)
print("Result SCP transfert : %s" % repr(proc.stderr))
if secproc.stderr == b'':
    print("+ './Backup/Files21' uploaded !")
else:
    print("+ No file to upload !")
    messagebox.showerror("Error", "./Backup/Files21 not uploaded !")

# To copy to ./Backup/Files22
try:
    src22 = r'./patient_agenda/events22/doc_events/fix_agenda/agenda_saved'
    dst22 = r'./Backup/Files22'
    shutil.copy(os.path.join(src22, file), dst22)
except (OSError, FileNotFoundError) as err_22shut:
    print("+ No files from agenda_22 copied !!!", err_22shut)

secproc = subprocess.run(["scp", "-r", "./Backup/Files22",
    "pi@192.168.18.12:~/tt_doc/doc_txt22"], stderr=subprocess.PIPE)
print("Result SCP transfert : %s" % repr(proc.stderr))
if secproc.stderr == b'':
    print("+ './Backup/Files22' uploaded !")
else:
    print("+ No file to upload !")
    messagebox.showerror("Error", "./Backup/Files22 not uploaded !")

# To copy to ./Backup/Files23
try:
    src23 = r'./patient_agenda/events23/doc_events/fix_agenda/agenda_saved'
    dst23 = r'./Backup/Files23'
    shutil.copy(os.path.join(src23, file), dst23)
except (OSError, FileNotFoundError) as err_23shut:
    print("+ No files from agenda_23 copied !!!", err_23shut)

secproc = subprocess.run(["scp", "-r", "./Backup/Files23",
    "pi@192.168.18.12:~/tt_doc/doc_txt23"], stderr=subprocess.PIPE)
print("Result SCP transfert : %s" % repr(proc.stderr))
if secproc.stderr == b'':
    print("+ './Backup/Files23' uploaded !")
else:
    print("+ No file to upload !")
    messagebox.showerror("Error", "./Backup/Files23 not uploaded !")

# To copy to ./Backup/Files24
try:
    src24 = r'./patient_agenda/events24/doc_events/fix_agenda/agenda_saved'
    dst24 = r'./Backup/Files24'
    shutil.copy(os.path.join(src24, file), dst24)
except (OSError, FileNotFoundError) as err_24shut:
    print("+ No files from agenda_24 copied !!!", err_24shut)

secproc = subprocess.run(["scp", "-r", "./Backup/Files24",
    "pi@192.168.18.12:~/tt_doc/doc_txt24"], stderr=subprocess.PIPE)
print("Result SCP transfert : %s" % repr(proc.stderr))
if secproc.stderr == b'':
    print("+ './Backup/Files24' uploaded !")
else:
    print("+ No file to upload !")
    messagebox.showerror("Error", "./Backup/Files24 not uploaded !")