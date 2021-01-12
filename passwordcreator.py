print("Create a password: ")


# Parameters
minimunlength = 8
numbers = 2
alphanumericchars = 1
uppercasechars = 1
lowercasechars = 1
aprobated = False


def successFunction():
    print("Your password is successfully created!")
    aprobated = True


def printPasswordRequisites():
    print("The password requires:")
    print(minimunlength, "characters minimum")
    print(numbers, "numbers")
    print(alphanumericchars, "alpha numeric characters")
    print(uppercasechars, "uppercase characters")
    print("Please write other password: ")
    

# While the password is not aprobated, ask to the user again
while aprobated == False:

    # USername ask
    password = input()
    
    # Check character per character if the password pass the security test
    uppercaseCount = 0
    lowercaseCount = 0
    numberCount = 0
    alphanumericCount = 0

    for i in range(len(password)):

        # Uppercase check
        if(password[i].isupper()):
            uppercaseCount += 1

        # Lowercase check
        if(password[i].islower):
            lowercaseCount += 1
       
        # Numbers check
        if(password[i].isnumeric()):
            numberCount += 1

        # Aphanumeric check
        if(password[i].isalnum()):
            alphanumericCount += 1
    pass

    # Final check with the requirements
    if(len(password) >= minimunlength and uppercaseCount >= uppercasechars and lowercaseCount >= lowercasechars and numberCount >= numbers and alphanumericCount >= alphanumericchars):
        successFunction()
    else:
        printPasswordRequisites()
        pass

    pass
