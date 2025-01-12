# Multiplication insertion program
expression = input("Enter an algebraic expression: ")

result = ""
for i in range(len(expression) - 1):
    result += expression[i]
    # Add '*' between digit and letter or ')' and '('
    if (expression[i].isdigit() and expression[i + 1].isalpha()) or (expression[i] == ')' and expression[i + 1] == '('):
        result += '*'
result += expression[-1]

print("Expression with multiplication:", result)
