import random
from replit import clear
from BlackJack_art import *
# Game Black Jack
cards = {
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
    '10': 10,
    'J' : 10,
    'Q' : 10,
    'K' : 10,
    'A' : 11,
}
black_jack = (
    ['10','A'],
    ['J','A'],
    ['Q','A'],
    ['K','A'],
    ['A','10'],
    ['A','J'],
    ['A','Q'],
    ['A','K'],
    ['A','A']
)
card_values = list(cards.keys())
def blackjack():
    print(logo)
    # Radom card user
    card_user_1 = random.choice(card_values)
    card_user_2 = random.choice(card_values)
    card_user = [card_user_1,card_user_2]
    # Radom card computer
    card_computer_1 = random.choice(card_values)
    card_computer_2 = random.choice(card_values)
    card_computer = [card_computer_1,card_computer_2]

    print("Hello, This is a Black Jack game from Tran Cong Hau")
    print(f"Your cards: {card_user}")
    print(f"Computer first cards {card_computer[0]}")
    card_user_1 = cards[card_user_1]
    card_user_2 = cards[card_user_2]
    card_computer_1 = cards[card_computer_1]
    card_computer_2 = cards[card_computer_2]
    new_card_user = 0
    new_card_computer = 0
    total_user = card_user_1 + card_user_2
    total_computer = card_computer_1 + card_computer_2
    while True:
        if sorted(card_user) in black_jack:
            print("You Black Jack, You Winnnnn!")
            blackjack()
        elif sorted(card_computer) in black_jack:
            print(f"Computer card {card_computer}")
            print("Computer Black Jack, You Loseeeee!")
            blackjack()
        elif sorted(card_user) in black_jack and sorted(card_computer) in black_jack:
            print("Drawwwww!")
            blackjack()
        first_question = input("Type 'y' to get another card,type 'n' to pass: ")
        # Check card
        if first_question.isalpha():
            if first_question == 'y':
                new_card_user = random.choice(card_values)
                card_user.append(new_card_user)
                new_card_user = cards[new_card_user]
                print(f"Your cards: {card_user}")
                if len(card_user) > 3:
                    cards['A'] == 1
                total_user += new_card_user
            elif first_question == 'n':
                if card_computer_1 + card_computer_2 < 15 :
                    new_card_computer = random.choice(card_values)
                    card_computer.append(new_card_computer)
                    new_card_computer = cards[new_card_computer]
                    if len(card_computer) > 3:
                        cards['A'] == 1
                    total_computer = card_computer_1 + card_computer_2 + new_card_computer
                print(f"Your Final Hand: {card_user}, total: {total_user}")
                print(f"Computer Final Hand: {card_computer}, total: {total_computer}")
                if total_user > 21:
                    print("You Loseeeee !")
                elif total_computer > 21:
                    print("You Winnnnn !")
                elif total_user > 21 and total_computer > 21:
                    print("Drawwwww!")
                elif total_user > total_computer:
                    print("You Winnnnn!")
                elif total_user < total_computer:
                    print("You Loseeeee!")
                elif total_user == total_computer:
                    print("Drawwwww!")
                second_question = input("Do you want continue play Black Jack Game by Tran Cong Hau. Type 'y' to start a new game, 'e' to end game: ")
                if second_question.isalpha():
                    if second_question == 'y':
                        clear()
                        blackjack()
                    else:
                        print("Thank you to play game. See you again.")
                        exit()
                else:
                    print("Please input 'y' or 'e' to continue.")
            
            else:
                print("Please, Input 'y' or 'n' to continue.")
        else:
            print("Please, Input 'y' or 'n' to continue.")

        
            