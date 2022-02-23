def calculate_double(amount):
    double = amount * 2
    return double


# Main Rutine
question = int(input("how much? :"))
answer = calculate_double(question)
print(f"Double {question} is {answer}")
