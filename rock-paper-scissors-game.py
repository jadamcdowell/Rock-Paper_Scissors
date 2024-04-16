import random

# prompt user for name
name = input("What is your name? ")

# welcome the user to the game
print("Welcome "+name+" to Rock Paper Scissors!")

# declare variables
wins = 0
computer_wins = 0

while True:
    # prompt user to make a selection
    user_input = input("Type Rock, Paper, Scissors or Q to quit: ").lower()

    # if user enters 'q', then exit program
    if user_input == "q":
        break
    if user_input not in ["rock", "paper", "scissors", "q"]:
        # error message for incorrect entry
        print("Sorry, that's not a valid input")

        # continue until correct input is entered
        continue

