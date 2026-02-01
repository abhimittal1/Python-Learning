
# Using try...finally to ensure file closure
file = open("order.txt", "w")
try:
    file.write("Chai Order Details\n")
finally:    
    file.close()

# Using with statement for file handling -- preferred way
with open("order_1.txt", "w") as file:
    file.write("Masala Chai - 2 cups\n")
    file.write("Ginger Chai - 1 cup\n")