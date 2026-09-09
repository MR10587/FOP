g = int(input("Enter money to return: "))

if (g < 0):
    print("Invalid input")
elif(g == 0):
    print("No money to return")
else:
    number_of_100 = g // 100
    g %= 100

    number_of_50 = g // 50
    g %= 50

    number_of_20 = g // 20
    g %= 20

    number_of_10 = g // 10
    g %= 10

    number_of_5 = g // 5
    g %= 5

    number_of_2 = g // 2
    g %= 2

    number_of_1 = g // 1

    print(f"{number_of_100} 100 euro, {number_of_50} 50 euro, {number_of_20} 20 euro, {number_of_10} 10 euro, {number_of_5} 5 euro, {number_of_2} 2 euro, {number_of_1} 1 euro")
