import json
import time
# Import Read/Write Classes
from rw import wrt
from rw import get
from rwshop import wrts
from rwshop import gets
from presencerw import getr
from presencerw import rwr
    
def Delete(launch):
    if launch == "Settings":
        print("ARE YOU SURE YOU WANNA DELETE YOUR DATA?? YOU WILL LOSE:")
        if gets('item1') == "owned":
            alsoitem1 = ", Your Double GameCredit BOOSTER"
        else:
            alsoitem1 = ""
        print(f"GAMECREDITS:{str(get('gamecoins'))}{alsoitem1}!")
        choice = input('Yes or No: ')
        if choice == "Yes":
            print("Destroying data")
            time.sleep(5)
            wrt({
                "user": "ASK",
                "platform": "ASK",
                "gamecoins": 0,
                "firsttime?": "true",
                "completedpyquiz": "false"
            })
            wrts({
                "item1": "notowned",
                "item1price": 10
            })
            rwr({
                "on": "Ask",
                "clientid": "0",
                "normallargeimage": "gamelabicon",
                "gtmlargeimage": "guess"
            })
            print("Done!")
            exit(0)
        if launch == "DEBUG":
            print("ARE YOU SURE YOU WANNA DELETE YOUR DATA?? YOU WILL LOSE:")
            if gets('item1') == "owned":
                alsoitem1 = ", Your Double GameCredit BOOSTER"
            else:
                alsoitem1 = ""
            print(f"GAMECREDITS:{str(get('gamecoins'))}{alsoitem1}!")
            choice = input('Yes or No: ')
            if choice == "Yes":
                print("Destroying data")
                time.sleep(5)
                wrt({
                    "user": "ASK",
                    "platform": "ASK",
                    "gamecoins": 0,
                    "firsttime?": "true",
                    "completedpyquiz": "false"
                })
                wrts({
                    "item1": "notowned",
                    "item1price": 10
                })
                print("Done!")
                exit(0)
