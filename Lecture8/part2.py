# TASK 1
# import math

# matrix = []
# multiplications = []
# sums = []

# with open("matrix1.txt", "r") as f:
#     for line in f:
#         matrix.append(list(map(int, line.split())))

# for i, row in enumerate(matrix):
#     if (i + 1) % 2 == 0:
#         sums.append(sum(row))
#     else:
#         multiplications.append(math.prod(row))

# print(matrix)
# print(multiplications)
# print(sums)

# TASK 2
# matrix = []

# with open("matrix2.txt", "r") as f:
#     for line in f:
#         matrix.append(list(map(int, line.split())))

# print(matrix)        

# matrix_transpose = [[], [], [], []]

# for row in matrix:
#     matrix_transpose[0].append(row[0])
#     matrix_transpose[1].append(row[1])
#     matrix_transpose[2].append(row[2])
#     matrix_transpose[3].append(row[3])

# print(matrix_transpose)

# first_column_sum_new_matrix = sum(matrix[0])
# first_column_sum_former_matrix = sum(matrix_transpose[0])

# print(f"Sum of columns of first matrix: {first_column_sum_former_matrix}, Sum of columns of second matrix: {first_column_sum_new_matrix}")

# if first_column_sum_former_matrix > first_column_sum_new_matrix:
#     print("First is bigger")
# elif first_column_sum_new_matrix > first_column_sum_former_matrix:
#     print("Second is bigger")
# else:
#     print("They are equal")

