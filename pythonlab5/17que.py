# Ask the user for a word
word = input("Enter a word: ")

# Generate permutations
def generate_permutations(current, remaining):
    if len(remaining) == 0:
        print(current)
        return
    for i in range(len(remaining)):
        generate_permutations(current + remaining[i], remaining[:i] + remaining[i+1:])

generate_permutations("", word)
