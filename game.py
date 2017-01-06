import random


user_choice = ["scissors", "papper", "rock"]

# player1
player1 = input("Enter your name here: ")
player1_choice = random.choice(list(user_choice))

player2 = input("Enter ypour name here: ")
player2_choice = random.choice(list(user_choice))


print("Player1 name is: ", player1)
print(player1, "choose", player1_choice, "\n")

print("Player2 name is:", player2)
print(player2, "choose", player2_choice, "\n")

# logic
def game():

    if player1_choice == player2_choice:
        print("Nobody wins")
        print("Do we play again?")
        # call function again?
        game()
    elif player1_choice == "scissors":
        if player2_choice == "papper":
            print(player1, "wins")
        else:
            print(player2, "wins")
    elif player1_choice == "papper":
        if player2_choice == "rock":
            print(player2, "wins")
        else:
            print(player1, "wins")
    elif player1_choice == "rock":
        if player2_choice == "scissors":
            print(player1, "wins")
        else:
            print(player2, "wins")
    elif player1_choice == "papper":
        if player2_choice == "rock":
            print(player1, "wins")
        else:
            print(player2, "wins")
    else:
        print("Do you want to play again?")

print(input("Do we play again? Y / N"))

'''

scissors > papper
papper < rock
rock > scissors
papper > rock

'''