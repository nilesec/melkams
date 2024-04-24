#!/usr/bin/python

import socket
from termcolor import colored
import os
import subprocess

os.system(
     f" sudo chmod +x banner && sudo ./banner"
 )

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(2)

host = input("[*] Please Specify a Host to Scan: ")
portr = int(input("[*] Enter Max Port Range: "))

def portscanner(port):
    if sock.connect_ex((host,port)):
        print(colored("[-] Port %d is closed" % (port), 'red'))
    else:
        print(colored("[+] Port %d is open" % (port), 'green'))

for port in range (1, portr +1):
    portscanner(port);
