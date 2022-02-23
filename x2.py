def calculate_half(amount):
    half = amount / 2
    return half


def calculate_ten(amount):
    ten_more = amount + 10
    return ten_more


# Main Routine

question = int(input("how much? :"))
answer1 = calculate_half(question)
answer2 = calculate_ten(question)
print(f"half {question} is {answer1}")
print(f"ten more than {question} is {answer2}")
