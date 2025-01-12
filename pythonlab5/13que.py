# Prompt the user to enter two strings
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

# Check length and concatenate alternately
if len(str1) != len(str2):
    print("The strings are not of the same length.")
else:
    result = ""
    for i in range(len(str1)):
        result += str1[i] + str2[i]
    print("Resulting string:", result)
