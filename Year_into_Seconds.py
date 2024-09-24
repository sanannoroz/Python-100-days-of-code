# asking for userinput how many days are in this year
years_into_seconds = int(input("how many days are in this year: "))


# define the values
day_in_year = 365
day_in_learyear = 366
hour_in_day = 24
mintues_in_hours = 60
seconds_in_mintues = 60

#mutliple the values to get the answer
seconds_in_year = day_in_year*hour_in_day*mintues_in_hours*seconds_in_mintues
seconds_in_leapyear = day_in_learyear*hour_in_day*mintues_in_hours*seconds_in_mintues

#define conditons for year and leapyear
if years_into_seconds == 366:
    print(seconds_in_leapyear)
else:
    print(seconds_in_year)
