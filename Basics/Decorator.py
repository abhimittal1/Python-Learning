from functools import wraps

def my_decorator(func):

    #this is the wrapper class.. containing the func that is coming from outside and can be replace if not working properly

    @wraps(func) # this is very important to save the function data -- meta data
    def wrapper():
        print("Before the function")
        func()
        print("After the function")
    return wrapper 

# when we write this ... the function written after this will go in the decorator
@my_decorator
def greet():
    print("Hello i am wrapped inside the decorater function")

greet()    

print(greet.__name__)