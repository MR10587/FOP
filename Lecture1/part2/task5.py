k = int(input("Number of ships: "))
n = int(input("Number of bags: "))
m = int(input("Number of ships sank: "))

saved_bags = (k - m) * n

print(saved_bags)