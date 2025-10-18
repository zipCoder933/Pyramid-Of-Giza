import json
import os
import gameUtils as gu
import randomSequence as rs

def load_json(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)
    
def load_file(filepath):
    with open(filepath, 'r') as file:
        return file.read()

def processRandomSequence(randomSequence):
    initialText = None
    minSteps=1
    maxSteps=3
    roomOdds=0.3
    hallwayNameArr = rs.hallwayNames

    if("initialText" in randomSequence):
        initialText = randomSequence["initialText"]
    if("minSteps" in randomSequence):
        minSteps = randomSequence["minSteps"]
    if("maxSteps" in randomSequence):
        maxSteps = randomSequence["maxSteps"]
    if("roomOdds" in randomSequence):
        roomOdds = randomSequence["roomOdds"]
    if("hallwayNames" in randomSequence):
        hallwayNameArr = randomSequence["hallwayNames"]
        
    rs.randomSequence(initialText=initialText, 
                        minSteps=minSteps, 
                        maxSteps=maxSteps, 
                        roomOdds=roomOdds,
                        hallwayNameArr=hallwayNameArr)



def play_node(base_dir):
    node = load_json(base_dir+"/story.json")
    while True:
        keys = list(node.keys())
        if("randomSequence" in node): #Random Sequence comes first
            if(gu.debugMessages):
                print("Found random sequence!")
            processRandomSequence(node["randomSequence"])

        story = node["story"]

        if("choices" in node):#Story
            gu.text(story)#tell the story after the random sequence!
            options = list(node["choices"].keys())
            choice,choice_num = gu.askFromList(options)
            selected = options[choice_num-1]
            print(f"You choose: {selected}")
            next_node = node["choices"][selected]

            # Check if it references another file
            if "path" in next_node:
                path = os.path.join(base_dir, next_node["path"])
                print(f"Loading {path}")
                if not os.path.exists(path):
                    print(f"Error: File not found - {path}")
                    break
                node = load_json(path)
            else:
                node = next_node
        else:
            gu.end(story)
            return

while True:
    base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "story")
    banner = load_file(base_dir+"/banner.txt")
    gu.revealLines(banner)
    play_node(base_dir)

    out = input("Play again? (Y/n) ").strip().lower()
    if(out == "n" or out == "no" or out == "exit"):
        break
    else:
        print("\n\n")