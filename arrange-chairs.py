# Initial matrix with chairs represented as 1s in a diagonal arrangement
matrix = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]

# Calculate the total number of chairs
num_chairs = sum(sum(row) for row in matrix)

# Create a new matrix with all chairs in the top row
new_matrix = [[1 if j < num_chairs and i == 0 else 0 for j in range(len(matrix[0]))] for i in range(len(matrix))]

print(new_matrix)
