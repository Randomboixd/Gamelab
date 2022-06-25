import time
# Import WRT Classes
from rw import wrt
from rw import get


def question1():
    print("What type is Python? (Compiled, Interpreted)")
    quess = input("Enter one from the following Choices! ")
    if quess == "Interpreted":
        print("You are right! Giving Flag to main code!")
        return "FLAG"
    if quess == "Compiled":
        print("Technically is compiled. but mostly its interpreted.")
        return "LOSE"

def question2():
    print("What Version is python. (Just the first number not the last 2)")
    quess = input("Enter A number: ")
    res = str(quess)
    if res == "3":
        print("Nice! You Got the flag! Returning Flag to main Code!")
        return "FLAG"
    else:
        print("Not quite!")
        return "LOSE"
#    if quess == 3:
#        print("Nice! You Got the flag! Returning Flag to main Code!")

def question3():
    print("How do you get the zen of python? (enter the import command)")
    quess = input("Enter the method: ")
    if quess == "import thsi":
        print("Easter egg found! Randomboi sometimes types thsi insted of this! Because of this get the flag!")
        return "FLAG"
    if quess == "import this":
        print("Yep! Thats it! Returning FLAG")
        return "FLAG"
    else:
        print("Thats not right!")
        return "LOSE"
    

def quiz(launchcode):
    if launchcode == 69424:
        print("Welcome to the python quiz! Ready to start?")
        readytostart = input("yes or NO: ")
        if readytostart == "yes":
            first = question1()
            if first == "FLAG":
                print("Good Job! Proceeding to next question")
                second = question2()
                if second == "FLAG":
                    print("Nice! One last Question!")
                    hype = question3()
                    if hype == "FLAG":
                        print("YOU WIN!!!")
                        return "VICTORY"
                    else:
                        print("Aw man! Failed at last question?")
                        print("No GameCredits?")
                        return "LOSE"
                else:
                    print("Aw man that was close!")
                    return "LOSE"
            if first == "LOSE":
                print("Aw man! You lost!")
                return "LOSE"
        else:
            print("Game Canceled by user.")
            return "Canceled"
    else:
        print("invalid launch code!")
        time.sleep(5)
        return "INVALID_LAUNCH_CODE"
        