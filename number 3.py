airports = {}
while True:
    print("\nAirport data system")
    print("1. Enter a new airport")
    print("2. Fetch airport information")
    print("3. Exit")
    choice = input("Enter your choice(1, 2, or 3): ").strip()
    if choice == "1":
        icao = input("Enter the ICAO: ").strip().upper()
        name = input("Enter the name of the airport: ").strip()
        airports[icao] = name
        print(f"Airport {icao} added successfully.")
    elif choice == "2":
        icao = input("Enter the ICAO code to fetch: ").strip().upper()
        if icao in airports:
            print(f"The name of the airport is {airports[icao]}")
        else:
            print("Airport does not exist.")
    elif choice == "3":
        print("Exit")
        break
    else:
        print("Please enter a valid choice.")