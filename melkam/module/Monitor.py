
#This Script Is A file of melkam 
# This script isb fully Made BY the Abugida SEcurity
import os
import subprocess
import time
from cl import color

os.system(
     f" sudo chmod +x banner && sudo ./banner"
 )



print(f"{color.YELLOW}1-Monitor Mode\n""2-Managed Mode \n""3-Mac Changer\n")
choice=input(f"{color.ORANGE}What Do YOU choice From the above : ")
os.system(
            f"sed '' iface"
        )
print(f"{color.BLUE}The Above IS your Interface Choice :")
time.sleep(5)
interface=input("what is Your Interface : ")



if choice == "3" :
      print(f"{color.GREEN}Well You Choice The mac changer\n")
      ecvil=input(f"{color.BLUE}IS it for evil : ")
      if ecvil == "yes" :
           print(f"{color.RED}Get out!!")
           exit()
      else:
        os.system(
             f"sudo   macchanger -r {interface} | grep New"
                 )    
elif choice == "1" :
    print(f"{color.GREEN}Well You choice the Monitor Mode.....")
    ecvil=input(f"{color.BLUE}IS it for evil : ")
    if ecvil == "yes" :
           print(f"{color.RED}Get out!!")
           exit()
    else:
        os.system(
             f"sudo airmon-ng  start {interface} "
                 )
        print("The Monitor Process Finizhed Succussfully!!0")
elif choice == "2" :
    print(f"{color.GREEN}Well You choice the managed Mode.....")
    ecvil=input(f"{color.BLUE}IS it for evil : ")
    if ecvil == "yes" :
           print(f"{color.RED}Get out!!")
           exit()
    else:
      
        os.system(
             f"sudo airmon-ng  stop {interface} "
                 )
        print(f"{color.ORANGE}The Mnaged Process Finizhed Succussfully!!0")        
else :
           print("You inter envalid Input ")
           
        









