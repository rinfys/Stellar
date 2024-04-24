# Stellar Multitool is proudly coded by @swedewtf, @rinfys and @crxelty (no longer active)
# Multitool maintained/updated by @swedewtf and @rinfys


from colorama import Fore, Style, init
init(convert=True)
import requests

red = Fore.RED + Style.BRIGHT
green = Fore.GREEN + Style.BRIGHT
blue = Fore.BLUE + Style.BRIGHT
white = Fore.WHITE
 
def join(token):
    header = {"authorization": token, "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}
    response = requests.post("https://discord.com/api/v9/invites/dn7qT8Wm", headers=header)
    print(response.content)

join("NTI3MTA2Mjg2MTA2NTc0ODQ4.GQbAaa.yzGbSNuSim98OnrvijLiIs2Uh93Iph-D6jGyf0")
 