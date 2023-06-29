import random

options = ["rock", "paper", "scissors"]
computer_won = 0
user_won = 0

while True:
    print("Welcome to Rock, Paper, Scissors game !!!")
    user_choice = input("--->Enter the choice:- \n"
                   "--->Rock\Paper\Scissors \n"
                   "--->Press q to quit")
    if user_choice == 'q':
        break
    elif user_choice not in options:
        print("Choose something from options ")
        continue

    computer_choice = random.choice(options)
    user_choice = user_choice.lower()

    if computer_choice == "scissors" and user_choice == "paper":
        print("computer won")
        computer_won += 1
    elif computer_choice == "paper" and user_choice == "rock":
        print("computer won")
        computer_won += 1
    elif computer_choice == "rock" and user_choice == "scissors":
        print("computer won")
        computer_won += 1
    elif computer_choice == "rock" and user_choice == "rock":
        print("It's a draw")
    elif computer_choice == "scissors" and user_choice == "scissors":
        print("It's a draw")
    elif computer_choice == "paper" and user_choice == "paper":
        print("It's a draw")
    else:
        print("You won")
        user_won += 1

print("User won     vs      Computer Won")
print(f"{user_won}                          {computer_won}")
print("\nGoodbye")