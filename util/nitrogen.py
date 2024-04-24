# Stellar Multitool is proudly coded by @swedewtf, @rinfys and @crxelty (no longer active)
# Multitool maintained/updated by @swedewtf and @rinfys

import requests
from colorama import Fore, Style, init
init(convert=True)
import random, string
from util.plugins.pluh import *

red = Fore.RED + Style.BRIGHT
green = Fore.GREEN + Style.BRIGHT
blue = Fore.BLUE + Style.BRIGHT
white = Fore.WHITE

def generate():
    while True:
        code = "".join(random.choices(string.ascii_uppercase+string.ascii_lowercase+string.digits, k=16))
        codetry = requests.get(f"https://discord.com/api/v9/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true",timeout=10)
        if codetry.status_code in list(range(200,300)):
            print(f"{green}discord.gift/{code} is valid!")
            input("Press anything to continue")
            return
        else:
            print(f"{red}discord.gift/{code} was invalid!")