talent = float(input("Enter talents: "))
pound = float(input("Enter pounds: "))
lot = float(input("Enter lots: "))
step1 = talent * 20
step2 = step1 + pound
step3 = step2 * 32
step4 = step3 + lot
mass = step4 * 13.3
mass_kg = int(mass // 1000)
mass_gr = mass % 1000
print("The weight in modern units:", mass_kg, f"kilograms and {mass_gr:.2f} grams")