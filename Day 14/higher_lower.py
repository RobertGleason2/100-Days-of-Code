import art
import game_data
import random

# TODO: create function for getting the dictionary values to compare
# TODO: Create a function for comparing the values
# TODO: Keep track in a score variable
# TODO: End the game when the user guesses wrong

score = 0

def generate_random_values():
    """Generates a random nuber that's in range of the game data list"""
    value = random.randint(0, len(game_data.data))
    return value

def get_name(number1):
    """Gets the game of the actor from the list"""
    # gets a random number that is in the list for game data

    name = game_data.data[number1]["name"]
    description = game_data.data[number1]["description"]
    country = game_data.data[number1]["country"]
    follower_count = game_data.data[number1]["follower_count"]
    return name, description, country, follower_count
    

def compare_values(user_input, game_list, ):
    """Compares the follower count of the two celebreties"""
    global score
    if user_input == "A":
        if game_list[user_input] > game_list["B"]:
            score += 1
            print(f"You're right! Current Score: {score}")
        else:
            print(f"Sorry that's wrong. Final Score: {score}")
            return False
    elif user_input == "B":
        if game_list[user_input] > game_list["A"]:
            score += 1
            print(f"You're right! Current Score: {score}")
        else:
            print(f"Sorry that's wrong. Final Score: {score}")
            return False
    return True

def main():

    playing_game = True
    game_list = {}
    while playing_game:
        first_number = generate_random_values()
        second_number = generate_random_values()
        first_celeb_name, first_celeb_desc, first_celeb_country, first_follower_count = get_name(first_number)
        second_celeb_name, second_celeb_desc, second_celeb_country, second_follower_count = get_name(second_number)
        
        print(art.logo)
        # Prints the First Celebrety 
        print(f"Compare A: {first_celeb_name}, a {first_celeb_desc}, from {first_celeb_country}")
        print(art.vs)
        # Prints the Second Celebrety
        print(f"Against B: {second_celeb_name}, a {second_celeb_desc}, from {second_celeb_country}")
        # Updates the list with the two celebreties being compared
        game_list.update({"A": first_follower_count})
        game_list.update({"B": second_follower_count})
        user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()
        # Sends the user's choice and dictionary containing two celebs to be compared 
        playing_game = compare_values(user_choice, game_list)
        
main()