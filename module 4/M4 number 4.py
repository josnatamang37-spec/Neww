import random

target = random.randint(1, 10)
guess = None

print("I'm thinking of a number between 1 and 10.")

while guess != target:
    guess = int(input("Your guess: "))
    if guess < target:
        print("Too low")
    elif guess > target:
        print("Too high")
    else:
        print("Correct!")