
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
least_char = None
least_freq = None
for key in frequency:
    if least_freq is None or frequency[key] < least_freq:
        least_char = key
        least_freq = frequency[key]
print("The least frequent character is:", least_char)
