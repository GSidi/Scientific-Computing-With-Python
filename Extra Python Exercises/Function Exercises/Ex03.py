def multiplication_of_every_element_in_list(list):
    sum_of_elements = 1
    for element in list:
        sum_of_elements = sum_of_elements * element

    return sum_of_elements


list_for_addition = (8, 2, 3, -1, 7)
print("Total sum of the given list is: ", multiplication_of_every_element_in_list(list_for_addition))
