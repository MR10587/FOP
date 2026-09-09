x = int(input("Enter hour: "))
y = int(input("Enter minutes: "))

min = x * 60 + y
sec = x * 3600 + y * 60

print(f"Elapsed minutes: {min}")
print(f"Elapsed seconds: {sec}")