# Derivative program
input_expression = input("Enter the expression (e.g., x3 or x25): ")

if input_expression.startswith("x") and input_expression[1:].isdigit():
    exponent = int(input_expression[1:])
    if exponent == 0:
        print("The derivative is 0")
    else:
        derivative = f"{exponent}x{exponent - 1}" if exponent > 1 else f"{exponent}"
        print("The derivative is:", derivative)
else:
    print("Invalid input. Please enter in the format 'x3' or 'x25'.")
