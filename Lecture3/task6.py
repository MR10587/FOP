all_nuts = int(input("How many nuts squirrel accimulated: "))
little_squirrels = int(input("How many little squirrel: "))

daily_nuts_needed = (little_squirrels + 1) * 3
nuts_needed_for_winter = daily_nuts_needed * 92

days_nuts_last = int(all_nuts / daily_nuts_needed)

if (nuts_needed_for_winter < all_nuts):
    print(f"Result: there are enough nuts for {days_nuts_last} days. Nuts will be enough for the whole winter.")
else: 
    print(f"Result: there are enough nuts for {days_nuts_last} days. Nuts will be not enough for the whole winter.")