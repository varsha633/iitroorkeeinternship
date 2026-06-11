secret_number = 7
guess = 0

while guess != secret_number:
    guess = int(input("Guess the number (1-10): "))

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Congratulations! You guessed it.")
