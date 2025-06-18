#Write a game function ,where the score is returned as an int and its stored in a file

import random

def game(): 
    print("You are playing the game..")
    score = random.randint(1, 62)
    # Fetch the hiscore
    with open("Chapter9/01/PS/highscores.txt") as f:
        hiscore = f.read()
        if(hiscore!=""):
            hiscore = int(hiscore)
        else:
            hiscore = 0

    print(f"Your score: {score}")
    if(score>hiscore):
        # write this hiscore to the file
        with open("Chapter9/01/PS/highscores.txt", "w") as f:
            f.write(str(score))

    return score

game()