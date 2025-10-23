import time
import os
import story as st 
dir_path = os.path.dirname(os.path.realpath(__file__))

while(True):
    st.startGame()
    while(True):
        val = input("\n\nDo you want to play again? (Y/n): ").lower().strip()
        if(val == 'y' or val == 'yes'):
            break
        elif(val == 'n' or val == 'no'):
            print("Goodbye.")
            time.sleep(3)
            exit()

