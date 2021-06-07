from art import logo
from randint import random

def easy_mod():
    attemps = 10
    end_game = False
    while not end_game:
        if attemps == 0:
            end_game = True
            result = print("You are out of guesses. You lose.")
            return result

        print(f"You have {attemps} remaining to guest the number.")
        user_guessing = int(input("Guess number: "))

        if user_guessing < guessing_number:
            print("Too low. Guess again.")
            attemps = attemps - 1
        elif user_guessing > guessing_number:
            print("Too high. Guess again.")
            attemps = attemps - 1
        else:
            result = print(f"Match! The number was {guessing_number}.")
            end_game = True
            return result


def hard_mod():
    attemps = 5
    end_game = False
    while not end_game:
        if attemps == 0:
            end_game = True
            result = print("You are out of guesses. You lose.")
            return result

        print(f"You have {attemps} remaining to guest the number.")
        user_guessing = int(input("Guess number: "))

        if user_guessing < guessing_number:
            print("Too low. Guess again.")
            attemps = attemps - 1
        elif user_guessing > guessing_number:
            print("Too high. Guess again.")
            attemps = attemps - 1
        else:
            result = print(f"Match! The number was {guessing_number}.")
            end_game = True
            return result


print(logo)
print("welcome to th Number Guessing game. I am thinking  of a number between 1 and 100.")
guessing_number = (random.randint(1, 100))
print(f"Psst, the correct answer is {guessing_number}")
difficulty = input("Choose a difficulty. Type ´easy´ or ´hard´: ")

if difficulty == "easy":
    easy_mod()
else:
    hard_mod()


