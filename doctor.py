age = int(input("please enter age : "))
temp = float(input("please enter temp : "))

if age < 2 and temp >= 38:
        print("CALL DOCTOR")
elif temp >39.5:
    print("high fever")
else:
    print("your fine")
