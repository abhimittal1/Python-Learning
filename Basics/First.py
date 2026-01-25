customer_order = input("Enter your order please : ")
order_we_have = ["Samosa" , "Cookies"]

if(customer_order in order_we_have):
    print(f"Your order is confirm :), We are cooking your {customer_order} ")
else:
    print("You can only order the Samosa and Cookies :) ")
    print("1 for Samosa")
    print("2 for Cookies")
    customer_input_number = int(input("Enter the order you want : "))
    if(customer_input_number == 1):
        print(f"Your order is confirm :), We are cooking your Samosa ")
    elif(customer_input_number == 2):
        print(f"Your order is confirm :), We are cooking your Cookies ")
    else:
        print("Wrong Input again sorry :(")    

 