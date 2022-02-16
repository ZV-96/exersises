count = 1
password = "pineapple"
attempt = input("Enter password: ")
while count < 3 and attempt != password:
     attempt = input("Password incorrect, try again!:  ")
     count += 1
if attempt == password:
    print("Access Granted")
else:
    print("too many attempts")
