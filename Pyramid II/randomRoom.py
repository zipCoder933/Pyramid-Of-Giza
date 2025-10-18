import time
import sys
import re
import gameUtils as gu

seededRandom = gu.seededRandom


class Danger:
    def __init__(self):
        if seededRandom.random() < 0.5:
            self.animal = seededRandom.choice([
                "malfunctioning laser grids",
                "unstable plasma vents",
                "electrified conduits",
                "exposed coolant leaks",
                "radiation zones",
                "rogue maintenance drones",
                "volatile fuel lines"
            ])
            self.desc = seededRandom.choice([
                "unstable", "hazardous", "sparking", "volatile", "dangerous"
            ])
            self.roomMedium = seededRandom.choice([
                "large", "dimly lit", "metallic", "pressurized", "cramped"
            ]) + " " + seededRandom.choice([
                "chamber", "corridor", "maintenance bay", "junction"
            ])
        else:
            self.animal = seededRandom.choice([
                "alien parasites",
                "rogue androids",
                "mutated lifeforms",
                "xenomorphs",
                "acid-spitting insects"
            ])
            self.desc = seededRandom.choice([
                "aggressive", "hostile", "lethal", "predatory",
                "terrifying", "mutated", "menacing"
            ])
            roomItem = [
                seededRandom.choice(["pressurized", "fog-filled", "hollow", "echoing"]) + " chamber",
                seededRandom.choice(["narrow", "dark", "glowing", "broken"]) + " passage",
                seededRandom.choice(["wide", "cavernous", "depressurized", "unstable"]) + " room",
                seededRandom.choice(["crumbling", "collapsed", "twisted", "warped"]) + " corridor"
            ]
            self.roomMedium = seededRandom.choice(roomItem)

    def returnOutcome(self, text2, fail, choice):
        if choice == "navigate through":
            if fail:
                gu.end("You attempt to navigate through the " + self.animal + ", but your suit alarms blare as systems fail. You perish in the chaos.")
            else:
                gu.text("You skillfully maneuver through the " + self.desc + " " + self.animal + ". " + text2)
                return
        elif "jet" in choice or "boost" in choice:
            if fail:
                gu.end("You ignite your thrusters, but lose control and collide with debris. Mission failed.")
            else:
                gu.text("You activate your jet boosters and soar past the " + self.animal + ". " + text2)
                return
        elif choice == "climb" or choice == "scale":
            if fail:
                gu.end("You attempt to climb the slick metallic wall, but gravity shifts and you plummet into the " + self.animal + ".")
            else:
                gu.text("You climb the wall panels, narrowly avoiding the " + self.animal + ". " + text2)
                return
        elif "jump" in choice:
            if fail:
                gu.end("You attempt to leap across the gap, but the gravity stabilizer fails mid-jump. You fall into the " + self.animal + ".")
            else:
                gu.text("You time your jump perfectly, soaring over the " + self.roomMedium + " filled with " + self.animal + ". " + text2)
                return
        elif choice == "reroute path":
            if fail:
                gu.end("You reroute through a maintenance duct, but it collapses under decompression. You’re lost to the void.")
            else:
                gu.text("You choose an alternate route, bypassing the " + self.desc + " " + self.animal + ". " + text2)
                return
        elif choice == "retreat":
            if fail:
                gu.end("You turn back, but the airlock behind you seals shut. The " + self.animal + " advance and consume the chamber.")
            else:
                gu.text("You retreat safely, escaping the " + self.animal + ". " + text2)
                return
        else:
            if fail:
                gu.end("You chose to " + choice + ", but the " + self.animal + " overwhelm you.")
            else:
                gu.text("You chose to " + choice + ". " + text2)
                return


def aiText(preText, danger):
    roomDesc = seededRandom.choice([
        "dimly lit", "sterile", "pressurized", "holographic", "wrecked",
        "fog-filled", "sparking", "massive", "dark", "echoing",
        "cramped", "flooded", "abandoned", "metallic"
    ])

    str = [
        f"""
        You drift down a long corridor, entering a {roomDesc} compartment...
        Ahead lies a {danger.roomMedium} filled with {danger.desc} {danger.animal}.
        The only way forward is through.
        """,

        f"""
        You step into a {roomDesc} bay. Warning lights flicker.
        A {danger.roomMedium} filled with {danger.animal} blocks your route.
        """,

        f"As you round a corner, you spot a {roomDesc} area. Your path is obstructed by a {danger.roomMedium} teeming with {danger.animal}.",
        
        f"""
        You cautiously enter a {roomDesc} room.
        Just beyond the entryway, a {danger.roomMedium} filled with {danger.desc} {danger.animal} hums with danger.
        """,

        f"A {danger.roomMedium} of {danger.animal} stretches across the chamber, their presence illuminated by flickering control panels."
    ]

    if preText:
        gu.text(preText + "\n" + seededRandom.choice(str))
    else:
        gu.text(seededRandom.choice(str))


def randomRoom(autoFail=False, preText=None, postText=""):
    danger = Danger()
    aiText(preText, danger)

    choices = [
        seededRandom.choice(["NAVIGATE THROUGH the hazard", "ATTEMPT TO CROSS the chamber"]),
        seededRandom.choice(["BOOST over using jetpack", "JET across the opening"]),
        seededRandom.choice(["CLIMB the structure", "SCALE the maintenance scaffolding"]),
        seededRandom.choice(["REROUTE PATH through nearby ducts", "TAKE AN ALTERNATIVE CORRIDOR"]),
        seededRandom.choice(["RETREAT back to safety", "TURN BACK to the last junction"]),
        seededRandom.choice(["JUMP across the gap", "LEAP over the dangers"])
    ]

    choices = seededRandom.sample(choices, seededRandom.randint(2, 3))
    correctChoice = seededRandom.randint(1, len(choices))

    if gu.debugMessages:
        print(f"Correct: {correctChoice}; Choices: {len(choices)}; AutoFail: {autoFail}")

    choice = gu.askFromList(choices)
    fail = choice[1] != correctChoice or autoFail

    return danger.returnOutcome(postText, fail, choice[0])
