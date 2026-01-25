users = [
    {"id": 1, "total": 100, "coupon": "P20"},
    {"id": 2, "total": 150, "coupon": "F20"},
    {"id": 3, "total": 200, "coupon": "P50"}
]

discounts = {
    "P20": (0.2, 0),   # 20% discount
    "F20": (0.5, 0),   # 50% discount
    "P50": (0, 10)     # Flat 10 discount
}

for user in users:
    percent, fixed = discounts.get(user["coupon"], (0, 0))
    discount = user["total"] * percent + fixed
    print(
        f"User with id {user['id']} paid {user['total']}"
        f"and will get a discount of {discount}"
    )
