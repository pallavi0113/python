# Prompt the user to enter a word and a letter
word = input("Enter a word: ")
letter = input("Enter the letter to split at: ")

# Split and print the result
found = False
for i in range(len(word)):
    if word[i] == letter:
        found = True
        print(word[:i + 1])  # Up to the letter (inclusive)
        print(word[i + 1:])  # Rest of the word
        break

if not found:
    print(f"The letter '{letter}' is not in the word.")
