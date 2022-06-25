from operator import sub
import time
from rwshop import gets
from rwshop import wrts
from rw import get
from rw import wrt

def purchase1process():
    print("Purchasing...")
    gc = get('gamecoins')
    pr = gets('item1price')
    minusss = sub(gc,pr)
    wrts({
        "item1": "owned",
        "item1price": 10
    })
    wrt({
        "user": get('user'),
        "platform": get('platform'),
        "gamecoins": minusss,
        "firsttime?": get('firsttime?'),
        "completedpyquiz": get('completedpyquiz')
    })

def purchaseitem1():
    print(f"Are you sure you wanna purchase Double Gamecredit? PRICE:{str(gets('item1price'))}?")
    r = input("yes or no: ")
    if r == "yes":
        purchase1process()
        time.sleep(5)
        print("purchased!")
        time.sleep(5)
        return "done"
    else:
        print("Purchase Failed!")
        return "cancel"

def Shop():
    print(f"Welcome to the shop! You currently have {str(get('gamecoins'))} GameCredits!")
    print(f"Listings: 1, Double GAMECREDIT (Bought?: {gets('item1')}) Price:{str(gets('item1price'))}.")
    print("What do you wanna buy?")
    buys = input("Enter the number of what you wanna buy: ")
    sus = str(buys)
    if sus == "1":
        if gets('item1') == "owned":
            print("You already own this!")
            time.sleep(5)
            return "alrowned"
        if get('gamecoins') < gets('item1price'):
            print("You dont have enough GameCredits to buy this!")
            time.sleep(5)
            return "no"
        else:
            purchaseitem1()
            return "purchaseditem1"
    return "done"
        