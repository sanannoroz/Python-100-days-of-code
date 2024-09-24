first_name = []
last_name = []
full_name = []


def printList():
    print()
    for i in first_name, last_name:
        print(i)
    print()

while True:
    addItem = input("What is your first name > ").strip().capitalize()
    if addItem not in first_name:
        first_name.append(addItem)
    addItem1 = input("What is your last name  > ").strip().capitalize()
    if addItem1 not in last_name:
        last_name.append(addItem1)
    printList()
  

    
    

    
