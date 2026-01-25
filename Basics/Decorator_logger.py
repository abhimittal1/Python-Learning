from functools import wraps

def logger(func):

    @wraps(func)
    def wrapper(*args , **kwags):
        print(f" Stating func {func.__name__} ")
        result = func(*args , **kwags)
        print(f" Ending func {func.__name__} ")
        return result
    return wrapper    


@logger
def chai(type , milk = "NO"):
    print(f"Making {type} chai. milk contains {milk} ")


chai("Masala")   

