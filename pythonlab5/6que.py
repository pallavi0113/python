# Prompt the user to enter a string
string = input("Enter a string: ")

# Convert to lowercase and remove periods and commas
new_string = ""
for char in string:
    if "A" <= char <= "Z":
        new_string += chr(ord(char) + 32)
    elif char != "." and char != ",":
        new_string += char

# Print the resulting string
print("Resulting string:", new_string)
