import time
import sys
import random
import re
import hashlib

#SETTINGS ===========================================================
fastMode = False #Used for development
debugMessages = False #Used for development
#====================================================================

# Your input string
player_steps = []
seededRandom = random.Random(0)

def hashSteps():
    # Create a hash object using SHA-256
    hash_object = hashlib.sha256("\n".join(player_steps).encode())
    # Convert the hash object to an integer
    hash_integer = int.from_bytes(hash_object.digest(), 'big')
    return hash_integer

def addStep(step):
    player_steps.append(step)
    if(debugMessages):
        print("STEPS:",player_steps,"HASH:",hashSteps())
    seededRandom.seed(hashSteps())
    



if(fastMode):
    print("Turbo mode: ON\nYou can select options via number keys.\n(1 = first option, 2 = second option and so forth)")

askedPreviously = True

endIcon = "\n░\        ∕░|\n░ \      ∕ ░|\n░  \ __ ∕  ░|\n░   |  |   ░|\n_==*    *==_|"

icon = """                                                         
                                                                            
                                          ▓▒                                    
                           █           ██▓▒░░▒                                  
                         ██▒░▓        ███▒▒▒▒▒▒▓                                
                        ▓█▓░░▒░▓    ████▒░░░░▒░░▒▓                              
                      ▓██▒▒▒░▒▒░▒▒██████░░░░░░░░░░▒▒       ▓█                   
                    ▒███▓░░░░▒░▒▒░▒▓███▒░░▒▒▒▓▒▓▓▓▓▓▓▓   ██▒░▒▒░                
                  ░████▓▒▒▒▓▒▓▓▒▒▒▒▓▒█▓░▒▒▒▒▒▒▒▒▒▒▒▒░▒▒███░░░░░░▒░              
                 ██████▒▓▓▒▓▓▓▒▓▓▒▓▒▒▓▒▓▒░▒▒░░░░░░░░░░░░░▓░░░░ ░░░░▒            
               ███████▒░▒░▒▒░▒▒░░░░▒░░░░░▓▓░░░░░░░▒░░▒▒░▒░░▓░░░░ ░░▒▒▒          
             ▓███████▓▓▓▓▓▓▓▓▓▒▓▒▒▒░▒▒░░▒░░▓░▒▒▒▓▓▓▓▓▓▓▓▓▒▒░░▓ ░░▒▓▓▒▓▓█        
           ▒████████▒░░░░░░▒░▒░░░░░▒░▒▒░▒▒▒▓▓█░░▒░▒░░░░░▒░░░▒▒▓█▒▒▒▒▒▒▒▒▒▒░     
         ░█████████░▒▒▓▓▒▓▓▒▒▒▒▒▒▒▒░▒▒░▒▒░▒░░▒▒▒▓▒▒░▒░░▒▒░▒░░░▒░░▒              
          ░▓██████▒▒▒▒▒▒▒▒▒▒▒▒▒░▒░░▒░▒▒▒▒▒▒▒▒▒▒▒▒▓░                                                                                                                                     


====================================================================================================
====================================================================================================
                  _____   _  _   ___      ___   ___   ___     _     _____                                      
                 |_   _| | || | | __|    / __| | _ \ | __|   /_\   |_   _|                                     
                   | |   | __ | | _|    | (_ | |   / | _|   / _ \    | |                                       
                   |_|   |_||_| |___|    \___| |_|_\ |___| /_/ \_\   |_|                                       
                                                                                               
  ___  __   __  ___     _     __  __   ___   ___       ___    ___      ___   ___   ____    _   
 | _ \ \ \ / / | _ \   /_\   |  \/  | |_ _| |   \     / _ \  | __|    / __| |_ _| |_  /   /_\\  
 |  _/  \ V /  |   /  / _ \  | |\/| |  | |  | |) |   | (_) | | _|    | (_ |  | |   / /   / _ \\ 
 |_|     |_|   |_|_\ /_/ \_\ |_|  |_| |___| |___/     \___/  |_|      \___| |___| /___| /_/ \_\\
                                                                                            
====================================================================================================
====================================================================================================
"""


def animation():
    print("\n\n")
    if(fastMode):
        t = 0.005
    else:
        t = 0.05

    sys.stdout.write("                              \r")
    time.sleep(t)
    sys.stdout.write("|                        |    \r")
    time.sleep(t)
    sys.stdout.write("↝                         ↜  \r")
    time.sleep(t)
    sys.stdout.write("  ↝                       ↜  \r")
    time.sleep(t)
    sys.stdout.write("  ↝↝                    ↜↜  \r")
    time.sleep(t)
    sys.stdout.write("    ↝↜↝                ↝↜↜ \r")
    time.sleep(t)
    sys.stdout.write("     ↝↝↜--          --↜↝↜  \r")
    time.sleep(t)
    sys.stdout.write("      ↝↜↝--   ⫷⫸   --↜↜↝  \r")
    time.sleep(t)
    sys.stdout.write("       ↜↝↝-- ⫷⫷⫸⫸ --↜↝↜  \r")
    time.sleep(t*1.4)
    sys.stdout.write("       ↝↜↝--⫷⫷||⫸⫸--↝↜↜  \r")
    time.sleep(t*1.8)
    sys.stdout.write("       ↝↝↜-⫷⫷||||⫸⫸-↜↝↜  \r")
    time.sleep(t*2.2)
    sys.stdout.write("       ↝↜↝╚╛╚╛ § ╚╛╚╛↜↜↝    \r")
    time.sleep(t*2.6)
    sys.stdout.write("      ↜↝↝ ╚╛╚╛ § ╚╛╚╛ ↜↝↜   \r")
    time.sleep(t*3.0)
    sys.stdout.write("     ↝↜↝ ╚╛╚╛░ § ░╚╛╚╛ ↝↜↜  \r")
    time.sleep(t*3.4)
    sys.stdout.write("     ↝↜↝ ╚╛╚╛░-(§)-░╚╛╚╛ ↝↜↜  \r")
    time.sleep(t*3.4)
    sys.stdout.write("    ↝↝↝ ╚╛╚╛░░=(§)=░░╚╛╚╛ ↜↜↜ \r")
    time.sleep(t*3.4)
    sys.stdout.write("   ↝↝↝ ╚╛╚╛░░ =(§)= ░░╚╛╚╛ ↜↜↜ \r")
    time.sleep(0.2)
    sys.stdout.flush()


def revealText(text, speed=0.015): #For asking the user
    text = text.replace("\r", "\n")

    if(fastMode):
        print(text)
        return

    for line in text.split("\n"):
        for character in line:
            sys.stdout.write(character)
            sys.stdout.flush()

            if(character == "." or character == "!" or character == "?" or character == ","):
                time.sleep(speed*6)
            time.sleep(speed)

        sys.stdout.write("\n")
        sys.stdout.flush()
        time.sleep(speed*10)


def revealLines(text, speed=0.11):
    if(fastMode):
        print(text)
        return

    for line in text.split("\n"):
        print(line)
        time.sleep(speed)



def askAndGetAll(text):
    global askedPreviously

    if(not fastMode):
        time.sleep(1.5)

    text = text.replace("?", "")

    val = input(f"\nDo you choose to {text}?\t".replace(
        "to :", "to:").replace(".?", "?").replace(".,", ",")).lower().strip()
    askedPreviously = True

    matches = re.finditer(r"([A-Z0-9]{1,500}\s?){2,100}", text)

    moves = []
    for matchNum, match in enumerate(matches, start=1):
        match = match.group().lower().strip()
        moves.append(match)
        
        if(val == match):
            addStep(match)
            return val,matchNum
        elif(fastMode and val == str(matchNum)):
            val = match.lower().strip()
            print("(You chose \""+val+"\")")
            addStep(match)
            return val,matchNum

    print("That move is invalid. Valid moves are:", moves)
    return askAndGetAll(text)

def ask(text):
    return askAndGetAll(text)[0]

def askFromList(arr):
    val = ":\n\t"
    for i in range(len(arr)):
        delimiter = ",\n\t"
        if(i == len(arr)-2):
            delimiter = ",\n\tor "
        elif(i == len(arr)-1):
            delimiter = ""
        val = val+arr[i]+delimiter

    return askAndGetAll(val)

def formatLineLength(text, maxLength=18):
    # for preserving double line breaks
    text = text.replace("\n", "{line_break}")

    # Add a line break every 100th word
    words = re.sub(r"\s+", " ", text).split(" ")
    text = ""

    word_count = 0
    for i in range(len(words)):
        word_count += 1
        if(words[i].__contains__("{line_break}")):
            word_count = 0

        if(word_count >= maxLength):
            word_count = 0
            text += "\n"
        text += words[i]+" "

    # for preserving double line breaks
    text = text.replace("{line_break}", "\n")
    return text


def text(text):
    global askedPreviously

    text = formatLineLength(text)
    text = text.replace("  ", " ").replace("  ", " ")

    if(not text.endswith("...")):
        text = text+"..."

    text = text.replace(". ...", "...")

    if(askedPreviously == True):
        animation()
        askedPreviously = False
        revealText("\n\n"+text)
    else:
        revealText(text)


def end(text):
    text = formatLineLength(text)
    animation()
    print()
    for line in endIcon.split("\n"):
        print(line)
        time.sleep(0.06)

    if(not fastMode):
        time.sleep(0.5)

    revealLines("\n. . .\n\n"+text)
    if(not fastMode):
        time.sleep(2)
    print("\nTHE END.\n")
    if(not fastMode):
        time.sleep(1)
    exit()


def success(index, text=None):
    if(index == 1):
        direction = "north"
    elif(index == 2):
        direction = "east"
    elif(index == 3):
        direction = "south"
    elif(index == 4):
        direction = "west"

    hanger = f"(This is the {direction} entrance to the pharoh's tomb. Now see if you can find the other 3 entrances...)"
    if(text == None):
        end(
            f"CONGRATULATIONS! You have made it to the entrance of the pharaoh's tomb!\n\n{hanger}")
    else:
        text = formatLineLength(text)
        if(text.__contains__("pharaoh") and text.__contains__("tomb")):
            end(f"{text}\nCONGRATULATIONS! You have made it!\n\n{hanger}")
        else:
            end(f"{text}\nCONGRATULATIONS! You have made it to the pharaoh's tomb!\n\n{hanger}")


def numberToNth(number):
    if(number == 1):
        return "1st"
    elif(number == 2):
        return "2nd"
    elif(number == 3):
        return "3rd"
    else:
        return str(number)+"th"
