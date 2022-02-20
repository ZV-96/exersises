import random
number = random.randint(1, 101)

count = 1
mode = ""
while mode != "H" and mode != "E":
    mode = input("Enter 'H' for Hard mode or 'E' for Easy mode: ").upper()
    if mode == "H":
        num_guess = 4
    elif mode == "E":
        num_guess = 10
    else:
        print("that anit a option mate")

guess = int(input("Guess number: "))
while guess != number and count < num_guess:
    count += 1
    if guess > number:
        print("To high")
    elif guess < number:
        print("To low")
    guess = int(input("Wrong number, Try again! "))
if guess == number:
    print(f"you got it in {count} guesses")
else:
    print(f"you used all {count} guesses and still couldn't get it, loser :c")
