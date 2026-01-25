"""
Class Methods in Python demonstrate how methods are defined within a class and how they can interact with class-level data.
They take 'cls' as the first parameter, which refers to the class itself rather than an instance of the class.

"""


class chai:
    def __init__(self, tea_type, sugar_level):
        self.tea_type = tea_type
        self.sugar_level = sugar_level

    #user can give you input in any case format and you want to standardize it --> like list , dict etc
    @classmethod
    def from_dict(cls , order_data):
        return cls(
            order_data["tea_type"],
            order_data["sugar_level"]
        )   

    @classmethod
    def from_string(cls , order_str):
        tea_type, sugar_level = order_str.split("-")
        return cls(tea_type, sugar_level)


order1 = chai.from_dict({"tea_type": "Masala Chai", "sugar_level": "Medium"})
order2 = chai.from_string("Ginge-High")

print(order1.__dict__)
print(order2.__dict__)








