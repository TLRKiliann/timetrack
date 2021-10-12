#!/usr/bin/python3
# -*- coding:utf-8 -*-


from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import time
import subprocess


app = tk.Tk()
app.title("Stix")
app.configure(bg='gray17')

def saveMyButt():
    MsgBox = messagebox.askyesno('Record', 'Results will be saved into Care and Monitoring, ok ?')
    if MsgBox == 1:
        print("Ok data saved")
        recordOption()
        uploadata()
        confRec()
        app.destroy()
    else:
        messagebox.showinfo('Return', 'Data have not been saved !')

def recordOption():
    print("+ Date : " + time.strftime("%d/%m/%Y"))
    print("+ Nom du patient : ", textName.get())
    with open('./need/doc_suivi8/patient8_14b.txt', 'a+') as file:
        with open('./labo/doc_labo/result8.txt', 'a+') as file_2:
            file.write("\n***************************************"\
                "************************************\n")
            file.write("Date : ")
            file.write(time.strftime("%d/%m/%Y") + '\n')
            file.write("Patient name : ")
            file.write(textName.get() + '\n')
            file.write("pH :")
            file.write(phchoosen.get() + '\n')
            file.write("Leuco :")
            file.write(Leuchoosen.get() + '\n')
            file.write("Nit :")
            file.write(Nitchoosen.get() + '\n')
            file.write("Pro :")
            file.write(Prochoosen.get() + '\n')
            file.write("Glu :")
            file.write(Gluchoosen.get() + '\n')
            file.write("Ket :")
            file.write(Ketchoosen.get() + '\n')
            file.write("Ery :")
            file.write(Erychoosen.get() + '\n')
            file.write("Hb :")
            file.write(Hbchoosen.get() + '\n')
            file.write("****************************************"\
                "***********************************\n\n")
            file_2.write("\n\n***********************************"\
                "****************************************\n")
            file_2.write("Date : ")
            file_2.write(time.strftime("%d/%m/%Y") + '\n')
            file_2.write("Patient name : ")
            file_2.write(textName.get() + ' |')
            file_2.write("pH :")
            file_2.write(phchoosen.get() + ' |')
            file_2.write(" Leuco :")
            file_2.write(Leuchoosen.get() + ' |')
            file_2.write(" Nit :")
            file_2.write(Nitchoosen.get() + ' |')
            file_2.write(" Pro :")
            file_2.write(Prochoosen.get() + ' |')
            file_2.write(" Glu :")
            file_2.write(Gluchoosen.get() + ' |')
            file_2.write(" Ket :")
            file_2.write(Ketchoosen.get() + ' |')
            file_2.write(" Ery :")
            file_2.write(Erychoosen.get() + ' |')
            file_2.write(" Hb :")
            file_2.write(Hbchoosen.get() + ' |')
            file_2.write("\n***********************************"\
                "****************************************\n\n")

def uploadata():
    """
        To upload data on server after creating files
    """
    proc = subprocess.run(["scp", "./need/doc_suivi8/patient8_14b.txt",
        "pi@192.168.18.12:~/tt_doc/doc_txt8/Files8/patient8_14b.txt"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File patient8_14b.txt uploaded !")
        messagebox.showinfo("INFO", "patient8_14b.txt uploaded...")
    else:
        print("+ No file to upload !")
        messagebox.showerror("Error", "No patient8_14b.txt to upload...")

    secproc = subprocess.run(["scp", "./labo/doc_labo/result8.txt",
        "pi@192.168.18.12:~/tt_doc/doc_txt8/Files8/result8.txt"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("+ File result8.txt uploaded !")
        messagebox.showinfo("INFO", "result8.txt uploaded...")
    else:
        print("+ No file to upload !")
        messagebox.showerror("Error", "No result8.txt to upload...")

def confRec():
    messagebox.showinfo("Confirmation", "Record confirmed and finished !")

ttk.Label(app, text="Stix", font=("Times 28 bold"), foreground='aquamarine',
    background='gray17').grid(row=0, column=1, columnspan=4)

# To read name of patient for entry widget
with open('./newpatient/entryfile8.txt', 'r') as filename:
    line1 = filename.readline()

textName = tk.Entry(app)
name_text = tk.StringVar()
textName = tk.Entry(textvariable=name_text,
    highlightbackground='gray', bd=4)
name_text.set(line1[:-1])
textName.grid(row=0, column=4, columnspan=8)

# ttk.Label
ttk.Label(app, text="pH :",
    font=("Times New Roman", 12), foreground='cyan', background='gray17',
    width=5).grid(column=1, row=1, padx=10)

n = tk.StringVar()
phchoosen = ttk.Combobox(app, width=5, textvariable = n)

# Adding ttk.combobox drop down list
phchoosen['values'] = (' 5',
    ' 6',
    ' 7',
    ' 8',
    ' 9')

phchoosen.grid(row=2, column=1)
phchoosen.current(0)

ttk.Label(app, text="Leu :",
    font=("Times New Roman", 12), foreground='cyan',
    background='gray17', width=5).grid(column=2,
    row=1, padx=10)

Leuco = tk.StringVar()
Leuchoosen = ttk.Combobox(app, width=5, textvariable = Leuco)
Leuchoosen['values'] = (' 0',
    ' +1',
    ' +2',
    ' +3')

Leuchoosen.grid(row=2, column=2)
Leuchoosen.current(0)

ttk.Label(app, text="Nit :",
    font=("Times New Roman", 12), foreground='cyan',
    background='gray17', width=5).grid(column=3,
    row=1, padx=10)

Nit = tk.StringVar()
Nitchoosen = ttk.Combobox(app, width=5, textvariable = Nit)
Nitchoosen['values'] = (' -', ' +')

Nitchoosen.grid(row=2, column=3)
Nitchoosen.current(0)

ttk.Label(app, text="Pro :",
    font=("Times New Roman", 12), foreground='cyan',
    background='gray17', width=5).grid(column=4,
    row=1, padx=10)

Pro = tk.StringVar()
Prochoosen = ttk.Combobox(app, width=5, textvariable = Pro)
Prochoosen['values'] = (' neg', ' +1', ' +2', ' +3')

Prochoosen.grid(row=2, column=4)
Prochoosen.current(0)

ttk.Label(app, text="Glu :",
    font=("Times New Roman", 12), foreground='cyan',
    background='gray17', width=5).grid(column=5,
    row=1, padx=10)

Glu = tk.StringVar()
Gluchoosen = ttk.Combobox(app, width=5, textvariable = Glu)
Gluchoosen['values'] = (' neg', ' +1', ' +2', ' +3', ' +4')

Gluchoosen.grid(row=2, column=5)
Gluchoosen.current(0)

ttk.Label(app, text="Ket :",
    font=("Times New Roman", 12), foreground='cyan',
    background='gray17', width=5).grid(column=6,
    row=1, padx=10)

Ket = tk.StringVar()
Ketchoosen = ttk.Combobox(app, width=5, textvariable = Ket)
Ketchoosen['values'] = (' neg', ' +1', ' +2', ' +3')

Ketchoosen.grid(row=2, column=6)
Ketchoosen.current(0)

ttk.Label(app, text="Ery :",
    font=("Times New Roman", 12), foreground='cyan',
    background='gray17', width=5).grid(column=7,
    row=1, padx=10)

Ery = tk.StringVar()
Erychoosen = ttk.Combobox(app, width=5, textvariable = Ery)

Erychoosen['values'] = (' neg',
    ' +1',
    ' +2',
    ' +3',
    ' +4')

Erychoosen.grid(row=2, column=7)
Erychoosen.current(0)

ttk.Label(app, text="Hb :",
    font=("Times New Roman", 12), foreground='cyan',
    background='gray17', width=5).grid(column=8,
    row=1, padx=10)

Hb = tk.StringVar()
Hbchoosen = ttk.Combobox(app, width=5, textvariable = Hb)

# Adding ttk.combobox drop down list
Hbchoosen['values'] = (' neg',
    ' +1',
    ' +2',
    ' +3',
    ' +4')

Hbchoosen.grid(row=2, column=8)
Hbchoosen.current(0)

buttSave=tk.Button(app, text='Save', width=8, bd=3,
    fg='cyan', bg='RoyalBlue3',
    activebackground='pale turquoise',
    highlightbackground='grey17', command=saveMyButt)
buttSave.grid(row=2, column=9, padx=10)

buttQuit=tk.Button(app, text='Quit', width=8, bd=3,
    fg='white', bg='RoyalBlue3',
    activebackground='pale turquoise',
    highlightbackground='grey17', command=quit)
buttQuit.grid(row=3, column=9, padx=10, pady=10)

app.mainloop()
