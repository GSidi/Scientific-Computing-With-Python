def calc_factorial_number(number_to_calc):
    factorial_number = 1
    factorial_result = 1
    while factorial_number <= number_to_calc:
        factorial_result *= factorial_number
        factorial_number += 1

    return factorial_result


user_choice = input("Enter a number you want the factorial of: ")
try:
    user_choice = float(user_choice)
    fact_res = calc_factorial_number(user_choice)
    print("The factorial of:", user_choice, " is:", fact_res)
except ValueError as err:
    print("Value not a number: ", err)


