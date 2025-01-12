
user_input = input("Enter the string: ")
def find_permutations(s, step, result):
    if step == len(s):
        print("".join(result))
        return
    for i in range(step, len(s)):
        s[step], s[i] = s[i], s[step]
        find_permutations(s, step + 1, result)
        s[step], s[i] = s[i], s[step]
char_list = list(user_input)
find_permutations(char_list, 0, char_list)
