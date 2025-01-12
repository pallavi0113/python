# Prompt the user to input a string
string = input("Enter a string: ")

# Triple each letter
for char in string:
    if "A" <= char <= "Z" or "a" <= char <= "z":  # Check for letters
        for _ in range(3):
            print(char, end="")
        print()  # Print on a new line for each letter
