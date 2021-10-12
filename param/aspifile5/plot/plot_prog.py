#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
    In this file the systol and diastol values are grouped together
    to make lists containing int values corresponding to the dates.
    Then, these lists are reused to form y_axis(systol) and
    z_axis(diastol). x_axis corresponding to the dates.
"""


import os
import json
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


print("\nListe1 = dates :")
print("--------------")

try:
    fileO = open('./param/aspifile5/data_date.json')
    list1 = json.load(fileO)
except ValueError as err_entry:
    print("+ Value Error", err_entry)

try:
    for letter in list1:
        print("list1: " + letter)
except NameError as err_list:
    print("+ Name Error list", err_list)

print("\nList2 = systol :")
print("--------------------")

try:
    fileO = open('./param/aspifile5/data_Systol.json')
    list2 = json.load(fileO)
except ValueError as err_entry2:
    print("+ Value Error", err_entry2)

try:
    for letter in list2:
        print("List2: " + letter)
except NameError as err_list2:
    print("+ Name Error list2", err_list2)

dicolist = {}

try:
    for list1, list2 in zip(list1, list2):
        dicolist[list1] = list2
except NameError as not_def:
    print("+ Name Error list", not_def)

print("\nAffichage du dictionnaire :")
print("---------------------------")
print(dicolist)

list1 = []
list2 = []

for key, value in dicolist.items():
    list1.append(key)
    list2.append(value)
    #list2 = [item.replace("/", ", ") for item in list2]

print("\nListe des dates dans l'ordre des entrées :")
print("----------------------------------")
print(list1)
print("\nListe des tensions :")
print("------------------------")
print("{}".format(list2))

try:
    list1 = list(map(str, list1))
    print(list1)
except ValueError as err_vlist1:
    print("+ False value (no: string or int value)", err_vlist1)

try:
    list2 = list(map(str, list2))
except ValueError as err_val:
    print("+ False value (no: string or int value)", err_val)
    list2 = []

#2ème fichier

print("\nListe3 = dates :")
print("--------------")

try:
    file3 = open('./param/aspifile5/data_dia.json')
    list3 = json.load(file3)
except ValueError as err_entry:
    print("+ Value Error", err_entry)

try:
    for letter in list3:
        print("list3: " + letter)
except NameError as err_list:
    print("+ Name Error list", err_list)

print("\nList4 = diastol :")
print("--------------------")

try:
    file4 = open('./param/aspifile5/data_Diastol.json')
    list4 = json.load(file4)
except ValueError as err_entry2:
    print("+ Value Error", err_entry2)

try:
    for letter in list4:
        print("List3: " + letter)
except NameError as err_list3:
    print("+ Name Error list3", err_list3)

dicofinal = {}

try:
    for list3, list4 in zip(list3, list4):
        dicofinal[list3] = list4
except NameError as not_def:
    print("+ Name Error list", not_def)

print("\nAffichage du dictionnaire :")
print("---------------------------")
print(dicofinal)

list3 = []
list4 = []

for key, value in dicofinal.items():
    list3.append(key)
    list4.append(value)
    #list3 = [item.replace("/", ", ") for item in list3]

print("\nListe des systols :")
print("----------------------------------")
print(list3)
print("\nListe des diastols :")
print("------------------------")
print("{}".format(list4))

try:
    list1 = list(map(str, list1))
    print(list1)
except ValueError as err_vlist1:
    print("+ False value (no: string or int value)", err_vlist1)

try:
    list2 = list(map(int, list2))
except ValueError as err_vallist2:
    print("+ False value (no: string or float value)", err_vallist2)
    list2 = []

try:
    list4 = list(map(int, list4))
except ValueError as err_vallist4:
    print("+ False value (no: string or float value)", err_vallist4)
    list4 = []

xdates = [datetime.datetime.strptime('{:10}'.format(str(li)),'%d/%m/%Y : %H:%M:%S') for li in list1]
print(xdates)

x_axis = xdates
y_axis = list2
z_axis = list4

# Color style : fivethirtyeight, seaborn-darkgrid, bmh, classic
try:
    show_grid = True
    with plt.style.context('seaborn-darkgrid'):
        fig = plt.figure()
        fig.set_facecolor("lightsteelblue")
        lab = fig.suptitle('Blood Pressure (TA) by Day',
            fontsize=18)
        lab.set_color('navy')
        ax = plt.subplot()
        ax.tick_params(axis='x', colors='navy')
        ax.tick_params(axis='y', colors='navy')
        labelc = plt.ylabel("y-label")
        labelc.set_color("navy")
        labelc2 = plt.xlabel("x-label")
        labelc2.set_color("navy")
        
        plt.plot(x_axis, y_axis, 'o', color='red')
        plt.plot(x_axis, z_axis, 'o', color='red')
        plt.vlines(x = x_axis, ymin = z_axis, ymax = y_axis,
           colors = 'blue',
           label = 'vline_multiple - full height')

        for x,y in zip(x_axis, y_axis):
            label = "{}".format(y)
            plt.annotate(label, (x,y), textcoords="offset points",
                xytext=(0,10), ha='center')

        for x,z in zip(x_axis, z_axis):
            label2 = "{}".format(z)
            plt.annotate(label2, (x,z), textcoords="offset points",
                xytext=(0,-15), ha='center')

        #plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y : %H:%M:%S'))
        plt.ylabel('TA (blood pressure)', fontsize=14)
        plt.xlabel('Dates', fontsize=14)
        #plt.xticks(rotation=25)
        plt.legend(['TA (blood pressure)'])
        plt.gcf().autofmt_xdate(rotation=25)
        plt.grid(show_grid)
        plt.show()
except ValueError as val:
    print("+ False entry value, ", val)

try:
    os.remove('./param/aspifile5/data_date.json')
    os.remove('./param/aspifile5/data_Systol.json')
    print("+ File data_date.json removed !")
    print("+ File data_Systol.json removed !")
    os.remove('./param/aspifile5/data_dia.json')
    os.remove('./param/aspifile5/data_Diastol.json')
    print("+ File data_dia.json removed !")
    print("+ File data_Diastol.json removed !")
except OSError as os_err:
    print("+ OS error ! ...", os_err)
