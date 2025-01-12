# Prompt the user to enter a formula
formula = input("Enter a formula: ")

# Count opening and closing parentheses
open_count = 0
close_count = 0
for char in formula:
    if char == "(":
        open_count += 1
    elif char == ")":
        close_count += 1

# Print the result
if open_count == close_count:
    print("The formula has balanced parentheses.")
else:
    print("The formula does not have balanced parentheses.")
