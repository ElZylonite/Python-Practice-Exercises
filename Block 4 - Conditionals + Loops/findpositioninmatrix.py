matrix = [
    [4, 8, 15],
    [16, 23, 42],
    [7, 3, 9]
]
number = int(input("Enter a number to search for: "))
found = False

for row in range(len(matrix)):
    for column in range(len(matrix[row])):
        if number == matrix[row][column]:
            found = True
            x_position = row
            y_position = column
            break



if found:
    print(f"{number} found in the matrix.")
    print(f"It is located at row {x_position} and column {y_position}.")
else:
    print(f"{number} not found in the matrix.")