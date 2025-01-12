# Ask the user for an encrypted string
encrypted = input("Enter an encrypted message: ")

# Decrypt the message
length = len(encrypted)
odd = encrypted[:(length + 1) // 2]
even = encrypted[(length + 1) // 2:]

decrypted = ""
for i in range(len(odd)):
    decrypted += odd[i]
    if i < len(even):
        decrypted += even[i]

print("Decrypted message:", decrypted)
