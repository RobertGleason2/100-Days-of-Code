from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def askii_art():
    print("""
 _______               ___.                    ________                                          
 \      \  __ __  _____\_ |__   ___________   /  _____/ __ __   ____   ______ ______ ___________ 
 /   |   \|  |  \/     \| __ \_/ __ \_  __ \ /   \  ___|  |  \_/ __ \ /  ___//  ___// __ \_  __ \ 
/    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/ \    \_\  \  |  /\  ___/ \___ \ \___ \\  ___/|  | \/
\____|__  /____/|__|_|  /___  /\___  >__|     \______  /____/  \___  >____  >____  >\___  >__|   
        \/            \/    \/     \/                \/            \/     \/     \/     \/       
          """)

def set_difficulty():
    difficulty = input("Choose a difficulty: Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        attempts = EASY_LEVEL_TURNS
    if difficulty == "hard":
        attempts = HARD_LEVEL_TURNS
    return attempts

def check_number_guess(number, guess):
    """
    Compares target number with user's guess. If number guessed right, ends game.
    """
    playing_game = True
    if number == guess:
        print(f"You win! The answer was {number}.")
        playing_game = False
        return playing_game
    elif number > guess:
        print("Too low. Guess again.")
    elif number < guess:
        print("Too high. Guess again")
    
    return playing_game

def main():
    askii_art()
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")
    number = randint(1,100)
    playing_game = True
    
    attempts = set_difficulty()

    while playing_game:
        if attempts > 0:
            print(f"You have {attempts} attempts remaining to guess the number.")
            guess = int(input("Make a guess: "))
            playing_game = check_number_guess(number, guess)
            attempts -= 1
        else: 
            print("Looks like you're out of guesses, try again.")
            playing_game = False

main()