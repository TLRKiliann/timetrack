#!/usr/bin/python3
# -*- coding: utf-8 -*-


import os
import json
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


print("\nListe1 = dates :")
print("--------------")
fileO = open('./param/aspifile18/data_datepuls.json')
list1 = json.load(fileO)

for letter in list1:
    print("list1: " + letter)

print("\nList2 = Puls :")
print("--------------------")

fileO = open('./param/aspifile18/data_puls.json')
list2 = json.load(fileO)

for letter in list2:
    print("List2: " + letter)

dicolist = {}

for list1, list2 in zip(list1, list2):
    dicolist[list1] = list2

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
print("\nListe des pulsations :")
print("------------------------")
print(list2)

try:
    list1 = list(map(str, list1))
except ValueError as dat_err:
    print("+ Invalid number (no: . or , !)", dat_err)

try:
    list2 = list(map(int, list2))
except ValueError as base_err:
    print("+ Invalid number (no: . or , !)", base_err)
    list2 = []

xdates = [datetime.datetime.strptime('{:10}'.format(str(li)),'%d/%m/%Y : %H:%M:%S') for li in list1]
print(xdates)

x_axis = xdates
y_axis = list2

try:
    show_grid = True
    with plt.style.context('seaborn-darkgrid'):
        fig = plt.figure()
        fig.set_facecolor('lightsteelblue')
        lab = fig.suptitle('Puls/min by Day',
            fontsize=18)
        lab.set_color('navy')
        lab.set_color('navy')
        ax = plt.subplot()
        ax.tick_params(axis='x', colors='navy')
        ax.tick_params(axis='y', colors='navy')
        labelc = plt.ylabel("y-label")
        labelc.set_color('navy')
        labelc2 = plt.xlabel("x-label")
        labelc2.set_color('navy')
        plt.plot(x_axis, y_axis, 's', color='red')
        plt.plot(x_axis, y_axis, '--', color='orange')
        
        for x,y in zip(x_axis, y_axis):
            label = "{}".format(y)
            plt.annotate(label, (x,y), textcoords="offset points",
                xytext=(0,10), ha='center')

        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y : %H:%M:%S'))
        plt.ylabel('Puls/min', fontsize=12)
        plt.xlabel('Dates', fontsize=12)
        #plt.title('Relevé des puls/min par date', fontsize=16)
        #plt.xticks(rotation=25)
        plt.legend(['Pulsations/min'])
        plt.gcf().autofmt_xdate(rotation=25)
        plt.grid(show_grid)
        plt.show()
except ValueError as shapes_err:
    print("Invalid number", shapes_err)

try:
    os.remove('./param/aspifile18/data_datepuls.json')
    print("+ File data_datepuls.json removed !")
    os.remove('./param/aspifile18/data_puls.json')
    print("+ File data_puls.json removed !\n")
except OSError as os_err:
    print("+ OS error ! ...", os_err)
