from operator import add # So + works
import os # Importing os for OS Related Features
import json # Importing JSON for data storing.
import time # Good for some stuff
# Import Game Classes.
from guessthenumber import GTM # Import Guess the number from guessthenumber.py
from freecredit import FreeCredit # Import the freecredit module from freecredit file
from Settings import SettingsMenu # Import settings menu
from pythonquiz import quiz # Import quiz
from Shop import Shop # import shop
# Import Read/Write Classes
from rw import wrt
from rw import get
from rwshop import wrts
from rwshop import gets
from presencerw import getr
from presencerw import rwr
# Import File Generate Jsons
from genfile import Genfiles


Genfiles()

def clear(): # Clearing is a lil harder since WINDOWS and LINUX uses diffrent syntax
    if get('platform') == "WINDOWS":
        os.system('cls')
    if get('platform') == "LINUX":
        os.system('clear')


if get('platform') == "ASK": # Reads from file to get os. If not defined ask.
    print("Whats your platform? (needed for: Operating system exclusive stuff)")
    oprsys = input('WINDOWS or LINUX: ')

    if oprsys == "WINDOWS": # If the user Specified WINDOWS then write that to the file!
        wrt({
            "user": "ASK",
            "platform": "WINDOWS",
            "gamecoins": 1,
            "firsttime?": "true",
            "completedpyquiz": "false"
        })
    if oprsys == "Windows": # If the user Specified WINDOWS then write that to the file!
        wrt({
            "user": "ASK",
            "platform": "WINDOWS",
            "gamecoins": 1,
            "firsttime?": "true",
            "completedpyquiz": "false"
        })
    if oprsys == "windows": # If the user Specified WINDOWS then write that to the file!
        wrt({
            "user": "ASK",
            "platform": "WINDOWS",
            "gamecoins": 1,
            "firsttime?": "true",
            "completedpyquiz": "false"
        })
    if oprsys == "LINUX": # Same as above just for LINUX
        wrt({
            "user": "ASK",
            "platform": "LINUX",
            "gamecoins": 1,
            "firsttime?": "true",
            "completedpyquiz": "false"
        })
    if oprsys == "Linux": # Same as above just for LINUX
        wrt({
            "user": "ASK",
            "platform": "LINUX",
            "gamecoins": 1,
            "firsttime?": "true",
            "completedpyquiz": "false"
        })
    if oprsys == "linux": # Same as above just for LINUX
        wrt({
            "user": "ASK",
            "platform": "LINUX",
            "gamecoins": 1,
            "firsttime?": "true",
            "completedpyquiz": "false"
        })

clear()

def Setup(): # First time set up!
    print("Welcome to GAMELAB! I'll ask you a question and we'll be ready!")
    usrname = input("Whats your username (I Will call you that): ")
    print(f"Nice name {usrname}!")
    print("Do you wanna enable rich presence?")
    Genfiles()
    prs = input("Yes or No: ")
    if prs == "Yes":
        prs = "Yes"
    else:
        prs = "No"
    wrt({
        "user": usrname,
        "platform": get('platform'),
        "gamecoins": 1,
        "firsttime?": "false",
        "completedpyquiz": "false"
    })
    rwr({
    "on": prs,
    "clientid": "990194726122692688",
    "normallargeimage": "gamelabicon",
    "gtmlargeimage": "guess"
    })
    time.sleep(3)
    print("Nice Im ready!")
    print("Lets get started!")
    time.sleep(2)
    clear()
    if getr('on') == "Yes":
        from pypresence import Presence
        RPC = Presence(getr('clientid'))
        RPC.connect()
        RPC.update(state="Playing Gamelab", details="Just playing gamelab.", large_image=getr('normallargeimage'))
    Mainmenu()

if getr('on') == "Yes":
    from pypresence import Presence
    RPC = Presence(getr('clientid'))
    RPC.connect()
    RPC.update(state="Playing Gamelab", details="Just playing gamelab.", large_image=getr('normallargeimage'))
def Mainmenu():
    print(f"Welcome to gamelab @{get('user')}!") # Welcomes the user
    print()
    print(f"Your GameCredits:{get('gamecoins')}") # Tells the user how much gamecoins he has
    print()
    print("Games: ")
    print()
    print(f" 1,Guess the number 2, Free Credits! 3, Python Quiz (Completed:{get('completedpyquiz')} ) 4,Settings 5, Shop 6, EXIT")
    gametoplay = input("Enter the number of the game you wanna play: ") # Lets user choose a game
    if gametoplay == "1": # If user selects GTM then
        clear() # Clear Screen
        guessit = GTM(348) # Launch GTM with startcode 348 (I made that up myself. its only for verifying.)
        if guessit == "WIN": # If the code returns WIN then do these
            clear()
            print(f"Congrats for the win! @{get('user')}!")
            print("12 GameCredits was added to your game account!")
            time.sleep(6)
            clear()
        if guessit == "LOSE": # else.
            print(f"Nice try. Unfortunately that wasnt good.")
            time.sleep(6)
            clear()
    if gametoplay == "2": # If user select Freecredits then launch freecredit()
        clear()
        freecreditslool = FreeCredit(846)
        if freecreditslool == "WIN":
            print("You got Your Credits!")
            time.sleep(6)
            clear()
        if freecreditslool == "LOSE":
            print("The funny thing is: You cant lose. so im writing this as a useless thing")
            # yes im stupid

    if gametoplay == "3":
        if get('completedpyquiz') == "true":
            print("You cant do this! Because you already completed the quiz! Reset Your Account if you wanna play again")
            time.sleep(5)
        else:
            clear()
            quizzlol = quiz(69424)
            if quizzlol == "VICTORY":
                print("VICTORY! 30 GameCredits was added to your account!")
                reward = get('gamecoins') + 30
                if gets('item1') == "owned":
                    reward = reward * 2
                wrt({
                    "user": get('user'),
                    "platform": get('platform'),
                    "gamecoins": reward,
                    "firsttime?": "false",
                    "completedpyquiz": "true"
                })
                time.sleep(6)
                clear()
            if quizzlol == "LOSE":
                print("Unfortunately You lose! You can still Retry.")
                time.sleep(5)
            if quizzlol == "Canceled":
                print("No QUIZ!")
                print("No coins were added to your account. You can still Retry.")
                time.sleep(5)
    if gametoplay == "4":
        clear()
        settings =  SettingsMenu()
        if settings == "Done!":
            print("Settings Saved!")
    if gametoplay == "5":
        clear()
        shoplol = Shop()
        if shoplol == "purchaseditem1":
            print("Congratulations on your Purchase for Double GameCredits!")
            time.sleep(5)
    if gametoplay == "6":
        if getr('on') == "Yes":
            RPC = Presence(getr('clientid'))
            RPC.connect()
            RPC.update(state="Quitting gamelab.")
            time.sleep(2)
            RPC.close()
        print("Quitting...")
        time.sleep(3)
        quit(0)
        
    clear()
    Mainmenu()

if get('firsttime?') == "true":
    Setup()
else:
    Mainmenu()
