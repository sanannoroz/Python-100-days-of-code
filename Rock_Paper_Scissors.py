from getpass import getpass as input

print("Welcome to Rock, Paper, Scissors Game 🪨📄✂️ ")
print("Type the R P S to play the game")

player_1 = input("player 1 your turn: ")
print()
player_2 = input("player 2 your turn: ")
print()

if player_1 == "R":
    if player_2 == "S":
        print("Player one is won")
    elif player_2 == "P":
        print("Player two won")
    elif player_2 == "R":
        print("The game is tie")
    else:
        print("Player Two invilde move")
elif player_1 == "P":
    if player_2 == "S":
        print("Player two is won")
    elif player_2 == "R":
        print("Player one won")
    elif player_2 == "P":
        print("The game is tie")
    else:
        print("Player Two invilde move")
elif player_1 == "S":
    if player_2 == "R":
        print("Player two won")
    elif player_2 == "P":
        print("Player one won")
    elif player_2 == "S":
        print("The game is tie")
    else:
        print("Player Two invilde move")
else:
    print("Player one invilde move")