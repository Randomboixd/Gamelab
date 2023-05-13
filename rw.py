# What is RW? Its a Read / Write Library i made just for this app.

import json
def get(data): # Declare function to get game data
    with open('gamedata.json', 'r') as file:
        Back = json.load(file)

    return Back[data]

def wrt(data): # Declare Function to Write game data. so you dont need to see with open('gamedata', 'w') as file: all around the code
    with open('gamedata.json', 'w') as file:
        data["clientid"] = "no" # 2023 Change: NO CLIENT ID!
        json.dump(data, file, indent=4)
