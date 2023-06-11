def perfect_number(inserted_number):
    list_of_numbers_that_divide = list()
    for number_each_iteration in range(1, inserted_number):
        if inserted_number % number_each_iteration == 0:
            list_of_numbers_that_divide.append(number_each_iteration)
            if sum(list_of_numbers_that_divide) == inserted_number:
                return str(inserted_number)+":Is a perfect number"


number = input("Give a number to be checked if it is perfect: ")

try:
    print(perfect_number(int(number)))
except ValueError as valErr:
    print("Not a number: ", valErr)


