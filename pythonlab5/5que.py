# Prompt the user to enter a string
string = input("Enter a string: ")

# Modify the string manually
new_str = ""
for i in range(len(string)):
    if i == 2:
        new_str += "*"
    else:
        new_str += string[i]
new_str += "!!"

# Print the result
print("New string:", new_str)
