GST = 0.15
item = float(input("enter item price: "))
item_GST = item * GST
total_cost = item + item_GST
print("total cost: $", total_cost)
print("-----------------------------")

meters = int(input("enter an number of meters for converstion "))
print(meters, "meters is:")
print(meters * 1000, "milimeters")
print(meters * 100, "centimeters")
print(meters / 1000, "kilometeres")
print(meters * 39.3701, "inchs")
print(meters * 3.28, "feet")
print(meters * 0.0006, "miles")
print(meters * 1.093613888889, "yards")

