
secret_word = "apple"


guess = input("Guess the word: ")


while guess != secret_word:
    print("Wrong guess, try again!")
    guess = input("Guess the word: ")


print("Congratulations, you guessed it! ")
