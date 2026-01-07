import sys
# Rules: 
# The deck is unlimited size
# There are no jokers
# The Jack/Queen/King count as 10
# Ace counts as either 1 or 11
# Cards in the list have equal probability of being drawn 
# Computer is the dealer
# You see your whole hand, one card from computer is shown

import random

def deal_cards(hand, deck, draw_number):
    for i in range(draw_number):
        card = random.choice(deck)
        hand.append(card)

    
def has_blackjack(hand):
    total = sum(hand)
    if total == 21:
        return True
    else:
        return False

def check_ace(hand):
    if 11 in hand and sum(hand) > 21:
        hand[hand.index(11)] = 1

def if_bust(hand):
    if sum(hand) > 21:
        return True

def high_card(user_hand, house_hand):
     if user_hand > house_hand:
          return "User wins!"
     elif house_hand > user_hand:
          return "House Wins!"
     else:
          return "Tied"

def main():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_cards = []
    dealer_cards = []
    lose_condition = False
    user_choice = ""

    game_start_input = input("Do you want to play a game of BlackJack? 'y' or 'n': ").lower()

    if game_start_input == 'y':
    
        first_draw = True

        while lose_condition != True and user_choice != "n":
            print("\n" * 20)
            deal_cards(user_cards, cards, 2 if first_draw else 1) #shorthand if statements, take condition and behind is value if true
            deal_cards(dealer_cards,cards, 2 if first_draw else 1)

            first_draw = False

            check_ace(user_cards)
            check_ace(dealer_cards)

            print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
            print(f"Dealer's first card: {dealer_cards[0]}")
            user_choice = input("Type 'y' to get another card or 'n' to pass: ").lower()

            if_bust(user_cards)
            if_bust(dealer_cards)

            user_hit_blackjack = has_blackjack(user_cards)
            computer_hit_blackjack = has_blackjack(dealer_cards)


        if computer_hit_blackjack == True:
                print("The dealer hit blackjack. Game over!")
                lose_condition == True
        elif user_hit_blackjack == True and computer_hit_blackjack == False:
                print("You win!")
                lose_condition == True
        else:
            print(f"Computer Hand: {dealer_cards}")
            print(f"User Cards: {user_cards}")
            high_card(user_cards, dealer_cards)
            lose_condition == True
    else:
         sys.exit()
main()