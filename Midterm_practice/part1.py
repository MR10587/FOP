# Task 1
# def read_data(filename):
#     with open(filename, "r") as f:
#         store_title = f.readline().strip()
#         goods = []

#         for line in f:
#             parts = line.strip().split(",")

#             good = {
#                 "name": parts[0],
#                 "purpose": parts[1],
#                 "price": float(parts[2]),
#                 "origin": parts[3],
#                 "stock": int(parts[4])
#             }

#             goods.append(good)

#     return store_title, goods

# def print_data(store_title, goods):
#     print("\n" + store_title)
#     print("-" * 85)

#     print(f"{"Name":<20}{"Purpose":<25}{"Price":>10}  {"Origin":<15}{"Stock":>10}")

#     for good in goods:
#         print(f"{good["name"]:<20}{good["purpose"]:<25}{good["price"]:>10}  {good["origin"]:<15}{good["stock"]:>10}")

# def max_price(goods):
#     return max(goods, key=lambda good: good["price"])

# def create_results(filename, stores):
#     with open(filename, "w", encoding="utf-8") as file:
#         for title, goods in stores:
#             for good in goods:
#                 if (good["country"] == "China"
#                         and good["amount"] > 500):
#                     file.write(
#                         f"{title}: {good['name']}, "
#                         f"{good['purpose']}, "
#                         f"{good['price']:.2f}, "
#                         f"{good['country']}, "
#                         f"{good['amount']}\n"
#                     )

# Task 2
def read_data(filename):
    with open(filename, "r") as f:
        store_title = f.readline().strip()

        products = []

        for line in f:
            parts = line.strip().split(",")

            product = {
                "name": parts[0],
                "category": parts[1],
                "price": float(parts[2]),
                "quantity": int(parts[3])
            }

            products.append(product)

    return store_title, products

def print_data(store_title, products):
    print("\n" + store_title)
    print("-" * 48)

    print(f"{"Name":<20}{"Category":<25}{"Price":>10}  {"Quantity":<10}")

    for product in products:
        print(f"{product["name"]:<20}{product["category"]:<25}{product["price"]:>10}  {product["quantity"]:<10}")

def max_price(products):
    return max(products, key=lambda product: product["price"])

def average_price(products):
    return sum(product["price"] for product in products) / len(products)

def sum_price(products):
    return sum(product["price"] for product in products)

def filtered_products(products):
    filtered_products = []

    for product in products:
        if product["price"] > 30 and product["quantity"] > 10:
            filtered_products.append(product)

    return filtered_products

def write_to_file(filename, products):
    with open(filename, "w") as f:
        products = filtered_products(products)

        for product in products:
            f.write(f"{product["name"]}{product["category"]:>15}{product["price"]:>10}  {product["quantity"]:<10}")

def main():
    store_title, products = read_data("products.txt")
    print_data(store_title, products)
    print(max_price(products))
    print(average_price(products))
    print(sum_price(products))
    write_to_file("filtered.txt", products)

main()