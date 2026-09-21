# Task 1
# print("-----------------------------")
# print("I     x      I     y     I")
# print("-----------------------------")

# for x in range(-10, 11):
#     y = 7 * (x ** 2) + 5 * x - 3
#     print("I%7d     I   %7.2f    I" %(x, y))
# print("------------------------------")

# Task 2
# n = int(input("Number of laps: "))
# m = int(input("Length of one lap: "))
# t = 0

# for i in range(n):
#     tt = int(input(f"Enter time spent for {i + 1} lap: "))
#     t += tt

# average_speed = float(m * n / t)

# print(f"The athlete's average speed v = {average_speed:.1f} m/s, the distance was covered in {t} seconds")

# Task 3
# n = int(input("Number of stages: "))
# k = int(input("Number of targets: "))
# b = int(input("Enter penalty minutes for each shot: "))

# t = 0

# for i in range(n):
#     tt = int(input("Minutes to complete stage: "))
#     kk = int(input("Number of targets hitted: "))
#     added_penalty = (k - kk) * b
#     t += tt + added_penalty
    
# print(f"The athlete completed track in {t} minutes")

# Task 4
# b = int(input("Strawberries ripened in first day: "))
# d = int(input("Number of more strawberries each subsequest day: "))
# n = int(input("Enter day count to calculate strawberry count: "))

# strawberry_count = 0

# for day in range(n):
#     strawberry_count += b + d * day

# print(f"{strawberry_count} strawberries rippened in {n} days")

# Task 5
# p1 = int(input("Enter initial price: "))
# n = int(input("Number of participants: "))

# p2 = p1

# for i in range(n):
#     d1 = int(input("Enter proposed increase in price: "))
#     p2 += d1

# print(f"The final price of the item will be {p2} euros")

# Task 6
# n = int(input("Enter member count: "))

# sum = 0
# first = 2
# second = 3

# for i in range(n):
#     sum += first * second
#     first += 1
#     second += 2
    
# print(sum)

# Task 7
# a = int(input("Current salary: "))
# x = int(input("Monthly increase in salary: "))
# n = int(input("Enter number of months: "))
# b = int(input("Enter minimum salary: "))

# print(f"Salary after a year: {a + 12 * x}")
# print(f"Salary after {n} months: {a + x * n}")

# month_count = 0
# doubled_salary = a * 2
# salary = a

# while salary <= doubled_salary:
#     month_count += 1
#     salary += x
    
# print(f"After {month_count} months, salary surpass its double {doubled_salary} with latest of {salary}")

# months = 0

# while a < b:
#     months += 1
#     a += x

# print(f"After {months} months, salary {a} is at least {b}")

# Task 8
# initial_deposit = int(input("Enter initial deposit: "))
# annual_interest = int(input("Enter annual interest: "))
# m = int(input("Enter years to calculate deposit value: "))

# total_money = initial_deposit

# for i in range(m):
#     added_money = total_money * annual_interest / 100
#     total_money += added_money

# print(total_money)

# Task 9
# whole_grade = 0
# number_of_classes = 0

# while True:
#     grade = int(input("Enter grade: "))
    
#     if grade == 0:
#         break
    
#     whole_grade += grade
#     number_of_classes += 1
    
# average_grade = whole_grade / number_of_classes
# print(average_grade)
