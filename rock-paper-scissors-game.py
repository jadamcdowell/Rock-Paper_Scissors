import random

# prompt user for name
name = input("What is your name? ")

# welcome the user to the game
print("Welcome "+name+" to Rock Paper Scissors!")

# declare variables
wins = 0
computer_wins = 0

choices = ["rock", "paper", "scissors"]

while True:
    # prompt user to make a selection
    user_input = input("\nType Rock, Paper, Scissors or Q to quit: ").lower()

    # if user enters 'q', then exit program
    if user_input == "q":
        break
    if user_input not in choices:
        # error message for incorrect entry
        print("Sorry, that's not a valid input")

        # continue until correct input is entered
        continue

    # rock is 1, paper is 2, and scissors is 3
    random_number = random.randint(0, 2)

    # computer pick is based on random number generated from 0 to 2
    computer_choice = choices[random_number]

    # print what the user picked
    print("\nComputer chose " + computer_choice)

    # determine who wins and increment wins
    if user_input == computer_choice:
        print("It's a tie!")
    elif (user_input == "rock" and computer_choice == "scissors") or \
            (user_input == "paper" and computer_choice == "rock") or \
            (user_input == "scissors" and computer_choice == "paper"):
        print("You won!")
        wins += 1
    else:
        print("Sorry, you lost :(")
        computer_wins += 1

# print final scores
print("\n----------------------Results----------------------")
print("You won", wins, "times.")
print("The computer won", computer_wins, "times.")