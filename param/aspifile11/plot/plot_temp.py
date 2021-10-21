#!/usr/bin/python3
# -*- coding: utf-8 -*-


import os
import json
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


print("\nListe1 = dates :")
print("--------------")

try:
    fileO = open('./param/aspifile11/data_datetemp.json')
    list1 = json.load(fileO)
except ValueError as err_entry:
    print("[!] Value Error", err_entry)

try:
    for obj in list1:
        print("list1: " + obj)
except NameError as err_list:
    print("[!] Name Error list", err_list)

print("\nList2 = temperatures :")
print("--------------------")

try:
    file1 = open('./param/aspifile11/data_temp.json')
    list2 = json.load(file1)
except ValueError as err_entry2:
    print("[!] Value Error", err_entry2)

try:
    for obj in list2:
        print("List2: " + obj)
except NameError as err_list2:
    print("[!] Name Error list2", err_list2)

dicolist = {}

try:
    for list1, list2 in zip(list1, list2):
        dicolist[list1] = list2
except NameError as not_def:
    print("[!] Name Error list", not_def)

print("\nAffichage du dictionnaire :")
print("---------------------------")
print(dicolist)

list1 = []
list2 = []

for key, value in dicolist.items():
    list1.append(key)
    list2.append(value)

print("\nListe des dates dans l'ordre des entrées :")
print("----------------------------------")
print(list1)
print("\nList of temperatures :")
print("------------------------")
print(list2)

try:
    list1 = list(map(str, list1))
    print(list1)
except ValueError as err_vlist1:
    print("[!] False value (no: string or int value)", err_vlist1)

#list3 = [int(list2) for list2 in list2]
try:
    list2 = list(map(float, list2))
except ValueError as err_val:
    print("[!] False value (no: string or int value)", err_val)
    list2 = []

xdates = [datetime.datetime.strptime('{:10}'.format(str(li)),'%d/%m/%Y : %H:%M:%S') for li in list1]
print(xdates)

x_axis = xdates
y_axis = list2

try:
    show_grid = True
    with plt.style.context('seaborn-darkgrid'):
        fig = plt.figure()
        fig.set_facecolor("lightsteelblue")
        lab = fig.suptitle('Temperature (C°)',
            fontsize=18)
        lab.set_color('navy')
        ax = plt.subplot()
        ax.tick_params(axis='x', colors='navy')
        ax.tick_params(axis='y', colors='navy')
        labelcol_y = plt.ylabel("y-label")
        labelcol_y.set_color('navy')
        labelcol_x = plt.xlabel("x-label")
        labelcol_x.set_color('navy')

        for x,y in zip(x_axis, y_axis):
            label = "{:.1f}".format(y)
            plt.annotate(label, (x,y), textcoords="offset points",
                xytext=(0,10), ha='center')

        reo_x, reo_y = zip(*sorted(zip(x_axis, y_axis)))
        plt.plot(reo_x, reo_y, 'o', color='red')
        plt.plot(reo_x, reo_y, '--', color='red')

        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y : %H:%M:%S'))
        plt.ylabel('Temperatures (C°)', fontsize=14)
        plt.xlabel('Dates', fontsize=14)
        plt.legend(['Tc°'])
        plt.gcf().autofmt_xdate(rotation=45)
        plt.grid(show_grid)
        plt.show()
except Exception as err_val:
    print("[!] Value Error !!! :", err_val)

try:
    os.remove('./param/aspifile11/data_datetemp.json')
    print("[+] File data_datetemp.json removed !")
    os.remove('./param/aspifile11/data_temp.json')
    print("[+] File data_temp.json removed !\n")
except OSError as os_err:
    print("[!] OS error ! ...", os_err)
