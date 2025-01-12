
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
words1 = []
words2 = []
word = ""
for char in string1:
    if char == " ":
        if word != "":
            words1.append(word)
        word = ""
    else:
        word += char
if word != "":
    words1.append(word)
word = ""
for char in string2:
    if char == " ":
        if word != "":
            words2.append(word)
        word = ""
    else:
        word += char
if word != "":
    words2.append(word)
uncommon = []
for word in words1:
    if word not in words2:
        uncommon.append(word)
for word in words2:
    if word not in words1:
        uncommon.append(word)
print("Uncommon words are:", uncommon)
