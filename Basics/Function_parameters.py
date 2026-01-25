def make_chai(tea , milk , sugar):
    print(f"{tea} , {milk} , {sugar}")

make_chai("Darjeeling" , "Yes" , "Medium")

make_chai(sugar="Low" , tea = "Cutting" , milk= True)


def chai(*important , **not_important):
    print(f" important in chai : " , important) # this is Tuple
    print(f" not_important in chai : " , not_important) # This is Dict

chai("Masala" , "Cutting" , sugar = "Yes" , other = "Ginger" , extra = "cardamon")    