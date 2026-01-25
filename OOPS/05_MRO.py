"""
Demonstration of Method Resolution Order (MRO) in Python with multiple inheritance.
means to show how Python determines which method to call when there are multiple
methods with the same name in the inheritance hierarchy.

"""

class A:
    def show(self):
        print("A")

class B:
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C): # MRO: D -> B -> C -> A --> order in which the Classes are passed
    pass        

d = D()
d.show()  # Output will be "B" due to MRO (Method Resolution Order
