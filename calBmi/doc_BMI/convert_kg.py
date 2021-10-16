#!/usr/bin/python3
# -*- coding: utf-8 -*-


import os
import subprocess
import datetime
import json
import matplotlib.pyplot as plt
from matplotlib import dates
import matplotlib.dates as mdates
from matplotlib.dates import date2num
from matplotlib.dates import AutoDateLocator
from matplotlib.dates import AutoDateFormatter


file = open('./calBmi/doc_BMI/file_kg.json')
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

data_list2 = []
for value in zip(value):
    data_list2.append(value[0]['Kg'])

dicolist = {}

for data_list1, data_list2 in zip(data_list1, data_list2):
    dicolist[data_list1] = data_list2

print("\nDisplay dictionary :")
print("--------------------")
print(dicolist)

list1 = []
list2 = []

for key, value in dicolist.items():
    list1.append(key)
    list2.append(value)

print("\nList of dates :")
print("---------------")
print("Voici les valeurs list1 : ", list1)

print("\nList of kilo :")
print("--------------")
print(list2)

try:
    list1 = list(map(str, list1))
except ValueError as dat_err:
    print("[!] Invalid number (no: . or , !)", dat_err)

try:
    list2 = list(map(float, list2))
except ValueError as base_err:
    print("[!] Invalid number (no: . or , !)", base_err)
    list2 = []

xdates = [datetime.datetime.strptime('{:10}'.format(str(li)),'%d/%m/%Y : %H:%M:%S') for li in list1]
print("xdates values : ", xdates)

x_axis = xdates
y_axis = list2

#print(plt.style.available):
#['Solarize_Light2', '_classic_test_patch', 'bmh', 'classic', 'dark_background', 'fast',
#'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn', 'seaborn-bright', 'seaborn-colorblind',
#'seaborn-dark', 'seaborn-dark-palette', 'seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted',
#'seaborn-notebook', 'seaborn-paper', 'seaborn-pastel', 'seaborn-poster', 'seaborn-talk',
#'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'tableau-colorblind10']

try:
    show_grid = True
    with plt.style.context('seaborn-darkgrid'):
        fig = plt.figure()
        fig.set_facecolor("lightsteelblue")
        titlab = fig.suptitle('kilograms per date',
            fontsize=18)
        titlab.set_color('navy')
        ax = plt.subplot()
        ax.tick_params(axis='x', colors='navy')
        ax.tick_params(axis='y', colors='navy')
        labelcol_x = plt.ylabel("y-label")
        labelcol_x.set_color('navy')
        labelcol_y = plt.xlabel("x-label")
        labelcol_y.set_color('navy')

        for x, y in zip(x_axis, y_axis):
            label = "{:.1f}".format(y)
            plt.annotate(label, (x,y), textcoords="offset points",
                xytext=(0, 10), ha='center')

        reo_x, reo_y = zip(*sorted(zip(x_axis, y_axis)))
        plt.plot(reo_x, reo_y, 'o', color='teal')
        plt.plot(reo_x, reo_y, '--', color='teal')

        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y : %H:%M:%S'))
        plt.ylabel('Kg', fontsize=14)
        plt.xlabel('Dates', fontsize=14)
        plt.legend(['Kg/Date'])
        plt.gcf().autofmt_xdate(rotation=45)
        plt.grid(show_grid)
        plt.show()
except Exception:
    print("[!] Error from graph kg/date (matplotlib)")

# to verify if file exist.
try:
    if os.path.getsize('./calBmi/doc_BMI/customBmi.py'):
        subprocess.run('./calBmi/doc_BMI/customBmi.py', check=True)
except FileNotFoundError as callfile1:
    print("[!] File customBmi.py doesn't exist !", callfile1)

# to read date into file.
try:
    with open('./calBmi/doc_BMI/custom_kg.txt', 'r') as namefile:
        line_1 = namefile.readline()
        print(line_1)
        line_2 = namefile.readline()
        print(line_2)
except FileNotFoundError as callfile2:
    print("[!] File custom_kg.txt doesn't exist !", callfile2)

# to delete last string ('\n') at the end of line_1
try:
    printmonth = len(line_1)
    convert_line = line_1[0:-1]
    print(convert_line)
except NameError as err_nam:
    print("None value was checked", err_nam)

# Matplotlib seaborn-darkgrid
try:
    toshow_grid = True
    with plt.style.context('seaborn-darkgrid'):
        figure, axes = plt.subplots()

        for x,y in zip(x_axis, y_axis):
            label = "{:.1f}".format(y)
            plt.annotate(label, (x,y), textcoords="offset points",
                xytext=(0,10), ha='center')

        reo_x, reo_y = zip(*sorted(zip(x_axis, y_axis)))
        plt.plot(reo_x, reo_y, 'o', color='purple')
        plt.plot(reo_x, reo_y, '--', color='purple')

        locator = AutoDateLocator()
        axes.xaxis.set_major_locator(locator)
        ax = plt.gcf().axes[0]

        ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y : %H:%M:%S'))
        min_date = date2num(datetime.datetime.strptime(convert_line, "%d/%m/%Y"))
        max_date = date2num(datetime.datetime.strptime(line_2, "%d/%m/%Y"))
        axes.set_xlim([min_date, max_date])

        plt.ylabel('Kg', fontsize=14)
        plt.xlabel('Dates', fontsize=14)
        plt.suptitle('kilograms per year', fontsize=18)
        plt.legend(['Kg/Date'])
        plt.gcf().autofmt_xdate(rotation=45)
        plt.grid(toshow_grid)
        plt.show()
except Exception:
    print("[!] Error from graph kg/year (matplotlib)")
