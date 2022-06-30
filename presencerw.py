import json # Imports The JSON MODULE

def getr(data):
    with open('presenceconfig.json', 'r') as file:
        a = json.load(file)
    return a[data]

def rwr(data):
    with open('presenceconfig.json', 'w') as file:
        json.dump(data, file, indent=4)
