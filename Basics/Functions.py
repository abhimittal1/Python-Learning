def print_order(name , chai_type):
    print(f"{name} ordered the {chai_type} chai")


print_order("Abhishek" , "Masala")
print_order("Atishay" , "tulsi")
print_order("Akash" , "ginger")
print_order(2 , "ginger")

def save_to_db():
    print("Saving to Database")

def users_data():
    print("This is the function Users : calling the DB function :)")
    save_to_db()

users_data()

def calculate_bill(number_of_cups , pre_cup_price):
    return number_of_cups*pre_cup_price

total_price = calculate_bill(23,3)
print(f"Print the total bill is {total_price}")

print(f"total bill is using direct call : {calculate_bill(2,2)}")


if(total := calculate_bill(23,20) >= 123):
    print(f"This is valid :) ")


