# Prompt the user to enter a string
string = input("Enter a string: ")

# Check if the string is a palindrome
is_palindrome = True
length = 0
for char in string:
    length += 1
for i in range(length // 2):
    if string[i] != string[length - i - 1]:
        is_palindrome = False
        break

# Print the result
if is_palindrome:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
