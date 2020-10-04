import os
import sys
import time

os.system("clear")
os.system("figlet NetSec")
print ("=====================")
print ("[       NetSec      ]")
print ("=====================")
print ("[1] DDOS")
print ("[2] Brute Force")
print ("[3] Database Dump")
print ("[4] Create Payload")
print ("[5] RED_HAWK")
print ("[6] Webdav")
Pilih = raw_input('====>')
if Pilih =="1":
  os.system("clear")
  os.system("apt-get install python2")
  os.system("apt-get install git")
  os.system("git clone https://github.com/Ha3MrX/DDos-Attack")
  os.system("python2 DDos-Attack/ddos-attack.py")
elif Pilih =="2":
  os.system("clear")
  os.system("apt-get install hydra")
  os.system("clear")
  os.system("hydra -h")
elif Pilih =="3":
  os.system("clear")
  os.system("apt-get install sqlmap")
  os.system("clear")
  os.system("sqlmap")
elif Pilih =="4":
  os.system("clear")
  os.system("apt-get install metasploit-fremawork")
  os.system("clear")
  os.system("msfconsole")
elif Pilih =="5":
  os.system("clear")
  os.system("apt-get install php python git php-curl php-xml")
  os.system("git clone https://github.com/Tuhinshubhra/RED_HAWK")
  os.system("php RED_HAWK/rhawk.php")
elif Pilih =="6":
  os.system("clear")
  os.system("apt-get install git python python2 ")
  os.system("git clone https://github.com/Infected14741/Massdav")
  os.system("clear}")
  os.system("python2 Massdav/tebas.py")
  