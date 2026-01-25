daily_sales = [21, 30, 4, 24, 34, 22, 234, 32, 34]

# comprehension means -->  ( expression for loop on iteratables if condition  ) <-- code in one line


# comprehension by the set
total_cups_set = {sales for sales in daily_sales if sales > 30}
print(" by the set : -", total_cups_set)

# for the generator
total_cups = sum(sales for sales in daily_sales if sales > 30)
print(" by the generator :: memory saving : ", total_cups)
