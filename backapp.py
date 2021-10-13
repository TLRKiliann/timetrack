#!/usr/bin/python3
# -*- coding: utf-8 -*-


from tkinter import *
import tkinter as tk
from tkinter import filedialog


"""
    To access to backup files
    from the main file time-track.py
    with a GUI self.textbox
"""


def backupFuncPatient(self):
    self.fen = tk.Tk()
    self.fen.title("Search File")
    self.fen.configure(bg='RoyalBlue3')
    filepath = tk.filedialog.askopenfilename(initialdir = "./Backup/Files1",
        title = "Select file", filetypes = (("txt files","*.txt"),("all files","*.*")))
    print(filepath)

    self.textBox = tk.Text(self.fen, height=30, width=60, font=18, relief=tk.SUNKEN)
    self.textBox.pack(padx=30, pady=30)

    try:
        if not filepath:
            self.fen.destroy()
    except Exception as ex_file:
        print("[!] Error unknow", ex_file)

    try:
        with open(filepath, 'r') as fichier:
            content=fichier.readlines()
            for li in content:
                self.textBox.insert(tk.END, li)
    except FileNotFoundError as error_file:
        print("[!] File not found !", error_file)
    except TypeError as type_err:
        print("[!] Type (of files) Error !", type_err)
    except UnboundLocalError as unb_err:
        print("[!] Unbound Local Error", unb_err)

def backupFuncPatient2(self):
    self.fen = tk.Tk()
    self.fen.title("Search File")
    self.fen.configure(bg='RoyalBlue3')
    filepath = tk.filedialog.askopenfilename(initialdir = "./Backup/Files2",
        title = "Select file", filetypes = (("txt files","*.txt"),("all files","*.*")))
    print(filepath)

    self.textBox = tk.Text(self.fen, height=30, width=60, font=18, relief=tk.SUNKEN)
    self.textBox.pack(padx=30, pady=30)

    try:
        if not filepath:
            self.fen.destroy()
    except Exception as ex_file:
        print("[!] Error unknow", ex_file)

    try:
        with open(filepath, 'r') as fichier:
            content=fichier.readlines()
            for li in content:
                self.textBox.insert(tk.END, li)
    except FileNotFoundError as error_file:
        print("[!] File not found !", error_file)
    except TypeError as type_err:
        print("[!] Type (of files) Error !", type_err)
    except UnboundLocalError as unb_err:
        print("[!] Unbound Local Error", unb_err)

def backupFuncPatient3(self):
    self.fen = tk.Tk()
    self.fen.title("Search File")
    self.fen.configure(bg='RoyalBlue3')
    filepath = tk.filedialog.askopenfilename(initialdir = "./Backup/Files3",
        title = "Select file", filetypes = (("txt files","*.txt"),("all files","*.*")))
    print(filepath)

    self.textBox = tk.Text(self.fen, height=30, width=60, font=18, relief=tk.SUNKEN)
    self.textBox.pack(padx=30, pady=30)

    try:
        if not filepath:
            self.fen.destroy()
    except Exception as ex_file:
        print("[!] Error unknow", ex_file)

    try:
        with open(filepath, 'r') as fichier:
            content=fichier.readlines()
            for li in content:
                self.textBox.insert(tk.END, li)
    except FileNotFoundError as error_file:
        print("[!] File not found !", error_file)
    except TypeError as type_err:
        print("[!] Type (of files) Error !", type_err)
    except UnboundLocalError as unb_err:
        print("[!] Unbound Local Error", unb_err)

def backupFuncPatient4(self):
    self.fen = tk.Tk()
    self.fen.title("Search File")
    self.fen.configure(bg='RoyalBlue3')
    filepath = tk.filedialog.askopenfilename(initialdir = "./Backup/Files4",
        title = "Select file", filetypes = (("txt files","*.txt"),("all files","*.*")))
    print(filepath)

    self.textBox = tk.Text(self.fen, height=30, width=60, font=18, relief=tk.SUNKEN)
    self.textBox.pack(padx=30, pady=30)

    try:
        if not filepath:
            self.fen.destroy()
    except Exception as ex_file:
        print("[!] Error unknow", ex_file)

    try:
        with open(filepath, 'r') as fichier:
            content=fichier.readlines()
            for li in content:
                self.textBox.insert(tk.END, li)
    except FileNotFoundError as error_file:
        print("[!] File not found !", error_file)
    except TypeError as type_err:
        print("[!] Type (of files) Error !", type_err)
    except UnboundLocalError as unb_err:
        print("[!] Unbound Local Error", unb_err)

def backupFuncPatient5(self):
    self.fen = tk.Tk()
    self.fen.title("Search File")
    self.fen.configure(bg='RoyalBlue3')
    filepath = tk.filedialog.askopenfilename(initialdir = "./Backup/Files5",
        title = "Select file", filetypes = (("txt files","*.txt"),("all files","*.*")))
    print(filepath)

    self.textBox = tk.Text(self.fen, height=30, width=60, font=18, relief=tk.SUNKEN)
    self.textBox.pack(padx=30, pady=30)

    try:
        if not filepath:
            self.fen.destroy()
    except Exception as ex_file:
        print("[!] Error unknow", ex_file)

    try:
        with open(filepath, 'r') as fichier:
            content=fichier.readlines()
            for li in content:
                self.textBox.insert(tk.END, li)
    except FileNotFoundError as error_file:
        print("[!] File not found !", error_file)
    except TypeError as type_err:
        print("[!] Type (of files) Error !", type_err)
    except UnboundLocalError as unb_err:
        print("[!] Unbound Local Error", unb_err)

def backupFuncPatient6(self):
    self.fen = tk.Tk()
    self.fen.title("Search File")
    self.fen.configure(bg='RoyalBlue3')
    filepath = tk.filedialog.askopenfilename(initialdir = "./Backup/Files6",
        title = "Select file", filetypes = (("txt files","*.txt"),("all files","*.*")))
    print(filepath)

    self.textBox = tk.Text(self.fen, height=30, width=60, font=18, relief=tk.SUNKEN)
    self.textBox.pack(padx=30, pady=30)

    try:
        if not filepath:
            self.fen.destroy()
    except Exception as ex_file:
        print("[!] Error unknow", ex_file)

    try:
        with open(filepath, 'r') as fichier:
            content=fichier.readlines()
            for li in content:
                self.textBox.insert(tk.END, li)
    except FileNotFoundError as error_file:
        print("[!] File not found !", error_file)
    except TypeError as type_err:
        print("[!] Type (of files) Error !", type_err)
    except UnboundLocalError as unb_err:
        print("[!] Unbound Local Error", unb_err)

def backupFuncPatient7(self):
    self.fen = tk.Tk()
    self.fen.title("Search File")
    self.fen.configure(bg='RoyalBlue3')
    filepath = tk.filedialog.askopenfilename(initialdir = "./Backup/Files7",
        title = "Select file", filetypes = (("txt files","*.txt"),("all files","*.*")))
    print(filepath)

    self.textBox = tk.Text(self.fen, height=30, width=60, font=18, relief=tk.SUNKEN)
    self.textBox.pack(padx=30, pady=30)

    try:
        if not filepath:
            self.fen.destroy()
    except Exception as ex_file:
        print("[!] Error unknow", ex_file)

    try:
        with open(filepath, 'r') as fichier:
            content=fichier.readlines()
            for li in content:
                self.textBox.insert(tk.END, li)
    except FileNotFoundError as error_file:
        print("[!] File not found !", error_file)
    except TypeError as type_err:
        print("[!] Type (of files) Error !", type_err)
    except UnboundLocalError as unb_err:
        print("[!] Unbound Local Error", unb_err)

def backupFuncPatient8(self):
    self.fen = tk.Tk()
    self.fen.title("Search File")
    self.fen.configure(bg='RoyalBlue3')
    filepath = tk.filedialog.askopenfilename(initialdir = "./Backup/Files8",
        title = "Select file", filetypes = (("txt files","*.txt"),("all files","*.*")))
    print(filepath)

    self.textBox = tk.Text(self.fen, height=30, width=60, font=18, relief=tk.SUNKEN)
    self.textBox.pack(padx=30, pady=30)

    try:
        if not filepath:
            self.fen.destroy()
    except Exception as ex_file:
        print("[!] Error unknow", ex_file)

    try:
        with open(filepath, 'r') as fichier:
            content=fichier.readlines()
            for li in content:
                self.textBox.insert(tk.END, li)
    except FileNotFoundError as error_file:
        print("[!] File not found !", error_file)
    except TypeError as type_err:
        print("[!] Type (of files) Error !", type_err)
    except UnboundLocalError as unb_err:
        print("[!] Unbound Local Error", unb_err)

def backupFuncPatient9(self):
    self.fen = tk.Tk()
    self.fen.title("Search File")
    self.fen.configure(bg='RoyalBlue3')
    filepath = tk.filedialog.askopenfilename(initialdir = "./Backup/Files9",
        title = "Select file", filetypes = (("txt files","*.txt"),("all files","*.*")))
    print(filepath)

    self.textBox = tk.Text(self.fen, height=30, width=60, font=18, relief=tk.SUNKEN)
    self.textBox.pack(padx=30, pady=30)

    try:
        if not filepath:
            self.fen.destroy()
    except Exception as ex_file:
        print("[!] Error unknow", ex_file)

    try:
        with open(filepath, 'r') as fichier:
            content=fichier.readlines()
            for li in content:
                self.textBox.insert(tk.END, li)
    except FileNotFoundError as error_file:
        print("[!] File not found !", error_file)
    except TypeError as type_err:
        print("[!] Type (of files) Error !", type_err)
    except UnboundLocalError as unb_err:
        print("[!] Unbound Local Error", unb_err)

def backupFuncPatient10(self):
    self.fen = tk.Tk()
    self.fen.title("Search File")
    self.fen.configure(bg='RoyalBlue3')
    filepath = tk.filedialog.askopenfilename(initialdir = "./Backup/Files10",
        title = "Select file", filetypes = (("txt files","*.txt"),("all files","*.*")))
    print(filepath)

    self.textBox = tk.Text(self.fen, height=30, width=60, font=18, relief=tk.SUNKEN)
    self.textBox.pack(padx=30, pady=30)

    try:
        if not filepath:
            self.fen.destroy()
    except Exception as ex_file:
        print("[!] Error unknow", ex_file)

    try:
        with open(filepath, 'r') as fichier:
            content=fichier.readlines()
            for li in content:
                self.textBox.insert(tk.END, li)
    except FileNotFoundError as error_file:
        print("[!] File not found !", error_file)
    except TypeError as type_err:
        print("[!] Type (of files) Error !", type_err)
    except UnboundLocalError as unb_err:
        print("[!] Unbound Local Error", unb_err)

def backupFuncPatient11(self):
    self.fen = tk.Tk()
    self.fen.title("Search File")
    self.fen.configure(bg='RoyalBlue3')
    filepath = tk.filedialog.askopenfilename(initialdir = "./Backup/Files11",
        title = "Select file", filetypes = (("txt files","*.txt"),("all files","*.*")))
    print(filepath)

    self.textBox = tk.Text(self.fen, height=30, width=60, font=18, relief=tk.SUNKEN)
    self.textBox.pack(padx=30, pady=30)

    try:
        if not filepath:
            self.fen.destroy()
    except Exception as ex_file:
        print("[!] Error unknow", ex_file)

    try:
        with open(filepath, 'r') as fichier:
            content=fichier.readlines()
            for li in content:
                self.textBox.insert(tk.END, li)
    except FileNotFoundError as error_file:
        print("[!] File not found !", error_file)
    except TypeError as type_err:
        print("[!] Type (of files) Error !", type_err)
    except UnboundLocalError as unb_err:
        print("[!] Unbound Local Error", unb_err)

def backupFuncPatient12(self):
    self.fen = tk.Tk()
    self.fen.title("Search File")
    self.fen.configure(bg='RoyalBlue3')
    filepath = tk.filedialog.askopenfilename(initialdir = "./Backup/Files12",
        title = "Select file", filetypes = (("txt files","*.txt"),("all files","*.*")))
    print(filepath)

    self.textBox = tk.Text(self.fen, height=30, width=60, font=18, relief=tk.SUNKEN)
    self.textBox.pack(padx=30, pady=30)

    try:
        if not filepath:
            self.fen.destroy()
    except Exception as ex_file:
        print("[!] Error unknow", ex_file)

    try:
        with open(filepath, 'r') as fichier:
            content=fichier.readlines()
            for li in content:
                self.textBox.insert(tk.END, li)
    except FileNotFoundError as error_file:
        print("[!] File not found !", error_file)
    except TypeError as type_err:
        print("[!] Type (of files) Error !", type_err)
    except UnboundLocalError as unb_err:
        print("[!] Unbound Local Error", unb_err)

def backupFuncPatient13(self):
    self.fen = tk.Tk()
    self.fen.title("Search File")
    self.fen.configure(bg='RoyalBlue3')
    filepath = tk.filedialog.askopenfilename(initialdir = "./Backup/Files13",
        title = "Select file", filetypes = (("txt files","*.txt"),("all files","*.*")))
    print(filepath)

    self.textBox = tk.Text(self.fen, height=30, width=60, font=18, relief=tk.SUNKEN)
    self.textBox.pack(padx=30, pady=30)

    try:
        if not filepath:
            self.fen.destroy()
    except Exception as ex_file:
        print("[!] Error unknow", ex_file)

    try:
        with open(filepath, 'r') as fichier:
            content=fichier.readlines()
            for li in content:
                self.textBox.insert(tk.END, li)
    except FileNotFoundError as error_file:
        print("[!] File not found !", error_file)
    except TypeError as type_err:
        print("[!] Type (of files) Error !", type_err)
    except UnboundLocalError as unb_err:
        print("[!] Unbound Local Error", unb_err)

def backupFuncPatient14(self):
    self.fen = tk.Tk()
    self.fen.title("Search File")
    self.fen.configure(bg='RoyalBlue3')
    filepath = tk.filedialog.askopenfilename(initialdir = "./Backup/Files14",
        title = "Select file", filetypes = (("txt files","*.txt"),("all files","*.*")))
    print(filepath)

    self.textBox = tk.Text(self.fen, height=30, width=60, font=18, relief=tk.SUNKEN)
    self.textBox.pack(padx=30, pady=30)

    try:
        if not filepath:
            self.fen.destroy()
    except Exception as ex_file:
        print("[!] Error unknow", ex_file)

    try:
        with open(filepath, 'r') as fichier:
            content=fichier.readlines()
            for li in content:
                self.textBox.insert(tk.END, li)
    except FileNotFoundError as error_file:
        print("[!] File not found !", error_file)
    except TypeError as type_err:
        print("[!] Type (of files) Error !", type_err)
    except UnboundLocalError as unb_err:
        print("[!] Unbound Local Error", unb_err)

def backupFuncPatient15(self):
    self.fen = tk.Tk()
    self.fen.title("Search File")
    self.fen.configure(bg='RoyalBlue3')
    filepath = tk.filedialog.askopenfilename(initialdir = "./Backup/Files15",
        title = "Select file", filetypes = (("txt files","*.txt"),("all files","*.*")))
    print(filepath)

    self.textBox = tk.Text(self.fen, height=30, width=60, font=18, relief=tk.SUNKEN)
    self.textBox.pack(padx=30, pady=30)

    try:
        if not filepath:
            self.fen.destroy()
    except Exception as ex_file:
        print("[!] Error unknow", ex_file)

    try:
        with open(filepath, 'r') as fichier:
            content=fichier.readlines()
            for li in content:
                self.textBox.insert(tk.END, li)
    except FileNotFoundError as error_file:
        print("[!] File not found !", error_file)
    except TypeError as type_err:
        print("[!] Type (of files) Error !", type_err)
    except UnboundLocalError as unb_err:
        print("[!] Unbound Local Error", unb_err)

def backupFuncPatient16(self):
    self.fen = tk.Tk()
    self.fen.title("Search File")
    self.fen.configure(bg='RoyalBlue3')
    filepath = tk.filedialog.askopenfilename(initialdir = "./Backup/Files16",
        title = "Select file", filetypes = (("txt files","*.txt"),("all files","*.*")))
    print(filepath)

    self.textBox = tk.Text(self.fen, height=30, width=60, font=18, relief=tk.SUNKEN)
    self.textBox.pack(padx=30, pady=30)

    try:
        if not filepath:
            self.fen.destroy()
    except Exception as ex_file:
        print("[!] Error unknow", ex_file)

    try:
        with open(filepath, 'r') as fichier:
            content=fichier.readlines()
            for li in content:
                self.textBox.insert(tk.END, li)
    except FileNotFoundError as error_file:
        print("[!] File not found !", error_file)
    except TypeError as type_err:
        print("[!] Type (of files) Error !", type_err)
    except UnboundLocalError as unb_err:
        print("[!] Unbound Local Error", unb_err)

def backupFuncPatient17(self):
    self.fen = tk.Tk()
    self.fen.title("Search File")
    self.fen.configure(bg='RoyalBlue3')
    filepath = tk.filedialog.askopenfilename(initialdir = "./Backup/Files17",
        title = "Select file", filetypes = (("txt files","*.txt"),("all files","*.*")))
    print(filepath)

    self.textBox = tk.Text(self.fen, height=30, width=60, font=18, relief=tk.SUNKEN)
    self.textBox.pack(padx=30, pady=30)

    try:
        if not filepath:
            self.fen.destroy()
    except Exception as ex_file:
        print("[!] Error unknow", ex_file)

    try:
        with open(filepath, 'r') as fichier:
            content=fichier.readlines()
            for li in content:
                self.textBox.insert(tk.END, li)
    except FileNotFoundError as error_file:
        print("[!] File not found !", error_file)
    except TypeError as type_err:
        print("[!] Type (of files) Error !", type_err)
    except UnboundLocalError as unb_err:
        print("[!] Unbound Local Error", unb_err)

def backupFuncPatient18(self):
    self.fen = tk.Tk()
    self.fen.title("Search File")
    self.fen.configure(bg='RoyalBlue3')
    filepath = tk.filedialog.askopenfilename(initialdir = "./Backup/Files18",
        title = "Select file", filetypes = (("txt files","*.txt"),("all files","*.*")))
    print(filepath)

    self.textBox = tk.Text(self.fen, height=30, width=60, font=18, relief=tk.SUNKEN)
    self.textBox.pack(padx=30, pady=30)

    try:
        if not filepath:
            self.fen.destroy()
    except Exception as ex_file:
        print("[!] Error unknow", ex_file)

    try:
        with open(filepath, 'r') as fichier:
            content=fichier.readlines()
            for li in content:
                self.textBox.insert(tk.END, li)
    except FileNotFoundError as error_file:
        print("[!] File not found !", error_file)
    except TypeError as type_err:
        print("[!] Type (of files) Error !", type_err)
    except UnboundLocalError as unb_err:
        print("[!] Unbound Local Error", unb_err)

def backupFuncPatient19(self):
    self.fen = tk.Tk()
    self.fen.title("Search File")
    self.fen.configure(bg='RoyalBlue3')
    filepath = tk.filedialog.askopenfilename(initialdir = "./Backup/Files19",
        title = "Select file", filetypes = (("txt files","*.txt"),("all files","*.*")))
    print(filepath)

    self.textBox = tk.Text(self.fen, height=30, width=60, font=18, relief=tk.SUNKEN)
    self.textBox.pack(padx=30, pady=30)

    try:
        if not filepath:
            self.fen.destroy()
    except Exception as ex_file:
        print("[!] Error unknow", ex_file)

    try:
        with open(filepath, 'r') as fichier:
            content=fichier.readlines()
            for li in content:
                self.textBox.insert(tk.END, li)
    except FileNotFoundError as error_file:
        print("[!] File not found !", error_file)
    except TypeError as type_err:
        print("[!] Type (of files) Error !", type_err)
    except UnboundLocalError as unb_err:
        print("[!] Unbound Local Error", unb_err)

def backupFuncPatient20(self):
    self.fen = tk.Tk()
    self.fen.title("Search File")
    self.fen.configure(bg='RoyalBlue3')
    filepath = tk.filedialog.askopenfilename(initialdir = "./Backup/Files20",
        title = "Select file", filetypes = (("txt files","*.txt"),("all files","*.*")))
    print(filepath)

    self.textBox = tk.Text(self.fen, height=30, width=60, font=18, relief=tk.SUNKEN)
    self.textBox.pack(padx=30, pady=30)

    try:
        if not filepath:
            self.fen.destroy()
    except Exception as ex_file:
        print("[!] Error unknow", ex_file)

    try:
        with open(filepath, 'r') as fichier:
            content=fichier.readlines()
            for li in content:
                self.textBox.insert(tk.END, li)
    except FileNotFoundError as error_file:
        print("[!] File not found !", error_file)
    except TypeError as type_err:
        print("[!] Type (of files) Error !", type_err)
    except UnboundLocalError as unb_err:
        print("[!] Unbound Local Error", unb_err)

def backupFuncPatient21(self):
    self.fen = tk.Tk()
    self.fen.title("Search File")
    self.fen.configure(bg='RoyalBlue3')
    filepath = tk.filedialog.askopenfilename(initialdir = "./Backup/Files21",
        title = "Select file", filetypes = (("txt files","*.txt"),("all files","*.*")))
    print(filepath)

    self.textBox = tk.Text(self.fen, height=30, width=60, font=18, relief=tk.SUNKEN)
    self.textBox.pack(padx=30, pady=30)

    try:
        if not filepath:
            self.fen.destroy()
    except Exception as ex_file:
        print("[!] Error unknow", ex_file)

    try:
        with open(filepath, 'r') as fichier:
            content=fichier.readlines()
            for li in content:
                self.textBox.insert(tk.END, li)
    except FileNotFoundError as error_file:
        print("[!] File not found !", error_file)
    except TypeError as type_err:
        print("[!] Type (of files) Error !", type_err)
    except UnboundLocalError as unb_err:
        print("[!] Unbound Local Error", unb_err)

def backupFuncPatient22(self):
    self.fen = tk.Tk()
    self.fen.title("Search File")
    self.fen.configure(bg='RoyalBlue3')
    filepath = tk.filedialog.askopenfilename(initialdir = "./Backup/Files22",
        title = "Select file", filetypes = (("txt files","*.txt"),("all files","*.*")))
    print(filepath)

    self.textBox = tk.Text(self.fen, height=30, width=60, font=18, relief=tk.SUNKEN)
    self.textBox.pack(padx=30, pady=30)

    try:
        if not filepath:
            self.fen.destroy()
    except Exception as ex_file:
        print("[!] Error unknow", ex_file)

    try:
        with open(filepath, 'r') as fichier:
            content=fichier.readlines()
            for li in content:
                self.textBox.insert(tk.END, li)
    except FileNotFoundError as error_file:
        print("[!] File not found !", error_file)
    except TypeError as type_err:
        print("[!] Type (of files) Error !", type_err)
    except UnboundLocalError as unb_err:
        print("[!] Unbound Local Error", unb_err)

def backupFuncPatient23(self):
    self.fen = tk.Tk()
    self.fen.title("Search File")
    self.fen.configure(bg='RoyalBlue3')
    filepath = tk.filedialog.askopenfilename(initialdir = "./Backup/Files23",
        title = "Select file", filetypes = (("txt files","*.txt"),("all files","*.*")))
    print(filepath)

    self.textBox = tk.Text(self.fen, height=30, width=60, font=18, relief=tk.SUNKEN)
    self.textBox.pack(padx=30, pady=30)

    try:
        if not filepath:
            self.fen.destroy()
    except Exception as ex_file:
        print("[!] Error unknow", ex_file)

    try:
        with open(filepath, 'r') as fichier:
            content=fichier.readlines()
            for li in content:
                self.textBox.insert(tk.END, li)
    except FileNotFoundError as error_file:
        print("[!] File not found !", error_file)
    except TypeError as type_err:
        print("[!] Type (of files) Error !", type_err)
    except UnboundLocalError as unb_err:
        print("[!] Unbound Local Error", unb_err)

def backupFuncPatient24(self):
    self.fen = tk.Tk()
    self.fen.title("Search File")
    self.fen.configure(bg='RoyalBlue3')
    filepath = tk.filedialog.askopenfilename(initialdir = "./Backup/Files24",
        title = "Select file", filetypes = (("txt files","*.txt"),("all files","*.*")))
    print(filepath)

    self.textBox = tk.Text(self.fen, height=30, width=60, font=18, relief=tk.SUNKEN)
    self.textBox.pack(padx=30, pady=30)

    try:
        if not filepath:
            self.fen.destroy()
    except Exception as ex_file:
        print("[!] Error unknow", ex_file)

    try:
        with open(filepath, 'r') as fichier:
            content=fichier.readlines()
            for li in content:
                self.textBox.insert(tk.END, li)
    except FileNotFoundError as error_file:
        print("[!] File not found !", error_file)
    except TypeError as type_err:
        print("[!] Type (of files) Error !", type_err)
    except UnboundLocalError as unb_err:
        print("[!] Unbound Local Error", unb_err)
