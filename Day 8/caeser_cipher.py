
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

#TODO-1 Create a function called 'encrypt()' that takes 'original_text' and shift_amount as 2 inputs

def caesar(original_text, shift_amount, direction):
    if direction == "encode":
        cipher_text = ""
        #TODO-4 What happens if you try to shift z forward by 9? Can you fix the code?
        #loop through the original text
        for character in original_text:
            if character not in alphabet:
                cipher_text += character
            else:
                #get the index of the current letter we are at in the loop and add it by the shift number
                shifted_position = alphabet.index(character) + shift_amount
                #can take the modulo of the shifted poition to get the right index for the letter in the list. 
                cipher_text += alphabet[shifted_position%len(alphabet)]
        print(f"Here is the encoded result {cipher_text}")
    elif direction == "decode":
        plain_text = ""
        for character in original_text:
            if character not in alphabet:
                cipher_text += character
            else:
                shifted_position = alphabet.index(character) - shift_amount
                plain_text += alphabet[shifted_position%len(alphabet)]
        print(f"Here is the decrypted result {plain_text}")



#TODO-2 Inside the 'encrypt' function, shift each letter of the original_text forwards in the alphabet by the shift_amount and print the encrypted text.You can use the built in Python function index() to find out the posistion of an item in a list.
should_continue = True
while(should_continue):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    original_text = input("Type the text you want to shift.\n").lower()
    shift_amount = int(input("Type the amount you want to shift the text by.\n"))
    caesar(original_text, shift_amount, direction)
    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye")