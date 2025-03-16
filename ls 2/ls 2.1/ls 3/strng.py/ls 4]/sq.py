import math
try:
    number = float(input("Enter a non-negative number: "))
    if number >= 0:
        square_root = math.sqrt(number)
        print(f"The square root of {number} is {square_root:.2f}")
    else:
        print("Error: Please enter a non-negative number.")
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")