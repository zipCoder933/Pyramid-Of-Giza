import time
import sys
import re
import gameUtils as gu

seededRandom = gu.seededRandom


class Danger:
    def __init__(self):
        if seededRandom.random() < 0.5:
            self.animal = seededRandom.choice(
                ["booby traps", "holes", "spikes", "poison darts", "crossbows", "loaded-pushplates", "tripwires"]
            )
            self.desc = seededRandom.choice(["deadly", "dangerous","massive", "loaded"])

            self.roomMedium = seededRandom.choice(["long", "large","loaded", ""]) +" "+ seededRandom.choice(["set", "wall", "floor"])
        else:
            self.animal = seededRandom.choice( ["snakes", "crocodiles", "rattlesnakes", "cobras", "tigers"])
            self.desc = seededRandom.choice(["deadly", "wild", "hungry","ferocious", "large","massive","angry","fearsome","scary"])

            roomItem = [
            seededRandom.choice(["shallow pool ","large body","large pool","deep pool"])+" of water", 
            seededRandom.choice(["large","massive", "raised","spiked"])+" floor", 
            seededRandom.choice(["long, narrow ","distant","very narrow"])+" ledge", 
            seededRandom.choice(["narrow", "massive","large","a","deep"])+" pit"]
            self.roomMedium = seededRandom.choice(roomItem)

    def returnOutcome(self, text2, fail, choice):
        if choice == "travel through":
            if fail:
                gu.end(
                    "You attempt to travel through the "
                    + self.animal
                    + ", but to no avail."
                )
            else:
                gu.text(
                    "You succesfully made it through the "
                    + self.desc
                    + " "
                    + self.animal
                    + ". "
                    + text2
                )
                return
        elif choice.__contains__("swing"):
            if fail:
                item = [
                    f"As you swung over the {self.animal}, the vine snapped and you fell to your death.",
                    f"You got very far as you swung over the {self.animal}, however, the vine couldnt swing far enough.",
                ]
                gu.end(seededRandom.choice(item))
            else:
                gu.text("You swung through the " + self.desc + " and made it! " + text2)
                return
        elif choice == "climb" or choice == "scale":
            if fail:
                gu.end(
                    "As you attempted to climb the wall. Unfortunately, you slipped and the "
                    + self.animal
                    + " caught you."
                )
            else:
                gu.text(
                    "After strenuous effort, you climb the wall and barely escape the "
                    + self.animal
                    + ". "
                    + text2
                )
                return
        elif choice.__contains__("jump"):
            if fail:
                gu.end(
                    "You tried to jump over the "
                    + self.animal
                    + ", but the distance was too great."
                )
            else:
                gu.text(
                    "You sucessfully jumped over the "
                    + self.roomMedium
                    + " "
                    + self.animal
                    + ". "
                    + text2
                )
                return
        elif choice == "alternative path":
            if fail:
                item = [
                    "You found another path, and as you entered the passage way, the floor opened up and another set of "
                    + self.animal
                    + " was waiting for you at the bottom.",
                    "You entered into an alternative passage way.\nAs you pursued the hallway down, however, the hallway gave way and collapsed.",
                ]
                gu.end(seededRandom.choice(item))
            else:
                gu.text(
                    "You took an alternative path, instead of crossing the "
                    + self.desc
                    + ". "
                    + text2
                )
                return
        elif choice == "go back" or choice == "turn back":
            if fail:
                item = [
                    "You chose to turn back, and as you entered the passage way, the floor opened up and another set of "
                    + self.animal
                    + " was waiting for you at the bottom.",
                    "You chose to leave the way you came.\nAs you pursued the hallway down, however, the hallway gave way and collapsed.",
                ]
                gu.end(seededRandom.choice(item))
            else:
                gu.text(
                    "You chose to retreat instead of crossing the "
                    + self.animal
                    + ". "
                    + text2
                )
                return
        else:
            if fail:
                gu.end(
                    "You chose to "
                    + choice
                    + ". Unfortunately, the "
                    + self.animal
                    + " caught you."
                )
            else:
                gu.text("You chose to " + choice + ". " + text2)
                return





def aiText(preText, danger):
    roomDesc = [
        "narrow",        "wide",        "heavily furnished",        "impressive",
        "long",        "large",        "tall, deep",        "closed, shallow",
        "trap",        "small",        "dark",        "small",
        "well lit",        "tall",        "deep",
    ]
    roomDesc = seededRandom.choice(roomDesc)

    str = [
        f"""
    You enter down a long corridor, and find yourself in a {roomDesc} room...
    As you enter, you realize that you cannot pass because of a massive {danger.roomMedium} of {danger.desc} {danger.animal} preventing you from crossing.
    If you are careful, you could make it to the next entrance.
    """,

        f"""
    You enter a room, astonished to see a {danger.roomMedium}, filled with {danger.animal}...
    Unsure what to do, you ruminate on what the safest option might be.
    """,

    
            f"As you turn the corner, a {roomDesc} room is waiting for you.\nYou see a doorway up ahead, but your heart sinks when you see the {danger.roomMedium}, full of {danger.animal} that are guarding the entrance.\nIt doesnt look like the egyptians wanted you to get across this one.",
       

        f"""
        You carefully enter a {roomDesc} room.
        As you enter, you almost fall into a {danger.roomMedium} full of {danger.desc} {danger.animal}.
        What do you choose to do next?
    """,

        f"You enter a very {roomDesc} room.\nYou see a doorway up ahead, however, a {danger.roomMedium} of {danger.animal} are blocking the entrance and you dont see any way across.",
       
  
        f"""
        You travel down a long corridor and find yourself in a {roomDesc} room...
        As you enter, you stop dead in your tracks...
        Beneath your feet are some {danger.desc} {danger.animal} standing in a {danger.roomMedium} in front of you just waiting for you to come closer.
        """,


        f"""
        This corridor leads to a {roomDesc} room.
        However, when you take a look Beneath your feet, you see some {danger.animal} standing in a {danger.roomMedium} in front of you,
        What do you think would be the best option?
        """,

        f"A {danger.roomMedium} of {danger.animal} is positioned in the center of the room.\nIt seems that you cannot make it to the next entrance, without crossing it.",
    ]

    if preText != None:
        gu.text(preText + "\n" + seededRandom.choice(str))
    else:
        gu.text(seededRandom.choice(str))




def randomRoom(autoFail=False, preText=None, postText=""):
    danger = Danger()

    aiText(preText, danger)

    choices = [
        seededRandom.choice(
            [
                "TRAVEL THROUGH it",
                "attempt to TRAVEL through them",
                "attempt to CROSS OVER it",
            ]
        ),
        seededRandom.choice(
            [
                "grab a rope and SWING OVER THEM",
                "reach for a vine and SWING OVER THEM",
            ]
        ),
        seededRandom.choice(
            ["CLIMB the wall", "SCALE the wall and attempt to avoid them"]
        ),
        seededRandom.choice(
            ["choose an ALTERNATIVE PATH", "go ANOTHER WAY", "TURN BACK", "RETREAT"]
        ),
        seededRandom.choice(
            ["GO BACK the way you came", "TURN BACK and go the way you came"]
        ),
        seededRandom.choice(["try to JUMP OVER THEM", "jump UP AND OVER the dangers"]),
    ]

    choices = seededRandom.sample(choices, seededRandom.randint(2, 3))
    correctChoice = seededRandom.randint(1, len(choices))

    if gu.debugMessages:
        print(
            f"Correct: {correctChoice}; Choices: {len(choices)}; AutoFail: {autoFail}"
        )

    choice = gu.askFromList(choices)
    fail = choice[1] != correctChoice or autoFail

    return danger.returnOutcome(postText, fail, choice[0])
