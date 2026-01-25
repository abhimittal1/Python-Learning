name = ["Abhishek" , "Aman" , "Sam"  , "Rahul"]
bills = [200,300,400,5000]

for name , amount in zip(name , bills):
    print(f"{name} is paying {amount}")