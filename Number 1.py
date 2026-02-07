seasons = ("winter", "spring", "summer", "autumn")
try:
    month = int(input("Enter the number of the month(1-12): "))
    if month <= 1 or month <= 12:
        index = (month % 12) // 3
        print(f"Month {month} is in {seasons[index]}.")
    else:
        print("Please enter a valid month.")
except Valueerror:
    print("Please enter a valid month.")