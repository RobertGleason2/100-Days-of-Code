print("Welcome to Treasure Island.")
print("Your mission is to find treasure.")
first_choice = input("There are two paths ahead of you. Whcih way do you go? \n\t Type \"left\" or \"right\" ")

if first_choice == "left" or first_choice == "Left":
    print("You chose the left path.")
    print("You now come accross a lake.")
    print("In the distance you see a boat coming your way.")
    second_choice = input("You could wait for the boat or swim accross. Which do you choose?\n\t Type \"wait\" or \"swim\" ")
    if second_choice == "wait" or second_choice == "Wait":
        print("you chose to wait for the boat. This was the right option since the lake's filled with deadly piranas!")
        print("You get out of the boat and make your way through the jungle to find 3 doors. Red, Blue, and Yellow.")
        third_choice = input("Which door do you choose? \n\t Type \"red\", \"blue\" or \"yellow\" ")

        if third_choice == "red" or third_choice == "Red":
            print("you find yourself engulfed in flames! GAME OVER")
        elif third_choice == "blue" or third_choice == "Blue":
            print("You take a step in and fall into the pirana infested waters. GAME OVER")
        elif third_choice == "yellow" or third_choice == "Yellow":
            print("The room is filled with imaculate treasure! YOU WIN")
        else:
            print("That is not a choice. Since you can't follow directions, GAME OVER")
    elif second_choice == "swim" or second_choice == "Swim":
        print("You quickly find that you are not alone in these waters.")
        print("You are eaten away painfully by all the fishys in the lake and die a horrible death. GAME OVER")
    else:
        print("You can't follow directions since it CLEARLY says swim or wait. GAME OVER")
elif first_choice == "right" or first_choice == "Right":
    print("You fall into a hole and die. GAME OVER.")
else:
    print("I know it's a choose your own adventure but there's only two choices here, left or right. GAME OVER")