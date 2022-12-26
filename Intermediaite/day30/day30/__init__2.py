
try:
    height = float(input("Height : "))
    weight = int(input("Weight : "))
except ValueError as value_error_msg:
    print(f"{value_error_msg}")
else:
    if height > 3:
        raise ValueError("Human Height should not be over 3 meters.")

    bmi = weight / height ** 2
    print(bmi)


