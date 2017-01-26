"""
Make a two-player Rock-Paper-Scissors game.
"""

from random import randint

choice = ["rock", "paper", "scissors"]

# user
player = False

# computer
computer = choice[randint(0, 2)]

# while not player == while player == False
while not player:
    player = input("What is you choice: rock, paper, scissors? \n")
    if player == computer:
        print("Tie! Nobody win.")
    # first
    elif player == "rock":
        if computer == "paper":
            print("You loose, ", computer, "covers", player)
        else:
            print("You win", player, "smashes", computer)
    # second
    elif player == "paper":
        if computer == "scissors":
            print("You loose, ", computer, "cuts", plyer)
        else:
            print("You win", player, "covers", computer)
    # third
    elif player == "scissors":
        if computer == "rock":
            print("You loose,", computer, "smashes", player)
        else:
            print("You win, ", player, "cut", computer)
    else:
        print("That's not a valid play. Check you spelling.")
    player = False
    computer = choice[randint(0, 2)]
