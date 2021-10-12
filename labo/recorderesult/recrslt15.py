#!/usr/bin/python3
# -*- coding:utf-8 -*-


"""
    Record all variables (attr of class) when this function called.
    All var are in ./labo/resultlabo_X.py
    The recording of data add date before upload files to server.
"""


from tkinter import *
import tkinter as tk
import time


def checkerecord15(self):
    """
        To upload data on server after creating files
    """
    print("[+] Date : " + time.strftime("%d/%m/%Y"))
    print("[+] Nom du patient : ", self.entrytext.get())
    with open('./need/doc_suivi15/patient15_14b.txt', 'a+') as file:
        with open('./labo/doc_labo/result15.txt', 'a+') as file2:
            file.write("----------------------------------------------------------\n")
            file.write("Date : ")
            file.write(time.strftime("%d/%m/%Y")+ '\n')
            file.write("Patient name : ")
            file.write(self.entrytext.get() + '\n')
            file2.write("\n---------------------------------------------------------\n")
            file2.write("Date : ")
            file2.write(time.strftime("%d/%m/%Y")+ '\n')
            file2.write("Patient name : ")
            file2.write(self.entrytext.get() + '\n')

    print(self.CheckVar1.get())
    if self.CheckVar1.get() == 1:
        print("[+] Abilify was checked !")
        with open('./need/doc_suivi15/patient15_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result15.txt', 'a+') as file2:
                file.write("# Abilify : " + time.strftime("%d/%m/%Y") + " checked\n")
                file2.write("# Abilify : " + time.strftime("%d/%m/%Y") + " checked\n")
    else:
        print("[-] Abilify ok, nothing to do")

    print(self.CheckVar2.get())
    if self.CheckVar2.get() == 1:
        print("[+] Clopixol was checked !")
        with open('./need/doc_suivi15/patient15_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result15.txt', 'a+') as file2:
                file.write("# Clopixol : " + time.strftime("%d/%m/%Y") + " checked\n")
                file2.write("# Clopixol : " + time.strftime("%d/%m/%Y") + " checked\n")
    else:
        print("[-] Clopixol ok, nothing to do")

    print(self.CheckVar3.get())
    if self.CheckVar3.get() == 1:
        print("[+] Clozapine was checked !")
        with open('./need/doc_suivi15/patient15_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result15.txt', 'a+') as file2:
                file.write("# Clozapine : " + time.strftime("%d/%m/%Y") + " checked\n")
                file2.write("# Clozapine : " + time.strftime("%d/%m/%Y") + " checked\n")
    else:
        print("[-] Clozapine ok, nothing to do")

    print(self.CheckVar4.get())
    if self.CheckVar4.get() == 1:
        print("[+] Dogmatil was checked !")
        with open('./need/doc_suivi15/patient15_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result15.txt', 'a+') as file2:
                file.write("# Dogmatil : " + time.strftime("%d/%m/%Y") + " checked\n")
                file2.write("# Dogmatil : " + time.strftime("%d/%m/%Y") + " checked\n")
    else:
        print("[-] Dogmatil ok, nothing to do")

    print(self.CheckVar5.get())
    if self.CheckVar5.get() == 1:
        print("[+] Entumine was checked !")
        with open('./need/doc_suivi15/patient15_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result15.txt', 'a+') as file2:
                file.write("# Entumine : " + time.strftime("%d/%m/%Y") + " checked\n")
                file2.write("# Entumine : " + time.strftime("%d/%m/%Y") + " checked\n")
    else:
        print("[-] Entumine ok, nothing to do")

    print(self.CheckVar6.get())
    if self.CheckVar6.get() == 1:
        print("[+] Fluanxol was checked !")
        with open('./need/doc_suivi15/patient15_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result15.txt', 'a+') as file2:
                file.write("# Fluanxol : " + time.strftime("%d/%m/%Y") + " checked\n")
                file2.write("# Fluanxol : " + time.strftime("%d/%m/%Y") + " checked\n")
    else:
        print("[-] Fluanxol ok, nothing to do")

    print(self.CheckVar7.get())
    if self.CheckVar7.get() == 1:
        print("[+] Haldol was checked !")
        with open('./need/doc_suivi15/patient15_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result15.txt', 'a+') as file2:
                file.write("# Haldol : " + time.strftime("%d/%m/%Y") + " checked\n")
                file2.write("# Haldol : " + time.strftime("%d/%m/%Y") + " checked\n")
    else:
        print("[-] Haldol ok, nothing to do")

    print(self.CheckVar8.get())
    if self.CheckVar8.get() == 1:
        print("[+] Invega was checked !")
        with open('./need/doc_suivi15/patient15_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result15.txt', 'a+') as file2:
                file.write("# Invega : " + time.strftime("%d/%m/%Y") + " checked\n")
                file2.write("# Invega : " + time.strftime("%d/%m/%Y") + " checked\n")
    else:
        print("[-] Invega ok, nothing to do")

    print(self.CheckVar9.get())
    if self.CheckVar9.get() == 1:
        print("[+] Nozinan was checked !")
        with open('./need/doc_suivi15/patient15_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result15.txt', 'a+') as file2:
                file.write("# Nozinan : " + time.strftime("%d/%m/%Y") + " checked\n")
                file2.write("# Nozinan : " + time.strftime("%d/%m/%Y") + " checked\n")
    else:
        print("[-] Nozinan ok, nothing to do")

    print(self.CheckVar10.get())
    if self.CheckVar10.get() == 1:
        print("[+] Prazine was checked !")
        with open('./need/doc_suivi15/patient15_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result15.txt', 'a+') as file2:
                file.write("# Prazine : " + time.strftime("%d/%m/%Y") + " checked\n")
                file2.write("# Prazine : " + time.strftime("%d/%m/%Y") + " checked\n")
    else:
        print("[-] Prazine ok, nothing to do")

    print(self.CheckVar12.get())
    if self.CheckVar12.get() == 1:
        print("[+] Quetiapine was checked !")
        with open('./need/doc_suivi15/patient15_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result15.txt', 'a+') as file2:
                file.write("# Quetiapine : " + time.strftime("%d/%m/%Y") + " checked\n")
                file2.write("# Quetiapine : " + time.strftime("%d/%m/%Y") + " checked\n")
    else:
        print("[-] Quetiapine ok, nothing to do")

    print(self.CheckVar13.get())
    if self.CheckVar13.get() == 1:
        print("[+] Risperdal was checked !")
        with open('./need/doc_suivi15/patient15_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result15.txt', 'a+') as file2:
                file.write("# Risperdal : " + time.strftime("%d/%m/%Y") + " checked\n")
                file2.write("# Risperdal : " + time.strftime("%d/%m/%Y") + " checked\n")
    else:
        print("[-] Risperdal ok, nothing to do")

    print(self.CheckVar14.get())
    if self.CheckVar14.get() == 1:
        print("[+] Serdolect was checked !")
        with open('./need/doc_suivi15/patient15_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result15.txt', 'a+') as file2:
                file.write("# Serdolect : " + time.strftime("%d/%m/%Y") + " checked\n")
                file2.write("# Serdolect : " + time.strftime("%d/%m/%Y") + " checked\n")
    else:
        print("[-] Serdolect ok, nothing to do")

    print(self.CheckVar15.get())
    if self.CheckVar15.get() == 1:
        print("[+] Solian was checked !")
        with open('./need/doc_suivi15/patient15_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result15.txt', 'a+') as file2:
                file.write("# Solian : " + time.strftime("%d/%m/%Y") + " checked\n")
                file2.write("# Solian : " + time.strftime("%d/%m/%Y") + " checked\n")
    else:
        print("[-] Solian ok, nothing to do")

    print(self.CheckVar16.get())
    if self.CheckVar16.get() == 1:
        print("[+] Tiapridal was checked !")
        with open('./need/doc_suivi15/patient15_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result15.txt', 'a+') as file2:
                file.write("# Tiapridal : " + time.strftime("%d/%m/%Y") + " checked\n")
                file2.write("# Tiapridal : " + time.strftime("%d/%m/%Y") + " checked\n")
    else:
        print("[-] Tiapridal ok, nothing to do")

    print(self.CheckVar17.get())
    if self.CheckVar17.get() == 1:
        print("[+] Truxal was checked !")
        with open('./need/doc_suivi15/patient15_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result15.txt', 'a+') as file2:
                file.write("# Truxal : " + time.strftime("%d/%m/%Y") + " checked\n")
                file2.write("# Truxal : " + time.strftime("%d/%m/%Y") + " checked\n")
    else:
        print("[-] Truxal ok, nothing to do")

    print(self.CheckVar18.get())
    if self.CheckVar18.get() == 1:
        print("[+] Zyprexa was checked !")
        with open('./need/doc_suivi15/patient15_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result15.txt', 'a+') as file2:
                file.write("# Zyprexa : " + time.strftime("%d/%m/%Y") + " checked\n")
                file2.write("# Zyprexa : " + time.strftime("%d/%m/%Y") + " checked\n")
    else:
        print("[-] Zyprexa ok, nothing to do")

    print(self.CheckVar19.get())
    if self.CheckVar19.get() == 1:
        print("[+] Briviact was checked !")
        with open('./need/doc_suivi15/patient15_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result15.txt', 'a+') as file2:
                file.write("# Briviact : " + time.strftime("%d/%m/%Y") + " checked\n")
                file2.write("# Briviact : " + time.strftime("%d/%m/%Y") + " checked\n")
    else:
        print("[-] Briviact ok, nothing to do")

    print(self.CheckVar20.get())
    if self.CheckVar20.get() == 1:
        print("[+] Carbamazepine was checked !")
        with open('./need/doc_suivi15/patient15_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result15.txt', 'a+') as file2:
                file.write("# Carbamazepine : " + time.strftime("%d/%m/%Y") + " checked\n")
                file2.write("# Carbamazepine : " + time.strftime("%d/%m/%Y") + " checked\n")
    else:
        print("[-] Carbamazepine ok, nothing to do")

    print(self.CheckVar21.get())
    if self.CheckVar21.get() == 1:
        print("[+] Depakine was checked !")
        with open('./need/doc_suivi15/patient15_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result15.txt', 'a+') as file2:
                file.write("# Depakine : " + time.strftime("%d/%m/%Y") + " checked\n")
                file2.write("# Depakine : " + time.strftime("%d/%m/%Y") + " checked\n")
    else:
        print("[-] Depakine ok, nothing to do")

    print(self.CheckVar22.get())
    if self.CheckVar22.get() == 1:
        print("[+] Ethosuximide was checked !")
        with open('./need/doc_suivi15/patient15_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result15.txt', 'a+') as file2:
                file.write("# Ethosuximide : " + time.strftime("%d/%m/%Y") + " checked\n")
                file2.write("# Ethosuximide : " + time.strftime("%d/%m/%Y") + " checked\n")
    else:
        print("[-] Ethosuximide ok, nothing to do")

    print(self.CheckVar23.get())
    if self.CheckVar23.get() == 1:
        print("[+] Fycompa was checked !")
        with open('./need/doc_suivi15/patient15_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result15.txt', 'a+') as file2:
                file.write("# Fycompa : " + time.strftime("%d/%m/%Y") + " checked\n")
                file2.write("# Fycompa : " + time.strftime("%d/%m/%Y") + " checked\n")
    else:
        print("[-] Fycompa ok, nothing to do")

    print(self.CheckVar24.get())
    if self.CheckVar24.get() == 1:
        print("[+] Gabitril was checked !")
        with open('./need/doc_suivi15/patient15_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result15.txt', 'a+') as file2:
                file.write("# Gabitril : " + time.strftime("%d/%m/%Y") + " checked\n")
                file2.write("# Gabitril : " + time.strftime("%d/%m/%Y") + " checked\n")
    else:
        print("[-] Gabitril ok, nothing to do")

    print(self.CheckVar25.get())
    if self.CheckVar25.get() == 1:
        print("[+] Inovelon was checked !")
        with open('./need/doc_suivi15/patient15_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result15.txt', 'a+') as file2:
                file.write("# Inovelon : " + time.strftime("%d/%m/%Y") + " checked\n")
                file2.write("# Inovelon : " + time.strftime("%d/%m/%Y") + " checked\n")
    else:
        print("[-] Inovelon ok, nothing to do")

    print(self.CheckVar26.get())
    if self.CheckVar26.get() == 1:
        print("[+] Keppra was checked !")
        with open('./need/doc_suivi15/patient15_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result15.txt', 'a+') as file2:
                file.write("# Keppra : " + time.strftime("%d/%m/%Y") + " checked\n")
                file2.write("# Keppra : " + time.strftime("%d/%m/%Y") + " checked\n")
    else:
        print("[-] Keppra ok, nothing to do")

    print(self.CheckVar27.get())
    if self.CheckVar27.get() == 1:
        print("[+] Lamictal was checked !")
        with open('./need/doc_suivi15/patient15_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result15.txt', 'a+') as file2:
                file.write("# Lamictal : " + time.strftime("%d/%m/%Y") + " checked\n")
                file2.write("# Lamictal : " + time.strftime("%d/%m/%Y") + " checked\n")
    else:
        print("[-] Lamictal ok, nothing to do")

    print(self.CheckVar28.get())
    if self.CheckVar28.get() == 1:
        print("[+] Lyrica was checked !")
        with open('./need/doc_suivi15/patient15_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result15.txt', 'a+') as file2:
                file.write("# Lyrica : " + time.strftime("%d/%m/%Y") + " checked\n")
                file2.write("# Lyrica : " + time.strftime("%d/%m/%Y") + " checked\n")
    else:
        print("[-] Lyrica ok, nothing to do")

    print(self.CheckVar29.get())
    if self.CheckVar29.get() == 1:
        print("[+] Myzoline was checked !")
        with open('./need/doc_suivi15/patient15_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result15.txt', 'a+') as file2:
                file.write("# Myzoline : " + time.strftime("%d/%m/%Y") + " checked\n")
                file2.write("# Myzoline : " + time.strftime("%d/%m/%Y") + " checked\n")
    else:
        print("[-] Myzoline ok, nothing to do")

    print(self.CheckVar30.get())
    if self.CheckVar30.get() == 1:
        print("[+] Neurontin was checked !")
        with open('./need/doc_suivi15/patient15_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result15.txt', 'a+') as file2:
                file.write("# Neurontin : " + time.strftime("%d/%m/%Y") + " checked\n")
                file2.write("# Neurontin : " + time.strftime("%d/%m/%Y") + " checked\n")
    else:
        print("[-] Neurontin ok, nothing to do")

    print(self.CheckVar31.get())
    if self.CheckVar31.get() == 1:
        print("[+] Phenobarbital was checked !")
        with open('./need/doc_suivi15/patient15_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result15.txt', 'a+') as file2:
                file.write("# Phenobarbital : " + time.strftime("%d/%m/%Y") + " checked\n")
                file2.write("# Phenobarbital : " + time.strftime("%d/%m/%Y") + " checked\n")
    else:
        print("[-] Phenobarbital ok, nothing to do")

    print(self.CheckVar32.get())
    if self.CheckVar32.get() == 1:
        print("[+] Phenytoine was checked !")
        with open('./need/doc_suivi15/patient15_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result15.txt', 'a+') as file2:
                file.write("# Phenytoine : " + time.strftime("%d/%m/%Y") + " checked\n")
                file2.write("# Phenytoine : " + time.strftime("%d/%m/%Y") + " checked\n")
    else:
        print("[-] Phenytoine ok, nothing to do")

    print(self.CheckVar33.get())
    if self.CheckVar33.get() == 1:
        print("[+] Sabril was checked !")
        with open('./need/doc_suivi15/patient15_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result15.txt', 'a+') as file2:
                file.write("# Sabril : " + time.strftime("%d/%m/%Y") + " checked\n")
                file2.write("# Sabril : " + time.strftime("%d/%m/%Y") + " checked\n")
    else:
        print("[-] Sabril ok, nothing to do")

    print(self.CheckVar34.get())
    if self.CheckVar34.get() == 1:
        print("[+] Taloxa was checked !")
        with open('./need/doc_suivi15/patient15_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result15.txt', 'a+') as file2:
                file.write("# Taloxa : " + time.strftime("%d/%m/%Y") + " checked\n")
                file2.write("# Taloxa : " + time.strftime("%d/%m/%Y") + " checked\n")
    else:
        print("[-] Taloxa ok, nothing to do")

    print(self.CheckVar35.get())
    if self.CheckVar35.get() == 1:
        print("[+] Topamax was checked !")
        with open('./need/doc_suivi15/patient15_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result15.txt', 'a+') as file2:
                file.write("# Topamax : " + time.strftime("%d/%m/%Y") + " checked\n")
                file2.write("# Topamax : " + time.strftime("%d/%m/%Y") + " checked\n")
    else:
        print("[-] Topamax ok, nothing to do")

    print(self.CheckVar36.get())
    if self.CheckVar36.get() == 1:
        print("[+] Trileptal was checked !")
        with open('./need/doc_suivi15/patient15_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result15.txt', 'a+') as file2:
                file.write("# Trileptal : " + time.strftime("%d/%m/%Y") + " checked\n")
                file2.write("# Trileptal : " + time.strftime("%d/%m/%Y") + " checked\n")
    else:
        print("[-] Trileptal ok, nothing to do")

    print(self.CheckVar37.get())
    if self.CheckVar37.get() == 1:
        print("[+] Trobalt was checked !")
        with open('./need/doc_suivi15/patient15_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result15.txt', 'a+') as file2:
                file.write("# Trobalt : " + time.strftime("%d/%m/%Y") + " checked\n")
                file2.write("# Trobalt : " + time.strftime("%d/%m/%Y") + " checked\n")
    else:
        print("[-] Trobalt ok, nothing to do")

    print(self.CheckVar38.get())
    if self.CheckVar38.get() == 1:
        print("[+] Vimpat was checked !")
        with open('./need/doc_suivi15/patient15_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result15.txt', 'a+') as file2:
                file.write("# Vimpat : " + time.strftime("%d/%m/%Y") + " checked\n")
                file2.write("# Vimpat : " + time.strftime("%d/%m/%Y") + " checked\n")
    else:
        print("[-] Vimpat ok, nothing to do")

    print(self.CheckVar39.get())
    if self.CheckVar39.get() == 1:
        print("[+] Zonegran was checked !")
        with open('./need/doc_suivi15/patient15_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result15.txt', 'a+') as file2:
                file.write("# Zonegran : " + time.strftime("%d/%m/%Y") + " checked\n")
                file2.write("# Zonegran : " + time.strftime("%d/%m/%Y") + " checked\n")
    else:
        print("[-] Zonegran ok, nothing to do")

    print(self.CheckVar40.get())
    if self.CheckVar40.get() == 1:
        print("[+] Anafranil was checked !")
        with open('./need/doc_suivi15/patient15_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result15.txt', 'a+') as file2:
                file.write("# Anafranil : " + time.strftime("%d/%m/%Y") + " checked\n")
                file2.write("# Anafranil : " + time.strftime("%d/%m/%Y") + " checked\n")
    else:
        print("[-] Anafranil ok, nothing to do")

    print(self.CheckVar41.get())
    if self.CheckVar41.get() == 1:
        print("[+] Citalopram was checked !")
        with open('./need/doc_suivi15/patient15_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result15.txt', 'a+') as file2:
                file.write("# Citalopram : " + time.strftime("%d/%m/%Y") + " checked\n")
                file2.write("# Citalopram : " + time.strftime("%d/%m/%Y") + " checked\n")
    else:
        print("[-] Citalopram ok, nothing to do")

    print(self.CheckVar42.get())
    if self.CheckVar42.get() == 1:
        print("[+] Cipralex was checked !")
        with open('./need/doc_suivi15/patient15_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result15.txt', 'a+') as file2:
                file.write("# Cipralex : " + time.strftime("%d/%m/%Y") + " checked\n")
                file2.write("# Cipralex : " + time.strftime("%d/%m/%Y") + " checked\n")
    else:
        print("[-] Cipralex ok, nothing to do")

    print(self.CheckVar43.get())
    if self.CheckVar43.get() == 1:
        print("[+] Cymbalta was checked !")
        with open('./need/doc_suivi15/patient15_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result15.txt', 'a+') as file2:
                file.write("# Cymbalta : " + time.strftime("%d/%m/%Y") + " checked\n")
                file2.write("# Cymbalta : " + time.strftime("%d/%m/%Y") + " checked\n")
    else:
        print("[-] Cymbalta ok, nothing to do")

    print(self.CheckVar44.get())
    if self.CheckVar44.get() == 1:
        print("[+] Deroxat was checked !")
        with open('./need/doc_suivi15/patient15_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result15.txt', 'a+') as file2:
                file.write("# Deroxat : " + time.strftime("%d/%m/%Y") + " checked\n")
                file2.write("# Deroxat : " + time.strftime("%d/%m/%Y") + " checked\n")
    else:
        print("[-] Deroxat ok, nothing to do")

    print(self.CheckVar45.get())
    if self.CheckVar45.get() == 1:
        print("[+] Effexor was checked !")
        with open('./need/doc_suivi15/patient15_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result15.txt', 'a+') as file2:
                file.write("# Effexor : " + time.strftime("%d/%m/%Y") + " checked\n")
                file2.write("# Effexor : " + time.strftime("%d/%m/%Y") + " checked\n")
    else:
        print("[-] Effexor ok, nothing to do")

    print(self.CheckVar46.get())
    if self.CheckVar46.get() == 1:
        print("[+] Floxifral was checked !")
        with open('./need/doc_suivi15/patient15_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result15.txt', 'a+') as file2:
                file.write("# Floxifral : " + time.strftime("%d/%m/%Y") + " checked\n")
                file2.write("# Floxifral : " + time.strftime("%d/%m/%Y") + " checked\n")
    else:
        print("[-] Floxifral ok, nothing to do")

    print(self.CheckVar47.get())
    if self.CheckVar47.get() == 1:
        print("[+] Fluctine was checked !")
        with open('./need/doc_suivi15/patient15_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result15.txt', 'a+') as file2:
                file.write("# Fluctine : " + time.strftime("%d/%m/%Y") + " checked\n")
                file2.write("# Fluctine : " + time.strftime("%d/%m/%Y") + " checked\n")
    else:
        print("[-] Fluctine ok, nothing to do")

    print(self.CheckVar48.get())
    if self.CheckVar48.get() == 1:
        print("[+] Ludiomil was checked !")
        with open('./need/doc_suivi15/patient15_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result15.txt', 'a+') as file2:
                file.write("# Ludiomil : " + time.strftime("%d/%m/%Y") + " checked\n")
                file2.write("# Ludiomil : " + time.strftime("%d/%m/%Y") + " checked\n")
    else:
        print("[-] Ludiomil ok, nothing to do")

    print(self.CheckVar49.get())
    if self.CheckVar49.get() == 1:
        print("[+] Remeron was checked !")
        with open('./need/doc_suivi15/patient15_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result15.txt', 'a+') as file2:
                file.write("# Remeron : " + time.strftime("%d/%m/%Y") + " checked\n")
                file2.write("# Remeron : " + time.strftime("%d/%m/%Y") + " checked\n")
    else:
        print("[-] Remeron ok, nothing to do")

    print(self.CheckVar50.get())
    if self.CheckVar50.get() == 1:
        print("[+] Saroten was checked !")
        with open('./need/doc_suivi15/patient15_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result15.txt', 'a+') as file2:
                file.write("# Saroten : " + time.strftime("%d/%m/%Y") + " checked\n")
                file2.write("# Saroten : " + time.strftime("%d/%m/%Y") + " checked\n")
    else:
        print("[-] Saroten ok, nothing to do")

    print(self.CheckVar51.get())
    if self.CheckVar51.get() == 1:
        print("[+] Sertraline was checked !")
        with open('./need/doc_suivi15/patient15_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result15.txt', 'a+') as file2:
                file.write("# Sertraline : " + time.strftime("%d/%m/%Y") + " checked\n")
                file2.write("# Sertraline : " + time.strftime("%d/%m/%Y") + " checked\n")
    else:
        print("[-] Sertraline ok, nothing to do")

    print(self.CheckVar52.get())
    if self.CheckVar52.get() == 1:
        print("[+] Surmontil was checked !")
        with open('./need/doc_suivi15/patient15_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result15.txt', 'a+') as file2:
                file.write("# Surmontil : " + time.strftime("%d/%m/%Y") + " checked\n")
                file2.write("# Surmontil : " + time.strftime("%d/%m/%Y") + " checked\n")
    else:
        print("[-] Surmontil ok, nothing to do")

    print(self.CheckVar53.get())
    if self.CheckVar53.get() == 1:
        print("[+] Wellbutrin was checked !")
        with open('./need/doc_suivi15/patient15_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result15.txt', 'a+') as file2:
                file.write("# Wellbutrin : " + time.strftime("%d/%m/%Y") + " checked\n")
                file2.write("# Wellbutrin : " + time.strftime("%d/%m/%Y") + " checked\n")
    else:
        print("[-] Wellbutrin ok, nothing to do")

    print(self.CheckVar54.get())
    if self.CheckVar54.get() == 1:
        print("[+] Lithium was checked !")
        with open('./need/doc_suivi15/patient15_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result15.txt', 'a+') as file2:
                file.write("# Lithium : " + time.strftime("%d/%m/%Y") + " checked\n")
                file2.write("# Lithium : " + time.strftime("%d/%m/%Y") + " checked\n")
    else:
        print("[-] Lithium ok, nothing to do")

    with open('./need/doc_suivi15/patient15_14b.txt', 'a+') as endfile:
        with open('./labo/doc_labo/result15.txt', 'a+') as endfile2:
            endfile.write("---------------------------------------------------------\n\n")
            endfile2.write("---------------------------------------------------------\n\n")
