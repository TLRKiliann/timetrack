#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
    This file is made to make 4 more. I could have made only 3,
    but I preferred to do it this way. Thus, systol and diastol
    each have values associated with the dates.
    Easier to reformat lists for plot_prog.py afterwards.
"""


import subprocess
import json


file = open('./param/aspifile22/systol.json')
data = json.load(file)

try:
    for (key, value) in data.items():
        print("Key: " + key)
        print("Valeur: " + str(value))
        print("\nTo represent the data_get:\n")
        print(data.get("data"))
        print("\n")
        print("Valeur: " + str(value[0]))
        print("\n")
        print("Date: " + str(value[0]["Date"]))
        print("Systol: " + str(value[0]["Systol"]))
        print("\n")
except IndexError as err_read:
    print("+ Error from aspidata.py", err_read)

print("\nList of dates :\n")

data_list1 = []
for value in zip(value):
    data_list1.append(value[0]['Date'])

print("--- Data_list1 de aspidata.py :---\n", data_list1)
print("\n")

with open('./param/aspifile22/data_date.json', 'a+') as datafile:
    json.dump(data_list1, datafile, indent=4)

for (key, value) in data.items():
    print(key, value)
    print("\n")

print("\nList of systol :\n")

data_list2 = []
for value in zip(value):
    data_list2.append((value[0])['Systol'])

print(data_list2)
print("\n")
print("\nThat seems correct!\n")

with open('./param/aspifile22/data_Systol.json', 'a+') as datafile:
    json.dump(data_list2, datafile, indent=4)

#second file ttt
filedias = open('./param/aspifile22/diastol.json')
data = json.load(filedias)

try:
    for (key, value) in data.items():
        print("Key: " + key)
        print("Valeur: " + str(value))
        print("\nTo represent the data_get:\n")
        print(data.get("data"))
        print("\n")
        print("Valeur: " + str(value[0]))
        print("\n")
        print("Date: " + str(value[0]["Date"]))
        print("Diastol: " + str(value[0]["Diastol"]))
        print("\n")
except IndexError as err_readia:
    print("+ Error from aspidata.py", err_readia)

print("\nList of dates\n")

data_listdia = []
for value in zip(value):
    data_listdia.append(value[0]['Date'])

with open('./param/aspifile22/data_dia.json', 'a+') as datafiled:
    json.dump(data_listdia, datafiled, indent=4)

for (key, value) in data.items():
    print(key, value)
    print("\n")

print("\nList of diastol :\n")

data_list2 = []
for value in zip(value):
    data_list2.append((value[0])['Diastol'])

print(data_list2)
print("\n")
print("\nThat seems correct!\n")

with open('./param/aspifile22/data_Diastol.json', 'a+') as datafile2d:
    json.dump(data_list2, datafile2d, indent=4)

try:
    proc = subprocess.run(["scp", "./param/paramdata22.txt",
        "pi@192.168.18.12:~/tt_doc/doc_txt22/paramdata22.txt"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    secproc = subprocess.run(["scp", "./param/aspifile22/diastol.json",
        "pi@192.168.18.12:~/tt_doc/doc_txt22/diastol.json"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    thirdproc = subprocess.run(["scp", "./param/aspifile22/systol.json",
        "pi@192.168.18.12:~/tt_doc/doc_txt22/systol.json"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(thirdproc.stderr))
except (OSError, FileNotFoundError) as e_failed:
    print("+ SCP transfert (upload) failed", e_failed)

print("\nLoading 'plot_prog.py'...")
subprocess.run('./param/aspifile22/plot/plot_prog.py', check=True)
