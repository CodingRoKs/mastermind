import string
import random
def levels(turns):
    displayed = ["A"]
    score = ""
    letters = list(string.ascii_uppercase)
    i = 0
    turns2 = turns
    while i <= len(letters):
        print("Turns left:", turns)
        print("Try to guess the order of these letters: ", letters[:i + 1])
        ask2 = input("Enter your guess here: ")
        while len(ask2) != len(displayed):
            print("That was not of the correct length.")
            turns -= 1
            print("Turns left:", turns)
            if turns == 0:
                return "game over"
            ask2 = input("Enter your guess here: ")
        for y in range(len(displayed)):
            if displayed[y].upper() == ask2[y].upper():
                score += "X"
            else:
                score += "O"
        print(ask2)
        print(score)
        if score == "X" * len(displayed):
            score = ""
            i += 1
            turns = turns2
            displayed.append(letters[i])
            random.shuffle(displayed)
            print("You got it right! level up!")
        else:
            turns -= 1
            score = ""
        if turns <= 0:
            return "game over"
    if len(displayed) == 26:
        print("You win!")

def mastermind():
    ask = input("Pick a level. Easy, medium, or hard?")
    if ask.lower() == "easy":
        print(levels(5))
    elif ask.lower() == "medium":
        print(levels(3))
    elif ask.lower() == "hard":
        print(levels(2))
    else:
        print("That is not valid. Please try again.")
        mastermind()
mastermind()
