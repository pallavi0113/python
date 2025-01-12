# Ask the user for a string and a letter
string = input("Enter a string: ")
letter = input("Enter a letter: ")

# Count occurrences
count = 0
for char in string:
    if char == letter:
        count += 1

print(f"The letter '{letter}' appears {count} times in the string.")
