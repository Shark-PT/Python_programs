#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator")
bill = int(input("What was the total bill? "))
tip = int(input("What percentage tip you would like to give? 10, 12 or 15? "))
persons = int(input("How many persons to split the bill? "))
final_tip = tip /100 + 1
payment = (bill / persons) * final_tip
round_payment = round(payment , 2)
print(f"Each person should pay: " , round_payment)