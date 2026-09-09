number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

if (number1 > 0 and number2 > 0):
    print("Both numbers positive")
elif (number1 < 0 and number2 < 0):
    print("Both numbers negative")
else:
    print("One positive, one negative")