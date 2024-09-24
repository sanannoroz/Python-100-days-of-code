print("Fill in the Blank lyrics!")
print("Type in the blank lyrics and see if you are as cool as me.")
print()
attempts = 0
while True:
    song = input("I think i'm losing my ____ now: ")
    print(song)
    print()
    attempts+=1
    if song == "mind" or song == "Mind":
        print(f"well done! it only took you {attempts} attempts.")
        break
    else:
        print("Nope, try again.")
