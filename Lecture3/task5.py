a = int(input("Enter a: "))
b = int(input("Enter b: "))

tshirt = 0
i = a

while (i <= b):
    if (i % 6 == 0):
        tshirt += 1
    i += 1

print(f"{tshirt} t-shirts needed")