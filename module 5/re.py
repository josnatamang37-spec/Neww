import random

rolls = []

# Phase 1: Collect the "rolls"
print("Press Enter to roll a die, or type 'done' to stop.")
action = input("Ready to roll? ")

while action.lower() != "done":
    result = random.randint(1, 6)
    rolls.append(result)
    print(f"Rolled a {result}!")
    action = input("Roll again? (Enter or 'done'): ")

# Phase 2: Use a for loop to calculate the sum
total_sum = 0
print("\n--- Summary ---")

for r in rolls:
    total_sum += r

print(f"Total dice rolled: {len(rolls)}")
print(f"The total sum is: {total_sum}")