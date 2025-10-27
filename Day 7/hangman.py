import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''']
wordlist = ["aardvark", "baboon", "camel"]
blanks =""
lives = 6
chosen_word = random.choice(wordlist)
print(chosen_word)

word_length = len(chosen_word)
for position in range(word_length):
    blanks += "_"
print (blanks)

game_over = False
correct_letters = []

while not game_over:
    print(f"*******************{lives}/6 LIVES LEFT*******************")
    print(stages[lives])
    guess = input(f"Which letter are you going to guess?").lower()
    if guess in correct_letters:
        print(f"You already printed {guess}.")

    display  = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
                

    print(display)

    if guess not in chosen_word:
        print(f"{guess} is not in the word, losing one life")
        lives -= 1
        if lives == 0:
            print("*******************You Lose*******************")
            game_over = True

    if "_" not in display:
        game_over = True
        print("*******************You win*******************")
