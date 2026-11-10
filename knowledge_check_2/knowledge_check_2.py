# TASK 1
# def read_file(filename):
#     data = []
#
#     with open(filename, "r") as f:
#         for line in f:
#             data.append(line.strip().split(", "))
#
#     return data
#
# def filter_data(data):
#     filtered_data = [scientist for scientist in data if scientist[3][1:3] == "89" and scientist[2] == "physics"]
#
#     return filtered_data
#
# def print_data(data, filename):
#     with open(filename, "w") as f:
#         f.write(f"{"Surname":<13}   {"N.":<2} {'Science'}\n")
#
#         for scientist in data:
#             f.write(f"{scientist[0]:<13}   {scientist[1][0]:.<2} {scientist[2]}\n")
#
# def main():
#     scientists = read_file("science.txt")
#     filtered_scientists = filter_data(scientists)
#     print_data(filtered_scientists, "PH_scientists.txt")
#
# main()

# TASK 2
# numbers = [1, -2, -5, 6, -15, 17, 10]
#
# def sum_of_negatives_divisible_by_5(numbers):
#     return sum([number for number in numbers if number < 0 and number % 5 == 0])
#
# def main():
#     print(sum_of_negatives_divisible_by_5(numbers))

# TASK 3
# def read_file(filename):
#     shops_data = []
#
#     with open(filename, "r") as f:
#         for line in f:
#             shops_data.append(list(map(int, line.strip().split(", "))))
#
#     return shops_data
#
# def make_new_array(data):
#     sum_n = []
#
#     len_shops = len(data)
#     len_products = len(data[0])
#
#     for j in range(len_products):
#         total_sale = 0
#         for i in range(len_shops):
#             total_sale += data[i][j]
#
#         sum_n.append(total_sale)
#
#     return sum_n
#
# def bestseller(sum_n):
#     bestseller_index = sum_n.index(max(sum_n)) + 1
#     return f"{bestseller_index} product is the bestseller"
#
# def main():
#     shop = read_file("shop.txt")
#     sum_of_sales = make_new_array(shop)
#     print(bestseller(sum_of_sales))
#
# main()