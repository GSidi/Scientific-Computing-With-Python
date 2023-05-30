def check_upper_case(sentence):
    upper_case_letters_count = 0
    lower_case_letters_count = 0
    for letter in sentence:
        if letter.isupper():
            upper_case_letters_count += 1
        elif letter.islower():
            lower_case_letters_count += 1

    print("No. of Upper case characters : ", upper_case_letters_count)
    print("No. of Lower case characters : ", lower_case_letters_count)
    return ''


test_string = 'The quick Brow Fox'
print(check_upper_case(test_string))
