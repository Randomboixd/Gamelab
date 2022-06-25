import random
import time
import json
# Import WRT Classes
from rw import wrt
from rw import get
from rwshop import gets
from rwshop import wrts

def FreeCredit(Launchcode):
    if Launchcode == 846:
        credits = random.randint(0, 10)
        if gets('item1') == "owned":
            credits = credits * 2
        print("You have to wait 30 seconds to get your free Credits!")
        print(f"Your Credit amount:{str(credits)}")


        time.sleep(10)
        reward = get('gamecoins') + credits
        windata = {
            "user": get('user'),
            "platform": get('platform'),
            "gamecoins": reward,
            "firsttime?": get('firsttime?'),
            "completedpyquiz": "false"
        }
        wrt(windata)
        return "WIN"
    else:
        print("ERR_NOT_A_VALID_LAUNCH_KEY")
        return "ERROR"