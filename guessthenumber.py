import random
import time
import json

def get(data): # Declare function to get game data
    with open('gamedata.json', 'r') as file:
        Back = json.load(file)

    return Back[data]

def GTM(launchcode):
    if launchcode == 348:
        print("Welcome to guess the number!")
        time.sleep(2)
        a = random.randint(0, 5)
        print("A Number Has been Generated! its between 0 and 5")
        b = input("Your Guess: ")

        if a == b:
            print("You WON! Returning with + 3 GameCredits")
            gmc = get('gamecoins') + 3
            return gmc
        else:
            print(f"Not quite! It was {str(a)}!")
    else:
        print("Not A valid Launch Code!")
