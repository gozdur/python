import random

number = str(random.randint(0, 9))
guess = []
guess_count = 0
user_input = []

while number != guess:
    guess = input("Guess a number between 0-9: ")
    if number < guess and guess != "exit":
        print("Number is to HIGH!")
        guess_count = guess_count + 1
    elif number > guess and guess != "exit":
        print("Number is to LOW!")
        guess_count = guess_count + 1
    elif guess == "exit":
        guess_count = guess_count + 1
        print("You quit")
        print("You have tried " + str(guess_count) + " number of times")
        break
    else:
        guess_count = guess_count + 1
        print("You won!")
        print("You have tried " + str(guess_count) + " number of times")







