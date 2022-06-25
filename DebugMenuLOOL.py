from operator import add
from rw import get
from rw import wrt
from rwshop import wrts
from rwshop import gets
from DataDestroy import Delete
from freecredit import FreeCredit
from pythonquiz import quiz

def DebugMenu():
    print("Enter HELP for All Commands.")
    action = input("> ")
    if action == "HELP":
        print("Here are ALL THE COMMANDS!")
        print("Randomboixd.Debug.ChangeCoin")
        print("Randomboixd.Debug.Reset")
        print("Randomboixd.Debug.Quizstart")
        print("Randomboixd.Debug.EXIT")
        print("Randomboixd.Debug.FORFREE")
    if action == "Randomboixd.Debug.ChangeCoin":
        valueforcoin:int = input("Enter Amount: ")
        gc:int = get('gamecoins')
        give = int(gc) + int(valueforcoin)
        give = int(give)
        final = {
            "user": get('user'),
            "platform": get('platform'),
            "gamecoins": give,
            "firsttime?": get('firsttime?'),
            "completedpyquiz": get('completedpyquiz')
        }
        wrt(final)
        print("done")
    if action == "Randomboixd.Debug.Reset":
        Delete("DEBUG")
    if action == "Randomboixd.Debug.Quizstart":
        final = {
            "user": get('user'),
            "platform": get('platform'),
            "gamecoins": get('gamecoins'),
            "firsttime?": get('firsttime?'),
            "completedpyquiz": "false"
        }
        wrt(final)
        print("Now Exit to get back to settings and then the main menu!")
    if action == "Randomboixd.Debug.EXIT":
        print("Exiting NOW")
        return "DONE"
    if action == "Randomboixd.Debug.FORFREE":
        print("Making all items in shop FREE")
        wrts({
            "item1": "notowned",
            "item1price": 0
        })
        print("If you already had the item it will be removed.")
    DebugMenu()

