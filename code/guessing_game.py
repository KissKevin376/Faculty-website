import random
guess = random.randint(1,10)

i = 0 
for i in range(4):
    guess_number = float(input("Enter a number "))
    if guess == guess_number:
        print("Congratulation, you won ")
        break
    elif guess_number != guess:
        print("Try again ")
    else:
        print("Try again ")
    i = i + 1
    if i == 4:
        print("Game over ")
        print("The number is " ,guess)

