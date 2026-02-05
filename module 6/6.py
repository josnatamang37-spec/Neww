import math
def calculate_unit_price(diameter_cm, price_euros):
    radius_m = (diameter_cm / 2) / 100
    area_m2 = math.pi * (radius_m**2)
    unit_price = price_euros / area_m2
    return unit_price
def main():
    diam1 = float(input("Enter diameter of pizza 1 (cm):"))
    price1 = float(input("Enter price of pizza 1 (euros):"))
    diam2 = float(input("Enter diameter of pizza 2 (cm):"))
    price2 = float(input("Enter price of pizza 2 (euros):"))
    unit_price1 = calculate_unit_price(diam1, price1)
    unit_price2 = calculate_unit_price(diam2, price2)
    print(f"\nPizza 1 unit price: {unit_price1: .2f} euros/m2")
    print(f"Pizza 2 unit rice:{unit_price2: .2f} euros/m2")
    if unit_price1 < unit_price2:
        print("Pizza 1 provides better value for money.")
    elif unit_price2 < unit_price1:
        print("Pizza 2 provides better value for money.")
    else:
        print("Both pizzas have the same price.")
main()