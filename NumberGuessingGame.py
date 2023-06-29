import random

print("Welcome to the Number Guessing Game !!!")
top_range = input("Enter the top range upto which you would want to guess ")
if top_range.isdigit():
    top_range = int(top_range)
    if top_range <= 0:
        print("Enter a no. greater than 0")
        quit()
else:
    print("Please enter the digit next time. ")
    quit()

random_int = random.randint(0, top_range)
guess = 0
while True:
    guess += 1
    user_guess = input("Guess the number ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please enter the digit next time. ")
        continue
    if random_int == user_guess:
        print("Correct Choice")
        print(f"You guessed it in {guess} guesses.")
        break
    if user_guess > random_int:
        print("Hint: Your guess is greater than the number. ;) ")
    else:
        print("Hint: Your guess is less than the number")
