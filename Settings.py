from DataDestroy import Delete

def SettingsMenu():
    print("Welcome to settings! Here is what you can do!")
    print("DATANUKE, QUIT")
    selected = input("Select one: ")
    if selected == "DATANUKE":
        delxd = Delete()
        if delxd == "DELETED":
            exit(0)
    if selected == "QUIT":
        print("Cant exit without making a loop! You'll have to relaunch the app!")
        exit(0)

