# Ask the user for an encrypted string
encrypted = input("Enter an encrypted message: ")

# Decrypt for groups of 3
n = len(encrypted)
group_sizes = [n // 3, n // 3, n // 3]
for i in range(n % 3):
    group_sizes[i] += 1

groups = [encrypted[:group_sizes[0]], encrypted[group_sizes[0]:group_sizes[0]+group_sizes[1]], encrypted[group_sizes[0]+group_sizes[1]:]]

decrypted = ""
for i in range(len(groups[0])):
    for group in groups:
        if i < len(group):
            decrypted += group[i]

print("Decrypted message:", decrypted)
