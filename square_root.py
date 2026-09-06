# Program to calculate the square root of a number

import math  # Import the math library for sqrt()

# Take input from the user and convert it to a float
number = float(input("Enter a number: "))

# Check if the number is negative, since sqrt() can't handle negative values
if number < 0:
    print("Error: Cannot calculate the square root of a negative number")
else:
    # Calculate the square root using math.sqrt()
    square_root = math.sqrt(number)
    print(f"The square root of {number} is {square_root}")