
user_input = input("Enter a string: ")
middle_string = ""
for i in range(1, len(user_input) - 1):
    middle_string += user_input[i]
print("The string with its first and last characters removed is:", middle_string)
