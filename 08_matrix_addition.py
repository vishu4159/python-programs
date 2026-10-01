# Python program to add two matrices using array and function

def add_matrices(A, B):
    rows = len(A)
    columns = len(A[0])

    result = []

    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(A[i][j] + B[i][j])
        result.append(row)

    return result


A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

result = add_matrices(A, B)

print("Sum of the two matrices:")

for row in result:
    print(row)
