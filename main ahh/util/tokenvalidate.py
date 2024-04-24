# Stellar Multitool is proudly coded by @swedewtf, @rinfys and @crxelty (no longer active)
# Multitool maintained/updated by @swedewtf and @rinfys

from colorama import Fore, Style, init
init(convert=True)
from util.plugins.pluh import *

red = Fore.RED + Style.BRIGHT
green = Fore.GREEN + Style.BRIGHT
blue = Fore.BLUE + Style.BRIGHT
white = Fore.WHITE

def validate():
    token = input("Enter token to validate: ")
    tokencheck(token)
    input("Press anything to continue...")
    __import__("Stellar").main()