
MENU = {
    "expresso":{
        "ingredients": {
            "water": 50,
            "coffee" : 18,
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients":{
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5, 
    },
    "cappuccino":{
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# When drink is selected, machine should check if there's enough resources for that drink
def check_resources(drink):
    """Checks if there's enough resources to make the drink"""
    # Loops through the specified drink ingredients and returns the items. those items are stored in two temp variables, igredients and required_ammount
    for ingredient, required_ammount in MENU[drink]["ingredients"].items():
        if resources[ingredient] < required_ammount:
            print("Sorry, there's not enough coffee.")
            return False
        return True
    # if drink == "expresso":
    #     if resources["water"] < MENU[drink]["ingredients"]["water"]:
    #         print("Sorry, there's not enough water.")
    #     if resources["coffee"] < MENU[drink]["ingredients"]["coffee"]:
    #         print("Sorry, there's not enough coffee.")
    # else:
    #     if resources["water"] < MENU[drink]["ingredients"]["water"]:
    #         print("Sorry, there's not enough water.")
    #     if resources["milk"] < MENU[drink]["ingredients"]["milk"]:
    #         print("Sorry, there's not enough milk.")
    #     if resources["coffee"] < MENU[drink]["ingredients"]["coffee"]:
    #         print("Sorry, there's not enough coffee.")



# Add various money together for total
def total_money(quarters, dimes, nickels):
    # sum only takes 2 args
    return quarters*.25 + dimes*.10 + nickels*.05

# Check if money given to machine is enough to make the purchase
def enough_money_for_purchace(monies, drink):
    if monies < MENU[drink]["cost"]:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    return True

def user_money_input():
    quarters = input("How many quarters?: ")
    dimes = input("How many dimes?: ")
    nickels = input("How many nickels?: ")
    # need to casat the returns as floats since they get returned as tuples
    return float(quarters), float(dimes), float(nickels)

# proceed with the order/ remove recources and give change
def proceed_with_order(drink, inputed_monies):
    change = 0
    cost = MENU[drink]["cost"]
    if inputed_monies > cost:
        change = inputed_monies - cost
    if drink == "expresso":
        resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
        resources["water"] -= MENU[drink]["ingredients"]["water"]
    else:
        resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
        resources["water"] -= MENU[drink]["ingredients"]["water"]
        resources["milk"] -= MENU[drink]["ingredients"]["milk"]
    return change


def main():
    machine_on = True
    money = 0
    while machine_on:
        user_input = input("What would you like? (expresso/latte/cappuccino)").lower()
        if user_input == "off":
            machine_on = False
        elif user_input == "report":
            print(resources)
            print(f"Money: ${money}")
        else:
            if check_resources(user_input):
                quarters, dimes, nickels = user_money_input()
                total = total_money(quarters, dimes, nickels)
                # checks if the money entered is enough for the drink
                enough_moneies = enough_money_for_purchace(total, user_input)

                if enough_moneies:
                    change = proceed_with_order(user_input, total)
                    # float 2 decimal places
                    print(f"Here is your change :) ${change:0.2f}")
                    print(f"Here is your {user_input}. Enjoy!")

main()