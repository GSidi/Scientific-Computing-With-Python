import random
test_dictionary = dict()

for number in range(0, 10):
    test_dictionary[number] = number

random_list = list(test_dictionary.items())
random.shuffle(random_list)
test_dictionary_shuffled = dict(random_list)
print("test_dictionary_shuffled: ", test_dictionary_shuffled)
random_list_sorted = list(test_dictionary_shuffled.values())
random_list_sorted.sort()
test_dictionary_shorted_asc = {i: test_dictionary[i] for i in random_list_sorted}
print("test_dictionary_shorted asc:", test_dictionary_shorted_asc)
random_list_sorted.reverse()
test_dictionary_shorted_desc = {i: test_dictionary[i] for i in random_list_sorted}
print("test_dictionary_shorted desc:", test_dictionary_shorted_desc)

