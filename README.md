```
                                                                            
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
```
# The Great Pyramid-Of-Giza
A text based adventure game written in python

Run the wrapper.py file to play the game

## To Play
1. Install google genai using pip `pip install -q -U google-genai`
2. Get an API key and pass it in

## Design (Pyramid II)
In order to create the feeling of infinite pathways we make use of an LLM to generate new stories on the fly.

## Generation in-between choices
We start with the hardcoded story, possibly adding LLM generated text in-between choices.
In between a specific choice, we can use Gemini to generate a new story, only one outcome produces the pathway that leads to the next choice, All other outcomes end in a dead end.

## New objective
The original objective was to find all 4 entrances to the tomb of the pharoh, The new objective was to find the pharoh's tomb. The 4 entrances are now just artifacts that allow us to find the pharaoh's tomb.
The first artifact is a hyrogliphic map, containing the code to decypher the pharaoh's tomb.
The second artifact is half of the map leading to the pharaoh's tomb.
The third artifact is the pharo's crown, This is the other half of the map, that allows us to find the pharaoh's tomb.
The fourth artifact is the cornerstone, the piece that we can place into the door of the tomb to open the tomb.

When we have all artifacts, we travel down a long underground tunnel to find the "real" pyramid.