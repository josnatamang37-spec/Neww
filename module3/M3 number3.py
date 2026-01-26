gender = input("Enter biological genger(male/female): ")
hemoglobin = float(input("Enter hemoglobin value(g/l): "))
if gender == "male":
    if hemoglobin < 134:
        print("Hemoglobin value is less than 134.")
    elif 134 <= hemoglobin <= 167:
        print("Hemoglobin value is normal")
    else:
        print("Hemoglobin value is high")
elif gender == "female":
            if hemoglobin < 117:
                print("Hemoglobin v is low.")
            elif 117 <= hemoglobin <= 155:
                print("Hemoglobin value is normal.")
            else:
                print("hemoglobin value is high.")
else:
print("Invalid gender entered.")

