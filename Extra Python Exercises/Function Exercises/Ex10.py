def find_even_number(list_of_numbers):
    new_list = list()
    for number in list_of_numbers:
        if number % 2 == 0:
            new_list.append(number)
    return new_list


given_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(find_even_number(given_list))

