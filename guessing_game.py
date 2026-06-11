# Exercise 6 - Guessing Game
from random import randint

# Write a program that:
# runs until the user guesses a number (hint: while loop)
# generates a random number between 1 and 9 (including 1 and 9)
# asks the user to guess the number
# then prints a message to the user, whether they guessed too low, too high
# if the user guesses the number right, print out YOU WON! and exit the program
# Hint: Use the built-in random module to generate random numbers https://docs.python.org/3/library/random.html
def guessing_game():
    while True:
        random_int = randint(1, 9)

        user_input = input("Guess the number between 1 and 9: ")
        if not user_input.isdigit():
            print(f"Invalid input. Try again.")
            continue

        user_input = int(user_input)
        if user_input == random_int:
            print("YOU WON!")
            break
        elif user_input > random_int:
            print(f"Your guess is too high. Try again.")
        else:
            print(f"Your guess is too low. Try again.")
