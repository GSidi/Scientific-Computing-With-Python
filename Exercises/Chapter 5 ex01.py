userContinue = True
totalSum = 0

while userContinue:

    userInput = input("Enter a number: ")

    if userInput == "done":
        break

    try:
        userInput = float(userInput)
    except:
        print("Invalid input")
        continue

    totalSum = totalSum + float(userInput)
print("Sum is : ", totalSum)
 