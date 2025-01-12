# Prompt the user to enter a word
word = input("Enter a word: ")

# Capitalize alternate letters
result = ""
for i in range(len(word)):
    if i % 2 == 0:
        result += word[i].lower()
    else:
        result += word[i].upper()

# Print the resulting word
print("Resulting word:", result)
