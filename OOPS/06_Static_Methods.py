"""
Static Methods in Python are methods that belong to a class rather than an instance of the class.
They do not require access to instance (self) or class (cls) variables and can be called on the class itself.

"""

class chaiUtils:

    @staticmethod 
    def clean_ingredients(text):
        return [item.strip().lower() for item in text.split(",")]
    

raw = " Milk, Sugar, Tea Leaves , Ginger , Cardamom "

# directly calling static method using class name without creating an instance / object of the class
cleaned = chaiUtils.clean_ingredients(raw)  # ['milk', 'sugar', 'tea leaves', 'ginger', 'cardamom']

print(cleaned)