#!/usr/bin/python3
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import messagebox
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


# Such as param
try:
    show_grid = True
    with plt.style.context('seaborn-darkgrid'):
        fig = plt.figure()
        fig.set_facecolor("black")
        lab = fig.suptitle('Blood Pressure (TA) by Month',
            fontsize=18)
        lab.set_color('aquamarine')
        ax = plt.subplot()
        ax.tick_params(axis='x', colors='aquamarine')
        #for tick in ax.get_xticklabels():
        #    tick.set_color('black')
        ax.tick_params(axis='y', colors='aquamarine')
        #for tick in ax.get_yticklabels():
        #    tick.set_color('black')
        # with bmh style context :
        #ax.spines['top'].set_color('cyan')
        #ax.spines['left'].set_color('cyan')
        #ax.spines['right'].set_color('cyan')
        #ax.spines['bottom'].set_color('cyan')
        labelc = plt.ylabel("y-label")
        labelc.set_color("aquamarine")
        labelc2 = plt.xlabel("x-label")
        labelc2.set_color("aquamarine")
        #labelc3 = plt.title("Relevé des tensions (TA) par date",
        #   fontsize=18)
        #labelc3.set_color('aquamarine')

        plt.plot(x_axis, y_axis, 'o', color='red')
        plt.plot(x_axis, z_axis, 'o', color='red')
        #plt.ylim(30, 240)
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
        plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
        plt.ylabel('TA (blood pressure)', fontsize=14)
        plt.xlabel('Dates', fontsize=14)
        #plt.title('Relevé des tensions (TA) par date', fontsize=18)
        plt.xticks(rotation=45)
        plt.legend(['TA (blood pressure)'])
        plt.grid(show_grid)
        plt.show()
except ValueError as val:
    print("+ False entry value, ", val)

# Such as BMI
show_grid = True
with plt.style.context('dark_background'):
    figure, axes = plt.subplots()
    # apply autoformatter for displaying of dates 
    locator = AutoDateLocator()
    axes.xaxis.set_major_locator(locator)
    ax = plt.gcf().axes[0]
    ax.xaxis.set_major_formatter(formatter)
    #axes.xaxis.set_major_formatter(AutoDateFormatter(locator))
    min_date = date2num(datetime.datetime.strptime('01-01-2020', "%d-%m-%Y"))
    max_date = date2num(datetime.datetime.strptime('31-12-2020', "%d-%m-%Y"))
    axes.set_xlim([min_date, max_date])
    #figure.autofmt_xdate()

    plt.plot(x_axis, y_axis, 'o-', color='cyan')
    plt.ylabel('Kg', fontsize=14)
    plt.xlabel('Dates', fontsize=14)
    plt.title('Kg by Date', fontsize=16)
    #plt.xticks(rotation=45)
    plt.legend(['kg/date'])
    plt.grid(show_grid)
    plt.gcf().autofmt_xdate(rotation=45)
    plt.show()