"""Inheritance in Python OOPS concept :
Inheritance is a mechanism where a new class (derived class) inherits attributes and methods from an existing class (base class). This allows for code reusability and the creation of hierarchical relationships between classes.

Three types of inheritance:
1. Single Inheritance: A derived class inherits from a single base class.
2. Multiple Inheritance: A derived class inherits from more than one base class.
3. Multilevel Inheritance: A derived class inherits from a base class, which itself is derived from another base class.

Three types of inheritance relationships:
1. "is-a" relationship: This indicates that one class is a specialized version of another class. For example, a "Dog" class can inherit from an "Animal" class because a dog is a type of animal.
2. "has-a" relationship: This indicates that one class contains or is composed of another class. For example, a "Car" class can have an "Engine" class as an attribute because a car has an engine.
3. "uses-a" relationship: This indicates that one class uses the functionality of another class without inheriting from it. For example, a "Driver" class may use a "Car" class to drive, but the driver is not a type of car.






"""


class BaseChai:

    def __init__(self, chai_type):
        self.tea_type = chai_type

    def preperation(self):
        print(f"Preparing a cup of {self.tea_type} chai ....")


class SpecialChai(BaseChai):

    def __init__(self, chai_type, special_ingredient):
        super().__init__(chai_type)
        self.special_ingredient = special_ingredient

    def preperation(self):
        super().preperation()
        print(f"Adding special ingredient: {self.special_ingredient}.")


class chaiShop:

    chai_class = BaseChai

    def __init__(self):
        self.chai = self.chai_class("Regular")
