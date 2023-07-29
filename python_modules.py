import subprocess
import sys
import pkg_resources
import os, sys
from tqdm import tqdm

from colorama import Fore, Back, Style
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
      
# List of Python modules to install
modules_to_install = ['requests', 'colorama', 'scrapy', 'lolcat']

banner = f'''{cyan}
 ___             __         __ __            
|   .-----.-----|  |_.---.-|  |  .-----.----.
|.  |     |__ --|   _|  _  |  |  |  -__|   _|
|.  |__|__|_____|____|___._|__|__|_____|__|  
|:  |            Developer ~ @G_Man_Official                            
|::.|            Tool ~ Termux Hacking Lab Setup                            
`---'            For More ~ Join | @hacking_network8
'''
colour = f"{no_colour} "

def install_modules(modules):
    """
    Install missing Python modules.
    """
    print(f"{red}                        Installing missing Python modules...")
    print(f"{yellow} ")
    try:
        command = [sys.executable, "-m", "pip", "install"] + modules
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        progress_bar = tqdm(total=len(modules), unit="module")
        for line in process.stdout:
            progress_bar.update()
        progress_bar.close()
        output, error = process.communicate()
        if process.returncode == 0:
            print(f"{green}All missing Python modules have been installed successfully.")
        else:
            print(f"{red}Failed to install Python modules. Error:", error.decode().strip())
    except subprocess.CalledProcessError as e:
        print(f"{red}Failed to install Python modules. Error:", e)

def check_installed_versions(modules):
    """
    Check installed versions of modules.
    """
    print("\nChecking installed module versions:")
    for module in modules:
        try:
            version = pkg_resources.get_distribution(module).version
            print(f"{cyan}{module}: {version}")
        except pkg_resources.DistributionNotFound:
            print(f"{red}{module} is not installed.")

def uninstall_module(module):
    """
    Uninstall a specific module.
    """
    print(f"{red}\nUninstalling {module}...")
    try:
        command = [sys.executable, "-m", "pip", "uninstall", "-y", module]
        uninstall_result = subprocess.run(command, capture_output=True, text=True)
        if uninstall_result.returncode == 0:
            print(f"{green}{module} has been successfully uninstalled.")
        else:
            print(f"Failed to uninstall {module}. Error:", uninstall_result.stderr.strip())
    except subprocess.CalledProcessError as e:
        print(f"Failed to uninstall {module}. Error:", e)

if __name__ == '__main__':
  try:
    os.system("clear")
    print(banner)
    print(colour)
    # Check if modules are already installed
    missing_modules = []
    for module in modules_to_install:
        try:
            __import__(module)
        except ImportError:
            missing_modules.append(module)

    # Install missing modules
    if missing_modules:
        install_modules(missing_modules)
    else:
        print("All required Python modules are already installed.")

    # Check installed versions of modules
    check_installed_versions(modules_to_install)

    # Uninstall specific module
    module_to_uninstall = 'scrapy'
    uninstall_module(module_to_uninstall)
    os.system("python3 tools_setup.py")
  except KeyboardInterrupt:
    line_print("\n" + green + "Thanks for using This Tool!\n" + no_colour)
