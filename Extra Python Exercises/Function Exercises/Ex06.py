def check_in_range(number_from, number_to, number_check):

    if number_from <= number_check <= number_to:
        return "Number in range"
    else:
        return "Number out of range"


number1 = input("Give lower end of range:")
number2 = input("Give upper end of range:")
number3 = input("Give number to be checked if in range:")

try:
    number1 = float(number1)
    number2 = float(number2)
    number3 = float(number3)
    print(check_in_range(number1, number2, number3))
except ValueError as err:
    print("Problem with numbers given:", err)

