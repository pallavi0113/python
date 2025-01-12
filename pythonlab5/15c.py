# Ask the user for a string and a letter
string = input("Enter a string: ")
letter = input("Enter a letter: ")

# Find the index
found = False
for i in range(len(string)):
    if string[i] == letter:
        print(f"The first occurrence of '{letter}' is at index {i}.")
        found = True
        break

if not found:
    print(f"The letter '{letter}' is not in the string.")
