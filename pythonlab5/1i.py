
user_input = input("Enter a string: ")
capitalized_string = ""
for char in user_input:
    if 'a' <= char <= 'z':
        capitalized_string += chr(ord(char) - 32)
    else:
        capitalized_string += char
print("The string in all capital letters is:", capitalized_string)
