import random 

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''

computer_choice = [rock, paper, scissors]
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for Scissors."))

if player_choice == 0:
    print(rock)
    comp_choice = (random.choice(computer_choice))
    print(comp_choice)
elif player_choice == 1:
    print(paper)
    comp_choice = (random.choice(computer_choice))
    print(comp_choice)
else:
    print(scissors)
    comp_choice = (random.choice(computer_choice))
    print(comp_choice)

if player_choice == 0 and comp_choice == rock:
    print("It's a draw")
elif player_choice == 0 and comp_choice == paper:
    print("You lose")
elif player_choice == 0 and comp_choice == scissors:
    print("You win")
elif player_choice == 1 and comp_choice == rock:
    print("you win")
elif player_choice == 1 and comp_choice == paper:
    print("It's a draw")
elif player_choice == 1 and comp_choice == scissors:
    print("You lose")
elif player_choice == 2 and comp_choice == rock:
    print("You lose")
elif player_choice == 2 and comp_choice == paper:
    print("You win")
elif player_choice == 2 and comp_choice == scissors:
    print("It's a draw")
else:
    print("That is not a valid option")