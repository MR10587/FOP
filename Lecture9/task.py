# TASK 1
# =============================================================================
# import numpy as np
#
# n = int(input("Enter number of elements of list: "))
#
# numbers = [int(input("Enter integer: ")) for i in range(n)]
#
# np_arr = np.array(numbers)
#
# print(np_arr)
# =============================================================================

# TASK 2
# =============================================================================
# import numpy as np
#
# numbers_list = [[3, 6, 9, 12], [15, 18, 21, 24], [27, 30, 33, 36], [39, 42, 45, 48], [51, 54, 57,
# 60], [88, 11, 66, 77]]
#
# np_arr = np.array(numbers_list)[1::2, ::2]
#
# print(np_arr)
# =============================================================================

# TASK 3
# import numpy as np
#
# arr = np.zeros((10, 10))
#
# print(arr)
#
# arr[0, :] = 1
# arr[9, :] = 1
#
# arr[:, 0] = 1
# arr[:, 9] = 1
#
# print(arr)

# TASK 4
# import numpy as np
#
# x = np.array([1, 2, 3])
# y = np.array([4, 5, 6])
#
# answers = np.round(5 * (x - y) + np.sin(x) - 1/2 * np.cos(y), 3)
#
# print(answers)

# TASK 5
# import numpy as np
#
# arr = np.repeat([0, 5, 10], 10)
#
# print(arr)

# TASK 6
# import numpy as np
#
# all_nums = np.arange(30, 71)
# even_nums = np.arange(30, 71, 2)
#
# print(all_nums)
# print(even_nums)

# TASK 7
# import numpy as np
#
# arr = np.arange(10, 22).reshape(3, 4)
#
# print(arr)

# TASK 8
# import numpy as np
#
# arr1 = np.array([0, 10, 20, 40, 60])
# arr2 = np.array([0, 40])
#
# arr3 = []
#
# for element in np.nditer(arr1):
#     if element in arr2:
#         arr3.append(True)
#     else:
#         arr3.append(False)
#
# print(arr3)

# TASK 9
# import numpy as np
#
# arr1 = np.array([0, 10, 20, 40, 60])
# arr2 = np.array([10, 30, 40])
#
# arr3 = np.intersect1d(arr1, arr2)
#
# print(arr3)

# TASK 10
# import numpy as np
#
# arr1 = np.array([10, 10, 20, 20, 30, 30])
#
# print(np.unique(arr1))

# TASK 11
# import numpy as np
#
# arr1 = np.array([[1, 2, 3], [4, 5, 6]])
#
# print(arr1)
#
# extra_column = np.array([[7], [8]])
#
# arr1 = np.concatenate([arr1, extra_column], axis=1)
#
# print(arr1)

# TASK 12
# import numpy as np
#
# arr = np.array([[0, 1, 2, 3, 4, 5, 6, 7, 8,],
# [9, 10, 11, 12, 13, 14, 15, 16, 17],
# [18, 19, 20, 21, 22, 23, 24, 25, 26],
# [27, 28, 29, 30, 31, 32, 33, 34, 35]])
#
# print(np.sum(arr, axis=0))

