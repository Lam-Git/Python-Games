import random


def guess(x):
    #MUST have .randint to generate the random sequence
    random_number = random.randint(1, x)
    guess = 0 #Cannot be number 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}:"))
        if guess < random_number:
            print("Sorry, guess again. Too low.")
        elif guess > random_number:
            print("Sorry, guess again. Too high.")
        
    print(f "Yep, congrats. You have guessed the number {random_number} correctly. ")

#You can make how big the range is for your number game
guess(20)
