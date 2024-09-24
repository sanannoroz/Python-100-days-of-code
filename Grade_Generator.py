# This script calculates the percentage score and assigns a grade for a given test
print("Welcome to Grade Generator")
# Prompt the user to input the name of the test
name_of_test = input("What is the name of test: ")

# Prompt the user to input the maximum possible score
max_score = int(input("What is the maximum score: "))

# Prompt the user to input the score they received
received_score = int(input("What is the score you got: "))

# Calculate the percentage score by dividing the received score by the maximum score and multiplying by 100
total_percentage = float(received_score/max_score)*100

# Round the percentage score to two decimal places
total_percentage = round(total_percentage, 2)

# Assign a grade based on the percentage score using a series of if and elif statements
if total_percentage >= 90 and total_percentage <= 100:
    print(f"You Got the Grade A+ and Percentage {total_percentage}%")
elif total_percentage >=80 and total_percentage <=89:
    print(f"You Got the Grade A and Percentage {total_percentage}%")
elif total_percentage >=70 and total_percentage <=79:
    print(f"You Got the Grade B and Percentage {total_percentage}%")
elif total_percentage >=60 and total_percentage <=69:
    print(f"You Got the Grade C and Percentage {total_percentage}%")
elif total_percentage >=50 and total_percentage <=59:
    print(f"You Got the Grade D and Percentage {total_percentage}%")
elif total_percentage <=49:
    print(f"You Got the Grade U and Percentage {total_percentage}%")
else:
    print("Try Again")