import random

total_points = int(input("How many random points to generate? "))
n = 0
iterator = 0

while iterator < total_points:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x ** 2 + y ** 2 < 1:
        n += 1

    iterator += 1

pi_approx = 4 * n / total_points
print(f"The approximation of pi using {total_points} points is: {pi_approx}")