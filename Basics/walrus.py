value  = 13

remainder = value % 5
if remainder:
    print(f"Value is not divisible, remainder is {remainder}")

if (remainder := value % 4):
    print(f"Value is not divisible, remainder is {remainder}")

