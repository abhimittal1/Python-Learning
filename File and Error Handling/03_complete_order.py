class InvalidChaiError(Exception):
    """Custom exception for invalid chai orders."""
    pass

def bill(flavour , cups):
    menu = {"masala": 20, "ginger": 25, "lemon": 15}

    try:
        if flavour not in menu:
            raise InvalidChaiError(f"Invalid chai flavour: {flavour}")
        
        price_per_cup = menu[flavour]
        total_cost = price_per_cup * cups
        return total_cost
    
    except InvalidChaiError as e:
        print(f"InvalidChaiError caught: {e}")

# Testing the function with different scenarios
print(bill("masala", 3))  # Valid order
print(bill("cardamom", 2))  # This will raise an InvalidChaiError
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
process_order("masala", 3)  # Valid order
