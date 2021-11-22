# TIME-TRACK 

* python3
* tkinter8.6)

![Anurag's GitHub stats](https://github-readme-stats.vercel.app/api?username=TLRKiliann&show_icons=true)

A medical application (time-track - future version) to connect PyMySQL with MySQL (MariaDB) on raspberry. Below, I explain how to use this application with the MariaDB table in localhost, LAN and WAN connection).
I chose a LAN infrastructure for security reasons. It is possible to extend the connection to the internet with a forwarding on the server (described below).

---

## Localhost :

### One user: (localhost - 127.0.0.1)

I recommend to create the MySQL database table in localhost (on your own machine). To do this you will have to modify the files of "update/" and "nutrition/" folders, as well as the "accessDB.py" file by replacing :

***LAN configuration :***\
`pymysql.connect(host='192.168.XX.XX', port=3306, user='usr_namedb', password='user_passwd', database='timetrackconn')`

by

***Localhost configuration :***\
`pymysql.connect(host='127.0.0.1', user='usr_namedb', password='user_passwd', database='timetrackconn')`\
(No port needed in this case).

---

## LAN or WAN :

### Multiple users: (LAN or WAN)

You should install MySQL on one server. Otherwise each user will have an independent database if it is installed on localhost. This is obviously not the point, if something changes, the other users will not see what has changed in their database.
It is also possible to extend the connection to the Internet (WAN) to have access outside the LAN (forwarding). In order to do this, replace the following lines:

`pymysql.connect(host='192.168.XX.XX', port=3306, user='usr_namedb', password='user_passwd', database='timetrackconn')`

by

`pymysql.connect(host='publicIP', port=3306, user='usr_namedb', password='user_passwd', database='timetrackconn')`

---

## Configuration for LOCALHOST :

### MySQL Workbench (config on your local machine ! (NOT DISTANT SERVER))


1) Create a database :\
MYSQL Connections --> click '+'

2) Enter connection name and password

3) Click on 'Test connection'\
Password required

4) Create a table Utf-8

5) Create columns

6) Save model

7) Return to 'home' and click on your new connection

---

## How to install pymysql on client (out of virtualenv)

You could install it on server too for solving problem.

### Install python3-pymysql (out of virutalenv !):

`sudo apt install python3-pymysql`

## Install PyMySQL and MySQL (in virtualenv !)

`pip3 install pymysql (or PyMySQL)`

`sudo apt-get build-dep python-mysqldb`

`pip install mysql-python`

`pip install mysql-connector-python`

---

## Configuration for LAN :

### Install ssh public key :

#### Private key and public key :

#### Generate rsa key :

`ssh-keygen -t rsa`

Enter file to save key : rsa_file

Enter passphrase : XXXXXXXX

---

#### Copy key on server :

`ssh-copy-id -i ~/.ssh/rsa_file.pub serv@192.168.x.x`
passwd

---

#### Connection with server :

`ssh -i ~/.ssh/rsa_file serv@192.168.x.x`

Enter passphrase: XXXXXX

_You don't need to enter password._

---

#### Save the key on client for remote server

_We place ourselves in the right folder (use ls and cd ;) !_

`ssh-agent bash`

`ssh -i ~/.ssh/rsa_file serv@192.168.x.x`

Enter your passphrase.

---

#### To keep passphrase in memory :

`ssh-add (-h = help) (-t = time in memory) (-l = list of keys) (-d rsa_file = delete the key)`

`ssh-add ~/.ssh/rsa_file`

Enter passphrase : (once time)
Connection established !!!

---

We only need to enter this sentence when we want to connect to the remote server :

#### For raspberry pi 3 :

`ssh -i ~/.ssh/rsa_file serv@192.168.x.x`

#### For linux distro :

`ssh -i ~/.ssh/rsa_file pi@192.168.x.x`

`logout`

---

#### Verification :

`cat ~/.ssh/config`

---

#### In the file there should be the following :

Host targetserver.serv@192.168.x.x\
IdentityFile ~/.ssh/rsa_file # private key

---

## How to install MySQL on Raspberry pi 3b (server) :

`sudo apt update`

`sudo apt upgrade`

`sudo apt install mariadb-server`

`sudo mysql_secure_installation`

Make sure you write down the password you set during this process as we will need to use it to access the MySQL server and create databases and users.

---

### To start mysql :

`sudo systemctl start mysql`

or

`sudo /etc/init.d/mysql start`

or

`service mysql start`

---

### To stop mysql :

`sudo systemctl stop mysql`

or

`sudo /etc/init.d/mysql stop`

or

`service mysql stop`

---

### To reload MySQL : (after changing conf)

`sudo systemctl reload mysql`

`sudo systemctl reload mariadb.service`

---

### To restart MySQL : (after changing conf)

`sudo systemctl restart mysql`

---

## How to create database with MySQL (on server side)

1) `sudo mysql -u root -p`

2) `CREATE USER 'user_name'@localhost IDENTIFIED BY 'password';`

3) `CREATE DATABASE database_name;`

### Create a new user (with remote access) and grant privileges to this user on the new database:
 
4) `GRANT ALL PRIVILEGES ON database_name.* TO 'user_name'@'%' IDENTIFIED BY 'password' WITH GRANT OPTION;`

5) `flush privileges;`

6) `quit;` or `exit;`

7) `sudo /etc/init.d/mysql restart`

---

### Now database is accessible for user_name :

8) `sudo mysql -u user_name -p`

9) `SHOW DATABASES;`

10) `USE timetrackconn;`

11) `SHOW TABLES;`

12)
    ```
    MariaDB [timetrackconn]> CREATE TABLE timetrackconn(
        -> stdid INT UNSIGNED NOT NULL AUTO_INCREMENT,
        -> firstname VARCHAR(45) NULL,
        -> surname VARCHAR(45) NULL,
        -> birth VARCHAR(45) NULL,
        -> allergy VARCHAR(45) NULL,
        -> disease VARCHAR(45) NULL,
        -> maindiagnostic VARCHAR(45) NULL,
        -> PRIMARY KEY (stdid)
        -> );
    ```

13) `sudo systemctl restart mysql`

14) Configure file to /etc/mysql/mariadb.d.conf/50-server.cnf :

`sudo nano /etc/mysql/mariadb.d.conf/50-server.cnf`

---

### Active/Change the following lines :

|Port|Address|
|----|-------|
|3306|0.0.0.0|

> port                3306\
> bind-address        0.0.0.0

15) Restart mariadb.service :

`sudo systemctl restart mariadb.service`

16) Configure firewall to open port 3306 for clients on LAN (for example) :

`sudo ufw allow from 192.168.XX.100 to any port 3306\`\

`sudo ufw allow from 192.168.XX.200 to any port 3306\`\

`sudo ufw allow from 192.168.XX.300 to any port 3306\`\

`sudo ufw allow from 192.168.XX.400 to any port 3306\`\

`sudo ufw reload`

---

### To test CONFIGURATION from server side :

`sudo netstat -anp | grep 3306`

---

### To test CONFIGURATION of server from client side :

`mysql -u koala33 -h 192.168.XX.XX -p`

---

Use a virtualenv (on client side)
---------------------------------

`$ virtualenv myvirtualenv`

`$ source myvirtualenv/bin/activate`

---

## How to install pymysql on client (out of virtualenv)

You could install it on server too for solving problem.

Install python3-pymysql (out of virutalenv !):

`sudo apt install python3-pymysql`

---

## Install PyMySQL and MySQL (in virtualenv !)

`$ pip3 install pymysql (or PyMySQL)`

`sudo apt-get build-dep python-mysqldb`

`$ pip install mysql-python`

`$ pip install mysql-connector-python`

---

## Compatibility with pymysql and mariadb (on client side - out of virtualenv !)

`sudo apt-get install mariadb-client-10.1`

---

## UFW : (Firewall)

You can grant access to the remote system with IP 192.168.XX.XX to connect
the port 3306 with the following command (on server side) :

* LAN 

`sudo ufw allow from 192.168.XX.XX to any port 22\`

`sudo ufw allow from 192.168.XX.XX to any port 3306\`

`sudo ufw reload`

---

* INTERNET

`sudo ufw allow from 192.168.XX.XX to any port 22\`

`sudo ufw allow 3306/tcp\`

`sudo ufw reload`

---

## Configuration of UFW :

* SERVEUR :

|  To  |  Action  |     From      |
|------|----------|---------------|
|   22 | ALLOW IN | 192.168.XX.XX |
| 3306 | ALLOW IN | 192.168.XX.XX |


---

* CLIENT :

> Status: active\
> Logging: on (low)\
> Default: deny (incoming), allow (outgoing), disabled (routed)\
> New profiles: skip

---

## Configuration for WAN

### PORT FOWARDING (on server) to access db from internet (WAN)

`# echo 1 > /proc/sys/net/ipv4/ip_forward`

---

### Launch app with :

`$ python3 heal_track.py`

or with :

`$ python3 heal_track.py '(Application.__init__(self))`

---

### To connect to server from client side :

Use ssh to remote access to server and configure all what you wants.

`ssh -i ~/.ssh/rsa_file server@192.168.XX.XX`

---

Still under development !
(It should be finished by june 2022)

Enjoy it ! :wink:

ko@l@tr33 :koala:
