from random import randint
import os

def get_int_input(prompt: str) -> int:
    while True:
        try:
            value = int(input(prompt))
            return value 
        except ValueError:
            os.system("clear")
            print("Invalid input. Please enter a valid integer.")

def check_valid_value(turn: int, min: int, maxi: int) -> int:
    while True:
        try:
            user_choice = int(input("Guess a number: "))
            return user_choice
        except ValueError:
            os.system("clear")
            print("Please enter a valid input.")
            print(f"Turn: {5 - turn}")
            print(f"Minimum: {min}, Maximum: {maxi}")

while True:
    os.system("clear")
    print("Welcome to the number guessing game.")
    print("Please select a range for integer number")

    min= get_int_input("Min: ")
    maxi= get_int_input("Max: ")

    if min > maxi:
        os.system("clear")
        swap = input("Minimum value can't be greater than Maximum value. If you want to swap press 'y' and Enter: ")
        if swap.lower() == "y":
            min, maxi = maxi, min
    
    if min and maxi:
        turn = 0
        os.system("clear")
        print(f"Turn: {5 - turn}")
        print(f"Minimum: {min}, Maximum: {maxi}")

        ran_num = randint(min, maxi)
        user_choice = check_valid_value(0, min, maxi)

        while user_choice != ran_num:
            turn += 1
            os.system("clear")
            print(f"Turn: {5 - turn}.")
            if turn > 4:
                break
            
            if user_choice < ran_num:
                print("Too Low")
            elif user_choice > ran_num:
                print("Too High.")
            user_choice = check_valid_value(5 - turn, min, maxi)

        if turn == 5:
            print(f"Game over\nThe number is {ran_num}")
        else:
            print(f"You found it. The number is {ran_num}")
        
        restart = input("\nYou want to restart the game?[y/n]")
        if restart.lower() == "n":
            break