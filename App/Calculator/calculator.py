from replit import clear
from calculator_art import *
# Caculator
def add(h1,h2):
    return h1 + h2
def subtract(h1,h2):
    return h1 - h2
def mutiply(h1,h2):
    return h1 * h2
def devide(h1,h2):
    return h1 / h2

opperations = {
    "+" : add,
    "-" : subtract,
    "*" : mutiply,
    "/" : devide
}

def caculator():
    print(logo)
    while True:
        first_number = input("What is first number?: ")
        if first_number.isalpha():
            print("Please, Input a numberI:")
        else:
            for symbol in opperations:
                print(symbol)
            operation_symbol = input("Pick an operation from the line above: ")
            if operation_symbol in opperations:
                second_number = input("What is second number?: ")
                if second_number.isalpha():
                    print("Please, Input a numberI:")
                else:
                    caculator_num = opperations[operation_symbol]
                    first_number = int(first_number)
                    second_number = int(second_number)
                    answer = caculator_num(first_number,second_number)
                    print(f"{first_number} {operation_symbol} {second_number} = {answer}")
                    while True:
                        next_caculator = input(f"Type 'y' to continue calculating with {answer}, or 'n' to start new calculator, and type 'e' to end calculator: ")
                        if next_caculator == 'y':
                            for symbol in opperations:
                                print(symbol)
                            operation_symbol = input("Pick an operation from the line above: ")
                            next_number = input("Input next Number: ")
                            caculator_num = opperations[operation_symbol]
                            answer = int(answer)
                            next_number = int(next_number)
                            next_answer = caculator_num(answer,next_number)
                            print(f"{answer} {operation_symbol} {next_number} = {next_answer}")
                            answer = next_answer
                        elif next_caculator == 'n':
                            clear()
                            caculator()
                        elif next_caculator == 'e':
                            print("Thank you. And see you again")
                            print("Code by Tran Cong Hau")
                            exit()
                        else:
                            print("Try again")
            else:
                print("Please try again:")
