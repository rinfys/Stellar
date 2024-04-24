# Stellar Multitool is proudly coded by @swedewtf, @rinfys and @crxelty (no longer active)
# Multitool maintained/updated by @swedewtf and @rinfys

from colorama import Fore, Style, init
init(convert=True)
from util.plugins.pluh import *
import stellar

red = Fore.RED + Style.BRIGHT
green = Fore.GREEN + Style.BRIGHT
blue = Fore.BLUE + Style.BRIGHT
white = Fore.WHITE

def choices():
    choice = int(input("""What would you like to do:
[1] View tokens
[2] Add token
[3] Purge invalid tokens
Choice: """))
    if choice == 1:
        viewtokens()
    elif choice == 2:
        addtokens()
    elif choice == 3:
        purgetokens()
    else:
        print("Invalid choice, please try again...")
        time.sleep(1)
        choices()

def viewtokens():
    for line in open('util/tokens.txt','r').readlines():
        print(f"{green}{line}", end="")
    input("\nPress anything to continue")

def addtokens():
    token = str(input("Enter token you would like to add: "))
    tokenfile = open("util/tokens.txt", "a")
    tokenfile.write(token + "\n")
    print(f"{green}Added token {token} to tokens.txt")
    secondchoice = int(input("""Would you like to:
[1] Add another token
[2] Go back to token management
[3] Return to Stellar
Choice: """))
    if secondchoice == 1:
        addtokens()
    elif secondchoice == 2:
        choices()
    elif secondchoice == 3:
        Stellar.main()

def purgetokens():
    print("Under development!")