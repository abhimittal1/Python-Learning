def pure_chai(cups):
    return cups * 10


total_cups = 2


# not recommended
def impure_chai(cups):
    global total_cups
    total_cups += cups


# recursive code
def pour_chai(n):
    if n == 0:
        return "All the cups poured"
    print("N : ", n)
    return pour_chai(n - 1)


pour_chai(2)


chai_types = ["light", "kadak", "ginger", "kadak"]

# go to every items on the chai_type and save in the variable chai 
strong_chai = list(filter(lambda chai: chai == "kadak", chai_types)) # one time use function




