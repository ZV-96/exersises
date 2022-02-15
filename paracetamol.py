age = int(input("what is paitents age? "))
if age < 12:
    wegh = int(input("what is childs weight? "))
    dose = wegh * 10
    print("Recommend", dose, "mg paracetamol")
else:
    dose = 1000
    print("Recommend", dose, "mg paracetamol")
