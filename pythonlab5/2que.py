
string = input("Enter a string: ")

# Count words manually and store their lengths
word_count = 0
words = []
word = ""
for char in string:
    if char != " ":
        word += char
    else:
        if word != "":
            words.append(word)
            word_count += 1
            word = ""
if word != "":
    words.append(word)
    word_count += 1

# Print the word count and table
print(f"Number of words: {word_count}")
print("Word\tLength")
for word in words:
    length = 0
    for char in word:
        length += 1
    print(f"{word}\t{length}")
