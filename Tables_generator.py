print("Welcome to Table Generator 🔢")
print()
print("Enter the number of table you want")

# asking user for what number of table he/she want?
table = int(input("Enter the Number: "))
# creating a for to print the complete the table.
for i in range(1, 11):
    answer = i*table
    print(table,"x", i ," = ",answer)

