import os, time
listOfEmail = []

def prettyPrint():
  os.system("clear")
  print("listofEmail")
  print()
  for index in range(len(listOfEmail)): # len counts how many items in a list
    print(f"{index}: {listOfEmail[index]}")
  time.sleep(1)

def spamming(max):                                                
  print()
  for i in range(0,max):
    print(f"""Email {i+1}
          Dear {listOfEmail[i]} 
           It has come to our attention taht you're missing out on the amazing Replite 100 days of code. We insis you do it right away. If you don't we will pass on your email address to every spammer we've ever encountered and also sign you up to the My Little Pony newsletter, because that's neat. We might just do that anyway.

           Love and hugs, 

           Ian Spammington III""")
    time.sleep(1)
    os.system("clear")
    
  


while True:
  print("SPAMMER Inc.")
  menu = input("1. Add email\n2: Remove email\n3. Show emails\n4. Get SPAMMING\n> ")
  if menu == "1":
    email = input("Email > ")
    listOfEmail.append(email)
  elif menu =="2":
    email = input ("Email > ")
    if email in listOfEmail:
      listOfEmail.remove(email)
  elif menu == "3":
    prettyPrint()
    time.sleep(1)
    os.system("clear")
  elif menu == "4":
    spamming(10)
    os.system("clear")
    time.sleep(1)