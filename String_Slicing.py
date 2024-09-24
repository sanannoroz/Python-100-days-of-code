print("🌟Star Wars Name Generator🌟")
print()
first_name, last_name, mother_name, city_name  = input("Input your first name > "), input("Input your last name > "), input("Input your mother's maiden name > "), input("Input your city name > ")
print()
print(f"{first_name[:3].title()}{last_name[:3].lower()} {mother_name[:2]}{city_name[-3:]}")
 




