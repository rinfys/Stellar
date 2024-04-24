# Stellar Multitool is proudly coded by @swedewtf, @rinfys and @crxelty (no longer active)
# Multitool maintained/updated by @swedewtf and @rinfys


from colorama import Fore, Style, init

init(convert=True)
import requests
import Stellar
from util.plugins.pluh import *

red = Fore.RED + Style.BRIGHT
green = Fore.GREEN + Style.BRIGHT
blue = Fore.BLUE + Style.BRIGHT
white = Fore.WHITE

def servernamechange():
    token = input("Enter targets token: ")
    tokencheck(token)
    guild_id = input("Enter target guild id: ")
    new_name = input("Enter new guild name: ")
    headers = {
        "Authorization": token,
        "Content-Type": "application/json",
    }

    data = {
        "name": new_name
    }

    requests.patch(f"https://discord.com/api/v9/channels/{guild_id}", json=data, headers=headers)
    input("Press any key to go back to start...")
    Stellar.main()