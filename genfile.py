from os.path import exists
import json

#GenfilePackage

def writebasicdata():
    open('gamedata.json', 'a').close()
    with open('gamedata.json', 'w') as file:
        basicdataig = {
            "user": "ASK",
            "platform": "ASK",
            "gamecoins": 0,
            "firsttime?": "true",
            "completedpyquiz": "false"
        }
        json.dump(basicdataig, file, indent=4)
    return "success"

def writeshopdata():
    open('shopsys.json', 'a').close()
    with open('shopsys.json', 'w') as file:
        basicdata = {
            "item1": "notowned",
            "item1price": 10
        }
        json.dump(basicdata,file,indent=4)
    return "success"

def writepresence():
    open('presenceconfig.json', 'a').close()
    with open('presenceconfig.json', 'w') as file:
        basicdata = {
            "on": "Ask",
            "clientid": "990194726122692688",
            "normallargeimage": "gamelabicon",
            "gtmlargeimage": "guess"
        }
        json.dump(basicdata, file, indent=4)

def Genfiles():
    files1real = exists('gamedata.json')
    files2real = exists('shopsys.json')
    files3real = exists('presenceconfig.json')

    if files1real == False:
        print("It seems Your filesystem didnt find gamedata.json! Let me generate them.")
        writebasicdata()

        

    if files2real == False:
        print("It seems Your filesystem didnt find shopsys.json! Let me generate them.")
        writeshopdata()
    
    if files3real == False:
        print("It seems Your filesystem didnt find presenceconfig.json! Let me generate them.")
        writepresence()
