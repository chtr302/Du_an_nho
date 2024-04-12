import random
from HigherLower_data import *
from HigherLower_art import *
from replit import clear

# Score
score = 0
def HigherLower():
    print("Hello, This is Higher Lower Game code by Tran Cong Hau.")
    print(logo)
    # User 1
    user_1 = random.choice(data)
    name_1 = user_1['name']
    follower_1 = user_1['follower_count']
    des_1 = user_1['description']
    country_1 = user_1['country']
    # User 2
    user_2 = random.choice(data)
    name_2 = user_2['name']
    follower_2 = user_2['follower_count']
    des_2 = user_2['description']
    country_2 = user_2['country']
    # Check User
    print(f"Compare A: {name_1}, a {des_1}, from {country_1}")
    print(vs)
    print(f"Against B: {name_2}, a {des_2}, from {country_2}")
    while True:
        first_question = input("Who has more Follower? Type 'A' or 'B': ")
        if first_question.isalpha():
            if first_question == 'A':
                if follower_1 > follower_2:
                    global score
                    score += 1
                    print(f"You're right! Current Score: {score}")
                    check_clear = input("Type 'C' to clear and continue game: ")
                    if check_clear == 'C':
                        clear()
                        HigherLower()
                else:
                    print(f"Sorry, that's wrong. Final score: {score}")
                    check_game = input("Type 'N' to start new game or 'E' to end game: ")
                    if check_game == 'N':
                        score = 0
                        clear()
                        HigherLower()
                        score = 0
                    elif check_game == 'E':
                        exit()
            elif first_question == 'B':
                if follower_1 < follower_2:
                    score += 1
                    print(f"You're right! Current Score: {score}")
                    check_clear = input("Type 'C' to clear and continue game: ")
                    if check_clear == 'C':
                        clear()
                        HigherLower()
                else:
                    print(f"Sorry, that's wrong. Final score: {score}")
                    check_game = input("Type 'N' to start new game or 'E' to end game: ")
                    if check_game == 'N':
                        score = 0
                        clear()
                        HigherLower()
                        score = 0
                    elif check_game == 'E':
                        exit()
            else:
                print("Please, Type 'A' or 'B'.")
        else:
            print("Please, Input string.")