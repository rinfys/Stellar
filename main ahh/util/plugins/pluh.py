# Stellar Multitool is proudly coded by @swedewtf, @rinfys and @crxelty (no longer active)
# Multitool maintained/updated by @swedewtf and @rinfys

from colorama import Fore, Style, init
init(convert=True)
from util.plugins.pluh import *

red = Fore.RED + Style.BRIGHT
green = Fore.GREEN + Style.BRIGHT
blue = Fore.BLUE + Style.BRIGHT
white = Fore.WHITE

import sys
import time
import requests
from colorama import Fore, Style, init
init(convert=True)

def slowprint(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)
def quickprint(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.03)
        
def tokencheck(token):
    url = 'https://discord.com/api/v9/users/@me'
    headers = {
        "Authorization": token,
        "Content-Type": "application/json",
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print(f"{green}[*] Valid Token{blue}")
    else:
        print(f"{red}[!] Invalid Token{blue}")
        time.sleep(3)
        __import__("Stellar").main()

