def make_sentences(data):
    # Combine corresponding words from lists
    sentences = []
    for i in range(len(data[0])):
        sentences.append(f"{data[1][i]} {data[2][i]} {data[0][i]}")
    return sentences

# Sample data
table_data = [
    ['Jasmine', 'Rose', 'Tulip', 'Chrysanthemum'],
    ['Julia', 'Jahanara', 'Manasi', 'Tapasi'],
    ['is akin to', 'resembles', 'reminds me the name of', 'is another name for']
]

sentences = make_sentences(table_data)
print("\n".join(sentences))
