matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

total = 0
for row in range(len(matrix)):
    for column in range(len(matrix[row])):
        total += matrix[row][column]

print(total)