# Prompt the user to enter a string
string = input("Enter a string: ")

# Count sentences and lines manually
sentence_count = 0
line_count = 1
for char in string:
    if char == ".":
        sentence_count += 1
    elif char == "\n":
        line_count += 1

# Print the counts
print("Number of sentences:", sentence_count)
print("Number of lines:", line_count)
