# Prompt the user for the coded string
code = input("Enter the coded string (numbers separated by spaces): ")

# Decipher the string
decoded_message = ""
temp = ""  # To store digits of the current number
for char in code:
    if char == " ":
        if temp:
            num = int(temp) + 5
            if num > 122:  # If exceeds 'z'
                num -= 10
            decoded_message += chr(num)
            temp = ""
        decoded_message += " "  # Add space as is
    else:
        temp += char
        if len(temp) == 3:  # Process numbers in groups of 3 digits
            num = int(temp) + 5
            if num > 122:  # If exceeds 'z'
                num -= 10
            decoded_message += chr(num)
            temp = ""

# Print the final translated code
print("Decoded message:", decoded_message)
