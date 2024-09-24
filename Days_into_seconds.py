print("Welcome")
print("Convert Days into Seconds")
days = int(input("How many days do you want to convert: "))

hour_in_day = 24
minutes_in_hour = 60
seconds_in_minutes = 60
answer = hour_in_day*minutes_in_hour*seconds_in_minutes

if days == 1:
    print(answer)
elif days == 2:
    answer = hour_in_day*minutes_in_hour*seconds_in_minutes*2
    print(answer)
elif days == 3:
    answer = hour_in_day*minutes_in_hour*seconds_in_minutes*3
    print(answer)
elif days == 4:
    answer = hour_in_day*minutes_in_hour*seconds_in_minutes*4
    print(answer)
elif days == 5:
    answer = hour_in_day*minutes_in_hour*seconds_in_minutes*5
    print(answer)
elif days == 6:
    answer = hour_in_day*minutes_in_hour*seconds_in_minutes*6
    print(answer)
elif days == 7:
    answer = hour_in_day*minutes_in_hour*seconds_in_minutes*7
    print(answer)
elif days == 8:
    answer = hour_in_day*minutes_in_hour*seconds_in_minutes*8
    print(answer)
elif days == 9:
    answer = hour_in_day*minutes_in_hour*seconds_in_minutes*9 
    print(answer)
elif days == 10:
    answer = hour_in_day*minutes_in_hour*seconds_in_minutes*10
    print(answer)
else:
    print("You Type Incorrect")
