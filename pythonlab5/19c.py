# Ask the user for a string and group size
message = input("Enter a message to encrypt: ")
group_size = int(input("Enter the group size for encryption (e.g., 3, 4): "))

# Encrypt by grouping characters
groups = ["" for _ in range(group_size)]
for i in range(len(message)):
    groups[i % group_size] += message[i]

encrypted = "".join(groups)
print("Encrypted message:", encrypted)
