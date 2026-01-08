# There is no block scope in Python!

# This is where when there's a variable indented or in a block of code like loops or conditional statements
# this does not count as a fence,has same scope as enclosing function, or if no enclosing function it has global scope

# Example: New enemy can be seen outside of the conditional but won't be able to be seen if it's inside a function
game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]

if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy)