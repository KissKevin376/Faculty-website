import random

# Generate a random number between 1 & 10
secret_number = random.randint(1,10)

# Start a game loop 
for attempts in range (3):
    # Prompt the user to guess the number
    user_guess = int(input("Guess the number(1-10) = "))

    # Check if the user's guess is correct
    if user_guess == secret_number:
        print("Congratulation! You guessed the number correctly.")
        break
    else:
        print ("Try again "), 3 - attempts, ("attempts left")

        # If the loop completes without a correct  guess, print the secret number
else:

    print("Oops!, Sorry you've run out of attempts the number was ", secret_number,  "Game Over!")  
