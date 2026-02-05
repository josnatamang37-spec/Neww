from random import randint

roll = []
print("Press E to roll a die or type D to stop.")
action = input("Do you want to roll?")
while action != "D":
    result = randint (1,6)
    roll.append(result)
    print(f"Rolled {result}")
    action = input("Roll again? (E or D):")
    total_sum = 0
    print("\n--Summary--")
    for r in roll:
        total_sum += r
        print(f"Rolled: {len(roll)}")
        print(f"Sum: {total_sum}")
