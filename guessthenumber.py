import random
import time
import json
from rw import wrt
from rw import get

def GTM(launchcode):
    if launchcode == 348:
        print("Welcome to guess the number!")
        time.sleep(2)
        a = random.randint(0, 3)
        print(f"A Number Has been Generated! its between 0 and 3 For Debug Purposes:{str(a)}")
        b = input("Your Guess: ")
        a = int(a)
        b = int(b)

        if a == b:
            print("You WON! Returning with + 12 GameCredits")
            gmc = get('gamecoins') + 12
            wrt({
                "user": get('user'),
                "platform": get('platform'),
                "gamecoins": gmc,
                "firsttime?": get('firsttime?'),
                "completedpyquiz": get('completedpyquiz')
            })
            time.sleep(5)
            return "WIN"
        else:
            print(f"Not quite! It was {str(a)}!")
            time.sleep(5)
    else:
        print("Not A valid Launch Code!")
