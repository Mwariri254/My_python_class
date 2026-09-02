# Simple Calculator Program

# Take input for the first number
num1 = float(input("Enter the first number: "))

# Take input for the operator
operator = input("Enter an operator (+, -, *, /): ")

# Take input for the second number
num2 = float(input("Enter the second number: "))

# Perform the calculation based on the operator
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    # Handle division by zero to avoid a crash
    if num2 == 0:
        result = "Error: Division by zero is not allowed"
    else:
        result = num1 / num2
else:
    # Handle invalid operator input
    result = "Error: Invalid operator"

# Print the final result
print(f"Result: {result}")