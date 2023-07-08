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
      
# CHECK INTERNET

socket.setdefaulttimeout(30)


def check_intr(host="8.8.8.8", port=53, timeout=5):
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except socket.error:
        print(f'{red}No internet!')
        time.sleep(2)
        check_intr()

def animate_hashtags():
    hashtags = f'''{green}                       ##########################'''
    while len(hashtags) > 0:
        print(hashtags)
        hashtags = hashtags[:-1]
        time.sleep(0.5)
        print("\033[F\033[K", end="")

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
  print("                       Developer: @G_Man_Official")
  print(f"{cyan}                Telegram :: https://t.me/hacking_network8")
  print(f'{yellow}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')


def check_termux():
  # Install a package using pkg command
  package_name = "proot"
  result = subprocess.run(["pkg", "install", package_name, "-y"], capture_output=True)
  
  if result.returncode == 0:
      print("Package installation successful.")
  else:
      print("Package installation failed. Error message:")
      print("Trying To Change The Repo")
      os.system(f"echo 'deb https://termux.mentality.rip/termux-main stable main stable main' > $PREFIX/etc/apt/sources.list")
      os.system("apt update && apt upgrade -y")
      
if __name__ == "__main__":
  try:
    os.system("clear")
    banner()
    time.sleep(1)
    print(" ")
    print(" ")
    print(f"{blue}                       Setting Up Everything.........")
    animate_hashtags()
    os.system("apt update && apt upgrade -y")
    os.system("termux-setup-storage")
    check_termux()
    os.system("python3 pkg_installer.py")

  except KeyboardInterrupt:
    line_print("\n" + green + "Thanks for using This Tool!\n" + no_colour)

