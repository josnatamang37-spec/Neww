SIZE_LIMIT=42
length = float(input("Enter the length of the zander in centimeters: "))
if length >= SIZE_LIMIT:
    print("This zander meets the size limit.")
else:
    difference = SIZE_LIMIT - length
    print("This zander is too small.")
    print(f"It is {difference} centimeters below the size limit ")
