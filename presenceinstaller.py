import time
import os
def installer():
    print("Gettings ready!")
    time.sleep(3)
    print("Installing dependencies")
    os.system('python -m pip install pypresence')
    print("Done installing dependencies")
    return "Done"