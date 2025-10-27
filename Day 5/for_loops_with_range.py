#first number is inclusive
#last number is not inclusive
#can add another number at the end that specifies how large the step is in the range
for number in range(1,11,3):
    print(number)

#adds the values of 1 between 100 together
total = 0
for i in range (1,101):
    total += i
print(total)

#challenge on Udemy
for number in range(1,101):
    if number%3 == 0 and number%5 == 0:
        print("FizzBuzz")
    elif number%3 == 0:
        print("Fizz")
    elif number%5 == 0:
        print("Buzz")
    else:
        print(number)