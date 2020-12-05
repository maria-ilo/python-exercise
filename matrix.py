row = int(input("Enter the number of rows: "))
column = int(input("Enter the number of columns: "))
matrix = []
print("Enter the entries row direction: ")

# For user input
for i in range(row):  # for loop for row entries
    a = []
    for j in range(column):  # for loop for column entries
        a.append(int(input()))
    matrix.append(a)

# For printing the matrix
for i in range(row):
    for j in range(column):
        print(matrix[i][j], end=" ")
    print()
