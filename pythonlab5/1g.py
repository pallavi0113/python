
user_input = input("Enter a string: ")
if len(user_input) >= 9:
    ninth_character = user_input[8]  
    print("The ninth character of the string is:", ninth_character)
else:
    print("The string is too short to have a ninth character.")
