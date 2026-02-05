import random
def roll_dice(sides):
    return random.randint(1, sides)
def main():
    max_number = int(input("How many sides does a die have: "))
    current_roll = 0
    while current_roll != max_number:
        current_roll = roll_dice(max_number)
        print(f"Roll: {current_roll}")

main()