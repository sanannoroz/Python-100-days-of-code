DOB = int(input("What is your date of Birth: "))
if DOB >= 1925 and DOB <=1946:
    print("Your are A Traditionalists.")
elif DOB >= 1947 and DOB <= 1964:
    print("You are Baby Boomers")
elif DOB >= 1965 and DOB <= 1981:
    print("You are Generation X")
elif DOB >= 1982 and DOB <= 1995:
    print("You are MIllenials")
elif DOB >= 1996 and DOB <= 2015:
    print("You are Generation Z")
else:
    print("Try Again.")
