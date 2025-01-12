
user_input = input("Enter a string: ")
last_two = ""
for i in range(len(user_input) - 2, len(user_input)):
    if i >= 0:
        last_two += user_input[i]
print("The last two characters of the string are:", last_two)
