weight = int(input("Weight: "))
unit = input("(L)bs or (K)g: ")

if unit.upper() == "L":
    converted = weight * 0.45
    print(f"Your weight in kg is {converted}kg")
else:
    converted = weight / 0.45
    print(f"Your weight in lbs is {converted}lbs")
    