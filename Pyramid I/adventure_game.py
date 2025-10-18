import time
import sys
import random
import re
import gameUtils as gu
import randomSequence as rs
import randomRoom as rr


def aqueduct_tunnel_random_sequence():
    initialText = "As you are swimming down this tunnel, the tunnel branches off into multiple tunnels."

    travelText = ["As you are swimming dont the tunnel, you approach yet another set of tunnels",
                  "You are stopped when you reach a fork in the path.",
                  "You have been swimming for a long time.\nAfter a few hours, you reach a fork in the path.",
                  "You travel down the path, but it appears that it ends very soon. You must choose your new path wisely.",
                  "You have been traveling down these tunnels for hours,\nAnother set of tunnels appear in front of you.",
                  "It seems you are lost. Trying to find your way back, you find a completely new network of tunnels."]

    lostText = ["You have lost your way.\nYou have no idea how you got here, and you have no idea where you are. As you run out of light, you are stranded in the middle of the tunnel.",
                "You quickly get lost. It has been hours and you just cant seem to find your way back.\nFinally, you just cant swim any longer and drown."]

    failTunnel = random.randint(0, 3) == 1

    rs.randomSequence(initialText, travelText, minSteps=2, maxSteps=4, roomOdds=0, initialVerbArr=[
                      "take the", "swim down the", "choose the", "travel down the", "pick the"], hallwayNameArr=["tunnel"], autoFail=failTunnel, lostTextArr=lostText)


def long_hallway(matches):
    firstTime = True
    iterations = 1
    while matches > 1:
        # print(f"(this is your {iterations} hallway)")
        if(firstTime):
            gu.text(
                f"You have taken the long path.\nYour only source of light is matches, and you only have {matches} of them, so make sure to use them wisely.\nWith that in mind, you are now faced with a desicion of which path to take.")
        else:
            hallwayName = random.choice(rs.hallwayNames)
            textSequences = [f"After a short venture you have landed in another set of {hallwayName}s to choose.",
                             "After a short venture you have landed in another set of doors to choose from.",
                             f"You soon discover that this {hallwayName} ends and branches off into multiple {hallwayName}s",
                             f"After traveling for a considerable time, you have made it to another set of {hallwayName}s.\nYou now have a desicion to make: ",
                             f"You have reached the end of this path, and now must choose what {hallwayName}s to take."]
            matches = matches-1
            gu.text(
                f"{random.choice(textSequences)}\n(You only have {matches} matches left)")

        firstTime = False

        if(random.randint(0, 14) == 3 and iterations > 3):
            gu.success(1,
                       "After hours of travelling, you have finally made it to the entrance of pharo's tomb!")
        else:
            rs.askRandomHallway()
        iterations = iterations + 1

    gu.end("The path that It took to make it to the tomb was long.\nSo long in fact, that you have run out of matches and are out of light.")


def map_game_path():
    matches = random.randint(5, 20)
    gu.text(f"You have the map. However, without your flashlight, all you have for light are matches.\n\nThe map has 2 paths that lead to the pharo's tomb.\nA path that is long but far less dangerous, and a shortcut, that is very dangerous.")
    resp = gu.ask("take the LONG PATH or the SHORT PATH")
    if(resp == "long path"):
        long_hallway(matches)
    elif(resp == "short path"):
        minutes = 3
        gu.text("You travel down the shortcut until you reach a room. The door is locked and the walls begin closing in. You have 3 minutes to find the key to open the door")
        resp = gu.ask("LOOK ON THE WALL or BUST THE DOOR down")
        if(resp == "look on the wall"):
            gu.text(
                "You see a brick; press it and you find a key. But it’s the wrong one. 2 minutes left")
            resp = gu.ask("PICKLOCK THE DOOR or LOOK IN THE CHEST")
            if(resp == "picklock the door"):
                gu.end("The door successfully opens, however, because the door was locked, it triggers a large bolder, that falls to the ground and blocks your path. You are now stuck.")
            if(resp == "look in the chest"):
                if(random.randint(0, 1) == 0):
                    gu.text(
                        "You find a key in the chest, and try to unlock the door, but it is the wrong one. 2 minutes left")
                    resp = gu.ask(
                        "LOOK ON THE OTHER WALL or BUST THE DOOR down")
                    if(resp == "look on the other wall"):

                        gu.text(
                            "You see several bricks indented into the wall. You only have 1 minute left.")
                        resp = gu.ask(
                            "press the TOP BRICK, the LEFTMOST BRICK, the CENTER BRICK, or the RIGHTMOST BRICK")

                        if(random.randint(0, 10) == 3):
                            gu.text(
                                "You a key inside of the brick.\nYou try to open the door and it opens.\nYou are almost there. The pharo's tomb is just beyond this room.")
                            rr.randomRoom()
                            gu.success(2)
                        else:
                            rand = random.randint(0, 3)
                            if(rand == 0):
                                gu.end(
                                    "You press the brick only to find that it is empty. 0 minutes left")
                            elif(rand == 1):
                                gu.end(
                                    "You press the brick, but that only causes the entire wall to collapse. 0 minutes left")
                            elif(rand == 2):
                                gu.end(
                                    "You press the brick, but the brick wont budge. You attempt to chip the brick out of the wall, but you run out of time.")
                            else:
                                gu.end(
                                    "You find a key, and run towards the door, but as you do, you run out of time. ")

                    elif(resp == "bust the door down"):
                        gu.end(
                            "You partially bust the door down, but the force of the blow was so great that a massive amount of debris prevents you from opening the door.")

                else:
                    gu.end(
                        "You look in the chest and take up 2 minutes. You find a crowbar to pry the door open with, but the door still won’t open.")
        if(resp == "bust the door"):
            gu.text(
                "It takes 2 minutes to open the door, but the door wont budge. 1 minute left")
            resp = gu.ask("LOOK IN THE CHEST or SEARCH THE FLOOR")
            if(resp == "look in the chest"):
                gu.end("The chest is empty. 0 minutes left.")
            elif(resp == "search the floor"):
                gu.end("You search the floor, but find nothing. 0 minutes left.")


start_text = "\n\n\n\n"+gu.icon
start_text = start_text
gu.revealLines(start_text)
time.sleep(0.4)
gu.revealLines(gu.formatLineLength("You are sitting inside the walls of the great pyramid of Giza. After three years of hard work, you have finally found the entrance of this 600 foot tall pyramid. " +
                                    "Your mission is to find all 4 (North, South, East and West) entrances to the tomb of the pharoh." +
                                    "\n\nThis pyramid has many pathways, adventures and pitfalls. Choose wisely.\n\n" +
                                    "Also be aware that no 2 adventures will be exactly the same... Your journey may be different, even if you took the same path you did before."))

if(not gu.fastMode):
    time.sleep(1)
input("\nPress Enter to start...")
# =======================


entranceName = random.choice(
    ["a grand entrance", "a large hallway leading", "an entrance"])

gu.text("As you "+random.choice(["step into", "walk into", "enter"])+" the "+random.choice(["great ", ""])+"pyramid, " +
        "you are encompassed by 2 "+random.choice(["large ", ""])+"entrances..." +
        "\nThere is "+entranceName+" to the EAST, and "+entranceName+" to the WEST.")


resp = gu.ask("GO EAST or GO WEST")
if(resp == "go east"):
    gu.text(
        "You approach a room with a "+random.choice(["locked ", ""])+"door and a key on the wall attatched to a chain.")
    resp = gu.ask("PICKLOCK THE DOOR or TAKE THE KEY")
    if(resp == "picklock the door"):
        gu.text(f"The walls {random.choice(['start to',''])} collapse, {random.choice(['and','as'])} the ceiling also begins to collapse. You dont have much time to lose!\nYou could enter the room, in hopes that it would lead somewhere, but you also see an aqueduct filled with water, covered by a grate fixed to the floor.")
        resp = gu.ask("ENTER THE ROOM or JUMP DOWN THE GRATE")
        if(resp == "enter the room"):
            if(random.randint(0, 1) == 0):
                gu.end(
                    "The room is completely empty with no doors or windows of any kind. You are now stuck in the room.")
            else:
                gu.end(
                    "You enter the room and are about to find another exit when the entire ceiling collapses.")
        elif(resp == "jump down the grate"):
            randomNumber = random.randint(0, 10)
            if(randomNumber == 3):
                gu.end(
                    "You attempt to pry the grate open, but it wont budge. You get crushed by the collapsed ceiling.")
            elif(randomNumber == 4):
                gu.end(
                    "You pry the grate open and jump in, but the current is so strong that you drown.")
            else:
                gu.text(
                    "You swim down the aqueduct a good distance. But all you can find is a narrow passage, completely submerged underwater.")
                resp = gu.ask("GO DOWN THE PASSAGE or KEEP SWIMMING")
                if(resp == "go down the passage"):
                    gu.end("You find nothing, and begin rapidly running out of breath. you try to turn back, but the strong current and the smooth walls of the tunnel prevent you from escaping and you drown.")
                elif(resp == "keep swimming"):
                    aqueduct_tunnel_random_sequence()
                    gu.text(
                        "You swim for hours, taking twists and turns and eventually find a grate fixed to the ceiling")
                    resp = gu.ask(
                        "attempt to REACH THE GRATE or FIND ANOTHER EXIT")
                    if(resp == "reach the grate"):
                        gu.text(
                            "You fall, and your flashlight breaks. All you have left now, is a box of matches.")
                        resp = gu.ask("TRY AGAIN or FIND ANOTHER EXIT")
                        if(resp == "try again"):
                            gu.end("You try again and fall. This time your box of matches gets carried away in the current. You have no light. Without light there is no way to escape the pyramid and you get stuck.")
                        elif(resp == "find another exit"):
                            aqueduct_tunnel_random_sequence()
                            gu.text("You search to find another grate and eventually, you do.\nAfter prying the grate open with much force, you find yourself in a long hallway.\nUnfortunately, your flashlight runs out of batteries and you are left without any light.\nLuckily, however you thought you saw a row of torches lined against the wall. If you can find one you may be able to see again.\nThe only problem would be not setting off the booby traps.")
                            resp = gu.ask(
                                "GO DOWN THE HALLWAY or FIND A TORCH to light")
                            if(resp == "go down the hallway"):
                                gu.end(
                                    "You go down the hallway, but with limited light, trip a wire and send poison darts your way.")
                            elif(resp == "find a torch"):
                                gu.success(3,
                                           "You light the torch and see the wires you could have stepped on. You carefully step over them and find yourself standing at the doorway to pharos’s tomb.")
                    elif(resp == "find another exit"):
                        aqueduct_tunnel_random_sequence()
                        gu.end(
                            "You keep swimming but never find an exit.\nYou grow tired and as your last match goes out, you become stuck in the pyramid without light.")
    elif(resp == "take the key"):
        gu.text("You rip the key off the chain and attempt to open the door, but It won’t open.\nApparently The key isn’t the right one.")
        resp = gu.ask("LOOK FOR ANOTHER KEY or GO SOMEWHERE ELSE")
        if(resp == "look for another key"):
            gu.text("As you look around, you discover 2 chests.")
            resp = gu.ask("Open the FIRST CHEST or open the SECOND CHEST")
            if(resp == "first chest"):
                gu.end("You open the chest and find a scorpion in it.")
            elif(resp == "second chest"):
                gu.text(
                    "You open the second chest and find a map. You can only keep it if you get rid of your flashlight.")
                resp = gu.ask(
                    "KEEP THE MAP, but get rid of your flashlight, or LEAVE THE MAP")
                if(resp == "keep the map"):
                    map_game_path()
                elif(resp == "leave the map"):
                    gu.text("You travel, forward, but as you do, you end up lost.")
                    resp = gu.ask("TRACE YOUR WAY BACK or CONTINUE")
                    if(resp == "trace your way back"):
                        rs.randomSequence()
                        gu.text("You have been searching for hours and are still lost. " +
                                "However, you see 2 doorways. One of which seems odly familiar")
                        resp = gu.ask(
                            "enter the LEFT DOORWAY, or enter the RIGHT DOORWAY?")
                        if(resp == "left doorway"):
                            gu.end(
                                "You enter the doorway. As you are travelling down the hall, you accidentally step on an elevated plate, that sends crossbows your way.")
                        else:
                            gu.end("The door does seem familliar, however the rest of the surroundings do not.\n" +
                                   "As you attempt to turn back, your foot trips a wire that opens up the floor underneath you. " +
                                   "Before you have a chance to realise what just happened, you fall right into a pit of snakes.")
                    if(resp == "continue"):
                        rs.randomSequence(maxSteps=7)
                        gu.end("You continue, but you get so lost you end up trapped in the pyramid. After travelling for several more ours, your flashlight goes out, and you are out of light.")
        elif(resp == "go somewhere else"):
            # if(random.randint(0,1) == 0):
            rs.randomSequence(roomOdds=0.15)
            gu.text("You discover a staircase and discover A key. However it is up high and very difficult to reach. You also see a narrow passage way.")
            resp = gu.ask("TAKE THE KEY and attempt to unlock the door, or TRAVEL DOWN THE PASSAGE instead")
            if(resp == "take the key"):
                rs.randomSequence(initialText="You have succesfully unlocked the door! "+
                "You enter, and find yourself wondering what kind of strange path this doorway will lead you to...\n", autoFail=True)
            elif(resp == "travel down the passage"):
                rs.randomSequence()
                gu.text("You travel down into a large banquet hall and find 2 doorways sitting on the back wall")
                resp = gu.ask("go LEFT or go RIGHT")
                if(resp == "left"):
                    gu.end("You cross the path but fall under some broken boards")
                elif(resp == "right"):
                    gu.end(
                        "The wall has closed behind you. And the only other way to go is a locked door, unfortunately you didn’t take the key.")
elif(resp == "go west"):
    gu.text("As you travel down the hallway, you find a room and see and a door with a code wheel.\nA code cypher is lying next to it. You examine the cypher and see some of the markings on the decipher scroll have worn off.\nOne of the characters could either be a bird or a snake.")
    resp = gu.ask("choose the BIRD or choose the SNAKE")
    if(resp == "bird"):
        gu.text("The code is correct.\nA door opens in front of you. As you enter, you notice a large hallway.\nHowever, a large basin of crocodiles is preventing you from reaching it.")
        resp = gu.ask(
            "SWIM AROUND the crocodiles or attempt to CLIMB THE WALL")
        if(resp == "swim around"):
            gu.text("You make it over the crocodiles, barely missing them.\nYou make it to a seemingly empty wall, but soon discover 3 bricks, each engraved with a unique symbol.")
            resp = gu.ask(
                "press the brick with the LION, press the brick with the SPHINX, or press the brick with the STAFF")
            if(resp == "sphinx"):
                gu.text("You press on the stone with a hieroglyphic of a Sphinx.\n\nAn entrance opens up, and a staircase appears before you.\nYou have barely descended down the stairs when your flashlight runs out of batteries.\nLuckily you saw a torch hanging on the wall just before your flashlight went out")
                resp = gu.ask("TAKE THE TORCH or USE YOUR MATCHES")
                if(resp == "take the torch"):
                    gu.text(
                        "As you pull the torch off of its hook, it opens up a trap door")
                    resp = gu.ask("TAKE THE TRAP DOOR or GO DOWN THE STAIRS")
                    if(resp == "take the trap door"):
                        gu.text(
                            "You decide to take the door. As you travel down the hallway, you, notice a dangerous, rickety old bridge")
                        resp = gu.ask(
                            "CROSS THE BRIDGE or carefully HAND OVER HAND underneath the rope railings")
                        if(resp == "cross the bridge"):
                            gu.end(
                                "You cross the bridge After about 3 steps, the floorboards snap beneath you, and you fall.")
                        elif(resp == "hand over hand"):
                            rs.randomSequence(
                                initialText="You make it across. However, you realize a large maze of tunnels was waiting for you on the other end. With lots to explore.", autoFail=True)
                    elif(resp == "go down the stairs"):
                        gu.text("You go down the stairs and they turn into a slide.\nYou slip down the steps, finally reaching the bottom.\nAfter surveying your surroundings, you discover that the floor beneath you is engulfed sharp spikes.")
                        resp = gu.ask(
                            "attempt to CLIMB UP over them or look for a way to DISARM THEM")
                        if(resp == "climb up"):
                            gu.end(
                                "You try to climb up over the spikes, but you end up falling.")
                        elif(resp == "disarm them"):
                            gu.text(
                                "You attempt to disarm the spikes.\nAs you look across the wall for something.\nYou see an indented brick, and a piece of rope sticking out of the wall.")
                            resp = gu.ask("PUSH THE BRICK or PULL THE ROPE")
                            if(resp == "push the brick"):
                                if(random.randint(0, 1) == 0):
                                    rs.randomSequence(
                                        initialText="You push the brick, and the spikes retract into the floor. You make it out into the hallway, and find yourself in a maze of tunnels.", minSteps=3, maxSteps=16)
                                    gu.text(
                                        "As You make it out of the maze of tunnels, you find yourself in a room with a large, dark, and ominous looking door. You see a key on the wall, and a torch on the wall.")
                                    resp = gu.ask(
                                        "TAKE THE KEY or TAKE THE TORCH")
                                    if(resp == "take the key"):
                                        gu.end(
                                            "You take the key, but the pressure off of the hook sets of a series of booby traps.")
                                    elif(resp == "take the torch"):
                                        gu.success(4,
                                                   "You take the torch off the wall, and immediately after, the door opens up.\nYou travel down the hallway, and find yourself at the foot of the entrance to the pharaoh's tomb.")
                                else:
                                    gu.end(
                                        "You push the brick, but as you do, it causes the room collapse.")
                            elif(resp == "pull the rope"):
                                gu.end(
                                    "You pull the rope, but that only causes the door behind you to close, trapping you in. You soon run out of matches, leaving you out of light.")
                elif(resp == "use your matches"):
                    gu.text("All you have for light now are matches. You travel down the stairs, but soon realize you are low on matches. Prior to burning through your twelfth match, you notice a long piece of twine, connected to the ceiling.")
                    resp = gu.ask(
                        "LIGHT THE TWINE or KEEP USING YOUR MATCHES")
                    if(resp == "light the twine"):
                        gu.text(
                            "The twine ignites a set of lamps that illuminate the room.\nYou see a door on the other side of the room, however, there is a thin iron beam encompassed by a deep shaft blocking your path to the door. All is not lost however, for as you look upwards, you also notice a rope that you can swing across in order to play it safe.")
                        resp = gu.ask(
                            "CROSS THE BEAM and hope you can keep your balance, or SWING USING THE ROPE")
                        if(resp == "cross the beam"):
                            gu.end("You cross the precarious beam, and see a light at the end of the tunnel.\nThe pharaoh’s tomb is close, just across the long hallway.\nAs you attempt to cross the last stretch of the beam, you slip and fall down the deep shaft.")
                        elif(resp == "swing using the rope"):
                            gu.end(
                                "You swing across the rope, but as you do, the rope snaps.")
                    elif(resp == "keep using your matches"):
                        gu.end(
                            "It’s much harder to see with only matches, failing to see the path, you misstep down a deep shaft.")

            elif(resp == "lion"):
                rs.randomSequence(
                    initialText="You pressed on the stone with a hieroglyphic of a lion.\n\nAn entrance opens up, and as you enter, you find yourslef in a large maze of tunnels.")
                gu.end("You continue traveling...\nAs you are running down a one of the hallways you hear a loud thud. As you turn around, you quickly realize that the door behind you has closed, leaving you trapped in a dead end.")
            elif(resp == "staff"):
                gu.end(
                    "You enter the room and proceed down the hallway, but suddenly fall into a pit covered in leaves, with a tiger.")
        elif(resp == "climb the wall"):
            gu.end(
                "You scale the wall, but one-foot slips, with a crocodile waiting for you at the bottom.")
    elif(resp == "snake"):
        gu.text(
            "You find a large room. Upon entering it, You see small idol standing on a pedestal.")
        resp = gu.ask("TAKE THE IDOL, DONT TAKE IT or LOOK AROUND FIRST")
        if(resp == "take the idol"):
            gu.end("You take the idol, which triggers another trap. The walls close shut and a flood of water fills the room.")
        elif(resp == "dont take it"):
            gu.end("Upon leaving the room, a trap was set off You leave the room only to find it locked behind you. A large bolder comes from the ceiling and falls down.")
        elif(resp == "look around first"):
            gu.text("You look around and find a rock.")
            resp = gu.ask("TAKE THE ROCK to the pedistal, or KEEP SEARCHING")
            if(resp == "take the rock"):
                gu.end(
                    "You take the rock and replace it with the idol; however, a key was required to prevent the trap from being set")
            elif(resp == "keep searching"):
                gu.text("You find a chest with a key. You may need this.")
                resp = gu.ask(
                    "TAKE THE ROCK AND THE KEY you found to the pedistal, or LEAVE WITH THE KEY")
                if(resp == "take the rock and the key"):
                    gu.text(
                        "You take the rock to the pedestal, but before you do you notice a keyhole. You enter the key into the keyhole and then take the idol.")
                    resp = gu.ask(
                        "LEAVE THE WAY YOU CAME or GO A DIFFERENT WAY")
                    # if(random.randint(0, 1) == 0):
                    if(resp == "leave the way you came"):
                        rs.randomSequence(initialText="It turns out you got lost. Your only option is to go thru one of these doors.")
                        gu.text("You see the way back. It is just just beyond this room.")
                        rr.randomRoom(autoFail=True)
                    
                    else:
                        rs.randomSequence(initialText="You decide to take a different path. As you travel down a new corridor, you notice a few more places you would like to explore.")
                        gu.text("You exit the room. As you travel down the path you find that you cannot pursue it any further because of a large pit. You notice at the end of the tunnel, one of the entrances to the pharos’s tomb.")
                        resp = gu.ask("SWING BY A VINE or TURN BACK")
                        if(resp == "swing by a vine"):
                            gu.end("The vine snaps")
                        elif(resp == "turn back"):
                            gu.text(
                                "You turn back but as you do your flashlight goes out. You are without light.")
                            resp = gu.ask(
                                "use my MATCHES or use my GLOWSTICKS")
                            if(resp == "matches"):
                                gu.end(
                                    "Oops! You must have lost your matches You are now out of light...")
                            elif(resp == "glowsticks"):
                                gu.end(
                                    "It appears your glowsticks are out. You are now out of light...")
                elif(resp == "leave with the key"):
                    gu.end("You take the key with you and leave the room You travel down several hallways. Eventually you happen upon one of the entrances to the pharaohs tomb. However, in order to unlock the door you need the idol.")
