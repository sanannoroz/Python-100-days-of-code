def colorChange(color):
  if color=="red":
    return ("\033[31m")
  elif color=="white":
    return ("\033[0m")
  elif color=="blue":
    return ("\033[34m")
  elif color=="yellow":
    return ("\033[33m")
  elif color == "green":
    return ("\033[32m")
  elif color == "purple":
    return ("\033[35m")

print("interface 1")
print()


title = f"{colorChange('red')}={colorChange('white')}={colorChange('blue')}= {colorChange('yellow')} Music App {colorChange('blue')}={colorChange('white')}={colorChange('red')}="
print(f"{title:>70}")

text = f"🔥▶️   {colorChange('white')}Radio Gaga"
print(f"{text:>30}")
text = f"{colorChange('yellow')} Queen"
print(f"{text:>20}")
text = f"{colorChange('white')}PREV"
print(f"\n{text}")
text = f"{colorChange('green')} NEXT"
print(f"{text:>15}")
text = f"{colorChange('purple')} PAUSE"
print(f"{text:>22}")

print()
print(f"{colorChange('white')}Interface 2")
print()
greeting = f"{colorChange('white')} WELCOME TO"
print(f"{greeting:>30}")
title = f"{colorChange('blue')} --   ARMBOOK   --"
print(f"{title:>34}")
print()
paragraph = f"{colorChange('yellow')} Definitely not a rip off of"
print(f"{paragraph:>45}")
paragraph = "a certain other social"
print(f"{paragraph:>40}")
paragraph = "networking site."
print(f"{paragraph:>40}")
print()
text = f" {colorChange('red')} Honest."
print(f"{text:>30}")
print()
text = f" {colorChange('white')} Username:"
print(f"{text:>30}")
text = f" {colorChange('white')} Password:"
print(f"{text:>30}")