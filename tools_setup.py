from colorama import Fore, Back, Style
import subprocess
import socket
import time
import os 
import os, sys
from os import system

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
      
def banner():
  print(f'{red} ______                                  __  __           __   _            ')
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
  print("                       Tool Name: TermuxSetupHackingLab")
  print("                       Made With L3v By @G_Man_Official")
  print(f'{yellow}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')


def nphish():
  try:
    os.system("cd && git clone https://github.com/Nishant2009/NPhish")
    os.system("cd termux_hackinglab_setup")
  except:
    print(red + "[!] Error Occured While Installing")

def sqlmap():
  try:
    os.system("cd $HOME && git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap-dev && cd termux_hackinglab_setup")
  except:
    print(red + "[!]Unable To Install SQLMAP install it Manually")
    
def installing_tools():
  ask = input("Do you want to install some basic termux tools?(Y/N): ")
  if ask == 'y' or ask == 'Y':
    nphish()
    seeker()
    sqlmap()
  else:
    print("Everything is fine in your termux [/\]")
    print("exiting........")
    time.sleep(1.5)
    os.system("clear")
    exit()


def seeker():
    try:
        subprocess.run(["git", "clone", "https://github.com/thewhiteh4t/seeker.git"], check=True, cwd=os.path.expanduser("~"))

        # Give executable permission to install.sh script
        subprocess.run(["chmod", "+x", os.path.expanduser("~/seeker/install.sh")], check=True)

        print(green + "[*] Seeker Tool Installed Successfully")

    except subprocess.CalledProcessError as e:
        print(red + "Unable To Install Seeker. Error Message:")
        if e.stderr:
            print(e.stderr.decode("utf-8"))
        else:
            print("Unknown error occurred")
    except Exception as e:
        print(red + "[!] Error Occurred While Installing Seeker:")
        print(str(e))

def camhack():
  try:
    subprocess.run(["git", "clone", "https://github.com/KasRoudra/CamHacker"], check=True, cwd=os.path.expanduser("~"))
    print(green + "[*] CamHacker Tool Installed Successfully")
  except subprocess.CalledProcessError as e:
    print(red + "Unable To Install CamHacker. Error Message:")
    if e.stderr:
        print(e.stderr.decode("utf-8"))
    else:
        print("Unknown error occurred")

  except Exception as e:
        print(red + "[!] Error Occurred While Installing CamHacker:")
        print(str(e))

def proxy():
  try:
    subprocess.run(["git", "clone", "https://github.com/mishakorzik/Free-Proxy"], check=True, cwd=os.path.expanduser("~"))
    print(green + "[*] FreeProxy Tool Installed  ")
  except subprocess.CalledProcessError as e:
    print(red + "Unable To Install FreeProxy. Error Message:")
    if e.stderr:
        print(e.stderr.decode("utf-8"))
    else:
        print("Unknown error occurred")

  except Exception as e:
        print(red + "[!] Error Occurred While Installing FreeProxy:")
        print(str(e))

def cloudflare():
  try:
    subprocess.run(["git", "clone", "git clone https://github.com/BHUTUU/cloudflare-ui"], check=True, cwd=os.path.expanduser("~"))
    print(green + "[*] Cloudflare-ui Tool Installed Successfully")
  except subprocess.CalledProcessError as e:
    print(red + "Unable To Install Cloudflare-ui. Error Message:")
    if e.stderr:
        print(e.stderr.decode("utf-8"))
    else:
        print("Unknown error occurred")

  except Exception as e:
        print(red + "[!] Error Occurred While Installing Cloudflare-ui:")
        print(str(e))
if __name__ == '__main__':
  try:
    os.system("clear")
    banner()
    installing_tools()
    seeker()
    nphish()
    camhack()
    proxy()
    sqlmap()
  except KeyboardInterrupt:
    line_print("\n" + green + "Thanks for using This Tool!\n" + no_colour)
