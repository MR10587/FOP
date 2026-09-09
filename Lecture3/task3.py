i = 1
sum = 0

while (1 / i ** 2) > 0.001:
    member = 1 / i ** 2
    sum += member
    print(i)
    i += 1

print(pow(3.14159, 2) / 6 - sum)