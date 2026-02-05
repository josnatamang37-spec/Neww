def gallons_to_liters(gallons):
    return gallons * 3.78541
gallons = float(input("Enter gallons(negative to quit):"))
while gallons >= 0:
    liters = gallons_to_liters(gallons)
    print(f"{liters} liters")
    gallons = float(input("Enter gallons(negative to quit):"))
    print("Done")