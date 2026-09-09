number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))

max = number1

if (max < number2):
    max = number2
    
if (max < number3):
    max = number3

print(max)
