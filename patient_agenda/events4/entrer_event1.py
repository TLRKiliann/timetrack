#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
1er fichier qui reprend
les valeurs du fichiers txt
pour les écrire dans patient_rdv.json
et lancer p1check_value.py
"""

from pickle import load
import os
import json
import subprocess


file=open('./patient_agenda/events4/patient_calendar.txt','rb')
data=load(file)
file.close()

for (key, value) in data.items():
    print("Key: " + key)
    print("Valeur: " + str(value))
    
print("\nLOOP Finished !\n")

data_list1 = []
for value in data.items():
    data_list1.append(value)

try:
    if os.path.getsize('./patient_agenda/events4/doc_events/patient_rdv.json'):
        print("+ File 'patient_rdv.json' exist !")   
        with open('./patient_agenda/events4/doc_events/patient_rdv.json', 'w') as datafile:
            json.dump(data_list1, datafile, indent=4)
except FileNotFoundError as msg:
    print("File doesn't exist, but it has been created !")
    with open('./patient_agenda/events4/doc_events/patient_rdv.json', 'w') as datafile:
        json.dump(data_list1, datafile, indent=4)

for (key, value) in data.items():
    print(key, value)
    print("\n")

subprocess.call('./patient_agenda/events4/doc_events/conver_value.py')
