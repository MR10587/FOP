all_nuts = int(input("How many nuts squirrel accimulated: "))
little_squirrels = int(input("How many little squirrel: "))

nuts_per_day = (little_squirrels + 1) * 3

days_nuts_last = 0

i = all_nuts

while (i >= nuts_per_day):
    days_nuts_last += 1
    i -= nuts_per_day

print(f"Result: there are enough nuts for {days_nuts_last} days.")

if (days_nuts_last > 92):
    print("Nuts will be enough for the whole winter.")
else: 
    print("Nuts will be not enough for the whole winter.")