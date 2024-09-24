import os, time
ToDo_List = []

def printList():
    print()
    for item in ToDo_List:
        print(item)
    print()

print("To Do List Manger")
while True:
    menu = input("Do you want to view, add, or edit your to do list? ")
    if menu == "add" or menu == "Add":
        item = input("What do you want to Add to List: ")
        ToDo_List.append(item)
        printList()
    elif menu == "view" or menu == "View":
        time.sleep(0.5)
        printList() 
    elif menu == "edit" or menu == "Edit":
        item = input("What do you want to edit remove or replace: ")
        if item == "remove" or item == "Remove":
            item = input("What do you want to remove: ")
            ToDo_List.remove(item)
        elif item == "Replace" or "replace":
            item = input("What do you want to replace: ")
            ToDo_List[item] = item
        else:
            print(f"{item} was not in the list")
    time.sleep(1)
    os.system("clear")




