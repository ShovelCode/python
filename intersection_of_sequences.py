def intersection_of_sequences(sequences):
    # Convert the first sequence to a set
    result_set = set(sequences[0])

    # Intersect it with sets of the remaining sequences
    for seq in sequences[1:]:
        result_set = result_set.intersection(seq)

    return result_set

# Example usage
seq1 = [1, 2, 3, 4]
seq2 = [3, 4, 5, 6]
seq3 = [4, 5, 6, 7]

# Find the intersection
intersect = intersection_of_sequences([seq1, seq2, seq3])
print(intersect)
