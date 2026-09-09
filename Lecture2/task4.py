import math

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

d = b ** 2 - 4 * a * c

if (d > 0):
    x1 = (-b - math.sqrt(d)) / (2 * a)
    x2 = (-b + math.sqrt(d)) / (2 * a)
    print(f"Two solutions: {x1} and {x2}")
elif (d == 0):
    x = -b / (2 * a)
    print(f"One solution: {x}")
else:
    print("No real solutions")