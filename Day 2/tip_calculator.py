print(f"Welcome to the tip calculator!")
#prompts the total bill, stored as float
bill_price = float(input(f"What was the total bill? $"))
#prompts the tip amount, stored as int
tip_input = int(input(f"How much tip would you like to give? 10, 12, or 15? "))
#prompts for the amount of people to pay, stored as int
people_split_bill = int(input(f"How many people are there to split the bill?"))
#calculates the tip amount and rounds it to the nearest 100th
tip_amount = round(bill_price * (tip_input / 100), 2)
#calculates the total price, rounds to nearest 100th
total = round((bill_price + tip_amount) / people_split_bill, 2)
print(f"Each person should pay: ${total}")