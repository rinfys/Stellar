# Stellar Multitool is proudly coded by @swedewtf, @rinfys and @crxelty (no longer active)
# Multitool maintained/updated by @swedewtf and @rinfys

from colorama import Fore, Style, init
init(convert=True)
from util.plugins.pluh import *
import Stellar

red = Fore.RED + Style.BRIGHT
green = Fore.GREEN + Style.BRIGHT
blue = Fore.BLUE + Style.BRIGHT
white = Fore.WHITE

from selenium import webdriver

def open():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, keep_alive=True)
    driver.get("https://discord.gg/NN96V5u9rQ")