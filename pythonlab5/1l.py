
user_input = input("Enter a string: ")
frequency = {}
for char in user_input:
    found = False
    for key in frequency:
        if key == char:
            frequency[key] += 1
            found = True
            break
    if not found:
        frequency[char] = 1
print("The frequency of each character is:")
for key in frequency:
    print(f"{key}: {frequency[key]}")
