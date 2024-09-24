total_bill = float(input("What was the total bill: "))
tip = int(input("The amount you want to leave as tip: "))
tip_bill = tip/100*total_bill
bill_withtip = tip_bill+total_bill
numberOfPeople = int(input("how many people are you: "))
anwser = bill_withtip/numberOfPeople
anwser = round(anwser, 2)
print(anwser)