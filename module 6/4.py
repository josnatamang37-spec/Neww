def calculate_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total
def main():
    my_list = [10, 20, 30, 40, 50]
    result = calculate_sum(my_list)
    print(f"The sum is: {result}")
main()