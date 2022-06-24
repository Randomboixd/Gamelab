import random
import time
import json

def get(data): # Declare function to get game data
    with open('gamedata.json', 'r') as file:
        Back = json.load(file)

    return Back[data]

def wrt(data): # Declare Function to Write game data. so you dont need to see with open('gamedata', 'w') as file: all around the code
    with open('gamedata.json', 'w') as file:
        json.dump(data, file, indent=4)

def FreeCredit(Launchcode):
    if Launchcode == 846:
        credits = random.randint(0, 10)
        print("You have to wait 30 seconds to get your free Credits!")
        print(f"Your Credit amount:{str(credits)}")


        time.sleep(10)
        reward = get('gamecoins') + credits
        windata = {
            "user": get('user'),
            "platform": get('platform'),
            "gamecoins": reward,
            "firsttime?": get('firsttime?')
        }
        wrt(windata)
        return "WIN"
    else:
        print("ERR_NOT_A_VALID_LAUNCH_KEY")
        return "ERROR"