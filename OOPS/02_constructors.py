class chaiOrder:
    tea_type = None
    sugar_level = None
    milk_type = None


    def __init__(self, tea_type, sugar_level, milk_type):
        self.tea_type = tea_type
        self.sugar_level = sugar_level
        self.milk_type = milk_type

    def summary(self):
        return f"Chai Order: {self.tea_type} tea with {self.sugar_level} sugar and {self.milk_type} milk."
    


order1 = chaiOrder("Masala", "Medium", "Whole")
print(order1.summary())

order2 = chaiOrder("Ginger", "Low", "Almond")
print(order2.summary())