import os
import time
from cl import color
############################################
version = "2.5"
codename = "Abu-cheker"
author = "abrham asrat(melkam cyber lab)"

#################################################

def user_name():
    user_name = os.name
    if user_name == "posix":
        print(f"{color.WHITE}Your os:   {color.RED}kali{color.WHITE}")
    elif user_name == "windows":
        print(f"{color.RED}Your os:   windows")
    else:
        print("Undtected Operating system")
        os.system("exit")
def views1():
    print("#"* 15)
    print("code name: ",codename)
    print("Version: ",version)
    print("Author: ",author)
    print("#"* 15)
def copy():
    os.system(f"cp -r {yorpname} {pwds}") 
def webdjango():
    print(f"{color.BLUE}Well My script help You Tpo generate The Simple Web Django app \n")
    os.system("clear")
    check = input(f"Doyou have Django? {color.YELLOW}[y][n]{color.GREEN}").lower()
    if check == "n":
        os.system(f"pip3 install django")
    elif check == "y":
        os.system("clear")
        yorpname = input("Enter Your Project Name: ")
        os.system(f"django-admin startproject {yorpname}")  
        modify = input("Do you want Me To modify The Project App:[y][n]").lower()
        pwds = os.system("pwd")
        if modify == "y":
            os.system(f"cd {yorpname} && python3 manage.py runserver")
            time.sleep(5)
        else:
            os.system(f"cp -r {yorpname} {pwds}")
            print(f"You can modify Your Web app in {pwds}!!")    
    else:
        print("Bad")      
 
def infoga():
    print("#*" * 15)   
    os.system("cd tool && sudo chmod +x infoga && sudo ./infoga")

def adbexploit():
    try:
        os.system("clear")
        print("well come to android app generator!! ")
        os.system(f"cd tool && sudo chmod +x ev && sudo ./ev")
    except KeyboardInterrupt:
        print("CTRL -C")
def views2():
   try:
    password = int(input(f"{color.GREEN}Enter your Password: "))
    if password == "":
        try:
           print(f"""
          
          {color.WHITE}1,{color.GREEN} Information gathering\n
          {color.WHITE}2,{color.GREEN} Android exploit\n
          {color.WHITE}3,{color.GREEN} Generate Your Own Django Web app simply\n""")
           choice = int(input("Enter Your Choices: "))
           if choice == 1:
            infoga()
           elif choice == 2:
            adbexploit()
           elif choice == 3:
            webdjango()
           else:
                print(f"{color.RED}You Entered invalid key!!")
                do = input(f"Doyou want to back{color.RED}[y][n]{color.GREEN}").lower()
                if do == "y":
                    return views2()
                else:
                    print("Good Bye")      
        except KeyboardInterrupt:
            print("\n CTRL-C")    
    elif password == "":
        return views2()    
    else:
        print("Wrong password!! retry")
        return views2()    
   except KeyboardInterrupt:
        print("\nbad gate way")       
         
user_name()
views1()
views2()

