x = int(input("Enter x coordinate of dot: "))
y = int(input("Enter y coordinate of dot: "))

if (x > 0 and y > 0):
    print(f"({x}, {y}) First plane part")
elif( x < 0 and y > 0):
    print(f"({x}, {y}) Second plane part")
elif (x < 0 and y < 0):
    print(f"({x}, {y}) Third plane part")
elif (x > 0 and y < 0):
    print(f"({x}, {y}) Fourth plane part")
else:
    print("(0, 0) coordinate plane center")