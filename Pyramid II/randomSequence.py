import time
import sys
import random
import re
import gameUtils as gu
import randomRoom as rr

r = random.Random()
# r.seed(0)

# Use seeded random for consistent randomness
seededRandom = gu.seededRandom

# Space-themed terms
hallwayNames = [
    "corridor",
    "airlock",
    "passageway",
    "tunnel",
    "hatchway",
    "deck",
    "hall",
    "chamber",
]

hallwayVerbs = [
    "navigate the",
    "proceed through the",
    "enter the",
    "float down the",
    "walk along the",
    "venture through the",
]


def askRandomHallway(initialVerbArr=hallwayVerbs, hallwayName="corridor"):
    hallwayName = hallwayName.upper()
    hallwayChoiceArray = []

    if seededRandom.randint(0, 3) == 1:
        for i in range(1, seededRandom.randint(3, 7)):
            hallwayChoiceArray.append(
                f"{r.choice(initialVerbArr)} {gu.numberToNth(i).upper()} {hallwayName}"
            )
    else:
        # Select 3 random alien symbols
        symbols = listSymbols()
        seededRandom.shuffle(symbols)

        firstVerb = initialVerbArr[0]
        symbol1 = symbols[0]
        symbol2 = symbols[1]
        symbol3 = symbols[2]

        hallwayChoiceArray = seededRandom.choice(
            [
                [
                    f"{r.choice(initialVerbArr)} EAST {hallwayName}",
                    f"{r.choice(initialVerbArr)} WEST {hallwayName}",
                    f"{r.choice(initialVerbArr)} NORTH {hallwayName}",
                    f"{firstVerb} SOUTH {hallwayName}",
                ],
                [
                    f"{firstVerb} LEFT {hallwayName}",
                    f"{r.choice(initialVerbArr)} FORWARD {hallwayName}",
                    f"{r.choice(initialVerbArr)} RIGHT {hallwayName}",
                ],
                [
                    f"{firstVerb} {hallwayName.lower()} marked with a {symbol1} insignia",
                    f"{r.choice(initialVerbArr)} {hallwayName.lower()} marked with a {symbol2} insignia",
                    f"{r.choice(initialVerbArr)} {hallwayName.lower()} marked with a {symbol3} insignia (etched into the metal plating)...",
                ],
                [
                    f"{firstVerb} LOWER {hallwayName}",
                    f"{firstVerb} UPPER {hallwayName}",
                    f"{r.choice(initialVerbArr)} {hallwayName.lower()} with a {symbol1} holographic marker glowing near it",
                ],
                [
                    f"{r.choice(initialVerbArr)} LEFT {hallwayName.lower()} illuminated by a {symbol1} glyph",
                    f"{firstVerb} CENTRAL {hallwayName}",
                    f"{r.choice(initialVerbArr)} RIGHT {hallwayName.lower()} with a {symbol2} glyph flickering on the floor panels",
                ],
                [
                    f"{firstVerb} PORT {hallwayName}",
                    f"{firstVerb} STARBOARD {hallwayName}",
                ],
                [
                    f"{firstVerb} FORWARD {hallwayName}",
                    f"{r.choice(initialVerbArr)} SIDE {hallwayName}",
                ],
                [f"{firstVerb} FRONT {hallwayName}", f"{firstVerb} LEFT {hallwayName}"],
            ]
        )
    gu.askFromList(hallwayChoiceArray)


def generate_traveling_text(hallwayName):
    travelingTextArr = [
        f"Hours drift by as you float weightlessly. Finally, after a long journey, you arrive at another cluster of {hallwayName}s.",
        f"The flickering lights guide you toward several new {hallwayName}s. Turning back isn’t an option — your oxygen is running low.",
        f"You push onward through the derelict ship until the path splits again. A new set of {hallwayName}s await your decision.",
        f"After some time, the bulkhead doors open, revealing more {hallwayName}s ahead.",
        f"The dim glow of emergency lights flickers across metallic walls as you step into yet another intersection of {hallwayName}s.",
        f"The hum of the reactor grows distant as you reach a new section of {hallwayName}s branching in every direction.",
        f"You glide through a narrow conduit and emerge into a vast chamber filled with doorways and {hallwayName}s.",
        f"A mechanical voice crackles: 'Multiple routes detected ahead.' You must choose your next {hallwayName}.",
        f"The cold air nips at your skin as you enter a junction where several {hallwayName}s extend into darkness.",
        f"Your footsteps echo as you approach yet another crossroads of {hallwayName}s.",
    ]

    actions = [
        "drift",
        "crawl",
        "float",
        "navigate",
        "traverse",
        "explore",
        "glide",
        "step",
    ]
    feelings = [
        "uneasy",
        "fatigued",
        "tense",
        "isolated",
        "disoriented",
        "restless",
        "wary",
    ]
    discoveries = [
        "discover",
        "encounter",
        "find",
        "detect",
        "uncover",
        "scan",
        "observe",
    ]
    decisions = [
        "weigh your next move carefully",
        "pause to study your surroundings",
        "check your scanner for safer routes",
        "decide which way to continue",
        "consult your navigation AI",
    ]

    for _ in range(25):
        action = seededRandom.choice(actions)
        feeling = seededRandom.choice(feelings)
        discovery = seededRandom.choice(discoveries)
        decision = seededRandom.choice(decisions)

        prompt = f"You {action} through the dimly lit {hallwayName}, feeling {feeling}. After some time, you {discovery} another junction of {hallwayName}s. You {decision}."
        travelingTextArr.append(prompt)

    return seededRandom.choice(travelingTextArr)


def listSymbols():
    # Space/alien symbols instead of animals
    symbols = [
        "STAR",
        "PLANET",
        "COMET",
        "MOON",
        "SATELLITE",
        "SPIRAL",
        "TRIDENT",
        "ASTEROID",
        "GALAXY",
        "CRESCENT",
        "EYE",
        "ORB",
        "CRYSTAL",
        "GEAR",
        "WING",
        "BLADE",
        "SPHERE",
        "TRIANGLE",
        "CUBE",
        "CIRCUIT",
        "PULSE",
        "BEACON",
    ]
    return symbols


def randomSequence(
    initialText=None,
    travelingTextArr=None,
    minSteps=1,
    maxSteps=5,
    roomOdds=0.4,
    initialVerbArr=hallwayVerbs,
    hallwayNameArr=hallwayNames,
    autoFail=False,
    lostTextArr=None,
):
    steps = seededRandom.randint(minSteps, maxSteps)
    hallwayName = seededRandom.choice(hallwayNameArr)

    if roomOdds > 0:
        roomOdds = int(1 // roomOdds)

    if lostTextArr == None:
        lostTextArr = [
            "Your oxygen alarm blares. You’ve wandered too far, and the ship’s corridors stretch endlessly. The lights flicker out, and the cold vacuum claims you.",
            "You’ve been adrift for hours. Every corridor looks the same. Your comms fall silent, and soon your power reserves drop to zero.",
            "The air grows thin as your flashlight dies. You’re lost in the bowels of the derelict vessel, surrounded by silence and metal.",
        ]

    if gu.debugMessages:
        print(
            f"(RANDOM SEQUENCE) autoFail: {autoFail}; steps: {steps}; roomOdds: 0-{roomOdds}"
        )

    i = 0
    while i < steps:
        i += 1
        if gu.debugMessages:
            print(f"STEP: {i}/{steps}")

        if roomOdds > 0 and i > 1 and seededRandom.randint(0, roomOdds) == 0:
            # Enter a room
            if gu.debugMessages:
                print("(ROOM)")

            if i == steps - 1 and autoFail:
                rr.randomRoom(preText=initialText, autoFail=True)
            else:
                rr.randomRoom(preText=initialText)
        else:
            if initialText is not None:
                gu.text(initialText)
            else:
                gu.text(generate_traveling_text(hallwayName))

            newHallway = seededRandom.choice(hallwayNameArr)
            askRandomHallway(hallwayName=newHallway)
            rand = seededRandom.randint(0, 5)
            if rand == 1:
                steps += 1
            elif rand == 2:
                steps -= 1
        initialText = None

    if autoFail:
        if roomOdds > 0 and seededRandom.randint(0, 2) == 1:
            rr.randomRoom(autoFail=True)
        else:
            gu.end(r.choice(lostTextArr))


def randomIfBlank(text, choices):
    if text == "" or text is None:
        return r.choice(choices)
    else:
        return text

#for testing
# randomSequence()