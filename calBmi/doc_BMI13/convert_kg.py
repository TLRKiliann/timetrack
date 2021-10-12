#!/usr/bin/python3
# -*- coding: utf-8 -*-


from tkinter import *
from tkinter import messagebox
import os
import time
import subprocess
import json
import datetime
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import dates
from matplotlib.dates import date2num
from matplotlib.dates import AutoDateLocator
from matplotlib.dates import AutoDateFormatter


file = open('./calBmi/doc_BMI13/file_kg.json')
data = json.load(file)
#file.close

try:
    for (key, value) in data.items():
        print("Key: " + key)
        print("Valeur: " + str(value))
        print("\nTo represent the data_get:\n")
        print(data.get("data"))
        print("\n")
        print("Valeur: " + str(value[0]))
        print("Valeur: " + str(value[1]))
        print("\n")
        print("Date: " + str(value[0]["Date"]))
        print("Kg: " + str(value[0]["Kg"]))
        print("\n")
        print("Date: " + str(value[1]["Date"]))
        print("Kg: " + str(value[1]["Kg"]))
except IndexError as ind_kg:
    print("Only one value for kg...", ind_kg)

data_list1 = []
for value in zip(value):
    data_list1.append(value[0]['Date'])

for (key, value) in data.items():
    print(key, value)
    print("\n")

print("\nList of weight\n")

data_list2 = []
for value in zip(value):
    data_list2.append(value[0]['Kg'])

dicolist = {}

for data_list1, data_list2 in zip(data_list1, data_list2):
    dicolist[data_list1] = data_list2

print("\nDisplay dictionary :")
print("---------------------------")
print(dicolist)

list1 = []
list2 = []

for key, value in dicolist.items():
    list1.append(key)
    list2.append(value)
    
print("\nList of dates :")
print("----------------------------------")
print(list1)

print("\nList of weight :")
print("------------------------")
print(list2)

list2 = list(map(float, list2))
list1 = list(map(str, list1))

converted_dates = list(map(datetime.datetime.strptime, list1, len(list1)*['%d-%m-%Y']))
x_axis = converted_dates
formatter = dates.DateFormatter('%d-%m-%Y')
y_axis = list2

show_grid = True
with plt.style.context('dark_background'):
    figure, axes = plt.subplots()
    # apply autoformatter for displaying of dates 
    locator = AutoDateLocator()
    axes.xaxis.set_major_locator(locator)
    ax = plt.gcf().axes[0]
    ax.xaxis.set_major_formatter(formatter)
    #axes.xaxis.set_major_formatter(AutoDateFormatter(locator))
    min_date = date2num(datetime.datetime.strptime('01/01/2021', "%d/%m/%Y"))
    max_date = date2num(datetime.datetime.strptime('31/12/2021', "%d/%m/%Y"))
    axes.set_xlim([min_date, max_date])
    #figure.autofmt_xdate()

    plt.plot(x_axis, y_axis, 'o--', color='cyan')
    plt.ylabel('Kg', fontsize=14)
    plt.xlabel('Dates', fontsize=14)
    plt.title('Kg by Date', fontsize=16)
    plt.legend(['kg/date'])
    plt.grid(show_grid)
    plt.gcf().autofmt_xdate(rotation=45)
    plt.show()

# to verify if file exist.
try:
    if os.path.getsize('./calBmi/doc_BMI13/customBmi.py'):
        subprocess.run('./calBmi/doc_BMI13/customBmi.py', check=True)
except FileNotFoundError as callfile1:
    print("+ File customBmi.py doesn't exist !", callfile1)

# to read into file the dates entered.
try:
    with open('./calBmi/doc_BMI13/custom_kg.txt', 'r') as namefile:
        line_1=namefile.readline()
        print(line_1)
        line_2=namefile.readline()
        print(line_2)
except FileNotFoundError as callfile2:
    print("+ File custom_kg.txt doesn't exist !", callfile2)

# to delete '\n' at the end of line_1
try:
    printmonth=len(line_1)
    convert_line=line_1[0:-1]
    print(convert_line)
except NameError as err_nam:
    print("None value was checked", err_nam)

try:
    show_grid = True
    with plt.style.context('seaborn-darkgrid'):
        figure, axes = plt.subplots()

        locator = AutoDateLocator()
        axes.xaxis.set_major_locator(locator)
        ax = plt.gcf().axes[0]
        ax.xaxis.set_major_formatter(formatter)
        min_date = date2num(datetime.datetime.strptime(convert_line, "%d-%m-%Y"))
        max_date = date2num(datetime.datetime.strptime(line_2, "%d-%m-%Y"))
        axes.set_xlim([min_date, max_date])

        plt.plot(x_axis, y_axis, 'o--', color='purple')
        plt.ylabel('Kg', fontsize=14)
        plt.xlabel('Dates', fontsize=14)
        plt.title('Kg by Date customised', fontsize=16)
        plt.legend(['kg/date'])
        plt.grid(show_grid)
        plt.gcf().autofmt_xdate(rotation=45)
        plt.show()
except NameError as data_err:
    print("Data BMI error", data_err)
    messagebox.showwarning("Warning", "None value was entered !")
