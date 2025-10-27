print(f"Weclome to the rollercoaster!")
height = int(input(f"What is your height in cm? "))
bill = 0

if height >= 120:
    print(f"You can ride the rollercoaster")
    age = int(input(f"What is your age? "))
    if age <= 12:
        print(f"Child tickets are $5.")
        bill = 5
    elif age <= 18:
        print(f"Youth tickets are $7.")
        bill = 7
    #same thing as age >= 45 and age <= 55
    elif 45 <= age <= 55:
        print("Everything is ok. Have a free ride on us.")
    else:
        print(f"Adult tickets are $12.")
        bill = 12
    
    wants_photo = input("Do you want a photo taken? Press Y for yes and N for no.")
    if wants_photo == "Y":
        #add $3 to bill
        bill += 3
    print(f"Your final bill is {bill}")
else:
    print(f"Sorry you have to grow a little taller before you can ride.")