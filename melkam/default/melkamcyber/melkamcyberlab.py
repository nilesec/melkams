import os
from terminaltables import DoubleTable
from tabulate import tabulate
#from banner import xe_header
import sys, traceback
from time import sleep

def config0():
    global up_interface
    up_interface = open('/usr/share/melkamcyber/tools/files/iface.txt', 'r').read()
    up_interface = up_interface.replace("\n", "")
    if up_interface == "0":
        up_interface = os.popen("route | awk '/Iface/{getline; print $8}'").read()
        up_interface = up_interface.replace("\n", "")

    global gateway
    gateway = open('/usr/share/melkamcyber/tools/files/gateway.txt', 'r').read()
    gateway = gateway.replace("\n", "")
    if gateway == "0":
        gateway = os.popen("ip route show | grep -i 'default via'| awk '{print $3 }'").read()
        gateway = gateway.replace("\n", "")
def home():
    config0()
    n_name = os.popen('iwgetid -r').read()
    n_mac = os.popen("ip addr | grep 'state UP' -A1 | tail -n1 | awk '{print $2}' | cut -f1  -d'/'").read()
    n_ip = os.popen("hostname -I").read()  # Local IP address
    n_host = os.popen("hostname").read()  # hostname

    table = [["IP Address", "MAC Address", "Gateway", "Iface", "Hostname"],
             ["", "", "", "", ""],
             [n_ip, n_mac.upper(), gateway, up_interface, n_host]]
    print(tabulate(table, stralign="center", tablefmt="fancy_grid", headers="firstrow"))
    print("")

def scan():
    os.system(f"sudo chmod +x /usr/share/melkamcyber/melkam.sh")
    os.system("sudo /usr/share/melkamcyber/./melkam.sh")
    config0()
    scan = os.popen("nmap " + gateway + "/24 -n -sP ").read()
    f = open('/usr/share/melkamcyber/tools/log/scan.txt', 'w')
    f.write(scan)
    f.close()

    devices = os.popen(" grep report /usr/share/melkamcyber/tools/log/scan.txt | awk '{print $5}'").read()
    devices_mac = os.popen("grep MAC /usr/share/melkamcyber/tools/log/scan.txt | awk '{print $3}'").read() + os.popen(
        "ip addr | grep 'state UP' -A1 | tail -n1 | awk '{print $2}' | cut -f1  -d'/'").read().upper()
    devices_name = os.popen(
        "grep MAC /usr/share/melkamcyber/tools/log/scan.txt | awk '{print $4 ,S$5 $6}'").read() + "\033[1;32m(This device)\033[1;m"
    table_data = [
        ['IP Address', 'Mac Address', 'Manufacturer'],
        [devices, devices_mac, devices_name]
    ]
    table = DoubleTable(table_data)
    print("\033[1;36m[melkamcyber]═══════════[ Devices  on your network ]═══════════[melkamcyber]\n\033[1;m")
    print(table.table)
#home()
scan()
