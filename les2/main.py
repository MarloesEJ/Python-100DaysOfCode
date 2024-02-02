print("Welcom to the tip calculator.")
total_amount = float(input("What was the total bill? $"))
percentage_tip = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
amount_of_people = float(input("how many people to split the bill? "))

tip_percentage = 1+percentage_tip/100
amount_pp = round(total_amount/amount_of_people*tip_percentage, 2)

print(f"Each person should pay: ${amount_pp}")


