
dollars = float(input("How much was the meal? "))
percent = float(input("What percentage would you like to tip? "))

tip = percent / 100 * dollars

tip_in_dollars = (f"Leave ${tip:.2f}")
print (tip_in_dollars)


