def getmaximumofthreenums(num1, num2, num3):

    if num1 > num2 and num1 > num3:
        max_number = num1
    elif num2 > num1 and num2 > num3:
        max_number = num2
    else:
        max_number = num3

    return max_number


try:
    print("Give random number1:")
    number1 = float(input())
    print("Give random number2:")
    number2 = float(input())
    print("Give random number2:")
    number3 = float(input())

except:

    print("That was not a number")
    quit()

max_number = getmaximumofthreenums(number1, number2, number3)

print("Max number is:", max_number)