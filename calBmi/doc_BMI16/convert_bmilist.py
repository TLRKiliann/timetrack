#!/usr/bin/python3
# -*- coding: utf-8 -*-


import os
import subprocess
import json
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import dates
from matplotlib.dates import date2num
from matplotlib.dates import AutoDateLocator
from matplotlib.dates import AutoDateFormatter
import datetime
import time


file = open('./calBmi/doc_BMI16/file_bmi.json')
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
        print("BMI: " + str(value[0]["BMI"]))
        print("\n")
        print("Date: " + str(value[1]["Date"]))
        print("BMI: " + str(value[1]["BMI"]))
except IndexError as ind_err:
    print("Only one value for BMI...", ind_err)

data_list1 = []
for value in zip(value):
    data_list1.append(value[0]['Date'])

for (key, value) in data.items():
    print(key, value)
    print("\n")

data_list2 = []
for value in zip(value):
    data_list2.append(value[0]['BMI'])

dicolist = {}

for data_list1, data_list2 in zip(data_list1, data_list2):
    dicolist[data_list1] = data_list2

print("\nAffichage du dictionnaire :")
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

print("\nList of BMI :")
print("------------------------")
print(list2)

list2 = list(map(float, list2))
list1 = list(map(str, list1))

converted_dates = list(map(datetime.datetime.strptime, list1, len(list1)*['%d-%m-%Y']))
x_axis = converted_dates
formatter = dates.DateFormatter('%d-%m-%Y')
y_axis = list2

# or seaborn-darkgrid
show_grid = True
with plt.style.context(('dark_background')):
    figure, axes = plt.subplots()
    locator = AutoDateLocator()
    axes.xaxis.set_major_locator(locator)
    ax = plt.gcf().axes[0]
    ax.xaxis.set_major_formatter(formatter)
    min_date = date2num(datetime.datetime.strptime("01-01-2021", "%d-%m-%Y"))
    max_date = date2num(datetime.datetime.strptime("31-12-2021", "%d-%m-%Y"))
    axes.set_xlim([min_date, max_date])

    plt.bar(x_axis, y_axis, width=1, color='yellow')
    plt.ylabel('BMI', fontsize=14)
    plt.xlabel('Dates', fontsize=14)
    plt.title('BMI by Date', fontsize=16)
    plt.legend(['BMI/date'])
    plt.grid(show_grid)
    plt.gcf().autofmt_xdate(rotation=45)
    plt.show()
