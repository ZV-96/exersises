price = float(input("whats the price?: "))
type = input("what type of item?:\neg food or electrical etc. ")
if price > 10 and type == "food":
    price = price * 0.64
elif price > 10 and type == "electrical":
    price *= 0.70
elif price > 10:
    price *= 0.80
print(f"the price for your {type} item will be {price}")
