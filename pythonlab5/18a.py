# Ask the user for a string
message = input("Enter a message: ")

# Encrypt using odd and even indices
odd = ""
even = ""
for i in range(len(message)):
    if i % 2 == 0:
        odd += message[i]
    else:
        even += message[i]

encrypted = odd + even
print("Encrypted message:", encrypted)
