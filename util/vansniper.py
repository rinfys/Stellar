# Stellar Multitool is proudly coded by @prettykills, @rinfys and @crxelty (no longer active)
# Multitool maintained/updated by @prettykills and @rinfys

from colorama import Fore, Style, init
init(convert=True)
from util.plugins.pluh import *
import Stellar

red = Fore.RED + Style.BRIGHT
green = Fore.GREEN + Style.BRIGHT
blue = Fore.BLUE + Style.BRIGHT
white = Fore.WHITE

def change_vanity(code: str, server_id: str, token: str) -> bool:
    response = requests.patch(
        f"https://discord.com/api/v9/guilds/{server_id}/vanity-url",
        headers={"authorization": token},
        json={"code": code},
    )
    if response.ok:
        print(f"Updated invite successfully, your server can now be accessed by 'discord.gg/{code}'. ")
        return True
    else:
        print(f"Failed to update vanity url. Status code: {response.status_code}")
        return False


def check_vanity(code: str) -> bool:
    response = requests.get(f"https://discord.com/api/v9/invites/{code}")
    if response.status_code == 404:
        return True
    else:
        return False


def snipe() -> None:
    token = input("Token: ")
    code = input("Vanity url to snipe: ")
    server_id = input("Server ID: ")

    try:
        while check_vanity(code=code) == True:
            if change_vanity(code, server_id, token) == True:
                print(f"Sucessfully changed vanity url '.gg/{code}'")


    except KeyboardInterrupt:
        pass