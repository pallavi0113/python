# Ask the user for a string
message = input("Enter a message: ")

# Encrypt by grouping in threes
groups = ["", "", ""]
for i in range(len(message)):
    groups[i % 3] += message[i]

encrypted = "".join(groups)
print("Encrypted message:", encrypted)
