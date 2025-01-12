
user_input = input("Enter the string: ")
urls = []
current_url = ""
is_url = False
for i in range(len(user_input)):
    char = user_input[i]
    if (user_input[i:i+7] == "http://" or user_input[i:i+8] == "https://") and not is_url:
        is_url = True
        current_url += char

    elif is_url:
        if char == " ":  
            urls.append(current_url)
            current_url = ""
            is_url = False
        else:
            current_url += char
if is_url and current_url:
    urls.append(current_url)
print("URLs found in the string are:")
for url in urls:
    print(url)
