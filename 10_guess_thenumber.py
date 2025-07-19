import random

number = random.randint(1, 20)
guess = 0

print("I have chosen a number between 1 and 20. Try to guess it!")

while guess != number:
    guess = int(input("Your guess: "))

    if guess < number:
        print("Try a higher number.")
    elif guess > number:
        print("Try a lower number.")
    else:
        print("Congratulations! You guessed it right 🎉")
