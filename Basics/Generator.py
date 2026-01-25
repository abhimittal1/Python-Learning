# Generators in Python are a way to create iterators that produce values one at a time, only when needed, instead of storing everything in memory at once.

# Think of them as a lazy sequence producer.
# Save memory
# when we want the result little late

numbers = [ i for i in range(101)] # use the memory to store the all number
numbers_Generated = sum( i for i in range(101)) # all generate the number one by one

# print(numbers)
# print(numbers_Generated)


def chai_shop():
    yield "cup 1 : masala chai"
    yield "cup 2 : ginger chai"
    yield "cup 3 : lemon chai"

# generator is holding the reference of the object that's we need to store
stall_0 = chai_shop()
for cup in stall_0:
    print(cup)

print(" generator different way to print :- ")
stall = chai_shop()
# can't name the stall as stall_0 because the above varible is named as the stall_0 which is the pointer type as will create problem


# another way
print(next(stall))
print(next(stall))
print(next(stall))

# inifinite generator
def chai_customer():
    print("Welcome! Give your order here : ")
    order = yield
    while True:
        print(f" Making the order : " , order)
        order = yield

stall_1 = chai_customer() # Reference of the function
next(stall_1) #  start of the generator

stall_1.send("Masala")
stall_1.send("Lemon")


# close is important to release the memory
stall_0.close()
stall.close()
stall_1.close()