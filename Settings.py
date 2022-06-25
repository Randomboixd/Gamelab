from DataDestroy import Delete
from rw import get
from rw import wrt
from DebugMenuLOOL import DebugMenu

def SettingsMenu():
    print("Welcome to settings! Here is what you can do!")
    print("DATANUKE, QUIT, NAMECHANGE")
    selected = input("Select one: ")
    if selected == "DATANUKE":
        delxd = Delete("Settings")
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
    if selected == "DebugConsole":
        print("You found the DEBUG CONSOLE! This menu was made for @Randomboixd! But hey you can use it!")
        DebugMenu()
        return "DONE"



