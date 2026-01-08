enemies = 1

# Global Constants: Variables that are defined in the global scope that you plan to never change again
# Naming convention is to name it in all uppercase
PI = 3.14159
GOOGLE_URL = "https://google.com"

# if you wanted to access variable outside of functions, you can use the global keyword

def increase_enemies():
    # global enemies
    enemies = 2
    print(f"enemies inside the function {enemies}")

increase_enemies()
print(f"enemies outside the function: {enemies}")

# Global Scope
# object or variable can be seen by everyone
player_health = 10

# Local scope
# variables only called or seen within a function
def drink_potion():
    potion_strength = 2
    print(potion_strength)
    print(player_health)

drink_potion()

# Namespace is the space in which your code is defined and defines what all can see or call your code

