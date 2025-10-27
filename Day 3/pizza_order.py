print("Welcome to Python Pizza Deliveries!")
size = input("What is the size you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("do you want extra cheese? Y or N: ")
bill = 0


if size == "S":
    bill = 15
    if pepperoni == "Y":
        bill += 2
elif size == "M":
    bill = 20
    if pepperoni == "Y":
        bill += 3
elif size == "L":
    bill = 25
    if pepperoni == "Y":
        bill += 3
else:
    print("You typed the wrong inputs.")
    
if extra_cheese == "Y":
    bill += 1

print(f"Your total bill is ${bill}")
# todo: work out how much they need to pay based on their size choice.

# todo: work out how much to add to their bill based on their pepperoni choice.

#todo: work out their final amount based on wether they want extra cheese