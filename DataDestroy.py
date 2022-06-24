import json
import time

def get(data): # Declare function to get game data
    with open('gamedata.json', 'r') as file:
        Back = json.load(file)

    return Back[data]

def wrt(data): # Declare Function to Write game data. so you dont need to see with open('gamedata', 'w') as file: all around the code
    with open('gamedata.json', 'w') as file:
        json.dump(data, file, indent=4)
    
def Delete():
    print("ARE YOU SURE YOU WANNA DELETE YOUR DATA?? YOU WILL LOSE:")
    print(f"GAMECREDITS:{str(get('gamecoins'))}!")
    choice = input('Yes or No: ')
    if choice == "Yes":
        print("Destroying data")
        time.sleep(5)
        wrt({
            "user": "ASK",
            "platform": "ASK",
            "gamecoins": 0,
            "firsttime?": "true"
        })
        print("Done!")
        return "DELETED"
