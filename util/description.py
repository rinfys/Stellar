# Stellar Multitool is proudly coded by @swedewtf, @rinfys and @crxelty (no longer active)
# Multitool maintained/updated by @swedewtf and @rinfys

from colorama import Fore, Style, init
init(convert=True)
from util.plugins.pluh import quickprint, slowprint
import time

red = Fore.RED + Style.BRIGHT
green = Fore.GREEN + Style.BRIGHT
blue = Fore.BLUE + Style.BRIGHT
white = Fore.WHITE

def describe():
    choice = input("Which feature do you want a description of?\nChoice: ")
    if choice == "1" or choice == "01":
        quickprint(f"{white}Webhook control. This feature allows you to control or delete webhooks that have been made in servers using their url. All you need to input is which choice you'd like and the url of the webhook.")
    elif choice == "2" or choice == "02":
        quickprint(f"{white}Custom status changer. This feature allows you to change the status of a user. All you need to input is their token.")
    elif choice == "3" or choice == "03":
        quickprint(f"{white}Guild name changer. This changes the name of a specific guild by using the token of an admin in that server. We plan on optomising this feature in the future.")
    elif choice == "4" or choice == "04":
        quickprint(f"{white}Profile stellar-ify-er. Changes entire profile to be stellar related, nukes account, blocks all friends, etc.")
    elif choice == "5" or choice == "05":
        quickprint(f"{white}Token login. Log into an account using the accounts token. Launches chrome and logs you into the account 100% automatically. Once you're logged in, the only way to be logged out is if the account owner logs you out.")
    elif choice == "6" or choice == "06":
        quickprint(f"{white}Account nuker. Changes language, theme, settings, unfriends everyone, etc.")
    elif choice == "7" or choice == "07":
        quickprint(f"{white}Block all friends. Uses user token to block all of the account's friends.")
    elif choice == "8" or choice == "08":
        quickprint(f"{white}MassDM all friends. DMs all of the account's friends with a custom message you choose. Option to block them all after.")
    elif choice == "9" or choice == "09":
        quickprint(f"{white}Nitro generator. Choosing this option will automatically start randomly generating discord nitro codes. Once the generator finds a code that is valid it will automatically stop generating and it will display the code.")
    elif choice == "10":
        quickprint(f"{white}Fake stellar rat. Writes a new file which is identical to the existing Stellar file, but is a virus. Once someone runs this file it will send all of the user's information to a discord bot in a server.")
    elif choice == "11":
        quickprint(f"{white}Token validator. Enter a discord token and it will check whether or not this token is a valid token. If it is, it will return the information of this token.")
    elif choice == "12":
        quickprint(f"{white}Account information. Enter a discord token and gain information about this account. If the account has nitro, it will return the billing information of the account, including the credit card number, address, full name, etc...")
    elif choice == "13":
        quickprint(f"{white}Token login. Enter a discord token and login to the token's account. It automtically starts chrome and logs in automatically.")
    elif choice == "14":
        quickprint(f"{white}Token management. Allows you to edit your stored tokens in your Stellar. You can purge invalid tokens, add new tokens or view current tokens.")
    elif choice == "15":
        quickprint(f"{white}Token profile changer. This option allows you to change the profile of every token you have stored to the same profile.")
    elif choice == "16":
        quickprint(f"{white}Token server joiner. This option makes every valid stored token join a server of your choice.")
    elif choice == "17":
        quickprint(f"{white}Token server raider. Allows every token in a server to spam messages, threads, reactions, etc..")
    elif choice == "18":
        quickprint(f"{white}Next page. Opens the second page")
    elif choice == "20":
        quickprint(f"{white}ChatGPT. Literally just chatgpt LOL")
    else:
        slowprint(f"{red}Invalid choice.")
        time.sleep(3)
        __import__("Stellar").main()

    input("Press anything to continue...")
    __import__("Stellar").main()