#!/usr/bin/python3
# -*- coding: utf-8 -*-


import subprocess
import json


file = open('./param/aspifile20/freq.json')
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
        print("FR: " + str(value[0]["FR"]))
        print("\n")
except IndexError as err_read:
    print("+ Error from aspidata.py", err_read)

print("\nList of dates\n")

data_list1 = []
for value in zip(value):
    data_list1.append(value[0]['Date'])
    print(value[0]['Date'])

print("\nThat seems ok!\n")

with open('./param/aspifile20/data_datefr.json', 'a+') as datafile:
    json.dump(data_list1, datafile, indent=4)

for (key, value) in data.items():
    print(key, value)
    print("\n")

print("\nList of freq\n")

data_list2 = []
for value in zip(value):
    data_list2.append(value[0]['FR'])
    print(value[0]['FR'])

print("\nThat seems correct!\n")

with open('./param/aspifile20/data_fr.json', 'a+') as datafile:
    json.dump(data_list2, datafile, indent=4)

try:
    proc = subprocess.run(["scp", "./param/paramdata20.txt",
        "pi@192.168.18.12:~/tt_doc/doc_txt20/paramdata20.txt"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    secproc = subprocess.run(["scp", "./param/aspifile20/freq.json",
        "pi@192.168.18.12:~/tt_doc/doc_txt20/freq.json"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
except (OSError, FileNotFoundError) as e_failed:
    print("+ SCP transfert (upload) failed", e_failed)

print("\nLoading 'plot_freq.py'...")
subprocess.run('./param/aspifile20/plot/plot_freq.py', check=True)
