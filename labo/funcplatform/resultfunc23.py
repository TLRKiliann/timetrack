#!/usr/bin/python3
# -*- coding:utf-8 -*-


"""
    Usr can open file ordinary and print it as well.
"""


import os
import sys
import subprocess
import platform


def funcOsLab23():
    """
        For openning file at pdf
        format with a bit prog-sys code.
        For Linux, Windows and MAC.
    """
    labos = platform.system()
    print(labos)

    if labos == 'Linux':
        os.system('gio open "./labo/labosheet.pdf"') # Linux
    elif labos =='Darwin':
        subprocess.call('open', './labo/labosheet.pdf') # Mac
    else:
        os.startfile('./labo/labosheet.pdf') # Windows

def funcOsMicrobio23():
    """
        For openning file at pdf
        format with a bit prog-sys code.
        For Linux, Windows and MAC.
    """
    microbios = platform.system()
    print(microbios)

    if microbios == 'Linux':
        os.system('gio open "./labo/microbio.pdf"') # Linux
    elif microbios =='Darwin':
        subprocess.call('open', './labo/microbio.pdf') # Mac
    else:
        os.startfile('./labo/microbio.pdf') # Windows

def callingOsRslt23():
    """
        To read laborslt.txt
    """
    callplatform = platform.system()
    print(callplatform)

    if callplatform == 'Linux':
        os.system('gio open "./labo/doc_labo/result23.txt"') # Linux
    elif callplatform =='Darwin':
        subprocess.call('open', './labo/doc_labo/result23.txt') # Mac
    else:
        os.startfile('./labo/doc_labo/result23.txt') # Windows
