# Ask the user for a large integer
number = input("Enter a large integer: ")

# Insert commas
result = ""
count = 0
for i in range(len(number) - 1, -1, -1):
    result = number[i] + result
    count += 1
    if count == 3 and i != 0:
        result = "," + result
        count = 0

print("Formatted number:", result)
