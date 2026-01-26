while True:
    inches = float(input("Enter inches (negative value to quit): "))
    if inches < 0:
        print("Negative value entered. Program ending.")
        break
    cm = inches * 2.54
    print(f"{inches} inches is {cm} centimeters.")