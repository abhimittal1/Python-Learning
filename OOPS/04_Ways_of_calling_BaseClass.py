class Chai:
    type_chai = None
    sugar_level = None

    def __init__(self, type_chai, sugar_level):
        self.type_chai = type_chai
        self.sugar_level = sugar_level

"""

3 ways to call the base class:
    1. Code Duplication: Directly calling the base class method using the class name.

    Important/ used most of the time  >>>
    2. Using super(): Calling the base class method using the super() function, which returns a temporary object of the superclass.

    3. Explicit call: Directly calling the base class method using the base class name and passing the derived class instance as an argument.

"""
# 1. Code Duplication
class SpecialChaiDup(Chai):
    special_ingredient = None

    def __init__(self, type_chai, sugar_level, special_ingredient):
        self.type_chai = type_chai
        self.sugar_level = sugar_level
        self.special_ingredient = special_ingredient

# 2. Explicit Call

class SpecialChaiExp(Chai):
    special_ingredient = None

    def __init__(self, type_chai, sugar_level, special_ingredient):
        Chai.__init__(self, type_chai, sugar_level)
        self.special_ingredient = special_ingredient  # Explicitly calling base class constructor

# 3. Super() method is used to call the base class constructor and methods.
class SpecialChaiOrder(Chai):
    special_ingredient = None

    def __init__(self, type_chai, sugar_level, special_ingredient):
        super().__init__(type_chai, sugar_level)
        self.special_ingredient = special_ingredient

    def order_summary(self):
        return (f"Special Chai Order: {self.type_chai} chai with "
                f"{self.sugar_level} sugar and special ingredient: {self.special_ingredient}.")

order1 = SpecialChaiOrder("Masala", "Medium", "Cardamom")
print(order1.order_summary())