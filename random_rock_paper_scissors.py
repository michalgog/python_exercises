import random
# global variable
option_list = {"scissors": 1, "paper": 2, "rock": 3}

# PLAYER 1 #
player1 = str(input("Enter your name: "))
choice_player1 = random.choice(list(option_list.keys()))
print(choice_player1)

# PLAYER 2 #

player2 = str(input("Enter your name: "))
choice_player2 = random.choice(list(option_list.keys()))
print(choice_player2)

# LOGIC #
def game():
    if choice_player1 > choice_player2:
        print(player1, "is a winner")
    elif choice_player2 < choice_player1:
        print(player2, "is a winner")
    else:
        print("nobody wins")
    return;

print = input("Again? y/n")
answer = ["y", "n"]

if answer == "y" or answer == "n":
    print("Ok")
    game()
else:
#print("Thx for game")
# game()