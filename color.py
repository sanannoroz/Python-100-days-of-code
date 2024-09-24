def newPrint(color, word):
    if color == 'red':
        print("\033[31m", word, sep= "", end=" ")
    elif color == 'green':
        print("\033[36m", word, sep= "", end=" ")
    elif color == 'blue':
        print("\033[34m", word, sep= "", end=" ")
    else:
        print("\033[0m", word, sep= "", end=" ")
        
print("Super Subroutine")
print("With my", end=" ")
newPrint("red", "new program")
newPrint("reset", 'I can just call red("red")')
newPrint("red", "and")
newPrint('green', 'that word will appear in the color I set it to.')
print("With no", end = " ")
newPrint('blue', 'weired gaps')
newPrint('white', 'Epic')




