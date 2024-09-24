from getpass import getpass as input

print("Welcome to Rock, Paper, Scissors Game 🪨📄✂️ ")
print("Type the R P S to play the game")

# creating the variable to Keep the Score of Player 1 and Player 2
score_p1 = 0
score_p2 = 0

# using a loop to repeat the game multiple rounds
while True:
    player_1 = input("player 1 your turn: ")
    print()
    player_2 = input("player 2 your turn: ")
    print()

# create the if statement for Players
    if player_1 == "R":
        if player_2 == "S":
            print("Player one is won")
            score_p1+=1
            print("player one you won ",score_p1,"rounds")
            print()

        elif player_2 == "P":
            print("Player two won")
            score_p2+=1
            print("player two you won ",score_p2,"rounds")
            print()
        elif player_2 == "R":
            print("The game is tie")   
        else:
            print("Player Two invilde move")
        
        if score_p1 == 3:
            break
        if score_p2 == 3:
            break
#Breaking the loop if one of two player won the rounds 
    
    elif player_1 == "P":
        if player_2 == "S":
            print("Player two is won")
            score_p2+=1
            print("player two you won ",score_p2,"rounds")
            print()
        elif player_2 == "R":
            print("Player one won")
            score_p1+=1
            print("player one you won ",score_p1,"rounds")
            print()
        elif player_2 == "P":
            print("The game is tie")
        else:
            print("Player Two invilde move")
        if score_p1 == 3:
            break
        if score_p2 == 3:
            break
#Breaking the loop if one of two player won the rounds 
        
    elif player_1 == "S":
        if player_2 == "R":
            print("Player two won")
            score_p1+=1
            print("player two you won ",score_p2,"rounds")
            print()
        elif player_2 == "P":
            print("Player one won")
            score_p1+=1
            print("player one you won ",score_p1,"rounds")
            print()
        elif player_2 == "S":
            print("The game is tie")          
        else:
            print("Player Two invilde move")
        if score_p1 == 3:
            break
        if score_p2 == 3:
            break
#Breaking the loop if one of two player won the three rounds 

        continue
#Continue the loop to restart the game            
    else:
        print("Player one invilde move")

# Printing the final score of Player
print("The total sorce of Player one is", score_p1)
print("The total sorce of Player two is", score_p2)
