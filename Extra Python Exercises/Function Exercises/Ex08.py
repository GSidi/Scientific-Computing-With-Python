def unique_elements(test_list):
    test_list = set(test_list)
    test_set_to_list = list(test_list)
    return test_set_to_list


list_to_check = [1,2,3,3,3,3,3,4,5,6,7,7,7,7,8,9,9,9,10,10]
list_after_check = unique_elements(list_to_check)
print("List after check: ",list_after_check)


