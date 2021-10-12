#!/usr/bin/python3
# -*- coding: utf-8 -*-


from tkinter import *
from tkinter import messagebox
import sys


def importationFile(fichier, encodage="Utf-8"):
    file = open(fichier, 'r', encoding=encodage)
    print("The size of bits for file is : ",
    sys.getsizeof(file), "bits") 
    content = file.readlines()
    print("The size of bits for content is : ",
    sys.getsizeof(content), "bits") 
    file.close()
    for li in content:
        textBox.insert(END, li)

def msgBox():
    messagebox.showinfo('Info', 'File bmi.txt does not exist')

fen=Tk()
print("The size of bits for fen is : ",
    sys.getsizeof(fen), "bits") 
fen.title("BMI results")
fen.configure(background='RoyalBlue4')

# To place side by side labelo + entrylab
top = Frame(fen, bg='RoyalBlue4')
print("The size of bits for top is : ",
    sys.getsizeof(top), "bits") 
bottom = Frame(fen, bg='RoyalBlue4')
top.pack(side=TOP)
bottom.pack(side=BOTTOM, fill=BOTH, expand=YES)

labelo=Label(fen, text="BMI results : ", width=15,
    font='Times 18 bold', fg='cyan', bg='RoyalBlue4')
labelo.pack(in_=top, side=LEFT, pady=20)
print("The size of bits for labelo is : ",
    sys.getsizeof(labelo), "bits") 

labelallergy=Label(fen, text="Allergy",
    font='Arial 18 bold', fg='coral', bg='RoyalBlue4')
labelallergy.pack(padx=5, pady=5)

# To read name in Entry widget
with open('./newpatient/entryfile.txt', 'r') as filename:
    line1=filename.readline()

text_name=StringVar()
print("The size of bits for text_name is : ",
    sys.getsizeof(text_name), "bits") 
text_name.set(line1)
print("The size of bits for text_name is : ",
    sys.getsizeof(text_name), "bits") 
Entryname=Entry(fen, textvariable=text_name)
print("The size of bits for Entryname is : ",
    sys.getsizeof(Entryname), "bits")
Entryname.pack(in_=top, side=LEFT, pady=20)

# To read allergy in Entry widget
with open('./newpatient/entryfile.txt', 'r') as allerfile:
    lineA1=allerfile.readline()
    print("The size of bits for lineA1 is : ",
    sys.getsizeof(lineA1), "bits") 
    lineA2=allerfile.readline()
    print("The size of bits for lineA2 is : ",
    sys.getsizeof(lineA2), "bits") 
    lineA3=allerfile.readline()
    print("The size of bits for variable lineA3 is : ",
    sys.getsizeof(lineA3), "bits")

text_all=StringVar()
print("The size of bits for text_all StringVar is : ",
    sys.getsizeof(text_all), "bits") 
text_all.set(lineA3)
print("The size of bits for text_all.set(lineA3) is : ",
    sys.getsizeof(text_all.set(lineA3)), "bits") 
Entryall=Entry(fen, textvariable=text_all, width=60)
Entryall.pack(padx=10, pady=5)

print("The size of bits for variable Entryall is : ",
    sys.getsizeof(Entryall.pack()), "bits")

print("The size of bits for text_all is : ",
    sys.getsizeof(text_all), "bits") 

textBox=Text(fen, height=15, width=60, font=18)
textBox.pack(padx=30, pady=30)

buttonClose=Button(fen, text="Quit", width=10, fg='cyan', 
    bg='gray30', activebackground='dark turquoise', 
    activeforeground='navy', command=quit)
buttonClose.pack(side='right', padx=10, pady=10)

try:
    importationFile('./calBmi/bmi.txt', encodage="Utf-8")
except FileNotFoundError as error_call:
    print("+ Import bmi.txt for " + line1 + " failed !")
    msgBox()

print("The size of bits for importationFile('./calBmi/bmi.txt') is : ",
    sys.getsizeof(importationFile('./calBmi/bmi.txt')), "bits") 

print("The size of bits for line1 is : ",
    sys.getsizeof(line1), "bits") 

fen.mainloop()
