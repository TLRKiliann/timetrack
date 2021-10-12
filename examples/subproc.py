#!/usr/bin/python3
# -*- coding: utf-8 -*-


import subprocess


proc = subprocess.Popen('./14besoins/checkb3.py')
try:
    outs, errs = proc.communicate(timeout=2)
except:
    proc.kill()
    outs, errs = proc.communicate()
    print(outs, errs)
