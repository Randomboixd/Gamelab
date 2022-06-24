import os # Importing os for OS Related Features
import json # Importing JSON for data storing.
import time
from guessthenumber import GTM
from freecredit import FreeCredit
from Settings import SettingsMenu


def get(data): # Declare function to get game data
    with open('gamedata.json', 'r') as file:
        Back = json.load(file)

    return Back[data]

def wrt(data): # Declare Function to Write game data. so you dont need to see with open('gamedata', 'w') as file: all around the code
    with open('gamedata.json', 'w') as file:
        json.dump(data, file, indent=4)
    
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
            "gamecoins": 0,
            "firsttime?": "true"
        })
    if oprsys == "LINUX": # Same as above just for LINUX
        wrt({
            "user": "ASK",
            "platform": "LINUX",
            "gamecoins": 0,
            "firsttime?": "true"
        })

clear()

def Setup(): # First time set up!
    print("Welcome to GAMELAB! I'll ask you a question and we'll be ready!")
    usrname = input("Whats your username (I Will call you that): ")
    print(f"Nice name {usrname} Let me write that down and I'll be ready!")
    wrt({
        "user": usrname,
        "platform": get('platform'),
        "gamecoins": 0,
        "firsttime?": "false"
    })
    time.sleep(3)
    print("Nice Im ready!")
    print("Lets get started!")
    time.sleep(2)
    clear()
    Mainmenu()

def Mainmenu():
    print(f"Welcome to gamelab @{get('user')}!")
    print(f"Your GameCredits:{get('gamecoins')}")
    print("Games: ")
    print(" 1,Guess the number 2, Free Credits! 3,Settings")
    gametoplay = input("Enter the number of the game you wanna play!")
    if gametoplay == "1":
        clear()
        guessit = GTM(348)
        if guessit == "WIN":
            clear()
            print(f"Congrats for the win! @{get('user')}!")
            print("3 Gamecoins was added to your game account!")
            time.sleep(6)
            clear()
        if guessit == "LOSE":
            print(f"Nice try. Unfortunately that wasnt good.")
            time.sleep(6)
            clear()
    if gametoplay == "2":
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
        clear()
        SettingsMenu()
        
    clear()
    Mainmenu()

if get('firsttime?') == "true":
    Setup()
else:
    Mainmenu()
