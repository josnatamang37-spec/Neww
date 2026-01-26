attempts = 0

while attempts < 5:
    user = input("Username: ")
    pw = input("Password: ")

    if user == "python" and pw == "rules":
        print("Welcome")
        break
    else:
        attempts += 1
        if attempts < 5:
            print(f"Incorrect. You have {5 - attempts} attempts left.")

if attempts == 5:
    print("Access denied")