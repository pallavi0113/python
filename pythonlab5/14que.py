# Prompt for the template string
template = "Tiger is a - animal. It likes to eat -. It lives in -."

# Ask the user for replacements
adj = input("Enter an adjective: ")
food = input("Enter the name of a food item: ")
place = input("Enter the name of a place: ")

# Replace the hyphens with the inputs
result = ""
i = 0
for char in template:
    if char == "-":
        if i == 0:
            result += adj
        elif i == 1:
            result += food
        elif i == 2:
            result += place
        i += 1
    else:
        result += char

# Print the reconstructed string
print("Reconstructed string:", result)
