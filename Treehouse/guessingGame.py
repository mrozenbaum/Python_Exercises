import random

print("I am thinking of a number between 1-100.")
user_number = input("What number am I thinking? ")
checkNumber(user_number)

def checkNumber(user_guess):
  if user_guess < 32:
    second_guess = input("Your guess is too low, guess again. ")
    checkNumber(second_guess)
  if user_guess > 32:
    third_guess = input("Your guess is too low, guess again. ")
    checkNumber(third_guess)
  else:
    print("You got it! Woop Woop!")
