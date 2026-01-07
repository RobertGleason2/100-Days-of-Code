
# function to add items to a dictionary
def add_to_dictioanry(key, value, auction_bids):
    auction_bids[key] = value
    return auction_bids

# function to compare the values in the dictionary
def compare_values_in_dict(auction_bids):
    value = 0
    for key in auction_bids:
        if auction_bids[key] > value:
            value = auction_bids[key]
    return key,value

# main function
def main():
    isTrue = True
    auction_bids = {}
    while isTrue:
        name = input("What is you name?: ")
        bid = int(input("What is your bid?: $"))
        auction_bids = add_to_dictioanry(name, bid, auction_bids)
        other_biders = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
        if other_biders == "no":
            isTrue == False
            bidder,highest_bid = compare_values_in_dict(auction_bids)
            print(f"The winner of the auction is {bidder} with ${highest_bid}!")
            break
        elif other_biders == 'yes':
            print("\n" * 100)
        else:
            print("Please pick 'yes' or 'no'!")
main()