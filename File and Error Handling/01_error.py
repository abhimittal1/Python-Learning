"""
Typres of Errors in Python: 
1. Syntax Error - Occurs when the code is not written in proper syntax.
2. Name Error - Occurs when a variable is not defined.
3. Index Error - Occurs when trying to access an index that is out of range.
4. Key Error - Occurs when trying to access a key that does not exist in a dictionary.
5. Type Error- Occurs when an operation is performed on incompatible data types.
6. Value Error- Occurs when a function receives an argument of the right type but inappropriate value.

"""


orders = ["masala dosa", "vada", "samosa"]
try:
    print(orders[3])  # This will raise an IndexError because there is no item at index 3
except IndexError as e:
    print(f"IndexError caught: {e}") 
menu = {
    "masala dosa": 50,
    "vada": 20,
    "samosa": 15
}

try:
    print(menu["idli"])  # This will raise a KeyError because "idli" is not a key in the menu dictionary
except KeyError as e:
    print(f"KeyError caught: {e}")    

try:
    total_price = "fifty" + 20  # This will raise a TypeError because you cannot add a string and an integer
    print(total_price)
except TypeError as e:
    print(f"TypeError caught: {e}")

try:
    age = int("twenty")  # This will raise a ValueError because "twenty" cannot be converted to an integer
    print(f"Your age is {age}")
except ValueError as e:
    print(f"ValueError caught: {e}")

try:
    10 / 0  # This will raise a ZeroDivisionError because division by zero is not allowed   
except ZeroDivisionError as e:
    print(f"ZeroDivisionError caught: {e}")
    
# defined
# print("Hello World"  # This will raise a SyntaxError due to missing closing parenthesis
# Uncomment the lines one by one to see the respective errors.
   



