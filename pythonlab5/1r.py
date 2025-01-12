
user_input = input("Enter the string: ")
letters = 0
digits = 0
special_characters = 0
for char in user_input:
    if "A" <= char <= "Z" or "a" <= char <= "z":  
        letters += 1
    elif "0" <= char <= "9":
        digits += 1
    else:
        special_characters += 1
print("Total letters:", letters)
print("Total digits:", digits)
print("Total special characters:", special_characters)
