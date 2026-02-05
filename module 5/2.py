numbers = []
user_input = input("Enter a number or press enter to quit:")
while user_input != "":
    number = (int(user_input))
    numbers.append(number)
    user_input = input("Enter a number or press enter to quit:")
    numbers.sort(reverse=True)
    print("\n--The five greatest numbers--")
    top_five = numbers[:5]
    for number in top_five:
        print(number)
