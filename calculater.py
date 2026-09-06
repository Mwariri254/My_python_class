# Simple Calculator Program

#input for the first number
number1 = float(input("Enter the first number: "))

#input for the operator
operator = input("Enter an operator (+, -, *, /): ")

#input for the second number
number2 = float(input("Enter the second number: "))

# Perform the calculation based on the operator input by the user
if operator == '+':
    result = number1 + number2
elif operator == '-':
    result = number1 - number2
elif operator == '*':
    result = number1 * number2
elif operator == '/':
    # Handle division by zero 
    if number2 == 0:
        result = "Error: Division by zero is not allowed"
    else:
        result = number1 / number2
else:
    # Handle invalid operator inputs
    result = "Error: Invalid operator"

# Print the final result
print(f"Result: {result}")