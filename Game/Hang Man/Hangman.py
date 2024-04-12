import random
from Hangman_art import *
from Hangman_word import *
from replit import clear
                                        
def game():
    print(logo)
    print("Hello, This is a Hangman game")
    private_word = "_"
    display = []
    turn_play = 6
    choosen_word = random.choice(word_list)
    print(choosen_word)
    print(f"You have 6 turn play for Hangman game:")
    word_length = len(choosen_word)
    for _ in range(word_length):
        display += private_word
    print(display)
    while True:
        guess = input("Please, Guess word: ").lower()
        clear()
        for position in range(word_length):
            letter = choosen_word[position]
            if letter == guess:
                display[position] = letter
                print(display)
        if private_word not in display:
            print("You Win")
            break
        if guess not in choosen_word:
            turn_play -= 1
            print(f"{guess} not in word:")
            print(f"You have {turn_play} turn play")
            print(stages[turn_play])
            if turn_play == 0:
                print("You lose")
                break
        else:
            print(f"{guess} in word")
print(game())
