import random, time , os

def rollDice(side):
    result = random.randint(1, side)
    return result

def health():
    healthStat = ((rollDice(6)*rollDice(12))/2) + 10
    return healthStat

def strength():
    strengthStat = ((rollDice(6)*rollDice(8))/2) +12
    return strengthStat


print("⚔️  BATTLE TIME ⚔️")
print()
c1Name = input("Name Your Legend:\n")
c1Type = input("Character Type (Human, Elf, Wiard, orc): ")
print()
print(c1Name)
c1Health = health()
c1Strength = strength()
print("HEALTH:", c1Health)
print("STRENGTH:", c1Strength)
print()
print("Who are they battling?")
print()
c2Name = input("Name Your Legend:\n")
c2Type = input("Character Type (Human, Elf, Wiard, orc): ")
print()
print(c2Name)
c2Health = health()
c2Strength = strength()
print("HEALTH:", c2Health)
print("STRENGTH:", c2Strength)
print()

round = 1
winner = None

while True:
        time.sleep(1)
        os.system("clear")
        print("⚔️  BATTLE TIME ⚔️")
        print()
        print("The battle begins")

        c1Dice = rollDice(6)
        c2Dice = rollDice(6)
        difference = abs(c1Health - c2Health) + 1

        if c1Dice > c2Dice:
            c2Health -= difference
            if round == 1:
                print(c1Name, "wins the first blow")
            else:
              print(c1Name, "wins the round")
        elif c2Dice > c1Dice:
            c1Health -= difference
            if round == 1:
                print(c2Name, "wins the first blow")
            else:
                print(c2Name,"wins the round",round)
        else:
            print("Their sword clash and they draw round", round)

            print(c1Name)
            print("HEALTH:", c1Health)
            print("STRENGTH:", c1Strength)
            print()
            print(c2Name)
            print("HEALTH:", c2Health)
            print("STRENGTH:", c2Strength)


        if c1Health <= 0 :
            print(c1Name, "has died!")
            winner = c2Name
            break
        elif c2Health <= 0:
            print(c2Name, "has died")
            winner = c1Name
            break
        else:
            print("They both standing for next round ")
            round += 1


time.sleep(1)
os.system("clear")
print("⚔️  BATTLE TIME ⚔️")
print()
print(winner, "wins with round",round)

