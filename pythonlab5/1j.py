
user_input = input("Enter a string: ")
replaced_string = ""
for char in user_input:
    if char == 'i':
        replaced_string += 'I'
    else:
        replaced_string += char
print("The string with every 'i' replaced with 'I' is:", replaced_string)
