import random
print("Welcome to Guess the Number Game")
print("Chosse a number between 1 to 1,000,000")
correct_number = random.randint(1, 1000000)
attempts = 0
while True:
    guess_number = int(input("Enter a number: "))
    if guess_number < 0:
        print("you enter a negative number you are out.")
        exit()
    elif guess_number > correct_number:
        print("you are too High")
        attempts+=1
    elif guess_number < correct_number:
        print("You are too low")
        attempts+=1
    elif guess_number == correct_number:
        print("you are the winner😎😎")
        attempts+=1
        break
    else:
        print("You Enter and invalid number.")
        break



print(f"you guess the number in {attempts} attempts")

