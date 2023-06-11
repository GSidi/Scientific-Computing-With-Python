def check_palindrome(inserted_string):
    if inserted_string == inserted_string[::-1]:
        return "Given string is palindrome"
    else:
        return "Given string is not palindrome"


string_to_be_checked = input("Give a string to be checked for palindrome: ")
try:
    string_to_be_checked = string_to_be_checked.replace(" ","")
    print(check_palindrome(string_to_be_checked))
except ValueError as valErr:
    print("Not a string:", valErr)
