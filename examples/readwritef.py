#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
    This main app introduce parameters
    and send back graphical matplotlib
    representations.
"""


import os


try:
    if os.path.getsize('rwfile.txt'):
        with open('rwfile.txt', 'r') as file_corr:
            with open('rwfile.txt', 'w') as file_mod:                   
                lines = file_corr.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if line in lines:
                        print(lines[i-10])
                        print(line)
                        break
                        file_mod.writelines(str("mark"))
                        print(lines[i-1])
                        print("[+] Modification finish")
                        break

except FileNotFoundError:
    print('[!] Sorry, file asked not exist !')

"""
with open('./examples/rwfile.txt', 'w') as file_mod:
    file_mod.writelines(str(""), lines[i-8])
    print("[+] Modification finish")
    break

    os.remove('./examples/paramdata1.txt')
    label['text'] = "File paramdata1.txt has been deleted !"
    print("[del] File paramdata1.txt has been deleted !")
    fencap
    aaaaaaaaaaa
    bbbbbbbbbb
    cccccccccc
    ddddddddd
    fffffffff
    gggggggggg
    hhhhhhhhhh
    gggggggggg
    hhhhhhhhh
    iiiiiiiii

    jjjjjjjjj
    kkkkkkkkk
    lllllllll
    mmmmmmmmm
    5555555555
    66666666666
    7777777777
    8888888888
    999999999
    101000000
    
"""
