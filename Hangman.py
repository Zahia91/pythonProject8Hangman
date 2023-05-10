import random
from words import English_words
from Hangman_Graphic import body_parts
name = input("Please enter your name to start the game  : ")
print(f" welcome to Hangman , Good luck! " + name,"\n Directions : you have 10 tries to guess a word correctly  "
        "please use the dashes to help you guess the number of letters in the correct word  ")
print(body_parts[0])
correct_word = random.choice(English_words)

max_guesses = 9
tries = max_guesses
guesses = []


while tries > 0:
    guess_is_new_letter = False
    while guess_is_new_letter is False:
        guess = input(f"Guess a letter (that you haven't guessed yet) in the word. You have {tries} attempt(s) left: ")
        if guess not in guesses:
            guess_is_new_letter = True

    guesses.append(guess)

    num_correct = 0
    for i in correct_word:
        if i in guesses:
            print(i, end=" ")
            num_correct = num_correct + 1 # we keep track of the correct letters
        else:
            print("_", end=" ")


    print("")




    if num_correct == len(correct_word):
        print("You won, the word is ", correct_word)



    if guess not in correct_word:
        tries = tries - 1
        if tries == 0:
            print("Game over you lose , the word is ", correct_word)

    print(body_parts[max_guesses - tries])