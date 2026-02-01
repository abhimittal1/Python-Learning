def process_order(item , quantity):
    try:
        price = {"masala": 20}[item]  # This may raise a KeyError
        total = price * quantity    # This may raise a TypeError if quantity is not a number

    except KeyError as ke:
        print(f"KeyError caught: {ke} - Item not found in the menu.")
    except TypeError as te:
        print(f"TypeError caught: {te} - Quantity should be a number.")     


# Testing the function with different scenarios
process_order("idli", 2)  # This will raise a KeyError
process_order("masala", "two")  # This will raise a TypeError