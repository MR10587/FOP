# Task 1
# def open_file(filename):
#     with open(filename, "r") as f:
#         data = [int(line) for line in f.read().splitlines()]
#         return data

# def filtering_list(data):
#     max = data[0]
#     for number in data:
#         if number < max:
#             data.remove(max)
#         else:
#             max = number

#     print(data)

# filtering_list(open_file("data.txt"))

# Task 2
# def enter_data(n):
#     return [int(input("Enter number: ")) for element in range(n)]

# def print_array(data):
#     print(data)

# def delete_element(data, index):
#     data.pop(index)

#     return data

# def delete_duplicates(data):
#     i = 0

#     while i < len(data) - 1:
#         if data[i] == data[i + 1]:
#             data = delete_element(data, i + 1)
#         else:
#             i += 1

# data = enter_data(5)
# print_array(data)
# delete_duplicates(data)
# print_array(data)

# Task 3
# def from_file(fv):
#     f = open(fv)
#     num = []
#     lines = f.readlines()
#     for line in lines:
#         number = int(line)
#         num.append(number)
#     f.close()
    
#     unique_num = []
#     for n in num:
#         if len(unique_num) == 0 or unique_num[-1] != n:
#             unique_num.append(n)
            
#     return unique_num

# def where_to_add(arr, x):
#     place = 0 
#     for i in range(len(arr)):
#         if x >= arr[i]:
#             place = i + 1
#     return place

# def add_all(arr, place, x, k):
#     for j in range(k):
#         arr.insert(place, x)
#     return arr

# numb = from_file("data_num.txt")

# print("array B before adding:")
# print(" ".join(map(str, numb))) 

# x = int(input("Enter element to add (x): "))
# k = int(input("Enter how many times (k): "))

# place = where_to_add(numb, x)
# numb = add_all(numb, place, x, k)

# print(f"Array B after adding (k={k}, x={x}):")
# print(" ".join(map(str, numb)))
