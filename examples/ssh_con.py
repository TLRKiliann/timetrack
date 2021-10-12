#!/usr/bin/python3
# -*- coding: utf-8 -*-

# First method with password asked :

import pexpect

# To download files

try:
    var_password  = "----"
    var_commandsys = ("scp esteban@192.168.18.8:~/doc_txt/systol.json ./param/aspifile7/")
    #make sure in the above command that username and hostname are according to your server
    child = pexpect.spawn(var_commandsys)
    i = child.expect(["password:", pexpect.EOF])

    if i == 0: # send password
            child.sendline(var_password)
            child.expect(pexpect.EOF)
            print("No problem ! Download done !!!")
    elif i == 1: 
            print("Got the key or connection timeout")
            pass

except Exception as e:
    print("Oops ! Something went wrong buddy...")
    print(e)

try:
    tovar_password  = "----"
    var_commandia = ("scp esteban@192.168.18.8:~/doc_txt/diastol.json ./param/aspifile7/")
    #make sure in the above command that username and hostname are according to your server
    var_child = pexpect.spawn(var_commandia)
    fu = var_child.expect(["password:", pexpect.EOF])

    if fu == 0: # send password
            var_child.sendline(tovar_password)
            var_child.expect(pexpect.EOF)
            print("No problem ! Download done !!!")
    elif fu == 1: 
            print("Got the key or connection timeout")
            pass

except Exception as ex:
    print("Oops ! Something went wrong buddy...")
    print(ex)

# Second method with public key asked :

try:
    out = subprocess.check_output(["ssh", "-i", "<path to your key>", "-p", "<port number>",
        "{}@{}".format(user, host), command])
    print(out)
except CalledProcessError as e:
    print("+ SSH connection failed", e)

try:
    subprocess.run(["scp", "esteban@192.168.18.8:~/doc_txt/diastol.json",
        "./param/aspifile7/"])
    subprocess.run(["scp", "esteban@192.168.18.8:~/doc_txt/systol.json",
        "./param/aspifile7/"])
except CalledProcessError as e_failed:
    print("+ SCP transfert failed", e_failed)


# To upload files
# Method 1

try:
    var_password  = "----"
    var_commandsys = ("scp ./param/aspifile7/systol.json esteban@192.168.18.8:~/doc_txt/systol.json")
    #make sure in the above command that username and hostname are according to your server
    sys_child = pexpect.spawn(var_commandsys)
    i = sys_child.expect(["password:", pexpect.EOF])

    if i == 0: # send password                
            sys_child.sendline(var_password)
            sys_child.expect(pexpect.EOF)
            print("No problem ! Upload done !!!")
    elif i == 1: 
            print("Got the key or connection timeout")
            pass

except Exception as e:
    print("Oops ! Something went wrong buddy...")
    print(e)

try:
    tovar_password  = "----"
    var_commandia = ("scp ./param/aspifile7/diastol.json esteban@192.168.18.8:~/doc_txt/diastol.json")
    #make sure in the above command that username and hostname are according to your server
    var_child = pexpect.spawn(var_commandia)
    fu = var_child.expect(["password:", pexpect.EOF])

    if fu == 0: # send password
            var_child.sendline(tovar_password)
            var_child.expect(pexpect.EOF)
            print("No problem ! Upload done !!!")
    elif fu == 1: 
            print("Got the key or connection timeout")
            pass

except Exception as ex:
    print("Oops ! Something went wrong buddy...")
    print(ex)

# Method 2

try:
    out = subprocess.check_output(["ssh", "-i", "~/.ssh/demo_rsa", "-p", "22",
        "{pi}@{192.168.18.11}".format(user, host), command])
    print(out)
except CalledProcessError as e:
    print("+ SSH connection failed", e)

try:
    subprocess.run(["scp", "./param/aspifile7/diastol.json",
        "pi@192.168.18.12:~/doc_txt7/diastol.json"])
    subprocess.run(["scp", "./param/aspifile7/systol.json",
        "pi@192.168.18.12:~/doc_txt7/systol.json"])
except CalledProcessError as e_failed: