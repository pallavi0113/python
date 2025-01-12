
user_input = input("Enter a string: ")
first_four = ""
for i in range(4):
    if i < len(user_input):
        first_four += user_input[i]
print("The first four characters of the string are:", first_four)
