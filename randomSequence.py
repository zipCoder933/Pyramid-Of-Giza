import time
import sys
import random
import re
import gameUtils as gu
import randomRoom as rr

r = random.Random()
# r.seed(0)

#Use seeded random as much as possible
#Guarantees that the same seed will always result in the same random sequence
seededRandom = gu.seededRandom


hallwayNames = [
    "entrance",
    "hallway",
    "doorway",
    "passage",
    "path",
    "corridor",
    "staircase",
    "stairwell",
]
hallwayVerbs = [
    "take the",
    "travel down the",
    "pursue the",
    "follow the",
    "choose the",
    "pick the",
]


def askRandomHallway(initialVerbArr=hallwayVerbs, hallwayName="hallway"):
    hallwayName = hallwayName.upper()
    hallwayChoiceArray = []

    if seededRandom.randint(0, 3) == 1:
        for i in range(1, seededRandom.randint(3, 7)):
            hallwayChoiceArray.append(
                f"{r.choice(initialVerbArr)} {gu.numberToNth(i).upper()} {hallwayName}"
            )
    else:
        # select 3 out of all the animals
        animals = listAnimals()
        seededRandom.shuffle(animals)

        firstVerb = initialVerbArr[0]
        animal1 = animals[0]
        animal2 = animals[1]
        animal3 = animals[2]

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
                    f"{firstVerb} {hallwayName.lower()} with a {animal1} hyroglyphic",
                    f"{r.choice(initialVerbArr)} {hallwayName.lower()} with a {animal2} hyroglyphic",
                    f"{r.choice(initialVerbArr)} {hallwayName.lower()} with a {animal3} hyroglyphic (All engraved on the cornerstone)...",
                ],
                [
                    f"{firstVerb} EAST {hallwayName}",
                    f"{firstVerb} WEST {hallwayName}",
                    f"{firstVerb} SOUTH {hallwayName}",
                ],
                [
                    f"{firstVerb} BOTTOM {hallwayName}",
                    f"{firstVerb} TOP {hallwayName}",
                    f"{r.choice(initialVerbArr)} {hallwayName.lower()} with a {animal1} hyroglyphic engraved atop it (to the {r.choice(['left','right','side of it'])})",
                ],
                [
                    f"{r.choice(initialVerbArr)} left {hallwayName.lower()} with a {animal1} hyroglyphic engraved on the floor",
                    f"{firstVerb} FRONT {hallwayName}",
                    f"{r.choice(initialVerbArr)} right {hallwayName.lower()} with a {animal2} hyroglyphic also engraved on the floor",
                ],
                [
                    f"{r.choice(initialVerbArr)} LEFT {hallwayName}",
                    f"{r.choice(initialVerbArr)} RIGHT {hallwayName}",
                ],
                [f"{firstVerb} LEFT {hallwayName}", f"{firstVerb} RIGHT {hallwayName}"],
                [
                    f"{firstVerb} SOUTH {hallwayName}",
                    f"{r.choice(initialVerbArr)} WEST {hallwayName}",
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
        f"Hours pass, You start to feel sore. Finally, After a short venture, you have landed in another set of {hallwayName}s to choose...",
        f"A new set of {hallwayName} stand in front of you. At first you decide to turn back, however, you soon realize that you have no choice.\nYou are now almost lost.\nYou must choose which other {hallwayName} to take...",
        "You jog along, trying to find your way, however it doesnt take long before you have more desicions to make. After a short venture, you have landed in another set of paths to choose from...",
        "After a short venture, you have landed in another set of paths to choose from...",
        f"You venture down the path and have finally reached the end of it. You now must choose what other {hallwayName}s to take...",
        f"It looks like you have finally reached the end of that one pretty quick. You now must choose what paths to take...",
        f"You soon discover that this path ends and branches off into multiple {hallwayName}s...",
        f"This path ends and branches off into multiple {hallwayName}s. What do you do?",
        f"After traveling down the path for a considerable time, you have made it to another set of {hallwayName}s.\nYou now have a desicion to make: ",
        f"After hours of traveling, you have finally landed in another set of paths to choose from...",
        f"You have finally reached the end of that one pretty quick. No matter how many {hallwayName}s you take, It seems as if you will never be able to find your way to the end of them. You now must choose what other {hallwayName}s to take...",
        f"You have been traveling for so long that you appear to be lost.\nIn an attempt to find your way back, you have found a completely new path.\nHopefully one of these paths will lead you back the way you came...",
        f"Too many {hallwayName}s! You exclaim in frustration, You feel as though this must be the last one...",
        f"A path has ended and branches off into multiple {hallwayName}s. What do you do?",
        f"If you were to choose, what other {hallwayName}s would you choose?",
        f"Another one, this one ends and branches off into multiple {hallwayName}s. What do you do?",
        f"There sure are a lot of {hallwayName}s here. What do you do?",
        f"Running at your top speed, you have finally reached the end of the path. You now must choose what other {hallwayName}s to take...",
        f"Walking at a snake like pace, you have finally reached the end of that one pretty quick. You now must choose what other {hallwayName}s to take...",
        f"Skillfully, you have finally reached the end of that one. You now must choose what other {hallwayName}s to take...",
        f"Another path. What do you do?",
        f"A set of {hallwayName}s surrounding you. What do you do?",
        f"A path ends and branches off into multiple {hallwayName}s... Desicions, Decisions, Decisions. What do you do?",
        f"The path twists and turns before opening up to yet another series of {hallwayName}s to consider.",
        f"You've been walking for what seems like an eternity when yet another set of {hallwayName}s appear before you.",
        f"As you proceed, the corridor splits into several {hallwayName}s, each beckoning you to explore.",
        f"A labyrinth of {hallwayName}s unfolds before you, which path will you choose?",
        f"Your journey has brought you to a complex network of {hallwayName}s. The choice is yours.",
        f"The {hallwayName} ahead splits into many paths, each shrouded in mystery.",
        f"You reach a crossroads where multiple {hallwayName}s diverge. Time to decide.",
        f"A myriad of {hallwayName}s lie ahead. Which direction holds the key to your quest?",
        f"You find yourself at an intersection of {hallwayName}s, indecision grips you for a moment.",
        f"The {hallwayName}s ahead are numerous and daunting. You steel yourself for the decision.",
        f"Another fork in the path presents a new selection of {hallwayName}s. Where to next?",
        f"The relentless journey has led you to a fresh set of {hallwayName}s. The adventure continues.",
        f"Each {hallwayName} seems to whisper promises of adventure. Which will you heed?",
        f"The {hallwayName}s ahead are as enigmatic as they are numerous. Choose your next step wisely.",
        f"Fatigue begins to set in, but the sight of new {hallwayName}s revitalizes your spirit.",
        f"A brief respite, and then the journey leads you to more {hallwayName}s. The saga goes on.",
        f"The {hallwayName}s before you are as perplexing as they are numerous. What lies ahead?",
        f"With a deep breath, you confront the next set of {hallwayName}s. Your journey is far from over.",
        f"The passage has ended, and now a collection of {hallwayName}s fan out before you.",
        f"The corridor yields to a series of {hallwayName}s, each a potential path to your destiny.",
        f"Endless choices lie ahead as a new set of {hallwayName}s emerges from the shadows.",
        f"You pause momentarily before the sprawling network of {hallwayName}s that awaits.",
        f"You've navigated countless {hallwayName}s, yet here stand more, challenging your resolve.",
        f"The {hallwayName}s multiply before your eyes. Which way will lead you to victory?",
        f"After much travel, the {hallwayName}s still stretch on. The quest is relentless.",
        f"The {hallwayName}s converge and diverge like a living maze. Your path is unclear.",
        f"It's a sea of {hallwayName}s, and you must navigate these waters with care.",
        f"Your path has been a winding one, and now more {hallwayName}s lie ahead.",
        f"The {hallwayName}s branch off into the unknown, each a silent invitation to explore.",
        f"The journey never seems to end, with each {hallwayName} leading to more choices.",
        f"You've traversed many a {hallwayName}, and still they unfold before you.",
        f"The {hallwayName}s are relentless, each turn bringing new decisions.",
        f"A new junction of {hallwayName}s appears, as if to test your determination.",
        f"You face the {hallwayName}s, each a potential path to an unseen fate.",
        f"The {hallwayName}s before you are a testament to the journey's complexity.",
        f"Another set of {hallwayName}s, another moment of choice. The journey continues.",
        f"The {hallwayName}s stretch on, an endless network of choices and chances.",
        f"You stand before a tapestry of {hallwayName}s, each thread a different path.",
        f"The {hallwayName}s offer no respite, only more questions. Which way will you go?",
        f"With each step, the {hallwayName}s multiply, a testament to the journey's challenge.",
        f"The {hallwayName}s are a puzzle, and you must piece together the route ahead.",
        f"The {hallwayName}s loom large, a network of paths sprawling into the distance.",
        f"You're met with a new set of {hallwayName}s, each promising its own adventure.",
        f"The {hallwayName}s are a web, intricate and confusing. Which strand will you follow?",
        f"The {hallwayName}s fork and weave, a labyrinthine dance of choices.",
    ]

    actions = [
        "wander",
        "amble",
        "stroll",
        "tread",
        "march",
        "journey",
        "trek",
        "saunter",
        "trudge",
    ]
    feelings = ["exhausted", "weary", "fatigued", "tired", "worn out"]
    discoveries = ["come across", "stumble upon", "find", "encounter", "reach"]
    decisions = [
        "ponder your next move",
        "hesitate",
        "contemplate your options",
        "consider your path",
        "think carefully about where to go next",
    ]

    for _ in range(25):
        action = seededRandom.choice(actions)
        feeling = seededRandom.choice(feelings)
        discovery = seededRandom.choice(discoveries)
        decision = seededRandom.choice(decisions)

        prompt = f"You {action} along and feel {feeling}. After a while, you {discovery} a new set of {hallwayName}s. You {decision}."
        travelingTextArr.append(prompt)

    return seededRandom.choice(travelingTextArr)


def listAnimals():
    snakeAnimal = r.choice(["SERPENT", "SNAKE"])
    animals = [
        "BIRD",
        snakeAnimal,
        "CRANE",
        "SPHINX",
        "WOLF",
        "ELEPHANT",
        "LION",
        "TIGER",
        "SHARK",
        "DOLPHIN",
        "OCTOPUS",
        "SNAIL",
        "CRAB",
        "GORILLA",
        "STAFF",
        "CAT",
        "BEAR",
        "DOUBLE STAFF",
        "MEDALLION",
        "ROD",
        "SWORD",
        "BOW",
        "ARROW",
    ]
    return animals


def randomSequence(
    initialText=None,
    travelingTextArr=None,
    minSteps=1,
    maxSteps=3,
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
            "You have been lost for hours and have no idea where you are.\nYou suddenly find yourself in pitch blackness as your flashlight runs out of batteries.",
            "It has been hours, You are likely stuck somewhere within the center of the pyramid, But you just cant seem to find your way back.\nFinally, you run out of light, trapping you in pitch darkness.",
            "You end up finding a room you havent seen before.\nHowever, before you are able to enter it, your flashlight runs out of batteries. You feel for where the entrance was, but you can't find it anywhere.",
        ]

    if gu.debugMessages:
        print(
            f"(RANDOM SEQUENCE) autoFail: "
            + str(autoFail)
            + "; steps: "
            + str(steps)
            + "; roomOdds: 0-"
            + str(roomOdds)
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

            if i == steps - 1 and autoFail:  # if this is the last step, then fail
                if gu.debugMessages:
                    print("(this is the room (auto fail))")
                rr.randomRoom(preText=initialText, autoFail=True)
            elif i == 0:
                rr.randomRoom(preText=initialText)
            else:
                rr.randomRoom(preText=initialText)
        else:
            if(initialText != None):
                gu.text(initialText)
            else:
                gu.text(generate_traveling_text(hallwayName))
                
            newHallway = seededRandom.choice(hallwayNameArr)
            askRandomHallway(hallwayName=newHallway)
            # Change the number of steps based on the path we took
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
    if text == "" or text == None:
        return r.choice(choices)
    else:
        return text