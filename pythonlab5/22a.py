def print_table(data):
    # Calculate column widths
    col_widths = [max(len(item) for item in col) for col in data]
    rows = len(data[0])

    # Print rows with right justification
    for i in range(rows):
        for j in range(len(data)):
            print(data[j][i].rjust(col_widths[j]), end="  ")
        print()

# Sample data
table_data = [
    ['Jasmine', 'Rose', 'Tulip', 'Chrysanthemum'],
    ['Julia', 'Jahanara', 'Manasi', 'Tapasi'],
    ['is akin to', 'resembles', 'reminds me the name of', 'is another name for']
]
print_table(table_data)
