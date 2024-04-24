# Stellar Multitool is proudly coded by @swedewtf & @rinfys
# Multitool maintained/updated by @swedewtf and @rinfys

import util.blocker
import util.description
import util.infograb
from util.logintoken import __tokenlogin__
import util.managetokens
import util.massdm
import util.nitrogen
import util.nuke
import util.profile
import util.servernamechange
import util.stellarify
import util.vansniper
import util.tokenjoiner
import util.tokenleaver
import util.tokenprofile
import util.tokenraider
import util.tokenvalidate
import util.webhookcontrol
import util.opendisc
import util.massreport

from util.plugins.pluh import slowprint
from colorama import Fore, Style, init

init(convert=True)
import os
import time

red = Fore.RED + Style.BRIGHT
green = Fore.GREEN + Style.BRIGHT
blue = Fore.BLUE + Style.BRIGHT
white = Fore.WHITE

version = "1.0.0"

def main():
    os.system('title Stellar Multitool |^| .gg/stellarx')
    os.system('cls || clear')
    slowprint(f"{blue}Welcome to Stellar...")
    time.sleep(1)
    print(fr"""{blue}          
                                    
                                  ██████╗████████╗███████╗██╗     ██╗      █████╗ ██████╗ 
                                 ██╔════╝╚══██╔══╝██╔════╝██║     ██║     ██╔══██╗██╔══██╗
                                 ╚█████╗    ██║   █████╗  ██║     ██║     ███████║██████╔╝
                                  ╚═══██╗   ██║   ██╔══╝  ██║     ██║     ██╔══██║██╔══██╗
                                 ██████╔╝   ██║   ███████╗███████╗███████╗██║  ██║██║  ██║
                                 ╚═════╝    ╚═╝   ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ x     
                                                                   
 > {white}developed by @swedewtf, @rinfys,                                                        {white}Educational purposes only{blue} <  
 > {white}({blue}DSC{white}){blue} Discord.gg/stellarx                                                                           {white}({blue}placeholder{white}){blue} <
 > {white}({blue}?{white}){blue} Feature Description                                                                  {white}({blue}current version: {version}{white}){blue} <     
╔═══════════════════════════════════════╦═══════════════════════════════════╦════════════════════════════════════════╗
║     {white}({blue}01{white}){blue} > Webhook Control            ║     {white}({blue}07{white}){blue} > block all friends      ║     {white}({blue}13{white}){blue} > Token Login                 ║
║     {white}({blue}02{white}){blue} > Profile control            ║     {white}({blue}08{white}){blue} > mass DM all friends    ║     {white}({blue}14{white}){blue} > Token management            ║
║     {white}({blue}03{white}){blue} > Guild name changer         ║     {white}({blue}09{white}){blue} > Nitro generator        ║     {white}({blue}15{white}){blue} > Token Profile changer       ║
║     {white}({blue}04{white}){blue} > Stellar-ify profile >_<    ║     {white}({blue}10{white}){blue} > Vanity url sniper      ║     {white}({blue}16{white}){blue} > Token server joiner         ║
║     {white}({blue}05{white}){blue} > Mass report account        ║     {white}({blue}11{white}){blue} > Token validator        ║     {white}({blue}17{white}){blue} > Token server raider         ║
║     {white}({blue}06{white}){blue} > Account nuker              ║     {white}({blue}12{white}){blue} > Account info           ║     {white}({blue}18{white}){blue} > Next Page                   ║
╚═══════════════════════════════════════╩═══════════════════════════════════╩════════════════════════════════════════╝
""")

    choice = str(input(fr"{blue}stellar{white}@{blue}root{white}~${blue} "))
    if choice == '1' or choice == '01':
        webhook = str(input(f"{blue}[{white}S{blue}]{white} Enter webhook URL: "))
        webhookchoice = str(input(f"{blue}[{white}S{blue}]{white} What would you like to do?\n{blue}[{white}1{blue}]{white} Spam webhook\n{blue}[{white}2{blue}]{white} Delete webhook\nChoice: "))
        if webhookchoice == '1' or webhookchoice == '01':
            util.webhookcontrol.spam_webhook(webhook)
        elif webhookchoice == '2' or webhookchoice == '02':
            util.webhookcontrol.delete_webhook(webhook)
        else:
            print(f"{red}[!] Invalid input, please try again")
            main()
    elif choice == '2' or choice == '02':
        util.profile.profile()
    elif choice == '3' or choice == '03':
        util.servernamechange.servernamechange()
    elif choice == '4' or choice == '04':
        util.stellarify.stellarify()
    elif choice == '5' or choice == '05':
        util.massreport.massreport()
    elif choice == '6' or choice == '06':
        util.nuke.nuke()
    elif choice == '7' or choice == '07':
        util.blocker.blocker()
    elif choice == '8' or choice == '08':
        util.massdm.massDM()
    elif choice == '9' or choice == '09':
        util.nitrogen.generate()
    elif choice == '10':
        util.vansniper.snipe()
    elif choice == '11':
        util.tokenvalidate.validate()
    elif choice == '12':
        util.infograb.grabinfo()
    elif choice == '13':
        __tokenlogin__()
    elif choice == '14':
        util.managetokens.choices()
    elif choice == '15':
        print("Still under development")
        time.sleep(3)
        main()
    elif choice == '16':
        print("Still under development")
        time.sleep(3)
        main()
    elif choice == '17':
        print("Still under development")
        time.sleep(3)
        main()
    elif choice == '18':
        print("The second page can be accessed by purchasing our premium version in our discord")
        time.sleep(3)
        main()
    elif choice == '?':
        util.description.describe()
    elif choice == "dsc":
        util.opendisc.open()
    else:
        print(f'{red}[!] Invalid Command')
        input("Press any key to go back to start...")
        main()

main()
