def transpose(matrix):
  transposed_matrix = []
  for i in range(len(matrix[0])):
    transposed_row = []
    for row in matrix:
      transposed_row.append(row[i])
    transposed_matrix.append(transposed_row)
  return transposed_matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed_matrix = transpose(matrix)
print(transposed_matrix)
