a = int(input("Enter number: "))

c = 0

while a != 0:
    c += 1
    a //= 10
    
print(f"The amount of digits: {c}")