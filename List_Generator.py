# This program generates a list of numbers based on 
print("List Generator 📃📃")
print()
print("You are going to give me a number you want to start with, an ending number, and by how many you want me to add each time.")

# the user's input. The user can choose how many numbers they want, 
starting_value = int(input("what number do you want to start with: "))
ending_value = int(input("what number do you want to end with: "))
Increment_value = int(input("what number do you want to increment with: "))

for i in range(starting_value, ending_value, Increment_value):
    print(i)
