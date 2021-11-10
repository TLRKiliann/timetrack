#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
    App for many doing severals interactions
    with a MySQL database in python code.
    Install python3-pymysql on your workstation
    at first. Not in your virtualenv 
    (otherwise doesn't work)!
    > sudo apt install python3-pymysql
    then install pymysql into your virtualenv.
    > pip3 install pymysql or PyMySQL
"""


import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
try:
    import pymysql
    pymysql.install_as_MySQLdb()
except ImportError as err_report:
    print("[!] An error occured about pymysql - accessDB.py [!]", err_report)
    pass


class ScrollCanvas(tk.Frame):
    """
        To prepare ScrollBar for main application.
    """
    def __init__(self, boss=None):
        tk.Frame.__init__(self, borderwidth=borderwidth, relief=relief)

        self.can = tk.Canvas(self, width=width, height=height, bd=bd,
            bg=bg, relief=relief)
        self.frame = tk.Frame(self.can)

        self.vsb = tk.Scrollbar(self, orient=tk.VERTICAL, command=self.can.yview)
        self.can.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(side=tk.RIGHT, fill=tk.Y)
        self.can.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        self.can.create_window((4,4), window=self.frame, anchor=tk.NW,
            tags="self.frame")

        self.frame.bind("<Configure>", self.onFrameConfigure)

class TrackDB(tk.Frame):
    """
        Main app for displaying
        data from mysql database
    """
    def __init__(self, boss=None):
        tk.Frame.__init__(self, borderwidth=5, bg='RoyalBlue4',
            padx=20, pady=20, relief=tk.GROOVE)
        self.master.title('Times-Track DataBase Viewer')

        self.can = tk.Canvas(self, width=1250, height=800, bg='white')
        self.frame = tk.Frame(self.can)

        self.vsb = tk.Scrollbar(self, orient=tk.VERTICAL,
            command=self.can.yview)
        self.can.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(side=tk.RIGHT, fill=tk.Y)

        self.can.create_window((4,4), window=self.frame,
            anchor=tk.NW, tags="self.frame")

        self.frame.bind("<Configure>", self.onFrameConfigure)
        self.can.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        ID = tk.StringVar()
        Firstname = tk.StringVar()
        Surname = tk.StringVar()
        Date_of_Birth = tk.StringVar()
        Allergy = tk.StringVar()
        Transmissible_Disease = tk.StringVar()
        Diagnostic = tk.StringVar()

        def searchDB():
            """
                To connect and search data from mysql
                and build a Treeview() with var and val.
                Configuration for mysql on your own machine:
                sqlCon = pymysql.connect(host='127.0.0.1', user='koala33',
                password='Ko@l@tr3379', database='timetrackconn')
                (no port needed)
            """
            try:
                sqlCon = pymysql.connect(host='192.168.18.12', port=3306, user='koala33',
                    password='Ko@l@tr3379', database='timetrackconn')
                print("\n[AccessDB] Step 1 : Connection to DB - OK")
                cur = sqlCon.cursor()
                print("[AccessDB] Step 2 : Connection cursor with DB - OK")
                cur.execute("SELECT * from timetrackconn")
                print("[AccessDB] Step 3 : Select all from DB - OK")
                result = cur.fetchall()
                print("[AccessDB] Step 4 : Cursor to fetchall in DB - OK")
                if len(result) != 0:
                    self.datatt_records.delete(*self.datatt_records.get_children())
                    for row in result:
                        self.datatt_records.insert('', tk.END, values = row)
                    sqlCon.commit()
                sqlCon.close()
                print("[AccessDB] Step 5 : Sounds good ! Everything works with SQL DB !\n")
            except:
                tk.messagebox.showwarning('Warning', 'Database no connected !')
                print("\n[AccessDB] Database no connected [!]")
        self.datatt_records = ttk.Treeview(self.can, height=24, columns=("stdid",
            "firstname", "surname", "birth", "allergy", "disease", "maindiagnostic"))

        # Headers
        self.datatt_records.heading("stdid", text="ID")
        self.datatt_records.heading("firstname", text="Firstname")
        self.datatt_records.heading("surname", text="Surname")
        self.datatt_records.heading("birth", text="Date_of_Birth")
        self.datatt_records.heading("allergy", text="Allergy")
        self.datatt_records.heading("disease", text="Transmissible_Disease")
        self.datatt_records.heading("maindiagnostic", text="Diagnostic")

        self.datatt_records['show']="headings"

        # Columns
        self.datatt_records.column("stdid", width=75)
        self.datatt_records.column("firstname", width=150)
        self.datatt_records.column("surname", width=150)
        self.datatt_records.column("birth", width=125)
        self.datatt_records.column("allergy", width=200)
        self.datatt_records.column("disease", width=200)
        self.datatt_records.column("maindiagnostic", width=200)

        self.datatt_records.pack(fill=tk.BOTH, expand=1)

        # Button refresh
        self.btnSearch = tk.Button(self.can, text="Refresh Data",
            font=('arial', 12, 'bold'), padx=8, width=16, height=1,
            fg='white', bg='RoyalBlue4', bd=3,  activebackground='cyan',
            activeforeground='RoyalBlue3', highlightbackground="white",
            command=searchDB)
        self.btnSearch.pack(side=tk.LEFT)

        # Button quit
        self.butBox = tk.Button(self.can, text="Return To App", font=('arial', 12, 'bold'),
            padx=8, width=16, height=1, fg='white', bg='RoyalBlue4', bd=3,
            activebackground='cyan', activeforeground='RoyalBlue3',
            highlightbackground='white', command=quit)
        self.butBox.pack(side=tk.RIGHT)
        self.pack()
        searchDB()

    def onFrameConfigure(self, event):
        """
            Reset the scroll region to encompass the inner frame
            and configure canvas for MouseWheel.
        """
        self.can.configure(scrollregion=self.can.bbox(tk.ALL))
        self.can.unbind_all("<Button-4>")
        self.can.unbind_all("<Button-5>")

if __name__=='__main__':
    gui = tk.Tk()
    gui.resizable(False, False)
    TrackDB(gui).pack()
    gui.mainloop()
