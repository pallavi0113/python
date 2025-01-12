# Ask the user for a string and a letter
string = input("Enter a string: ")
letter = input("Enter a letter: ")

# Check if the letter appears in the string
found = False
for char in string:
    if char == letter:
        found = True
        break

if found:
    print(f"The letter '{letter}' appears in the string.")
else:
    print(f"The letter '{letter}' does not appear in the string.")
