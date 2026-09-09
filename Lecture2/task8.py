year = int(input("Year you born: "))
month = int(input("Month you born: "))

if (month > 9):
    age = 2026 - year - 1
else:
    age = 2026 - year
    
if month == 1:
    month_name = "January"
elif month == 2:
    month_name = "February"
elif month == 3:
    month_name = "March"
elif month == 4:
    month_name = "April"
elif month == 5:
    month_name = "May"
elif month == 6:
    month_name = "June"
elif month == 7:
    month_name = "July"
elif month == 8:
    month_name = "August"
elif month == 9:
    month_name = "September"
elif month == 10:
    month_name = "October"
elif month == 11:
    month_name = "November"
elif month == 12:
    month_name = "December"
else:
    month_name = "Invalid Month"

print(age, month_name)