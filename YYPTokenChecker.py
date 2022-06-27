import tkinter
import requests, colorama, os, inspect, json, time, ctypes, threading
from colorama import Fore, init
from tkinter import Tk
from tkinter.filedialog import askopenfilename

good = 0
bad = 0

Tk().withdraw()
root = tkinter.Tk()
root.withdraw()

def res():
    while 1:
        TokenChecker()
        time.sleep(2)
        os.system("pause")


def TokenChecker():
    global verify, unverify, tokensline, good, bad, combonumber, tokensline
    os.system("cls")
    ctypes.windll.kernel32.SetConsoleTitleW("Token Checker by YYP#6761")
    design = """
\u001b[38;5;46m                                                 ▄▄▄▄▀ \u001b[38;5;47m████▄ \u001b[38;5;48m█  █▀ \u001b[38;5;49m▄███▄   \u001b[38;5;50m   ▄   
\u001b[38;5;46m                                              ▀▀▀ █    \u001b[38;5;47m█   █ \u001b[38;5;48m█▄█   \u001b[38;5;49m█▀   ▀  \u001b[38;5;50m    █  
\u001b[38;5;46m                                                  █    \u001b[38;5;47m█   █ \u001b[38;5;48m█▀▄   \u001b[38;5;49m██▄▄    \u001b[38;5;50m██   █ 
\u001b[38;5;46m                                                 █     \u001b[38;5;47m▀████ \u001b[38;5;48m█  █  \u001b[38;5;49m█▄   ▄▀ \u001b[38;5;50m█ █  █ 
\u001b[38;5;46m                                                ▀      \u001b[38;5;47m      \u001b[38;5;48m  █   \u001b[38;5;49m▀███▀   \u001b[38;5;50m█  █ █ 
\u001b[38;5;46m                                                       \u001b[38;5;47m      \u001b[38;5;48m ▀    \u001b[38;5;49m        \u001b[38;5;50m█   ██ 
\u001b[38;5;46m                                                    Made by YYP#6630
                                    


    """
    
    print(design)
    time.sleep(3)
    while True:
        combo_filename = askopenfilename(filetypes=(("Text File", "*.txt"), ("All Files", "*.*")), title="Choose Your unchecked TokensList!")
        try:
            with open(combo_filename, 'r') as UseFile:
                tokensline = sum(1 for _ in UseFile)
            break
        except:
            print(f'{Fore.RED} [{Fore.LIGHTGREEN_EX}-{Fore.RED}] Not existing combo File')
            time.sleep(1)
            continue

    def pathcheck1():
        if os.path.exists("Valid.txt"):
            print("")

        else:
            with open("Valid.txt", "a") as i:
                i.write("")

    def pathcheck2():
        if os.path.exists("NotValidTokens.txt"):
            print("")

        else:
            with open("NotValidTokens.txt", "a") as i:
                i.write("")

    pathcheck1()
    pathcheck2()

    try:
        with open(combo_filename, 'r') as UseFilee:
            tokens = UseFilee.readlines()
            for x in tokens:
                token = x.rstrip()
                api = requests.get('https://discordapp.com/api/v6/users/@me/library', headers={'authorization': token})
                if api.status_code == 200:
                    ctypes.windll.kernel32.SetConsoleTitleW(f"Checked: {good}/{tokensline} | Accounts: {good} | Unverify: {bad} |")
                    good += 1
                    res = requests.get('https://discordapp.com/api/v6/users/@me', headers={'Authorization': token,'Content-Type': 'application/json'})

                    res_json = res.json()
                    user_name = f'{res_json["username"]}#{res_json["discriminator"]}'
                    phone_number = res_json['phone']
                    email = res_json['email']
                    mfa_enabled = res_json['mfa_enabled']
                    verified = res_json['verified']
                    
                    
                    print(f"\u001b[38;5;46m╠\u001b[38;5;47m══\u001b[38;5;48m[To\u001b[38;5;49mken\u001b[38;5;50m\u001b[38;5;51m]═>\u001b[38;5;7m\u001b[38;5;46m {token} \n            \u001b[38;5;46m╠\u001b[38;5;47m══\u001b[38;5;48m[User\u001b[38;5;49mName\u001b[38;5;50m\u001b[38;5;51m]═>\u001b[38;5;7m {user_name} \n            \u001b[38;5;46m╠\u001b[38;5;47m══\u001b[38;5;48m[E-\u001b[38;5;49mMail\u001b[38;5;50m\u001b[38;5;51m]═>\u001b[38;5;7m {email} \n            \u001b[38;5;46m╠\u001b[38;5;47m══\u001b[38;5;48m[Num\u001b[38;5;49mber\u001b[38;5;50m\u001b[38;5;51m]═>\u001b[38;5;7m {phone_number} \n            \u001b[38;5;46m╠\u001b[38;5;47m══\u001b[38;5;48m[Ver\u001b[38;5;49mified\u001b[38;5;50m\u001b[38;5;51m]═>\u001b[38;5;7m {verified} \n            \u001b[38;5;46m╠\u001b[38;5;47m══\u001b[38;5;48m[Mfa\u001b[38;5;49mSecurity\u001b[38;5;50m\u001b[38;5;51m]═>\u001b[38;5;7m {mfa_enabled} \n")
                    with open('Valid.txt', 'a') as c:
                        c.write(f'{token}\n')
                    ctypes.windll.kernel32.SetConsoleTitleW(f"Checked: {good}/{tokensline} | Accounts: {good} | Unverify: {bad} |")
                    
                elif api.status_code == 401:
                    ctypes.windll.kernel32.SetConsoleTitleW(f"Checked: {good}/{tokensline} | Accounts: {good} | Unverify: {bad} |")
                    bad += 1
                    with open('NotValidTokens.txt', 'a') as v:
                        v.write(f'{token}\n')
                    ctypes.windll.kernel32.SetConsoleTitleW(f"Checked: {good}/{tokensline} | Accounts: {good} | Unverify: {bad} |")
                    
                    

    except:
        print("")


res()
