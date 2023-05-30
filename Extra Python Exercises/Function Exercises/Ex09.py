def find_primes(check_prime):
    if check_prime > 1:
        if check_prime % 2 != 0:
            return check_prime
        else:
            return "That was not a prime number"
    else:
        return "That was not a prime number"


given_number_for_check = input('Give number to check if prime: ')

try:
    given_number_for_check = float(given_number_for_check)
    print("Prime number : ", find_primes(given_number_for_check))
except ValueError as valErr:
    print("Not a number :", valErr)