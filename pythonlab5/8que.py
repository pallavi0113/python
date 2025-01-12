# Prompt for the number of email addresses
n = int(input("Enter the number of email addresses: "))

# Initialize counters
student_count = 0
professor_count = 0

# Process email addresses
for _ in range(n):
    email = input("Enter email address: ")
    if "@student.tiu.edu" in email:
        student_count += 1
    elif "@prof.tiu.edu" in email:
        professor_count += 1

# Print the results
print(f"Student emails: {student_count}")
print(f"Professor emails: {professor_count}")
