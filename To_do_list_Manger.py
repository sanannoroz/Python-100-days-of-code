import os, time
ToDo_List = []

def printList():
    print()
    for item in ToDo_List:
        print(item)
    print()

print("To Do List Manger")
while True:
    menu = input("Do you want to view, add, edit,remove or remove all your item from your to do list? ")
    if menu == "add" or menu == "Add":
        item = input("What do you want to Add to you List: ")
        ToDo_List.append(item)
    elif menu == "view" or menu == "View":
        time.sleep(1)
        printList()
    elif menu == "remove" or menu == "Remove":
        item  = input("What do you want to remove: ")
        check = input("Are you sure you want to remove this item? ")
        if check[0] == "y" or check == "Y":
            if item in ToDo_List:
                ToDo_List.remove(item)
    elif menu == "edit" or menu == "Edit":
        item = input("What do you want to Edit:\n").title()
        new = input("What do you want to change it to?")
        for i in range(0, len(ToDo_List)):
            if ToDo_List[i] == item:
               ToDo_List[i] = new

    elif menu == "remove all" or menu == "Remove All":
        ToDo_List = []
    else:
        print(f"{item} was not in your to do list")
    time.sleep(1)