from DataDestroy import Delete
from rw import get
from rw import wrt

def SettingsMenu():
    print("Welcome to settings! Here is what you can do!")
    print("DATANUKE, QUIT, NAMECHANGE")
    selected = input("Select one: ")
    if selected == "DATANUKE":
        delxd = Delete()
        if delxd == "DELETED":
            exit(0)
    if selected == "QUIT":
        return "Done!"
    if selected == "NAMECHANGE":
        newname = input("Enter a new name: ")
        wrt({
        "user": newname,
        "platform": get('platform'),
        "gamecoins": get('gamecoins'),
        "firsttime?": get('firsttime?'),
        "completedpyquiz": "false"
        })
        return "Done!"


