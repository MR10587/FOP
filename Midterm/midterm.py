def read_data(filename):
    with open(filename, "r") as f:
        fruits = []

        for line in f:
            parts = line.strip().split(" ")

            fruit = {
                "tree_type": parts[0],
                "tree_name": parts[1],
                "plant_year": int(parts[2]),
                "amount_of_fruit": int(parts[3])
            }

            fruits.append(fruit)

    return fruits

def count_data(fruits):
    number_of_apple_trees = len([fruit for fruit in fruits if fruit["tree_type"] == "apple"])
    total_gathered_fruits = sum([fruit["amount_of_fruit"] for fruit in fruits])

    return number_of_apple_trees, total_gathered_fruits
 
def print_to_file(filename, data1, data2):
    total_gathered_fruits = 0
    more_apple_trees = ""

    number_of_apple_trees1, total_gathered_fruits1 = count_data(data1)
    number_of_apple_trees2, total_gathered_fruits2 = count_data(data2)

    total_gathered_fruits += total_gathered_fruits1 + total_gathered_fruits2

    if number_of_apple_trees1 > number_of_apple_trees2:
        more_apple_trees = "Garden 1"
    else:
        more_apple_trees = "Garden 2"

    with open(filename, "w") as f:
        f.write(f"More apple trees in {more_apple_trees}\n")
        f.write(f"Total gathered fruits: {total_gathered_fruits}")

def main():
    data1 = read_data("garden1.txt")
    data2 = read_data("garden2.txt")

    print_to_file("result.txt", data1, data2)

main()
