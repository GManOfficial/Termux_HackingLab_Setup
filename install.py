import subprocess
import os 
import sys
from os import system

modules = ['requests', 'colorama', 'setuptools', 'tqdm']

def install_module(module):
    try:
        os.system("pkg update && pkg upgrade -y")
        print(f"Installing {module}")
        subprocess.run(["pip3", "install", module, "--break-system-packages"], check=True)
    except subprocess.CalledProcessError:
        os.system("apt update && apt upgrade -y")
        os.system("")
        print(f"{module} cannot be installed! Install it manually by 'pip3 install {module}'")
        sys.exit(1)

for module in modules:
    try:
        __import__(module)
    except ImportError:
        install_module(module)
    except:
        sys.exit(1)


# Install a package using pkg command
    package_name = "proot"
    result = subprocess.run(["pkg", "install", package_name, "-y"], capture_output=True)

    if result.returncode == 0:
        print("Package installation successful.")
        os.system("python3 start.py")
    else:
        print("Package installation failed. Error message:")
        print("Trying To Change The Repo")
        os.system(f"echo 'deb https://termux.mentality.rip/termux-main stable main stable main' > $PREFIX/etc/apt/sources.list")
        os.system("apt update && apt upgrade -y")
        os.system("python3 start.py")
  
