
user_input = input("Enter a string: ")
reversed_string = ""
for i in range(len(user_input) - 1, -1, -1):
    reversed_string += user_input[i]
print("The reversed string is:", reversed_string)
