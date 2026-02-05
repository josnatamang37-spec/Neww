cities = []
print("Please enter names of five cities:")
for i in range(5):
    city = input(f"Enter city names {i + 1}:")
    cities.append(city)
    print("\nThe cities you entered are:")
    for city in cities:
        print(city)