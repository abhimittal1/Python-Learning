"""

Property Decorator in Python allows you to define methods in a class that can be accessed like attributes.
It is commonly used to manage the access to private attributes and implement getter, setter, and deleter functionalities.
defines a method as a property, enabling controlled access to instance variables.
Using @property, you can create managed attributes in your classes.Here's an example to illustrate its usage.

"""

class teaLeave:
    def __init__(self , age):
        self._age = age  # private attribute

    @property
    def age(self):
        return self._age + 2

    @age.setter
    def age(self, age):
        if age > 18:
            self._age = age
        else:
            raise ValueError("Age must be greater than 18")
        
leaf = teaLeave(5) # Normal access to constructor --> not using setter
print(leaf.age)  # Output: 7 (5 + 2 from the getter 

leaf.age = 2 # Using the setter to update age
print(leaf.age)  # Output: ValueError: Age must be greater than 18