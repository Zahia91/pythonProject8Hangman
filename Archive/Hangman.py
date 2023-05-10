import random
from words import English_words
from Hangman_Graphic import body_parts
name = input("Please enter your name to start the game  : ")
print(f" welcome to Hangman , Good luck! " + name,"\n Directions : you have 10 tries to guess a word correctly  "
        "please use the dashes to help you guess the number of letters in the correct word  ")
print(body_parts[0])

# keep track of user input used letters
# anytime the user enters wrong letter , show part of the hangman body
correct_word = random.choice(English_words)
MAX_GUESSES = 10

print(correct_word)
tries = MAX_GUESSES
guesses = []

Hangman_Body = []
while tries > 0:
    guess_is_new_letter = False # this gonna controle the letters that are already in the list , to help check
    while guess_is_new_letter is False:
        guess = input(f"Guess a letter (that you haven't guessed yet) in the word. You have {tries} attempt(s) left: ")
        if guess not in guesses:
            guess_is_new_letter = True # this will break from this loop and it will go down to rest of the program

    guesses.append(guess)

    num_correct = 0
    for i in correct_word:
        if i in guesses:
            print(i, end=" ")
            num_correct = num_correct + 1 # we keep track of the correct letters
        else:
            print("_", end=" ")

    print("")

    # for i in correct_word:
    #     if i not in guesses:
    #         break # try not to use the break keyword

    #if guesses == correct_word:
    if num_correct == len(correct_word):
        print("You won, the word is ", correct_word)
        tries = 0
        # break

    if guess not in correct_word:
        tries = tries - 1
        if tries == 0:
            print("Game over you lose , the word is ", correct_word)

    # 10 - 10 = 0; 10 - 9 = 1
    print(body_parts[MAX_GUESSES - tries])