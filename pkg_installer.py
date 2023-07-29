#!/bin/usr/env python3
# Code credit goes to https://github.com/mishakorzik/AllHackingTools

import subprocess
from colorama import Fore, Back, Style
import os
import sys
import time

red = Fore.RED + Style.BRIGHT
green = Fore.GREEN + Style.BRIGHT
yellow = Fore.YELLOW + Style.BRIGHT
blue = Fore.BLUE + Style.BRIGHT
purple = Fore.MAGENTA + Style.BRIGHT
cyan = Fore.CYAN + Style.BRIGHT
white = Fore.WHITE + Style.BRIGHT
no_colour = Fore.RESET + Back.RESET + Style.RESET_ALL


def line_print(n):
    for word in n + "\n":
        sys.stdout.write(word)
        sys.stdout.flush()
        time.sleep(0.05)


try:
    subprocess.call("clear", shell=True)
    subprocess.call("sleep 1", shell=True)
    print(f"{red} ______                                  __  __           __   _            ")
    print(f'{cyan}/_  __/__  _________ ___  __  ___  __   / / / /___ ______/ /__(_)___  ____ _')
    print(f'{yellow} / / / _ \/ ___/ __ `__ \/ / / / |/_/  / /_/ / __ `/ ___/ //_/ / __ \/ __ `/')
    print(f'{blue} / / /  __/ /  / / / / / / /_/ />  <   / __  / /_/ / /__/ ,< / / / / / /_/ / ')
    print(f'{red}/_/  \___/_/  /_/ /_/ /_/\__,_/_/|_| _/_/ /_/\__,_/\___/_/|_/_/_/ /_/\__, /  ')
    print(f'{yellow}             __          (_)      __(_)      __                     /____/   ')
    print(f'{green}            / /   ____ _/ /_     / ___/___  / /___  ______                   ')
    print(f'{cyan}           / /   / __ `/ __ \    \__ \/ _ \/ __/ / / / __ \                  ')
    print(f'{red}          / /___/ /_/ / /_/ /   ___/ /  __/ /_/ /_/ / /_/ /                  ')
    print(f'{yellow}         /_____/\__,_/_.___/   /____/\___/\__/\__,_/ .___/                   ')
    print(f'{blue}                                                  /_/                        ')
    print("                         Tool Name: TermuxSetupHackingLab")
    print("                           Developer: @G_Man_Official")
    print(f'{yellow}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    git_installed = subprocess.call("command -v git > /dev/null 2>&1", shell=True)
    if git_installed == 0:
        print(f"{green}[+]-[Git].............................[ Installed ]")
        subprocess.call("sleep 1.5", shell=True)
    else:
        print(f"{red}[-]-[Git]..........................[ Not Found ]")
        subprocess.call("sleep 1.5", shell=True)
        print(f"{yellow}[!][Installing Module Git...]")
        subprocess.call("apt install git", shell=True)

    python_installed = subprocess.call("command -v python > /dev/null 2>&1", shell=True)
    if python_installed == 0:
        print(f"{green}[+]-[Python]..........................[ Installed ]")
        subprocess.call("sleep 1.5", shell=True)
    else:
        print(f"{red}[-]-[Python].......................[ Not Found ]")
        subprocess.call("sleep 1.5", shell=True)
        print(f"{yellow}[!][Installing Module Python...]")
        subprocess.call("apt install python > /dev/null", shell=True)
        subprocess.call("apt install python", shell=True)
        subprocess.call("apt install python2", shell=True)
        subprocess.call("apt install python3", shell=True)
        subprocess.call("pkg install pip", shell=True)
        subprocess.call("pkg install pip2", shell=True)
        subprocess.call("pip2 install --upgrade pip", shell=True)

    openssl_installed = subprocess.call("command -v openssl > /dev/null 2>&1", shell=True)
    if openssl_installed == 0:
        print(f"{green}[+]-[OpenSSL]..........................[ Installed ]")
        subprocess.call("sleep 1.5", shell=True)
    else:
        print(f"{red}[-]-[Python].......................[ Not Found ]")
        subprocess.call("sleep 1.5", shell=True)
        print(f"{yellow}[!][Installing Module openssl...]")
        subprocess.call("apt install openssl -y > /dev/null", shell=True)
    
    wget_installed = subprocess.call("command -v wget > /dev/null 2>&1", shell=True)
    if wget_installed == 0:
        print(f"{green}[+]-[Wget]............................[ Installed ]")
        subprocess.call("sleep 1.5", shell=True)
    else:
        print(f"{red}[-]-[Wget].........................[ Not Found ]")
        subprocess.call("sleep 1.5", shell=True)
        print(f"{yellow}[!][Installing Module Wget...]")
        subprocess.call("apt install wget -y", shell=True)

    ruby_installed = subprocess.call("command -v ruby > /dev/null 2>&1", shell=True)
    if ruby_installed == 0:
        print(f"{green}[+]-[Ruby]............................[ Installed ]")
        subprocess.call("sleep 1.5", shell=True)
    else:
        print(f"{red}[-]-[Ruby].........................[ Not Found ]")
        subprocess.call("sleep 1.5", shell=True)
        print(f"{yellow}[!][Installing Module Ruby...]")
        subprocess.call("apt install ruby -y", shell=True)

    lolcat_installed = subprocess.call("command -v lolcat > /dev/null 2>&1", shell=True)
    if lolcat_installed == 0:
        print(f"{green}[+]-[Lolcat]..........................[ Installed ]")
        subprocess.call("sleep 1.5", shell=True)
    else:
        print(f"{red}[-]-[Lolcat].......................[ Not Found ]")
        subprocess.call("sleep 1.5", shell=True)
        print(f"{yellow}[!][Installing Module Lolcat...]")
        subprocess.call("gem install lolcat -y", shell=True)

    php_installed = subprocess.call("command -v php > /dev/null 2>&1", shell=True)
    if php_installed == 0:
        print(f"{green}[+]-[PHP].............................[ Installed ]")
        subprocess.call("sleep 1.5", shell=True)
    else:
        print(f"{red}[-]-[PHP]..........................[ Not Found ]")
        subprocess.call("sleep 1.5", shell=True)
        print(f"{yellow}[!][Installing Module PHP...]")
        subprocess.call("apt install php -y", shell=True)

    zip_installed = subprocess.call("command -v zip > /dev/null 2>&1", shell=True)
    if zip_installed == 0:
        print(f"{green}[+]-[Zip].............................[ Installed ]")
        subprocess.call("sleep 1.5", shell=True)
    else:
        print(f"{red}[-]-[Zip]..........................[ Not Found ]")
        subprocess.call("sleep 1.5", shell=True)
        print(f"{yellow}[!][Installing Module Zip...]")
        subprocess.call("apt install zip -y", shell=True)

    pip_installed = subprocess.call("command -v pip > /dev/null 2>&1", shell=True)
    if pip_installed == 0:
        print(f"{green}[+]-[PIP].............................[ Installed ]")
        subprocess.call("sleep 1.5", shell=True)
    else:
        print(f"{red}[-]-[PIP]..........................[ Not Found ]")
        subprocess.call("sleep 1.5", shell=True)
        print(f"{yellow}[!][Installing Module pip...]")
        subprocess.call("apt install pip", shell=True)
        subprocess.call("pkg install pip", shell=True)
        subprocess.call("pkg install pip2", shell=True)
        subprocess.call("apt install pip", shell=True)
        subprocess.call("apt install pip2", shell=True)
        subprocess.call("pip2 install --upgrade pip", shell=True)

    curl_installed = subprocess.call("command -v curl > /dev/null 2>&1", shell=True)
    if curl_installed == 0:
        print(f"{green}[+]-[Curl]............................[ Installed ]")
        subprocess.call("sleep 1.5", shell=True)
    else:
        print(f"{red}[-]-[Curl].........................[ Not Found ]")
        subprocess.call("sleep 1.5", shell=True)
        print(f"{yellow}[!][Installing Module Curl...]")
        subprocess.call("apt install curl -y", shell=True)

    subprocess.call("clear", shell=True)
    print(f'''{green}
   ___             __         __ __          __ 
  |   .-----.-----|  |_.---.-|  |  .-----.--|  |
  |.  |     |__ --|   _|  _  |  |  |  -__|  _  |
  |.  |__|__|_____|____|___._|__|__|_____|_____|
  |:  |                                         
  |::.|                                         
  `---' ''')
    print("                       Tool Name: TermuxSetupHackingLab")
    print("                       Developer: @G_Man_Official")
    print(f"{cyan}                Telegram :: https://t.me/hacking_network8")
    print(f'{yellow}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print(f"{green}[+]-[Git].............................[ Installed ]")
    print(f"{green}[+]-[Python]..........................[ Installed ]")
    print(f"{green}[+]-[OpenSSL].........................[ Installed ]")
    print(f"{green}[+]-[Wget]............................[ Installed ]")
    print(f"{green}[+]-[Ruby]............................[ Installed ]")
    print(f"{green}[+]-[Lolcat]..........................[ Installed ]")
    print(f"{green}[+]-[PHP].............................[ Installed ]")
    print(f"{green}[+]-[PIP].............................[ Installed ]")
    print(f"{green}[+]-[Curl]............................[ Installed ]")
    print(f"{green}[+]-[Nodejs]..........................[ Installed ]")
    print("")
    time.sleep(2)
    os.system("python3 python_modules.py")
except KeyboardInterrupt:
    line_print("\n" + green + "Thanks for using This Tool!\n" + no_colour)
    exit(0)
