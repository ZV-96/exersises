amount = int(input("how many numbers to be averaged?: "))
counter = 1
total = 0
while counter != amount + 1:
    number = int(input(f"enter number {counter} "))
    total += number
    counter += 1
print(f"total is {total} ")
print(f"Average is {round(total / amount, 2)} ")

