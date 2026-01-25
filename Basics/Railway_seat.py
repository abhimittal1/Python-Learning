seat_type = input("Enter the seat type you want like (Sleeper / AC / General / Luxury) : ").lower()

match seat_type:
    case "sleeper":
        print("You have selected the sleeper :)")
    case "ac":
        print("You have selected the AC :)")
    case "general":
        print("You have selected the general :)")
    case "luxury":
        print("You have selected the luxury :)")
    case _:
        print("No seat type")


for i in range(1 , 11 , 1):
    print(f"Serving chai to token {i}")