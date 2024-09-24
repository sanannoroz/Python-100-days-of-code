animal_sound = ""
exited = ""
while True:
    animal_sound = input("What animal do you want?: ")
    if animal_sound == "Cow" :
        print("A Cow goes mood")
        print()
    elif animal_sound == "Cat" :
        print("A Cat goes miyo miyo")
        print()
    elif animal_sound == "Dog" :
        print("A Dog goes Woo Woo")
        print()
    else:
        print("Sorry! I don't know about this animal")
    exited =input("Do you want to exit?: ")
    print()
    if exited == "yes":
        break