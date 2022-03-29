"""A number-guessing game."""
import random

name = input("Howdy, what's your name? ")
print(name + ", I'm thinking of a number between 1 and 100.")
secret_number = random.randint(1, 100)
guess = None

while secret_number != guess:
    guess = int(input("Try to guess my number: "))
    print("Your guess? " + str(guess))
    if guess > secret_number:
        print("Your guessed number is too high!")
        #guess = int(input("What's your next guess?"))
    if guess < secret_number:
        print("You guessed number is too low! ")
        #guess = int(input("What's your next guess?"))

print("You guessed right!")