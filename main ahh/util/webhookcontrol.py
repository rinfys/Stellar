# Stellar Multitool is proudly coded by @swedewtf, @rinfys and @crxelty (no longer active)
# Multitool maintained/updated by @swedewtf and @rinfys

from colorama import Fore, Style, init
init(convert=True)
import requests
import time
import threading
import Stellar

red = Fore.RED + Style.BRIGHT
green = Fore.GREEN + Style.BRIGHT
blue = Fore.BLUE + Style.BRIGHT
white = Fore.WHITE

threads = []

def spam_webhook(webhook):
    message = input(f"{blue}[{white}S{blue}]{white} Enter message to send to webhook: ")
    while True:
        requests.post(webhook, json={'content': message})
        print(f"{green}[+] Sent " + message + "to " + webhook)
def delete_webhook(webhook):
    try: 
        requests.delete(webhook)
        print(f"{green}[+] Deleted " + webhook)
        input(f"{blue}[{white}S{blue}]{white} Press anything to continue...")
        Stellar.main()
    except Exception as e:
        print(f"{red}[!] We ran into an error: {e}")
