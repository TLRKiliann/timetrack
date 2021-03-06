#!/usr/bin/python3
# -*- coding: utf-8 -*-


import os
import json
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


print("\nListe1 = dates :")
print("--------------")
fileO = open('./param/aspifile22/data_datedlr.json')
list1 = json.load(fileO)

for letter in list1:
    print("list1: " + letter)

print("\nList2 = douleurs :")
print("--------------------")

fileO = open('./param/aspifile22/data_dlr.json')
list2 = json.load(fileO)

for letter in list2:
    print("List2: " + letter)

dicolist = {}

for list1, list2 in zip(list1, list2):
    dicolist[list1] = list2

print("\nDictionnary display :")
print("---------------------------")
print(dicolist)

list1 = []
list2 = []

for key, value in dicolist.items():
    list1.append(key)
    list2.append(value)
    
print("\nList of date by entry's order :")
print("----------------------------------")
print(list1)

print("\nList of pain evaluation :")
print("------------------------")
print(list2)

try:
    list1 = list(map(str, list1))
except ValueError as fmt_err:
    print("[!] Invalid number (no: . or , !)", fmt_err)

try:
    list2 = list(map(int, list2))
except ValueError as base_err:
    print("[!] Invalid number (no: . or , !)", base_err)
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
        lab = fig.suptitle('Pain Scale (1-10)',
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
            label = "{}".format(y)
            plt.annotate(label, (x,y), textcoords="offset points",
                xytext=(0,10), ha='center')

        reo_x, reo_y = zip(*sorted(zip(x_axis, y_axis)))
        plt.plot(reo_x, reo_y, 'o', color='purple')
        plt.plot(reo_x, reo_y, '-', color='purple')

        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y : %H:%M:%S'))
        plt.ylabel('Dlrs', fontsize=14)
        plt.xlabel('Dates', fontsize=14)
        plt.legend(['Pain (Dlrs)'])
        plt.gcf().autofmt_xdate(rotation=25)
        plt.grid(show_grid)
        plt.show()
except Exception as err_val:
    print("[!] Value Error !!! :", err_val)

try:
    os.remove('./param/aspifile22/data_datedlr.json')
    print("[+] File data_datedlr.json removed !")
    os.remove('./param/aspifile22/data_dlr.json')
    print("[+] File data_dlr.json removed !\n")
except OSError as os_err:
    print("[!] OS error ! ...", os_err)
