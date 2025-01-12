# Ask the user for an encrypted string and group size
encrypted = input("Enter an encrypted message to decrypt: ")
group_size = int(input("Enter the group size used for encryption: "))

# Calculate the size of each group
n = len(encrypted)
group_sizes = [n // group_size] * group_size
for i in range(n % group_size):
    group_sizes[i] += 1

# Split the encrypted string into groups
groups = []
start = 0
for size in group_sizes:
    groups.append(encrypted[start:start + size])
    start += size

# Reconstruct the decrypted message
decrypted = ""
for i in range(max(group_sizes)):
    for group in groups:
        if i < len(group):
            decrypted += group[i]

print("Decrypted message:", decrypted)
