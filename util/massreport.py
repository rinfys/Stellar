# Stellar Multitool is proudly coded by @swedewtf, @rinfys and @crxelty (crxelty is no longer active)
# Multitool maintained/updated by @swedewtf and @rinfys

from colorama import Fore, Style, init
init(convert=True)
import requests
import time

red = Fore.RED + Style.BRIGHT
green = Fore.GREEN + Style.BRIGHT
blue = Fore.BLUE + Style.BRIGHT
purple = Fore.MAGENTA + Style.BRIGHT
yellow = Fore.YELLOW + Style.BRIGHT
white = Fore.WHITE
def massreport():
    token = input(f"{blue}[{white}S{blue}]{white} Enter user token: ")
    channelid = input(f"{blue}[{white}S{blue}]{white} Enter channel ID: ")
    messageid = input(f"{blue}[{white}S{blue}]{white} Enter message ID: ")
    guildid = input(f"{blue}[{white}S{blue}]{white} Enter guild ID: ")
    reasonong = input(f"{blue}[{white}S{blue}]{white} Enter reason: ")
    run = True
    json={
           "channel_id": channelid,
           "message_id": messageid,
           "guild_id": guildid,
           "reason": reasonong
         }   
    headers = {
                "Accept": '*/*',
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "sv-SE",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
                "Content-Type": "application/json",
                "Authorization": token
              }

    report = requests.post("https://discordapp.com/api/v9/report", json=json, headers=headers)
    if report.status_code == 400:
        print(f'{red}[-] Failed to report user [Error: {report.content}]')