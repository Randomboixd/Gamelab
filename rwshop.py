# same as RW but for the shop json

import json
def gets(data): # Declare function to get game data
    with open('shopsys.json', 'r') as file:
        Back = json.load(file)

    return Back[data]

def wrts(data): # Declare Function to Write game data. so you dont need to see with open('shopsys', 'w') as file: all around the code
    with open('shopsys.json', 'w') as file:
        json.dump(data, file, indent=4)