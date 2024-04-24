# Stellar Multitool is proudly coded by @swedewtf, @rinfys and @crxelty (no longer active)
# Multitool maintained/updated by @swedewtf and @rinfys

from colorama import Fore, Style, init
init(convert=True)
import requests
import openai

red = Fore.RED + Style.BRIGHT
green = Fore.GREEN + Style.BRIGHT
blue = Fore.BLUE + Style.BRIGHT
white = Fore.WHITE

def runchatgpt():
    print(f"{blue}[{white}S{blue}]{white} Before using chatGPT, you need to enter your api key which you can find at https://platform.openai.com/account/api-keys")
    openai.api_key = input('Enter API key: ')
    messagesong = [ {"role": "system", "content": 
              ""} ]
    while True:
        messageong = input("Enter a message : ")
        if messageong:
            messagesong.append(
                {"role": "user", "content": messageong},
            )
            chat = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", messages=messagesong
            )
        reply = chat.choices[0].message.content
        print(f"ChatGPT: {reply}")
        messagesong.append({"role": "assistant", "content": reply})
